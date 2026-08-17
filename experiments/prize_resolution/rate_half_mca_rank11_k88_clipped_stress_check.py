#!/usr/bin/env python3
"""Check a paired K'=88 raw-clipped stress capture."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


UNSAFE_UNITS = {1: 27_562, 22: 15_109, 30: 8_841, 44: 195}


def json_rows(text: str):
    for line in text.splitlines():
        if not line.startswith("{"):
            continue
        try:
            yield json.loads(line)
        except json.JSONDecodeError:
            continue


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("capture", type=Path)
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    raw = args.capture.read_bytes()
    jobs, batch = {}, None
    for row in json_rows(raw.decode(errors="replace")):
        if row.get("event") == "JOB_RESULT":
            assert row["job"] not in jobs
            jobs[row["job"]] = row
        elif row.get("event") in {"BATCH_COMPLETE", "BATCH_INCOMPLETE"}:
            batch = row
    offsets = (44,) if args.smoke else (1, 22, 30, 44)
    assert batch == {
        "completed": 2 * len(offsets),
        "event": "BATCH_COMPLETE",
        "expected": 2 * len(offsets),
        "infrastructure_failures": 0,
        "smoke": args.smoke,
    }
    expected = {
        f"{implementation}:offset{offset}"
        for implementation in ("primary", "audit")
        for offset in offsets
    }
    assert set(jobs) == expected
    results = {"primary": {}, "audit": {}}
    for job, wrapper in jobs.items():
        implementation, lane = job.split(":", 1)
        offset = int(lane.removeprefix("offset"))
        assert wrapper["exit"] == 0 and wrapper["timed_out"] is False
        assert 0 < int(wrapper["peak_mb"]) <= 128
        row = wrapper["result"]
        assert row["event"] in {"FALSIFIED", "SURVIVED"}
        assert row["offset"] == offset
        results[implementation][offset] = row

    compare = (
        "event", "offset", "units_checked", "unsafe_units_checked",
        "profiles_checked", "leader", "complete",
    )
    witness = (
        "m2", "m3", "s2", "s3", "s4", "s5", "m4", "m5", "case",
        "charges", "adjacent_edges", "raw_before", "raw_before_high",
        "clipped_after", "clipped_high", "excess_over_leader",
    )
    falsified = []
    for offset in offsets:
        primary, audit = results["primary"][offset], results["audit"][offset]
        for key in compare:
            assert primary[key] == audit[key], (offset, key)
        if primary["event"] == "FALSIFIED":
            falsified.append(offset)
            for key in witness:
                assert primary[key] == audit[key], (offset, key)
        else:
            assert primary["units_checked"] == (78 - offset) * 6241
            assert primary["unsafe_units_checked"] == UNSAFE_UNITS[offset]
            assert jobs[f"primary:offset{offset}"]["progress_rows"] == 78 - offset
            assert jobs[f"audit:offset{offset}"]["progress_rows"] == 78 - offset
    print(json.dumps({
        "status": "FALSIFIED" if falsified else "PASS",
        "capture_sha256": hashlib.sha256(raw).hexdigest(),
        "jobs": len(jobs),
        "offsets": list(offsets),
        "falsified_offsets": falsified,
        "source_units": sum(
            int(results["primary"][offset]["units_checked"])
            for offset in offsets
        ),
        "unsafe_units": sum(
            int(results["primary"][offset]["unsafe_units_checked"])
            for offset in offsets
        ),
        "profiles_per_implementation": sum(
            int(results["primary"][offset]["profiles_checked"])
            for offset in offsets
        ),
        "peak_mb": max(int(row["peak_mb"]) for row in jobs.values()),
    }, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Merge the paired complete K'=87 raw-clipped residual wave."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def json_rows(text: str):
    for line in text.splitlines():
        if line.startswith("{"):
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("capture", type=Path)
    parser.add_argument("--sha256")
    args = parser.parse_args()
    raw = args.capture.read_bytes()
    capture_sha = hashlib.sha256(raw).hexdigest()
    if args.sha256 is not None:
        assert capture_sha == args.sha256
    jobs, batch = {}, None
    for row in json_rows(raw.decode(errors="replace")):
        if row.get("event") == "JOB_RESULT":
            assert row["job"] not in jobs
            jobs[row["job"]] = row
        elif row.get("event") in {"BATCH_COMPLETE", "BATCH_INCOMPLETE"}:
            batch = row
    assert batch == {
        "completed": 86,
        "event": "BATCH_COMPLETE",
        "expected": 86,
        "infrastructure_failures": 0,
    }
    expected = {
        f"{implementation}:offset{offset}"
        for implementation in ("primary", "audit")
        for offset in range(1, 44)
    }
    assert set(jobs) == expected
    results = {"primary": {}, "audit": {}}
    for job, wrapper in jobs.items():
        implementation, lane = job.split(":", 1)
        offset = int(lane.removeprefix("offset"))
        assert wrapper["exit"] == 0 and wrapper["timed_out"] is False
        assert 0 < wrapper["peak_mb"] <= 128
        row = wrapper["result"]
        assert row["event"] in {"FALSIFIED", "SURVIVED"}
        assert row["offset"] == offset
        results[implementation][offset] = row

    falsified = []
    compare = (
        "event", "offset", "units_checked", "unsafe_units_checked",
        "profiles_checked", "leader", "complete",
    )
    witness = (
        "m2", "m3", "s2", "s3", "s4", "s5", "m4", "m5", "case",
        "charges", "adjacent_edges", "raw_before", "raw_before_high",
        "clipped_after", "clipped_high", "excess_over_leader",
    )
    for offset in range(1, 44):
        primary, audit = results["primary"][offset], results["audit"][offset]
        for key in compare:
            assert primary[key] == audit[key], (offset, key)
        if primary["event"] == "FALSIFIED":
            falsified.append(offset)
            for key in witness:
                assert primary[key] == audit[key], (offset, key)
        else:
            assert primary["units_checked"] == (77 - offset) * 6084
            assert jobs[f"primary:offset{offset}"]["progress_rows"] == 77 - offset
            assert jobs[f"audit:offset{offset}"]["progress_rows"] == 77 - offset

    if falsified:
        status = "FALSIFIED"
    else:
        status = "PASS"
        source_units = sum(
            results["primary"][offset]["units_checked"]
            for offset in range(1, 44)
        )
        unsafe_units = sum(
            results["primary"][offset]["unsafe_units_checked"]
            for offset in range(1, 44)
        )
        assert source_units == 14_388_660
        assert unsafe_units == 511_677
    print(json.dumps({
        "status": status,
        "capture_sha256": capture_sha,
        "jobs": len(jobs),
        "offsets": len(results["primary"]),
        "falsified_offsets": falsified,
        "source_units": sum(
            results["primary"][offset]["units_checked"]
            for offset in range(1, 44)
        ),
        "unsafe_units": sum(
            results["primary"][offset]["unsafe_units_checked"]
            for offset in range(1, 44)
        ),
        "profiles_per_implementation": sum(
            results["primary"][offset]["profiles_checked"]
            for offset in range(1, 44)
        ),
    }, sort_keys=True))


if __name__ == "__main__":
    main()

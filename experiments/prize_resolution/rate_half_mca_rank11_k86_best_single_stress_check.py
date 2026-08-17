#!/usr/bin/env python3
"""Check the paired K'=86 best-single stress capture."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


OFFSETS = (1, 23, 32, 42)


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

    jobs = {}
    batch = None
    for row in json_rows(raw.decode(errors="replace")):
        if row.get("event") == "JOB_RESULT":
            assert row["job"] not in jobs
            jobs[row["job"]] = row
        elif row.get("event") in {"BATCH_COMPLETE", "BATCH_INCOMPLETE"}:
            batch = row
    assert batch == {
        "completed": 8,
        "event": "BATCH_COMPLETE",
        "expected": 8,
        "infrastructure_failures": 0,
    }
    expected = {
        f"{implementation}:offset{offset}"
        for implementation in ("primary", "audit")
        for offset in OFFSETS
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

    keys = (
        "event", "offset", "units_checked", "unsafe_units_checked",
        "profiles_checked", "leader", "complete",
    )
    for offset in OFFSETS:
        primary = results["primary"][offset]
        audit = results["audit"][offset]
        for key in keys:
            assert primary[key] == audit[key], (offset, key)
        if primary["event"] == "SURVIVED":
            assert primary["units_checked"] == (76 - offset) * 5929
        else:
            for key in (
                "m2", "m3", "s2", "s3", "s4", "s5", "m4", "m5",
                "case", "charges", "single_edges", "raw_before",
                "raw_before_high", "single_after", "single_high",
                "excess_over_leader",
            ):
                assert primary[key] == audit[key], (offset, key)

    events = {
        offset: results["primary"][offset]["event"] for offset in OFFSETS
    }
    status = "SURVIVED" if set(events.values()) == {"SURVIVED"} else "FALSIFIED"
    print(json.dumps({
        "status": status,
        "capture_sha256": capture_sha,
        "jobs": len(jobs),
        "events": events,
        "profiles_per_implementation": sum(
            results["primary"][offset]["profiles_checked"] for offset in OFFSETS
        ),
        "source_units_completed": sum(
            results["primary"][offset]["units_checked"] for offset in OFFSETS
        ),
    }, sort_keys=True))


if __name__ == "__main__":
    main()

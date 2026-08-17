#!/usr/bin/env python3
"""Check the paired K'=87 raw-clipped offset-1 capture."""

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

    jobs = {}
    batch = None
    for row in json_rows(raw.decode(errors="replace")):
        if row.get("event") == "JOB_RESULT":
            assert row["job"] not in jobs
            jobs[row["job"]] = row
        elif row.get("event") in {"BATCH_COMPLETE", "BATCH_INCOMPLETE"}:
            batch = row
    assert batch == {
        "completed": 2,
        "event": "BATCH_COMPLETE",
        "expected": 2,
        "infrastructure_failures": 0,
    }
    assert set(jobs) == {"primary", "audit"}
    results = {}
    for implementation, wrapper in jobs.items():
        assert wrapper["exit"] == 0 and wrapper["timed_out"] is False
        assert 0 < wrapper["peak_mb"] <= 128
        row = wrapper["result"]
        assert row["event"] in {"FALSIFIED", "SURVIVED"}
        assert row["offset"] == 1
        results[implementation] = row

    primary, audit = results["primary"], results["audit"]
    for key in (
        "event", "offset", "units_checked", "unsafe_units_checked",
        "profiles_checked", "leader", "complete",
    ):
        assert primary[key] == audit[key], key
    if primary["event"] == "SURVIVED":
        assert primary["units_checked"] == 462_384
        assert jobs["primary"]["progress_rows"] == 76
        assert jobs["audit"]["progress_rows"] == 76
    else:
        for key in (
            "m2", "m3", "s2", "s3", "s4", "s5", "m4", "m5",
            "case", "charges", "adjacent_edges", "raw_before",
            "raw_before_high", "clipped_after", "clipped_high",
            "excess_over_leader",
        ):
            assert primary[key] == audit[key], key
    print(json.dumps({
        "status": primary["event"],
        "capture_sha256": capture_sha,
        "jobs": len(jobs),
        "source_units_completed": primary["units_checked"],
        "unsafe_units_completed": primary["unsafe_units_checked"],
        "profiles_per_implementation": primary["profiles_checked"],
        "result": primary,
    }, sort_keys=True))


if __name__ == "__main__":
    main()

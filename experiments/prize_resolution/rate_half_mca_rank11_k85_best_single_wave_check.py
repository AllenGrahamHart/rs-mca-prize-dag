#!/usr/bin/env python3
"""Merge a paired complete K'=85 best-single domination wave."""

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
        "completed": 82,
        "event": "BATCH_COMPLETE",
        "expected": 82,
        "infrastructure_failures": 0,
    }
    expected = {
        f"{implementation}:offset{offset}"
        for implementation in ("primary", "audit")
        for offset in range(1, 42)
    }
    assert set(jobs) == expected

    results = {"primary": {}, "audit": {}}
    for job, wrapper in jobs.items():
        implementation, lane = job.split(":", 1)
        offset = int(lane.removeprefix("offset"))
        assert wrapper["exit"] == 0 and wrapper["timed_out"] is False
        assert 0 < wrapper["peak_mb"] <= 128
        row = wrapper["result"]
        assert row["event"] == "SURVIVED" and row["complete"] is True
        assert row["offset"] == offset
        assert row["units_checked"] == (75 - offset) * 5776
        assert wrapper["progress_rows"] == 75 - offset
        results[implementation][offset] = row

    for offset in range(1, 42):
        primary = results["primary"][offset]
        audit = results["audit"][offset]
        for key in (
            "offset", "units_checked", "unsafe_units_checked",
            "profiles_checked", "leader", "complete",
        ):
            assert primary[key] == audit[key], (offset, key)

    source_units = sum(
        row["units_checked"] for row in results["primary"].values()
    )
    unsafe_units = sum(
        row["unsafe_units_checked"] for row in results["primary"].values()
    )
    profiles = sum(
        row["profiles_checked"] for row in results["primary"].values()
    )
    assert source_units == 12_788_064
    assert unsafe_units == 331_533
    print(json.dumps({
        "status": "PASS",
        "capture_sha256": capture_sha,
        "jobs": len(jobs),
        "offsets": len(results["primary"]),
        "source_units": source_units,
        "unsafe_units": unsafe_units,
        "profiles_per_implementation": profiles,
        "leader": next(iter(results["primary"].values()))["leader"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()

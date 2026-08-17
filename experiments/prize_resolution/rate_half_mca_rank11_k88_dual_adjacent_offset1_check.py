#!/usr/bin/env python3
"""Check the paired K'=88 dual-adjacent offset-1 capture."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


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
    args = parser.parse_args()
    raw = args.capture.read_bytes()
    jobs, batch = {}, None
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
    for wrapper in jobs.values():
        assert wrapper["exit"] == 0 and wrapper["timed_out"] is False
        assert 0 < int(wrapper["peak_mb"]) <= 128
    primary, audit = jobs["primary"]["result"], jobs["audit"]["result"]
    compare = (
        "event", "offset", "units_checked", "unsafe_units_checked",
        "profiles_checked", "leader", "complete",
    )
    for key in compare:
        assert primary[key] == audit[key], key
    witness = (
        "m2", "m3", "s2", "s3", "s4", "s5", "m4", "m5", "case",
        "charges", "adjacent_edges", "raw_before", "raw_before_high",
        "clipped_after", "clipped_high", "excess_over_leader",
    )
    if primary["event"] == "FALSIFIED":
        for key in witness:
            assert primary[key] == audit[key], key
        status = "FALSIFIED"
    else:
        assert primary["units_checked"] == 480_557
        assert primary["unsafe_units_checked"] == 27_562
        assert jobs["primary"]["progress_rows"] == 77
        assert jobs["audit"]["progress_rows"] == 77
        status = "PASS"
    print(json.dumps({
        "status": status,
        "capture_sha256": hashlib.sha256(raw).hexdigest(),
        "source_units": primary["units_checked"],
        "unsafe_units": primary["unsafe_units_checked"],
        "profiles_per_implementation": primary["profiles_checked"],
        "result": primary,
        "peak_mb": max(int(row["peak_mb"]) for row in jobs.values()),
    }, sort_keys=True))


if __name__ == "__main__":
    main()

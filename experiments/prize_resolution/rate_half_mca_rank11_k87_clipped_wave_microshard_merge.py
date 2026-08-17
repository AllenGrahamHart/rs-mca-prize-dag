#!/usr/bin/env python3
"""Validate contiguous K'=87 microshards and emit one canonical capture."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def json_rows(path: Path):
    for line in path.read_text(errors="replace").splitlines():
        if line.startswith("{"):
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("captures", nargs="+", type=Path)
    parser.add_argument("--sha256", nargs="+", required=True)
    args = parser.parse_args()
    assert len(args.captures) == len(args.sha256)
    jobs, ranges = {}, []
    for path, expected_sha in zip(args.captures, args.sha256):
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected_sha
        batch = None
        shard_jobs = {}
        for row in json_rows(path):
            if row.get("event") == "JOB_RESULT":
                assert row["job"] not in shard_jobs
                shard_jobs[row["job"]] = row
            elif row.get("event") in {"BATCH_COMPLETE", "BATCH_INCOMPLETE"}:
                batch = row
        assert batch is not None and batch["event"] == "BATCH_COMPLETE"
        start, end = int(batch["start"]), int(batch["end"])
        expected_count = 2 * (end - start + 1)
        assert batch == {
            "completed": expected_count,
            "end": end,
            "event": "BATCH_COMPLETE",
            "expected": expected_count,
            "infrastructure_failures": 0,
            "start": start,
        }
        expected_jobs = {
            f"{implementation}:offset{offset}"
            for implementation in ("primary", "audit")
            for offset in range(start, end + 1)
        }
        assert set(shard_jobs) == expected_jobs
        assert not set(jobs).intersection(shard_jobs)
        jobs.update(shard_jobs)
        ranges.append((start, end))
    ranges.sort()
    assert ranges[0][0] == 1 and ranges[-1][1] == 43
    assert all(left[1] + 1 == right[0] for left, right in zip(ranges, ranges[1:]))
    assert len(jobs) == 86
    for name in sorted(jobs):
        print(json.dumps(jobs[name], sort_keys=True))
    print(json.dumps({
        "completed": 86,
        "event": "BATCH_COMPLETE",
        "expected": 86,
        "infrastructure_failures": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()

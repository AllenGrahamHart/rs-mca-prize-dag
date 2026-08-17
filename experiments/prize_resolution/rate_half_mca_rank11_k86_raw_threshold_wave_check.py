#!/usr/bin/env python3
"""Merge and compare a complete paired K'=86 raw-threshold capture."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


COMPARE_KEYS = (
    "units",
    "raw_rows",
    "high_vectors",
    "safe_units",
    "unsafe_units",
    "safe_maximum",
    "safe_margin",
    "safe_branch",
    "unsafe_minimum",
    "unsafe_minimum_branch",
    "unsafe_maximum",
    "unsafe_maximum_branch",
    "classification_sha256",
    "m2_profile",
    "complete",
)


def json_lines(text: str):
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
    parser.add_argument("--sha256")
    args = parser.parse_args()
    raw = args.capture.read_bytes()
    capture_sha = hashlib.sha256(raw).hexdigest()
    if args.sha256 is not None:
        assert capture_sha == args.sha256

    jobs: dict[str, dict[str, object]] = {}
    batch = None
    for row in json_lines(raw.decode(errors="replace")):
        if row.get("event") == "JOB_RESULT":
            assert row["job"] not in jobs
            jobs[row["job"]] = row
        elif row.get("event") in {"BATCH_PASS", "BATCH_INCOMPLETE"}:
            batch = row
    assert batch == {
        "completed": 150,
        "event": "BATCH_PASS",
        "expected": 150,
        "failures": 0,
    }
    expected = {
        f"{implementation}:offset{offset}"
        for implementation in ("primary", "audit")
        for offset in range(1, 76)
    }
    assert set(jobs) == expected

    results: dict[str, dict[int, dict[str, object]]] = {
        "primary": {},
        "audit": {},
    }
    for job, wrapper in jobs.items():
        implementation, lane = job.split(":", 1)
        offset = int(lane.removeprefix("offset"))
        assert wrapper["exit"] == 0 and wrapper["timed_out"] is False
        assert 0 < int(wrapper["peak_mb"]) <= 128
        rows = [
            row
            for row in json_lines(str(wrapper["stdout"]))
            if row.get("event") == "K86_RAW_OFFSET"
        ]
        assert len(rows) == 1
        row = rows[0]
        assert row["implementation"] == implementation
        assert row["offset"] == offset and row["complete"] is True
        assert row["units"] == (76 - offset) * 5929
        assert row["high_vectors"] == 7
        assert row["raw_rows"] == 7 * row["units"]
        assert row["safe_units"] + row["unsafe_units"] == row["units"]
        assert len(row["m2_profile"]) == 76 - offset
        assert sum(item["safe_units"] for item in row["m2_profile"]) == row["safe_units"]
        assert sum(item["unsafe_units"] for item in row["m2_profile"]) == row["unsafe_units"]
        results[implementation][offset] = row

    for offset in range(1, 76):
        primary = results["primary"][offset]
        audit = results["audit"][offset]
        for key in COMPARE_KEYS:
            assert primary[key] == audit[key], (offset, key)

    leader = max(
        (int(row["safe_maximum"]), offset, str(row["safe_branch"]))
        for offset, row in results["primary"].items()
    )
    total_units = sum(int(row["units"]) for row in results["primary"].values())
    total_safe = sum(int(row["safe_units"]) for row in results["primary"].values())
    total_unsafe = sum(int(row["unsafe_units"]) for row in results["primary"].values())
    unsafe_offsets = [
        offset for offset, row in results["primary"].items()
        if int(row["unsafe_units"]) > 0
    ]
    assert total_safe + total_unsafe == total_units
    print(json.dumps({
        "status": "PASS",
        "capture_sha256": capture_sha,
        "jobs": len(jobs),
        "offsets": len(results["primary"]),
        "source_units": total_units,
        "raw_rows_per_implementation": 7 * total_units,
        "safe_units": total_safe,
        "unsafe_units": total_unsafe,
        "unsafe_offsets": unsafe_offsets,
        "safe_leader": leader[0],
        "safe_leader_offset": leader[1],
        "safe_leader_branch": leader[2],
    }, sort_keys=True))


if __name__ == "__main__":
    main()

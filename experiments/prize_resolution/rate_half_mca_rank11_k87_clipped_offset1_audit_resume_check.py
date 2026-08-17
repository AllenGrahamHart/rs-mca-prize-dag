#!/usr/bin/env python3
"""Merge the completed primary capture with the cached audit resume."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def rows(path: Path):
    for line in path.read_text(errors="replace").splitlines():
        if line.startswith("{"):
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("original", type=Path)
    parser.add_argument("resume", type=Path)
    parser.add_argument("--original-sha256", required=True)
    parser.add_argument("--resume-sha256", required=True)
    args = parser.parse_args()
    assert hashlib.sha256(args.original.read_bytes()).hexdigest() == args.original_sha256
    assert hashlib.sha256(args.resume.read_bytes()).hexdigest() == args.resume_sha256
    original = list(rows(args.original))
    resumed = list(rows(args.resume))
    primary_wrappers = [
        row for row in original
        if row.get("event") == "JOB_RESULT" and row.get("job") == "primary"
    ]
    audit_wrappers = [
        row for row in resumed
        if row.get("event") == "JOB_RESULT" and row.get("job") == "audit-cached"
    ]
    assert len(primary_wrappers) == len(audit_wrappers) == 1
    primary_wrapper, audit_wrapper = primary_wrappers[0], audit_wrappers[0]
    for wrapper in (primary_wrapper, audit_wrapper):
        assert wrapper["exit"] == 0 and wrapper["timed_out"] is False
        assert 0 < wrapper["peak_mb"] <= 128
    primary, audit = primary_wrapper["result"], audit_wrapper["result"]
    for key in (
        "event", "offset", "units_checked", "unsafe_units_checked",
        "profiles_checked", "leader", "complete",
    ):
        assert primary[key] == audit[key], key
    assert primary["event"] == "SURVIVED" and primary["complete"] is True
    assert primary["units_checked"] == 462_384
    assert primary["unsafe_units_checked"] == 23_104
    assert primary_wrapper["progress_rows"] == audit_wrapper["progress_rows"] == 76
    assert audit["clipped_cache_entries"] > 0
    print(json.dumps({
        "status": "PASS",
        "original_capture_sha256": args.original_sha256,
        "resume_capture_sha256": args.resume_sha256,
        "source_units": primary["units_checked"],
        "unsafe_units": primary["unsafe_units_checked"],
        "profiles_per_implementation": primary["profiles_checked"],
        "audit_cache_entries": audit["clipped_cache_entries"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()

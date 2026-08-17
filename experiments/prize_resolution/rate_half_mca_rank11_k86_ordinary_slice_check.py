#!/usr/bin/env python3
"""Verify the paired ordinary slice retained by the incomplete K'=86 pilot."""

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

    wrappers = {}
    for row in json_rows(raw.decode(errors="replace")):
        if row.get("event") != "JOB_RESULT" or not row.get("job", "").endswith(
            ":ordinary"
        ):
            continue
        assert row["job"] not in wrappers
        wrappers[row["job"]] = row
    assert set(wrappers) == {"primary:ordinary", "audit:ordinary"}

    results = {}
    for implementation in ("primary", "audit"):
        wrapper = wrappers[f"{implementation}:ordinary"]
        assert wrapper["exit"] == 0 and wrapper["timed_out"] is False
        assert 0 < wrapper["peak_mb"] <= 128
        terminals = [
            row
            for row in json_rows(wrapper["stdout"])
            if row.get("event") in {"LANE", "AUDIT_LANE"}
        ]
        assert len(terminals) == 1
        row = terminals[0]
        assert row["complete"] is True and row["lane"] == "ordinary"
        results[implementation] = row

    keys = (
        "units", "raw_rows", "raw_safe_units", "expanded_units",
        "geometry_rows", "maximum", "margin", "complete", "lane",
    )
    for key in keys:
        assert results["primary"][key] == results["audit"][key], key
    row = results["primary"]
    assert row["units"] == 504_660
    assert row["raw_rows"] == 7 * row["units"] == 3_532_620
    assert row["raw_safe_units"] == 115_523
    assert row["expanded_units"] == 3_037
    assert row["geometry_rows"] == 2_718_499
    assert row["maximum"] == 41436497718685364991538520386265961874369213524
    ceiling = 41436893577610853150410067365747465877788324838
    assert row["margin"] == ceiling - row["maximum"] > 0
    print(json.dumps({
        "status": "PASS",
        "capture_sha256": capture_sha,
        "jobs": len(wrappers),
        "source_units": row["units"],
        "raw_rows": row["raw_rows"],
        "expanded_units": row["expanded_units"],
        "geometry_rows_per_implementation": row["geometry_rows"],
        "premium": row["maximum"],
        "margin": row["margin"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()

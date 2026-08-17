#!/usr/bin/env python3
"""Check the paired K'=87 ordinary-lane capture."""

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


def normalized_branch(label: str) -> str:
    return label.removesuffix("-safe")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("capture", type=Path)
    parser.add_argument("--sha256", required=True)
    args = parser.parse_args()
    raw = args.capture.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == args.sha256

    wrappers, batch = {}, None
    for row in json_rows(raw.decode(errors="replace")):
        if row.get("event") == "JOB_RESULT":
            assert row["job"] not in wrappers
            wrappers[row["job"]] = row
        elif row.get("event") in {"BATCH_COMPLETE", "BATCH_INCOMPLETE"}:
            batch = row
    assert batch == {
        "completed": 2,
        "event": "BATCH_COMPLETE",
        "expected": 2,
        "infrastructure_failures": 0,
    }
    assert set(wrappers) == {"primary:ordinary", "audit:ordinary"}

    results, terminals, starts = {}, {}, {}
    for implementation in ("primary", "audit"):
        wrapper = wrappers[f"{implementation}:ordinary"]
        assert wrapper["exit"] == 0 and wrapper["timed_out"] is False
        assert 0 < wrapper["peak_mb"] <= 128
        payload = list(json_rows(wrapper["stdout"]))
        result_event = "LANE" if implementation == "primary" else "AUDIT_LANE"
        final = [row for row in payload if row.get("event") == result_event]
        terminal = [row for row in payload if row.get("event") == "K87_LANE"]
        start = [
            row for row in payload
            if row.get("event") in {"K87_START", "K87_AUDIT_START"}
        ]
        assert len(final) == len(terminal) == len(start) == 1
        assert final[0]["lane"] == terminal[0]["lane"] == "ordinary"
        assert final[0]["complete"] is True
        assert start[0]["kprime"] == 87 and start[0]["lane"] == "ordinary"
        results[implementation] = final[0]
        terminals[implementation] = terminal[0]
        starts[implementation] = start[0]

    compare = (
        "units", "raw_rows", "raw_safe_units", "expanded_units",
        "geometry_rows", "maximum", "margin", "complete", "lane",
    )
    for key in compare:
        assert results["primary"][key] == results["audit"][key], key
    assert starts["primary"]["ceiling"] == starts["audit"]["ceiling"]
    assert normalized_branch(results["primary"]["active_branch"]) == normalized_branch(
        results["audit"]["active_branch"]
    )
    row = results["primary"]
    ceiling = starts["primary"]["ceiling"]
    assert row["raw_rows"] == 7 * row["units"]
    assert row["geometry_rows"] >= row["expanded_units"]
    assert row["margin"] == ceiling - row["maximum"]
    for implementation in ("primary", "audit"):
        terminal = terminals[implementation]
        assert terminal["maximum"] == row["maximum"]
        assert terminal["margin"] == row["margin"]
        assert terminal["safe"] == (row["margin"] >= 0)

    print(json.dumps({
        "status": "PASS" if row["margin"] >= 0 else "UNSAFE",
        "capture_sha256": args.sha256,
        "jobs": 2,
        "source_units": row["units"],
        "raw_rows": row["raw_rows"],
        "raw_safe_units": row["raw_safe_units"],
        "expanded_units": row["expanded_units"],
        "geometry_rows_per_implementation": row["geometry_rows"],
        "premium": row["maximum"],
        "safe_premium_ceiling": ceiling,
        "margin": row["margin"],
        "active_branch": row["active_branch"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()

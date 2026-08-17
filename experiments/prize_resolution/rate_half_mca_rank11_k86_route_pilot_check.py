#!/usr/bin/env python3
"""Check a paired K'=86 route-locating pilot capture."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


EXPECTED_LANES = {"ordinary", "offset11", "offset23", "offset41", "offset75"}
COMPARE_KEYS = (
    "units",
    "raw_rows",
    "raw_safe_units",
    "expanded_units",
    "maximum",
    "margin",
)


def json_lines(text: str):
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
    parser.add_argument("capture")
    parser.add_argument("--sha256", required=True)
    args = parser.parse_args()
    raw = Path(args.capture).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == args.sha256
    attempts = {}
    batch = None
    for row in json_lines(raw.decode(errors="replace")):
        if row.get("event") == "JOB_RESULT":
            attempts.setdefault(row["job"], []).append(row)
        elif row.get("event") in {"BATCH_PASS", "BATCH_INCOMPLETE"}:
            batch = row
    assert batch == {
        "completed": 10,
        "event": "BATCH_PASS",
        "expected": 10,
        "failures": 0,
    }
    expected_jobs = {
        f"{implementation}:{lane}"
        for implementation in ("primary", "audit")
        for lane in EXPECTED_LANES
    }
    assert set(attempts) == expected_jobs
    assert all(len(rows) == 1 for rows in attempts.values())

    results = {"primary": {}, "audit": {}}
    terminals = {"primary": {}, "audit": {}}
    for job, rows in attempts.items():
        row = rows[0]
        implementation, lane = job.split(":", 1)
        assert row["exit"] == 0 and not row["timed_out"]
        assert 0 < row["peak_mb"] <= 128
        payload = list(json_lines(row["stdout"]))
        event = "LANE" if implementation == "primary" else "AUDIT_LANE"
        final = [item for item in payload if item.get("event") == event]
        terminal = [item for item in payload if item.get("event") == "K86_LANE"]
        assert len(final) == len(terminal) == 1
        assert final[0]["lane"] == lane and final[0]["complete"] is True
        assert terminal[0]["lane"] == lane
        results[implementation][lane] = final[0]
        terminals[implementation][lane] = terminal[0]

    for lane in EXPECTED_LANES:
        primary, audit = results["primary"][lane], results["audit"][lane]
        for key in COMPARE_KEYS:
            assert primary[key] == audit[key], (lane, key)
        assert normalized_branch(primary["active_branch"]) == normalized_branch(
            audit["active_branch"]
        )
        assert primary["raw_rows"] == 7 * primary["units"]
        assert audit["geometry_rows"] >= primary["geometry_rows"]
        pterm, aterm = terminals["primary"][lane], terminals["audit"][lane]
        assert pterm["safe"] == aterm["safe"] == (primary["margin"] >= 0)
        if lane != "ordinary":
            offset = int(lane.removeprefix("offset"))
            assert primary["units"] == (76 - offset) * 5929
            assert primary["raw_safe_units"] + primary["expanded_units"] == primary["units"]

    sampled_maximum = max(
        (row["maximum"], lane, row["active_branch"])
        for lane, row in results["primary"].items()
    )
    unsafe = sorted(
        lane for lane, row in terminals["primary"].items() if not row["safe"]
    )
    print(json.dumps({
        "status": "PASS",
        "capture_sha256": args.sha256,
        "jobs": len(attempts),
        "lanes": len(EXPECTED_LANES),
        "unsafe_sampled_lanes": unsafe,
        "sampled_global_maximum": sampled_maximum[0],
        "sampled_global_lane": sampled_maximum[1],
        "sampled_global_branch": sampled_maximum[2],
    }, sort_keys=True))


if __name__ == "__main__":
    main()

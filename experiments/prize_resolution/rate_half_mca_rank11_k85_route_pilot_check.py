#!/usr/bin/env python3
"""Check the paired K'=85 route-locating pilot capture."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


CAPTURE_SHA256 = "5a6ee4f212571eae022ed943c6062e95f6b6a2ccb186dbf4338f1b0cf2f45327"
EXPECTED_LANES = {"ordinary", "offset1", "offset15", "offset23", "offset74"}
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
    if len(sys.argv) != 2:
        raise SystemExit("usage: k85_route_pilot_check.py CAPTURE")
    raw = Path(sys.argv[1]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == CAPTURE_SHA256
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
    for job, rows in attempts.items():
        row = rows[0]
        implementation, lane = job.split(":", 1)
        assert row["exit"] == 0 and not row["timed_out"]
        assert 0 < row["peak_mb"] <= 128
        payload = list(json_lines(row["stdout"]))
        event = "LANE" if implementation == "primary" else "AUDIT_LANE"
        final = [item for item in payload if item.get("event") == event]
        assert len(final) == 1
        assert final[0]["lane"] == lane and final[0]["complete"] is True
        terminal = "K85_PASS" if implementation == "primary" else "K85_AUDIT_PASS"
        assert any(item.get("event") == terminal for item in payload)
        results[implementation][lane] = final[0]

    for lane in EXPECTED_LANES:
        primary, audit = results["primary"][lane], results["audit"][lane]
        for key in COMPARE_KEYS:
            assert primary[key] == audit[key], (lane, key)
        assert normalized_branch(primary["active_branch"]) == normalized_branch(
            audit["active_branch"]
        )
        assert primary["raw_rows"] == 7 * primary["units"]
        assert audit["geometry_rows"] >= primary["geometry_rows"]
        if lane == "ordinary":
            assert primary["units"] == 492960
        else:
            offset = int(lane.removeprefix("offset"))
            assert primary["units"] == (75 - offset) * 5776
            assert (
                primary["raw_safe_units"] + primary["expanded_units"]
                == primary["units"]
            )

    ordered = {}
    for lane in sorted(EXPECTED_LANES, key=lambda name: (name != "ordinary", name)):
        row = results["primary"][lane]
        ordered[lane] = {
            "maximum": row["maximum"],
            "margin": row["margin"],
            "active_branch": row["active_branch"],
        }
    sampled_maximum = max(
        (row["maximum"], lane, row["active_branch"])
        for lane, row in results["primary"].items()
    )
    assert sampled_maximum[0] <= 41412869809855175413648318362513310330909061869
    print(json.dumps({
        "status": "PASS",
        "capture_sha256": CAPTURE_SHA256,
        "jobs": len(attempts),
        "lanes": len(EXPECTED_LANES),
        "sampled_global_maximum": sampled_maximum[0],
        "sampled_global_lane": sampled_maximum[1],
        "sampled_global_branch": sampled_maximum[2],
        "lanes_detail": ordered,
    }, sort_keys=True))


if __name__ == "__main__":
    main()

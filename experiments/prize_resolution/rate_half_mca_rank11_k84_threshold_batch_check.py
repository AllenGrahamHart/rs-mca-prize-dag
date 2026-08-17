#!/usr/bin/env python3
"""Check the complete primary/audit K'=84 exact-router outputs."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


EXPECTED_LANES = {"ordinary"} | {
    f"offset{value}" for value in range(1, 74)
}
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
    if len(sys.argv) != 3:
        raise SystemExit(
            "usage: k84_threshold_batch_check.py PRIMARY_OUTPUT AUDIT_OUTPUT"
        )
    attempts = {}
    digests = []
    for name in sys.argv[1:]:
        path = Path(name)
        raw = path.read_bytes()
        digests.append([path.name, hashlib.sha256(raw).hexdigest()])
        batch = None
        local_jobs = 0
        for row in json_lines(raw.decode(errors="replace")):
            if row.get("event") == "JOB_RESULT":
                local_jobs += 1
                attempts.setdefault(row["job"], []).append(row)
            elif row.get("event") in {"BATCH_PASS", "BATCH_INCOMPLETE"}:
                batch = row
        assert batch is not None and batch["event"] == "BATCH_PASS"
        assert batch["completed"] == local_jobs == batch["expected"] == 74

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
        terminal = "K84_PASS" if implementation == "primary" else "K84_AUDIT_PASS"
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
            assert (
                primary["units"],
                primary["raw_safe_units"],
                primary["expanded_units"],
            ) == (457938, 108047, 1621)
        else:
            offset = int(lane.removeprefix("offset"))
            assert primary["units"] == (74 - offset) * 5625
            assert (
                primary["raw_safe_units"] + primary["expanded_units"]
                == primary["units"]
            )

    maximum = max(
        (row["maximum"], lane, row["active_branch"])
        for lane, row in results["primary"].items()
    )
    assert maximum == (
        41388798786059119503097492734939028640066114130,
        "ordinary",
        "s2=74/s3=55/s4=45/s5=37/ordinary-single/"
        "c6d3/c7d2/c8d1/c9d0/raw-safe",
    )
    minimum_margin = min(
        row["margin"] for row in results["primary"].values()
    )
    assert minimum_margin == 44581160171407926086602515730765812413619
    print(json.dumps({
        "batch_sha256": digests,
        "jobs": len(attempts),
        "lanes": len(EXPECTED_LANES),
        "global_maximum": maximum[0],
        "global_lane": maximum[1],
        "global_branch": maximum[2],
        "minimum_margin": minimum_margin,
        "source_units": sum(
            row["units"] for row in results["primary"].values()
        ),
        "raw_rows": sum(
            row["raw_rows"] for row in results["primary"].values()
        ),
        "primary_geometry_rows": sum(
            row["geometry_rows"] for row in results["primary"].values()
        ),
        "audit_geometry_rows": sum(
            row["geometry_rows"] for row in results["audit"].values()
        ),
        "status": "PASS",
    }, sort_keys=True))


if __name__ == "__main__":
    main()

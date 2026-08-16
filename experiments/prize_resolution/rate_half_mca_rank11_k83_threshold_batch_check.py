#!/usr/bin/env python3
"""Check the complete primary/audit K'=83 exact-router outputs."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


EXPECTED_LANES = {"ordinary"} | {
    f"offset{value}" for value in range(1, 73)
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


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("usage: threshold_batch_check.py BATCH_OUTPUT [...]")
    attempts = {}
    digests = []
    duplicate_jobs = 0
    for name in sys.argv[1:]:
        path = Path(name)
        raw = path.read_bytes()
        digests.append([path.name, hashlib.sha256(raw).hexdigest()])
        batch = None
        local_jobs = 0
        for row in json_lines(raw.decode(errors="replace")):
            if row.get("event") == "JOB_RESULT":
                local_jobs += 1
                job = row["job"]
                duplicate_jobs += int(job in attempts)
                attempts.setdefault(job, []).append(row)
            elif row.get("event") in {"BATCH_PASS", "BATCH_INCOMPLETE"}:
                batch = row
        if batch is not None:
            assert batch["completed"] == local_jobs
            assert batch["expected"] >= local_jobs
    expected_jobs = {
        f"{implementation}:{lane}"
        for implementation in ("primary", "audit")
        for lane in EXPECTED_LANES
    }
    assert set(attempts) == expected_jobs

    results = {"primary": {}, "audit": {}}
    jobs = {}
    for job, rows in attempts.items():
        successful = [
            row for row in rows
            if row["exit"] == 0 and not row["timed_out"]
        ]
        assert successful, job
        row = successful[0]
        for duplicate in successful[1:]:
            assert duplicate["stdout"] == row["stdout"], job
        jobs[job] = row
        implementation, lane = job.split(":", 1)
        assert row["exit"] == 0 and not row["timed_out"]
        assert 0 < row["peak_mb"] <= 128
        payload = list(json_lines(row["stdout"]))
        event = "LANE" if implementation == "primary" else "AUDIT_LANE"
        final = [item for item in payload if item.get("event") == event]
        assert len(final) == 1
        assert final[0]["lane"] == lane and final[0]["complete"] is True
        terminal = "PASS" if implementation == "primary" else "AUDIT_PASS"
        assert any(item.get("event") == terminal for item in payload)
        results[implementation][lane] = final[0]

    for lane in EXPECTED_LANES:
        primary, audit = results["primary"][lane], results["audit"][lane]
        for key in COMPARE_KEYS:
            assert primary[key] == audit[key], (lane, key)
        assert primary["raw_rows"] == 7 * primary["units"]
        if lane == "ordinary":
            assert (
                primary["units"],
                primary["raw_safe_units"],
                primary["expanded_units"],
            ) == (446823, 106914, 1272)
        else:
            offset = int(lane.removeprefix("offset"))
            assert primary["units"] == (73 - offset) * 5476
            assert (
                primary["raw_safe_units"] + primary["expanded_units"]
                == primary["units"]
            )

    maximum = max(
        (row["maximum"], lane, row["active_branch"])
        for lane, row in results["primary"].items()
    )
    minimum_margin = min(
        row["margin"] for row in results["primary"].values()
    )
    assert minimum_margin > 0
    print(json.dumps({
        "batch_sha256": digests,
        "duplicate_jobs": duplicate_jobs,
        "jobs": len(jobs),
        "lanes": len(EXPECTED_LANES),
        "global_maximum": maximum[0],
        "global_lane": maximum[1],
        "global_branch": maximum[2],
        "minimum_margin": minimum_margin,
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

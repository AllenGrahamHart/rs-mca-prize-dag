#!/usr/bin/env python3
"""Seal the interrupted pairing-5 primary ledger from exact recovery rows."""

from __future__ import annotations

import itertools
import json
import os
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.sharded_result import (
    ShardedResultWriter,
    iter_records,
    load_manifest,
    verify,
)


EXP = ROOT / "experiments/prize_resolution"
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing5_chart_result"
RECOVERY = EXP / (
    "rate_half_kb_positive_433_1b_cell9_de_pairing5_chart_result_"
    "recovery_175_176_177"
)
SUMMARY = EXP / (
    "rate_half_kb_positive_433_1b_cell9_de_pairing5_chart_scout_result.json"
)
STAGING = PRIMARY.with_name(PRIMARY.name + "_sealed")
BACKUP = PRIMARY.with_name(PRIMARY.name + "_interrupted")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def key(row: dict) -> tuple[int, ...]:
    return (
        *row["epsilon"],
        *row["sigma"],
        row["xi_index"],
        row["b_row_index"],
        row["c_row_index"],
    )


def compact(row: dict) -> dict:
    return {
        "epsilon": row["epsilon"],
        "sigma": row["sigma"],
        "xi_index": row["xi_index"],
        "pairing_index": 5,
        "b_row_index": row["b_row_index"],
        "c_row_index": row["c_row_index"],
        "status": row["status"],
        "excluded": row["excluded"],
        "target_root_count": row["target_root_count"],
        "candidate_root_count": row["candidate_root_count"],
        "source_point_count": row["source_point_count"],
        "route_point_count": row["route_point_count"],
        "finite_row_count": len(row["finite_rows"]),
        "boundary_row_count": len(row["boundary_rows"]),
        "paid_rows": row["paid_rows"],
        "target_boundary_count": len(row["target_boundary_rows"]),
        "colored_solution_count": row["colored_solution_count"],
        "witnesses": row["witnesses"],
        "unresolved": row["unresolved"],
    }


def main() -> None:
    primary_manifest = PRIMARY / "manifest.json"
    recovery_manifest = RECOVERY / "manifest.json"
    require(not STAGING.exists() and not BACKUP.exists(), "stale recovery directory")
    require(
        verify(primary_manifest, require_complete=False)
        == {"shards": 5, "records": 160, "bytes": 56782159},
        "interrupted finalized custody",
    )
    require(
        verify(recovery_manifest)["records"] == 3,
        "recovery custody",
    )

    records = list(iter_records(primary_manifest))
    temporary = PRIMARY / "shards/part-00005.jsonl.tmp"
    require(temporary.is_file(), "interrupted temporary shard")
    with temporary.open() as handle:
        records.extend(json.loads(line) for line in handle)
    recovery_rows = list(iter_records(recovery_manifest))
    require(len(records) == 189 and len(recovery_rows) == 3, "recovery census")

    expected_cases = tuple(
        (*epsilon, sigma_c, sigma_o, xi_index, b_index, c_index)
        for epsilon in itertools.product((-1, 1), repeat=2)
        for sigma_c in (-1, 1)
        for sigma_o in (-1, 1)
        for xi_index in (0, 2)
        for b_index in (2, 3)
        for c_index in (4, 5, 6)
    )
    expected = set(expected_cases)
    seen = {key(row) for row in records}
    require(len(seen) == len(records), "duplicate interrupted Cartesian key")
    missing = expected - seen
    require(
        {expected_cases[index] for index in (175, 176, 177)} == missing,
        "unexpected interrupted key set",
    )
    require({key(row) for row in recovery_rows} == missing, "recovery key join")
    records.extend(recovery_rows)
    require(len({key(row) for row in records}) == len(records) == 192,
            "complete Cartesian key cover")
    require(
        all(
            row["status"] == "COMPLETE"
            and row["excluded"]
            and row["pairing_index"] == 5
            and not row["witnesses"]
            and not row["unresolved"]
            and not row["colored_solutions"]
            for row in records
        ),
        "nonterminal recovered row",
    )
    records.sort(key=key)

    metadata = load_manifest(primary_manifest)["metadata"]
    writer = ShardedResultWriter(STAGING, metadata=metadata, shard_records=32)
    for row in records:
        writer.add(row)
    staging_manifest = writer.close(complete=True)
    sealed_counts = verify(staging_manifest)
    require(sealed_counts["shards"] == 6 and sealed_counts["records"] == 192,
            "sealed custody")

    os.replace(PRIMARY, BACKUP)
    os.replace(STAGING, PRIMARY)
    verify(PRIMARY / "manifest.json")
    shutil.rmtree(BACKUP)

    summary = {
        "schema": (
            "rate-half-kb-positive-433-1b-cell9-de-pairing5-"
            "chart-scout-v1"
        ),
        "field": 2130706433,
        "scope": "Compact six-chart feasibility scout; no exclusion claim.",
        "source_template_sha256": metadata["source_template_sha256"],
        "source_tower_sha256": metadata["source_tower_sha256"],
        "source_kernel_sha256": metadata["source_kernel_sha256"],
        "rows": [compact(row) for row in records],
    }
    temporary_summary = SUMMARY.with_suffix(".json.tmp")
    temporary_summary.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    os.replace(temporary_summary, SUMMARY)
    print(
        "PAIRING5_RECOVERY_MERGE_PASS "
        f"rows=192 shards=6 bytes={sealed_counts['bytes']} missing=175,176,177"
    )


if __name__ == "__main__":
    main()

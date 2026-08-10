#!/usr/bin/env python3
"""Compile the exact cell-11 nested-norm exceptional replay manifest."""

from collections import Counter
import hashlib
import json
from pathlib import Path


DIRECTORY = Path(__file__).parent
PREFIX = (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_uncolored_resultant_norm_"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_uncolored_exceptional_replay_manifest.json"
)
EXPECTED_STATUSES = {
    "DEPLOYED_OFF_GUARD_UNIT": 288,
    "DEPLOYED_POINTWISE_NORM_COVER": 432,
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    shards = sorted(DIRECTORY.glob(f"{PREFIX}bc*_e*_result.json"))
    require(len(shards) == 8, "expected eight norm shards")
    cases = []
    statuses = Counter()
    row_count = 0
    shard_hashes = {}
    for path in shards:
        payload = json.loads(path.read_text())
        require(
            payload["schema"].endswith("cell11-uncolored-resultant-factor-atlas-v1"),
            f"schema: {path.name}",
        )
        require(payload["case_count"] == 90, f"case count: {path.name}")
        require(len(payload["rows"]) == 90, f"row count: {path.name}")
        shard_hashes[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
        for row in payload["rows"]:
            row_count += 1
            statuses[row["status"]] += 1
            norm = row["selected"]["resultant_nested_norm"]
            for root in norm["non_guard_base_field_roots"]:
                cases.append({
                    "bc_sign": row["bc_sign"],
                    "epsilon": row["epsilon"],
                    "missing_record": row["missing_record"],
                    "sigma_o": row["sigma_o"],
                    "pairing_index": row["pairing_index"],
                    "x": root["x"],
                    "root_multiplicity": root["multiplicity"],
                    "root_factor_sha256": root["factor_sha256"],
                    "norm_numerator_sha256": norm["numerator"]["sha256"],
                })
    require(row_count == 720, "expected 720 norm rows")
    require(dict(statuses) == EXPECTED_STATUSES, "norm status census")
    keys = [
        (
            row["bc_sign"], *row["epsilon"], row["missing_record"],
            row["sigma_o"], row["pairing_index"], row["x"],
        )
        for row in cases
    ]
    require(len(keys) == len(set(keys)) == 1584, "replay case census")
    require(len({row["x"] for row in cases}) == 126, "distinct root census")
    cases.sort(key=lambda row: (
        row["bc_sign"], *row["epsilon"], row["missing_record"],
        row["sigma_o"], row["pairing_index"], row["x"],
    ))
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-o0b-common-repeat-"
            "cell11-uncolored-exceptional-replay-manifest-v1"
        ),
        "scope": (
            "Every non-guard deployed base-field root in the exact nested-"
            "norm atlas; no root is omitted or deduplicated across formal cases."
        ),
        "norm_shard_sha256": shard_hashes,
        "norm_row_count": row_count,
        "norm_status_counts": dict(sorted(statuses.items())),
        "case_count": len(cases),
        "distinct_x_count": len({row["x"] for row in cases}),
        "cases": cases,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(
        "CELL11_EXCEPTIONAL_MANIFEST_PASS "
        f"norm_rows={row_count} cases={len(cases)} distinct_x=126"
    )


if __name__ == "__main__":
    main()

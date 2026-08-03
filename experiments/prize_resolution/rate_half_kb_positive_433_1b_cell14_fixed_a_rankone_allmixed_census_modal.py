#!/usr/bin/env python3
"""Audit the complete all-mixed cell-14 exclusion ledger on Modal."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
SOURCE = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_result.json"
COMPILER = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_modal.py"
REPLAY = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_root_replay_result.json"
REPLAY_SCRIPT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_root_replay_modal.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_census_result.json"
REMOTE_SOURCE = "/root/allmixed.json"
REMOTE_REPLAY = "/root/replay.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell14-allmixed-census")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .add_local_file(SOURCE, REMOTE_SOURCE)
    .add_local_file(REPLAY, REMOTE_REPLAY)
)


def digest(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024*1024), b""):
            result.update(block)
    return result.hexdigest()


@app.function(image=image, cpu=1.0, memory=2048, timeout=180)
def audit_remote():
    source = json.loads(Path(REMOTE_SOURCE).read_text())
    replay = json.loads(Path(REMOTE_REPLAY).read_text())

    def require(condition, message):
        if not condition:
            raise RuntimeError(message)

    require(source["schema"] ==
            "rate-half-kb-positive-433-1b-cell14-fixed-a-allmixed-v1",
            "source schema")
    require(source["field"] == PRIME, "field")
    require(source["case_count"] == 144 and source["unit_count"] == 144,
            "source census")
    expected = {
        (epsilon_1, epsilon_2, sigma_c, sigma_o, xi_index, pairing_index)
        for epsilon_1 in (-1, 1)
        for epsilon_2 in (-1, 1)
        for sigma_c in (-1, 1)
        for sigma_o in (-1, 1)
        for xi_index in range(3)
        for pairing_index in (6, 7, 8)
    }
    observed = {
        (*row["epsilon"], *row["sigma"], row["xi_index"], row["pairing_index"])
        for row in source["rows"]
    }
    require(observed == expected and len(source["rows"]) == len(expected),
            "Cartesian case ledger")

    counts = {
        "root_count": 0,
        "guard_boundary_count": 0,
        "checked_root_count": 0,
        "common_factor_root_count": 0,
        "factor_no_weight_root_count": 0,
        "factor_excluded_count": 0,
        "factor_weight_branch_count": 0,
        "factor_f_root_count": 0,
        "factor_boundary_solution_count": 0,
        "residual_outer_root_count": 0,
        "direct_fiber_count": 0,
        "target_boundary_count": 0,
    }
    maximum_eliminant_degree = 0
    maximum_eliminant_terms = 0
    for row in source["rows"]:
        key = (*row["epsilon"], *row["sigma"], row["xi_index"],
               row["pairing_index"])
        require(row["status"] == "COMPLETE", f"case status: {key}")
        require(row["unit"] and row["case_excluded"], f"case unit: {key}")
        require(not row["unresolved_roots"], f"unresolved root: {key}")
        require(row["field_root_gcd_degree"] == len(row["field_roots"]),
                f"field-root degree: {key}")
        roots = row["field_root_rows"]
        require([item["r"] for item in roots] == row["field_roots"],
                f"field-root order: {key}")
        profile = row["selected_profile"]
        require(profile["status"] == "NONZERO_SELECTED", f"profile: {key}")
        maximum_eliminant_degree = max(
            maximum_eliminant_degree, profile["outer_degree"]
        )
        maximum_eliminant_terms = max(
            maximum_eliminant_terms, profile["outer_terms"]
        )
        counts["root_count"] += len(roots)
        for root in roots:
            if root["status"] == "GUARD_BOUNDARY":
                require(root["zero_guards"] or root["denominator_guards"],
                        f"unexplained guard boundary: {key}, {root['r']}")
                counts["guard_boundary_count"] += 1
                continue
            require(root["status"] == "CHECKED",
                    f"unclassified root: {key}, {root['r']}")
            require(not root["clearing_boundaries"],
                    f"live coefficient-clearing boundary: {key}, {root['r']}")
            require(not root["zero_guards"] and not root["denominator_guards"],
                    f"live guard at checked root: {key}, {root['r']}")
            counts["checked_root_count"] += 1
            factor = root.get("common_factor_fiber")
            if factor is not None:
                counts["common_factor_root_count"] += 1
                require(not factor["witnesses"],
                        f"guarded factor witness: {key}, {root['r']}")
                require(factor["status"] in
                        ("EXCLUDED_NO_WEIGHT_ROOTS", "EXCLUDED"),
                        f"factor status: {key}, {root['r']}")
                if factor["status"] == "EXCLUDED_NO_WEIGHT_ROOTS":
                    counts["factor_no_weight_root_count"] += 1
                else:
                    counts["factor_excluded_count"] += 1
                    counts["factor_weight_branch_count"] += len(factor["branches"])
                    counts["factor_boundary_solution_count"] += factor[
                        "boundary_solution_count"
                    ]
                    for branch in factor["branches"]:
                        require(branch["status"] == "CHECKED",
                                f"factor branch: {key}, {root['r']}")
                        counts["factor_f_root_count"] += len(branch["f_roots"])
            outer_roots = root.get("outer_roots", [])
            counts["residual_outer_root_count"] += len(outer_roots)
            direct_rows = root.get("direct_rows", [])
            require(len(direct_rows) == len(outer_roots),
                    f"direct outer census: {key}, {root['r']}")
            for direct_row in direct_rows:
                direct = direct_row["direct"]
                require(direct["status"] == "CHECKED" and not direct["solutions"],
                        f"live direct fiber: {key}, {root['r']}")
                counts["direct_fiber_count"] += 1
                counts["target_boundary_count"] += len(
                    direct.get("target_boundaries", [])
                )

    require(replay["schema"] ==
            "rate-half-kb-positive-433-1b-cell14-allmixed-root-replay-v1",
            "replay schema")
    require(replay["status"] == "COMPLETE" and replay["case_count"] == 144,
            "replay census")
    require(replay["root_count"] == counts["root_count"], "replay roots")
    require(replay["source_sha256"] == digest(REMOTE_SOURCE), "replay custody")
    require(all(row["status"] == "COMPLETE" for row in replay["shards"]),
            "replay shard")
    return {
        "status": "PASS",
        "case_count": len(source["rows"]),
        **counts,
        "maximum_eliminant_degree": maximum_eliminant_degree,
        "maximum_eliminant_terms": maximum_eliminant_terms,
        "eliminant_bytes": replay["eliminant_bytes"],
        "recorded_compiler_sha256": source["source_script_sha256"],
        "recorded_replay_script_sha256": replay["source_script_sha256"],
    }


@app.local_entrypoint()
def main():
    payload = audit_remote.remote()
    payload.update({
        "schema": "rate-half-kb-positive-433-1b-cell14-allmixed-census-v1",
        "compiler_sha256": digest(COMPILER),
        "ledger_sha256": digest(SOURCE),
        "replay_script_sha256": digest(REPLAY_SCRIPT),
        "replay_sha256": digest(REPLAY),
        "source_script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    })
    if payload.pop("recorded_compiler_sha256") != payload["compiler_sha256"]:
        raise RuntimeError("compiler self-custody")
    if payload.pop("recorded_replay_script_sha256") != payload[
        "replay_script_sha256"
    ]:
        raise RuntimeError("replay self-custody")
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True)+"\n")
    print(json.dumps(payload, sort_keys=True))

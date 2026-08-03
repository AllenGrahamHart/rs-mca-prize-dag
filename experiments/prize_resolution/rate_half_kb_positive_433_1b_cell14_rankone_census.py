#!/usr/bin/env python3
"""Aggregate and audit the exact cell-14 rank-one exclusion ledger."""

import base64
from collections import Counter
import hashlib
import json
from pathlib import Path
import zlib


DIRECTORY = Path(__file__).parent
PROJECTION_SCRIPT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_target_projection_modal.py"
BOUNDARY_SCRIPT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_missing_ratio_boundary_modal.py"
BOUNDARY_RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_missing_ratio_boundary_result.json"
ROOT_REPLAY_SCRIPT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_rankone_root_replay_modal.py"
ROOT_REPLAY_RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_rankone_root_replay_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_rankone_census_result.json"
PRIME = 2130706433
SCHEMA = "rate-half-kb-positive-433-1b-cell14-target-projection-v1"
SIGNS = ((-1, -1), (-1, 1), (1, -1), (1, 1))
ROUTE_GUARDS = {
    "r", "t", "r2_minus_1", "r2_plus_1", "t2_minus_1", "t2_plus_1",
    "t2_minus_r2", "t2_plus_r2",
}

SHARDS = (
    {
        "name": "simple",
        "file": "rate_half_kb_positive_433_1b_cell14_rankone_simple_full_result.json",
        "branch": "rankone_resultant",
        "xi_indices": (3, 4),
        "pairing_indices": (0,),
        "count": 32,
        "blob": ("resultant_zlib_base64", "resultant_sha256"),
    },
    {
        "name": "df_chain",
        "file": "rate_half_kb_positive_433_1b_cell14_rankone_df_chain_full_result.json",
        "branch": "rankone_chain",
        "xi_indices": (3,),
        "pairing_indices": tuple(range(1, 15)),
        "count": 224,
        "blob": ("outer_zlib_base64", "outer_sha256"),
    },
    {
        "name": "ef_chain",
        "file": "rate_half_kb_positive_433_1b_cell14_rankone_ef_chain_full_result.json",
        "branch": "rankone_chain",
        "xi_indices": (4,),
        "pairing_indices": tuple(range(1, 15)),
        "count": 224,
        "blob": ("outer_zlib_base64", "outer_sha256"),
    },
    {
        "name": "bf_targetfree",
        "file": "rate_half_kb_positive_433_1b_cell14_rankone_bf_targetfree_full_result.json",
        "branch": "rankone_targetfree",
        "xi_indices": (5,),
        "pairing_indices": tuple(range(15)),
        "count": 240,
        "blob": ("polynomial_zlib_base64", "polynomial_sha256"),
    },
    {
        "name": "cf_targetfree",
        "file": "rate_half_kb_positive_433_1b_cell14_rankone_cf_targetfree_full_result.json",
        "branch": "rankone_targetfree",
        "xi_indices": (6,),
        "pairing_indices": tuple(range(15)),
        "count": 240,
        "blob": ("polynomial_zlib_base64", "polynomial_sha256"),
    },
)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


def expected_cases(specification):
    return {
        (epsilon, sigma, xi_index, pairing_index)
        for epsilon in SIGNS
        for sigma in SIGNS
        for xi_index in specification["xi_indices"]
        for pairing_index in specification["pairing_indices"]
    }


def audit_checked_root(branch, row):
    require(row["status"] in {
        "NO_ELIMINATION_ROOT", "PROJECTED_CHECKED", "CHECKED",
    }, "unsupported finite-root status")
    if row["status"] == "NO_ELIMINATION_ROOT":
        require(row.get("elimination_roots") == [], "nonempty elimination roots")
        return
    if branch == "rankone_resultant":
        require(row["status"] == "PROJECTED_CHECKED", "resultant root status")
        for solution in row["projected_solutions"]:
            direct = solution.get("direct_boundary")
            if direct is not None:
                require(direct.get("status") == "CHECKED", "direct boundary status")
                require(not direct.get("solutions"), "direct boundary solution")
                continue
            secondary_keys = [key for key in solution if key.endswith("_roots")]
            require(len(secondary_keys) == 1, "secondary-root key")
            require(solution[secondary_keys[0]] == [], "secondary target root")
        return
    require(row["status"] == "CHECKED", "direct root status")
    if branch == "rankone_chain":
        if "direct_unbounded" in row:
            direct = row["direct_unbounded"]
            require(direct.get("status") == "CHECKED", "unbounded status")
            require(not direct.get("solutions"), "unbounded solution")
        else:
            for item in row["direct_rows"]:
                direct = item["direct"]
                require(direct.get("status") == "CHECKED", "chain direct status")
                require(not direct.get("solutions"), "chain direct solution")
        return
    require(branch == "rankone_targetfree", "unknown direct branch")
    direct = row["direct"]
    require(direct.get("status") == "CHECKED", "target-free direct status")
    require(not direct.get("solutions"), "target-free direct solution")


def audit_shard(specification, projection_hash, curve_hash):
    path = DIRECTORY / specification["file"]
    payload = json.loads(path.read_text())
    require(payload["schema"] == SCHEMA, "projection schema")
    require(payload["field"] == PRIME, "projection field")
    require(payload["source_script_sha256"] == projection_hash, "projection source hash")
    require(payload["source_curve_sha256"] == curve_hash, "projection curve hash")
    require(payload["case_count"] == specification["count"], "shard case count")
    require(payload["unit_count"] == specification["count"], "shard unit count")
    require(payload["status_counts"] == {"COMPLETE": specification["count"]}, "status census")
    selection = payload["selection"]
    require(selection["branch"] == specification["branch"], "selection branch")
    require(tuple(selection["xi_indices"]) == specification["xi_indices"], "selection xi")
    require(tuple(selection["pairing_indices"]) == specification["pairing_indices"], "selection pairings")
    require({tuple(value) for value in selection["signs"]} == set(SIGNS), "source signs")
    require({tuple(value) for value in selection["lanes"]} == set(SIGNS), "target lanes")
    require(selection["factor_indices"] == [-1], "factor selection")

    cases = set()
    root_statuses = Counter()
    guard_sets = Counter()
    eliminant_hashes = set()
    total_roots = 0
    checked_roots = 0
    maximum_degree = 0
    maximum_terms = 0
    blob_key, blob_hash_key = specification["blob"]
    for row in payload["rows"]:
        require(row["branch"] == specification["branch"], "row branch")
        case = (
            tuple(row["epsilon"]), tuple(row["sigma"]),
            row["xi_index"], row["pairing_index"],
        )
        require(case not in cases, "duplicate case")
        cases.add(case)
        require(row["status"] == "COMPLETE", "row incomplete")
        require(row["unit"] and row["case_excluded"], "row not excluded")
        require(row["unresolved_roots"] == [], "unresolved root")

        eliminant = zlib.decompress(base64.b64decode(row[blob_key]))
        eliminant_hash = hashlib.sha256(eliminant).hexdigest()
        require(eliminant_hash == row[blob_hash_key], "eliminant hash")
        eliminant_hashes.add(eliminant_hash)
        if specification["branch"] == "rankone_resultant":
            require(row["resultant_nonzero"], "zero resultant")
            maximum_degree = max(maximum_degree, max(row["resultant_degrees"]))
            maximum_terms = max(maximum_terms, row["resultant_terms"])
        elif specification["branch"] == "rankone_chain":
            maximum_degree = max(maximum_degree, max(row["outer_degrees"]))
            maximum_terms = max(maximum_terms, row["outer_terms"])
        else:
            maximum_degree = max(maximum_degree, row["polynomial_degree"])
            maximum_terms = max(maximum_terms, row["polynomial_terms"])

        roots = row["field_roots"]
        require(roots == sorted(set(roots)), "field roots not unique")
        require(row["field_root_gcd_degree"] == len(roots), "field-root degree")
        root_rows = row["field_root_rows"]
        require([item["r"] for item in root_rows] == roots, "root-row coverage")
        total_roots += len(roots)
        for root_row in root_rows:
            root_statuses[root_row["status"]] += 1
            if root_row["status"] == "GUARD_BOUNDARY":
                guards = set(root_row["zero_guards"]+root_row["denominator_guards"])
                require(guards, "empty guard boundary")
                # inverse_3 is A(xi); its zero boundary is independently closed.
                require(bool(guards & ROUTE_GUARDS) or guards == {"inverse_3"}, "unsupported inverse boundary")
                guard_sets[tuple(sorted(guards))] += 1
            else:
                checked_roots += 1
                audit_checked_root(specification["branch"], root_row)

    require(cases == expected_cases(specification), "Cartesian case coverage")
    return {
        "name": specification["name"],
        "file": specification["file"],
        "file_sha256": sha256_file(path),
        "branch": specification["branch"],
        "case_count": len(cases),
        "unit_count": payload["unit_count"],
        "total_field_roots": total_roots,
        "checked_field_roots": checked_roots,
        "root_statuses": dict(sorted(root_statuses.items())),
        "guard_sets": {"|".join(key): value for key, value in sorted(guard_sets.items())},
        "distinct_eliminant_count": len(eliminant_hashes),
        "maximum_eliminant_degree": maximum_degree,
        "maximum_eliminant_terms": maximum_terms,
    }


def audit_boundary(curve_hash):
    payload = json.loads(BOUNDARY_RESULT.read_text())
    require(
        payload["schema"] == "rate-half-kb-positive-433-1b-cell14-missing-ratio-boundary-v1",
        "boundary schema",
    )
    require(payload["field"] == PRIME, "boundary field")
    require(payload["source_curve_sha256"] == curve_hash, "boundary curve hash")
    require(payload["source_script_sha256"] == sha256_file(BOUNDARY_SCRIPT), "boundary source hash")
    require(payload["case_count"] == 4 and payload["unit_count"] == 4, "boundary count")
    require({tuple(row["epsilon"]) for row in payload["rows"]} == set(SIGNS), "boundary signs")
    root_count = 0
    curve_leading_root_count = 0
    for row in payload["rows"]:
        require(row["status"] == "COMPLETE" and row["unit"], "boundary row")
        require(row["unresolved_roots"] == [], "boundary unresolved")
        require(row["field_root_gcd_degree"] == len(row["field_roots"]), "boundary root degree")
        require([item["r"] for item in row["field_root_rows"]] == row["field_roots"], "boundary roots")
        for root_row in row["field_root_rows"]:
            require(root_row["status"] == "ROUTE_BOUNDARY", "live ratio boundary")
            require(set(root_row["zero_guards"]) & ROUTE_GUARDS, "unsupported ratio boundary")
        root_count += len(row["field_roots"])
        leading_roots = row["curve_leading_field_roots"]
        require(
            row["curve_leading_field_root_gcd_degree"] == len(leading_roots),
            "curve-leading root degree",
        )
        require(
            [item["r"] for item in row["curve_leading_field_root_rows"]] == leading_roots,
            "curve-leading roots",
        )
        for root_row in row["curve_leading_field_root_rows"]:
            require(root_row["status"] == "ROUTE_BOUNDARY", "live curve-leading boundary")
            require(set(root_row["zero_guards"]) & ROUTE_GUARDS, "unsupported curve-leading boundary")
        curve_leading_root_count += len(leading_roots)
    return {
        "file": BOUNDARY_RESULT.name,
        "file_sha256": sha256_file(BOUNDARY_RESULT),
        "case_count": payload["case_count"],
        "unit_count": payload["unit_count"],
        "field_root_count": root_count,
        "curve_leading_field_root_count": curve_leading_root_count,
    }


def audit_root_replay():
    payload = json.loads(ROOT_REPLAY_RESULT.read_text())
    require(
        payload["schema"] == "rate-half-kb-positive-433-1b-cell14-rankone-root-replay-v1",
        "root-replay schema",
    )
    require(payload["field"] == PRIME, "root-replay field")
    require(payload["source_script_sha256"] == sha256_file(ROOT_REPLAY_SCRIPT),
            "root-replay source hash")
    require(payload["case_count"] == payload["pass_count"] == 960,
            "root-replay case count")
    require(payload["field_root_count"] == 12880, "root-replay root count")
    replay_shards = {row["name"]: row for row in payload["shards"]}
    require(set(replay_shards) == {row["name"] for row in SHARDS},
            "root-replay shard names")
    for specification in SHARDS:
        replay = replay_shards[specification["name"]]
        source_path = DIRECTORY / specification["file"]
        source = json.loads(source_path.read_text())
        require(replay["file"] == specification["file"], "root-replay file")
        require(replay["file_sha256"] == sha256_file(source_path),
                "root-replay file hash")
        expected = {}
        hash_key = specification["blob"][1]
        for row in source["rows"]:
            case = tuple((*row["epsilon"], *row["sigma"],
                          row["xi_index"], row["pairing_index"]))
            roots_text = json.dumps(row["field_roots"], separators=(",", ":"))
            expected[case] = (
                row[hash_key], len(row["field_roots"]),
                hashlib.sha256(roots_text.encode()).hexdigest(),
            )
        observed = {}
        for row in replay["rows"]:
            case = tuple(row["case"])
            require(case not in observed, "duplicate root-replay case")
            require(row["status"] == "PASS", "root-replay row status")
            require(len(row["field_gcd_sha256"]) == 64, "root-replay gcd hash")
            observed[case] = (
                row["eliminant_sha256"], row["field_root_count"],
                row["field_roots_sha256"],
            )
        require(observed == expected, "root-replay row cross-match")
        require(replay["case_count"] == replay["pass_count"] == len(expected),
                "root-replay shard count")
        require(replay["field_root_count"] ==
                sum(value[1] for value in expected.values()),
                "root-replay shard roots")
    return {
        "file": ROOT_REPLAY_RESULT.name,
        "file_sha256": sha256_file(ROOT_REPLAY_RESULT),
        "source_script_sha256": sha256_file(ROOT_REPLAY_SCRIPT),
        "case_count": payload["case_count"],
        "pass_count": payload["pass_count"],
        "field_root_count": payload["field_root_count"],
    }


def main():
    projection_hash = sha256_file(PROJECTION_SCRIPT)
    curve_path = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_curve_kernel_result.json"
    curve_hash = sha256_file(curve_path)
    shards = [audit_shard(specification, projection_hash, curve_hash) for specification in SHARDS]
    boundary = audit_boundary(curve_hash)
    root_replay = audit_root_replay()
    require(sum(row["case_count"] for row in shards) == 960, "total case count")
    payload = {
        "schema": "rate-half-kb-positive-433-1b-cell14-rankone-census-v1",
        "scope": "All retained cell-14 cases whose missing record is df, ef, bf, or cf.",
        "field": PRIME,
        "projection_script_sha256": projection_hash,
        "boundary_script_sha256": sha256_file(BOUNDARY_SCRIPT),
        "source_curve_sha256": curve_hash,
        "raw_cell_case_count": 1680,
        "prior_linear_pair_excluded_count": 144,
        "rankone_excluded_count": 960,
        "combined_excluded_count": 1104,
        "retained_case_count": 576,
        "shards": shards,
        "missing_ratio_boundary": boundary,
        "independent_root_replay": root_replay,
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT),
        "rankone_excluded_count": payload["rankone_excluded_count"],
        "combined_excluded_count": payload["combined_excluded_count"],
        "retained_case_count": payload["retained_case_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()

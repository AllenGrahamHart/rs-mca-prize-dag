#!/usr/bin/env python3
"""Verify the cell-3 xi5 finite-source pairing exclusion."""

import collections
import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
PRIMARY_SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi5_"
    "finite_source_pairing_solver_modal.py"
)
PRIMARY_RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi5_"
    "finite_source_pairing_solver_census_result.json"
)
AUDIT_SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi5_"
    "finite_source_pairing_audit_modal.py"
)
AUDIT_RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi5_"
    "finite_source_pairing_audit_census_result.json"
)
SOURCE = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi5_xi6_"
    "endpoint_compatibility_census_result.json"
)
KERNEL = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_compact_kernel_result.json"
)
PARENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell3_xi6_endpoint_compatibility_exclusion"
)
PINNED = {
    PRIMARY_SCRIPT: "059bebe72375f5adcb215aaf9a3fa41ba1ecf56e5078decf19f073b1a1cdef60",
    PRIMARY_RESULT: "bd5819475633a6f188635c2fefdd338cd1707db2249cb5e4276ef7687db248a2",
    AUDIT_SCRIPT: "10a830f0e2864393548e50e8705e2b2c8c3a408b32fbf7d38b47e9f19cb64401",
    AUDIT_RESULT: "fbdeb02f8baaa12af3c9240299eed49f932b24b9f0dde66fdf872fdc6b9d49c0",
}
SIGNS = set(itertools.product((-1, 1), repeat=2))
LANES = set(itertools.product((-1, 1), repeat=2))
PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_matchings(items):
    if not items:
        return ((),)
    output = []
    for index in range(1, len(items)):
        for tail in canonical_matchings(items[1:index]+items[index+1:]):
            output.append(((items[0], items[index]),)+tail)
    return tuple(output)


def source_ledger():
    payload = json.loads(SOURCE.read_text())
    require(
        payload["schema"] ==
        "rate-half-kb-positive-433-1b-cell3-xi5-xi6-"
        "endpoint-compatibility-source-census-v1",
        "source schema",
    )
    output = {}
    for row in payload["rows"]:
        if row["xi_index"] != 5:
            continue
        epsilon = tuple(row["epsilon"])
        compatible = row["direct_lift"]["compatible_source_points"]
        require(len(compatible) == 6, "six compatible sources")
        for index, source in enumerate(compatible):
            b_value = source["point"][2]
            f_value = source["signed_other"]
            require(
                b_value*f_value % PRIME == source["source_missing"] and
                pow(b_value+f_value, 2, PRIME) == source["source_sum"],
                "source endpoint replay",
            )
            output[epsilon, index] = source
    require(len(output) == 24, "24-source endpoint ledger")
    return output


def verify_primary(payload, sources, matchings):
    require(
        payload["schema"] ==
        "rate-half-kb-positive-433-1b-cell3-xi5-finite-source-"
        "pairing-census-v1",
        "primary schema",
    )
    require("no claim beyond the printed source rows" in payload["scope"],
            "primary scope")
    require(payload["source_census_sha256"] == digest(SOURCE),
            "primary source custody")
    require(payload["source_kernel_sha256"] == digest(KERNEL),
            "primary kernel custody")

    rows = {}
    root_profile = collections.Counter()
    selected_pairs = collections.Counter()
    total_pairings = total_outer = total_inner = 0
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), row["point_index"])
        require(key in sources and key not in rows, "primary source row")
        rows[key] = row
        require(row["source"] == sources[key], "primary source identity")
        require(
            row["status"] == "COMPLETE" and row["source_excluded"] and
            row["boundary_count"] == 0 and row["boundaries"] == [] and
            row["witness_count"] == 0 and row["witnesses"] == [] and
            row["unresolved_count"] == 0 and row["unresolved"] == [],
            "primary exclusion ledger",
        )
        lane_rows = row["lane_rows"]
        require(
            len(lane_rows) == 4 and
            {tuple(lane["sigma"]) for lane in lane_rows} == LANES,
            "four primary lanes",
        )
        row_outer = row_inner = 0
        for lane in lane_rows:
            pairing_rows = lane["pairing_rows"]
            require(
                len(pairing_rows) == 15 and
                {item["pairing_index"] for item in pairing_rows} == set(range(15)),
                "15 primary matchings",
            )
            for pairing in pairing_rows:
                index = pairing["pairing_index"]
                require(
                    pairing["matching"] == [list(value) for value in matchings[index]] and
                    pairing["status"] == "CHECKED" and
                    len(pairing["equation_profiles"]) == 3 and
                    all(not item["zero"] for item in pairing["equation_profiles"]) and
                    len(pairing["resultant_profiles"]) == 3 and
                    all(not item["zero"] for item in pairing["resultant_profiles"]) and
                    pairing["selected_resultant_degree"] == 8 and
                    pairing["u_roots"] == sorted(set(pairing["u_roots"])) and
                    len(pairing["fiber_rows"]) == len(pairing["u_roots"]),
                    "primary resultant row",
                )
                selected_pairs[tuple(pairing["selected_equations"])] += 1
                row_outer += len(pairing["u_roots"])
                for fiber in pairing["fiber_rows"]:
                    require(
                        fiber["status"] == "CHECKED" and
                        fiber["u"] in pairing["u_roots"] and
                        fiber["common_v_degree"] == 0 and
                        fiber["v_roots"] == [] and
                        fiber["solutions"] == [],
                        "constant primary fiber gcd",
                    )
                    row_inner += len(fiber["v_roots"])
                total_pairings += 1
        require(
            row["u_root_count"] == row_outer and
            row["v_root_count"] == row_inner == 0,
            "primary row root ledger",
        )
        root_profile[row_outer] += 1
        total_outer += row_outer
        total_inner += row_inner

    require(set(rows) == set(sources), "complete primary source ledger")
    require(total_pairings == 1440, "1440 primary subcases")
    require(total_outer == 2208 and total_inner == 0,
            "primary root aggregate")
    require(root_profile == collections.Counter({44: 8, 108: 8, 124: 8}),
            "primary per-source profile")
    require(selected_pairs == collections.Counter({
        (0, 1): 672, (0, 2): 672, (1, 2): 96,
    }), "primary selected-pair profile")
    return rows


def verify_audit(payload, sources, primary_rows):
    require(
        payload["schema"] ==
        "rate-half-kb-positive-433-1b-cell3-xi5-finite-source-"
        "pairing-dual-elimination-census-v1",
        "audit schema",
    )
    require("Independent u-elimination" in payload["scope"], "audit scope")
    require(payload["source_census_sha256"] == digest(SOURCE),
            "audit source custody")
    require(payload["source_kernel_sha256"] == digest(KERNEL),
            "audit kernel custody")

    rows = {}
    root_profile = collections.Counter()
    total_pairings = total_outer = total_inner = 0
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), row["point_index"])
        require(key in sources and key not in rows, "audit source row")
        rows[key] = row
        require(row["source"] == sources[key], "audit source identity")
        require(
            row["status"] == "COMPLETE" and row["source_excluded"] and
            row["solution_count"] == 0 and row["solutions"] == [] and
            row["unresolved_count"] == 0 and row["unresolved"] == [] and
            len(row["pairing_rows"]) == 60,
            "audit exclusion ledger",
        )
        keys = {
            (tuple(item["sigma"]), item["pairing_index"])
            for item in row["pairing_rows"]
        }
        require(keys == {(lane, index) for lane in LANES for index in range(15)},
                "audit matching/lane ledger")
        row_outer = row_inner = 0
        for pairing in row["pairing_rows"]:
            require(
                pairing["status"] == "CHECKED" and
                len(pairing["resultant_profiles"]) == 3 and
                all(not item["zero"] for item in pairing["resultant_profiles"]) and
                pairing["selected_resultant_degree"] == 8 and
                pairing["v_roots"] == sorted(set(pairing["v_roots"])) and
                len(pairing["fiber_rows"]) == len(pairing["v_roots"]),
                "audit resultant row",
            )
            row_outer += len(pairing["v_roots"])
            for fiber in pairing["fiber_rows"]:
                require(
                    fiber["status"] == "CHECKED" and
                    fiber["v"] in pairing["v_roots"] and
                    fiber["u_roots"] == [],
                    "empty audit fiber",
                )
                row_inner += len(fiber["u_roots"])
            total_pairings += 1
        require(
            row["v_root_count"] == row_outer ==
            primary_rows[key]["u_root_count"] and
            row["u_root_count"] == row_inner == 0,
            "dual row agreement",
        )
        root_profile[row_outer] += 1
        total_outer += row_outer
        total_inner += row_inner

    require(set(rows) == set(sources), "complete audit source ledger")
    require(total_pairings == 1440, "1440 audit subcases")
    require(total_outer == 2208 and total_inner == 0,
            "audit root aggregate")
    require(root_profile == collections.Counter({44: 8, 108: 8, 124: 8}),
            "audit per-source profile")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED",
            "DAG node")
    require(PARENT in nodes and nodes[PARENT]["status"] == "PROVED",
            "parent")
    edges = {(row["from"], row["to"], row["kind"])
             for row in dag["edges"]}
    require((PARENT, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")


def main():
    matchings = canonical_matchings(tuple(range(6)))
    require(len(matchings) == 15, "15 canonical matchings")
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    sources = source_ledger()
    primary_rows = verify_primary(
        json.loads(PRIMARY_RESULT.read_text()), sources, matchings
    )
    verify_audit(json.loads(AUDIT_RESULT.read_text()), sources, primary_rows)
    verify_dag()
    print(
        "cell=3 xi=5 sources=24 subcases=1440 "
        "primary_outer=2208 audit_outer=2208 inner_roots=0 raw_cases=240"
    )


if __name__ == "__main__":
    main()

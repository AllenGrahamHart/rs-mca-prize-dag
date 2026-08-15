#!/usr/bin/env python3
"""Verify the corank-three projective-basis kernel capacity cut."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "2cf4bca5b0dc130a84bbee61c0769a7a700f0f4f9eeac633d9c0b3c0936a2c76"
ROOT = Path(__file__).resolve().parents[3]
TREE = [(2, 4), (2, 5), (3, 6), (4, 7), (5, 8), (6, 9)]


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def ceil_fraction(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def record_cap(kprime: int, d: int, p: dict[str, object]) -> int:
    special = {
        1: int(p["projective_corank1_record_cap"]),
        2: int(p["projective_corank2_record_cap"]),
        3: int(p["projective_corank3_record_cap"]),
        9: int(p["rank9_record_cap"]),
    }
    if d in special:
        return special[d]
    rank = int(p["correction_dimension"]) - d
    shortened = kprime - rank
    n0, m0 = int(p["n_offset"]), int(p["m_offset"])
    return int(max(
        Fraction(
            falling(n0 + shortened, d + 1),
            (m0 + shortened) * rising(m0 + 1, d - 1),
        ),
        Fraction(falling(n0 + d, d + 1), rising(m0 + 1, d)),
    ))


def cap_data(kprime: int, p: dict[str, object]) -> tuple[list[Fraction], list[str]]:
    nprime = int(p["n_offset"]) + kprime
    mprime = int(p["m_offset"]) + kprime
    residual = int(p["residual_record_floor"])
    caps, branches = [], []
    for d in range(1, 10):
        extension = comb(kprime - 10, d + 1)
        ambient = Fraction(
            comb(nprime, 10 - d) * record_cap(kprime, d, p) * extension // (d + 2),
            residual,
        )
        support = Fraction(comb(mprime, 10 - d) * extension // (d + 2))
        caps.append(min(ambient, support))
        branches.append("ambient" if ambient <= support else "record")
    return caps, branches


def raising(kprime: int, step: int, source: int, p: dict[str, object]) -> Fraction:
    return Fraction(
        comb(source + 2, step) * comb(int(p["m_offset"]) + source, step),
        comb(kprime - source - 11 + step, step),
    )


def multiplicity(step: int, source: int) -> int:
    return comb(9 - source + step, step)


def certificate(kprime: int, p: dict[str, object]) -> dict[str, object]:
    caps, branches = cap_data(kprime, p)
    parent = {source: (step, source) for step, source in TREE}
    children: dict[int, list[tuple[int, int]]] = {d: [] for d in range(1, 10)}
    for step, source in TREE:
        children[source - step].append((step, source))

    factors = [Fraction(0) for _ in range(9)]
    roots = [0 for _ in range(9)]
    for root in (1, 2, 3):
        factors[root - 1] = Fraction(1)
        roots[root - 1] = root
    for source in range(4, 10):
        step, _ = parent[source]
        target = source - step
        factors[source - 1] = (
            multiplicity(step, source)
            * factors[target - 1]
            / raising(kprime, step, source, p)
        )
        roots[source - 1] = roots[target - 1]
    allocation = [factors[i] * caps[roots[i] - 1] for i in range(9)]

    hierarchy_dual: dict[tuple[int, int], Fraction] = {}
    for source in range(9, 3, -1):
        edge = parent[source]
        child_charge = sum(
            multiplicity(*child) * hierarchy_dual[child]
            for child in children[source]
        )
        hierarchy_dual[edge] = (1 + child_charge) / raising(kprime, *edge, p)
    cap_dual = {
        root: 1 + sum(
            multiplicity(*child) * hierarchy_dual[child]
            for child in children[root]
        )
        for root in (1, 2, 3)
    }
    optimum = sum(allocation, Fraction(0))
    require(
        optimum == sum(cap_dual[root] * caps[root - 1] for root in (1, 2, 3)),
        "duality",
    )
    require(all(value > 0 for value in hierarchy_dual.values()), "edge dual signs")
    require(all(value > 0 for value in cap_dual.values()), "cap dual signs")
    require(branches[:3] == ["ambient", "ambient", "ambient"], "active branches")
    require(all(0 < value <= cap for value, cap in zip(allocation, caps)), "individual caps")
    require(allocation[:3] == caps[:3], "root caps")
    require(all(allocation[i] < caps[i] for i in range(3, 9)), "nonroot caps")

    mprime = int(p["m_offset"]) + kprime
    shadow = [Fraction(comb(d + 2, 2), comb(kprime - d - 9, 2)) for d in range(1, 10)]
    require(sum(shadow[i] * allocation[i] for i in range(9)) < comb(mprime, 9), "nine-shadow")
    e0 = comb(mprime - 9, 2)
    containment = [
        52 + Fraction(3 * e0, comb(kprime - 10, 2)),
        55 + Fraction(6 * comb(67474, 2), comb(kprime - 11, 2)),
        *[Fraction(55) for _ in range(7)],
    ]
    require(
        sum(containment[i] * allocation[i] for i in range(9)) < e0 * comb(mprime, 9),
        "containment",
    )

    tight = []
    for step in range(2, 9):
        for source in range(step + 1, 10):
            left = raising(kprime, step, source, p) * allocation[source - 1]
            right = multiplicity(step, source) * allocation[source - step - 1]
            require(left <= right, "hierarchy")
            if left == right:
                tight.append([step, source])

    demand = Fraction(
        int(p["lane_density_numerator"]) * comb(mprime, 11),
        int(p["lane_density_denominator"]),
    )
    integer_demand = ceil_fraction(int(p["residual_record_floor"]) * demand)
    scaled_capacity = int(p["residual_record_floor"]) * optimum
    integer_capacity = scaled_capacity.numerator // scaled_capacity.denominator
    return {
        "optimum_numerator": optimum.numerator,
        "optimum_denominator": optimum.denominator,
        "integer_demand": integer_demand,
        "integer_capacity": integer_capacity,
        "signed_gap": integer_demand - integer_capacity,
        "tight": tight,
    }


def expected_row(p: dict[str, object], prefix: str, wall: bool = False) -> dict[str, object]:
    signed_gap = -int(p["wall_excess"]) if wall else int(p[f"{prefix}_gap"])
    return {
        "optimum_numerator": int(p[f"{prefix}_optimum_numerator"]),
        "optimum_denominator": int(p[f"{prefix}_optimum_denominator"]),
        "integer_demand": int(p[f"{prefix}_demand_ceiling"]),
        "integer_capacity": int(p[f"{prefix}_capacity"]),
        "signed_gap": signed_gap,
        "tight": p["tight_hierarchy_rows"],
    }


def verify_result(data: dict[str, object], p: dict[str, object]) -> None:
    evidence = data["evidence"]
    script = ROOT / str(evidence["script"])
    result_path = ROOT / str(evidence["result"])
    require(hashlib.sha256(script.read_bytes()).hexdigest() == evidence["script_sha256"], "script hash")
    require(hashlib.sha256(result_path.read_bytes()).hexdigest() == evidence["result_sha256"], "result hash")
    result = json.loads(result_path.read_text())
    require(result["schema"] == evidence["result_schema"], "result schema")
    require(result["complete"] is True and result["error"] is None, "result completion")
    require(result["script_sha256"] == evidence["script_sha256"], "embedded script hash")
    require(result["expected_chunks"] == result["completed_chunks"] == evidence["expected_chunks"], "chunks")
    require(result["checked_rows"] == p["checked_rows_including_wall"], "checked rows")
    require(result["interval"] == [p["replay_minimum"], p["closed_dimension_maximum"], p["first_open_dimension"]], "interval")
    require(result["record_cap_M1"] == p["projective_corank1_record_cap"], "result M1")
    require(result["record_cap_M2"] == p["projective_corank2_record_cap"], "result M2")
    require(result["record_cap_M3"] == p["projective_corank3_record_cap"], "result M3")
    require(0 < result["peak_mb"] <= evidence["worker_memory_mb"], "worker memory")
    require(result["peak_mb"] == evidence["observed_peak_mb"], "observed peak")

    cursor = int(p["replay_minimum"])
    embedded_endpoints = []
    for chunk in sorted(result["chunks"], key=lambda item: item["start"]):
        require(chunk["start"] == cursor and chunk["end"] > chunk["start"], "chunk coverage")
        require(chunk["checked"] == chunk["end"] - chunk["start"], "chunk count")
        require(0 < chunk["peak_mb"] <= evidence["worker_memory_mb"], "chunk memory")
        cursor = chunk["end"]
        embedded_endpoints.extend(chunk["endpoint_rows"])
    require(cursor == int(p["first_open_dimension"]) + 1, "coverage endpoint")
    require(sorted(embedded_endpoints, key=lambda item: item["kprime"]) == result["endpoint_rows"], "endpoint custody")

    expected = {
        int(p["replay_minimum"]): expected_row(p, "replay_start"),
        int(p["closed_dimension_maximum"]): expected_row(p, "endpoint"),
        int(p["first_open_dimension"]): expected_row(p, "wall", True),
    }
    require([row["kprime"] for row in result["endpoint_rows"]] == sorted(expected), "endpoint keys")
    for row in result["endpoint_rows"]:
        observed = {key: row[key] for key in expected[row["kprime"]]}
        require(observed == expected[row["kprime"]], "endpoint row")


def validate(data: object, files: bool) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-corank3-projective-capacity-cut-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_corank2_projective_capacity_cut",
        "rate_half_mca_rank11_kernel_corank3_uniform_projective_basis_cap",
        "rate_half_mca_rank11_kernel_multistep_shadow_hierarchy",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["n_offset"], p["m_offset"], p["residual_record_floor"]) == (
        1048576, 67472, 274980728111260126
    ), "base parameters")
    require((p["projective_corank1_record_cap"], p["projective_corank2_record_cap"], p["projective_corank3_record_cap"]) == (
        8147918, 84416263, 983902549
    ), "projective caps")
    require((p["previous_closed_maximum"], p["replay_minimum"], p["closed_dimension_maximum"], p["first_open_dimension"]) == (
        568338, 568339, 796598, 796599
    ), "cut interval")
    require(p["checked_rows_including_wall"] == p["first_open_dimension"] - p["replay_minimum"] + 1 == 228261, "row count")
    require(p["active_individual_caps"] == [1, 2, 3], "active caps")
    require(p["active_individual_cap_branches"] == ["ambient", "ambient", "ambient"], "active branches")
    require(p["active_shared_resources"] == [], "shared active")
    require(p["dual_forest"] == [list(edge) for edge in TREE], "dual forest")
    require(len(p["tight_hierarchy_rows"]) == 12, "tight rows")

    endpoints = (
        (int(p["replay_minimum"]), expected_row(p, "replay_start")),
        (int(p["closed_dimension_maximum"]), expected_row(p, "endpoint")),
        (int(p["first_open_dimension"]), expected_row(p, "wall", True)),
    )
    for kprime, expected in endpoints:
        require(certificate(kprime, p) == expected, f"certificate {kprime}")
    require(int(p["replay_start_gap"]) > 0 and int(p["endpoint_gap"]) > 0, "closed signs")
    require(int(p["wall_excess"]) > 0, "wall sign")
    require("conditional" in str(data.get("nonclaim")).lower(), "nonclaim")
    if files:
        verify_result(data, p)
    return {"checked": int(p["checked_rows_including_wall"]), "wall": int(p["first_open_dimension"])}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data, True)
    mutations = (
        lambda item: item["parameters"].__setitem__("projective_corank3_record_cap", item["parameters"]["projective_corank3_record_cap"] + 1),
        lambda item: item["parameters"].__setitem__("replay_minimum", item["parameters"]["replay_minimum"] + 1),
        lambda item: item["parameters"].__setitem__("closed_dimension_maximum", item["parameters"]["closed_dimension_maximum"] - 1),
        lambda item: item["parameters"]["active_individual_caps"].pop(),
        lambda item: item["parameters"]["dual_forest"].pop(),
        lambda item: item["parameters"]["tight_hierarchy_rows"].pop(),
        lambda item: item["parameters"].__setitem__("endpoint_gap", item["parameters"]["endpoint_gap"] + 1),
        lambda item: item["parameters"].__setitem__("wall_excess", item["parameters"]["wall_excess"] - 1),
    )
    caught = 0
    for mutation in mutations:
        altered = copy.deepcopy(data)
        mutation(altered)
        try:
            validate(altered, False)
        except (Reject, KeyError, TypeError, ValueError, ZeroDivisionError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_CORANK3_PROJECTIVE_CAPACITY_CUT_PASS "
        f"checked={result['checked']} wall={result['wall']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()

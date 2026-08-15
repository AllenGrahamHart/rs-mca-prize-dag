#!/usr/bin/env python3
"""Verify the exact projective-pair kernel capacity interval."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "05df2ec3f8cb69275a1aa0b4d0295ad82621e9ad6792dd2a70edf27cf6684156"
ROOT = Path(__file__).resolve().parents[3]


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def record_cap(p: dict[str, int], kprime: int, d: int) -> int:
    if d == 1:
        return p["projective_corank1_record_cap"]
    if d == 9:
        return p["rank9_record_cap"]
    rank = p["correction_dimension"] - d
    shortened = kprime - rank
    first = Fraction(
        falling(p["n_offset"] + shortened, d + 1),
        (p["m_offset"] + shortened) * rising(p["m_offset"] + 1, d - 1),
    )
    second = Fraction(
        falling(p["n_offset"] + d, d + 1),
        rising(p["m_offset"] + 1, d),
    )
    return int(max(first, second))


def cap_data(p: dict[str, int], kprime: int) -> tuple[list[Fraction], list[str]]:
    nprime, mprime = p["n_offset"] + kprime, p["m_offset"] + kprime
    caps, branches = [], []
    for d in range(1, 10):
        extension = comb(kprime - 10, d + 1)
        ambient = Fraction(
            comb(nprime, 10 - d) * record_cap(p, kprime, d) * extension // (d + 2),
            p["residual_record_floor"],
        )
        support = Fraction(comb(mprime, 10 - d) * extension // (d + 2))
        caps.append(min(ambient, support))
        branches.append("ambient" if ambient <= support else "record")
    return caps, branches


def raising(p: dict[str, int], kprime: int, step: int, source: int) -> Fraction:
    return Fraction(
        comb(source + 2, step) * comb(p["m_offset"] + source, step),
        comb(kprime - source - 11 + step, step),
    )


def multiplicity(step: int, source: int) -> int:
    return comb(9 - source + step, step)


def certificate(p: dict[str, object], kprime: int) -> tuple[Fraction, list[str], list[list[int]]]:
    caps, branches = cap_data(p, kprime)
    tree = [tuple(edge) for edge in p["dual_tree"]]
    parent = {source: (step, source) for step, source in tree}
    children: dict[int, list[tuple[int, int]]] = {d: [] for d in range(1, 10)}
    for step, source in tree:
        children[source - step].append((step, source))

    factors = [Fraction(0) for _ in range(9)]
    roots = [0 for _ in range(9)]
    factors[0] = factors[1] = Fraction(1)
    roots[0], roots[1] = 1, 2
    for source in range(3, 10):
        require(source in parent, f"tree source {source}")
        step, _ = parent[source]
        target = source - step
        require(roots[target - 1] != 0, f"tree order {source}")
        factors[source - 1] = (
            multiplicity(step, source)
            * factors[target - 1]
            / raising(p, kprime, step, source)
        )
        roots[source - 1] = roots[target - 1]
    require(roots == [1, 2, 1, 1, 1, 1, 1, 1, 1], f"roots K={kprime}")
    allocation = [factors[index] * caps[roots[index] - 1] for index in range(9)]

    dual: dict[tuple[int, int], Fraction] = {}
    for source in range(9, 2, -1):
        edge = parent[source]
        child_charge = sum(
            multiplicity(*child) * dual[child]
            for child in children[source]
        )
        dual[edge] = (1 + child_charge) / raising(p, kprime, *edge)
    cap_dual = {
        root: 1 + sum(multiplicity(*child) * dual[child] for child in children[root])
        for root in (1, 2)
    }

    require(all(value > 0 for value in allocation), f"positive allocation K={kprime}")
    require(all(value <= cap for value, cap in zip(allocation, caps)), f"individual caps K={kprime}")
    require(allocation[0] == caps[0] and allocation[1] == caps[1], f"root caps K={kprime}")
    require(all(allocation[index] < caps[index] for index in range(2, 9)), f"nonroot caps K={kprime}")
    require(branches[:2] == p["active_individual_cap_branches"], f"root branches K={kprime}")

    mprime = p["m_offset"] + kprime
    shadow = [Fraction(comb(d + 2, 2), comb(kprime - d - 9, 2)) for d in range(1, 10)]
    shadow_budget = Fraction(comb(mprime, p["shadow_subset_size"]))
    require(sum(shadow[i] * allocation[i] for i in range(9)) < shadow_budget, f"shadow slack K={kprime}")
    e0 = comb(mprime - p["shadow_subset_size"], 2)
    containment = [
        52 + Fraction(3 * e0, comb(kprime - 10, 2)),
        55 + Fraction(6 * p["rank8_independent_pair_floor"], comb(kprime - 11, 2)),
        *[Fraction(55) for _ in range(7)],
    ]
    require(
        sum(containment[i] * allocation[i] for i in range(9)) < e0 * shadow_budget,
        f"containment slack K={kprime}",
    )

    tight = []
    for step in range(2, 9):
        for source in range(step + 1, 10):
            left = raising(p, kprime, step, source) * allocation[source - 1]
            right = multiplicity(step, source) * allocation[source - step - 1]
            require(left <= right, f"hierarchy t={step} d={source} K={kprime}")
            if left == right:
                tight.append([step, source])
    require(tight == p["tight_hierarchy_rows"], f"tight rows K={kprime}")
    require(all(value > 0 for value in dual.values()), f"tree dual signs K={kprime}")
    require(all(value > 0 for value in cap_dual.values()), f"cap dual signs K={kprime}")
    optimum = sum(allocation, Fraction(0))
    require(optimum == cap_dual[1] * caps[0] + cap_dual[2] * caps[1], f"strong duality K={kprime}")
    return optimum, branches, tight


def demand_ratio(p: dict[str, int], kprime: int) -> Fraction:
    return Fraction(
        p["lane_density_numerator"] * comb(p["m_offset"] + kprime, p["component_subset_size"]),
        p["lane_density_denominator"],
    )


def integer_values(p: dict[str, int], kprime: int, optimum: Fraction) -> tuple[int, int]:
    demand = p["residual_record_floor"] * demand_ratio(p, kprime)
    capacity = p["residual_record_floor"] * optimum
    return -(-demand.numerator // demand.denominator), capacity.numerator // capacity.denominator


def check_named_row(p: dict[str, object], prefix: str, kprime: int) -> dict[str, object]:
    optimum, _, tight = certificate(p, kprime)
    require(optimum == Fraction(p[f"{prefix}_optimum_numerator"], p[f"{prefix}_optimum_denominator"]), f"{prefix} optimum")
    demand, capacity = integer_values(p, kprime, optimum)
    expected_gap = p["wall_excess"] if prefix == "wall" else p[f"{prefix}_gap"]
    actual_gap = capacity - demand if prefix == "wall" else demand - capacity
    require(demand == p[f"{prefix}_demand_ceiling"], f"{prefix} demand")
    require(capacity == p[f"{prefix}_capacity"], f"{prefix} capacity")
    require(actual_gap == expected_gap > 0, f"{prefix} sign")
    return {
        "kprime": kprime,
        "optimum_numerator": optimum.numerator,
        "optimum_denominator": optimum.denominator,
        "integer_demand": demand,
        "integer_capacity": capacity,
        "signed_gap": demand - capacity,
        "tight": tight,
    }


def validate_evidence(data: dict[str, object], expected_rows: list[dict[str, object]]) -> dict[str, object]:
    p, evidence = data["parameters"], data["evidence"]
    script = ROOT / evidence["script"]
    result_path = ROOT / evidence["result"]
    require(hashlib.sha256(script.read_bytes()).hexdigest() == evidence["script_sha256"], "script hash")
    require(hashlib.sha256(result_path.read_bytes()).hexdigest() == evidence["result_sha256"], "result hash")
    result = json.loads(result_path.read_text())
    require(result.get("schema") == evidence["result_schema"], "result schema")
    require(result.get("complete") is True and result.get("error") is None, "complete result")
    require(result.get("script_sha256") == evidence["script_sha256"], "embedded script hash")
    require(result.get("interval") == [p["replay_minimum"], p["closed_dimension_maximum"], p["first_open_dimension"]], "result interval")
    require(result.get("record_cap_M1") == p["projective_corank1_record_cap"], "result cap")
    require(result.get("tree") == p["dual_tree"], "result tree")
    require(result.get("expected_chunks") == evidence["expected_chunks"], "expected chunks")
    require(result.get("completed_chunks") == evidence["expected_chunks"], "completed chunks")
    require(result.get("checked_rows") == p["checked_rows_including_wall"], "checked rows")
    require(result.get("peak_mb") == evidence["observed_peak_mb"] <= evidence["worker_memory_mb"], "peak memory")
    require(result.get("endpoint_rows") == expected_rows, "endpoint rows")

    cursor = p["replay_minimum"]
    checked = 0
    chunks = result.get("chunks")
    require(isinstance(chunks, list) and len(chunks) == evidence["expected_chunks"], "chunk ledger")
    for chunk in chunks:
        require(chunk["start"] == cursor and chunk["end"] > chunk["start"], "chunk continuity")
        require(chunk["checked"] == chunk["end"] - chunk["start"], "chunk count")
        require(0 <= chunk["seconds"] < evidence["worker_timeout_seconds"], "worker timeout")
        require(0 < chunk["peak_mb"] <= evidence["worker_memory_mb"], "worker memory")
        cursor = chunk["end"]
        checked += chunk["checked"]
    require(cursor == p["first_open_dimension"] + 1, "chunk endpoint")
    require(checked == p["checked_rows_including_wall"], "chunk total")
    return result


def validate(data: object, check_evidence: bool = True) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-projective-pair-capacity-cut-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_three_step_shadow_capacity_cut",
        "rate_half_mca_rank11_kernel_projective_paving_integer_gap_fence",
        "rate_half_mca_rank11_kernel_multistep_shadow_hierarchy",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["previous_closed_maximum"], p["replay_minimum"], p["closed_dimension_maximum"], p["first_open_dimension"]) == (18158, 18159, 377673, 377674), "interval")
    require(p["checked_rows_including_wall"] == p["first_open_dimension"] - p["replay_minimum"] + 1, "row count")
    require(p["projective_corank1_record_cap"] == 8147918, "projective cap")
    require(p["active_individual_caps"] == [1, 2], "active caps")
    require(p["active_shared_resources"] == [], "active shared resources")
    require(p["slack_shared_resources"] == ["rank_preserving_nine_shadow", "full_containment"], "slack resources")
    require(p["positive_coranks"] == list(range(1, 10)), "positive coranks")
    require(p["dual_tree"] == [[2, 3], [3, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9]], "dual tree")
    require(len(p["tight_hierarchy_rows"]) == 22, "tight row count")

    rows = [
        check_named_row(p, "replay_start", p["replay_minimum"]),
        check_named_row(p, "endpoint", p["closed_dimension_maximum"]),
        check_named_row(p, "wall", p["first_open_dimension"]),
    ]
    if check_evidence:
        validate_evidence(data, rows)
    require("remains open" in str(data.get("nonclaim")), "nonclaim")
    return {
        "gap": p["endpoint_gap"],
        "wall": p["wall_excess"],
        "rows": p["checked_rows_including_wall"],
    }


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("closed_dimension_maximum", 377674),
        lambda item: item["parameters"].__setitem__("projective_corank1_record_cap", 8147919),
        lambda item: item["parameters"]["dual_tree"].pop(),
        lambda item: item["parameters"]["tight_hierarchy_rows"].pop(),
        lambda item: item["parameters"].__setitem__("endpoint_gap", item["parameters"]["endpoint_gap"] - 1),
        lambda item: item["parameters"].__setitem__("wall_excess", item["parameters"]["wall_excess"] - 1),
    )
    caught = 0
    for mutation in mutations:
        altered = copy.deepcopy(data)
        mutation(altered)
        try:
            validate(altered, check_evidence=False)
        except (Reject, KeyError, TypeError, ValueError, ZeroDivisionError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_PROJECTIVE_PAIR_CAPACITY_CUT_PASS "
        f"checked={result['rows']} endpoint_gap={result['gap']} wall_excess={result['wall']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()

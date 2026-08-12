#!/usr/bin/env python3
"""Verify the support-wise affine-span MCA compiler."""

from __future__ import annotations

import copy
import hashlib
import itertools
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "79c81b807ab3e176fdedff84a8cb2d204a8236fff2b001738c826488ce7d46c6"
CONTROL = HERE.parent / "rate_half_mca_record_local_core_owner_noninvariance" / "source_contract.json"
CONTROL_SHA256 = "7a27aef1521b42bc9704c97345be34263e8b22980b5e7fd65f84560b92ff6c94"


class Reject(ValueError):
    pass


def trim(poly: list[int], p: int) -> tuple[int, ...]:
    out = [value % p for value in poly]
    while out and out[-1] == 0:
        out.pop()
    return tuple(out)


def evaluate(poly: tuple[int, ...], x: int, p: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def rank_mod(matrix: list[list[int]], p: int) -> int:
    rows = [row[:] for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next(
            (index for index in range(rank, len(rows)) if rows[index][column] % p),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, p)
        rows[rank] = [(inverse * value) % p for value in rows[rank]]
        for index in range(len(rows)):
            if index == rank:
                continue
            factor = rows[index][column]
            rows[index] = [
                (left - factor * right) % p
                for left, right in zip(rows[index], rows[rank])
            ]
        rank += 1
        if rank == len(rows):
            break
    return rank


def solve_interpolant(
    points: tuple[int, ...], values: tuple[int, ...], p: int
) -> tuple[int, ...]:
    size = len(points)
    matrix = [
        [pow(x, j, p) for j in range(size)] + [value % p]
        for x, value in zip(points, values)
    ]
    for column in range(size):
        pivot = next(row for row in range(column, size) if matrix[row][column] % p)
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        inverse = pow(matrix[column][column], -1, p)
        matrix[column] = [(inverse * value) % p for value in matrix[column]]
        for row in range(size):
            if row == column:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                (left - factor * right) % p
                for left, right in zip(matrix[row], matrix[column])
            ]
    coefficients = [matrix[row][-1] for row in range(size)]
    return trim(coefficients, p)


def divide_by_root(poly: tuple[int, ...], root: int, p: int) -> tuple[int, ...]:
    if evaluate(poly, root, p):
        raise Reject("root division")
    descending = list(reversed(poly))
    quotient_desc = [descending[0]]
    for coefficient in descending[1:-1]:
        quotient_desc.append((coefficient + root * quotient_desc[-1]) % p)
    remainder = (descending[-1] + root * quotient_desc[-1]) % p
    if remainder:
        raise Reject("division remainder")
    return trim(list(reversed(quotient_desc)), p)


def falling(value: int, count: int) -> int:
    return math.prod(value - index for index in range(count))


def rising(value: int, count: int) -> int:
    return math.prod(value + index for index in range(count))


def j_value(reserve: int, defect: int, s: int) -> int:
    return math.prod(reserve + index for index in range(s + 1)) // math.prod(
        defect + index for index in range(s + 1)
    )


def validate(contract: object, control: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {
        "schema",
        "source",
        "theorem",
        "gf11_control",
        "deployed_boundaries",
    }:
        raise Reject("contract schema")
    if contract["schema"] != "rate-half-mca-supportwise-affine-span-compiler-v1":
        raise Reject("schema")
    if contract["source"] != {
        "upstream_pr": 1163,
        "upstream_head": "e26c15b2d2c2f98ae12dda17b97c40981f76e1ff",
        "source_theorem": "grande_finale.tex thm:affine-span-mca",
        "replacement_hypothesis": "exact same-support pair noncontainment for every counted slope",
        "whole_line_router_node": "rate_half_mca_whole_line_global_core_router",
    }:
        raise Reject("source")
    if contract["theorem"] != {
        "agreement": "m=K+w with w>=1",
        "affine_explanation_dimension": "s>=1",
        "old_hypothesis_removed": "max_c agr(r_1,c)<m",
        "rank_failure_conclusion": "the selected support is pair-contained",
        "bound": "floor(max(n_fall_(s+1)/(m*w_rise_s),(n-K+s)_fall_(s+1)/w_rise_(s+1)))",
    }:
        raise Reject("theorem")
    if not isinstance(control, dict):
        raise Reject("control")

    p = control["field"]
    domain = tuple(control["domain"])
    u = tuple(control["received_line"]["u"])
    v = tuple(control["received_line"]["v"])
    explanations = {item["slope"]: item for item in control["explanations"]}
    selected = tuple(sorted(explanations))
    root = 10
    shortened_domain = tuple(x for x in domain if x != root)
    shortened_u = tuple(
        (u[i] - u[-1]) * pow((x - root) % p, -1, p) % p
        for i, x in enumerate(shortened_domain)
    )
    shortened_v = tuple(
        (v[i] - v[-1]) * pow((x - root) % p, -1, p) % p
        for i, x in enumerate(shortened_domain)
    )
    K, m, s, w = 4, 6, 4, 2
    ranks = []
    for slope in selected:
        item = explanations[slope]
        source_poly = list(item["coefficients"])
        source_poly[0] = (source_poly[0] - u[-1] - slope * v[-1]) % p
        quotient = divide_by_root(tuple(source_poly), root, p)
        support = tuple(x for x in item["maximal_support"] if x != root)
        word = tuple((a + slope * b) % p for a, b in zip(shortened_u, shortened_v))
        if tuple(
            x
            for x, value in zip(shortened_domain, word)
            if evaluate(quotient, x, p) == value
        ) != support:
            raise Reject("shortened support")
        normals = [
            [shortened_v[shortened_domain.index(x)]]
            + [(-pow(x, degree, p)) % p for degree in range(s)]
            for x in support
        ]
        ranks.append(rank_mod(normals, p))
    gf11 = contract["gf11_control"]
    if gf11 != {
        "shortened_n": 9,
        "shortened_K": 4,
        "shortened_m": 6,
        "w": 2,
        "affine_dimension": 4,
        "parameter_dimension": 5,
        "slopes": 7,
        "direction_max_agreement": 6,
        "direction_separation_fails": True,
        "minimum_incident_normal_rank": 5,
        "J_4": 21,
    } or min(ranks) != gf11["minimum_incident_normal_rank"]:
        raise Reject("GF11 rank control")

    best = 0
    for support in itertools.combinations(shortened_domain, K):
        indices = tuple(shortened_domain.index(x) for x in support)
        candidate = solve_interpolant(support, tuple(shortened_v[i] for i in indices), p)
        best = max(
            best,
            sum(
                evaluate(candidate, x, p) == value
                for x, value in zip(shortened_domain, shortened_v)
            ),
        )
    if best != gf11["direction_max_agreement"] or best < m:
        raise Reject("direction-list control")
    term1 = falling(9, s + 1) // (m * rising(w, s))
    term2 = falling(9 - K + s, s + 1) // rising(w, s + 1)
    if term1 != term2 or term1 != gf11["J_4"] or len(selected) > term1:
        raise Reject("GF11 bound")

    rows = contract["deployed_boundaries"]
    if not isinstance(rows, list) or len(rows) != 2:
        raise Reject("deployed rows")
    expected = {
        "KoalaBear MCA": (1048576, 67472, 274980728111395087, 13, 47876303026096432, 14, 743896698428332665),
        "Mersenne-31 MCA": (1048576, 67448, 16777215, 5, 14115447, 6, 219426634),
    }
    for row in rows:
        name = row["row"]
        values = (
            row["R"],
            row["d"],
            row["B_star"],
            row["last_paid_s"],
            row["J_last"],
            row["first_unpaid_s"],
            row["J_first_unpaid"],
        )
        if values != expected.get(name):
            raise Reject("row constants")
        reserve, defect, budget, paid_s, paid, unpaid_s, unpaid = values
        if (
            j_value(reserve, defect, paid_s) != paid
            or j_value(reserve, defect, unpaid_s) != unpaid
            or not paid <= budget < unpaid
            or unpaid_s != paid_s + 1
        ):
            raise Reject("row boundary")
    return {"slopes": len(selected), "min_rank": min(ranks), "direction_max": best}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    if hashlib.sha256(CONTROL.read_bytes()).hexdigest() != CONTROL_SHA256:
        raise Reject("control hash")
    contract = json.loads(CONTRACT.read_text())
    control = json.loads(CONTROL.read_text())
    result = validate(contract, control)
    cases = []
    changed = copy.deepcopy(contract)
    changed["theorem"]["old_hypothesis_removed"] = "retained"
    cases.append(changed)
    changed = copy.deepcopy(contract)
    changed["gf11_control"]["minimum_incident_normal_rank"] = 4
    cases.append(changed)
    changed = copy.deepcopy(contract)
    changed["deployed_boundaries"][0]["J_last"] += 1
    cases.append(changed)
    changed = copy.deepcopy(contract)
    changed["deployed_boundaries"][1]["first_unpaid_s"] = 7
    cases.append(changed)
    caught = 0
    for changed in cases:
        try:
            validate(changed, control)
        except Reject:
            caught += 1
    if caught != len(cases):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_SUPPORTWISE_AFFINE_SPAN_COMPILER_PASS "
        f"slopes={result['slopes']} min_rank={result['min_rank']} "
        f"direction_max={result['direction_max']} mutations={caught}/{len(cases)}"
    )


if __name__ == "__main__":
    main()

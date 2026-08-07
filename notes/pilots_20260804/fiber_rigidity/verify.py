#!/usr/bin/env python3
"""Independent checker for the XR fiber-rigidity boundary fixture."""

from __future__ import annotations

import argparse
import copy
import json
from itertools import combinations
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "fixture.json"
INF = "inf"


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def inverse(value: int, prime: int) -> int:
    need(value % prime != 0, "inverse of zero")
    return pow(value, prime - 2, prime)


def evaluate(coefficients: list[int], value: int, prime: int) -> int:
    result = 0
    for coefficient in reversed(coefficients):
        result = (result * value + coefficient) % prime
    return result


def multiply(first: list[int], second: list[int], prime: int) -> list[int]:
    result = [0] * (len(first) + len(second) - 1)
    for left_index, left in enumerate(first):
        for right_index, right in enumerate(second):
            result[left_index + right_index] = (
                result[left_index + right_index] + left * right
            ) % prime
    return result


def locator(values: list[int], prime: int) -> list[int]:
    result = [1]
    for value in values:
        result = multiply(result, [(-value) % prime, 1], prime)
    return result


def interpolate(indices: tuple[int, ...], values: list[int], domain: list[int], prime: int) -> list[int]:
    degree = len(indices)
    result = [0] * degree
    for position, index in enumerate(indices):
        numerator = [1]
        denominator = 1
        x_value = domain[index]
        for other_position, other_index in enumerate(indices):
            if other_position == position:
                continue
            other = domain[other_index]
            numerator = multiply(numerator, [(-other) % prime, 1], prime)
            denominator = denominator * (x_value - other) % prime
        scale = values[index] * inverse(denominator, prime) % prime
        for coefficient, value in enumerate(numerator):
            result[coefficient] = (result[coefficient] + scale * value) % prime
    return result


def matrix_rank(rows: list[list[int]], prime: int) -> int:
    matrix = [row[:] for row in rows]
    pivot_row = 0
    columns = len(matrix[0]) if matrix else 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, len(matrix)) if matrix[row][column] % prime),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = inverse(matrix[pivot_row][column], prime)
        matrix[pivot_row] = [value * scale % prime for value in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                (left - factor * right) % prime
                for left, right in zip(matrix[row], matrix[pivot_row])
            ]
        pivot_row += 1
    return pivot_row


def profile(
    u_values: list[int],
    v_values: list[int],
    first: list[int],
    second: list[int],
    domain: list[int],
    prime: int,
) -> tuple[tuple[int, ...], dict[object, tuple[int, ...]]]:
    core = []
    extras: dict[object, list[int]] = {}
    for index, value in enumerate(domain):
        left = (u_values[index] - evaluate(first, value, prime)) % prime
        right = (v_values[index] - evaluate(second, value, prime)) % prime
        if left == 0 and right == 0:
            core.append(index)
        elif right == 0:
            extras.setdefault(INF, []).append(index)
        else:
            slope = -left * inverse(right, prime) % prime
            extras.setdefault(slope, []).append(index)
    return tuple(core), {key: tuple(value) for key, value in extras.items()}


def set_maximum(
    maxima: dict[object, int],
    selected: dict[object, tuple[int, ...]],
    slope: object,
    support: tuple[int, ...],
) -> None:
    size = len(support)
    if size > maxima.get(slope, -1):
        maxima[slope] = size
        selected[slope] = support
    elif size == maxima.get(slope, -1) and support < selected[slope]:
        selected[slope] = support


def independent_scan(payload: dict) -> tuple[dict[str, int], dict[str, list[int]], int]:
    row = payload["row"]
    prime, n, k = row["q"], row["n"], row["k"]
    domain = payload["domain"]
    u_values = payload["received"]["u_values"]
    v_values = payload["received"]["v_values"]
    slopes = [*range(prime), INF]

    maxima: dict[object, int] = {}
    selected: dict[object, tuple[int, ...]] = {}
    zero_core, zero_extras = profile(
        u_values, v_values, [0], [0], domain, prime
    )
    for slope in slopes:
        support = tuple(sorted((*zero_core, *zero_extras.get(slope, ()))))
        set_maximum(maxima, selected, slope, support)

    anchors = 0
    floor = len(zero_core)
    for indices in combinations(range(n), k):
        anchors += 1
        first = interpolate(indices, u_values, domain, prime)
        second = interpolate(indices, v_values, domain, prime)
        core, extras = profile(
            u_values, v_values, first, second, domain, prime
        )
        if len(core) >= floor:
            for slope in slopes:
                support = tuple(sorted((*core, *extras.get(slope, ()))))
                set_maximum(maxima, selected, slope, support)
        else:
            for slope, extra in extras.items():
                support = tuple(sorted((*core, *extra)))
                set_maximum(maxima, selected, slope, support)
        if anchors % 100000 == 0:
            print(
                f"audit_progress anchors={anchors} max={max(maxima.values())}",
                flush=True,
            )
    return (
        {str(key): value for key, value in maxima.items()},
        {str(key): list(value) for key, value in selected.items()},
        anchors,
    )


def validate(payload: dict, full_scan: bool) -> None:
    need(payload["schema"] == "xr-fiber-rigidity-boundary-fixture-v1", "schema")
    need(payload["verdict"] == "COUNTEREXAMPLE_TO_FIELD_INDEPENDENT_FR", "verdict")
    row = payload["row"]
    prime, n, k, depth = row["q"], row["n"], row["k"], row["d"]
    need((prime, n, k, depth, row["h"], row["ell"]) == (193, 64, 4, 13, 18, 2), "row")
    need(row["A"] == k + row["h"] == 22, "agreement")
    need(row["r"] == row["h"] - depth == 2 * row["ell"] + 1 == 5, "boundary")
    need(row["sigma"] == depth - row["ell"] - 1 - 2 * row["r"] == 0, "sigma")
    need(row["rprime"] == n - k - depth == 47, "rprime")

    domain = payload["domain"]
    need(len(domain) == n and len(set(domain)) == n and domain[0] == 1, "domain")
    omega = domain[1]
    need(all(domain[index] == pow(omega, index, prime) for index in range(n)), "domain powers")
    need(pow(omega, n, prime) == 1 and pow(omega, n // 2, prime) != 1, "domain order")

    P, Q = payload["P"], payload["Q"]
    need(P == [1, 0, 1] and Q == [0, 1], "primitive pair")
    received = payload["received"]
    u_values, v_values = received["u_values"], received["v_values"]
    u_poly, v_poly = received["u_polynomial"], received["v_polynomial"]
    need(len(u_values) == len(v_values) == n, "received lengths")
    need(all(evaluate(u_poly, x, prime) == y for x, y in zip(domain, u_values)), "u evaluation")
    need(all(evaluate(v_poly, x, prime) == y for x, y in zip(domain, v_values)), "v evaluation")

    D = payload["active_defect"]["D"]
    need(len(D) == 10 and len(set(D)) == 10, "D size")
    Z_D = locator([domain[index] for index in D], prime)
    need(Z_D == payload["Z_D"], "D locator")
    expected_A = multiply(Z_D, P, prime)
    expected_B = multiply(Z_D, Q, prime)
    syzygy = payload["syzygy"]
    need(expected_A == syzygy["A"] and expected_B == syzygy["B"], "syzygy products")

    rprime = row["rprime"]
    first_rows = [
        [u_poly[(row_index - column) % n] for column in range(rprime + 1)]
        for row_index in range(n - depth, n)
    ]
    second_rows = [
        [v_poly[(row_index - column) % n] for column in range(rprime + 1)]
        for row_index in range(n - depth, n)
    ]
    stacked_rank = matrix_rank(first_rows + second_rows, prime)
    need(stacked_rank == syzygy["stacked_rank"] == 25, "stacked rank")
    need(syzygy["left_nullity"] == 2 * depth - stacked_rank == 1, "left nullity")
    left = list(reversed(expected_A + [0] * (depth - len(expected_A))))
    right = list(reversed(expected_B + [0] * (depth - len(expected_B))))
    relation = [
        sum(
            left[index] * first_rows[index][column]
            + right[index] * second_rows[index][column]
            for index in range(depth)
        )
        % prime
        for column in range(rprime + 1)
    ]
    need(not any(relation) and syzygy["relation_zero"], "left relation")

    residual = [
        (evaluate(P, x, prime) * u_values[index] + evaluate(Q, x, prime) * v_values[index]) % prime
        for index, x in enumerate(domain)
    ]
    need({index for index, value in enumerate(residual) if value} == set(D), "residual support")
    need(payload["active_defect"]["support_exact"], "support flag")
    core = tuple(
        index for index, pair in enumerate(zip(u_values, v_values)) if pair == (0, 0)
    )
    need(list(core) == payload["core"] and len(core) == k + depth == 17, "maximal core")

    fibers: dict[int, list[int]] = {}
    for index in D:
        value = evaluate(P, domain[index], prime) * inverse(evaluate(Q, domain[index], prime), prime) % prime
        fibers.setdefault(value, []).append(index)
    need(sorted(len(points) for points in fibers.values()) == [2] * 5, "fiber sizes")
    expected_fibers = {str(key): value for key, value in sorted(fibers.items())}
    need(expected_fibers == payload["fiber_partition"], "fiber partition")

    blocks = payload["blocks"]
    plus, minus = blocks["plus"], blocks["minus"]
    need(len(plus) == len(minus) == 5 and set(plus).isdisjoint(minus), "blocks")
    need(set(plus) | set(minus) == set(D), "two-block cover")
    for label, block in (("plus", plus), ("minus", minus)):
        counts = sorted(
            (len(set(points) & set(block)) for points in fibers.values() if set(points) & set(block)),
            reverse=True,
        )
        need(counts == blocks["profiles"][label] == [2, 1, 1, 1], f"{label} profile")
        partial_points = sum(
            len(set(points) & set(block))
            for points in fibers.values()
            if 0 < len(set(points) & set(block)) < len(points)
        )
        need(partial_points == 3 > 1, f"{label} violates broad FR")

    rays = payload["rays"]
    need(rays["slope_plus"] == -inverse(rays["error_plus"], prime) % prime, "plus slope")
    need(rays["slope_minus"] == -inverse(rays["error_minus"], prime) % prime, "minus slope")
    for label, slope, block in (
        ("plus", rays["slope_plus"], plus),
        ("minus", rays["slope_minus"], minus),
    ):
        support = [index for index in range(n) if (u_values[index] + slope * v_values[index]) % prime == 0]
        need(support == rays[f"support_{label}"] and len(support) == row["A"], f"{label} support")
        need(set(support) == set(core) | set(block), f"{label} block locality")
        for index in block:
            denominator = (evaluate(Q, domain[index], prime) - slope * evaluate(P, domain[index], prime)) % prime
            need(denominator != 0, f"{label} BE denominator")

    scan = payload["scan"]
    need(scan["complete"] and scan["subsets"] == scan["expected_subsets"] == comb(n, k), "scan coverage")
    need(scan["maximum"] == row["A"], "scan maximum")
    need(scan["live_slopes"] == sorted((rays["slope_minus"], rays["slope_plus"])), "live slopes")
    plus_key, minus_key = str(rays["slope_plus"]), str(rays["slope_minus"])
    need(scan["selected"][plus_key] == rays["support_plus"], "plus first match")
    need(scan["selected"][minus_key] == rays["support_minus"], "minus first match")
    need(set(scan["selected_slopes_containing_core"]) == {plus_key, minus_key}, "selected L_P=2")

    if full_scan:
        maxima, selected, anchors = independent_scan(payload)
        need(anchors == scan["subsets"], "independent anchor coverage")
        need(maxima == scan["maxima"], "independent maxima")
        need(selected == scan["selected"], "independent first matches")


def tamper_selftest(payload: dict) -> int:
    mutations = []
    for path, value in (
        (("row", "A"), 23),
        (("syzygy", "stacked_rank"), 24),
        (("syzygy", "A", 0), 2),
        (("received", "u_values", 0), 1),
        (("active_defect", "D", 0), 2),
        (("core", 0), 2),
        (("blocks", "profiles", "plus", 0), 1),
        (("blocks", "plus", 0), 5),
        (("rays", "slope_plus"), 0),
        (("scan", "subsets"), 635375),
        (("scan", "maximum"), 23),
        (("scan", "selected", "192", 0), 2),
    ):
        candidate = copy.deepcopy(payload)
        target = candidate
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        mutations.append(candidate)
    rejected = 0
    for candidate in mutations:
        try:
            validate(candidate, full_scan=False)
        except (ValueError, KeyError, IndexError, TypeError):
            rejected += 1
    need(rejected == len(mutations), "tamper rejection")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--full-scan", action="store_true")
    parser.add_argument("--tamper-selftest", action="store_true")
    arguments = parser.parse_args()
    payload = json.loads(arguments.certificate.read_text(encoding="ascii"))
    validate(payload, full_scan=arguments.full_scan)
    mutations = tamper_selftest(payload) if arguments.tamper_selftest else 0
    print(
        "XR_FIBER_RIGIDITY_INDEPENDENT_AUDIT_PASS "
        f"full_scan={str(arguments.full_scan).lower()} mutations={mutations}"
    )


if __name__ == "__main__":
    main()

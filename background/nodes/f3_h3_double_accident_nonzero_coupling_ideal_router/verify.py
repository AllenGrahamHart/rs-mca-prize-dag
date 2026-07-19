#!/usr/bin/env python3
"""Replay the H3 nonzero-coupling ideal router."""

from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from collections import defaultdict
from functools import reduce
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_double_accident_nonzero_coupling_ideal_router"
DEPENDENCIES = {
    "f3_h3_double_accident_low_distance_joint_ideal_router",
    "f3_h3_shifted_product_sidon",
}
CONSUMER = "f3_h3_mobius_excess_half"


def folded_signature(terms: tuple[tuple[int, int], ...], n: int) -> tuple[int, ...]:
    degree = n // 2
    out = [0] * degree
    for coefficient, exponent in terms:
        exponent %= n
        if exponent >= degree:
            exponent -= degree
            coefficient = -coefficient
        out[exponent] += coefficient
    return tuple(out)


def triple_signature(a: int, b: int, c: int, n: int) -> tuple[int, ...]:
    return folded_signature(
        (
            (-1, a),
            (-1, b),
            (-1, c),
            (1, a + b),
            (1, a + c),
            (1, b + c),
            (-1, a + b + c),
        ),
        n,
    )


def is_telescoping(triple: tuple[int, int, int], output: int, n: int) -> bool:
    target = tuple(sorted(triple))
    return any(
        4 * q % n == output
        and tuple(sorted((q, (q + n // 2) % n, (2 * q + n // 2) % n))) == target
        for q in range(1, n)
        if 4 * q % n != 0
    )


def classify_order(n: int) -> tuple[int, int, int]:
    outputs = {
        folded_signature(((-1, exponent),), n): exponent
        for exponent in range(1, n)
    }
    solutions: list[tuple[tuple[int, int, int], int]] = []
    for triple in itertools.combinations_with_replacement(range(1, n), 3):
        output = outputs.get(triple_signature(*triple, n))
        if output is None:
            continue
        assert is_telescoping(triple, output, n)
        solutions.append((triple, output))

    assert len(solutions) == (n - 4) // 2
    anchors: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    for triple, output in solutions:
        assert len(set(triple)) == 3
        for denominator_index in range(3):
            denominator = triple[denominator_index]
            product_pair = tuple(
                sorted(value for index, value in enumerate(triple) if index != denominator_index)
            )
            anchors.add((product_pair, (denominator, output)))
    assert len(anchors) == 3 * (n - 4) // 2

    by_product: dict[tuple[int, int], int] = defaultdict(int)
    for product_pair, _ in anchors:
        by_product[product_pair] += 1
    assert max(by_product.values(), default=0) == 1
    return len(solutions), len(anchors), max(by_product.values(), default=0)


def load_joint_helpers():
    sys.dont_write_bytecode = True
    path = ROOT / "background" / "nodes" / "f3_h3_double_accident_low_distance_joint_ideal_router" / "verify.py"
    spec = importlib.util.spec_from_file_location("joint_ideal_verify", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def finite_fixture() -> tuple[int, int, int]:
    helper = load_joint_helpers()
    n, p, generator, target = 32, 1153, 194, 230
    center, leaf_f, leaf_g = (2, 25), (5, 10), (6, 8)
    zero_quotient = (9, 4)
    nonzero_quotient = (23, 26)
    pi = [1, -1]
    pi_squared = helper.multiply(pi, pi)

    beta_center = helper.beta(center)
    alpha_f = helper.divide_exact(
        helper.subtract(helper.beta(leaf_f), beta_center), pi_squared
    )
    alpha_g = helper.divide_exact(
        helper.subtract(helper.beta(leaf_g), beta_center), pi_squared
    )

    def coupling(quotient: tuple[int, int]):
        u, v = quotient
        return helper.divide_exact(
            helper.subtract(
                helper.multiply(beta_center, helper.shifted(u)),
                helper.shifted(v),
            ),
            pi,
        )

    lambda_zero = coupling(zero_quotient)
    lambda_nonzero = coupling(nonzero_quotient)
    assert helper.reduce_cyclotomic(lambda_zero, n) == [0]
    assert helper.reduce_cyclotomic(lambda_nonzero, n) != [0]
    assert is_telescoping(tuple(sorted((*center, zero_quotient[0]))), zero_quotient[1], n)
    assert not is_telescoping(
        tuple(sorted((*center, nonzero_quotient[0]))), nonzero_quotient[1], n
    )

    quotient_values = []
    for u, v in (zero_quotient, nonzero_quotient):
        c_value = helper.evaluate(helper.shifted(u), generator, p)
        d_value = helper.evaluate(helper.shifted(v), generator, p)
        quotient_values.append(d_value * pow(c_value, -1, p) % p)
    assert quotient_values == [target, target]
    assert helper.evaluate(lambda_nonzero, generator, p) == 0

    norms = [
        helper.principal_norm(alpha_f, n),
        helper.principal_norm(alpha_g, n),
        helper.principal_norm(lambda_nonzero, n),
    ]
    assert norms == [18448, 2306, 2306]
    common = reduce(gcd, norms)
    assert common == 2 * p
    return len(quotient_values), norms[-1], common


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "3(n-4)/2",
        ">= R(t)-1",
        "K_t^NZ=(alpha_F,alpha_G",
        "Y_18>0  =>  p in D_n^NZ",
        "does not construct",
    ):
        assert marker in statement


def main() -> None:
    classified = [classify_order(n) for n in (8, 16, 32, 64)]
    quotient_lifts, coupling_norm, common = finite_fixture()
    packet_check()
    print(
        "F3_H3_DOUBLE_ACCIDENT_NONZERO_COUPLING_IDEAL_ROUTER_PASS "
        f"rows={len(classified)} zero_anchors={','.join(str(row[1]) for row in classified)} "
        f"quotient_lifts={quotient_lifts} coupling_norm={coupling_norm} gcd={common}"
    )


if __name__ == "__main__":
    main()

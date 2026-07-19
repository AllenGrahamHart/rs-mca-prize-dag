#!/usr/bin/env python3
"""Replay the H3 coupling-batch odd-saturation theorem."""

from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_double_accident_coupling_batch_odd_saturation"
DEPENDENCIES = {
    "f3_h3_double_accident_low_distance_joint_ideal_router",
    "f3_h3_double_accident_nonzero_coupling_ideal_router",
}
CONSUMER = "f3_h3_mobius_excess_half"


def load_helpers():
    sys.dont_write_bytecode = True
    path = ROOT / "background" / "nodes" / "f3_h3_double_accident_low_distance_joint_ideal_router" / "verify.py"
    spec = importlib.util.spec_from_file_location("joint_ideal_verify", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


HELPER = load_helpers()
PI = [1, -1]


def normalized_shift(exponent: int) -> list[int]:
    return HELPER.divide_exact(HELPER.shifted(exponent), PI)


def coupling(beta: list[int], quotient: tuple[int, int]) -> list[int]:
    u, v = quotient
    return HELPER.subtract(
        HELPER.multiply(beta, normalized_shift(u)), normalized_shift(v)
    )


def quotient_collision(
    left: tuple[int, int], right: tuple[int, int]
) -> list[int]:
    u0, v0 = left
    u1, v1 = right
    return HELPER.subtract(
        HELPER.multiply(normalized_shift(v1), normalized_shift(u0)),
        HELPER.multiply(normalized_shift(v0), normalized_shift(u1)),
    )


def negate(poly: list[int]) -> list[int]:
    return [-coefficient for coefficient in poly]


def identity_check(n: int, product_pair: tuple[int, int], q0, q1) -> None:
    beta = HELPER.beta(product_pair)
    lambda_0 = coupling(beta, q0)
    lambda_1 = coupling(beta, q1)
    theta = quotient_collision(q0, q1)
    left = HELPER.subtract(
        HELPER.multiply(normalized_shift(q0[0]), lambda_1),
        HELPER.multiply(normalized_shift(q1[0]), lambda_0),
    )
    error = HELPER.subtract(left, negate(theta))
    assert HELPER.reduce_cyclotomic(error, n) == [0]


def norm_formula_check() -> int:
    checked = 0
    for n in (8, 16, 32):
        for exponent in range(1, n):
            level = (exponent & -exponent).bit_length() - 1
            expected = 2 ** (2**level - 1)
            assert HELPER.principal_norm(normalized_shift(exponent), n) == expected
            checked += 1
    return checked


def exhaustive_identity_check() -> int:
    n = 8
    product_pairs = tuple(itertools.combinations_with_replacement(range(1, n), 2))
    quotient_lifts = tuple(
        (u, v) for u in range(1, n) for v in range(1, n) if u != v
    )
    checked = 0
    for product_pair in product_pairs:
        for q0, q1 in itertools.combinations(quotient_lifts, 2):
            identity_check(n, product_pair, q0, q1)
            checked += 1
    assert checked == 24108
    return checked


def finite_fixture() -> tuple[int, int, int]:
    n = 32
    beta = HELPER.beta((2, 25))
    q0, q1 = (9, 4), (23, 26)
    lambda_0 = coupling(beta, q0)
    lambda_1 = coupling(beta, q1)
    theta = quotient_collision(q0, q1)
    identity_check(n, (2, 25), q0, q1)
    assert HELPER.reduce_cyclotomic(lambda_0, n) == [0]
    assert HELPER.principal_norm(normalized_shift(q0[0]), n) == 1
    theta_norm = HELPER.principal_norm(theta, n)
    lambda_norm = HELPER.principal_norm(lambda_1, n)
    assert theta_norm == lambda_norm == 2306
    return theta_norm, lambda_norm, HELPER.principal_norm(normalized_shift(q0[0]), n)


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
        "|Norm(c_a)|=2^(2^r-1)",
        "c_(u_0)lambda_1-c_(u_1)lambda_0=-theta_01",
        "I_anchor O[1/2]=I_batch O[1/2]",
        "identical odd parts",
        "does not say",
    ):
        assert marker in statement


def main() -> None:
    norms = norm_formula_check()
    identities = exhaustive_identity_check()
    theta_norm, lambda_norm, coefficient_norm = finite_fixture()
    packet_check()
    print(
        "F3_H3_DOUBLE_ACCIDENT_COUPLING_BATCH_ODD_SATURATION_PASS "
        f"norms={norms} identities={identities} fixture={theta_norm}/{lambda_norm}/{coefficient_norm}"
    )


if __name__ == "__main__":
    main()

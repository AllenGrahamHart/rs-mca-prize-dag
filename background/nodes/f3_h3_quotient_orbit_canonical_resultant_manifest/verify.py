#!/usr/bin/env python3
"""Verify the quotient-orbit canonical resultant manifest."""

from __future__ import annotations

import json
from pathlib import Path

from sympy import Poly, QQ, ZZ, expand, resultant, symbols


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_quotient_orbit_canonical_resultant_manifest"
DEPENDENCY = "f3_h3_quotient_galois_orbit_scalar_decomposition"
CONSUMERS = {
    "f3_h3_dsp8_correlation_bound",
    "f3_h3_official_order_template_survivor",
}
Z, T = symbols("Z T")


def valuation_two(value: int) -> int:
    result = 0
    while value % 2 == 0:
        result += 1
        value //= 2
    return result


def canonical_representatives(exponent: int) -> list[tuple[int, str, int, int, int]]:
    representatives: list[tuple[int, str, int, int, int]] = []
    for degree_exponent in range(1, exponent):
        conductor = 2 ** (degree_exponent + 1)
        scale = 2 ** (exponent - degree_exponent - 1)
        for parameter in range(3, conductor, 2):
            representatives.append(
                (degree_exponent, "+", parameter, scale, scale * parameter)
            )
        for parameter in range(2, conductor, 2):
            representatives.append(
                (degree_exponent, "+", parameter, scale, scale * parameter)
            )
            representatives.append(
                (degree_exponent, "-", parameter, scale * parameter, scale)
            )
    return representatives


def orbit(exponent: int, pair: tuple[int, int]) -> frozenset[tuple[int, int]]:
    order = 2**exponent
    return frozenset(
        (unit * pair[0] % order, unit * pair[1] % order)
        for unit in range(1, order, 2)
    )


def representative_check() -> None:
    for exponent in range(2, 7):
        order = 2**exponent
        representatives = canonical_representatives(exponent)
        expected_count = 3 * (order - exponent - 1)
        assert len(representatives) == expected_count

        blocks = [orbit(exponent, (u, v)) for _, _, _, u, v in representatives]
        assert len(set(blocks)) == len(blocks)
        assert set().union(*blocks) == {
            (u, v)
            for u in range(1, order)
            for v in range(1, order)
            if u != v
        }

        for degree_exponent in range(1, exponent):
            rows = [row for row in representatives if row[0] == degree_exponent]
            assert len(rows) == 3 * (2**degree_exponent - 1)
            assert {len(orbit(exponent, (row[3], row[4]))) for row in rows} == {
                2**degree_exponent
            }


def power_of_two(value: int) -> bool:
    return value > 0 and value & (value - 1) == 0


def resultant_check() -> None:
    for degree_exponent in range(1, 4):
        conductor = 2 ** (degree_exponent + 1)
        degree = 2**degree_exponent
        cyclotomic = Z**degree + 1
        for parameter in range(2, conductor):
            if parameter == 1:
                continue
            geometric_sum = sum(Z**power for power in range(parameter))
            plus = Poly(
                resultant(cyclotomic, T - geometric_sum, Z), T, domain=ZZ
            )
            norm = int(resultant(cyclotomic, geometric_sum, Z))
            expected_norm = (
                1
                if parameter % 2
                else 2 ** (2 ** valuation_two(parameter) - 1)
            )
            assert plus.degree() == degree
            assert plus.LC() == 1
            assert plus.TC() == expected_norm
            assert norm == expected_norm
            assert plus.is_irreducible

            if parameter % 2:
                continue
            raw_reverse = Poly(
                resultant(cyclotomic, geometric_sum * T - 1, Z), T, domain=ZZ
            )
            reciprocal = expand(T**degree * plus.as_expr().subs(T, 1 / T))
            assert expand(raw_reverse.as_expr() - reciprocal) == 0
            reverse = Poly(raw_reverse.as_expr() / norm, T, domain=QQ)
            assert reverse.degree() == degree
            assert reverse.LC() == 1
            assert reverse.is_irreducible
            assert all(power_of_two(int(coefficient.q)) for coefficient in reverse.all_coeffs())


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    for consumer in CONSUMERS:
        assert (NODE, consumer, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join(
        (base / name).read_text() for name in required if name.endswith(".md")
    )
    for marker in (
        "(j,+,w)",
        "(j,-,w)",
        "Res_Z(Phi_L(Z),T-S_w(Z))",
        "2^(2^a-1)",
        "does not identify",
        "without constructing any orbit",
    ):
        assert marker in text


def main() -> None:
    representative_check()
    resultant_check()
    packet_check()
    print(
        "F3_H3_QUOTIENT_ORBIT_CANONICAL_RESULTANT_MANIFEST_PASS "
        "families=3 max_checked_order=64 max_resultant_conductor=16"
    )


if __name__ == "__main__":
    main()

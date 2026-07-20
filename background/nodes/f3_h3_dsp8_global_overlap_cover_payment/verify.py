#!/usr/bin/env python3
"""Verify the global overlap-cover payment and DSP8 constants."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_global_overlap_cover_payment"
DEPENDENCIES = {
    "f3_h3_distance_six_support_overlap_payment",
    "f3_affine_coset_pair_cubic_preimage_stepanov",
    "f3_h3_dsp8_antipodal_quotient_mass_payment",
    "f3_h3_dsp8_primitive_shift_pair_adapter",
}
CONSUMER = "f3_h3_dsp8_correlation_bound"


def cover_identity_check(prime: int = 1_000_003) -> None:
    inverse = lambda value: pow(value % prime, -1, prime)

    u = 3
    x = 2 * u * u * inverse(1 + u * u) % prime
    y = -u % prime
    v = -2 * u * inverse(1 + u * u) % prime
    assert u * v % prime == -x % prime
    assert (1 - x) * (1 - y) % prime == (1 - u) * (1 - v) % prime

    y = 5
    x = (1 + y * y) * inverse(2 * y * y) % prime
    u = x * y % prime
    v = -inverse(y) % prime
    assert u * v % prime == -x % prime
    assert (1 - x) * (1 - y) % prime == (1 - u) * (1 - v) % prime


def arithmetic_check() -> int:
    assert Fraction(17, 10) * 2 * Fraction(51, 16) == Fraction(867, 80)
    assert Fraction(17, 10) * 2 == Fraction(17, 5)
    assert 68 * Fraction(51, 32) == Fraction(867, 8)
    assert Fraction(867, 8) + Fraction(867, 4) == Fraction(2601, 8)
    assert Fraction(495) - Fraction(2601, 160) == Fraction(76599, 160)
    assert Fraction(750, 20) == Fraction(300, 8)
    assert -Fraction(255, 20) == -Fraction(102, 8)
    assert -Fraction(68, 20) == -Fraction(17, 5)
    assert Fraction(867, 4) / 20 == Fraction(867, 80)

    rows = 0
    for exponent in range(13, 42):
        n = 1 << exponent
        quotient_mass = (n - 1) * (n - 2)
        root_free = (
            750 * n * n
            - 255 * quotient_mass
            - Fraction(76599, 160) * n * n
        )
        assert root_free > 0
        assert Fraction(2601, 8) ** 3 * n**5 < root_free**3
        rows += 1
    return rows


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    statement = "".join((base / "statement.md").read_text().split())
    proof = "".join((base / "proof.md").read_text().split())
    for marker in (
        "<(867/80)n^(5/3)+(17/5)S_A",
        "10K_25^0+17K_25^A+68S_A+(867/4)n^(5/3)",
        "160(10K_25^0+17K_25^A)<=76599n^2",
        "atmost`2n`suchedgesglobally",
    ):
        assert marker in statement + proof

    target = "".join(
        (ROOT / "critical" / "nodes" / CONSUMER / "statement.md")
        .read_text()
        .split()
    )
    conditional = "".join(
        (
            ROOT
            / "critical"
            / "nodes"
            / "f3_h3_mobius_excess_half"
            / "conditional.md"
        )
        .read_text()
        .split()
    )
    live_marker = "10K_25^0+17K_25^A+68S_A+(867/4)n^(5/3)"
    assert live_marker in target
    assert live_marker in conditional


def main() -> None:
    cover_identity_check()
    rows = arithmetic_check()
    packet_check()
    print(
        "F3_H3_DSP8_GLOBAL_OVERLAP_COVER_PAYMENT_PASS "
        f"official_rows={rows} global_edge_cap=2n "
        "uniform_numerator=76599 denominator=160"
    )


if __name__ == "__main__":
    main()

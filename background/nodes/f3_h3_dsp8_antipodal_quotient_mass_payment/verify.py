#!/usr/bin/env python3
"""Verify the antipodal quotient-mass payment and DSP8 constants."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_antipodal_quotient_mass_payment"
DEPENDENCIES = {
    "f3_h3_distance_six_support_overlap_payment",
    "f3_affine_coset_pair_cubic_preimage_stepanov",
    "f3_h3_dsp8_primitive_shift_pair_adapter",
}
CONSUMER = "f3_h3_dsp8_correlation_bound"
SUCCESSOR = "f3_h3_dsp8_global_overlap_cover_payment"


def arithmetic_check() -> int:
    assert Fraction(17, 10) * 8 - 6 == Fraction(38, 5)
    assert 152 * Fraction(51, 32) == Fraction(969, 4)
    assert Fraction(375) - Fraction(969, 80) == Fraction(29031, 80)
    assert Fraction(750, 20) == Fraction(300, 8)
    assert -Fraction(375, 20) == -Fraction(102, 8) - 6
    assert -Fraction(152, 20) == -Fraction(38, 5)

    for disjoint_free in range(5):
        for disjoint_antipodal in range(5):
            k_weight = 10 * (2 * disjoint_free) + 17 * (2 * disjoint_antipodal)
            d_weight = disjoint_free + Fraction(17, 10) * disjoint_antipodal
            assert k_weight == 20 * d_weight

    rows = 0
    for exponent in range(13, 42):
        n = 1 << exponent
        quotient_mass = (n - 1) * (n - 2)
        exact_without_root = (
            750 * n * n
            - 375 * quotient_mass
            - Fraction(29031, 80) * n * n
        )
        assert exact_without_root > 0

        # Prove (969/4)(n-2)n^(2/3) < exact_without_root by cubing.
        assert (
            Fraction(969 * (n - 2), 4) ** 3 * n * n
            < exact_without_root**3
        )
        rows += 1
    return rows


def subgroup(prime: int, order: int) -> list[int]:
    for base in range(2, prime):
        generator = pow(base, (prime - 1) // order, prime)
        if pow(generator, order // 2, prime) != 1:
            return [pow(generator, exponent, prime) for exponent in range(order)]
    raise AssertionError("subgroup generator not found")


def target_count_check(prime: int, order: int) -> int:
    group = subgroup(prime, order)
    targets = {
        (1 - a * a) % prime for a in group if a not in {1, prime - 1}
    }
    assert 0 not in targets
    assert 1 not in targets
    assert len(targets) == (order - 2) // 2
    return len(targets)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    assert nodes[SUCCESSOR]["status"] == "PROVED"
    assert (NODE, SUCCESSOR, "req") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "S_A<(51/32)(n-2)n^(2/3)",
        "<=6Q_n+(38/5)S_A",
        "10K_25^0+17K_25^A+152S_A",
        "80(10K_25^0+17K_25^A)<=29031n^2",
        "replacingtheformersufficientconstant`223`",
    ):
        assert marker in statement

    successor = "".join(
        (ROOT / "background" / "nodes" / SUCCESSOR / "statement.md")
        .read_text()
        .split()
    )
    assert "replacingtheprecedingsufficientconstant`29031/80`" in successor


def main() -> None:
    rows = arithmetic_check()
    targets_32 = target_count_check(97, 32)
    targets_64 = target_count_check(193, 64)
    packet_check()
    print(
        "F3_H3_DSP8_ANTIPODAL_QUOTIENT_MASS_PAYMENT_PASS "
        f"official_rows={rows} targets32={targets_32} targets64={targets_64} "
        "uniform_numerator=29031 denominator=80"
    )


if __name__ == "__main__":
    main()

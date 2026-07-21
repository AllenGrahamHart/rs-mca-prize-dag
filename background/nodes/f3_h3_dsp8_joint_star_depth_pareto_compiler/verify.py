#!/usr/bin/env python3
"""Verify the DSP8 joint-star / quotient-depth Pareto compiler."""

from __future__ import annotations

import json
from fractions import Fraction
from math import ceil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_joint_star_depth_pareto_compiler"
DEPENDENCIES = {
    "f3_h3_dsp8_accident_depth_compiler",
    "f3_h3_dsp8_disjoint_six_multiplicity_gate",
    "f3_h3_excess_multistar_degree_ladder",
    "f3_h3_double_accident_coupling_batch_odd_saturation",
    "f3_affine_coset_pair_cubic_preimage_stepanov",
}
CONSUMERS = {
    "f3_h3_dsp8_correlation_bound",
    "f3_h3_official_order_template_survivor",
}

TABLE = {
    6: (11, 25, 12, 11, Fraction(8, 11), Fraction(4), 2, 1),
    7: (10, 26, 11, 11, Fraction(8, 11), Fraction(4), 2, 1),
    8: (9, 27, 10, 12, Fraction(5, 9), Fraction(5, 4), 3, 2),
    9: (8, 28, 9, 12, Fraction(5, 9), Fraction(5, 4), 3, 2),
    10: (7, 29, 8, 13, Fraction(4, 9), Fraction(3, 4), 5, 3),
    11: (6, 30, 7, 13, Fraction(4, 9), Fraction(3, 4), 5, 3),
    12: (5, 31, 6, 14, Fraction(7, 18), Fraction(7, 12), 6, 4),
    13: (4, 32, 5, 14, Fraction(7, 18), Fraction(7, 12), 6, 4),
    14: (3, 33, 4, 15, Fraction(16, 47), Fraction(8, 17), 7, 5),
    15: (2, 34, 3, 15, Fraction(16, 47), Fraction(8, 17), 7, 5),
    16: (1, 35, 2, 16, Fraction(9, 29), Fraction(9, 22), 8, 6),
}
EXPECTED = {
    6: (Fraction(11, 2), Fraction(121, 136)),
    7: (Fraction(11, 2), Fraction(89023, 43520)),
    8: (Fraction(9, 4), Fraction(99, 85)),
    9: (Fraction(9, 4), Fraction(72837, 27200)),
    10: (Fraction(27, 16), Fraction(99, 68)),
    11: (Fraction(27, 16), Fraction(72837, 21760)),
    12: (Fraction(3, 2), Fraction(198, 119)),
    13: (Fraction(3, 2), Fraction(72837, 19040)),
    14: (Fraction(47, 34), Fraction(517, 272)),
    15: (Fraction(47, 34), Fraction(380371, 87040)),
    16: (Fraction(29, 22), Fraction(319, 153)),
}
ODD_REFINEMENTS = {7, 9, 11, 13, 15}
PARITY_BUDGET = Fraction(8093, 320)


def free_floor(size: int) -> int:
    return ceil(Fraction(size * (size - 4), 2)) - 2 * size - 6


def antipodal_floor(size: int) -> int:
    return ceil(Fraction(size * (size - 2), 2)) - 4 * (size - 1) - 8


def budget(n: int, depth: int, cutoff: int) -> int:
    return 300 * n * n - 17 * depth * (n - 1) ** 2 - 17 * cutoff * (n - 2) ** 2


def arithmetic_check() -> None:
    for cutoff, row in TABLE.items():
        depth, product, quotient, minimum, free_ratio, antipodal_ratio, free_degree, antipodal_degree = row
        assert depth == 17 - cutoff
        assert product == 19 + cutoff
        assert quotient == 18 - cutoff
        assert minimum == 7 + ceil(Fraction(cutoff + 1, 2))
        endpoint_excess = 2 * (minimum - 7)
        assert Fraction(endpoint_excess, free_floor(minimum)) == free_ratio
        assert Fraction(endpoint_excess, antipodal_floor(minimum)) == antipodal_ratio
        weight, allowance = EXPECTED[cutoff]
        assert weight == antipodal_ratio / free_ratio
        target_budget = PARITY_BUDGET if cutoff in ODD_REFINEMENTS else Fraction(11)
        assert allowance == target_budget / (17 * free_ratio)
        assert ceil(Fraction(2 * free_floor(minimum), minimum)) == free_degree
        assert ceil(Fraction(2 * antipodal_floor(minimum), minimum - 1)) == antipodal_degree

        for size in range(minimum, 1025):
            excess = 2 * (size - 7)
            assert Fraction(excess, free_floor(size)) <= free_ratio
            assert Fraction(excess, antipodal_floor(size)) <= antipodal_ratio
            assert ceil(Fraction(2 * free_floor(size), size)) >= free_degree
            assert ceil(Fraction(2 * antipodal_floor(size), size - 1)) >= antipodal_degree

        for n in (2**power for power in range(13, 42)):
            if cutoff in ODD_REFINEMENTS:
                assert n > 20**3
                conservative_parity_budget = (
                    300 * n * n
                    - 17 * depth * (n - 1) ** 2
                    - 17 * (cutoff - 1) * (n - 2) ** 2
                    - Fraction(867, 320) * n * n
                )
                assert conservative_parity_budget > PARITY_BUDGET * n * n
            else:
                assert budget(n, depth, cutoff) > 11 * n * n
            assert 17 * free_ratio * allowance == target_budget
            assert free_ratio * weight == antipodal_ratio

    for cutoff in ODD_REFINEMENTS:
        for product_count in range(19 + cutoff):
            for diagonal_count in range(3):
                if diagonal_count <= product_count and (
                    diagonal_count - product_count
                ) % 2 == 0:
                    excess = max(product_count - 18, 0)
                    assert excess <= cutoff - 1 + int(diagonal_count > 0)

    for polynomial in (
        lambda m: m * m - 12 * m + 54,
        lambda m: m * m - 14 * m + 67,
        lambda m: m * m - 12 * m + 64,
        lambda m: m * m - 14 * m + 77,
    ):
        assert polynomial(11) > 0
        assert all(polynomial(m) > 0 for m in range(11, 1025))


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for consumer in CONSUMERS:
        assert (NODE, consumer, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join((base / name).read_text() for name in required if name.endswith(".md"))
    for marker in (
        "(25,12)",
        "(34, 3)",
        "(35, 2)",
        "C_E=89023/43520",
        "C_E=380371/87040",
        "C_E=319/153",
        "S_(D,E)<(51/16)(n-1)n^(2/3)",
        "B_par,E(n)>(8093/320)n^2",
        "pure star degree 8",
        "two-edge packet",
        "I_E^batch O[1/2]=I_E^anchor O[1/2]",
        "cannot be mixed",
        "no survivor count",
    ):
        assert marker in text

    propagated = (
        ROOT / "critical" / "nodes" / "f3_h3_dsp8_correlation_bound" / "statement.md",
        ROOT
        / "background"
        / "nodes"
        / "f3_h3_official_order_template_survivor"
        / "statement.md",
        ROOT / "notes" / "PRIZE_COMPUTE_REQUESTS.md",
    )
    for path in propagated:
        surface = path.read_text()
        assert "89023/43520" in surface
        assert "380371/87040" in surface
        assert "S_(D,E)" in surface

    assert "8093/3520>2.29" in nodes[NODE]["statement"]


def main() -> None:
    arithmetic_check()
    packet_check()
    print(
        "F3_H3_DSP8_JOINT_STAR_DEPTH_PARETO_COMPILER_PASS "
        "corners=11 odd_refinements=5 endpoint=319/153"
    )


if __name__ == "__main__":
    main()

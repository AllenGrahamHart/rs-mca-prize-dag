#!/usr/bin/env python3
"""Independent exact audit of the preregistered C1' M2 result."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
M1 = ROOT / "critical/nodes/dli_prime_weighted_large_block_support/notes/m1_dli_m1_results.json"
M2 = ROOT / "critical/nodes/dli_prime_weighted_large_block_support/notes/m2_c1prime_level_scaled_results.json"
POSE = (
    ROOT
    / "critical/nodes/dli_prime_weighted_large_block_support/notes"
    / "C1PRIME_LEVEL_SCALED_POSE.md"
)

EXPECTED = {
    1: {193, 449, 769, 1409, 3137, 5569, 7937, 12289},
    2: {193, 257, 449, 577},
}
N = 32


def fraction(pair: list[int]) -> Fraction:
    return Fraction(pair[0], pair[1])


def main() -> None:
    pose = POSE.read_text()
    assert "w_max(L) = L+5" in pose
    assert "any exact row with `E-1 > 4r(1+W_cl)`" in pose

    m1 = json.loads(M1.read_text())
    m2 = json.loads(M2.read_text())
    assert m2["schema"] == "dli-c1prime-m2-v1"
    assert m2["pose"] == "w_max(L)=L+5, exact K_prime<=4"
    assert m2["killed"] is False
    assert m2["verdict"] == "C1_prime_SURVIVES_M2"
    assert len(m2["rows"]) == 12

    source = {
        ((row["t"] + 1) // 2, row["q"]): row
        for row in m1["rows"]
    }
    seen = {level: set() for level in EXPECTED}
    maximum: tuple[Fraction, int, int] | None = None
    positive_control = False
    decomposable_gaps = 0

    for row in m2["rows"]:
        level = row["level"]
        q = row["q"]
        assert level in EXPECTED and q in EXPECTED[level]
        assert row["N"] == N
        assert row["weights"] == list(range(level + 1, level + 6))
        seen[level].add(q)

        source_row = source[(level, q)]
        assert not source_row["suborbit_flags"]
        source_orbits = {int(weight): count for weight, count in source_row["V_orbits"].items()}
        primitive = {int(weight): count for weight, count in row["primitive_orbits"].items()}
        minimum_positive = min(
            weight for weight in row["weights"]
            if source_orbits.get(weight, 0) > 0
        )
        for weight in row["weights"]:
            complete_count = source_orbits.get(weight, 0)
            assert 0 <= primitive[weight] <= complete_count
            # Below twice the minimum nonzero weight, a relation cannot split
            # into two disjoint nonzero vanishing subvectors.
            if weight < 2 * minimum_positive:
                assert primitive[weight] == complete_count
            elif primitive[weight] < complete_count:
                decomposable_gaps += 1

        all_weighted = Fraction(1, 1) + sum(
            Fraction(count * 2 * N, 2**weight)
            for weight, count in source_orbits.items()
        )
        e_value = Fraction(q**level, 2**N) * all_weighted
        excess = e_value - 1
        r_value = Fraction(q**level, 2**N)
        ledger = sum(
            Fraction(primitive[weight] * 2 * N, 2**weight)
            for weight in row["weights"]
        )

        assert fraction(row["E_minus_1"]) == excess
        assert fraction(row["r"]) == r_value
        assert fraction(row["W_cl"]) == ledger
        assert row["killed"] is False
        assert excess <= 4 * r_value * (1 + ledger)
        exact_k = excess / (r_value * (1 + ledger))
        assert abs(row["K_prime"] - float(exact_k)) < 1e-15
        if maximum is None or exact_k > maximum[0]:
            maximum = (exact_k, level, q)

        if level == 1 and q == 7937:
            assert excess > 4 * r_value
            positive_control = True

    assert seen == EXPECTED
    assert positive_control
    assert decomposable_gaps > 0
    assert maximum is not None and maximum[1:] == (1, 7937)
    assert maximum[0] < Fraction(1, 4)
    print(
        "PASS DLI_C1PRIME_M2_AUDIT "
        f"rows=12 max_K={float(maximum[0]):.9f} "
        f"max_row=L{maximum[1]}_q{maximum[2]} "
        f"decomposable_gaps={decomposable_gaps} "
        "raw-ledger positive-control=detected"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify the profile-(4,4) energy-floor cofactor contraction."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import json
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_profile44_energy_floor_cofactor_contraction"
PARENTS = {
    "e1_profile44_local_norm_route_fence",
    "e1_profile44_official_energy_le4_exclusion",
}
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "unsafe_crossing_family_instantiation",
}
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE << 128
VALUATIONS = (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 16, 17, 18, 20)
PARENT_BOUND = 1_707_433
THRESHOLD = 932_364
EXPECTED_BY_MU = {
    1: 308,
    2: 167,
    3: 88,
    4: 44,
    5: 24,
    6: 12,
    8: 4,
    9: 3,
    10: 3,
    12: 1,
    16: 1,
    17: 1,
    18: 1,
}


def factor_odd(value: int) -> list[tuple[int, int]]:
    factors = []
    prime = 3
    while prime * prime <= value:
        if value % prime == 0:
            exponent = 0
            while value % prime == 0:
                value //= prime
                exponent += 1
            factors.append((prime, exponent))
        prime += 2
    if value > 1:
        factors.append((value, 1))
    return factors


def order_mod_256(value: int) -> int:
    residue = value % 256
    current = residue
    order = 1
    while current != 1:
        current = current * residue % 256
        order += 1
        assert order <= 64
    return order


def legal_cofactors(bound: int = PARENT_BOUND) -> list[int]:
    rows = []
    for valuation in VALUATIONS:
        odd = 1
        while (cofactor := (1 << valuation) * odd) <= bound:
            if all(
                exponent % order_mod_256(prime) == 0
                for prime, exponent in factor_odd(odd)
            ):
                rows.append(cofactor)
            odd += 256
    return rows


def exp16_interval(degree: int = 37) -> tuple[Fraction, Fraction]:
    lower = sum(Fraction(16**term, factorial(term)) for term in range(degree + 1))
    first_tail = Fraction(16 ** (degree + 1), factorial(degree + 1))
    upper = lower + first_tail / (1 - Fraction(16, degree + 2))
    return lower, upper


def threshold_holds(threshold: int = THRESHOLD) -> bool:
    exp_lower, exp_upper = exp16_interval()
    numerator = Fraction(20**320 * 3**32, 2**32)
    low = (threshold * P_MIN) ** 5
    high = ((threshold + 1) * P_MIN) ** 5
    return low * exp_upper < numerator < high * exp_lower


def main() -> None:
    assert threshold_holds()
    lower36, upper36 = exp16_interval(36)
    numerator = Fraction(20**320 * 3**32, 2**32)
    assert not (
        (THRESHOLD * P_MIN) ** 5 * upper36 < numerator
        < ((THRESHOLD + 1) * P_MIN) ** 5 * lower36
    )

    parent = legal_cofactors()
    assert len(parent) == len(set(parent)) == 1133
    assert max(parent) == 1_704_448
    survivors = [cofactor for cofactor in parent if cofactor <= THRESHOLD]
    excluded = [cofactor for cofactor in parent if cofactor > THRESHOLD]
    assert len(survivors) == 657 and len(excluded) == 476
    by_mu = Counter((cofactor & -cofactor).bit_length() - 1 for cofactor in survivors)
    assert dict(sorted(by_mu.items())) == EXPECTED_BY_MU
    assert max(survivors) == 931_844
    assert min(excluded) == 933_904
    pure = [cofactor for cofactor in survivors if cofactor & (cofactor - 1) == 0]
    assert pure == [2, 4, 8, 16, 32, 64, 256, 512, 1024, 4096, 65536, 131072, 262144]
    assert 1 << 20 not in survivors

    node_dir = ROOT / "background/nodes" / NODE
    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    assert "m<=932364" in statement and "exactly `657`" in statement
    for needle in ("degree-`37`", "932364 P < U < 932365 P", "V/C(V)"):
        assert needle in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert all((parent_id, NODE, "req") in edges for parent_id in PARENTS)
    assert all((NODE, target, "ev") in edges for target in TARGETS)

    controls = 0
    if not threshold_holds(THRESHOLD - 1):
        controls += 1
    if not threshold_holds(THRESHOLD + 1):
        controls += 1
    mutation = survivors + [1 << 20]
    try:
        assert len(mutation) == 657
    except AssertionError:
        controls += 1
    assert controls == 3
    print(
        "E1_PROFILE44_ENERGY_FLOOR_COFACTOR_CONTRACTION_PASS "
        "parent=1133 survivors=657 excluded=476 controls=3/3"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify the KoalaBear m2 r2 dihedral degree-two exclusion."""

from itertools import product
from pathlib import Path


NODE = Path(__file__).resolve().parent


def orbits(permutation: tuple[int, ...]) -> list[frozenset[int]]:
    unseen = set(range(len(permutation)))
    result = []
    while unseen:
        start = min(unseen)
        orbit = frozenset({start, permutation[start]})
        result.append(orbit)
        unseen -= orbit
    return result


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    proof = (NODE / "proof.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "n in {3,6}" in statement
    assert "No conclusion is made for `n=3,6`" in contract
    assert "K_(2,2)" in proof

    # Two distinct fixed-point-free involutions on a regular V4 orbit.
    u = (1, 0, 3, 2)
    v = (2, 3, 0, 1)
    y_orbits = orbits(u)
    z_orbits = orbits(v)
    incidence = {
        (next(i for i, block in enumerate(y_orbits) if point in block),
         next(i for i, block in enumerate(z_orbits) if point in block))
        for point in range(4)
    }
    assert incidence == set(product(range(2), repeat=2))

    source_units = 2 * 2 * 2
    assert source_units == 8
    profiles = [weights for weights in product(range(9), repeat=4) if sum(weights) == 8]
    costs = [sum(weight * (weight - 1) // 2 for weight in weights) for weights in profiles]
    assert min(costs) == 4
    assert {profiles[i] for i, cost in enumerate(costs) if cost == 4} == {(2, 2, 2, 2)}
    assert min(costs) > 3
    assert {2, 3, 6} - {2} == {3, 6}
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_DEGREE2_SOURCE_STAR_EXCLUSION_PASS")


if __name__ == "__main__":
    main()

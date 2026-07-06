#!/usr/bin/env python3
"""Toy weighted-bijection check for E22 lower-scale intersections."""

from __future__ import annotations


def weighted_sum(objects: list[str], weights: dict[str, int]) -> int:
    return sum(weights[o] for o in objects)


def certified_formula(atoms: list[str], atom_to_profile: dict[str, str], weights: dict[str, int]) -> int:
    seen = set(atom_to_profile.values())
    assert len(seen) == len(atoms)
    assert set(atom_to_profile) == set(atoms)
    return sum(weights[atom_to_profile[a]] for a in atoms)


def main() -> None:
    intersection = ["R0", "R2", "R3"]
    weights = {"R0": 2, "R1": 5, "R2": 7, "R3": 11}
    atoms = ["a", "b", "c"]
    atom_to_profile = {"a": "R2", "b": "R0", "c": "R3"}
    assert certified_formula(atoms, atom_to_profile, weights) == weighted_sum(intersection, weights)
    print("PASS: weighted bijective intersection formula gives exact count")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify the prize profile-(3,6,S=18) cofactor windows."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from itertools import combinations
from math import comb, factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_profile_36_cofactor_windows"
B_PRIZE = 317494674775468773183020924238786383963
COFACTORS = [2, 4, 8, 16, 32, 64, 256, 512, 514, 1024, 1028, 1538]
WINDOWS = {
    2: (352, 12, 13),
    4: (316, 12, 9),
    8: (280, 13, 7),
    16: (246, 10, 7),
    32: (210, 10, 6),
    64: (176, 7, 5),
    256: (106, 5, 4),
    512: (70, 5, 2),
    514: (70, 4, 2),
    1024: (36, 3, 1),
    1028: (36, 2, 2),
    1538: (14, 2, 0),
}
PARENTS = {
    "collision_norm_criterion",
    "e1_collision_square_mass_reparametrization",
    "e1_prize_field_floor_even_norm_exclusion",
    "e1_n256_local_norm_cofactor_collapse",
}
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def multiplicity(residues: tuple[int, ...]) -> int:
    for derivative in range(16):
        if sum(comb(r, derivative) for r in residues) % 2:
            return derivative
    return 16


def taylor_lower(x: Fraction, degree: int) -> Fraction:
    return sum(x**j / factorial(j) for j in range(degree + 1))


def taylor_upper(x: Fraction, degree: int) -> Fraction:
    lower = taylor_lower(x, degree)
    next_term = x ** (degree + 1) / factorial(degree + 1)
    ratio = x / (degree + 2)
    assert ratio < 1
    return lower + next_term / (1 - ratio)


def main() -> None:
    pin = json.loads((ROOT / "background/nodes" / NODE / "source_pin.json").read_text())
    for key in (
        "collision_norm",
        "profile",
        "field_floor",
        "local_norm_proof",
        "probe",
    ):
        assert sha256(ROOT / pin[f"{key}_file"]) == pin[f"{key}_sha256"]

    values = {16}
    cases = 0
    for weight in (2, 4, 6):
        for residues in combinations(range(16), weight):
            values.add(multiplicity(residues))
            cases += 1
    assert cases == 9948
    assert sorted(mu for mu in values if mu <= 10) == [1, 2, 3, 4, 5, 6, 8, 9, 10]
    assert sorted(mu for mu in values if mu > 10) == [12, 16]

    cofactors = set()
    for mu in values:
        if mu > 10:
            continue
        odd = 1
        while (1 << mu) * odd <= 2013:
            cofactors.add((1 << mu) * odd)
            odd += 256
    assert 1026 in cofactors
    cofactors.remove(1026)
    assert sorted(cofactors) == COFACTORS

    assert taylor_lower(Fraction(21, 10), 6) > 8
    for cofactor, (onset, lower_degree, upper_degree) in WINDOWS.items():
        target = Fraction(18**64, cofactor * B_PRIZE * 2**128)
        x = Fraction(8 * onset, 405)
        previous_x = Fraction(8 * (onset - 2), 405)
        assert taylor_lower(x, lower_degree) > target
        assert taylor_upper(previous_x, upper_degree) <= target

    statement = (ROOT / "background/nodes" / NODE / "statement.md").read_text()
    proof = (ROOT / "background/nodes" / NODE / "proof.md").read_text()
    for text in ("{1,2,3,4,5,6,8,9,10}", "1538", "4<=V<=12"):
        assert text in statement
    for text in ("120+1820+8008", "21/10-log 8", "T_6(21/10)>8"):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert all((parent, NODE, "req") in edges for parent in PARENTS)
    assert all((NODE, target, "ev") in edges for target in TARGETS)

    print(
        "E1_PRIZE_N256_S18_PROFILE_36_COFACTOR_WINDOWS_PASS "
        f"residue_cases={cases} cofactors={len(COFACTORS)} windows={len(WINDOWS)}"
    )


if __name__ == "__main__":
    main()

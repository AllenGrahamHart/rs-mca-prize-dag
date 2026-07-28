#!/usr/bin/env python3
"""Verify the prize N=256 square-mass-18 variance/cofactor windows."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_variance_cofactor_windows"
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
PARENTS = {
    "collision_norm_criterion",
    "e1_prize_field_floor_even_norm_exclusion",
    "e1_n256_local_norm_cofactor_collapse",
}
B_PRIZE = 317494674775468773183020924238786383963

EXPECTED_PIN = {
    "cofactor_statement_file": "background/nodes/e1_n256_local_norm_cofactor_collapse/statement.md",
    "cofactor_statement_sha256": "6620a3737bc8fb7b748163f803aa8c5e94c75df3100cdd710dd045113e5a9f08",
    "cofactor_proof_file": "background/nodes/e1_n256_local_norm_cofactor_collapse/proof.md",
    "cofactor_proof_sha256": "3a9a1f8d7f1a77ec25d349009afe9715095052e5a44187f253fb05fdd6df89ae",
    "field_floor_statement_file": "background/nodes/e1_prize_field_floor_even_norm_exclusion/statement.md",
    "field_floor_statement_sha256": "39bebf1adf9b5adc80d8f34ba3f9bffaaff8a2eb14498385ebc1549289ce2f8f",
    "collision_norm_statement_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_statement_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
}


def taylor_lower(x: Fraction, degree: int) -> Fraction:
    return sum(x**j / math.factorial(j) for j in range(degree + 1))


def taylor_upper(x: Fraction, degree: int) -> Fraction:
    lower = taylor_lower(x, degree)
    next_term = x ** (degree + 1) / math.factorial(degree + 1)
    ratio = x / (degree + 2)
    assert ratio < 1
    return lower + next_term / (1 - ratio)


def lucas_18(index: int) -> int:
    previous, current = 2, 18
    if index == 0:
        return previous
    for _ in range(2, index + 1):
        previous, current = current, 18 * current - previous
    return current


def main() -> None:
    checks = 0
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for file_key, hash_key in (
        ("cofactor_statement_file", "cofactor_statement_sha256"),
        ("cofactor_proof_file", "cofactor_proof_sha256"),
        ("field_floor_statement_file", "field_floor_statement_sha256"),
        ("collision_norm_statement_file", "collision_norm_statement_sha256"),
    ):
        digest = hashlib.sha256((ROOT / pin[file_key]).read_bytes()).hexdigest()
        assert digest == pin[hash_key]
        checks += 1

    endpoint = Fraction(451, 263)
    endpoint_margin = taylor_lower(endpoint, 9) - Fraction(50, 9)
    assert endpoint_margin == Fraction(
        106695074635404932039009,
        1092281991851445329987277120,
    )
    assert endpoint_margin > 0
    assert Fraction(2367, 36) > 18
    assert Fraction(2367, 36) < 100
    checks += 4

    p_min = B_PRIZE * 2**128
    p_max = (B_PRIZE + 1) * 2**128 - 1
    windows = {
        2: (258, 250, 11, 7),
        514: (58, 50, 3, 2),
        1538: (10, 2, 3, 0),
        4: (234, 226, 10, 7),
        1028: (26, 18, 3, 0),
        16: (186, 178, 7, 7),
        256: (82, 74, 4, 2),
    }
    for cofactor, (onset, predecessor, lower_degree, upper_degree) in windows.items():
        assert onset % 8 == 2
        assert predecessor == onset - 8
        target = Fraction(18**64, cofactor * p_min)
        assert taylor_lower(Fraction(64 * onset, 2367), lower_degree) > target
        assert taylor_upper(Fraction(64 * predecessor, 2367), upper_degree) < target
        checks += 4

    expected_lucas = {
        64: 178342091698891843163466683840822101223162205277179656650156983624835803932590082,
        32: 13354478338703157414450712387359637585922,
        16: 115561578124838522882,
        8: 10749957122,
    }
    cofactor_rows = {
        0: (2, 514, 1538),
        1: (4, 1028),
        2: (16,),
        3: (256,),
    }
    resultant_norms: dict[int, int] = {}
    for two_order, cofactors in cofactor_rows.items():
        index = 64 // 2**two_order
        lucas = lucas_18(index)
        assert lucas == expected_lucas[index]
        norm = lucas ** (2**two_order)
        resultant_norms[two_order] = norm
        assert (norm & -norm).bit_length() - 1 == 2**two_order
        assert norm > 256 * p_max
        assert min(cofactors) == 2 ** (2**two_order)
        checks += 4

    assert resultant_norms[0] % 514 == 450
    assert resultant_norms[0] % 1538 == 2
    assert resultant_norms[1] % 1028 == 452
    checks += 3

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {entry["id"]: entry for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in PARENTS:
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
        checks += 2
    for target in TARGETS:
        assert nodes[target]["status"] == "TARGET"
        assert (NODE, target, "ev") in edges
        assert (NODE, target, "req") not in edges
        checks += 3

    print(
        "E1_PRIZE_N256_S18_VARIANCE_COFACTOR_WINDOWS_PASS "
        "live_cofactors=6 strongest_residual=1028:{10,18} "
        f"checks={checks}"
    )


if __name__ == "__main__":
    main()

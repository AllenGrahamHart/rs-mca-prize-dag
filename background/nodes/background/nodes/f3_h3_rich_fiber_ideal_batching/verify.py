#!/usr/bin/env python3
"""Audit the exact boundary certificate for same-fiber ideal batching.

The general ideal sandwich is proved in proof.md. This stdlib replay checks
the finite-field fibers, exact norm divisibilities and gcds, resultant route
fence, DAG wiring, and mutation controls. It does not recompute FLINT
resultants locally.
"""

from __future__ import annotations

import copy
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CERTIFICATE = ROOT / "experiments/prize_resolution/h3_rich_norm_gcd_result.json"
DAG = ROOT / "dag.json"
NODE = "f3_h3_rich_fiber_ideal_batching"
CONSUMER = "f3_h3_mobius_excess_half"
ORDER = 8192
PRIME = 67_657_729
GENERATOR = 41_542_468
EXPECTED_PAIRS = {
    40_697_698: (
        (751, 2815), (758, 7217), (808, 2323), (918, 1027),
        (1905, 7976), (3738, 5802), (4230, 5745), (4648, 6769),
        (5526, 5635), (5795, 7528),
    ),
    16_650_852: (
        (216, 3544), (664, 7434), (975, 2397), (1423, 6287),
        (2390, 5377), (2447, 5869), (2557, 7165), (2666, 7274),
        (3962, 7384), (4454, 7441),
    ),
}
EXPECTED_RESULTANTS = {
    40_697_698: (752, 2906, 2880),
    16_650_852: (217, 3481, 3455),
}


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor <= math.isqrt(value):
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def p_valuation(value: int, prime: int) -> int:
    exponent = 0
    while value and value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def shifted_product(pair: tuple[int, int], generator: int, prime: int) -> int:
    left, right = pair
    return (
        (1 - pow(generator, left, prime))
        * (1 - pow(generator, right, prime))
    ) % prime


def validate_certificate(data: dict[str, object]) -> None:
    if data.get("schema") != "h3-rich-norm-gcd-v1":
        raise AssertionError("schema")
    if (data.get("order"), data.get("prime"), data.get("generator")) != (
        ORDER, PRIME, GENERATOR
    ):
        raise AssertionError("row")
    if not is_prime(PRIME) or PRIME % ORDER != 1:
        raise AssertionError("prime corridor")
    if pow(GENERATOR, ORDER, PRIME) != 1:
        raise AssertionError("generator power")
    if pow(GENERATOR, ORDER // 2, PRIME) == 1:
        raise AssertionError("generator order")

    targets = data.get("targets")
    if not isinstance(targets, list) or len(targets) != 2:
        raise AssertionError("target count")
    by_target = {int(row["target"]): row for row in targets}
    if set(by_target) != set(EXPECTED_PAIRS):
        raise AssertionError("targets")

    minimum = 4 * PRIME
    for target, expected_pairs in EXPECTED_PAIRS.items():
        row = by_target[target]
        pairs = tuple(tuple(int(x) for x in pair) for pair in row["pairs"])
        if pairs != expected_pairs:
            raise AssertionError((target, "pairs"))
        if len(set(pairs)) != 10:
            raise AssertionError((target, "pair uniqueness"))
        for pair in pairs:
            if not (0 < pair[0] <= pair[1] < ORDER):
                raise AssertionError((target, "pair range"))
            if shifted_product(pair, GENERATOR, PRIME) != target:
                raise AssertionError((target, "fiber"))

        norms = tuple(int(value) for value in row["norms"])
        if len(norms) != 9 or any(value <= 0 for value in norms):
            raise AssertionError((target, "norm count"))
        if any(value % minimum for value in norms):
            raise AssertionError((target, "4p divisibility"))
        if math.gcd(*norms[:2]) != minimum:
            raise AssertionError((target, "two-generator saturation"))
        if math.gcd(*norms) != minimum:
            raise AssertionError((target, "all-generator saturation"))
        if int(row["gcd"]) != minimum:
            raise AssertionError((target, "stored gcd"))
        if int(row["cofactor"]) != 4 or int(row["p_valuation"]) != 1:
            raise AssertionError((target, "stored factorization"))

        reduced = row["reduced_resultant"]
        common_degree, bits, cofactor_bits = EXPECTED_RESULTANTS[target]
        resultant = int(reduced["resultant"])
        if int(reduced["target"]) != target:
            raise AssertionError((target, "resultant target"))
        if (int(reduced["common_degree"]), int(reduced["common_terms"])) != (
            common_degree, 2
        ):
            raise AssertionError((target, "rational gcd"))
        if resultant <= 0 or resultant.bit_length() != bits:
            raise AssertionError((target, "resultant bits"))
        if p_valuation(resultant, PRIME) != 1:
            raise AssertionError((target, "resultant valuation"))
        if (resultant // PRIME).bit_length() != cofactor_bits:
            raise AssertionError((target, "resultant cofactor"))
        if (int(reduced["resultant_bits"]), int(reduced["p_valuation"]),
                int(reduced["cofactor_bits"])) != (bits, 1, cofactor_bits):
            raise AssertionError((target, "stored resultant summary"))


def validate_dag(data: dict[str, object]) -> None:
    nodes = {row["id"]: row for row in data["nodes"]}
    if nodes.get(NODE, {}).get("status") != "PROVED":
        raise AssertionError("DAG node status")
    edges = {(row["from"], row["to"], row["kind"]) for row in data["edges"]}
    if ("f3_h3_shifted_product_sidon", NODE, "req") not in edges:
        raise AssertionError("DAG dependency")
    if (NODE, CONSUMER, "ev") not in edges:
        raise AssertionError("DAG evidence edge")


def mutation_controls(certificate: dict[str, object], dag: dict[str, object]) -> int:
    mutations = []
    changed = copy.deepcopy(certificate)
    changed["schema"] = "h3-rich-norm-gcd-v0"
    mutations.append((validate_certificate, changed))
    changed = copy.deepcopy(certificate)
    changed["targets"][0]["target"] += 1
    mutations.append((validate_certificate, changed))
    changed = copy.deepcopy(certificate)
    changed["targets"][0]["pairs"][0][0] += 1
    mutations.append((validate_certificate, changed))
    changed = copy.deepcopy(certificate)
    changed["targets"][0]["norms"][0] = str(4 * PRIME + 1)
    mutations.append((validate_certificate, changed))
    changed = copy.deepcopy(certificate)
    changed["targets"][0]["gcd"] = str(8 * PRIME)
    mutations.append((validate_certificate, changed))
    changed = copy.deepcopy(certificate)
    changed["targets"][0]["reduced_resultant"]["resultant"] = str(PRIME + 1)
    mutations.append((validate_certificate, changed))
    changed_dag = copy.deepcopy(dag)
    next(row for row in changed_dag["nodes"] if row["id"] == NODE)["status"] = "TARGET"
    mutations.append((validate_dag, changed_dag))

    caught = 0
    for validator, mutation in mutations:
        try:
            validator(mutation)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    if caught != len(mutations):
        raise AssertionError(("mutation controls", caught, len(mutations)))
    return caught


def main() -> None:
    certificate = json.loads(CERTIFICATE.read_text())
    dag = json.loads(DAG.read_text())
    validate_certificate(certificate)
    validate_dag(dag)
    caught = mutation_controls(certificate, dag)
    print(
        "H3_RICH_FIBER_IDEAL_BATCHING_PASS "
        f"targets=2 pairs=20 norms=18 gcd=4p mutations={caught}/7"
    )


if __name__ == "__main__":
    main()

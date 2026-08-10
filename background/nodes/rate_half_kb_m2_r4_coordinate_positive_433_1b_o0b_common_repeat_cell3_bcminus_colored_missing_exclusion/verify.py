#!/usr/bin/env python3
"""Verify the complete cell-3 BC- colored missing-edge exclusion."""

from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
PREFIX = "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcminus_"
NORM_RESULT = PREFIX + "colored_norm_result.json"
REPLAY_LAUNCHER = PREFIX + "colored_finite_replay_modal.py"
REPLAY_RESULT = PREFIX + "colored_finite_replay_result.json"
HASHES = {
    NORM_RESULT: "323507a457f1fa34a0e1f9ad77cdfae34ee8ff21c56551ebf32234ce7d64d687",
    REPLAY_LAUNCHER: "fe1eac5ccd59095c9a0e5d3bf73533b532668a83fff44657c48a811645c11c38",
    REPLAY_RESULT: "e0d77b9d4d70d1aa1c809c991c361e03e359e7fbfefbc48d4eb06137dd8d6459",
}
PARENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_"
    "cell3_bcminus_colored_norm_atlas"
)
CONSUMER = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_"
    "cells3_6_bcminus_complete_outside_exclusion"
)
PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def trim(polynomial):
    output = [value % PRIME for value in polynomial]
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output or [0]


def poly_sub(left, right):
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else 0)
        - (right[index] if index < len(right) else 0)
        for index in range(size)
    ])


def poly_mul(left, right):
    output = [0] * (len(left) + len(right) - 1)
    for left_degree, left_value in enumerate(left):
        for right_degree, right_value in enumerate(right):
            output[left_degree + right_degree] = (
                output[left_degree + right_degree] + left_value * right_value
            ) % PRIME
    return trim(output)


def poly_divmod(numerator, denominator):
    numerator = trim(numerator)
    denominator = trim(denominator)
    require(denominator != [0], "zero polynomial divisor")
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
    denominator_inverse = pow(denominator[-1], -1, PRIME)
    while numerator != [0] and len(numerator) >= len(denominator):
        shift = len(numerator) - len(denominator)
        scalar = numerator[-1] * denominator_inverse % PRIME
        quotient[shift] = scalar
        for index, value in enumerate(denominator):
            numerator[index + shift] = (
                numerator[index + shift] - scalar * value
            ) % PRIME
        numerator = trim(numerator)
    return trim(quotient), numerator


def monic(polynomial):
    polynomial = trim(polynomial)
    if polynomial == [0]:
        return polynomial
    inverse = pow(polynomial[-1], -1, PRIME)
    return trim([value * inverse for value in polynomial])


def poly_gcd(left, right):
    left, right = trim(left), trim(right)
    while right != [0]:
        _, remainder = poly_divmod(left, right)
        left, right = right, remainder
    return monic(left)


def poly_mod(polynomial, modulus):
    return poly_divmod(polynomial, modulus)[1]


def poly_pow_mod(base, exponent, modulus):
    output = [1]
    base = poly_mod(base, modulus)
    while exponent:
        if exponent & 1:
            output = poly_mod(poly_mul(output, base), modulus)
        base = poly_mod(poly_mul(base, base), modulus)
        exponent //= 2
    return output


def poly_eval(polynomial, value):
    output = 0
    for coefficient in reversed(polynomial):
        output = (output * value + coefficient) % PRIME
    return output


ROOT_CACHE = {}


def validate_complete_roots(polynomial, roots, message):
    polynomial = trim(polynomial)
    require(roots == sorted(set(roots)), message + " ordering")
    require(all(poly_eval(polynomial, value) == 0 for value in roots),
            message + " evaluation")
    listed = [1]
    for value in roots:
        listed = poly_mul(listed, [-value, 1])
    key = tuple(polynomial)
    if key not in ROOT_CACHE:
        field_part = poly_gcd(
            polynomial,
            poly_sub(poly_pow_mod([0, 1], PRIME, polynomial), [0, 1]),
        )
        ROOT_CACHE[key] = field_part
    require(ROOT_CACHE[key] == monic(listed), message + " completeness")


def canonical_incidence(rows):
    return sorted(
        (tuple(row["epsilon"]), row["missing_record"],
         row["kind"], row["identity"])
        for row in rows
    )


def validate(norms, replay):
    require(norms["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cell3-bcminus-colored-norm-v1",
            "norm schema")
    require(replay["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cell3-bcminus-colored-finite-replay-v1",
            "replay schema")
    require(replay["source_norms_sha256"] == HASHES[NORM_RESULT],
            "source custody")
    norm_rows = {
        (tuple(row["epsilon"]), row["missing_record"]): row
        for row in norms["rows"]
    }
    ledger_rows = {}
    for row in replay["root_ledger"]:
        key = (tuple(row["epsilon"]), row["missing_record"],
               row["kind"], row["identity"])
        require(key not in ledger_rows, "duplicate ledger row")
        ledger_rows[key] = row
    expected_polynomials = {}
    for case, row in norm_rows.items():
        expected_polynomials[case + ("CUT_NORM_NUMERATOR", "numerator")] = (
            row["cut_norm_numerator"]
        )
        expected_polynomials[case + ("CUT_NORM_DENOMINATOR", "denominator")] = (
            row["cut_norm_denominator"]
        )
        for digest, coefficients in row["construction_guards"].items():
            expected_polynomials[case + ("CONSTRUCTION_GUARD", digest)] = coefficients
    require(set(ledger_rows) == set(expected_polynomials) and
            len(ledger_rows) == 48, "ledger coverage")

    incidence = defaultdict(list)
    root_profile = Counter()
    for key, polynomial in expected_polynomials.items():
        row = ledger_rows[key]
        require(row["degree"] == len(polynomial) - 1, "ledger degree")
        validate_complete_roots(polynomial, row["roots"], "ledger roots")
        root_profile[(row["kind"], len(row["roots"]))] += 1
        for value in row["roots"]:
            incidence[value].append({
                "epsilon": list(key[0]), "missing_record": key[1],
                "kind": key[2], "identity": key[3],
            })
    require(root_profile == Counter({
        ("CUT_NORM_NUMERATOR", 5): 8,
        ("CUT_NORM_DENOMINATOR", 2): 8,
        ("CONSTRUCTION_GUARD", 2): 16,
        ("CONSTRUCTION_GUARD", 3): 16,
    }), "root profile")
    require(sum(map(len, incidence.values())) == 136 and len(incidence) == 8,
            "incidence census")

    rows = replay["rows"]
    require(replay["q_count"] == len(rows) == 8, "q count")
    require([row["q"] for row in rows] == sorted(incidence), "q union")
    statuses = Counter(row["status"] for row in rows)
    require(statuses == Counter({
        "PROJECTION_DENOMINATOR_BOUNDARY": 3,
        "NO_BASE_FIELD_Y": 2,
        "NO_GUARDED_COMMON_POINT": 3,
    }) and replay["status_counts"] == dict(sorted(statuses.items())),
            "status census")
    for row in rows:
        q_value = row["q"]
        require(canonical_incidence(row["incidence"]) ==
                canonical_incidence(incidence[q_value]), "row incidence")
        q2 = q_value * q_value % PRIME
        q3 = q2 * q_value % PRIME
        numerator = (q3 + 2 * q2 + q_value + 4) % PRIME
        denominator = (q3 + 6 * q2 + q_value) % PRIME
        require((row["numerator"], row["denominator"]) ==
                (numerator, denominator), "tower specialization")
        if denominator == 0:
            require(row["status"] == "PROJECTION_DENOMINATOR_BOUNDARY" and
                    row["y_rows"] == [], "projection boundary")
            continue
        y_square = numerator * pow(denominator, -1, PRIME) % PRIME
        require(row["y_square"] == y_square, "y square")
        validate_complete_roots([-y_square, 0, 1], row["y_values"], "y roots")
        require([item["y"] for item in row["y_rows"]] == row["y_values"],
                "y row coverage")
        if not row["y_values"]:
            require(row["status"] == "NO_BASE_FIELD_Y", "empty y status")
            continue
        for y_row in row["y_rows"]:
            y_value = y_row["y"]
            if (y_value - 1) % PRIME == 0 or (q_value * y_value - 1) % PRIME == 0:
                require(y_row["status"] == "MOBIUS_DENOMINATOR_BOUNDARY",
                        "Mobius boundary")
                continue
            b_value = ((q_value * y_value + 1)
                       * pow(q_value * y_value - 1, -1, PRIME)) % PRIME
            c_value = ((y_value + 1) * pow(y_value - 1, -1, PRIME)) % PRIME
            require((y_row["b"], y_row["c"]) == (b_value, c_value),
                    "Mobius replay")
            target_guard = (
                b_value * c_value * (b_value - 1) * (b_value + 1)
                * (c_value - 1) * (c_value + 1)
                * (b_value - c_value) * (b_value + c_value)
            ) % PRIME
            require(target_guard == 0 or (b_value * c_value - 1) % PRIME == 0,
                    "unexpected guarded y")
            require(y_row["status"] == "TARGET_GUARD_BOUNDARY",
                    "target boundary status")
        require(row["status"] == "NO_GUARDED_COMMON_POINT" and
                row["guarded_point_count"] == 0, "guarded point status")
    require(replay["guarded_point_count"] == 0 and
            replay["cut_zero_points"] == [], "survivor census")


def main():
    for filename, digest in HASHES.items():
        require(hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
                == digest, f"file custody {filename}")
    norms = json.loads((EXPERIMENTS / NORM_RESULT).read_text())
    replay = json.loads((EXPERIMENTS / REPLAY_RESULT).read_text())
    validate(norms, replay)
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require(nodes[PARENT]["status"] == "PROVED" and
            (PARENT, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer edge")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELL3_BCMINUS_COLORED_EXCLUSION_VERIFY_PASS ledger=48 incidences=136 q=8 systems=240")


if __name__ == "__main__":
    main()

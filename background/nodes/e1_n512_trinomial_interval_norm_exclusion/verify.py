#!/usr/bin/env python3
"""Verify the complete N=512 trinomial interval-norm certificate."""

from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from itertools import combinations, product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n512_trinomial_interval_norm_exclusion"
L2_PARENT = "e1_prime_field_l2_norm_collision_radius"
FOUR_PARENT = "e1_n512_four_singleton_collision_exclusion"
NORM_PARENT = "collision_norm_criterion"
E1_TARGET = "e1_official_prime_exception_control"
UNIVERSAL_TARGET = "unsafe_crossing_family_instantiation"
ORDER = 512
HALF = ORDER // 2
PRIZE_BUDGET = 317494674775468773183020924238786383963
NAMED_INTERVALS = (
    (1 << 250, (1 << 250) + (1 << 128) - 1),
    (PRIZE_BUDGET << 128, ((PRIZE_BUDGET + 1) << 128) - 1),
)

EXPECTED_PIN = {
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "four_singleton_file": "background/nodes/e1_n512_four_singleton_collision_exclusion/statement.md",
    "four_singleton_file_sha256": "153d2997c0fc92d439abf4dabaf366e119750f08f1a9122162dc7c353d241676",
    "l2_radius_file": "background/nodes/e1_prime_field_l2_norm_collision_radius/statement.md",
    "l2_radius_file_sha256": "ed607ee0d843c1f2c74c79129d19ef8d52be96ba2a8ceb77d35014f95d852995",
}


def canonical_pair(left: int, right: int, left_sign: int, right_sign: int):
    if left > right:
        return right, left, right_sign, left_sign
    return left, right, left_sign, right_sign


def conjugate(state, unit: int):
    terms = []
    for exponent, sign in zip(state[:2], state[2:]):
        residue = unit * exponent % ORDER
        if residue >= HALF:
            residue -= HALF
            sign = -sign
        assert 0 < residue < HALF
        assert sign in (-1, 1)
        terms.append((residue, sign))
    terms.sort()
    assert terms[0][0] < terms[1][0]
    return terms[0][0], terms[1][0], terms[0][1], terms[1][1]


def orbit_representatives():
    universe = {
        canonical_pair(left, right, left_sign, right_sign)
        for left, right in combinations(range(1, HALF), 2)
        for left_sign, right_sign in product((-1, 1), repeat=2)
    }
    states = set(universe)
    seen = set()
    representatives = []
    orbit_sizes = []
    units = tuple(range(1, ORDER, 2))
    while states:
        representative = min(states)
        orbit = {conjugate(representative, unit) for unit in units}
        assert orbit <= universe
        assert not orbit & seen
        representatives.append(representative)
        orbit_sizes.append(len(orbit))
        seen.update(orbit)
        states.difference_update(orbit)
    assert seen == universe
    assert sum(orbit_sizes) == 4 * int(sp.binomial(HALF - 1, 2))
    return representatives, orbit_sizes


def negacyclic_variance(state) -> int:
    left, right, left_sign, right_sign = state
    support = (0, left, right)
    values = (2, left_sign, right_sign)
    coefficients = [0] * HALF
    for source, source_value in zip(support, values):
        for target, target_value in zip(support, values):
            quotient, residue = divmod(source - target, HALF)
            coefficients[residue] += (
                -1 if quotient % 2 else 1
            ) * source_value * target_value
    coefficients[0] -= 6
    return sum(value * value for value in coefficients)


def interval_divisor_screen(norm_groups):
    window_integers = 0
    max_window_width = 0
    divisible_records = []
    candidate_primes = set()
    for norm, states in norm_groups.items():
        for interval_index, (lower, upper) in enumerate(NAMED_INTERVALS):
            cofactor_low = (norm + upper - 1) // upper
            cofactor_high = norm // lower
            width = max(0, cofactor_high - cofactor_low + 1)
            max_window_width = max(max_window_width, width)
            window_integers += width
            for cofactor in range(cofactor_low, cofactor_high + 1):
                if cofactor == 0 or norm % cofactor:
                    continue
                quotient = norm // cofactor
                assert lower <= quotient <= upper
                quotient_mod = quotient % ORDER
                quotient_is_prime = False if quotient_mod == 0 else bool(sp.isprime(quotient))
                divisible_records.append(
                    {
                        "interval": interval_index,
                        "state": list(states[0]),
                        "norm": norm,
                        "cofactor": cofactor,
                        "quotient": quotient,
                        "quotient_is_prime": quotient_is_prime,
                        "quotient_mod_512": quotient_mod,
                    }
                )
                if quotient_is_prime and quotient_mod == 1:
                    candidate_primes.add(quotient)
    payload = {
        "norms_screened": len(norm_groups),
        "intervals_per_norm": len(NAMED_INTERVALS),
        "window_integers": window_integers,
        "max_window_width": max_window_width,
        "divisible_records": divisible_records,
        "candidate_primes": sorted(candidate_primes),
    }
    digest_payload = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["screen_sha256"] = hashlib.sha256(digest_payload).hexdigest()
    return payload


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for file_key, hash_key in (
        ("collision_norm_file", "collision_norm_file_sha256"),
        ("four_singleton_file", "four_singleton_file_sha256"),
        ("l2_radius_file", "l2_radius_file_sha256"),
    ):
        assert hashlib.sha256((ROOT / pin[file_key]).read_bytes()).hexdigest() == pin[hash_key]

    certificate = json.loads(Path(__file__).with_name("certificate.json").read_text())
    assert certificate["intervals"] == [list(interval) for interval in NAMED_INTERVALS]
    representatives, orbit_sizes = orbit_representatives()
    variable = sp.symbols("x")
    cyclotomic = variable**HALF + 1
    rows = []
    norm_groups = defaultdict(list)
    variance_histogram = Counter()
    for state in representatives:
        left, right, left_sign, right_sign = state
        polynomial = 2 + left_sign * variable**left + right_sign * variable**right
        norm = abs(int(sp.resultant(cyclotomic, polynomial, variable)))
        assert norm > 0
        row = {
            "state": state,
            "variance": negacyclic_variance(state),
            "norm": norm,
            "bits": norm.bit_length(),
        }
        rows.append(row)
        norm_groups[norm].append(state)
        variance_histogram[row["variance"]] += 1

    canonical_rows = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    computed = {
        "normalized_state_count": sum(orbit_sizes),
        "orbit_representatives": len(representatives),
        "orbit_size_histogram": {str(k): v for k, v in sorted(Counter(orbit_sizes).items())},
        "distinct_norms": len(norm_groups),
        "below_2^250": sum(row["norm"] < 1 << 250 for row in rows),
        "at_least_2^250": sum(row["norm"] >= 1 << 250 for row in rows),
        "max_norm_bits": max(row["bits"] for row in rows),
        "variance_histogram": {str(k): v for k, v in sorted(variance_histogram.items())},
        "rows_sha256": hashlib.sha256(canonical_rows).hexdigest(),
    }
    for key, value in computed.items():
        assert certificate[key] == value

    interval_result = interval_divisor_screen(norm_groups)
    assert interval_result == certificate["interval_screen"]
    assert interval_result["candidate_primes"] == []
    assert interval_result["max_window_width"] == 1
    assert len(interval_result["divisible_records"]) == 1
    assert interval_result["divisible_records"][0]["quotient_mod_512"] == 0

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[L2_PARENT] == "PROVED"
    assert statuses[FOUR_PARENT] == "PROVED"
    assert statuses[NORM_PARENT] == "PROVED"
    assert statuses[E1_TARGET] == "TARGET"
    assert statuses[UNIVERSAL_TARGET] == "TARGET"
    assert (L2_PARENT, NODE, "req") in edges
    assert (FOUR_PARENT, NODE, "req") in edges
    assert (NORM_PARENT, NODE, "req") in edges
    assert (NODE, E1_TARGET, "ev") in edges
    assert (NODE, UNIVERSAL_TARGET, "ev") in edges
    assert "129540" in statements[NODE]
    assert "s>=3" in statements[NODE]

    print(
        "E1_N512_TRINOMIAL_INTERVAL_NORM_EXCLUSION_PASS "
        "states=129540 orbits=748 norms=746 window_integers=4 candidate_primes=0"
    )


if __name__ == "__main__":
    main()

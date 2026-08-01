#!/usr/bin/env python3
"""Exact residual-gauge quotient of the positive 433-1a outside ledger."""

import argparse
import copy
import hashlib
import itertools
import json
from pathlib import Path


RECORDS = ("DE+", "DE-", "DF+", "DF-", "EF", "BE", "CF")
INTERNAL = RECORDS[:5]
VERTICES = ("A", "B", "C", "D", "E", "F")
TAU = {
    "DE+": "DE-",
    "DE-": "DE+",
    "DF+": "DF-",
    "DF-": "DF+",
    "EF": "EF",
    "BE": "BE",
    "CF": "CF",
}
RESULT = Path(__file__).with_name(
    "rate_half_kb_positive_433_1a_outside_case_symmetry_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def payload_hash(value):
    clone = copy.deepcopy(value)
    clone.pop("payload_sha256", None)
    return hashlib.sha256(canonical_json(clone).encode()).hexdigest()


def perfect_matchings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        rest = values[1:index] + values[index + 1:]
        for tail in perfect_matchings(rest):
            yield canonical_matching(((first, values[index]), *tail))


def canonical_matching(matching):
    order = {record: index for index, record in enumerate(RECORDS)}
    pairs = [tuple(sorted(pair, key=order.get)) for pair in matching]
    return tuple(sorted(pairs, key=lambda pair: (order[pair[0]], order[pair[1]])))


def cases(alignment):
    output = set()
    for eta in INTERNAL:
        xi_values = (eta,) if alignment == "aligned" else tuple(
            record for record in RECORDS if record != eta
        )
        for xi in xi_values:
            residual = tuple(record for record in RECORDS if record != xi)
            for matching in perfect_matchings(residual):
                output.add((eta, xi, matching))
    return output


def tau_case(case):
    eta, xi, matching = case
    return (
        TAU[eta],
        TAU[xi],
        canonical_matching(tuple((TAU[left], TAU[right])
                                 for left, right in matching)),
    )


def case_key(case):
    order = {record: index for index, record in enumerate(RECORDS)}
    eta, xi, matching = case
    return (
        order[eta],
        order[xi],
        tuple((order[left], order[right]) for left, right in matching),
    )


def orbit_partition(values):
    unseen = set(values)
    output = []
    while unseen:
        seed = min(unseen, key=case_key)
        orbit = {seed, tau_case(seed)}
        require(orbit <= values, "gauge closure")
        unseen -= orbit
        output.append(tuple(sorted(orbit, key=case_key)))
    return tuple(sorted(output, key=lambda orbit: case_key(orbit[0])))


def encoded_case(case):
    eta, xi, matching = case
    return {
        "eta": eta,
        "xi": xi,
        "matching": [list(pair) for pair in matching],
    }


def gauge_stabilizer():
    stabilizer = []
    induced = set()
    index = {vertex: position for position, vertex in enumerate(VERTICES)}
    for signs in itertools.product((-1, 1), repeat=len(VERTICES)):
        sign = {vertex: signs[index[vertex]] for vertex in VERTICES}
        constraints = (
            sign["A"] * sign["B"],
            sign["A"] * sign["C"],
            sign["B"] * sign["E"],
            sign["C"] * sign["F"],
            sign["E"] * sign["F"],
        )
        if constraints != (1, 1, 1, 1, 1):
            continue
        stabilizer.append(signs)
        induced.add("tau" if sign["D"] * sign["E"] == -1 else "identity")
    require(len(stabilizer) == 4, "raw gauge stabilizer")
    require(induced == {"identity", "tau"}, "induced gauge quotient")
    return {
        "raw_vertex_sign_stabilizer_size": len(stabilizer),
        "global_sign_kernel_size": 2,
        "faithful_record_action_size": len(induced),
        "nontrivial_action": "DE+<->DE-, DF+<->DF-, EF/BE/CF fixed",
    }


def template_cases(alignment):
    matching_a = canonical_matching((
        ("DE+", "DF-"), ("DE-", "CF"), ("DF+", "BE"),
    ))
    matching_b = canonical_matching((
        ("DE+", "CF"), ("DE-", "DF+"), ("DF-", "BE"),
    ))
    require(canonical_matching(tuple((TAU[left], TAU[right])
                                     for left, right in matching_a))
            == matching_b, "template gauge equivalence")
    eta_values = ("EF",) if alignment == "aligned" else INTERNAL[:4]
    values = {
        (eta, "EF", matching)
        for eta in eta_values for matching in (matching_a, matching_b)
    }
    require(values <= cases(alignment), f"{alignment} template cases")
    return values


def compile_result():
    aligned = cases("aligned")
    near = cases("near")
    require(len(aligned) == 75, "aligned count")
    require(len(near) == 450, "near count")
    require(len(aligned) + len(near) == 525, "formal ledger count")

    aligned_orbits = orbit_partition(aligned)
    near_orbits = orbit_partition(near)
    aligned_fixed = sum(len(orbit) == 1 for orbit in aligned_orbits)
    near_fixed = sum(len(orbit) == 1 for orbit in near_orbits)
    require((aligned_fixed, near_fixed) == (3, 6), "Burnside fixed cases")
    require((len(aligned_orbits), len(near_orbits)) == (39, 228),
            "orbit counts")

    ef_aligned = {case for case in aligned if case[1] == "EF"}
    ef_near = {case for case in near if case[1] == "EF"}
    ef_aligned_orbits = orbit_partition(ef_aligned)
    ef_near_orbits = orbit_partition(ef_near)
    require((len(ef_aligned), len(ef_near)) == (15, 60), "EF case counts")
    require((len(ef_aligned_orbits), len(ef_near_orbits)) == (9, 30),
            "EF orbit counts")

    templates_aligned = template_cases("aligned")
    templates_near = template_cases("near")
    template_aligned_orbits = orbit_partition(templates_aligned)
    template_near_orbits = orbit_partition(templates_near)
    require((len(template_aligned_orbits), len(template_near_orbits)) == (1, 4),
            "template orbit counts")

    data = {
        "schema": "rate-half-kb-positive-433-1a-outside-case-symmetry-v1",
        "scope": (
            "formal outside eta/xi/matching cases per fixed common row and "
            "cycle sign; no algebraic realizability or route conclusion"
        ),
        "records": list(RECORDS),
        "internal_eta_records": list(INTERNAL),
        "gauge_stabilizer": gauge_stabilizer(),
        "ledger": {
            "aligned": {
                "labeled_cases": len(aligned),
                "fixed_cases": aligned_fixed,
                "orbits": len(aligned_orbits),
            },
            "near": {
                "labeled_cases": len(near),
                "fixed_cases": near_fixed,
                "orbits": len(near_orbits),
            },
            "total": {
                "labeled_cases": len(aligned) + len(near),
                "orbits": len(aligned_orbits) + len(near_orbits),
            },
        },
        "missing_mate_EF": {
            "aligned_labeled_cases": len(ef_aligned),
            "aligned_orbits": len(ef_aligned_orbits),
            "near_labeled_cases": len(ef_near),
            "near_orbits": len(ef_near_orbits),
            "total_orbits": len(ef_aligned_orbits) + len(ef_near_orbits),
            "current_templates": {
                "A_and_B_are_one_gauge_orbit": True,
                "aligned_orbits": len(template_aligned_orbits),
                "near_orbits": len(template_near_orbits),
                "total_orbits": len(template_aligned_orbits)
                + len(template_near_orbits),
                "uncovered_orbits": (
                    len(ef_aligned_orbits) + len(ef_near_orbits)
                    - len(template_aligned_orbits) - len(template_near_orbits)
                ),
            },
        },
        "representatives": {
            "aligned": [
                {"orbit_size": len(orbit), **encoded_case(orbit[0])}
                for orbit in aligned_orbits
            ],
            "near": [
                {"orbit_size": len(orbit), **encoded_case(orbit[0])}
                for orbit in near_orbits
            ],
        },
        "nonclaims": [
            "the 267 formal orbits are not algebraic survivor counts",
            "duplicate-role and common-root-sign quotients are not composed here",
            "the two current EF templates cover only five of 39 formal EF orbits",
            "no outside system, alignment branch, 433-1a route, K3 row, or Prize result is closed",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    arguments = parser.parse_args()
    expected = compile_result()
    if arguments.write:
        RESULT.write_text(json.dumps(expected, indent=2, sort_keys=True) + "\n")
    if arguments.check or not arguments.write:
        observed = json.loads(RESULT.read_text())
        require(payload_hash(observed) == observed.get("payload_sha256"),
                "result seal")
        require(observed == expected, "result content")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_OUTSIDE_CASE_SYMMETRY_PASS "
        f"labeled={expected['ledger']['total']['labeled_cases']} "
        f"orbits={expected['ledger']['total']['orbits']} "
        f"aligned={expected['ledger']['aligned']['orbits']} "
        f"near={expected['ledger']['near']['orbits']} "
        f"ef={expected['missing_mate_EF']['total_orbits']} "
        f"template_covered={expected['missing_mate_EF']['current_templates']['total_orbits']}"
    )


if __name__ == "__main__":
    main()

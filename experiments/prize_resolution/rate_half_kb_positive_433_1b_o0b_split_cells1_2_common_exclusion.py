#!/usr/bin/env python3
"""Transport and recount common emptiness of O0b split cells 1 and 2."""

from collections import Counter
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT = HERE / "rate_half_kb_positive_433_1b_cells1_2_principal_common_charts_result.json"
S0_PATH = HERE / "rate_half_kb_positive_433_1b_o0b_s0_v4_label_quotient.py"
REPEATED_PATH = HERE / "rate_half_kb_positive_433_1b_o0b_repeated_outside_v4_quotient.py"
RESULT_SHA256 = "a466fa1850647a8bfa9a988229f8d3f8f03bd510ca739edb6cf256315b22531a"
ROLE_SHAPES = {
    1: ("LA", [["AB", "BC+"], ["AC", "BC-"]]),
    2: ("LA", [["AB", "BC-"], ["AC", "BC+"]]),
}


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


S0 = load("o0b_s0_v4", S0_PATH)
REPEATED = load("o0b_repeated_v4", REPEATED_PATH)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-principal-common-charts-v1",
            "chart schema")
    require(payload["case_count"] == 48 and len(payload["rows"]) == 48 and
            payload["status_counts"] == {"COMPLETE": 48} and
            payload["unit_count"] == 48 and payload["nonunit_count"] == 0,
            "chart aggregate")
    expected = set(itertools.product((1, 2), (-1, 1), (-1, 1), range(6)))
    actual = set()
    program_hashes = set()
    for row in payload["rows"]:
        key = (row["cell"], *row["epsilon"], row["chart"])
        require(key not in actual, "duplicate chart")
        actual.add(key)
        require((row["singleton"], row["matching"]) == ROLE_SHAPES[row["cell"]],
                "role shape")
        require(row["status"] == "COMPLETE" and row["unit"] is True and
                row["dimension"] == -1 and row["basis_size"] == 1 and
                "UNIT=1" in row["stdout"] and "END" in row["stdout"] and
                not row["stderr"], "unit chart")
        program_hashes.add(row["program_sha256"])
    require(actual == expected and len(program_hashes) == 48,
            "chart Cartesian cover")
    return len(actual)


def orbit_profile(rows, first_action, second_action):
    rows = set(rows)
    require({first_action(row) for row in rows} == rows, "first action closure")
    require({second_action(row) for row in rows} == rows, "second action closure")
    require(all(first_action(first_action(row)) == row for row in rows),
            "first action involution")
    require(all(second_action(second_action(row)) == row for row in rows),
            "second action involution")
    require(all(first_action(second_action(row)) ==
                second_action(first_action(row)) for row in rows),
            "commuting actions")
    unseen = set(rows)
    profile = Counter()
    while unseen:
        seed = min(unseen)
        orbit = {
            seed, first_action(seed), second_action(seed),
            first_action(second_action(seed)),
        }
        require(orbit <= rows, "orbit cover")
        unseen -= orbit
        profile[len(orbit)] += 1
    return dict(sorted(profile.items()))


def verify_quotient(s0_d_permutation=S0.D_PERMUTATION,
                    duplicate_permutations=REPEATED.DUPLICATE_PERMUTATIONS):
    matching_rows = tuple(S0.BC.pairings(range(6)))
    labels = tuple(itertools.product(range(7), range(15)))
    signs = tuple(itertools.product((-1, 1), repeat=2))
    s0_rows = {
        ("S0", sigma_o, cell, epsilon_1, epsilon_2, xi, matching)
        for sigma_o, cell, (epsilon_1, epsilon_2), (xi, matching) in
        itertools.product((-1, 1), (1, 2), signs, labels)
    }
    s0_profile = orbit_profile(
        s0_rows,
        lambda row: S0.bc_action(row, matching_rows),
        lambda row: S0.d_action(row, s0_d_permutation),
    )
    require(len(s0_rows) == 1680 and s0_profile == {2: 72, 4: 384},
            "cells1/2 S0 quotient")

    repeated_rows = {
        (lane, sigma_o, cell, epsilon_1, epsilon_2, xi, matching)
        for lane, sigma_o, cell, (epsilon_1, epsilon_2), (xi, matching) in
        itertools.product(("SDE", "SDF"), (-1, 1), (1, 2), signs, labels)
    }
    repeated_profile = orbit_profile(
        repeated_rows,
        lambda row: REPEATED.bc_action(row, matching_rows),
        lambda row: REPEATED.duplicate_action(row, duplicate_permutations),
    )
    require(len(repeated_rows) == 3360 and
            repeated_profile == {2: 240, 4: 720},
            "cells1/2 repeated-lane quotient")
    return s0_profile, repeated_profile


def verify(s0_d_permutation=S0.D_PERMUTATION,
           duplicate_permutations=REPEATED.DUPLICATE_PERMUTATIONS):
    require(hashlib.sha256(RESULT.read_bytes()).hexdigest() == RESULT_SHA256,
            "chart result custody")
    charts = validate_payload(json.loads(RESULT.read_text()))
    s0_profile, repeated_profile = verify_quotient(
        s0_d_permutation, duplicate_permutations
    )
    raw_closed = 2 * 4 * 6 * 105
    representatives_closed = (sum(s0_profile.values()) +
                              sum(repeated_profile.values()))
    require(raw_closed == 5040 and representatives_closed == 1416,
            "closure census")
    return {
        "charts": charts,
        "raw_closed": raw_closed,
        "representatives_closed": representatives_closed,
        "s0_profile": s0_profile,
        "repeated_profile": repeated_profile,
        "owner_raw_remaining": 36960 - raw_closed,
        "owner_representatives_remaining": 10368 - representatives_closed,
    }


def main():
    result = verify()
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS1_2_EXCLUSION_PASS "
          f"charts={result['charts']} "
          f"closed={result['raw_closed']}/{result['representatives_closed']} "
          f"owner={result['owner_raw_remaining']}/"
          f"{result['owner_representatives_remaining']}")


if __name__ == "__main__":
    main()

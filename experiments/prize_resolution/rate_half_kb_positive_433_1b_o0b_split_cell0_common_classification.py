#!/usr/bin/env python3
"""Import and recount the exact O0b split cell-0 common classification."""

from collections import Counter
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CHARTS = HERE / "rate_half_kb_positive_433_1b_principal_common_charts_result.json"
COMPONENTS = (
    HERE / "rate_half_kb_positive_433_1b_cell0_principal_component_compiler_result.json"
)
S0_PATH = HERE / "rate_half_kb_positive_433_1b_o0b_s0_v4_label_quotient.py"
REPEATED_PATH = (
    HERE / "rate_half_kb_positive_433_1b_o0b_repeated_outside_v4_quotient.py"
)

CHARTS_SHA256 = "c4bbba007d2d4b7a5cd40fd1afb299c5233eaf878b2fc5bee71b3b6e254bd9f5"
COMPONENTS_SHA256 = "2fd2d65ebd033d8cd784f428d31d9b49eb66c4b6a059326ed7efcd60d53ed100"
MIXED_SIGNS = ((-1, 1), (1, -1))


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


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_common_payload(charts, components):
    require(charts["schema"] ==
            "rate-half-kb-positive-433-1b-principal-common-charts-v1",
            "chart schema")
    require(charts["case_count"] == 24 and len(charts["rows"]) == 24,
            "chart completeness")
    require(charts["status_counts"] == {"COMPLETE": 24}, "chart status")
    require(charts["unit_count"] == 12 and charts["nonunit_count"] == 12,
            "chart unit split")

    keys = Counter()
    mixed = []
    equal = []
    for row in charts["rows"]:
        require(row["cell"] == 0 and row["singleton"] == "LA",
                "cell-0 scope")
        require(row["matching"] == [["AB", "AC"], ["BC+", "BC-"]],
                "cell-0 role placement")
        require(row["status"] == "COMPLETE", "complete chart row")
        key = (tuple(row["epsilon"]), row["chart"])
        keys[key] += 1
        if row["epsilon"][0] != row["epsilon"][1]:
            require(row["unit"] is True and row["dimension"] == -1 and
                    row["basis_size"] == 1, "mixed-sign unit chart")
            mixed.append(row)
        else:
            require(row["unit"] is False and row["dimension"] == 1 and
                    row["basis_size"] == 14, "equal-sign curve chart")
            equal.append(row)
    require(keys == Counter({(signs, chart): 1
                             for signs in itertools.product((-1, 1), repeat=2)
                             for chart in range(6)}), "chart Cartesian product")
    require(len(mixed) == 12 and len(equal) == 12, "chart sign partition")

    require(components["schema"] ==
            "rate-half-kb-positive-433-1b-cell0-principal-components-v2",
            "component schema")
    rows = components["rows"]
    require(len(rows) == 4, "component row count")
    require({(row["component"], row["source_sign"]) for row in rows} ==
            {(component, sign) for component in ("A", "B") for sign in (-1, 1)},
            "component/sign cover")
    for row in rows:
        require(row["field"] == 2130706433 and row["all_rows_zero"] is True,
                "component exactness")
        require(len(row["row_checks"]) == 10 and
                all(check["zero"] is True for check in row["row_checks"]),
                "component common-row checks")
    return len(mixed), len(equal), len(rows)


def verify_common_certificates(charts_path=CHARTS, components_path=COMPONENTS):
    require(digest(charts_path) == CHARTS_SHA256, "chart certificate custody")
    require(digest(components_path) == COMPONENTS_SHA256,
            "component certificate custody")
    charts = json.loads(charts_path.read_text())
    components = json.loads(components_path.read_text())
    return validate_common_payload(charts, components)


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
            seed,
            first_action(seed),
            second_action(seed),
            first_action(second_action(seed)),
        }
        require(orbit <= rows, "orbit closure")
        unseen -= orbit
        profile[len(orbit)] += 1
    return dict(sorted(profile.items()))


def verify_mixed_quotient(s0_d_permutation=S0.D_PERMUTATION,
                          duplicate_permutations=REPEATED.DUPLICATE_PERMUTATIONS):
    matching_rows = tuple(S0.BC.pairings(range(6)))
    labels = tuple(itertools.product(range(7), range(15)))

    s0_rows = {
        ("S0", sigma_o, 0, epsilon_1, epsilon_2, xi, matching)
        for sigma_o, (epsilon_1, epsilon_2), (xi, matching) in itertools.product(
            (-1, 1), MIXED_SIGNS, labels
        )
    }
    s0_profile = orbit_profile(
        s0_rows,
        lambda row: S0.bc_action(row, matching_rows),
        lambda row: S0.d_action(row, s0_d_permutation),
    )
    require(len(s0_rows) == 420 and s0_profile == {2: 18, 4: 96},
            "mixed S0 quotient")

    repeated_rows = {
        (lane, sigma_o, 0, epsilon_1, epsilon_2, xi, matching)
        for lane, sigma_o, (epsilon_1, epsilon_2), (xi, matching) in
        itertools.product(("SDE", "SDF"), (-1, 1), MIXED_SIGNS, labels)
    }
    repeated_profile = orbit_profile(
        repeated_rows,
        lambda row: REPEATED.bc_action(row, matching_rows),
        lambda row: REPEATED.duplicate_action(row, duplicate_permutations),
    )
    require(len(repeated_rows) == 840 and
            repeated_profile == {2: 60, 4: 180},
            "mixed repeated-lane quotient")
    return s0_profile, repeated_profile


def verify(charts_path=CHARTS, components_path=COMPONENTS,
           s0_d_permutation=S0.D_PERMUTATION,
           duplicate_permutations=REPEATED.DUPLICATE_PERMUTATIONS):
    mixed_charts, equal_charts, component_rows = verify_common_certificates(
        charts_path, components_path
    )
    s0_profile, repeated_profile = verify_mixed_quotient(
        s0_d_permutation, duplicate_permutations
    )
    mixed_raw = 2 * 6 * 105
    mixed_orbits = sum(s0_profile.values()) + sum(repeated_profile.values())
    require(mixed_raw == 1260 and mixed_orbits == 354, "mixed closure census")
    return {
        "mixed_charts": mixed_charts,
        "equal_charts": equal_charts,
        "component_rows": component_rows,
        "mixed_raw_closed": mixed_raw,
        "mixed_orbits_closed": mixed_orbits,
        "s0_profile": s0_profile,
        "repeated_profile": repeated_profile,
        "owner_raw_remaining": 39480 - mixed_raw,
        "owner_orbits_remaining": 11076 - mixed_orbits,
        "equal_raw_remaining": 1260,
        "equal_component_orbits": 2 * mixed_orbits,
    }


def main():
    result = verify()
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELL0_COMMON_CLASSIFICATION_PASS "
        f"closed={result['mixed_raw_closed']}/{result['mixed_orbits_closed']} "
        f"owner={result['owner_raw_remaining']}/{result['owner_orbits_remaining']} "
        f"equal_raw={result['equal_raw_remaining']} "
        f"component_orbits={result['equal_component_orbits']}"
    )


if __name__ == "__main__":
    main()

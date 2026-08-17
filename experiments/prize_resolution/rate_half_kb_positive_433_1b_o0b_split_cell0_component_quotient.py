#!/usr/bin/env python3
"""Exact Klein-four quotient of the O0b split cell-0 component ledger."""

from collections import Counter
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
BC_PATH = HERE / "rate_half_kb_positive_433_1b_o0b_split_bc_ef_involution.py"
S0_PATH = HERE / "rate_half_kb_positive_433_1b_o0b_s0_v4_label_quotient.py"
REPEATED_PATH = HERE / "rate_half_kb_positive_433_1b_o0b_repeated_outside_v4_quotient.py"
COMPONENTS_PATH = (
    HERE / "rate_half_kb_positive_433_1b_cell0_principal_component_compiler_result.json"
)
PRIME = 2130706433
INV2 = pow(2, -1, PRIME)
LANES = tuple(itertools.product(("S0", "SDE", "SDF"), (-1, 1)))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BC = load("o0b_bc_ef", BC_PATH)
S0 = load("o0b_s0_v4", S0_PATH)
REPEATED = load("o0b_repeated_v4", REPEATED_PATH)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


# Gaussian coefficients a+b*i modulo PRIME, with i^2=-1.
def gadd(left, right):
    return ((left[0] + right[0]) % PRIME, (left[1] + right[1]) % PRIME)


def gmul(left, right):
    return ((left[0]*right[0] - left[1]*right[1]) % PRIME,
            (left[0]*right[1] + left[1]*right[0]) % PRIME)


def gpow(value, exponent):
    if exponent < 0:
        norm = (value[0]*value[0] + value[1]*value[1]) % PRIME
        value = (value[0]*pow(norm, -1, PRIME) % PRIME,
                 -value[1]*pow(norm, -1, PRIME) % PRIME)
        exponent = -exponent
    output = (1, 0)
    for _ in range(exponent):
        output = gmul(output, value)
    return output


def padd(left, right):
    output = dict(left)
    for monomial, coefficient in right.items():
        output[monomial] = gadd(output.get(monomial, (0, 0)), coefficient)
        if output[monomial] == (0, 0):
            del output[monomial]
    return output


def pscale(value, scalar):
    return {monomial: gmul(coefficient, scalar)
            for monomial, coefficient in value.items()
            if gmul(coefficient, scalar) != (0, 0)}


def relation(component, source_sign):
    alpha = (INV2, source_sign*INV2 % PRIME)
    unit_i = (0, source_sign % PRIME)
    if component == "A":
        terms = (
            ((1, 1), (1, 0)),
            ((2, 1), alpha),
            ((0, 0), alpha),
            ((1, 0), unit_i),
        )
    elif component == "B":
        terms = (
            ((1, 1), (1, 0)),
            ((0, 1), alpha),
            ((2, 0), alpha),
            ((1, 0), unit_i),
        )
    else:
        raise RuntimeError("unknown component")
    output = {}
    for monomial, coefficient in terms:
        output = padd(output, {monomial: coefficient})
    return output


def substitute_b_x(value, b_scale, x_scale=(-1, 0)):
    output = {}
    for (b_power, x_power), coefficient in value.items():
        factor = gmul(gpow(b_scale, b_power), gpow(x_scale, x_power))
        output = padd(output, {(b_power, x_power): gmul(coefficient, factor)})
    return output


def verify_component_action(destination=None):
    payload = json.loads(COMPONENTS_PATH.read_text())
    require({(row["component"], row["source_sign"]) for row in payload["rows"]} ==
            {(component, sign) for component in ("A", "B") for sign in (-1, 1)},
            "component source cover")
    destination = destination or {"A": "A", "B": "B"}
    rows = 0
    for component, source_sign in itertools.product(("A", "B"), (-1, 1)):
        unit_i = (0, source_sign % PRIME)
        minus_unit_i = (0, -source_sign % PRIME)
        b_scale = unit_i if component == "A" else minus_unit_i
        expected_scale = minus_unit_i if component == "A" else unit_i
        image = substitute_b_x(
            relation(destination[component], -source_sign), b_scale
        )
        require(image == pscale(relation(component, source_sign), expected_scale),
                "component relation covariance")

        # B/C exchange gives b'=c. Cell-0 source normalization has
        # r'=(-s*i)r and x'=-x; these preserve component type and flip s.
        if component == "A":
            require(gpow(b_scale, -1) == minus_unit_i,
                    "A inverse-coordinate transport")
        else:
            require(b_scale == minus_unit_i, "B diagonal-coordinate transport")
        rows += 1
    return rows


def bc_action(row, matching_rows, destination=None):
    component, lane, sigma_o, source_sign, xi, matching = row
    destination = destination or {"A": "A", "B": "B"}
    state = BC.state_action((lane, sigma_o, 0, source_sign, source_sign))
    require(state[2] == 0 and state[3] == state[4] == -source_sign,
            "equal-sign cell-0 state action")
    new_xi, new_matching = BC.case_transport(
        xi, matching, matching_rows, BC.OUTSIDE_PERMUTATION
    )
    return (destination[component], state[0], state[1], state[3],
            new_xi, new_matching)


def secondary_action(row, s0_d_permutation=S0.D_PERMUTATION,
                     duplicate_permutations=REPEATED.DUPLICATE_PERMUTATIONS):
    component, lane, sigma_o, source_sign, xi, matching = row
    if lane == "S0":
        new_xi, new_matching = S0.D_SIGN.act(
            (xi, matching), s0_d_permutation
        )
    else:
        new_xi, new_matching = REPEATED.ROUTER.act(
            (xi, matching), duplicate_permutations[lane]
        )
    return component, lane, sigma_o, source_sign, new_xi, new_matching


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
    orbits = []
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
        orbits.append(tuple(sorted(orbit)))
    return dict(sorted(Counter(map(len, orbits)).items())), tuple(
        orbit[0] for orbit in sorted(orbits)
    )


def representative_manifest(destination=None,
                            s0_d_permutation=S0.D_PERMUTATION,
                            duplicate_permutations=REPEATED.DUPLICATE_PERMUTATIONS):
    matching_rows = tuple(BC.pairings(range(6)))
    rows = {
        (component, lane, sigma_o, source_sign, xi, matching)
        for component, (lane, sigma_o), source_sign, xi, matching in itertools.product(
            ("A", "B"), LANES, (-1, 1), range(7), range(15)
        )
    }
    require(len(rows) == 2520, "component raw-case census")
    first = lambda row: bc_action(row, matching_rows, destination)
    second = lambda row: secondary_action(
        row, s0_d_permutation, duplicate_permutations
    )
    s0_rows = {row for row in rows if row[1] == "S0"}
    repeated_rows = rows - s0_rows
    s0_profile, s0_representatives = orbit_profile(s0_rows, first, second)
    repeated_profile, repeated_representatives = orbit_profile(
        repeated_rows, first, second
    )
    require(s0_profile == {2: 36, 4: 192}, "S0 component quotient")
    require(repeated_profile == {2: 120, 4: 360},
            "repeated-lane component quotient")
    representatives = tuple(sorted(s0_representatives + repeated_representatives))
    require(len(representatives) == 708, "component representative census")
    encoded = json.dumps(representatives, separators=(",", ":"))
    return {
        "raw_cases": len(rows),
        "s0_profile": s0_profile,
        "repeated_profile": repeated_profile,
        "representative_count": len(representatives),
        "representatives_sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "representatives": representatives,
    }


def verify(destination=None, s0_d_permutation=S0.D_PERMUTATION,
           duplicate_permutations=REPEATED.DUPLICATE_PERMUTATIONS):
    component_rows = verify_component_action(destination)
    result = representative_manifest(
        destination, s0_d_permutation, duplicate_permutations
    )
    result = dict(result)
    result.pop("representatives")
    result["component_rows"] = component_rows
    return result


def main():
    result = verify()
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELL0_COMPONENT_QUOTIENT_PASS "
        f"raw={result['raw_cases']} reps={result['representative_count']} "
        f"sha256={result['representatives_sha256']}"
    )


if __name__ == "__main__":
    main()

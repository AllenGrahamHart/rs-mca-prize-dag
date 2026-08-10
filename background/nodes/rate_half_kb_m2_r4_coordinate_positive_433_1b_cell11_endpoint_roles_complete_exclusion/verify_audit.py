#!/usr/bin/env python3
"""Independent lift replay and hostile audit for cell-11 endpoints."""

import copy
import importlib.util
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
VERIFY = NODE / "verify.py"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell11_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
PRIME = 2130706433
t, r, c, b = sp.symbols("t r c b")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_verifier():
    spec = importlib.util.spec_from_file_location("cell11_endpoint_verify", VERIFY)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def square_root(value):
    value %= PRIME
    if value == 0:
        return 0
    require(pow(value, (PRIME - 1) // 2, PRIME) == 1, "nonsquare")
    q = PRIME - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(value, (PRIME + 1) // 4, PRIME)
    z = 2
    while pow(z, (PRIME - 1) // 2, PRIME) != PRIME - 1:
        z += 1
    m = s
    x = pow(value, (q + 1) // 2, PRIME)
    residue = pow(value, q, PRIME)
    factor = pow(z, q, PRIME)
    while residue != 1:
        i = 1
        probe = residue * residue % PRIME
        while probe != 1:
            probe = probe * probe % PRIME
            i += 1
        update = pow(factor, 1 << (m - i - 1), PRIME)
        x = x * update % PRIME
        residue = residue * update * update % PRIME
        factor = update * update % PRIME
        m = i
    return x


def roots(expression, variable):
    polynomial = sp.Poly(expression, variable, modulus=PRIME)
    coefficients = [int(value) % PRIME for value in polynomial.all_coeffs()]
    while coefficients and coefficients[0] == 0:
        coefficients.pop(0)
    if len(coefficients) == 2:
        return [(-coefficients[1] * pow(coefficients[0], -1, PRIME)) % PRIME]
    require(len(coefficients) == 3, "nonquadratic tower relation")
    a_value, linear, constant = coefficients
    discriminant = (linear * linear - 4 * a_value * constant) % PRIME
    symbol = pow(discriminant, (PRIME - 1) // 2, PRIME)
    if symbol == PRIME - 1:
        return []
    root = square_root(discriminant)
    inverse = pow(2 * a_value, -1, PRIME)
    return sorted({
        (-linear + root) * inverse % PRIME,
        (-linear - root) * inverse % PRIME,
    })


def rejected(verifier, pilot, replay, root, kernel):
    try:
        verifier.validate(pilot, replay, root, kernel)
    except RuntimeError:
        return True
    return False


def main():
    verifier = load_verifier()
    pilot = verifier.load("pilot")
    replay = verifier.load("replay")
    frobenius = verifier.load("root")
    kernel_payload = json.loads(KERNEL.read_text())
    verifier.validate(pilot, replay, frobenius, kernel_payload)

    tower = json.loads(TOWER.read_text())
    kernel = [
        sp.sympify(item["expression"])
        for item in kernel_payload["rows"][0]["kernel"]
    ]
    replay_rows = {
        (tuple(row["epsilon"]), row["endpoint"]): row
        for row in replay["rows"]
    }
    no_b = 0
    lifts = 0
    incompatible = 0
    for root_row in frobenius["rows"]:
        signs = tuple(root_row["epsilon"])
        endpoint = root_row["endpoint"]
        tower_row = next(
            row for row in tower["rows"]
            if tuple(row["epsilon"]) == signs and row["c_row_index"] == 5
        )
        base = sp.sympify(tower_row["base"]["expression"])
        b_relation = sp.sympify(tower_row["b_relation"]["expression"])
        c_relation = sp.sympify(tower_row["c_relation"]["expression"])
        b_leading = sp.sympify(tower_row["b_leading"]["expression"])
        c_leading = sp.sympify(tower_row["c_leading"]["expression"])
        row_lifts = 0
        row_no_b = 0
        r_value = root_row["roots"][0]
        for t_value in roots(base.subs(r, r_value), t):
            b_roots = roots(
                b_relation.subs({r: r_value, t: t_value}), b
            )
            if not b_roots:
                row_no_b += 1
                continue
            for b_value in b_roots:
                substitutions = {r: r_value, t: t_value, b: b_value}
                require(int(b_leading.subs(substitutions)) % PRIME,
                        "b-leading boundary")
                c_polynomial = sp.Poly(
                    c_relation.subs(substitutions), c, modulus=PRIME
                )
                coefficient = int(c_polynomial.coeff_monomial(c)) % PRIME
                constant = int(c_polynomial.coeff_monomial(1)) % PRIME
                require(coefficient, "c recovery boundary")
                c_value = -constant * pow(coefficient, -1, PRIME) % PRIME
                substitutions[c] = c_value
                require(int(c_leading.subs(substitutions)) % PRIME,
                        "c-leading boundary")
                guards = (
                    r_value, t_value, b_value, c_value,
                    b_value - 1, b_value + 1, c_value - 1, c_value + 1,
                    b_value - c_value, b_value + c_value,
                    r_value*r_value - 1, r_value*r_value + 1,
                    t_value*t_value - 1, t_value*t_value + 1,
                    t_value*t_value - r_value*r_value,
                    t_value*t_value + r_value*r_value,
                )
                require(all(value % PRIME for value in guards),
                        "route guard")
                values = [
                    int(expression.subs(substitutions)) % PRIME
                    for expression in kernel
                ]
                label = -t_value * t_value % PRIME
                a_value = sum(
                    values[index] * pow(label, index, PRIME)
                    for index in range(3)
                ) % PRIME
                b_value_at_label = sum(
                    values[index + 3] * pow(label, index, PRIME)
                    for index in range(3)
                ) % PRIME
                require(a_value, "missing-record denominator")
                missing = b_value_at_label * pow(a_value, -1, PRIME) % PRIME
                beta = (values[6] + values[7] * label) % PRIME
                source_sum = (
                    label * beta * beta * pow(a_value, -2, PRIME)
                ) % PRIME
                endpoint_value = (
                    substitutions[b] if endpoint == "b" else substitutions[c]
                )
                compatibility = (
                    pow((endpoint_value*endpoint_value + missing) % PRIME,
                        2, PRIME)
                    - source_sum * endpoint_value * endpoint_value
                ) % PRIME
                require(compatibility, "compatible endpoint lift")
                row_lifts += 1
                incompatible += 1
        replay_row = replay_rows[(signs, endpoint)]
        require(row_no_b == 1 and row_lifts == 2 and
                replay_row["lifted_point_count"] == row_lifts,
                "independent lift ledger")
        no_b += row_no_b
        lifts += row_lifts

    require(no_b == 8 and lifts == incompatible == 16,
            "independent global totals")

    dropped = copy.deepcopy(frobenius)
    dropped["rows"].pop()
    require(rejected(verifier, pilot, replay, dropped, kernel_payload),
            "dropped root row accepted")
    changed = copy.deepcopy(frobenius)
    changed["rows"][0]["roots"][0] += 1
    require(rejected(verifier, pilot, replay, changed, kernel_payload),
            "changed root accepted")
    invented = copy.deepcopy(replay)
    invented["rows"][0]["generic_point_count"] = 1
    require(rejected(verifier, pilot, invented, frobenius, kernel_payload),
            "invented compatible point accepted")
    divergent = copy.deepcopy(kernel_payload)
    divergent["rows"][0]["kernel"][0]["sha256"] = "0" * 64
    require(rejected(verifier, pilot, replay, frobenius, divergent),
            "sign-dependent kernel accepted")
    print(
        "PASS cell-11 endpoint audit: lifts=16 incompatible=16 "
        "hostile_mutations=4/4"
    )


if __name__ == "__main__":
    main()

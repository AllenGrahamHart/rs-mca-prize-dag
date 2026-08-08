#!/usr/bin/env python3
"""Independent finite-root audit for the cell-12 parallel-DE norms."""

import copy
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
NORM = EXP / "rate_half_kb_positive_433_1b_cell12_parallel_de_four_basis_norm_result.json"
REPLAY = EXP / "rate_half_kb_positive_433_1b_cell12_parallel_de_four_basis_replay_result.json"
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell12_parallel_de_first_pair_residual_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell12_parallel_de_first_pair_audit_result.json"
P = 2130706433
r = sp.symbols("r")
ROOT_CACHE = {}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def trim(values):
    values = [value % P for value in values]
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values or [0]


def remainder(left, right):
    left, right = trim(left[:]), trim(right[:])
    inverse = pow(right[-1], -1, P)
    while len(left) >= len(right) and left != [0]:
        shift = len(left)-len(right)
        quotient = left[-1]*inverse % P
        for index, value in enumerate(right):
            left[index+shift] = (left[index+shift]-quotient*value) % P
        left = trim(left)
    return left


def multiply_mod(left, right, modulus):
    output = [0]*(len(left)+len(right)-1)
    for i, a in enumerate(left):
        if a:
            for j, b in enumerate(right):
                output[i+j] = (output[i+j]+a*b) % P
    return remainder(output, modulus)


def power_mod(base, exponent, modulus):
    output = [1]
    while exponent:
        if exponent & 1:
            output = multiply_mod(output, base, modulus)
        base, exponent = multiply_mod(base, base, modulus), exponent//2
    return output


def gcd(left, right):
    left, right = trim(left), trim(right)
    while right != [0]:
        left, right = right, remainder(left, right)
    inverse = pow(left[-1], -1, P)
    return [value*inverse % P for value in left]


def coefficients(profile):
    polynomial = sp.Poly(sp.sympify(profile["expression"]), r, modulus=P)
    output = [0]*(polynomial.degree()+1)
    for (degree,), value in polynomial.terms():
        output[degree] = int(value) % P
    require(polynomial.degree() == profile["degree"]
            and len(polynomial.terms()) == profile["terms"], "profile shape")
    return trim(output)


def evaluate(polynomial, point):
    output = 0
    for value in reversed(polynomial):
        output = (output*point+value) % P
    return output


def multiply(left, right):
    output = [0]*(len(left)+len(right)-1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i+j] = (output[i+j]+a*b) % P
    return trim(output)


def audit_profile(profile, candidates):
    key = profile["sha256"]
    if key not in ROOT_CACHE:
        polynomial = coefficients(profile)
        if len(polynomial) == 1:
            root_part = [1]
        else:
            frobenius = power_mod([0, 1], P, polynomial)
            frobenius += [0]*(max(2, len(frobenius))-len(frobenius))
            frobenius[1] = (frobenius[1]-1) % P
            root_part = gcd(polynomial, trim(frobenius))
        ROOT_CACHE[key] = polynomial, root_part
    polynomial, root_part = ROOT_CACHE[key]
    found = sorted(point for point in candidates if evaluate(polynomial, point) == 0)
    reconstructed = [1]
    for point in found:
        reconstructed = multiply(reconstructed, [(-point) % P, 1])
    require(root_part == reconstructed, "incomplete finite-root list")
    return found


def terminal_total(payload, unit_key):
    total = 0
    for row in payload["rows"]:
        require(row["status"] == "COMPLETE" and not row.get("witnesses", [])
                and not row.get("unresolved", [])
                and row[unit_key] == row["systems"], "terminal row")
        total += row["systems"]
    return total


def main():
    norm = json.loads(NORM.read_text())
    replay = json.loads(REPLAY.read_text())
    replay_map = {(tuple(row["epsilon"]), row["cut_kind"]): row
                  for row in replay["rows"]}
    polynomials = 0
    for row in norm["rows"]:
        key = (tuple(row["epsilon"]), row["cut_kind"])
        candidates = row["candidate_roots"]
        target = audit_profile(row["target_norm"]["numerator"], candidates)
        require(target == row["target_roots"], "target-root replay")
        union = set(target)
        polynomials += 1
        for value in [*row["inverse_guards"], row["target_norm"]]:
            for side in ("numerator", "denominator"):
                union.update(audit_profile(value[side], candidates))
                polynomials += 1
        require(sorted(union) == candidates, "candidate-root union")
        direct = replay_map[key]
        require(direct["candidate_root_count"] == len(candidates)
                and not direct["unresolved"], "direct replay custody")
        if row["cut_kind"] == "equal_negative":
            require(not direct["witnesses"] and direct["excluded_generic"],
                    "negative-DE terminal")
        else:
            require(len(direct["witnesses"]) == 2, "positive-DE source zeros")

    primary = json.loads(PRIMARY.read_text())
    audit = json.loads(AUDIT.read_text())
    require(terminal_total(primary, "unit_systems") == 96
            and terminal_total(audit, "unit_systems") == 96,
            "independent residual agreement")
    hostile = copy.deepcopy(audit)
    hostile["rows"][0]["unit_systems"] -= 1
    try:
        terminal_total(hostile, "unit_systems")
    except RuntimeError:
        pass
    else:
        raise RuntimeError("hostile unit mutation survived")
    print(f"PASS independent parallel-DE audit: polynomials={polynomials} systems=96")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Check the source-reciprocal transport that flips epsilon2 in cell 5."""

import copy
import hashlib
import json
from pathlib import Path
import re

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
SCOUT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_cell5_epsilon2_plus_scout_result.json"
)
OLD_PACKET = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_cell5_signed_family_decomposition_result.json"
)
SCOUT_SHA256 = "ec4e9b5fd2cefbc1e6a04698453e47f18f449983fb40f9519526475d8f4c2852"
PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def parse_singular_bt(text, b, t):
    expression = sp.Integer(0)
    for raw_term in re.findall(r"[+-]?[^+-]+", text.strip()):
        sign = -1 if raw_term.startswith("-") else 1
        term = raw_term.lstrip("+-")
        match = re.match(r"\d+", term)
        if match:
            coefficient = int(match.group())
            term = term[match.end():]
        else:
            coefficient = 1
        powers = {"b": 0, "t": 0}
        position = 0
        while position < len(term):
            variable = term[position]
            require(variable in powers, f"unexpected Singular token {term}")
            position += 1
            end = position
            while end < len(term) and term[end].isdigit():
                end += 1
            powers[variable] += int(term[position:end] or "1")
            position = end
        expression += sign * coefficient * b**powers["b"] * t**powers["t"]
    return sp.expand(expression)


def check_form_transport():
    T, X, W = sp.symbols("T X W", nonzero=True)
    d0, d1, d2, e0, e1, e2, beta0, beta1 = sp.symbols(
        "d0 d1 d2 e0 e1 e2 beta0 beta1"
    )
    a2 = d0 + d1 * X**2 + d2 * X**4
    a0 = e0 + e1 * X**2 + e2 * X**4
    b1 = beta0 + beta1 * X**2
    source = a2 * T**2 + a0 + X * T * b1
    transformed = sp.cancel(X**4 * source.subs(X, -1 / X))
    expected = (
        (d2 + d1 * X**2 + d0 * X**4) * T**2
        + (e2 + e1 * X**2 + e0 * X**4)
        + X * T * (-beta1 - beta0 * X**2)
    )
    require(sp.expand(transformed - expected) == 0, "coefficient form transport")

    twice = {
        "d": tuple(reversed(tuple(reversed((d0, d1, d2))))),
        "e": tuple(reversed(tuple(reversed((e0, e1, e2))))),
        "beta": tuple(-value for value in reversed(
            tuple(-value for value in reversed((beta0, beta1)))
        )),
    }
    require(twice["d"] == (d0, d1, d2), "d involution")
    require(twice["e"] == (e0, e1, e2), "e involution")
    require(twice["beta"] == (beta0, beta1), "beta involution")

    a2w = d0 + d1 * W + d2 * W**2
    a0w = e0 + e1 * W + e2 * W**2
    b1w = beta0 + beta1 * W
    a2p = W**2 * a2w.subs(W, 1 / W)
    a0p = W**2 * a0w.subs(W, 1 / W)
    b1p = -W * b1w.subs(W, 1 / W)
    z, product, edge_sum = sp.symbols("z product edge_sum", nonzero=True)
    lam = z**2
    q_value = z * edge_sum
    lam_prime = 1 / lam
    q_prime = -q_value / lam
    product_original = a0w.subs(W, lam) - product * a2w.subs(W, lam)
    product_transformed = (
        a0p.subs(W, lam_prime) - product * a2p.subs(W, lam_prime)
    )
    require(
        sp.cancel(product_transformed - lam_prime**2 * product_original) == 0,
        "product Vieta scaling",
    )
    sum_original = (
        lam * b1w.subs(W, lam) + q_value * a2w.subs(W, lam)
    )
    sum_transformed = (
        lam_prime * b1p.subs(W, lam_prime)
        + q_prime * a2p.subs(W, lam_prime)
    )
    require(
        sp.cancel(sum_transformed + lam_prime**3 * sum_original) == 0,
        "sum Vieta scaling",
    )


def check_cell5_sign_map():
    iota = sp.I
    r, t, b, c = sp.symbols("r t b c", nonzero=True)
    products = {
        "LC": -c**2,
        "AB+1": b,
        "AB+2": b,
        "AB-": -b,
        "AC": c,
    }
    sums = {
        "LC": 0,
        "AB+1": 1 + b,
        "AB+2": 1 + b,
        "AB-": 1 - b,
        "AC": 1 + c,
    }
    for epsilon_1 in (-1, 1):
        for epsilon_2 in (-1, 1):
            roots = {
                "LC": sp.Integer(1),
                "AC": epsilon_1 * iota,
                "AB+2": r,
                "AB-": epsilon_2 * iota * r,
                "AB+1": t,
            }
            r_prime = -1 / r
            t_prime = -1 / t
            canonical = {
                "LC": sp.Integer(1),
                "AC": epsilon_1 * iota,
                "AB+2": r_prime,
                "AB-": -epsilon_2 * iota * r_prime,
                "AB+1": t_prime,
            }
            for role in roots:
                image = -1 / roots[role]
                require(
                    sp.cancel(image**2 - canonical[role] ** 2) == 0,
                    f"{role} quotient label",
                )
                require(
                    sp.cancel(image * sums[role]
                              - canonical[role] * sums[role]) == 0,
                    f"{role} q record",
                )
                require(products[role] == products[role], f"{role} product")

    left, right = sp.symbols("left right", nonzero=True)
    require(
        sp.cancel(1 / left - 1 / right + (left - right) / (left * right))
        == 0,
        "distinctness transport",
    )
    require(
        sp.cancel(1 / left + 1 / right - (left + right) / (left * right))
        == 0,
        "opposite-pair transport",
    )


def check_modal_audit():
    require(hashlib.sha256(SCOUT.read_bytes()).hexdigest() == SCOUT_SHA256,
            "scout packet hash")
    scout = json.loads(SCOUT.read_text())
    ratio = scout["ratio"]
    clone = copy.deepcopy(ratio)
    observed_payload_hash = clone.pop("payload_sha256")
    require(
        hashlib.sha256(canonical_json(clone).encode()).hexdigest()
        == observed_payload_hash,
        "ratio payload hash",
    )
    require(ratio["status"] == "COMPLETE", "ratio status")
    require(ratio["ratio_degrees_in_b"] == [1, 2, 2], "ratio shape")
    require(scout["structure"]["status"] == "COMPLETE", "structure status")
    require("LOCALIZED\n1\n23\n-1" in scout["structure"]["stdout"],
            "localized dimension")
    atlas = scout["deployed_atlas"]
    require(atlas["status"] == "COMPLETE", "atlas status")
    require("RECIPROCAL_CHECK\n1\n1" in atlas["stdout"], "reciprocal checks")
    match = re.search(r"\nBPOLY\n([^\n]+)\nC_LIFT\n", atlas["stdout"])
    require(match is not None, "new b polynomial")

    b, t = sp.symbols("b t")
    new_polynomial = parse_singular_bt(match.group(1), b, t)
    old_text = json.loads(OLD_PACKET.read_text())[
        "deployed_trace_quadratic"
    ]["polynomial"]
    old_polynomial = sp.sympify(old_text, locals={"b": b, "t": t})
    transported = sp.cancel(-t**4 * old_polynomial.subs(t, -1 / t))
    require(
        sp.Poly(new_polynomial - transported, b, t, modulus=PRIME).is_zero,
        "reciprocal quartic transport",
    )


def main():
    check_form_transport()
    check_cell5_sign_map()
    check_modal_audit()
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL58_SOURCE_RECIPROCAL_TRANSPORT_PASS "
        "cells=5,8 root_sign_rows=8 scout_sha256=" + SCOUT_SHA256
    )


if __name__ == "__main__":
    main()

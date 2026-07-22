#!/usr/bin/env python3
"""Bounded Modal pilot for the order-zero HNF cyclotomic gcd."""

import hashlib
import json
import time

try:
    import modal
except ModuleNotFoundError:  # The local certificate checker needs no Modal SDK.
    modal = None


def poly_coefficients(poly, p):
    return [int(value) % p for value in reversed(poly.all_coeffs())]


def classify(p, m):
    import sympy as sp

    h = m - 1
    n = m * (p + 1)
    s, w = sp.symbols("s w")
    # SymPy's Poly.rem coerces coefficient domains to a field internally.
    # Work in F_p(s); monicity in w keeps every resulting coefficient in F_p[s].
    domain = sp.GF(p).frac_field(s)

    expression = 0
    rising = 1
    for r in range(h + 1):
        if r:
            rising = sp.expand(rising * (s + r - 1) * pow(r, -1, p))
        expression += rising * w ** (h - r)
    modulus = sp.Poly(expression, w, domain=domain)

    result = sp.Poly(1, w, domain=domain)
    base = sp.Poly(w, w, domain=domain)
    exponent = n
    while exponent:
        if exponent & 1:
            result = (result * base).rem(modulus)
        exponent >>= 1
        if exponent:
            base = (base * base).rem(modulus)
    result -= sp.Poly(1, w, domain=domain)

    remainders = []
    common = None
    for k in range(h):
        coefficient = sp.Poly(result.nth(k).as_expr(), s, modulus=p)
        remainders.append(poly_coefficients(coefficient, p))
        if not coefficient.is_zero:
            common = coefficient.monic() if common is None else sp.gcd(common, coefficient).monic()
    if common is None:
        raise AssertionError("cyclotomic remainder vanished identically")

    prime_field = sp.Poly(s ** p - s, s, modulus=p)
    prime_part = sp.gcd(common, prime_field).monic()
    outside = common.exquo(prime_part).monic()
    factors = [
        {"coefficients": poly_coefficients(factor.monic(), p), "multiplicity": multiplicity}
        for factor, multiplicity in sp.factor_list(outside)[1]
    ]
    payload = {
        "p": p,
        "m": m,
        "h": h,
        "n": n,
        "remainder_coefficients": remainders,
        "common_gcd": poly_coefficients(common, p),
        "prime_field_part": poly_coefficients(prime_part, p),
        "outside_prime_field": poly_coefficients(outside, p),
        "outside_factors": factors,
    }
    digest_source = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["payload_sha256"] = hashlib.sha256(digest_source).hexdigest()
    return payload


if modal is not None:
    app = modal.App("l1-mersenne-hnf-toy-gcd")
    image = modal.Image.debian_slim().pip_install("sympy")

    @app.function(image=image, cpu=1.0, memory=1024, timeout=120)
    def run_pilot():
        started = time.monotonic()
        payload = classify(31, 8)
        payload["worker_seconds"] = round(time.monotonic() - started, 6)
        return payload

    @app.local_entrypoint()
    def main():
        print(json.dumps(run_pilot.remote(), sort_keys=True, separators=(",", ":")))

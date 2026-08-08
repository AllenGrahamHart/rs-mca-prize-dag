#!/usr/bin/env sage
"""Exact lex and F_(p^6) sieve for the surviving M01-A-RL chart."""

load("/near_literal_assignment_transport_audit.sage")

import hashlib
import json
import sys
import time


assignment = "M01"
target_id = "A-RL"
residuals, systems = cache[assignment]
target_pair = TARGETS[target_id]

p = 2130706433
Fp = GF(p)
S = PolynomialRing(Fp, names=("b", "c", "d"), order="degrevlex")
bS, cS, dS = S.gens()
equations = []
for residual, target in zip(residuals, target_pair):
    for index in (0, 1):
        raw = K(residual[index] - residual[2] * target[index])
        equations.append(S(primitive(R(raw.numerator()))))

factors = [S(R(text)) for text in factor_set(systems[target_id], "I")]
factors.extend((bS, cS, dS, cS - dS))
current = S.ideal(equations)
started = time.monotonic()
for factor in factors:
    saturation = current.saturation(S.ideal([factor]))
    current = saturation if hasattr(saturation, "gens") else saturation[0]

primary_basis = current.groebner_basis()
compiled = {
    "schema": "kb-c2-112-near-positive-m01-a-rl-field-sieve-v1",
    "cell": "M01-A-RL",
    "equation_count": len(equations),
    "localizer_count": len(factors),
    "primary_basis_size": len(primary_basis),
    "primary_basis_sha256": hashlib.sha256(
        "\n".join(str(item) for item in primary_basis).encode()
    ).hexdigest(),
    "saturation_seconds": float(time.monotonic() - started),
    "terminal": "SATURATED",
}
print("M01_A_RL_FIELD_SIEVE_JSON " + json.dumps(
    compiled, sort_keys=True, separators=(",", ":")
))
sys.stdout.flush()

L = PolynomialRing(Fp, names=("b", "c", "d"), order="lex")
bL, cL, dL = L.gens()
lex_started = time.monotonic()
lex_basis = L.ideal([L(item) for item in primary_basis]).groebner_basis()
univariate = [
    item for item in lex_basis
    if all(index[0] == 0 and index[1] == 0 for index in item.dict())
]
if len(univariate) != 1:
    raise RuntimeError(f"expected one d-eliminant, got {len(univariate)}")
eliminant = univariate[0].univariate_polynomial()
factorization = eliminant.factor()
factor_degrees = [
    {"degree": int(factor.degree()), "multiplicity": int(multiplicity)}
    for factor, multiplicity in factorization
]
compatible_degrees = [
    row for row in factor_degrees if 6 % row["degree"] == 0
]
payload = {
    **compiled,
    "lex_seconds": float(time.monotonic() - lex_started),
    "lex_basis_size": len(lex_basis),
    "lex_basis": [str(item) for item in lex_basis],
    "lex_basis_sha256": hashlib.sha256(
        "\n".join(str(item) for item in lex_basis).encode()
    ).hexdigest(),
    "eliminant_degree": int(eliminant.degree()),
    "eliminant_terms": int(len(eliminant.dict())),
    "eliminant_sha256": hashlib.sha256(str(eliminant).encode()).hexdigest(),
    "factor_degrees": factor_degrees,
    "f_p6_compatible_degrees": compatible_degrees,
    "f_p6_empty_by_eliminant": not compatible_degrees,
    "terminal": (
        "F_P6_EMPTY_BY_ELIMINANT"
        if not compatible_degrees
        else "F_P6_COMPATIBLE_FACTOR_REMAINS"
    ),
}
print("M01_A_RL_FIELD_SIEVE_JSON " + json.dumps(
    payload, sort_keys=True, separators=(",", ":")
))
sys.stdout.flush()

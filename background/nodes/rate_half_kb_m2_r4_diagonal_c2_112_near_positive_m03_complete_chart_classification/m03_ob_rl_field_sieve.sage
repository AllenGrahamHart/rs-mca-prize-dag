#!/usr/bin/env sage
"""Exact lex and F_(p^6) sieve for the surviving M03-OB-RL chart."""

load("/near_literal_assignment_transport_audit.sage")

import hashlib
import json
import sys
import time


assignment = "M03"
target_id = "OB-RL"
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
    "schema": "kb-c2-112-near-positive-m03-ob-rl-field-sieve-v1",
    "cell": "M03-OB-RL",
    "equation_count": len(equations),
    "localizer_count": len(factors),
    "primary_basis_size": len(primary_basis),
    "primary_basis_sha256": hashlib.sha256(
        "\n".join(str(item) for item in primary_basis).encode()
    ).hexdigest(),
    "saturation_seconds": float(time.monotonic() - started),
    "terminal": "SATURATED",
}
print("M03_OB_RL_FIELD_SIEVE_JSON " + json.dumps(
    compiled, sort_keys=True, separators=(",", ":")
))
sys.stdout.flush()

L = PolynomialRing(Fp, names=("b", "c", "d"), order="lex")
lex_started = time.monotonic()
lex_basis = L.ideal([L(item) for item in primary_basis]).groebner_basis()
univariate = [
    item for item in lex_basis
    if all(index[0] == 0 and index[1] == 0 for index in item.dict())
]
if len(univariate) != 1:
    raise RuntimeError(f"expected one d-eliminant, got {len(univariate)}")
eliminant = univariate[0].univariate_polynomial()
factor_degrees = [
    {"degree": int(factor.degree()), "multiplicity": int(multiplicity)}
    for factor, multiplicity in eliminant.factor()
]
c_univariate = [
    item for item in lex_basis
    if all(index[0] == 0 and index[2] == 0 for index in item.dict())
]
if len(c_univariate) != 1:
    raise RuntimeError(f"expected one c-eliminant, got {len(c_univariate)}")
c_eliminant = c_univariate[0](L(0), L.gen(1), L(0)).univariate_polynomial()
c_factorization = c_eliminant.factor()
c_factor_degrees = [
    {"degree": int(factor.degree()), "multiplicity": int(multiplicity)}
    for factor, multiplicity in c_factorization
]
compatible_degrees = [
    row for row in c_factor_degrees if 6 % row["degree"] == 0
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
    "c_eliminant_degree": int(c_eliminant.degree()),
    "c_eliminant_terms": int(len(c_eliminant.dict())),
    "c_eliminant_sha256": hashlib.sha256(str(c_eliminant).encode()).hexdigest(),
    "c_factor_degrees": c_factor_degrees,
    "c_factors": [str(factor) for factor, multiplicity in c_factorization],
    "f_p6_compatible_degrees": compatible_degrees,
    "f_p6_empty_by_eliminant": not compatible_degrees,
    "terminal": (
        "F_P6_EMPTY_BY_ELIMINANT"
        if not compatible_degrees
        else "F_P6_COMPATIBLE_FACTOR_REMAINS"
    ),
}
print("M03_OB_RL_FIELD_SIEVE_JSON " + json.dumps(
    payload, sort_keys=True, separators=(",", ":")
))
sys.stdout.flush()

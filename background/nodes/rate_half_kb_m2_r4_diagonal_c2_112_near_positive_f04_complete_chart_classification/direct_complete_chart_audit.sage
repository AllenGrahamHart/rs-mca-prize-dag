#!/usr/bin/env sage
"""Independent one-step Rabinowitsch audit for the six F04 cells."""

load("/near_literal_assignment_transport_audit.sage")

import hashlib
import json
import os
import sys
import time


cell = os.environ["DIRECT_CELL"]
assignment, root, allocation = cell.split("-")
assert assignment == "F04"
assert root in ("A", "OB")
assert allocation in ("RX", "RL", "RM")
target_id = f"{root}-{allocation}"
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
localizer_product = S.one()
for factor in factors:
    localizer_product *= factor

compiled = {
    "schema": "kb-c2-112-near-positive-f04-complete-chart-audit-v1",
    "cell": cell,
    "equation_count": len(equations),
    "equation_tuple_sha256": hashlib.sha256(
        "\n".join(str(item) for item in equations).encode()
    ).hexdigest(),
    "localizer_count": len(factors),
    "localizer_product_degree": int(localizer_product.total_degree()),
    "localizer_product_terms": int(len(localizer_product.dict())),
    "localizer_product_sha256": hashlib.sha256(
        str(localizer_product).encode()
    ).hexdigest(),
    "terminal": "RABINOWITSCH_COMPILED",
}
print("DIRECT_COMPLETE_CHART_AUDIT_JSON " + json.dumps(
    compiled, sort_keys=True, separators=(",", ":")
))
sys.stdout.flush()

T = PolynomialRing(Fp, names=("y", "b", "c", "d"), order="degrevlex")
y = T.gen(0)
extended = [T(equation) for equation in equations]
extended.append(1 - y * T(localizer_product))
started = time.monotonic()
basis = T.ideal(extended).groebner_basis()
unit = len(basis) == 1 and basis[0] == 1
payload = {
    **compiled,
    "basis_seconds": float(time.monotonic() - started),
    "basis_size": len(basis),
    "unit_ideal": bool(unit),
    "terminal": "RABINOWITSCH_UNIT_IDEAL" if unit else "RABINOWITSCH_NONUNIT_FAILURE",
}
print("DIRECT_COMPLETE_CHART_AUDIT_JSON " + json.dumps(
    payload, sort_keys=True, separators=(",", ":")
))
sys.stdout.flush()

if not unit:
    raise RuntimeError("Rabinowitsch audit did not close the cell")

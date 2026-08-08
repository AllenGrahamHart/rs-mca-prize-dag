#!/usr/bin/env sage
"""Independent one-step Rabinowitsch audit for a direct residual cell."""

load("/near_literal_assignment_transport_audit.sage")

import os
import sys
import time


cell = os.environ["DIRECT_CELL"]
assignment, root, allocation = cell.split("-")
target_id = f"{root}-{allocation}"
residuals, systems = cache[assignment]
target_pair = TARGETS[target_id]

p = 2130706433
Fp = GF(p)
S = PolynomialRing(Fp, names=("b", "c", "d"), order="degrevlex")
equations = []
for residual, target in zip(residuals, target_pair):
    for index in (0, 1):
        raw = K(residual[index] - residual[2] * target[index])
        equations.append(S(primitive(R(raw.numerator()))))

localizers = [S(R(text)) for text in factor_set(systems[target_id], "I")]
localizer_product = S.one()
for factor in localizers:
    localizer_product *= factor

compiled = {
    "schema": "kb-c2-112-near-literal-direct-cell-rabinowitsch-audit-v1",
    "cell": cell,
    "equation_count": int(len(equations)),
    "localizer_count": int(len(localizers)),
    "localizer_product_degree": int(localizer_product.total_degree()),
    "localizer_product_terms": int(len(localizer_product.dict())),
    "terminal": "RABINOWITSCH_COMPILED",
}
print(
    "DIRECT_CELL_AUDIT_JSON "
    + json.dumps(compiled, sort_keys=True, separators=(",", ":"), default=int)
)
sys.stdout.flush()

T = PolynomialRing(Fp, names=("y", "b", "c", "d"), order="degrevlex")
y = T.gen(0)
extended_equations = [T(equation) for equation in equations]
extended_equations.append(1 - y * T(localizer_product))
started = time.monotonic()
basis = T.ideal(extended_equations).groebner_basis()
unit = len(basis) == 1 and basis[0] == 1
payload = {
    **compiled,
    "basis_seconds": float(time.monotonic() - started),
    "basis_size": int(len(basis)),
    "unit_ideal": bool(unit),
    "terminal": "RABINOWITSCH_UNIT_IDEAL" if unit else "RABINOWITSCH_NONUNIT_IDEAL",
}
print(
    "DIRECT_CELL_AUDIT_JSON "
    + json.dumps(payload, sort_keys=True, separators=(",", ":"), default=int)
)
sys.stdout.flush()

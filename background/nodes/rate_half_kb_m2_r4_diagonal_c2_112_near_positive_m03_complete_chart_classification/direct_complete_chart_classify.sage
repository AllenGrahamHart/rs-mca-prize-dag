#!/usr/bin/env sage
"""Classify one M03 residual q-slice cell on its complete affine chart."""

load("/near_literal_assignment_transport_audit.sage")

import hashlib
import json
import os
import sys
import time


cell = os.environ["DIRECT_CELL"]
assignment, root, allocation = cell.split("-")
assert assignment == "M03"
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

recorded = [S(R(text)) for text in factor_set(systems[target_id], "I")]
recorded.sort(key=lambda value: (value.total_degree(), len(value.dict()), str(value)))
localizers = [
    *[("recorded:" + str(factor), factor) for factor in recorded],
    ("chart:b", bS),
    ("chart:c", cS),
    ("chart:d", dS),
    ("chart:c-d", cS - dS),
]

payload = {
    "schema": "kb-c2-112-near-positive-m03-complete-chart-classifier-v1",
    "cell": cell,
    "equation_count": len(equations),
    "equation_tuple_sha256": hashlib.sha256(
        "\n".join(str(item) for item in equations).encode()
    ).hexdigest(),
    "recorded_localizer_count": len(recorded),
    "complete_localizer_count": len(localizers),
    "terminal": "COMPILED",
}
print("DIRECT_COMPLETE_CHART_JSON " + json.dumps(
    payload, sort_keys=True, separators=(",", ":")
))
sys.stdout.flush()

started = time.monotonic()
current = S.ideal(equations)
progress = []
for index, (name, factor) in enumerate(localizers):
    saturation = current.saturation(S.ideal([factor]))
    current = saturation if hasattr(saturation, "gens") else saturation[0]
    basis = current.groebner_basis()
    unit = len(basis) == 1 and basis[0] == 1
    progress.append({
        "index": index,
        "factor": name,
        "factor_degree": int(factor.total_degree()),
        "factor_terms": int(len(factor.dict())),
        "basis_size": len(basis),
        "unit": bool(unit),
    })
    payload.update({
        "progress": progress,
        "seconds": float(time.monotonic() - started),
        "unit_ideal": bool(unit),
        "terminal": "COMPLETE_CHART_UNIT_IDEAL" if unit else "SATURATION_PROGRESS",
    })
    print("DIRECT_COMPLETE_CHART_JSON " + json.dumps(
        payload, sort_keys=True, separators=(",", ":")
    ))
    sys.stdout.flush()
    if unit:
        break

if not payload["unit_ideal"]:
    basis = current.groebner_basis()
    payload.update({
        "dimension": int(current.dimension()),
        "basis_size": len(basis),
        "basis_sha256": hashlib.sha256(
            "\n".join(str(item) for item in basis).encode()
        ).hexdigest(),
        "terminal": "COMPLETE_CHART_NONUNIT_IDEAL",
    })
    print("DIRECT_COMPLETE_CHART_JSON " + json.dumps(
        payload, sort_keys=True, separators=(",", ":")
    ))
    sys.stdout.flush()

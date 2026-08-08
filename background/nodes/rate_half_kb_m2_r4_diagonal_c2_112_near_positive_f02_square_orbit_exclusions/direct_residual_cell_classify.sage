#!/usr/bin/env sage
"""Attempt one exact direct q-slice cell ideal over the deployed prime."""

load("/near_literal_assignment_transport_audit.sage")

import os
import sys
import time


cell = os.environ["DIRECT_CELL"]
assignment, root, allocation = cell.split("-")
target_id = f"{root}-{allocation}"
assert assignment in ("F02", "F04", "F06", "M01", "M03")
assert root in ("A", "OB")
assert allocation in ("RX", "RL", "RM")

residuals, systems = cache[assignment]
target_pair = TARGETS[target_id]
equations_qq = []
for residual, target in zip(residuals, target_pair):
    for index in (0, 1):
        raw = K(residual[index] - residual[2] * target[index])
        equations_qq.append(primitive(R(raw.numerator())))

p = 2130706433
Fp = GF(p)
S = PolynomialRing(Fp, names=("b", "c", "d"), order="degrevlex")
equations = [S(equation) for equation in equations_qq]
compile_payload = {
    "schema": "kb-c2-112-near-literal-direct-cell-classifier-v1",
    "cell": cell,
    "equation_count": int(len(equations)),
    "degrees": [int(equation.total_degree()) for equation in equations],
    "terms": [int(len(equation.dict())) for equation in equations],
    "terminal": "CELL_COMPILED",
}
print(
    "DIRECT_CELL_JSON "
    + json.dumps(compile_payload, sort_keys=True, separators=(",", ":"), default=int)
)
sys.stdout.flush()

started = time.monotonic()
basis = S.ideal(equations).groebner_basis()
unit = len(basis) == 1 and basis[0] == 1
payload = {
    **compile_payload,
    "basis_seconds": float(time.monotonic() - started),
    "basis_size": int(len(basis)),
    "unit_ideal": bool(unit),
    "terminal": "UNSATURATED_UNIT_IDEAL" if unit else "UNSATURATED_NONUNIT_IDEAL",
}
print(
    "DIRECT_CELL_JSON "
    + json.dumps(payload, sort_keys=True, separators=(",", ":"), default=int)
)
sys.stdout.flush()

if os.environ.get("DIRECT_SATURATE", "0") == "1" and not unit:
    localizer_texts = factor_set(systems[target_id], "I")
    localizers = [S(R(text)) for text in localizer_texts]
    localizers.sort(key=lambda value: (value.total_degree(), len(value.dict()), str(value)))
    current = S.ideal(equations)
    progress = []
    saturation_started = time.monotonic()
    for index, factor in enumerate(localizers):
        saturation = current.saturation(S.ideal([factor]))
        current = saturation if hasattr(saturation, "gens") else saturation[0]
        current_basis = current.groebner_basis()
        unit = len(current_basis) == 1 and current_basis[0] == 1
        progress.append({
            "index": int(index),
            "factor_degree": int(factor.total_degree()),
            "factor_terms": int(len(factor.dict())),
            "basis_size": int(len(current_basis)),
            "unit": bool(unit),
        })
        payload = {
            **payload,
            "localizer_count": int(len(localizers)),
            "saturation_progress": progress,
            "saturation_seconds": float(time.monotonic() - saturation_started),
            "unit_ideal": bool(unit),
            "terminal": (
                "SATURATED_UNIT_IDEAL" if unit else "SATURATION_PROGRESS"
            ),
        }
        print(
            "DIRECT_CELL_JSON "
            + json.dumps(payload, sort_keys=True, separators=(",", ":"), default=int)
        )
        sys.stdout.flush()
        if unit:
            break
    if not unit:
        payload["terminal"] = "SATURATED_NONUNIT_IDEAL"
        print(
            "DIRECT_CELL_JSON "
            + json.dumps(payload, sort_keys=True, separators=(",", ":"), default=int)
        )
        sys.stdout.flush()

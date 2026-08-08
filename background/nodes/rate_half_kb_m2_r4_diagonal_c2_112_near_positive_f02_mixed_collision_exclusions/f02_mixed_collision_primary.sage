#!/usr/bin/env sage
"""Sequential exact collision-localization proof for the two F02 mixed cells."""

load("/near_literal_assignment_transport_audit.sage")

import hashlib
import json
import os
import sys
import time


cell = os.environ["DIRECT_CELL"]
assert cell in ("F02-A-RM", "F02-OB-RM")
assignment, root, allocation = cell.split("-")
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

reconstruction_localizers = [
    S(R(text)) for text in factor_set(systems[target_id], "I")
]
reconstruction_localizers.sort(
    key=lambda value: (value.total_degree(), len(value.dict()), str(value))
)
collision = cS - dS

payload = {
    "schema": "kb-c2-112-near-positive-f02-mixed-collision-primary-v1",
    "cell": cell,
    "equation_count": len(equations),
    "equation_tuple_sha256": hashlib.sha256(
        "\n".join(str(item) for item in equations).encode()
    ).hexdigest(),
    "reconstruction_localizer_count": len(reconstruction_localizers),
    "chart_unit_localizers": ["b", "c", "d", "c-d"],
    "terminal": "COMPILED",
}
print("F02_MIXED_COLLISION_JSON " + json.dumps(
    payload, sort_keys=True, separators=(",", ":")
))
sys.stdout.flush()

started = time.monotonic()
current = S.ideal(equations)
progress = []
for name, factor in [
    *[(str(item), item) for item in reconstruction_localizers],
    ("b", bS),
    ("c", cS),
    ("d", dS),
]:
    saturation = current.saturation(S.ideal([factor]))
    current = saturation if hasattr(saturation, "gens") else saturation[0]
    basis = current.groebner_basis()
    progress.append({
        "factor": name,
        "basis_size": len(basis),
        "unit": bool(len(basis) == 1 and basis[0] == 1),
    })

pre_collision_basis = current.groebner_basis()
collision_remainder = collision.reduce(pre_collision_basis)
payload.update({
    "pre_collision_basis_size": len(pre_collision_basis),
    "pre_collision_basis_sha256": hashlib.sha256(
        "\n".join(str(item) for item in pre_collision_basis).encode()
    ).hexdigest(),
    "collision_remainder": str(collision_remainder),
    "localization_progress": progress,
})
print("F02_MIXED_COLLISION_JSON " + json.dumps(
    payload, sort_keys=True, separators=(",", ":")
))
sys.stdout.flush()

saturation = current.saturation(S.ideal([collision]))
terminal_ideal = saturation if hasattr(saturation, "gens") else saturation[0]
terminal_basis = terminal_ideal.groebner_basis()
unit = len(terminal_basis) == 1 and terminal_basis[0] == 1
payload.update({
    "basis_seconds": float(time.monotonic() - started),
    "terminal_basis_size": len(terminal_basis),
    "unit_ideal": bool(unit),
    "terminal": "COLLISION_SATURATED_UNIT_IDEAL" if unit else "NONUNIT_FAILURE",
})
print("F02_MIXED_COLLISION_JSON " + json.dumps(
    payload, sort_keys=True, separators=(",", ":")
))
sys.stdout.flush()

if not unit or collision_remainder != 0:
    raise RuntimeError("collision localization did not close the cell")

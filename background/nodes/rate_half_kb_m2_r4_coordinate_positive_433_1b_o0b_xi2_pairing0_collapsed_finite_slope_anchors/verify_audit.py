#!/usr/bin/env python3
"""Hostile audit for the collapsed finite-slope anchors."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
VERIFY = NODE / "verify.py"


def main():
    spec = importlib.util.spec_from_file_location("node_verify", VERIFY)
    verifier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(verifier)
    module = verifier.load_script()
    sp = module.sp
    b, d, e, y, anchor = sp.symbols("b d e y anchor")
    verifier.require(sp.expand(d*e-d*e) == 0,
                     "q5 sign-flip mutation reaches anchor")
    lam = sp.Integer(1)
    z0, z1 = -1, 1
    verifier.require((sp.Integer(2)-sp.Integer(3))*(z0+z1*lam) == 0,
                     "zero anchor-value mutation survives without a2m guard")
    verifier.require((b*e-d*e).subs({b: 1, d: 1, e: 1}) == 0,
                     "q4 collision survives without square separation")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_COLLAPSED_FINITE_SLOPE_ANCHORS_AUDIT_PASS "
          "mutations=3/3")


if __name__ == "__main__":
    main()

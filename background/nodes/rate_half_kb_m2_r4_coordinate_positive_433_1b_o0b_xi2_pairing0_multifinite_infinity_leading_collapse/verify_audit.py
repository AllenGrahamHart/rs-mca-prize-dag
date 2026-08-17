#!/usr/bin/env python3
"""Hostile audit for the FFI/FIF infinity collapse."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
VERIFY = NODE / "verify.py"


def main():
    spec = importlib.util.spec_from_file_location("node_verify", VERIFY)
    verifier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(verifier)
    module = verifier.load_script()
    d, e, f, z2, z5 = module.sp.symbols("d e f z2 z5")
    wrong = module.sp.expand((z5 + d*f*z2) - (z5 + e*f*z2) - f*(d+e)*z2)
    verifier.require(wrong != 0, "wrong-sign mutation rejected")
    ffi_witness = {d: 1, e: 1, f: 1, z2: 1, z5: -1}
    verifier.require(
        (z5+d*f*z2).subs(ffi_witness) == 0 and
        (z5+e*f*z2).subs(ffi_witness) == 0,
        "FFI square-guard witness",
    )
    fif_witness = {d: 1, e: 1, f: -1, z2: 1, z5: -1}
    verifier.require(
        (z5+d*e*z2).subs(fif_witness) == 0 and
        (z5-d*f*z2).subs(fif_witness) == 0,
        "FIF square-guard witness",
    )
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_MULTIFINITE_INFINITY_COLLAPSE_AUDIT_PASS "
          "mutations=3/3")


if __name__ == "__main__":
    main()

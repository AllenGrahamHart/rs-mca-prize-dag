#!/usr/bin/env python3
"""Hostile audit for the FFF generic-root dichotomy."""

import importlib.util
from pathlib import Path


VERIFY = Path(__file__).resolve().parent / "verify.py"


def main():
    spec = importlib.util.spec_from_file_location("generic_verify", VERIFY)
    verifier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(verifier)
    det_checker, root_checker = verifier.checkers()
    require = verifier.require
    require(det_checker.hostile_audit() == 5, "determinant mutations")
    require(root_checker.hostile_audit() == 4, "root mutations")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_XI2_PAIRING0_FFF_"
          "GENERIC_ROOT_DICHOTOMY_AUDIT_PASS mutations=9/9")


if __name__ == "__main__":
    main()

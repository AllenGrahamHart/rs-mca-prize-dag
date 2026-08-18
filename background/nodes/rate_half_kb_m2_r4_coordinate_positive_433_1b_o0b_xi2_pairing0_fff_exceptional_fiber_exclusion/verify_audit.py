#!/usr/bin/env python3
"""Hostile audit for exceptional FFF fiber exclusion."""

import importlib.util
from pathlib import Path


VERIFY = Path(__file__).resolve().parent / "verify.py"


def main():
    spec = importlib.util.spec_from_file_location("exception_verify", VERIFY)
    verifier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(verifier)
    first, second = verifier.checkers()
    verifier.require(first.hostile_audit() == 4, "first-wave mutations")
    verifier.require(second.hostile_audit() == 4, "final-wave mutations")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_XI2_PAIRING0_FFF_"
          "EXCEPTIONAL_FIBER_AUDIT_PASS mutations=8/8")


if __name__ == "__main__":
    main()

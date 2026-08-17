#!/usr/bin/env python3
"""Hostile audit for the O0b all-infinity chart exclusion."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
VERIFY = NODE / "verify.py"


def main():
    spec = importlib.util.spec_from_file_location("node_verify", VERIFY)
    verifier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(verifier)
    checker = verifier.load_checker()
    count = checker.hostile_audit()
    verifier.require(count == 3, "hostile mutation census")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_XI2_PAIRING0_ALL_INFINITY_AUDIT_PASS "
          "mutations=3/3")


if __name__ == "__main__":
    main()

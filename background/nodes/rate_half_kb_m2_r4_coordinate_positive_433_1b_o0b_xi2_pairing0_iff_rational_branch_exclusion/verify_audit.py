#!/usr/bin/env python3
"""Hostile audit for the O0b IFF rational-branch exclusion."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
VERIFY = NODE / "verify.py"


def main():
    spec = importlib.util.spec_from_file_location("node_verify", VERIFY)
    verifier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(verifier)
    checker = verifier.load("iff_check", verifier.CHECK)
    verifier.require(checker.hostile_audit() == 3,
                     "checker hostile mutations")
    row = json.loads(verifier.RESULT.read_text())["row"]
    verifier.require(row["route_stages"][4]["dimension"] == 0 and
                     row["route_stages"][4]["basis_size"] == 44,
                     "pre-b+1 locus nonunit")
    verifier.require(row["route_stages"][5]["dimension"] == -1 and
                     row["route_stages"][5]["basis_size"] == 1,
                     "b+1 removes final locus")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_IFF_RATIONAL_BRANCH_EXCLUSION_AUDIT_PASS "
          "mutations=5/5")


if __name__ == "__main__":
    main()

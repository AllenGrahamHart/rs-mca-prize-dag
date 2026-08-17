#!/usr/bin/env python3
"""Hostile audit for the exact O0b FFI/FIF exclusions."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
VERIFY = NODE / "verify.py"


def main():
    spec = importlib.util.spec_from_file_location("node_verify", VERIFY)
    verifier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(verifier)
    checker = verifier.load("admissible_check", verifier.CHECK)
    verifier.require(checker.hostile_audit() == 3,
                     "checker hostile mutations")
    payload = json.loads(verifier.RESULT.read_text())
    stages = payload["row"]["stages"]
    verifier.require(stages[4]["basis_size"] == 22 and
                     stages[4]["dimension"] == 0,
                     "pre-b+1 locus nonunit")
    verifier.require(stages[5]["basis_size"] == 1 and
                     stages[5]["dimension"] == -1,
                     "b+1 removes final locus")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFI_FIF_COLLAPSED_COMMON_EXCLUSIONS_AUDIT_PASS "
          "mutations=5/5")


if __name__ == "__main__":
    main()

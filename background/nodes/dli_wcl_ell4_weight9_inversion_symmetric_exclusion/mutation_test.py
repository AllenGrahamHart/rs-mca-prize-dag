#!/usr/bin/env python3
"""Hostile mutations for the independent WCL (4,9) component audit."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("wcl49_inversion_audit", HERE / "verify_audit.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)
baseline = json.loads(MODULE.RESULT.read_text())


def rejected(mutator):
    candidate = copy.deepcopy(baseline)
    mutator(candidate)
    try:
        MODULE.audit(candidate, emit=False)
    except (AssertionError, ValueError):
        return True
    return False


assert rejected(lambda data: data["branches"].pop())
assert rejected(lambda data: data["branches"][0].__setitem__("obstruction_gcd", "2"))
assert rejected(
    lambda data: data["branches"][4]["remainder"][0].__setitem__(
        "resultant", str(int(data["branches"][4]["remainder"][0]["resultant"]) + 1)
    )
)
assert rejected(lambda data: data.__setitem__("official_compatible_exception_primes", [17]))

print("DLI_WCL_ELL4_WEIGHT9_INVERSION_SYMMETRIC_EXCLUSION_MUTATION_PASS controls=4")

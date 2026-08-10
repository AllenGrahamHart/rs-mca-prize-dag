#!/usr/bin/env python3
"""Hostile controls for the repeated-BC missing-CF residual exclusion."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cf_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(source, payload, label):
    try:
        VERIFY.validate(source, payload)
    except (RuntimeError, KeyError, ValueError):
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    source = json.loads(VERIFY.SOURCE.read_text())
    payload = json.loads(VERIFY.RESULT.read_text())
    VERIFY.validate(source, payload)
    mutation = copy.deepcopy(payload)
    mutation["rows"].pop()
    reject(source, mutation, "lost case")
    mutation = copy.deepcopy(payload)
    mutation["rows"][0]["kernel"][0] ^= 1
    reject(source, mutation, "kernel")
    mutation = copy.deepcopy(payload)
    mutation["rows"][0]["pairing_rows"][0][
        "selected_resultant_coefficients"
    ][0] ^= 1
    reject(source, mutation, "resultant")
    mutation = copy.deepcopy(payload)
    mutation["rows"][0]["pairing_rows"][0]["selected_roots"].append(1)
    reject(source, mutation, "projected root")
    mutation = copy.deepcopy(payload)
    mutation["rows"][0]["pairing_rows"][0]["fiber_certificates"][0][
        "gcd_coefficients"
    ] = [0, 1]
    reject(source, mutation, "fiber gcd")
    print("PASS repeated-BC BC+ missing-CF residual hostile audit: 5/5")


if __name__ == "__main__":
    main()

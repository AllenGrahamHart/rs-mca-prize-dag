#!/usr/bin/env python3
"""Hostile controls for the cell-3 BC- colored norm atlas."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("norm_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(payload):
    try:
        VERIFY.validate(payload)
    except RuntimeError:
        return
    raise RuntimeError("mutation survived")


def main():
    payload = json.loads((VERIFY.EXPERIMENTS / VERIFY.RESULT).read_text())
    VERIFY.validate(payload)
    mutation = copy.deepcopy(payload)
    mutation["rows"].pop()
    reject(mutation)
    mutation = copy.deepcopy(payload)
    mutation["rows"][0]["cut_norm_numerator"].pop()
    reject(mutation)
    mutation = copy.deepcopy(payload)
    mutation["rows"][0]["construction_guards"].popitem()
    reject(mutation)
    mutation = copy.deepcopy(payload)
    digest = next(iter(mutation["rows"][0]["construction_guards"]))
    mutation["rows"][0]["construction_guards"][digest][0] ^= 1
    reject(mutation)
    mutation = copy.deepcopy(payload)
    mutation["status_counts"] = {}
    reject(mutation)
    print("PASS repeated-BC cell3 BC- colored norm hostile audit: 5/5")


if __name__ == "__main__":
    main()

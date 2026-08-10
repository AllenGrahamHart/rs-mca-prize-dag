#!/usr/bin/env python3
"""Hostile controls for cells 3 and 6 compact loci."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("compact_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(payload, label):
    try:
        VERIFY.validate(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    payload = json.loads((VERIFY.EXPERIMENTS / VERIFY.FILES["result"][0]).read_text())
    VERIFY.validate(payload)
    mutation = copy.deepcopy(payload); mutation["rows"].pop(); reject(mutation, "lost case")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["common_dimension"] = 0; reject(mutation, "dimension")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["reduced_remainders"][9] = "1"; reject(mutation, "remainder")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["identically_zero_rows"][6] = False; reject(mutation, "identity")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["kernel"][0]["sha256"] = "0" * 64; reject(mutation, "kernel custody")
    print("PASS repeated-BC cells3/6 compact hostile audit: 5/5")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Hostile controls for the uncolored generic-rank atlas."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("rank_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(payload, label):
    try:
        VERIFY.validate(payload)
    except (RuntimeError, KeyError, ValueError):
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    payload = json.loads(VERIFY.RESULT.read_text())
    VERIFY.validate(payload)
    mutation = copy.deepcopy(payload)
    mutation["rows"].pop()
    reject(mutation, "lost case")
    mutation = copy.deepcopy(payload)
    mutation["rows"][0]["selected"]["rank"] -= 1
    reject(mutation, "rank drop")
    mutation = copy.deepcopy(payload)
    mutation["rows"][0]["matching"][0].reverse()
    reject(mutation, "matching")
    mutation = copy.deepcopy(payload)
    digest = next(iter(mutation["guard_atlas"]))
    mutation["guard_atlas"][digest] += ",1"
    reject(mutation, "guard coefficients")
    mutation = copy.deepcopy(payload)
    mutation["rows"][0]["guard_hashes"].pop()
    reject(mutation, "guard cover")
    print("PASS uncolored generic-rank hostile audit: 5/5")


if __name__ == "__main__":
    main()

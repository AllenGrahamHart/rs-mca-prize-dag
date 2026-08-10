#!/usr/bin/env python3
"""Hostile controls for the repeated-BC cell-3 BC+ torus locus."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("torus_verify", NODE / "verify.py")
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
    mutation = copy.deepcopy(payload); mutation["rows"][0]["gcd_identity"] = False; reject(mutation, "gcd")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["torus_core"]["expression"] = "1"; reject(mutation, "core")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["t_relation_remainder"] = "r"; reject(mutation, "relation")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["saturated_unit"] = False; reject(mutation, "residual")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["parameter_dimension"] = 0; reject(mutation, "dimension")
    print("PASS repeated-BC cell3 BC+ torus hostile audit: 6/6")


if __name__ == "__main__":
    main()

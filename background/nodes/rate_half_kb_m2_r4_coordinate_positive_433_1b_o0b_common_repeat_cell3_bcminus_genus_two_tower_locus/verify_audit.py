#!/usr/bin/env python3
"""Hostile controls for the repeated-BC cell-3 BC- tower locus."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("bcminus_tower_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(function, payload, label):
    try:
        function(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    projection = json.loads((
        VERIFY.EXPERIMENTS / VERIFY.FILES["projection_result"][0]
    ).read_text())
    tower = json.loads((
        VERIFY.EXPERIMENTS / VERIFY.FILES["tower_result"][0]
    ).read_text())
    VERIFY.validate_projection(projection)
    VERIFY.validate_tower(tower)
    mutation = copy.deepcopy(projection); mutation["rows"].pop()
    reject(VERIFY.validate_projection, mutation, "lost projection row")
    mutation = copy.deepcopy(projection); mutation["rows"][0]["elimination_output"] = "1"
    reject(VERIFY.validate_projection, mutation, "projection")
    mutation = copy.deepcopy(tower); mutation["rows"][0]["r_relation"] = "1"
    reject(VERIFY.validate_tower, mutation, "r relation")
    mutation = copy.deepcopy(tower); mutation["rows"][0]["remainders"]["primitive_0_mod_tower"] = "r"
    reject(VERIFY.validate_tower, mutation, "containment")
    mutation = copy.deepcopy(tower); mutation["rows"][0]["tower_dimension"] = 0
    reject(VERIFY.validate_tower, mutation, "dimension")
    mutation = copy.deepcopy(tower); mutation["source_sha256"] = "0"*64
    reject(VERIFY.validate_tower, mutation, "source")
    print("PASS repeated-BC cell3 BC- tower hostile audit: 6/6")


if __name__ == "__main__":
    main()

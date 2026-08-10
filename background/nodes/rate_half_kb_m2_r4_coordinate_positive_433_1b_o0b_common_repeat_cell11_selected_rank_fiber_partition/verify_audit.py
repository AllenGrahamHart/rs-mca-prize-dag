#!/usr/bin/env python3
"""Hostile controls for the cell-11 selected-rank fiber partition."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell11_rank_verify", NODE / "verify.py")
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
    mutation = copy.deepcopy(payload); mutation["rows"].pop()
    reject(mutation, "lost row")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["t_relation_remainder"] = "r"
    reject(mutation, "t relation")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["selected_rank_minor_remainder"] = "0"
    reject(mutation, "zero cofactor")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["selected_rank_fiber_dimension"] = 1
    reject(mutation, "fiber dimension")
    mutation = copy.deepcopy(payload); mutation["rows"][1]["selected_rank_fiber_vdim"] = 5
    reject(mutation, "fiber degree")
    mutation = copy.deepcopy(payload); mutation["source_sha256"] = "0" * 64
    reject(mutation, "source")
    print("PASS repeated-BC cell11 selected-rank fiber hostile audit: 6/6")


if __name__ == "__main__":
    main()

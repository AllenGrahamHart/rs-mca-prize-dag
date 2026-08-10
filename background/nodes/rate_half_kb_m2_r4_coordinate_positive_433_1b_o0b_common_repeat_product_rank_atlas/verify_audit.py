#!/usr/bin/env python3
"""Hostile controls for the repeated-BC product-rank atlas."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("product_verify", NODE / "verify.py")
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
    mutation = copy.deepcopy(payload); mutation["rows"][0]["raw"].pop(); reject(mutation, "lost cofactor")
    mutation = copy.deepcopy(payload); mutation["guard_only_cells"].pop("3:-1"); reject(mutation, "guard-only set")
    mutation = copy.deepcopy(payload); mutation["stripped_degree_histogram"]["0"] = 7; reject(mutation, "histogram")
    print("PASS repeated-BC product-rank atlas hostile audit: 4/4")


if __name__ == "__main__":
    main()

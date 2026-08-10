#!/usr/bin/env python3
"""Hostile controls for the cell-11 common-kernel reconstruction."""

import copy
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell11_kernel_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(payload, label):
    try:
        VERIFY.validate(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    payload = VERIFY.load()
    VERIFY.validate(payload)
    mutation = copy.deepcopy(payload); mutation["rows"].pop()
    reject(mutation, "coverage")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["tower_checks"][1] = False
    reject(mutation, "tower")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["product_kernel_checks"][2] = False
    reject(mutation, "product")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["sum_kernel_checks"][4] = False
    reject(mutation, "sum")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["kernel_nonzero"][0] = False
    reject(mutation, "cofactor")
    mutation = copy.deepcopy(payload); mutation["rows"][1]["missing_product_degrees"]["numerator"] += 1
    reject(mutation, "missing coordinate")
    print("PASS repeated-BC cell11 common-kernel hostile audit: 6/6")


if __name__ == "__main__":
    main()

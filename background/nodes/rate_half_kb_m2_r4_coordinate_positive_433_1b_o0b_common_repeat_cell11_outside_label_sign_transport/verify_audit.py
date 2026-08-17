#!/usr/bin/env python3
"""Hostile controls for the cell-11 outside-label sign transport."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("sign_transport_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(permutation, label):
    try:
        VERIFY.validate(permutation)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    VERIFY.validate(VERIFY.ROUTER.D_SIGN_FLIP)
    reject(tuple(range(7)), "identity")
    reject((0, 1, 3, 2, 4, 5, 6), "one sign pair")
    reject((0, 1, 3, 2, 5, 4, 4), "non-bijection")
    print("PASS repeated-BC cell11 outside-label sign transport audit: 3/3")


if __name__ == "__main__":
    main()

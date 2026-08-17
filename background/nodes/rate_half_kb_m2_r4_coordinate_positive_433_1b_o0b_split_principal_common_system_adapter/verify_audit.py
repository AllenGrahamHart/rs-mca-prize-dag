#!/usr/bin/env python3
"""Hostile controls for the O0b split common-system adapter."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("split_adapter_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(keys, products, label):
    try:
        VERIFY.validate(keys, products)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    VERIFY.validate()
    keys = (("S0", -1), ("S0", 1), ("SDE", -1), ("SDE", 1), ("SDF", -1))
    reject(keys, None, "missing lane")
    reject(None, ("-a^2", "a*b", "a*c", "b*c", "b*c"), "common sign")
    print("PASS O0b split principal common-system adapter audit: 2/2")


if __name__ == "__main__":
    main()

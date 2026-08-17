#!/usr/bin/env python3
"""Hostile controls for the duplicate-role cells 11-14 transport."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cells11_14_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(partner, rows, label):
    try:
        VERIFY.validate(partner, rows)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    VERIFY.validate()
    reject(13, ("BC", "BC"), "wrong partner")
    reject(14, ("BC1", "BC2"), "nonduplicate target rows")
    print("PASS repeated-BC cells11-14 duplicate-role transport audit: 2/2")


if __name__ == "__main__":
    main()

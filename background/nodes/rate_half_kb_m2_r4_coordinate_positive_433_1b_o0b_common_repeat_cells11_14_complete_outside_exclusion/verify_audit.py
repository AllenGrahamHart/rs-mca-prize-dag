#!/usr/bin/env python3
"""Hostile controls for the complete cells 11-14 assembly."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cells11_14_complete_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(cells, rows, labels, label):
    try:
        VERIFY.validate(cells, rows, labels)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    VERIFY.validate()
    reject((11,), 16, 105, "missing cell14")
    reject((11, 14), 16, 104, "missing label")
    print("PASS complete repeated-BC cells11-14 audit: 2/2")


if __name__ == "__main__":
    main()

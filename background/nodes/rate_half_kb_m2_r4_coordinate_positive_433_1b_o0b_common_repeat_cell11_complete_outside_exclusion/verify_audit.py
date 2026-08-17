#!/usr/bin/env python3
"""Hostile controls for the complete cell-11 outside assembly."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell11_complete_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(records, towers, signs, label):
    try:
        VERIFY.validate(records, towers, signs)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    VERIFY.validate()
    reject(VERIFY.RECORDS[:-1], 8, (-1, 1), "missing record")
    reject(VERIFY.RECORDS, 7, (-1, 1), "missing tower")
    reject(VERIFY.RECORDS, 8, (1,), "missing outside sign")
    print("PASS complete repeated-BC cell11 outside assembly audit: 3/3")


if __name__ == "__main__":
    main()

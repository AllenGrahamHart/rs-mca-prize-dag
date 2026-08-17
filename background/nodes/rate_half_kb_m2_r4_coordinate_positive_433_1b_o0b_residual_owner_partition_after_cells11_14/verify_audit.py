#!/usr/bin/env python3
"""Hostile controls for the revised O0b owner partition."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("o0b_owner_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(blocks, label):
    try:
        VERIFY.validate(blocks)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    VERIFY.validate()
    reject((("split_rank5", 360), ("cells1_2", 16), ("cells11_14", 31)),
           "removed block size")
    reject((("split_rank5", 359), ("cells1_2", 16), ("cells11_14", 32)),
           "residual size")
    print("PASS revised O0b owner partition audit: 2/2")


if __name__ == "__main__":
    main()

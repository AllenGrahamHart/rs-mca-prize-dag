#!/usr/bin/env python3
"""Hostile controls for the cell-11 uncolored generic-rank atlas."""

import copy
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell11_rank_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(payload, bc_sign, label):
    try:
        VERIFY.validate(payload, bc_sign)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    plus = VERIFY.load("plus")
    minus = VERIFY.load("minus")
    VERIFY.validate(plus, 1); VERIFY.validate(minus, -1)
    mutation = copy.deepcopy(plus); mutation["rows"].pop()
    reject(mutation, 1, "coverage")
    mutation = copy.deepcopy(plus); mutation["rows"][0]["status"] = "NO_UNIT_PAIR"
    reject(mutation, 1, "status")
    mutation = copy.deepcopy(plus); mutation["rows"][0]["selected"]["witness_x"] = 3
    reject(mutation, 1, "specialization")
    mutation = copy.deepcopy(minus); mutation["rows"][0]["selected"]["witness_determinant"] = 0
    reject(mutation, -1, "determinant")
    mutation = copy.deepcopy(minus); mutation["rows"][0]["selected"]["construction_guards_nonzero"] = False
    reject(mutation, -1, "guard")
    mutation = copy.deepcopy(minus); mutation["rows"][0]["selected"]["last_rank"] -= 1
    reject(mutation, -1, "rank")
    print("PASS repeated-BC cell11 uncolored generic-rank hostile audit: 6/6")


if __name__ == "__main__":
    main()

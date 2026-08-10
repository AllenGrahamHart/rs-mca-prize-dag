#!/usr/bin/env python3
"""Hostile controls for the complete O0b common compiler atlas."""

import copy
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("common_atlas_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def rejected(rows, counts, label):
    try:
        VERIFY.validate(rows, counts)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    assembly = VERIFY.load_assembly()
    rows, counts = assembly.assemble()
    VERIFY.validate(rows, counts)

    mutation = copy.deepcopy(rows)
    mutation.pop()
    rejected(mutation, counts, "lost lane")

    mutation = copy.deepcopy(rows)
    mutation[0]["compiler"] = "repeat" if mutation[0]["compiler"] == "split" else "split"
    rejected(mutation, counts, "compiler class")

    mutation = dict(counts)
    mutation["formal_common_systems"] -= 60
    rejected(rows, mutation, "formal census")

    mutation = dict(counts)
    mutation["distinct_algebra_rows"] += 60
    rejected(rows, mutation, "distinct census")
    print("PASS O0b common compiler atlas hostile audit: 4/4")


if __name__ == "__main__":
    main()

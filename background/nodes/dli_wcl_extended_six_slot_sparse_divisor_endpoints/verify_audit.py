#!/usr/bin/env python3
"""Mutation audit for the extended WCL endpoint verifier."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("endpoint_verify", HERE / "verify.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def rejected(row: tuple[int, ...]) -> bool:
    try:
        MODULE.verify_row(row)
    except AssertionError:
        return True
    return False


def main() -> None:
    caught = 0
    for index, row in enumerate(MODULE.ROWS):
        mutated = list(row)
        mutated[6] += 1
        caught += rejected(tuple(mutated))

        mutated = list(row)
        mutated[7] -= 1
        caught += rejected(tuple(mutated))

        mutated = list(row)
        mutated[8] += index + 1
        caught += rejected(tuple(mutated))

        mutated = list(row)
        mutated[9] += 1
        caught += rejected(tuple(mutated))

    assert caught == 24, caught
    print("DLI_WCL_EXTENDED_SIX_ENDPOINTS_AUDIT_PASS mutations=24")


if __name__ == "__main__":
    main()

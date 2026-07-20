#!/usr/bin/env python3
"""Mutation audit for the RF3-double-prime exact-row verifier."""

from __future__ import annotations

from copy import deepcopy

from verify import ROWS, check_rows


def rejected(rows: list[dict[str, int | str]]) -> None:
    try:
        check_rows(tuple(rows))
    except AssertionError:
        return
    raise AssertionError("semantic mutation was accepted")


def main() -> None:
    bad = deepcopy(list(ROWS))
    bad[0]["upper"] = int(bad[0]["upper"]) - 1
    rejected(bad)

    bad = deepcopy(list(ROWS))
    bad[1]["A"] = int(bad[1]["A"]) + 1
    rejected(bad)

    bad = deepcopy(list(ROWS))
    bad[2]["margin"] = int(bad[2]["margin"]) + 1
    rejected(bad)

    bad = deepcopy(list(ROWS))
    bad[3]["V"] = int(bad[3]["V"]) - 1
    rejected(bad)

    print("PAVING_RF3_DOUBLE_PRIME_KOALABEAR_SAFE_ROWS_AUDIT_PASS mutations=4")


if __name__ == "__main__":
    main()

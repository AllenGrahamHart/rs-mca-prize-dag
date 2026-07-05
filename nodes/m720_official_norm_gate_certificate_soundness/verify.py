#!/usr/bin/env python3
"""Tiny checker for official M720 norm-gate payload semantics."""

from __future__ import annotations


def accepts_payload(expected_cases, records) -> bool:
    by_case = {tuple(record["case"]): record for record in records}
    for case in expected_cases:
        record = by_case.get(tuple(case))
        if record is None:
            return False
        if record.get("branch") != "primitive_norm_gate":
            return False
        if record.get("complete") is not True:
            return False
        if record.get("unpaid_non_toral_survivors") != 0:
            return False
    return True


def main() -> None:
    expected = [(128, 7), (128, 8), (256, 20)]
    good = [
        {
            "case": [128, 7],
            "branch": "primitive_norm_gate",
            "complete": True,
            "unpaid_non_toral_survivors": 0,
        },
        {
            "case": [128, 8],
            "branch": "primitive_norm_gate",
            "complete": True,
            "unpaid_non_toral_survivors": 0,
        },
        {
            "case": [256, 20],
            "branch": "primitive_norm_gate",
            "complete": True,
            "unpaid_non_toral_survivors": 0,
        },
    ]
    assert accepts_payload(expected, good)

    missing = good[:-1]
    assert not accepts_payload(expected, missing)

    incomplete = [dict(record) for record in good]
    incomplete[0]["complete"] = False
    assert not accepts_payload(expected, incomplete)

    nonzero = [dict(record) for record in good]
    nonzero[1]["unpaid_non_toral_survivors"] = 1
    assert not accepts_payload(expected, nonzero)

    print("PASS: official norm-gate payload semantics")


if __name__ == "__main__":
    main()

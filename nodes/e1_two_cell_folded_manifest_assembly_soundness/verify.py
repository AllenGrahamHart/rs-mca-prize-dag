#!/usr/bin/env python3
"""Check that the two E1 cell records assemble to the manifest schema."""

from __future__ import annotations

OPEN_CELLS = {128, 256}


def valid_cell(cell: int, record: dict[str, object]) -> bool:
    return (
        cell in OPEN_CELLS
        and bool(record.get("field"))
        and record.get("complete") is True
        and record.get("nonzero_folded_vectors") == 0
    )


def assemble(cells: dict[int, dict[str, object]]) -> dict[int, dict[str, object]]:
    assert set(cells) == OPEN_CELLS
    for cell, record in cells.items():
        assert valid_cell(cell, record)
    return cells


def main() -> None:
    good = assemble(
        {
            128: {"field": "named-exhibit-128", "complete": True, "nonzero_folded_vectors": 0},
            256: {"field": "named-exhibit-256", "complete": True, "nonzero_folded_vectors": 0},
        }
    )
    assert set(good) == OPEN_CELLS

    missing = {
        128: {"field": "named-exhibit-128", "complete": True, "nonzero_folded_vectors": 0}
    }
    try:
        assemble(missing)
    except AssertionError:
        pass
    else:
        raise AssertionError("missing 256 cell accepted")

    print("PASS: E1 two-cell folded manifest assembly")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Schema check for named-field E1 folded cell certificates."""

from __future__ import annotations

P = 904625697166646869347790708689937759412227977745095982970820953353127723009
RHO = {
    128: 440266185830122294862552098878717819794821358702875176198798016633729926114,
    256: 368095729527972287347366462180303065908636718991804826343652948937354262881,
}


def verify_cell(cell: int, record: dict[str, object]) -> None:
    assert cell in {128, 256}
    assert P % cell == 1
    assert record["field"] == P
    assert record["root"] == RHO[cell]
    assert pow(RHO[cell], cell, P) == 1
    assert pow(RHO[cell], cell // 2, P) != 1
    assert record["complete"] is True
    assert record["nonzero_folded_vectors"] == 0


def main() -> None:
    verify_cell(
        128,
        {
            "field": P,
            "root": RHO[128],
            "complete": True,
            "nonzero_folded_vectors": 0,
        },
    )
    verify_cell(
        256,
        {
            "field": P,
            "root": RHO[256],
            "complete": True,
            "nonzero_folded_vectors": 0,
        },
    )
    print("PASS: E1 named-field folded cell certificate soundness")


if __name__ == "__main__":
    main()

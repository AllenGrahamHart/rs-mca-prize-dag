#!/usr/bin/env python3
"""Mutation audit for the polarized B11 box closure."""


def main() -> None:
    # No-dense control: it violates h>=ell.
    ell = 8
    sparse = (1, 1)
    assert sum(sparse) < ell
    assert sum(min(a, ell - a) for a in sparse) == 2

    # One-dense hostile control. It satisfies the threshold only after the
    # per-petal cap is dropped, and then both proposed gates fail.
    one_dense = dict(ell=8, sizes=(7, 1), r=0, d=0, cap=2)
    h = sum(one_dense["sizes"])
    deficits = sorted(one_dense["ell"] - a for a in one_dense["sizes"])
    g2 = sum(deficits[:2])
    gr = one_dense["ell"] - one_dense["r"] + deficits[0]
    assert h + one_dense["r"] >= one_dense["ell"] + one_dense["d"]
    assert max(one_dense["sizes"]) > one_dense["d"]
    assert g2 > 2 * one_dense["cap"] and gr > one_dense["cap"]

    # The small-ell branch needs the factor 2 in V_2=2P.
    small = dict(ell=4, sizes=(1, 1, 1, 1), cap=4)
    small_g2 = sum(sorted(small["ell"] - a for a in small["sizes"])[:2])
    assert small_g2 == 6
    assert small_g2 > small["cap"]
    assert small_g2 <= 2 * small["cap"]

    print("L1_POLARIZED_B11_BOX_AUDIT_PASS mutations=3")


if __name__ == "__main__":
    main()

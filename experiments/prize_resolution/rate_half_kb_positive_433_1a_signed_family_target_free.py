#!/usr/bin/env python3
"""Verify the target-free unsquared signed-family identities."""

import sympy as sp


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify():
    D0, D1, D2, N0, N1, N2 = sp.symbols(
        "D0 D1 D2 N0 N1 N2", nonzero=True
    )
    Q0, Q1, Q2, Delta, scale = sp.symbols(
        "Q0 Q1 Q2 Delta scale", nonzero=True
    )
    y, v = sp.symbols("y v")

    products = (N0/D0, N1/D1, N2/D2)
    sums = (
        -Q0/(Delta*D0),
        -Q1/(Delta*D1),
        -Q2/(Delta*D2),
    )
    cuts = (
        N1*D0+N0*D1,
        Q0**2*D1**2-Q1**2*D0**2
        -4*N0*Delta**2*D0*D1**2,
        2*N2*Delta*D0*D1-scale*D2*(Q1*D0-Q0*D1),
        -2*Q2*D0*D1-2*scale*Delta*D0*D1*D2
        -D2*(Q1*D0-Q0*D1),
    )
    realization = {
        N0: D0*y*v,
        N1: -D1*y*v,
        N2: D2*scale*v,
        Q0: -Delta*D0*(y+v),
        Q1: -Delta*D1*(y-v),
        Q2: -Delta*D2*(scale+v),
    }
    require(all(sp.expand(cut.subs(realization)) == 0 for cut in cuts),
            "forward target elimination")

    reconstructed_y = (sums[0]+sums[1])/2
    reconstructed_v = (sums[0]-sums[1])/2
    residuals = (
        products[1]+products[0],
        reconstructed_y*reconstructed_v-products[0],
        products[2]-scale*reconstructed_v,
        sums[2]-scale-reconstructed_v,
    )
    cleared_residuals = (
        cuts[0]/(D0*D1),
        cuts[1]/(4*Delta**2*D0**2*D1**2),
        cuts[2]/(2*Delta*D0*D1*D2),
        cuts[3]/(2*Delta*D0*D1*D2),
    )
    require(all(sp.cancel(left-right) == 0
                for left, right in zip(residuals, cleared_residuals)),
            "converse reconstruction identities")
    return {
        "cut_count": len(cuts),
        "source_slot_count": 3,
        "target_variables_eliminated": 2,
        "families": ("DE+/DE-/BE", "DF+/DF-/CF"),
    }


def main():
    result = verify()
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_SIGNED_FAMILY_TARGET_FREE_PASS "
        f"cuts={result['cut_count']} slots={result['source_slot_count']} "
        f"targets_eliminated={result['target_variables_eliminated']}"
    )


if __name__ == "__main__":
    main()

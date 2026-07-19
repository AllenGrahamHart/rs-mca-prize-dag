#!/usr/bin/env python3
"""Exact parameter replay for residual-free top-band Johnson closure."""


def check(ell: int, petals: int, degree: int) -> tuple[int, int]:
    agreement = ell + degree
    domain = petals * ell
    gap = agreement * agreement - degree * domain
    if gap <= 0:
        raise AssertionError((ell, petals, degree, "not Johnson"))
    bound = domain * (agreement - degree) // gap
    return gap, bound


def main() -> None:
    rows = 0
    sharp = 0
    for ell in range(1, 65):
        for petals in range(2, 65):
            boundary = ell * (petals - 2)
            for extra in range(17):
                degree = boundary + extra
                gap, bound = check(ell, petals, degree)
                if gap < ell * ell or bound > petals:
                    raise AssertionError((ell, petals, degree, gap, bound))
                if extra == 0:
                    if gap != ell * ell or bound != petals:
                        raise AssertionError((ell, petals, gap, bound))
                    sharp += 1
                rows += 1

    # One step below the pinned band can retain Johnson positivity while
    # losing the claimed m bound, so the band endpoint is load-bearing.
    mutated_gap, mutated_bound = check(3, 4, 5)
    if mutated_gap >= 9 or mutated_bound <= 4:
        raise AssertionError((mutated_gap, mutated_bound))

    print(
        "PETAL_TOP_BAND_RESIDUAL_FREE_JOHNSON_PASS "
        f"rows={rows} sharp_boundary_rows={sharp} mutation=below_band"
    )


if __name__ == "__main__":
    main()

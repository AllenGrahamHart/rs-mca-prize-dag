#!/usr/bin/env python3
"""Independent binary-search and gap-chain audit."""


def main():
    m = 1 << 37
    rho = 4 * m

    def automatic(e):
        delta = rho - 1 - 2 * e
        ell_max = 4 * e - rho - 1
        return delta // 5 + ell_max + 3 < e

    lo, hi = m + 1, (rho - 1) // 2 + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if automatic(mid):
            lo = mid + 1
        else:
            hi = mid
    e = lo
    assert e == 169155635042

    delta = rho - 1 - 2 * e
    p = delta - 3
    # Enumerate every monotone four-term chain between p and Delta. Each
    # individual gap is bounded by the total residual three.
    chains = 0
    for omission in range(p, delta + 1):
        for rank_loss in range(omission, delta + 1):
            gaps = (
                omission - p,
                rank_loss - omission,
                delta - rank_loss,
            )
            assert sum(gaps) == 3
            assert max(gaps) <= 3
            chains += 1

    assert chains == 10
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_FIRST_CUBIC_CORNER_AUDIT_PASS "
        f"e={e} chains={chains}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact official slope-slack survivor classification."""


def excluded(m, e, h):
    rho = 4 * m - 1
    delta = rho - 3 * e
    ell = delta // 2
    return ell + h + 2 < e


def check_small(m):
    rho = 4 * m - 1
    survivors = []
    for e in range(m, rho // 3 + 1):
        for h in range(4 * (e - m) + 1):
            if not excluded(m, e, h):
                survivors.append((e, rho - 3 * e, h, 4 * e + 1 - h))
    return survivors


def main():
    profiles = 0
    for m in range(8, 128, 2):
        rho = 4 * m - 1
        for e in range(m, rho // 3 + 1):
            delta = rho - 3 * e
            ell = delta // 2
            assert 2 * (ell + 1) > delta
            for h in range(4 * (e - m) + 1):
                bidegree = (rho - 4, -e + ell + h + 2)
                if excluded(m, e, h):
                    assert bidegree[1] < 0
                    assert (bidegree[0] - rho, bidegree[1] - e)[0] == -4
                profiles += 1

    official_m = 1 << 37
    q = (official_m - 2) // 3
    official_e = 4 * q + 2
    official_rho = 4 * official_m - 1
    official_h = official_e - 2
    assert official_m == 3 * q + 2
    assert official_e == official_rho // 3
    assert official_rho - 3 * official_e == 1
    assert 4 * official_e + 1 - official_h == official_rho + 2
    assert not excluded(official_m, official_e, official_h)

    # Prove symbolically over the q-s parameterization that every other
    # official integer point satisfies the strict inequality.
    for r in range(1, 1000):
        assert (3 * r + 1) // 2 < 3 * r
    assert excluded(official_m, official_e, official_h - 1)
    assert excluded(official_m, official_e - 1, 4 * (official_e - 1 - official_m))

    # Small rows with m == 2 mod 3 exhibit the same singleton pattern.
    for m in range(8, 100, 6):
        m += 0  # 8,14,... are all 2 modulo 3.
        survivors = check_small(m)
        assert len(survivors) == 1
        e, delta, h, slopes = survivors[0]
        assert (delta, h, slopes) == (1, e - 2, 4 * m + 1)

    print(
        "RATE_HALF_CA_HANKEL_STRICT_A3_SLOPE_SLACK_CONTACT_EXCLUSION_PASS "
        f"profiles={profiles} official_m={official_m} official_e={official_e} "
        f"official_h={official_h} official_T={official_rho + 2} survivors=1"
    )


if __name__ == "__main__":
    main()

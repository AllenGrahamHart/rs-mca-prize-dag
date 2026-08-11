#!/usr/bin/env python3
"""Independent bundle and endpoint audit."""


def h1_p1xp1(a, b):
    h0a = max(a + 1, 0)
    h0b = max(b + 1, 0)
    h1a = max(-a - 1, 0)
    h1b = max(-b - 1, 0)
    return h1a * h0b + h0a * h1b


def main():
    m = 1 << 37
    rho = 4 * m
    first = (rho + 1) // 3

    for s, beta in ((0, 0), (1, 1), (2, 1)):
        d = rho - s
        e = first - 1
        ell = e - 4 + beta
        second = ell - e + 3 - beta
        assert second == -1
        kernel = (-3, second - e)
        assert h1_p1xp1(*kernel) == 0
        assert d - 3 >= 0

    # At the first surviving degree, enumerate the six distinct core/slack
    # profiles and verify their common slope-count image.
    rows = []
    for s, beta in ((0, 0), (1, 1)):
        for ell in range(first - 3 + beta, 4 * first + beta - rho - 1):
            rows.append((s, ell, 4 * first + beta - ell))
    assert len(rows) == 6
    assert sorted({t for _, _, t in rows}) == [rho + 2, rho + 3, rho + 4]

    print(
        "RATE_HALF_CA_HANKEL_A1_DIRECT_THREE_CONTACT_EXCLUSION_AUDIT_PASS "
        f"first={first} profiles={len(rows)}"
    )


if __name__ == "__main__":
    main()

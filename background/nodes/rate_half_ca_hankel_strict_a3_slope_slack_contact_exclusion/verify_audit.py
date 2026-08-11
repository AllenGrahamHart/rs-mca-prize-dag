#!/usr/bin/env python3
"""Local pole-length and inequality mutation audit."""


def main():
    profiles = 0
    for delta in range(0, 80):
        ell = delta // 2
        assert 2 * (ell + 1) > delta
        for omitted in range(delta + 1):
            assert 2 * (ell + 1) > omitted
            profiles += 1

    m = 32
    rho = 4 * m - 1
    e = rho // 3
    delta = rho - 3 * e
    h = 4 * (e - m)
    target_second = -e + delta // 2 + h + 2
    assert target_second == 0
    assert -e + delta // 2 + (h - 1) + 2 == -1

    mutated_ell = (delta + 1) // 2
    assert -e + mutated_ell + (h - 1) + 2 == 0

    print(
        "RATE_HALF_CA_HANKEL_STRICT_A3_SLOPE_SLACK_CONTACT_EXCLUSION_AUDIT_PASS "
        f"profiles={profiles} boundary_target={target_second} mutation=detected"
    )


if __name__ == "__main__":
    main()

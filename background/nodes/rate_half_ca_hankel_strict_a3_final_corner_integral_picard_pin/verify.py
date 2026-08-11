#!/usr/bin/env python3
"""Arithmetic replay for the final-corner Picard pin."""


def check(e, d):
    assert e >= 2 and d in (0, 1)
    rho = 3 * e + 1
    n_domain = 4 * rho + 4
    n_slopes = rho + 2
    contact = (-rho - 3, e + 1)
    target = (
        3 * contact[0] + n_domain + d,
        3 * contact[1] - n_slopes,
    )
    assert target == (rho - 5 + d, 0)
    kernel = (target[0] - rho, target[1] - e)
    assert kernel == (-5 + d, -e)
    assert kernel[0] < 0 and kernel[1] < 0
    assert contact[0] * e + contact[1] * rho == 1
    return rho


def main():
    profiles = 0
    for e in range(2, 160):
        for d in (0, 1):
            check(e, d)
            profiles += 1

    official_m = 1 << 37
    official_e = (4 * official_m - 1) // 3
    official_rho = check(official_e, 1)
    profiles += 1

    for e in range(2, 80):
        possible_zero = []
        for e_i in range(1, e + 1):
            for a_i in range(0, 4 * e_i):
                if e * e_i - (e + 1) * a_i == 0:
                    possible_zero.append((e_i, a_i))
        assert not possible_zero

    print(
        "RATE_HALF_CA_HANKEL_STRICT_A3_FINAL_CORNER_INTEGRAL_PICARD_PIN_PASS "
        f"profiles={profiles} official_e={official_e} official_rho={official_rho}"
    )


if __name__ == "__main__":
    main()

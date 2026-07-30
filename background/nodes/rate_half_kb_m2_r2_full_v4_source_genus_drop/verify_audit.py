#!/usr/bin/env python3
"""Audit the V4 conjugation and tame fixed-point arithmetic."""


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[value]] for value in range(4))


def inverse(value: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * 4
    for source, target in enumerate(value):
        result[target] = source
    return tuple(result)


def main() -> None:
    # D8 on the square: a=r^2 is central, eta=s, and c=r conjugates
    # eta to eta*a while fixing a.
    r = (1, 2, 3, 0)
    eta = (0, 3, 2, 1)
    a = compose(r, r)
    eta_a = compose(eta, a)
    c_eta_c_inverse = compose(compose(r, eta), inverse(r))
    c_a_c_inverse = compose(compose(r, a), inverse(r))
    assert c_eta_c_inverse == eta_a
    assert c_a_c_inverse == a
    assert len({(0, 1, 2, 3), eta, a, eta_a}) == 4

    admissible = []
    for genus in range(4):
        n_eta = 2 * genus + 2
        n_eta_a = n_eta
        n_a = 2 * genus + 6 - n_eta - n_eta_a
        if n_a >= 0:
            admissible.append((genus, n_a))
    assert admissible == [(0, 2), (1, 0)]
    print("RATE_HALF_KB_M2_R2_FULL_V4_SOURCE_GENUS_DROP_AUDIT_PASS")


if __name__ == "__main__":
    main()

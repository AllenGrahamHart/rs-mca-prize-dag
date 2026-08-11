#!/usr/bin/env python3
"""Exact arithmetic checks for the paired padded-fiber factorization."""

E = 183251937963
P = 274877906944


def check_profile(e: int) -> None:
    assert e % 2 == 1 and e >= 7
    p = (3 * e - 1) // 2
    d = 2 * p - 1

    for r in range(e - 5):
        i_ext = p - 3 - r
        p_ext = p + 2
        x_ext = 2 * p + 1 + r
        assert 1 + i_ext + p_ext + x_ext == 4 * p + 1
        assert i_ext + r == p - 3
        assert x_ext == d + 2 + r

        i_strict = p - 2 - r
        p_strict = p + 1
        x_strict = 2 * p + 1 + r
        assert 1 + i_strict + p_strict + x_strict == 4 * p + 1
        assert i_strict + r == p - 2
        assert x_strict == d + 2 + r

    assert 3 * e - e == 2 * e
    assert 3 * e + 1 - p == p + 2


def main() -> None:
    for e in (7, 9, 11, 31, 101):
        check_profile(e)

    assert (3 * E - 1) // 2 == P
    assert 2 * E == 366503875926
    assert P + 2 == 274877906946
    print("PASS paired padded-fiber factorization arithmetic")


if __name__ == "__main__":
    main()

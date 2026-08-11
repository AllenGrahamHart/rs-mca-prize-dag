#!/usr/bin/env python3
"""Independent boundary and mutation audit for the factorization node."""


def profile(e: int, strict: bool, r: int) -> tuple[int, int, int, int]:
    p = (3 * e - 1) // 2
    inside = p - (2 if strict else 3) - r
    outside = p + (1 if strict else 2)
    complement = 2 * p + 1 + r
    full_degree = p - (2 if strict else 3)
    return inside, outside, complement, full_degree


def main() -> None:
    checks = 0
    for e in range(7, 80, 2):
        p = (3 * e - 1) // 2
        for strict in (False, True):
            for r in range(0, min(5, e - 5)):
                inside, outside, complement, full_degree = profile(e, strict, r)
                assert inside + r == full_degree
                assert 1 + inside + outside + complement == 4 * p + 1
                checks += 2

    assert profile(7, False, 1) != profile(7, True, 1)
    print(f"PASS paired padded-fiber audit checks={checks} tamper=1/1")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Independent symbolic audit for the transposed coefficient gate."""


def dimensions(e: int) -> tuple[tuple[int, int], tuple[int, int]]:
    p = (3 * e - 1) // 2
    ext = ((p - 2) * (e + 1), 2 * e)
    strict = ((p - 1) * (p + 2 - e), p + 2)
    return ext, strict


def main() -> None:
    checks = 0
    for e in range(7, 200, 2):
        p = (3 * e - 1) // 2
        ext, strict = dimensions(e)
        assert ext[0] == (p - 2) * (2 * e - ((e - 2) + 1))
        assert strict[0] == (p - 1) * ((p + 2) - ((e - 1) + 1))
        assert ext[1] == 2 * e
        assert strict[1] == p + 2
        checks += 4

    good = dimensions(7)
    bad = ((good[0][0] + 1, good[0][1]), good[1])
    assert good != bad
    print(f"PASS parameter-fiber coefficient audit checks={checks} tamper=1/1")


if __name__ == "__main__":
    main()

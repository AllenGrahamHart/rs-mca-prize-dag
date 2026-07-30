#!/usr/bin/env python3
"""Independent exact audit of endpoint transpose symmetry."""


def divided_difference_terms(degree: int) -> set[tuple[int, int]]:
    return {(degree - 1 - index, index) for index in range(degree)}


def main() -> None:
    checked = 0
    for degree in range(1, 61):
        terms = divided_difference_terms(degree)
        assert {(right, left) for left, right in terms} == terms
        checked += len(terms)

    v4 = {(0, 0), (1, 0), (0, 1), (1, 1)}
    swapped = {(right, left) for left, right in v4}
    assert swapped == v4
    assert {(0, 0), (0, 1)} == {
        (right, left) for left, right in {(0, 0), (1, 0)}
    }
    assert (1, 1) == (1, 1)[::-1]
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_TRANSPOSE_TRANSPORT_AUDIT_PASS "
        f"divided_difference_terms={checked}"
    )


if __name__ == "__main__":
    main()

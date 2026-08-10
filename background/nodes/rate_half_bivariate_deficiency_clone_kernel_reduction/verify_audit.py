#!/usr/bin/env python3
"""Independent integer-polynomial audit of clone-column expansion."""


def convolution(left: list[int], right: list[int]) -> list[int]:
    output = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] += a * b
    return output


def shifted(poly: list[int], amount: int) -> list[int]:
    return [0] * amount + poly


def main() -> None:
    m = 5
    points = (1, 3, 5)
    roots_by_point = ((2, 4, 6, 8, 10), (2, 4, 6, 8), (2, 4, 6))
    linears = ((7, 1), (9, 0), (11, 3))
    quotients = ((13,), (15, 17), (19, 21, 23))
    checks = 0

    for moment in range(4 * m + 1):
        direct = [0] * (m + 2)
        expanded = [0] * (m + 2)
        for x, roots, linear, quotient in zip(
            points, roots_by_point, linears, quotients
        ):
            locator = [1]
            for root in roots:
                locator = convolution(locator, [-root, 1])
            base = convolution(list(linear), locator)
            product = convolution(base, list(quotient))
            for degree, value in enumerate(product):
                direct[degree] += value * x**moment
            for quotient_degree, value in enumerate(quotient):
                column = shifted(base, quotient_degree)
                for degree, entry in enumerate(column):
                    expanded[degree] += value * entry * x**moment
        assert direct == expanded
        checks += len(direct)

    deficits = [m - len(roots) for roots in roots_by_point]
    assert deficits == [0, 1, 2]
    assert sum(delta + 1 for delta in deficits) == len(points) + sum(deficits)
    print(
        "RATE_HALF_BIVARIATE_DEFICIENCY_CLONE_KERNEL_REDUCTION_AUDIT_PASS "
        f"coefficient_checks={checks}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Independent audit of the shortened RS extension equations."""


def rank(rows, prime):
    rows = [list(row) for row in rows]
    output = 0
    for column in range(len(rows[0])):
        pivot = next(
            (row for row in range(output, len(rows)) if rows[row][column] % prime),
            None,
        )
        if pivot is None:
            continue
        rows[output], rows[pivot] = rows[pivot], rows[output]
        scale = pow(rows[output][column], prime - 2, prime)
        rows[output] = [value * scale % prime for value in rows[output]]
        for row in range(output + 1, len(rows)):
            factor = rows[row][column]
            if factor:
                rows[row] = [
                    (value - factor * base) % prime
                    for value, base in zip(rows[row], rows[output])
                ]
        output += 1
    return output


def main() -> None:
    prime = 103
    points = list(range(1, 10))
    rho = 4
    checks = []
    for moment in range(len(points) - rho - 1):
        row = []
        for x in points:
            derivative = 1
            for y in points:
                if y != x:
                    derivative = derivative * (x - y) % prime
            row.append(pow(x, moment, prime) * pow(derivative, prime - 2, prime) % prime)
        checks.append(row)
    assert len(checks) == 4 and rank(checks, prime) == 4

    quartic = [(x**4 + 3 * x + 7) % prime for x in points]
    quintic = [(x**5 + 3 * x + 7) % prime for x in points]
    assert all(
        sum(a * b for a, b in zip(row, quartic)) % prime == 0 for row in checks
    )
    assert any(
        sum(a * b for a, b in zip(row, quintic)) % prime for row in checks
    )
    print(
        "RATE_HALF_BIVARIATE_LOCATOR_EXTENSION_KERNEL_REDUCTION_AUDIT_PASS "
        "checks=4 dimension=5"
    )


if __name__ == "__main__":
    main()

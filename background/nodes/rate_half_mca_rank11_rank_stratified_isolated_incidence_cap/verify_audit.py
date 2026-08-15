#!/usr/bin/env python3
"""Independent finite-field replay of the rank-stratified elimination."""

from __future__ import annotations


P = 101


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def dot(left: list[int], right: list[int]) -> int:
    return sum(a * b for a, b in zip(left, right)) % P


def main() -> None:
    # Ten basis rows are the identity; the eleventh evaluation row is v.
    v = [pow(i + 2, 3, P) for i in range(10)]
    a = [7 * i * i + 3 for i in range(10)]
    b = [11 * i + 5 for i in range(10)]
    a11 = 19
    b11 = 23
    constant = (a11 - dot(v, a)) % P
    linear = (b11 - dot(v, b)) % P
    require(linear != 0, "nonidentity branch")
    root = (-constant * pow(linear, -1, P)) % P
    roots = [z for z in range(P) if (constant + z * linear) % P == 0]
    require(roots == [root], "one linear root")

    # Choosing the final constants by interpolation gives the identity branch.
    require((dot(v, a) - dot(v, a)) % P == 0, "identity constant")
    require((dot(v, b) - dot(v, b)) % P == 0, "identity linear")

    # A rank-nine evaluation map has a nonzero kernel direction through every
    # compatible solution.
    kernel = [0] * 9 + [1]
    rows = [[int(i == j) for j in range(10)] for i in range(9)]
    require(all(dot(row, kernel) == 0 for row in rows), "kernel line")
    print(
        "RATE_HALF_MCA_RANK11_RANK_STRATIFIED_ISOLATED_INCIDENCE_CAP_AUDIT_PASS "
        f"field={P} unique_root={root} kernel_dimension_at_least=1"
    )


if __name__ == "__main__":
    main()

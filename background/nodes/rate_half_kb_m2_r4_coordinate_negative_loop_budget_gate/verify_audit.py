#!/usr/bin/env python3
"""Independent audit of the negative loop root count."""


P = 29
K = (1, 28, 4, 25, 9)


def evaluate(poly: tuple[int, int, int], value: int) -> int:
    return sum(coefficient * pow(value, degree, P) for degree, coefficient in enumerate(poly)) % P


def main() -> None:
    # A nonzero quadratic cannot vanish at the first three distinct K values.
    vandermonde = 1
    for i in range(3):
        for j in range(i + 1, 3):
            vandermonde = vandermonde * (K[j] - K[i]) % P
    if vandermonde == 0:
        raise RuntimeError("distinct loop fibers")

    pinned = (K[0] * K[1] % P, -(K[0] + K[1]) % P, 1)
    if evaluate(pinned, K[0]) or evaluate(pinned, K[1]):
        raise RuntimeError("two-loop factor pin")
    if evaluate(pinned, K[2]) == 0:
        raise RuntimeError("spurious third root")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_LOOP_BUDGET_AUDIT_PASS "
        f"vandermonde={vandermonde} two_loop_pin={pinned}"
    )


if __name__ == "__main__":
    main()

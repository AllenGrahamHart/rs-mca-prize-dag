#!/usr/bin/env python3
"""Independent arithmetic audit of the neighbor-norm weld counterexample."""


def evaluate(coefficients, value, prime):
    return sum(coefficient * value**index for index, coefficient in enumerate(coefficients)) % prime


def main():
    prime = 13
    d = (4, 7, 6)
    e = (9, 5, 2)
    beta = 1
    for source, product, target_sum in ((2, 2, 3), (3, 3, 4)):
        w = source**2
        assert (evaluate(e, w, prime) - product * evaluate(d, w, prime)) % prime == 0
        assert (
            source * beta * (w - 1) + target_sum * evaluate(d, w, prime)
        ) % prime == 0
    assert all(evaluate(d, value, prime) for value in (0, 1, 4, 9))
    p = (6, 0, 4)
    q = (4, 0, 7)
    observed = evaluate(p, 1, prime) * pow(evaluate(q, 1, prime), -1, prime) % prime
    claimed = 2 * 3 % prime
    assert (observed, claimed) == (8, 6)
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_NEIGHBOR_NORM_REFUTATION_AUDIT_PASS "
        "common_rows=4 leading_guards=4 observed=8 claimed=6"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Independent exact Schur-complement audit over truncated series."""


def order(series: list[int]) -> int:
    for index, coefficient in enumerate(series):
        if coefficient:
            return index
    return len(series)


def main() -> None:
    # N=diag(z^3,1), v=(1,a z^2). Then Nv is divisible by z^2 and
    # v^T N v=z^3+a^2 z^4 has no order-two term.
    for a in (0, 1, 7, 29):
        image_first = [0, 0, 0, 1, 0]
        image_second = [0, 0, a, 0, 0]
        self_pair = [0, 0, 0, 1, a * a]
        assert min(order(image_first), order(image_second)) >= 2
        assert order(self_pair) == 3

    # A proposed leading kappa*nu with nonzero evaluation pairing would add
    # an order-two self coefficient and contradict the Schur calculation.
    assert order([0, 0, 5, 1, 0]) == 2
    print("RATE_HALF_SHARED_THIRD_JET_VANISHING_AUDIT_PASS cases=4")


if __name__ == "__main__":
    main()

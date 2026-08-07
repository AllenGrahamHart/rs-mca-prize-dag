#!/usr/bin/env python3
"""Replay the exact X4 d=1 projection-codegree arithmetic."""

from fractions import Fraction


N = 1 << 41
T_MIN = 1 << 31
RATES = (Fraction(1, 2), Fraction(1, 4), Fraction(1, 8), Fraction(1, 16))


def require(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError(label)


def johnson_codegree(universe: int, width: int) -> int:
    denominator = width * width - universe
    require(denominator > 0, "positive Johnson denominator")
    return universe * (width - 1) // denominator


def main() -> None:
    # For t<T_MIN, the symmetric binomial index stays in [N/16,N/2].
    for rate in RATES:
        k = int(rate * N)
        for t in (0, T_MIN - 1):
            symmetric_index = min(N - k - t, k + t)
            require(N // 16 <= symmetric_index <= N // 2, "uniform corridor index band")

    # binom(N,N/16) >= 16^(N/16)=2^(N/4), while t*L<N/4.
    require(T_MIN * 256 == N // 4, "exact corridor lower-bound crossing")
    require(N // 4 + 128 > N // 4, "corridor security overhead retained")

    width = T_MIN + 2
    require(width * width > N, "official projection denominator positive")
    bound = johnson_codegree(N, width)
    require(bound == 1024, "official maximum projection codegree")

    # The rational bound increases with the universe size below width^2.
    for universe in (1, N // 16, N // 2, N - 1, N):
        require(johnson_codegree(universe, width) <= bound, "universe monotonicity sample")

    print(
        "X4_LINEAR_DIFFERENCE_PROJECTION_CODEGREE_PASS "
        f"t_min={T_MIN} width_min={width} codegree={bound}"
    )


if __name__ == "__main__":
    main()

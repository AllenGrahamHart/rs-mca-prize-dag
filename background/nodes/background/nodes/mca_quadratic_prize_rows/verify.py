#!/usr/bin/env python3
"""Replay the quadratic MCA theorem arithmetic and four prize rows."""

from __future__ import annotations

from itertools import product


TARGET_DENOMINATOR = 1 << 128
K = 1 << 40

ROWS = (
    (
        "r1_2",
        1,
        2,
        41,
        132540169958804033333249306710494641010898987122689,
        389500552609,
        92,
        26766274163673319604503,
        3,
        5154112775168,
        -663955886271,
    ),
    (
        "r1_4",
        1,
        4,
        42,
        411940680852499481698306614369841346700408394874881,
        1210584858040,
        93,
        41595378994516821279015,
        13,
        7590647904465,
        -3182321912768,
    ),
    (
        "r1_8",
        1,
        8,
        43,
        979947269755402568812854322316630667196565607677953,
        2879806199253,
        95,
        24737346889219389259839,
        5,
        13908181940112,
        -6720484728007,
    ),
    (
        "r1_16",
        1,
        16,
        44,
        2121285573237585848299875619011192262679065433997313,
        6233898019554,
        97,
        13387194060291799253121,
        5,
        19335616403905,
        -20973145690236,
    ),
)


def quadratic_margin(n: int, k: int, radius: int) -> int:
    return radius * radius - n * (3 * radius - (n - k))


def verify_proof_arithmetic() -> int:
    checked = 0
    for n in range(2, 81):
        for k in range(1, n):
            redundancy = n - k
            for radius in range(redundancy):
                if quadratic_margin(n, k, radius) < 0:
                    continue
                checked += 1
                agreement = n - radius
                if agreement * agreement < n * (k + radius):
                    raise AssertionError((n, k, radius, "equivalence"))
                if 3 * radius <= redundancy:
                    continue
                count = radius + 2
                lower_twice_n = (
                    count * count * agreement * agreement
                    - count * agreement * n
                )
                upper_twice_n = (
                    n * count * (count - 1) * (k + radius - 1)
                )
                if lower_twice_n <= upper_twice_n:
                    raise AssertionError((n, k, radius, "overlap gap"))
                for common in range(k + radius, n + 1):
                    cancellations = max(1, agreement - common)
                    if (n - common) // cancellations > radius + 1:
                        raise AssertionError(
                            (n, k, radius, common, "collapse")
                        )
    return checked


def span(vectors: tuple[tuple[int, ...], ...], prime: int) -> set[tuple[int, ...]]:
    if not vectors:
        return {(0,) * 3}
    return {
        tuple(
            sum(coefficient * vector[j] for coefficient, vector in zip(coeffs, vectors))
            % prime
            for j in range(3)
        )
        for coeffs in product(range(prime), repeat=len(vectors))
    }


def exhaustive_toy() -> tuple[int, int]:
    prime = 5
    columns = tuple((1, x, x * x % prime) for x in range(1, 5))
    syndrome_space = tuple(product(range(prime), repeat=3))
    maximums = []
    for radius in (0, 1):
        support_spans = [span((), prime)]
        if radius:
            support_spans.extend(span((column,), prime) for column in columns)
        maximum = 0
        for y0 in syndrome_space:
            for y1 in syndrome_space:
                bad = 0
                for slope in range(prime):
                    point = tuple(
                        (left + slope * right) % prime
                        for left, right in zip(y0, y1)
                    )
                    if any(
                        point in space
                        and not (y0 in space and y1 in space)
                        for space in support_spans
                    ):
                        bad += 1
                maximum = max(maximum, bad)
        expected = radius + 1
        if maximum != expected:
            raise AssertionError((radius, maximum, expected))
        maximums.append(maximum)
    return tuple(maximums)


def verify_rows() -> list[str]:
    summaries = []
    for (
        name,
        rate_numerator,
        rate_denominator,
        length_exponent,
        prime,
        budget,
        proth_exponent,
        proth_odd,
        witness,
        expected_before,
        expected_at,
    ) in ROWS:
        n = 1 << length_exponent
        if K * rate_denominator != n * rate_numerator:
            raise AssertionError((name, "rate"))
        if prime != proth_odd * (1 << proth_exponent) + 1:
            raise AssertionError((name, "Proth decomposition"))
        if not proth_odd & 1 or proth_odd >= 1 << proth_exponent:
            raise AssertionError((name, "Proth shape"))
        if pow(witness, (prime - 1) // 2, prime) != prime - 1:
            raise AssertionError((name, "Proth witness"))
        if prime >= 1 << 256 or (prime - 1) % n:
            raise AssertionError((name, "field/domain"))

        quotient, remainder = divmod(prime, TARGET_DENOMINATOR)
        if quotient != budget or not 0 < remainder < TARGET_DENOMINATOR:
            raise AssertionError((name, "target budget"))

        redundancy = n - K
        if not 1 <= budget <= redundancy - 1:
            raise AssertionError((name, "radius scope"))
        before = quadratic_margin(n, K, budget - 1)
        at = quadratic_margin(n, K, budget)
        if (before, at) != (expected_before, expected_at):
            raise AssertionError((name, before, at))
        if not before >= 0 > at:
            raise AssertionError((name, "adjacent signs"))
        if quadratic_margin(n, K, budget - 2) < before:
            raise AssertionError((name, "monotonic margin"))

        summaries.append(
            f"{name}:n=2^{length_exponent},pbits={prime.bit_length()},"
            f"B={budget},grid=({budget}-1)/n,sup={budget}/n"
        )
    return summaries


def mutation_controls() -> None:
    name, _, _, exponent, prime, budget, s, odd, witness, _, _ = ROWS[0]
    n = 1 << exponent
    caught = 0
    caught += prime + 2 != odd * (1 << s) + 1
    caught += pow(witness, (prime - 1) // 2, prime) != prime - 2
    caught += quadratic_margin(n, K, budget) < 0
    if caught != 3:
        raise AssertionError((name, "mutation controls", caught))


def main() -> None:
    proof_rows = verify_proof_arithmetic()
    toy = exhaustive_toy()
    rows = verify_rows()
    mutation_controls()
    print(
        "MCA_QUADRATIC_PRIZE_ROWS_PASS "
        f"proof_rows={proof_rows} toy_max={toy} " + " ".join(rows)
    )


if __name__ == "__main__":
    main()

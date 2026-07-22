#!/usr/bin/env python3
"""Independent structural audit of the cyclic rate-half list floor."""

from __future__ import annotations

from itertools import combinations
from math import comb, log2


def audit_support_map() -> int:
    checks = 0
    for quotient_size in range(4, 66, 2):
        half = quotient_size // 2
        for d in range(1, half):
            m = half + d
            source_to_index: dict[int, int] = {}
            for j in range(m + 1):
                index = quotient_size - d + j
                if index >= quotient_size:
                    index -= quotient_size
                source_to_index[j] = index

            high_sources = {j for j, index in source_to_index.items() if index >= half}
            assert high_sources == set(range(d)) | {m}
            assert source_to_index[m] == half
            assert max(quotient_size - d + j for j in range(m + 1)) < 2 * quotient_size

            for c in (2, 3, 5):
                k = half * c
                for s in range(1, c):
                    for index in range(quotient_size):
                        block_is_high = index * c >= k
                        assert block_is_high == (index >= half)
                        if index < half:
                            assert index * c + s < k
                    checks += 1
    return checks


def audit_constant_terms() -> int:
    checks = 0
    for quotient_size in range(4, 15, 2):
        half = quotient_size // 2
        for d in range(1, half):
            m = half + d
            # Elements of a multiplicative coset are represented by exponents
            # modulo N. A product is addition of exponents plus one fixed shift.
            values = {
                sum(chosen) % quotient_size
                for chosen in combinations(range(1, quotient_size), m)
            }
            assert len(values) <= quotient_size
            checks += 1
    return checks


def log2_bigint(value: int) -> float:
    bits = value.bit_length()
    shift = max(0, bits - 200)
    return shift + log2(value >> shift)


def audit_historical_cap() -> tuple[float, float]:
    quotient_size = 1 << 19
    d = 2048
    m = (quotient_size // 2) + d
    count = comb(quotient_size - 1, m)
    q_bits = 256

    left = count << 128
    new_right = quotient_size << (q_bits * d)
    old_right = 1 << (q_bits * (d + 1))
    assert left > new_right
    assert left < old_right

    margin = 128 + log2_bigint(count) - log2(quotient_size) - q_bits * d
    boundary = (128 + log2_bigint(count) - log2(quotient_size)) / d
    assert 75.079 < margin < 75.080
    assert 256.036 < boundary < 256.037
    return margin, boundary


def audit_optimized_cap() -> tuple[float, float, int, int, int]:
    n = 1 << 41
    k = 1 << 40
    c = 1 << 33
    quotient_size = n // c
    d = 1
    s = c - 1
    m = quotient_size // 2 + d
    agreement = k + d * c + s
    errors = n - agreement
    count = comb(quotient_size - 1, m)
    lower = -(-count // quotient_size)

    assert (quotient_size, m) == (256, 129)
    assert agreement == 1_116_691_496_959
    assert errors == 1_082_331_758_593
    assert lower == (
        11092230961998080258863221315535829014398723445840079610908300691051869570
    )
    assert agreement * agreement < n * (k - 1)
    johnson_gap = n * (k - 1) - agreement * agreement
    assert johnson_gap > 0
    assert lower > 1 << 238
    assert ((1 << 256) - 1) < lower << 128

    margin = 128 + log2_bigint(count) - log2(quotient_size) - 256 * d
    boundary = (128 + log2_bigint(count) - log2(quotient_size)) / d
    assert 114.650 < margin < 114.651
    assert 370.650 < boundary < 370.651

    # Replay the entropy-upper-bound exclusion used for maximal-prefix
    # instances under the same q=2^256 cap criterion.
    extremality_checks = 0
    for exponent in range(1, 42):
        size = 1 << exponent
        if size <= 128:
            assert exponent + 256 >= size + 127
            extremality_checks += 1
            continue
        first_better_d = size // 128
        assert exponent + 256 * first_better_d >= size + 127
        extremality_checks += 1
        if size >= 512:
            tie_d = size // 128 - 1
            assert exponent + 256 * tie_d >= size + 127
            extremality_checks += 1
    assert extremality_checks == 74
    return margin, boundary, lower.bit_length(), johnson_gap, extremality_checks


def main() -> None:
    support_checks = audit_support_map()
    constant_checks = audit_constant_terms()
    old_margin, old_boundary = audit_historical_cap()
    margin, boundary, list_bits, johnson_gap, extremality = audit_optimized_cap()
    print(
        "AUDIT_RATE_HALF_CYCLIC_ROTATED_PREFIX_FLOOR_PASS "
        f"support_checks={support_checks} constant_checks={constant_checks} "
        f"historical_margin_bits={old_margin:.9f} "
        f"historical_q_boundary_bits={old_boundary:.12f} "
        f"optimized_margin_bits={margin:.9f} "
        f"optimized_q_boundary_bits={boundary:.12f} "
        f"list_bits={list_bits} johnson_gap={johnson_gap} "
        f"extremality_checks={extremality}"
    )


if __name__ == "__main__":
    main()

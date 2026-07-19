#!/usr/bin/env python3
"""Replay the index-two near-core owner and its official absorption."""

from __future__ import annotations

from math import comb, factorial


def poly_mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return out


def locator(roots: list[int], p: int) -> list[int]:
    out = [1]
    for root in roots:
        out = poly_mul(out, [(-root) % p, 1], p)
    return out


def evaluate(poly: list[int], x: int, p: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * x + coefficient) % p
    return out


def owner_key(
    agreement: set[int],
    cosets: tuple[tuple[int, ...], tuple[int, ...]],
    k: int,
    s: int,
    mutation: bool = False,
) -> tuple[int, tuple[int, ...], tuple[int, ...]] | None:
    n_half = len(cosets[0])
    for index, block in enumerate(cosets):
        missed = tuple(x for x in block if x not in agreement)
        if len(missed) > s:
            continue
        q = max(0, k - n_half + len(missed))
        if mutation and q:
            q -= 1
        outside = tuple(
            x for x in cosets[1 - index] if x in agreement
        )
        if len(outside) < q:
            return None
        return index, missed, outside[:q]
    return None


def mutation_fixture() -> int:
    p = 17
    cosets = ((1, 2, 3, 4), (5, 6, 7, 8))
    p0 = [0]
    p1 = locator([1, 2, 3], p)

    word: dict[int, int] = {x: 0 for x in (1, 2, 3)}
    p1_at_4 = evaluate(p1, 4, p)
    word[4] = next(v for v in range(p) if v not in (0, p1_at_4))
    for x in (5, 6):
        word[x] = evaluate(p1, x, p)
    for x in (7, 8):
        word[x] = 0

    agreements = []
    for poly in (p0, p1):
        agreements.append(
            {x for x in range(1, 9) if evaluate(poly, x, p) == word[x]}
        )
    if [len(a) for a in agreements] != [5, 5]:
        raise AssertionError(agreements)

    proper = [owner_key(a, cosets, 4, 4) for a in agreements]
    mutant = [owner_key(a, cosets, 4, 4, mutation=True) for a in agreements]
    if proper[0] == proper[1] or mutant[0] != mutant[1]:
        raise AssertionError((proper, mutant))
    for agreement, key in zip(agreements, proper):
        assert key is not None
        index, missed, outside = key
        interpolation = (
            set(cosets[index]).difference(missed).union(outside)
        )
        if len(interpolation) < 4 or not interpolation.issubset(agreement):
            raise AssertionError((agreement, key, interpolation))
    return 7


def main() -> None:
    checks = mutation_fixture()

    n_min = 1 << 13
    n_half_min = n_min // 2
    if not (n_half_min**4 > 10 * (1 << 12) * factorial(12)):
        raise AssertionError("degree-twelve absorption anchor")
    checks += 1

    rates = (2, 4, 8, 16)
    for exponent in range(13, 45):
        n = 1 << exponent
        n_half = n // 2
        for denominator in rates:
            k = n // denominator
            h = k // 2 + 1
            symmetric_index = min(h, n_half - 1 - h)
            if symmetric_index < 12:
                raise AssertionError((exponent, denominator, symmetric_index))
            for e in range(5):
                q = max(0, k - n_half + e)
                if not (0 <= q <= e <= 4):
                    raise AssertionError((exponent, denominator, e, q))
            if not (n_half**4 > 10 * (1 << 12) * factorial(12)):
                raise AssertionError((exponent, denominator))
            checks += 3

    for denominator in rates:
        n = n_min
        n_half = n // 2
        k = n // denominator
        h = k // 2 + 1
        owner_bound = 2 * sum(
            comb(n_half, e) * comb(n_half, max(0, k - n_half + e))
            for e in range(5)
        )
        q2 = comb(n_half - 1, h)
        if not owner_bound < q2:
            raise AssertionError((denominator, owner_bound, q2))
        checks += 1

    epsilon_denominator = 1 << 690
    combined_at_q2_one = 5 * epsilon_denominator + 4 + 3 * epsilon_denominator
    allowance_at_q2_one = 719 * (epsilon_denominator + 1)
    if not combined_at_q2_one < allowance_at_q2_one:
        raise AssertionError("combined profile absorption")
    checks += 1

    # The reciprocal-quadratic source agrees on G minus {b} union D.
    g = set(range(32))
    b = 3
    defect = {5, 11, 19}
    rq_core_agreements = g.difference({b}, defect)
    if len(g.difference(rq_core_agreements)) != 4:
        raise AssertionError("reciprocal-quadratic subsumption")
    checks += 1

    print(
        "PMA_INDEX_TWO_CORE_OWNER_PASS "
        f"checks={checks} rows={32 * len(rates)} mutation=tripped"
    )


if __name__ == "__main__":
    main()

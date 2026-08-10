#!/usr/bin/env python3
"""Independent direct-PF6 audit of the official shortening prefixes."""

from functools import lru_cache
from math import comb


FIELD_CAP = (1 << 256) - 1
SCALE = 1 << 128
G8 = 195112047344632914122867933361797765038
G16 = 2444555448501019158442942184801171570


def direct_pf6(rate_den: int, source_scale: int, touched: int) -> list[int]:
    code_length = 8192 // rate_den
    core = code_length - 1
    ell, background = divmod(
        (rate_den - 1) * code_length + 1, source_scale
    )
    support = touched * ell
    if support > core:
        return []

    answer = []
    for defect in range(core + 1):
        rank = 2 * defect - support
        u = defect - (touched - 1) * ell
        if defect >= ell * (source_scale - 2):
            continue
        if rank < 0 or u > background:
            continue
        if 2 * defect > core + (touched - 2) * ell + background:
            continue
        if defect * defect > core * rank:
            continue
        joint = (
            background * defect * defect
            + core * u * u
            - core * background * rank
        )
        if u >= 0 and background > 0 and joint > 0:
            continue
        answer.append(defect)
    return answer


@lru_cache(maxsize=None)
def direct_cap(length: int, weight: int, half_distance: int) -> tuple[int, int]:
    best = comb(length, weight)
    owner_depth = -1
    choose_length = 1
    choose_weight = 1
    for depth in range(weight + 1):
        residual = weight - depth
        if residual < half_distance:
            terminal = 1
        else:
            denominator = residual**2 - (length - depth) * (
                residual - half_distance
            )
            terminal = (
                None
                if denominator <= 0
                else (length - depth) * half_distance // denominator
            )
        if terminal is not None:
            candidate = choose_length * terminal // choose_weight
            if candidate < best:
                best = candidate
                owner_depth = depth
        if depth != weight:
            choose_length = choose_length * (length - depth) // (depth + 1)
            choose_weight = choose_weight * (weight - depth) // (depth + 1)
    return best, owner_depth


def direct_scale(rate_den: int, source_scale: int) -> tuple[int, int, int]:
    code_length = 8192 // rate_den
    core = code_length - 1
    ell, background = divmod(
        (rate_den - 1) * code_length + 1, source_scale
    )
    total = 0
    cell_count = 0
    group_count = 0
    for touched in range(2, source_scale + 1):
        defects = direct_pf6(rate_den, source_scale, touched)
        if not defects:
            continue
        subtotal = 0
        for defect in defects:
            u = defect - (touched - 1) * ell
            endpoint = touched * ell if u < 0 else defect + ell
            support_weight = min(defect, core - defect)
            cap, _ = direct_cap(core, support_weight, endpoint - defect)
            subtotal += (1 if u < 0 else comb(background, u)) * cap
        total += comb(source_scale, touched) * subtotal + source_scale
        cell_count += len(defects)
        group_count += 1
    return total, cell_count, group_count


def main() -> None:
    rate8 = tuple(direct_scale(8, scale) for scale in range(29, 33))
    rate16 = tuple(direct_scale(16, scale) for scale in range(57, 68))
    assert sum(row[0] for row in rate8) == G8
    assert sum(row[1] for row in rate8) == 126
    assert sum(row[2] for row in rate8) == 5
    assert sum(row[0] for row in rate16) == G16
    assert sum(row[1] for row in rate16) == 374
    assert sum(row[2] for row in rate16) == 12
    assert SCALE * G8 <= FIELD_CAP
    assert SCALE * G16 <= FIELD_CAP

    blocked = ((2, 5), (4, 13), (8, 33), (16, 68))
    for rate_den, source_scale in blocked:
        value, cells, _ = direct_scale(rate_den, source_scale)
        assert cells > 0
        assert value > FIELD_CAP // SCALE

    # A one-unit distance mutation changes the M=61 certificate.
    assert direct_cap(511, 225, 124) != direct_cap(511, 225, 125)

    print(
        "L1_FPC5_GRS_SHORTENING_OFFICIAL_PREFIX_PAYMENT_AUDIT_PASS "
        "prefixes=2 blocked_scales=4 mutation_controls=1"
    )


if __name__ == "__main__":
    main()

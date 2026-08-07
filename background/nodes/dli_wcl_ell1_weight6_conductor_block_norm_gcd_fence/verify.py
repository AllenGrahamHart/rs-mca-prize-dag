#!/usr/bin/env python3
"""Verify the WCL conductor and Heron block-norm gcd fence."""

from __future__ import annotations

import itertools
import math


def canonical(signs: tuple[int, ...]) -> tuple[int, ...]:
    return signs if signs[0] == 1 else tuple(-value for value in signs)


CLASSES = tuple(
    (1,) + tail for tail in itertools.product((-1, 1), repeat=5)
)


def sigma(signs: tuple[int, ...], parity: tuple[int, ...]) -> tuple[int, ...]:
    return canonical(tuple(s * (-1 if bit else 1) for s, bit in zip(signs, parity)))


def blocks(pairing: tuple[tuple[int, int], ...]):
    answer: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
    for signs in CLASSES:
        internal = tuple(signs[b] * signs[a] for a, b in pairing)
        answer.setdefault(internal, set()).add(signs)
    assert sorted(map(len, answer.values())) == [4] * 8
    return answer


def adapted_pairing(parity: tuple[int, ...]):
    even = [index for index, bit in enumerate(parity) if bit == 0]
    odd = [index for index, bit in enumerate(parity) if bit == 1]
    pairs: list[tuple[int, int]] = []
    if sum(parity) % 2:
        mixed = (even.pop(), odd.pop())
    else:
        mixed = None
    for group in (even, odd):
        pairs.extend((group[index], group[index + 1]) for index in range(0, len(group), 2))
    if mixed is not None:
        pairs.append(mixed)
    return tuple(sorted(tuple(sorted(pair)) for pair in pairs))


def orbit_representatives(values, parity):
    remaining = set(values)
    reps = []
    while remaining:
        value = min(remaining)
        mate = sigma(value, parity)
        assert mate != value
        assert mate in remaining
        remaining.remove(value)
        remaining.remove(mate)
        reps.append(value)
    return reps


def conductor_depth(values: tuple[int, ...], modulus: int) -> int:
    depth = 0
    while modulus % (2 ** (depth + 1)) == 0:
        residues = {value % (2 ** (depth + 1)) for value in values}
        if len(residues) != 1:
            break
        depth += 1
    return depth


def check_conductor_sets():
    checked = 0
    for values in itertools.combinations(range(16), 6):
        depth = conductor_depth(values, 16)
        base = values[0] % (2**depth)
        reduced = tuple(((value - base) // (2**depth)) % (16 // (2**depth)) for value in values)
        assert len(set(reduced)) == 6
        assert len({value & 1 for value in reduced}) == 2
        assert depth <= 1  # six distinct values cannot fit in one mod-4 coset of Z/16.
        checked += 1
    assert checked == math.comb(16, 6)
    return checked


def main():
    patterns = 0
    even_blocks = 0
    odd_blocks = 0
    owned_norm_factors = 0
    for parity in itertools.product((0, 1), repeat=6):
        if len(set(parity)) == 1:
            continue
        pairing = adapted_pairing(parity)
        partition = blocks(pairing)
        if sum(parity) % 2 == 0:
            for block in partition.values():
                assert {sigma(value, parity) for value in block} == block
                reps = orbit_representatives(block, parity)
                assert len(reps) == 2
                owned_norm_factors += len(reps)
                even_blocks += 1
        else:
            seen = set()
            for key, block in partition.items():
                if key in seen:
                    continue
                image = {sigma(value, parity) for value in block}
                mate = next(other for other, candidate in partition.items() if candidate == image)
                assert mate != key
                union = block | partition[mate]
                reps = orbit_representatives(union, parity)
                assert len(union) == 8 and len(reps) == 4
                owned_norm_factors += len(reps)
                seen.update((key, mate))
                odd_blocks += 1
        patterns += 1

    assert patterns == 62
    assert even_blocks == 30 * 8
    assert odd_blocks == 32 * 4
    assert owned_norm_factors == even_blocks * 2 + odd_blocks * 4
    conductor_sets = check_conductor_sets()
    print(
        "DLI_WCL_ELL1_WEIGHT6_CONDUCTOR_BLOCK_GCD_FENCE_PASS "
        f"mixed_patterns={patterns} even_blocks={even_blocks} "
        f"odd_blocks={odd_blocks} owned_norm_factors={owned_norm_factors} "
        f"conductor_sets={conductor_sets}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Independent combinatorial audit of the WCL block-norm route fence."""

from __future__ import annotations

import itertools
import random


def normalized(bits):
    bits = tuple(bits)
    return bits if bits[0] == 0 else tuple(bit ^ 1 for bit in bits)


SIGN_CLASSES = tuple((0,) + tail for tail in itertools.product((0, 1), repeat=5))


def involution(sign_class, parity):
    return normalized(a ^ b for a, b in zip(sign_class, parity))


def all_pairings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first = items[0]
    for index in range(1, len(items)):
        second = items[index]
        rest = items[1:index] + items[index + 1 :]
        for tail in all_pairings(rest):
            yield ((first, second),) + tail


PAIRINGS = tuple(all_pairings(range(6)))
assert len(PAIRINGS) == 15


def block_map(pairing):
    groups = {}
    for sign_class in SIGN_CLASSES:
        tag = tuple(sign_class[a] ^ sign_class[b] for a, b in pairing)
        groups[tag] = groups.get(tag, frozenset()) | {sign_class}
    return groups


def pairing_is_adapted(pairing, parity):
    mixed = sum(parity[a] ^ parity[b] for a, b in pairing)
    return mixed == (sum(parity) & 1)


def depth_and_reduction(values):
    depth = 0
    while depth < 8 and len({value % (1 << (depth + 1)) for value in values}) == 1:
        depth += 1
    residue = values[0] % (1 << depth)
    reduced = tuple(((value - residue) // (1 << depth)) % (256 >> depth) for value in values)
    return depth, reduced


def main():
    block_maps = {pairing: block_map(pairing) for pairing in PAIRINGS}
    audited_pairings = 0
    isolated_intersections = 0
    for parity in itertools.product((0, 1), repeat=6):
        if len(set(parity)) == 1:
            continue
        adapted = [pairing for pairing in PAIRINGS if pairing_is_adapted(pairing, parity)]
        assert adapted
        orbit = {SIGN_CLASSES[0], involution(SIGN_CLASSES[0], parity)}
        containing_blocks = []
        for pairing in adapted:
            groups = block_maps[pairing]
            if sum(parity) % 2 == 0:
                block = next(group for group in groups.values() if SIGN_CLASSES[0] in group)
                assert {involution(value, parity) for value in block} == set(block)
                assert len(block) == 4
            else:
                raw = next(group for group in groups.values() if SIGN_CLASSES[0] in group)
                image = frozenset(involution(value, parity) for value in raw)
                block = raw | image
                assert len(block) == 8
            assert orbit <= set(block)
            containing_blocks.append(set(block))
            audited_pairings += 1
        for left, right in itertools.combinations(containing_blocks, 2):
            if left & right == orbit:
                isolated_intersections += 1

    # The set intersection can isolate one conjugacy orbit, but its formal
    # block norms both contain the orbit's complete norm variable N_0.
    assert isolated_intersections > 0

    rng = random.Random(0xCB16)
    conductor_samples = 0
    for _ in range(4096):
        values = tuple(sorted(rng.sample(range(256), 6)))
        depth, reduced = depth_and_reduction(values)
        assert depth <= 5
        assert len(set(reduced)) == 6
        assert len({value & 1 for value in reduced}) == 2
        conductor_samples += 1

    print(
        "DLI_WCL_ELL1_WEIGHT6_CONDUCTOR_BLOCK_GCD_FENCE_AUDIT_PASS "
        f"pairings=15 audited_pairings={audited_pairings} "
        f"isolated_intersections={isolated_intersections} "
        f"conductor_samples={conductor_samples}"
    )


if __name__ == "__main__":
    main()

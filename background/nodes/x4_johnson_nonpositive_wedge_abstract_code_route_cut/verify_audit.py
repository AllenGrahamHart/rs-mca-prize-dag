#!/usr/bin/env python3
"""Independent finite audit of the bipartite binary-word construction."""

from itertools import product


def changed_set(word):
    half = len(word) // 2
    q = {("q", i, bit) for i, bit in enumerate(word[:half])}
    p = {("p", i, bit) for i, bit in enumerate(word[half:])}
    return p, q, p | q


def hamming(left, right):
    return sum(a != b for a, b in zip(left, right))


def main() -> None:
    # Even-parity length-eight code: 128 words, minimum distance two.
    code = [word for word in product((0, 1), repeat=8) if sum(word) % 2 == 0]
    assert len(code) == 128
    blocks = [changed_set(word) for word in code]
    for p, q, block in blocks:
        assert len(p) == len(q) == 4 and len(block) == 8
    for i, left in enumerate(code):
        for j in range(i + 1, len(code)):
            distance = hamming(left, code[j])
            assert distance >= 2
            assert len(blocks[i][2] & blocks[j][2]) == 8 - distance

    n = 1 << 41
    assert 25 * (n // 4) // 32 - 35 > 127
    print(
        "X4_JOHNSON_NONPOSITIVE_ABSTRACT_CODE_ROUTE_CUT_AUDIT_PASS "
        "small_code=128 min_distance=2"
    )


if __name__ == "__main__":
    main()

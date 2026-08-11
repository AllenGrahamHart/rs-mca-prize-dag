#!/usr/bin/env python3
"""Replay the cyclic design and bounded triple-expander probe."""


def build(e):
    rho = 3 * e - 1
    block_count = 3 * e + 3
    marked = {
        j
        for j in range(block_count)
        if ((j + 1) * 7) // block_count > (j * 7) // block_count
    }
    assert len(marked) == 7

    starts = []
    for j in range(block_count):
        starts.extend([j] * (2 if j in marked else 3))
    assert len(starts) == 3 * rho + 5

    blocks = []
    deficient = []
    for t in range(block_count):
        mask = 0
        for i, start in enumerate(starts):
            if (t - start) % block_count < e:
                mask |= 1 << i
        mark_count = sum((t - j) % block_count < e for j in marked)
        assert mark_count in (2, 3)
        is_deficient = mark_count == 3
        if is_deficient:
            mask |= 1 << len(starts)
        mask |= 1 << (len(starts) + 1)
        assert mask.bit_count() == rho
        blocks.append(mask)
        deficient.append(is_deficient)

    assert sum(deficient) == e - 6
    degrees = [sum((block >> i) & 1 for block in blocks) for i in range(len(starts))]
    assert set(degrees) == {e}
    return blocks, deficient


for e in range(7, 61):
    build(e)

# Bounded evidence only: replay the triple-expander test on toy rows.
for e in range(7, 31):
    blocks, deficient = build(e)
    rho = 3 * e - 1
    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            pair = blocks[i] | blocks[j]
            expanders = sum(
                (pair | blocks[k]).bit_count() >= 2 * rho + 1
                for k in range(len(blocks))
                if k not in (i, j)
            )
            assert expanders >= 3 + deficient[i] + deficient[j]

print(
    "QUADRATIC_GAP_FOUR_ABSTRACT_INCIDENCE_DESIGN_PASS",
    "symbolic_rows=7..60",
    "spread_probe=7..30",
)

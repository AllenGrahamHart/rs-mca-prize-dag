#!/usr/bin/env python3
"""Independent multiplicity-vector and Burnside audit."""

from verify import GROUP_J0, MIXED, MIXED_INDEX, PURE, PURE_INDEX, TAU_PURE, valid


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, length - 1):
            yield (first,) + tail


def expand(weights):
    return tuple(index for index, weight in enumerate(weights) for _ in range(weight))


def action(perm, swap):
    pure_map = tuple(
        PURE_INDEX[tuple(sorted((perm[left], perm[right])))]
        for left, right in PURE
    )
    mixed_map = tuple(
        MIXED_INDEX[(perm[left], right ^ swap)]
        for left, right in MIXED
    )
    return pure_map, mixed_map


def fixed(packet, maps):
    pure_packet, mixed_packet = packet
    pure_map, mixed_map = maps
    return (tuple(sorted(pure_map[index] for index in pure_packet)) == pure_packet
            and tuple(sorted(mixed_map[index] for index in mixed_packet)) == mixed_packet)


def main() -> None:
    universal = []
    source_line = []
    for pure_weights in compositions(4, 6):
        pure_packet = expand(pure_weights)
        for mixed_weights in compositions(4, 8):
            mixed_packet = expand(mixed_weights)
            if valid(pure_packet, mixed_packet):
                universal.append((pure_packet, mixed_packet))
            if valid(pure_packet, mixed_packet, source_line=True):
                source_line.append((pure_packet, mixed_packet))

    actions = [action(perm, swap) for perm in GROUP_J0 for swap in (0, 1)]
    universal_fixed = sum(sum(fixed(packet, maps) for packet in universal)
                          for maps in actions)
    source_line_fixed = sum(sum(fixed(packet, maps) for packet in source_line)
                           for maps in actions)
    assert len(actions) == 16
    assert len(universal) == 1560 and universal_fixed // 16 == 123
    assert len(source_line) == 96 and source_line_fixed // 16 == 12

    # The five source-line pure multisets are derived independently here.
    pure_source = {
        expand(weights)
        for weights in compositions(4, 6)
        if all(weights[index] == weights[TAU_PURE[index]] for index in range(6))
        and all(TAU_PURE[index] != index or weights[index] % 2 == 0
                for index in range(6))
        and sum(weight * (weight - 1) // 2 for weight in weights) <= 1
    }
    assert len(pure_source) == 5
    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_112_SATURATED_DEFECT_CLASSIFIER_AUDIT_PASS "
        "burnside_group=16 universal=1560/123 source_line=96/12 pure_types=5"
    )


if __name__ == "__main__":
    main()

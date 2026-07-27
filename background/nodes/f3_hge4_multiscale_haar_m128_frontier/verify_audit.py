#!/usr/bin/env python3
"""Independent arithmetic audit for the m=128 balanced-factor gate."""

from pathlib import Path


def gate(width: int, mask: int, include_balance: bool = True) -> bool:
    ambient_order = 1 << 13
    exact_order = 128
    half_moment = (width - 1) // 2
    depth = half_moment.bit_length()
    base_weight = exact_order // 4
    scales = tuple(exact_order >> (index + 1) for index in range(depth))
    live = tuple(index for index in range(depth) if mask & (1 << index))
    dead = tuple(index for index in range(depth) if index not in live)
    scale_weights = tuple(scales[index] // 4 for index in live)
    total_weight = base_weight + sum(scale_weights)

    prime_power = width // 2
    for index in live:
        reduced_half = half_moment >> index
        prime_power += (reduced_half + 1) // 2

    evaluated_orders = (exact_order,) + tuple(scales[index] for index in live)
    twos = sum(
        min(order, scales[index]) // 2
        for order in evaluated_orders
        for index in dead
    )
    if include_balance:
        twos += len(evaluated_orders)

    denominator_twos = sum(
        (index + 1) * (scales[index] // 4) for index in live
    )
    lhs = (1 << twos) * ambient_order ** (2 * prime_power)
    lhs *= total_weight**total_weight
    rhs = (1 << denominator_twos) * (4 * width) ** total_weight
    rhs *= base_weight**base_weight
    for weight in scale_weights:
        rhs *= weight**weight
    return lhs >= rhs


def main() -> None:
    for width in range(12, 32):
        depth = ((width - 1) // 2).bit_length()
        assert all(gate(width, mask) for mask in range(1 << depth))

    assert gate(11, 0b011)
    assert not gate(11, 0b011, include_balance=False)
    assert not gate(11, 0b111)
    assert gate(10, 0b001)
    assert not gate(10, 0b011)

    text = Path(__file__).with_name("audit.md").read_text()
    for anchor in ("integer identity", "coprime", "strict contradiction", "sampling"):
        assert anchor in text

    print(
        "F3_HGE4_MULTISCALE_HAAR_M128_FRONTIER_AUDIT_PASS "
        "mutation=balance-factor-required"
    )


if __name__ == "__main__":
    main()

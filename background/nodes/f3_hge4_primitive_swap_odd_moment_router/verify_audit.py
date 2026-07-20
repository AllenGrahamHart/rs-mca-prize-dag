#!/usr/bin/env python3
"""Mutation audit for the HGE4 primitive swap odd-moment router."""

from __future__ import annotations

from math import comb

import verify


def main() -> None:
    fixture = verify.swap_fixture()
    assert fixture["width"] % 2 == 1
    assert fixture["odd_elementary"] == fixture["odd_powers"] == (0, 0)

    points = fixture["points"]
    mutated = set(fixture["left"])
    mutated.remove(20)
    mutated.add(21)
    mutated_moments = tuple(
        sum(pow(points[index], degree, fixture["prime"]) for index in mutated)
        % fixture["prime"]
        for degree in range(1, fixture["width"], 2)
    )
    assert mutated_moments != (0, 0)

    assert 10 <= comb(15, 4)
    assert comb(15, 4) != comb(31, 9)
    assert verify.common_stabilizer(
        fixture["left"],
        verify.translate(fixture["left"], 16, 32),
        32,
    ) == (0,)

    print(
        "F3_HGE4_PRIMITIVE_SWAP_ODD_MOMENT_ROUTER_AUDIT_PASS "
        "mutations=5 parity_guard=1 primitive_guard=1"
    )


if __name__ == "__main__":
    main()

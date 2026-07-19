#!/usr/bin/env python3
"""Consumer-backward audit of the exact rate-half pole trigger."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def main() -> None:
    n, k = 1 << 41, 1 << 40
    q = 1 << 256
    scale = 1 << 22
    old_sigma = 8_592_912_738
    d, tail = 2048, scale - 1
    sigma = d * scale + tail
    quotient_size = n // scale
    m = k // scale + d
    count = comb(quotient_size - 1, m)
    denominator = quotient_size * q ** (d - 1)
    list_size = (count + denominator - 1) // denominator

    assert (sigma, quotient_size, m) == (8_594_128_895, 524_288, 264_192)
    assert 0 < tail < scale
    assert old_sigma + 1 <= sigma

    collision_denominator = q - n + k * list_size
    bad_slopes = (
        list_size * (q - n) + collision_denominator - 1
    ) // collision_denominator
    prize_numerator = q >> 128
    assert bad_slopes > prize_numerator

    exact_required_denominator = (1 << 128) * (q - n) - q * k
    assert exact_required_denominator > 0
    required_list = q * (q - n) // exact_required_denominator + 1
    assert list_size >= required_list
    assert (1 << 128) * list_size * (q - n) > q * collision_denominator

    # The clean ~1/(2k) trigger genuinely fails; it was sufficient, not necessary.
    assert list_size <= (q - n) // k
    assert bad_slopes > prize_numerator

    # Independent uniform envelope used in the written proof.
    assert quotient_size * q**d < (1 << 53) * count
    assert k * (n + 1) < 1 << 82
    assert (1 << 53) + (1 << 82) < 1 << 83

    # Radius endpoints remain positive and inside the simple-pole interval.
    sigma_min = 1
    for current in (sigma_min, sigma):
        error_numerator = n - k - current
        assert 0 < error_numerator < n - k
    assert n - k - sigma <= n - k - sigma_min

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_cyclic_simple_pole_mca_floor"]["status"] == "PROVED"
    assert nodes["rate_half_band_closure"]["status"] == "TARGET"
    edges = {
        (edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]
    }
    assert (
        "rate_half_cyclic_rotated_prefix_floor",
        "rate_half_cyclic_simple_pole_mca_floor",
        "req",
    ) in edges
    assert (
        "rate_half_cyclic_simple_pole_mca_floor",
        "rate_half_band_closure",
        "ev",
    ) in edges

    print(
        "AUDIT_RATE_HALF_CYCLIC_SIMPLE_POLE_MCA_FLOOR_PASS "
        f"list_bits={list_size.bit_length()} bad_slope_bits={bad_slopes.bit_length()} "
        f"required_list_bits={required_list.bit_length()} trigger_q_over_k_fails=1"
    )


if __name__ == "__main__":
    main()

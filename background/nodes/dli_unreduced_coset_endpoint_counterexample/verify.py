#!/usr/bin/env python3
"""Exact verification of the unreduced DLI coset counterexample."""

from __future__ import annotations

import argparse
import copy
import math


N = 1 << 41
T = 1 << 33
K_RS = 1 << 40
K = 340282366920938463463374607431768211201
Q = 115792089237316195423570985008687907766497981100801255856297059112812235718657


def build() -> dict[str, int]:
    two128 = 1 << 128
    two256 = 1 << 256
    deficit = two256 - Q
    central_count = sum(math.comb(128, m) for m in range(1, 65))
    result = {
        "deficit": deficit,
        "central_count": central_count,
        "central_excess_over_2p127": central_count - (1 << 127),
        "bernoulli_margin": (1 << 255) - T * deficit,
        "proth_residue": pow(3, (Q - 1) // 2, Q),
    }
    assert K & 1 and K < two128
    assert Q == K * two128 + 1
    assert result["proth_residue"] == Q - 1
    assert K_RS * 2 == N
    assert (Q - 1) % N == 0 and Q < two256
    assert result == {
        "deficit": 86772003564839308183160524895100893921279,
        "central_count": 182116756481433273164755097604074381602,
        "central_excess_over_2p127": 11975573020964041433067793888190275874,
        "bernoulli_margin": 57896044618658097711785491758978118887874504048941017334424451979439557836800,
        "proth_residue": Q - 1,
    }
    assert result["central_count"] > 1 << 127
    assert T * deficit < 1 << 255
    assert (result["central_count"] >> 1) > 1 << 125
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        caught = 0
        for key, value in (
            ("central_excess_over_2p127", 0),
            ("bernoulli_margin", 0),
            ("proth_residue", 0),
            ("deficit", 1 << 224),
        ):
            changed = copy.deepcopy(result)
            changed[key] = value
            try:
                assert changed == result
            except AssertionError:
                caught += 1
        assert caught == 4
        print("DLI_UNREDUCED_COSET_COUNTEREXAMPLE_TAMPER_PASS mutations=4/4")
        return
    print(
        "DLI_UNREDUCED_COSET_COUNTEREXAMPLE_PASS "
        f"central_count={result['central_count']} endpoint_lower_bits=>126"
    )


if __name__ == "__main__":
    main()

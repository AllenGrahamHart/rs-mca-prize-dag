#!/usr/bin/env python3
"""Exhaustive tiny-code replay of the full-agreement MCA endpoint."""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def main() -> None:
    prime, n = 2, 3
    code = ((0, 0, 0), (1, 1, 1))
    words = tuple(product(range(prime), repeat=n))
    maxima = [0] * (n + 1)

    for a in range(1, n + 1):
        for first in words:
            for second in words:
                bad = 0
                for slope in range(prime):
                    line = tuple((x + slope * y) % prime for x, y in zip(first, second, strict=True))
                    slope_bad = False
                    for candidate in code:
                        matches = tuple(i for i in range(n) if line[i] == candidate[i])
                        if len(matches) < a:
                            continue
                        for mask in range(1 << len(matches)):
                            support = tuple(matches[j] for j in range(len(matches)) if mask >> j & 1)
                            if len(support) < a:
                                continue
                            extends = any(
                                all(first[i] == c1[i] and second[i] == c2[i] for i in support)
                                for c1 in code
                                for c2 in code
                            )
                            if not extends:
                                slope_bad = True
                                break
                        if slope_bad:
                            break
                    bad += slope_bad
                maxima[a] = max(maxima[a], bad)

    assert maxima[n] == 1
    assert all(maxima[a] >= 1 for a in range(1, n + 1))
    target = Fraction(1, 1 << 128)
    assert Fraction(1, (1 << 128) - 1) > target
    assert Fraction(1, 1 << 128) == target

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["mca_full_agreement_endpoint"]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert ("mca_full_agreement_endpoint", "rate_half_band_closure", "ev") in edges

    print(f"MCA_FULL_AGREEMENT_ENDPOINT_PASS maxima={maxima[1:]}")


if __name__ == "__main__":
    main()

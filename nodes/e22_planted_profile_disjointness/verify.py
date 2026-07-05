#!/usr/bin/env python3
"""Check planted profile disjointness on the local E22 sunflower cells."""

from __future__ import annotations

import sys
from pathlib import Path

CORE = Path(__file__).resolve().parents[1] / "worst_word_challenger_pricing" / "notes"
sys.path.insert(0, str(CORE))

from e22_core import pattern, poly_eval, poly_scale, sunflower_word  # noqa: E402


def main() -> None:
    checks = 0
    for n in (16, 32):
        for sigma in (1, 2):
            for k in (1, 2, 4, 8):
                if k > n:
                    continue
                word = sunflower_word(n, k, sigma, "cyclic_step_1", "linear")
                core_size = len(word["core"])
                if len(set(word["scalars"])) != len(word["scalars"]):
                    continue
                for scalar, petal in zip(word["scalars"], word["petals"]):
                    poly = poly_scale(word["core_locator"], scalar)
                    rec = pattern(poly, word)
                    petal_hits = rec["petal_agreements"]
                    assert rec["core_agreement"] == core_size
                    assert rec["background_agreement"] == 0
                    assert petal_hits.count(word["ell"]) == 1
                    assert all(c in (0, word["ell"]) for c in petal_hits)
                    assert sum(1 for c in petal_hits if c) == 1
                    for idx in word["background"]:
                        assert poly_eval(poly, word["domain"][idx]) != 0
                    checks += 1
    print(f"E22 planted profile checks passed: {checks}")


if __name__ == "__main__":
    main()

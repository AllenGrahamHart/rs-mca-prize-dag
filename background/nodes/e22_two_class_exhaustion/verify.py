#!/usr/bin/env python3
"""Light sanity checks for the E22 two-class exhaustion proof.

The proof is algebraic.  This script only checks the reconstructed finite E22
sweep cells for the ratio-flat obstruction eliminated in proof.md.
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CORE = ROOT / "critical" / "nodes" / "worst_word_challenger_pricing" / "notes"
sys.path.insert(0, str(CORE))

from e22_core import P, inv_mod, locator, poly_eval, sunflower_word  # noqa: E402


RATE_K = {
    16: [1, 2, 4, 8],
    32: [2, 4, 8, 16],
    64: [4, 8, 16, 32],
}

LAYOUTS = {
    16: ["cyclic_step_1", "shuffle_1601"],
    32: ["cyclic_step_1", "shuffle_3201"],
    64: ["cyclic_step_1", "shuffle_6401"],
}


def ratio_values(num: tuple[int, ...], den: tuple[int, ...], points: list[int]) -> set[int]:
    values: set[int] = set()
    for x in points:
        den_x = poly_eval(den, x, P)
        if den_x == 0:
            raise AssertionError("petal point hit a core/background locator root")
        values.add(poly_eval(num, x, P) * inv_mod(den_x, P) % P)
    return values


def main() -> None:
    checked_cells = 0
    checked_swaps = 0
    for n, ks in RATE_K.items():
        for k in ks:
            for sigma in (1, 2, 3):
                ell = sigma + 1
                if k + sigma >= n:
                    continue
                for layout in LAYOUTS[n]:
                    word = sunflower_word(n, k, sigma, layout, "linear")
                    core = sorted(word["core"])
                    background = sorted(word["background"])
                    petals = word["petals"]
                    domain = word["domain"]
                    if len(background) >= ell:
                        raise AssertionError((n, k, sigma, layout, len(background), ell))
                    checked_cells += 1
                    for r in range(1, len(background) + 1):
                        for removed_core in itertools.combinations(core, r):
                            den = locator([domain[i] for i in removed_core], P)
                            for added_background in itertools.combinations(background, r):
                                num = locator([domain[i] for i in added_background], P)
                                for petal in petals:
                                    checked_swaps += 1
                                    values = ratio_values(num, den, [domain[i] for i in petal])
                                    if len(values) == 1:
                                        raise AssertionError(
                                            "non-core ratio-flat swap",
                                            {
                                                "n": n,
                                                "k": k,
                                                "sigma": sigma,
                                                "layout": layout,
                                                "removed_core": removed_core,
                                                "added_background": added_background,
                                                "petal": petal,
                                                "value": next(iter(values)),
                                            },
                                        )
    print("E22 ratio-flat sanity check passed")
    print(f"checked_cells={checked_cells}")
    print(f"checked_noncore_swap_petal_tests={checked_swaps}")


if __name__ == "__main__":
    main()

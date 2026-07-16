#!/usr/bin/env python3
"""Verify the PMA full-petal band/root composition arithmetically."""

from __future__ import annotations

import json


NODE = "pma_full_petal_band_composition"


def admissible(ell: int, petals: int, r: int, d: int, touched: int) -> bool:
    return (
        0 <= r < ell
        and 2 <= touched <= petals
        and touched * ell + r >= d + ell
    )


def run() -> dict[str, int | str]:
    shapes = 0
    top_shapes = 0
    root_zero_shapes = 0
    residual_shapes = 0
    coordinate_checks = 0

    for ell in range(1, 13):
        for petals in range(2, 13):
            for background_size in range(ell):
                for r in range(background_size + 1):
                    for touched in range(2, petals + 1):
                        for d in range(touched * ell):
                            if not admissible(ell, petals, r, d, touched):
                                continue
                            shapes += 1
                            top = d >= ell * (petals - 2)
                            excess = max(0, 2 * d + 1 - touched * ell)
                            root_zero = excess == 0
                            if top:
                                top_shapes += 1
                                assert touched >= petals - 1
                            if root_zero:
                                root_zero_shapes += 1
                            if touched >= 2 * petals - 4:
                                assert top or root_zero
                            if petals <= 3:
                                assert top or root_zero
                            if petals == 4 and touched == 4:
                                assert top or root_zero

                            if not top:
                                a = petals - touched
                                v = ell * (petals - 2) - d
                                assert v >= 1
                                assert (a - 1) * ell <= r + v
                                assert excess == max(
                                    0, ell * (petals + a - 4) - 2 * v + 1
                                )
                                coordinate_checks += 1
                                if not root_zero:
                                    residual_shapes += 1
                                    assert petals >= 4
                                    assert touched < 2 * petals - 4

    # Equality mutant: this legal top-band shape has one untouched petal.
    equality_mutant = dict(ell=2, petals=4, r=0, d=4, touched=3)
    assert admissible(**equality_mutant)
    assert equality_mutant["d"] >= equality_mutant["ell"] * (
        equality_mutant["petals"] - 2
    )
    assert equality_mutant["touched"] != equality_mutant["petals"]

    # Maximality mutant: allowing r=ell permits M-2 touched petals on-band.
    ell, petals, r, d, touched = 2, 4, 2, 4, 2
    assert touched * ell + r >= d + ell
    assert d >= ell * (petals - 2)
    assert touched == petals - 2
    assert not admissible(ell, petals, r, d, touched)

    # Non-planted mutant: t=1 leaves an unclosed M=3 arithmetic shape.
    ell, petals, r, d, touched = 5, 3, 3, 3, 1
    assert touched * ell + r >= d + ell
    assert d < ell * (petals - 2)
    assert max(0, 2 * d + 1 - touched * ell) > 0

    return {
        "node": NODE,
        "status": "PASS",
        "admissible_shapes": shapes,
        "top_shapes": top_shapes,
        "root_zero_shapes": root_zero_shapes,
        "residual_shapes": residual_shapes,
        "coordinate_checks": coordinate_checks,
        "mutations_caught": 3,
    }


if __name__ == "__main__":
    print(json.dumps(run(), sort_keys=True))

#!/usr/bin/env python3
"""Independent replay of the seed-3 sharp-cell witness."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import random


ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "notes/pilots_20260807/fpc5_ratehalf_m4_t2_small_census.py"
RESULT = ROOT / "notes/pilots_20260807/fpc5_ratehalf_m4_t2_small_census_result.json"


def load_script():
    spec = importlib.util.spec_from_file_location("fpc5_census", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_script()
    result = json.loads(RESULT.read_text())
    assert result["mode"] == "adversarial-label"
    assert result["layouts"] == 50
    assert result["nonempty_layouts"] == 41
    assert result["total_contributors"] == 71
    assert result["maximum_layout"] == 5

    p, n, ell, k = 97, 32, 4, 16
    generator = module.primitive_root(p)
    domain = [pow(generator, 3 * exponent, p) for exponent in range(n)]
    points = domain[:]
    random.Random(3).shuffle(points)
    core = points[:15]
    background = points[15:16]
    tail = points[16:]
    petals = [tail[index * ell : (index + 1) * ell] for index in range(4)]
    witnesses = module.adversarial_layout(core, background, petals, p)
    witness = next(item for item in witnesses if item["pair"] == [1, 3])
    assert witness["missed"] == [75, 28, 30, 50, 19]
    assert witness["labels"] == [2, 1, 3, 72]
    assert witness["f"] == [67, 32, 8, 88, 89, 1]
    assert witness["w"] == [40, 90, 43, 55, 78, 76]

    missed = set(witness["missed"])
    retained = [point for point in core if point not in missed]
    p_poly = module.mul(module.locator(retained, p), witness["w"], p)
    assert len(p_poly) - 1 < k
    core_locator = module.locator(core, p)
    word = {point: 0 for point in core + background}
    for petal, label in zip(petals, witness["labels"]):
        for point in petal:
            word[point] = label * module.evaluate(core_locator, point, p) % p
    agreements = {
        point
        for point in domain
        if module.evaluate(p_poly, point, p) == word[point]
    }
    expected = set(retained + background + petals[1] + petals[3])
    assert agreements == expected
    assert len(agreements) == k + ell - 1 == 19

    print(
        "L1_FPC5_RATEHALF_M4_T2_SHARP_NONEMPTY_PASS "
        "layouts=50 nonempty=41 contributors=71 seed3_agreements=19"
    )


if __name__ == "__main__":
    main()

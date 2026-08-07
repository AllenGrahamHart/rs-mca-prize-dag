#!/usr/bin/env python3
"""Finite-field replay of the primitive cofactor determinant distance."""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path
import random


HELPER = (
    Path(__file__).resolve().parents[1]
    / "l1_fpc5_ratehalf_m4_t2_sharp_projective_flat_descriptor"
    / "verify.py"
)


def load_helper():
    spec = importlib.util.spec_from_file_location("joint_distance_helper", HELPER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_helper()
    ell, s = 5, 2
    degree = ell + s
    c1, c2 = 2, 5
    l1 = module.locator(list(range(20, 20 + ell)))
    l2 = module.locator(list(range(40, 40 + ell)))
    core = list(range(1, 18))
    background = list(range(60, 72))
    rng = random.Random(20260807)

    records: dict[tuple[int, ...], dict[str, object]] = {}
    attempts = 0
    while len(records) < 120 and attempts < 20_000:
        attempts += 1
        a1 = [rng.randrange(module.P) for _ in range(s + 1)]
        a2 = [rng.randrange(module.P) for _ in range(s + 1)]
        if module.gcd_basis([a1, a2]) != [1]:
            continue
        f_poly = module.scale(
            module.add(
                module.mul(l1, a1), module.scale(module.mul(l2, a2), -1)
            ),
            pow(c2 - c1, -1, module.P),
        )
        if len(f_poly) - 1 != degree:
            continue
        normalization = pow(f_poly[-1], -1, module.P)
        a1 = module.scale(a1, normalization)
        a2 = module.scale(a2, normalization)
        f_poly = module.scale(f_poly, normalization)
        w_poly = module.add(module.scale(f_poly, c1), module.mul(l1, a1))
        assert f_poly[-1] == 1
        assert module.gcd_basis([a1, a2]) == [1]
        key = tuple(module.pad(f_poly, degree + 1))
        records[key] = {
            "a1": a1,
            "a2": a2,
            "f": f_poly,
            "w": w_poly,
            "D": {point for point in core if module.evaluate(f_poly, point) == 0},
            "R": {
                point for point in background if module.evaluate(w_poly, point) == 0
            },
        }
    assert len(records) == 120

    rows = list(records.values())
    pair_checks = 0
    witnessed_shared_roots = 0
    for index, left in enumerate(rows):
        for right in rows[index + 1 :]:
            delta = module.add(
                module.mul(left["a1"], right["a2"]),
                module.scale(module.mul(right["a1"], left["a2"]), -1),
            )
            assert delta != [0]
            assert len(delta) - 1 <= 2 * s
            common = (left["D"] & right["D"]) | (left["R"] & right["R"])
            assert all(module.evaluate(delta, point) == 0 for point in common)
            assert len(common) <= 2 * s
            witnessed_shared_roots += len(common)
            pair_checks += 1

    # A scalar multiple has zero determinant, but monic normalization returns
    # the same locator/cofactor record rather than a second contributor.
    sample = rows[0]
    scalar = 7
    scaled_a1 = module.scale(sample["a1"], scalar)
    scaled_a2 = module.scale(sample["a2"], scalar)
    zero_delta = module.add(
        module.mul(sample["a1"], scaled_a2),
        module.scale(module.mul(scaled_a1, sample["a2"]), -1),
    )
    assert zero_delta == [0]
    scaled_f = module.scale(sample["f"], scalar)
    renormalized_f = module.scale(scaled_f, pow(scaled_f[-1], -1, module.P))
    assert renormalized_f == sample["f"]

    packing_cells = 0
    for test_ell in range(3, 12):
        k_minus_one = 5 * test_ell - 5
        b = test_ell - 3
        for test_s in range(test_ell - 2):
            choose = 2 * test_s + 1
            numerator = math.comb(k_minus_one + b, choose)
            denominator = math.comb(test_ell + 2 * test_s, choose)
            assert denominator > 0 and numerator >= denominator
            assert numerator // denominator >= 1
            packing_cells += 1

    print(
        "L1_FPC5_JOINT_SUPPORT_DISTANCE_PASS "
        f"records={len(rows)} pairs={pair_checks} "
        f"shared_roots={witnessed_shared_roots} packing_cells={packing_cells}"
    )


if __name__ == "__main__":
    main()

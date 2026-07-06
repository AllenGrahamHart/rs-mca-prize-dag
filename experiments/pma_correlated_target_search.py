#!/usr/bin/env python3
"""Adversarial PMA correlated-target search.

The PMA wide residual is about auxiliary words of the form

    U*(x) = c_i L_D(x),  x in T_i,

with a common defect locator and one scalar per petal.  The earlier
`pma_aux_list_probe.py` tests one scalar/defect choice.  This script varies the
scalar pattern and defect locator, then classifies threshold candidates by
simple structural diagnostics: character/twist support and how their agreement
is distributed across petals.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
import time
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "experiments" / "amber_stress" / "pma_correlated_target_search_results.json"

P = 109
ELL = 3
D_DEG = 5
SIGMA = ELL - 1
AGREE_THRESHOLD = D_DEG + 1 + SIGMA


def factor_int(n: int) -> list[int]:
    factors: list[int] = []
    d = 2
    value = n
    while d * d <= value:
        if value % d == 0:
            factors.append(d)
            while value % d == 0:
                value //= d
        d += 1 if d == 2 else 2
    if value > 1:
        factors.append(value)
    return factors


def primitive_root(p: int) -> int:
    factors = factor_int(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // f, p) != 1 for f in factors):
            return g
    raise ValueError(f"no primitive root for p={p}")


def subgroup(p: int, n: int) -> list[int]:
    if (p - 1) % n:
        raise ValueError(f"n={n} does not divide p-1={p - 1}")
    z = pow(primitive_root(p), (p - 1) // n, p)
    h = [pow(z, i, p) for i in range(n)]
    if len(set(h)) != n:
        raise AssertionError("wrong subgroup order")
    return h


def eval_poly(coeffs: tuple[int, ...], x: int) -> int:
    value = 0
    for c in reversed(coeffs):
        value = (value * x + c) % P
    return value


def solve_interpolation(xs: list[int], ys: list[int]) -> tuple[int, ...] | None:
    n = D_DEG + 1
    mat = [[pow(xs[i], j, P) for j in range(n)] + [ys[i] % P] for i in range(n)]
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, n) if mat[i][c] % P), None)
        if pivot is None:
            return None
        mat[r], mat[pivot] = mat[pivot], mat[r]
        inv = pow(mat[r][c] % P, -1, P)
        mat[r] = [(v * inv) % P for v in mat[r]]
        for i in range(n):
            if i != r and mat[i][c] % P:
                f = mat[i][c] % P
                mat[i] = [(mat[i][j] - f * mat[r][j]) % P for j in range(n + 1)]
        r += 1
    return tuple(mat[i][n] % P for i in range(n))


def locator_value(roots: list[int], x: int) -> int:
    value = 1
    for root in roots:
        value = value * (x - root) % P
    return value


def defect_roots(kind: str, h: list[int], rng: random.Random) -> list[int]:
    outside = [x for x in range(1, P) if x not in set(h)]
    if kind == "first":
        return outside[:D_DEG]
    if kind == "stride2":
        return outside[::2][:D_DEG]
    if kind == "tail":
        return outside[-D_DEG:]
    if kind == "random":
        return sorted(rng.sample(outside, D_DEG))
    raise ValueError(kind)


def scalar_pattern(kind: str, image: list[int], rng: random.Random) -> list[int]:
    if kind == "constant":
        return [1 for _ in image]
    if kind == "linear_index":
        return [(i + 1) % P for i, _ in enumerate(image)]
    if kind == "quadratic_index":
        return [(i * i + 2 * i + 3) % P for i, _ in enumerate(image)]
    if kind == "alternating":
        return [1 if i % 2 == 0 else P - 1 for i, _ in enumerate(image)]
    if kind == "image_linear":
        return [(7 + 5 * y) % P for y in image]
    if kind == "image_quadratic":
        return [(3 + 2 * y + 11 * y * y) % P for y in image]
    if kind == "random":
        return [rng.randrange(1, P) for _ in image]
    raise ValueError(kind)


def make_aux_word(m: int, defect_kind: str, scalar_kind: str, rng: random.Random) -> dict[str, Any]:
    h = subgroup(P, ELL * m)
    image = sorted({pow(x, ELL, P) for x in h})
    if len(image) != m:
        raise AssertionError("wrong petal quotient")
    roots = defect_roots(defect_kind, h, rng)
    scalars = scalar_pattern(scalar_kind, image, rng)
    scalar_by_image = dict(zip(image, scalars))
    fibers: dict[int, list[int]] = {y: [] for y in image}
    word: dict[int, int] = {}
    for x in h:
        y = pow(x, ELL, P)
        fibers[y].append(x)
        word[x] = scalar_by_image[y] * locator_value(roots, x) % P
    if any(len(xs) != ELL for xs in fibers.values()):
        raise AssertionError("wrong petal fiber size")
    return {
        "points": sorted(word),
        "word": word,
        "image": image,
        "fibers": fibers,
        "defect_roots": roots,
        "scalars": scalars,
    }


def is_twist_or_pullback(coeffs: tuple[int, ...]) -> bool:
    residues = {i % ELL for i, c in enumerate(coeffs) if c % P}
    return len(residues) <= 1


def petal_profile(coeffs: tuple[int, ...], word_data: dict[str, Any]) -> dict[str, int]:
    profile = []
    word = word_data["word"]
    for y in word_data["image"]:
        agree = sum(eval_poly(coeffs, x) == word[x] for x in word_data["fibers"][y])
        profile.append(agree)
    return {
        "agreement": sum(profile),
        "petals_touched": sum(1 for a in profile if a),
        "full_petals": sum(1 for a in profile if a == ELL),
        "partial_petals": sum(1 for a in profile if 0 < a < ELL),
        "max_petal_agreement": max(profile, default=0),
    }


def total_combinations(npoints: int) -> int:
    total = 1
    for a in range(npoints - D_DEG, npoints + 1):
        total *= a
    for a in range(1, D_DEG + 2):
        total //= a
    return total


def combo_iterator(npoints: int, sample_limit: int | None, rng: random.Random):
    total = total_combinations(npoints)
    if sample_limit is None or total <= sample_limit:
        yield from itertools.combinations(range(npoints), D_DEG + 1)
        return
    seen: set[tuple[int, ...]] = set()
    while len(seen) < sample_limit:
        combo = tuple(sorted(rng.sample(range(npoints), D_DEG + 1)))
        if combo not in seen:
            seen.add(combo)
            yield combo


def scan_profile(spec: dict[str, Any], rng: random.Random, deadline: float) -> dict[str, Any]:
    word_data = make_aux_word(spec["M"], spec["defect"], spec["scalars"], rng)
    points = word_data["points"]
    word = word_data["word"]
    sample_limit = spec.get("sample_limit")
    total = total_combinations(len(points))

    candidates: dict[tuple[int, ...], dict[str, int]] = {}
    checked = 0
    partial = False
    for combo in combo_iterator(len(points), sample_limit, rng):
        if time.monotonic() >= deadline:
            partial = True
            break
        coeffs = solve_interpolation([points[i] for i in combo], [word[points[i]] for i in combo])
        checked += 1
        if coeffs is None or coeffs in candidates:
            continue
        prof = petal_profile(coeffs, word_data)
        if prof["agreement"] >= AGREE_THRESHOLD:
            candidates[coeffs] = prof

    full_agreement = sum(1 for p in candidates.values() if p["agreement"] == len(points))
    twist_like = sum(1 for c in candidates if is_twist_or_pullback(c))
    spread_non_twist = sum(
        1
        for c, p in candidates.items()
        if not is_twist_or_pullback(c) and p["petals_touched"] >= 4 and p["partial_petals"] >= 2
    )
    max_agreement = max((p["agreement"] for p in candidates.values()), default=0)
    max_touched = max((p["petals_touched"] for p in candidates.values()), default=0)
    max_partial = max((p["partial_petals"] for p in candidates.values()), default=0)
    estimated_threshold_count = len(candidates) * total / checked if checked and checked < total else len(candidates)

    return {
        "name": spec["name"],
        "M": spec["M"],
        "defect": spec["defect"],
        "scalars": spec["scalars"],
        "points": len(points),
        "agreement_threshold": AGREE_THRESHOLD,
        "johnson_safe": AGREE_THRESHOLD * AGREE_THRESHOLD > D_DEG * len(points),
        "total_interpolation_subsets": total,
        "checked_interpolation_subsets": checked,
        "exact": checked == total and not partial,
        "partial": partial,
        "threshold_candidates": len(candidates),
        "estimated_threshold_candidates": estimated_threshold_count,
        "full_agreement_candidates": full_agreement,
        "twist_or_pullback_like_candidates": twist_like,
        "spread_non_twist_candidates": spread_non_twist,
        "max_agreement": max_agreement,
        "max_petals_touched": max_touched,
        "max_partial_petals": max_partial,
    }


def planned_profiles() -> list[dict[str, Any]]:
    profiles = []
    for defect, scalars in [
        ("first", "constant"),
        ("first", "linear_index"),
        ("first", "image_linear"),
        ("first", "alternating"),
        ("stride2", "alternating"),
        ("random", "linear_index"),
        ("random", "random"),
    ]:
        profiles.append({"name": f"M6_{defect}_{scalars}", "M": 6, "defect": defect, "scalars": scalars})
    for defect, scalars in [
        ("first", "constant"),
        ("first", "linear_index"),
        ("random", "random"),
    ]:
        profiles.append({"name": f"M9_{defect}_{scalars}", "M": 9, "defect": defect, "scalars": scalars})
    for defect, scalars in [
        ("first", "linear_index"),
        ("stride2", "alternating"),
        ("random", "random"),
    ]:
        profiles.append(
            {
                "name": f"M12_{defect}_{scalars}_sample",
                "M": 12,
                "defect": defect,
                "scalars": scalars,
                "sample_limit": 60_000,
                "min_seconds": 4.0,
            }
        )
    return profiles


def checkpoint(results: dict[str, Any]) -> None:
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")


def summarize(results: dict[str, Any]) -> None:
    profiles = results.get("profiles", [])
    alarms = []
    for profile in profiles:
        if profile.get("partial"):
            alarms.append({"profile": profile["name"], "reason": "partial"})
        if profile.get("exact") and profile.get("spread_non_twist_candidates", 0) > 5000:
            alarms.append(
                {
                    "profile": profile["name"],
                    "reason": "many_exact_spread_non_twist_candidates",
                    "count": profile["spread_non_twist_candidates"],
                }
            )
    results["summary"] = {
        "status": "FAIL" if alarms else "PASS",
        "profiles_checked": len(profiles),
        "alarms": alarms,
        "exact_profiles": sum(1 for p in profiles if p.get("exact")),
        "sampled_profiles": sum(1 for p in profiles if not p.get("exact") and not p.get("partial")),
        "max_threshold_candidates": max((p.get("threshold_candidates", 0) for p in profiles), default=0),
        "max_spread_non_twist_candidates": max(
            (p.get("spread_non_twist_candidates", 0) for p in profiles), default=0
        ),
        "max_agreement": max((p.get("max_agreement", 0) for p in profiles), default=0),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-limit", type=float, default=55.0)
    parser.add_argument("--seed", type=int, default=20260706)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    deadline = time.monotonic() + args.time_limit
    results: dict[str, Any] = {
        "started_at_unix": time.time(),
        "node": "petal_mixed_amplification / pma_wide_residual",
        "seed": args.seed,
        "time_limit_seconds": args.time_limit,
        "profiles": [],
    }
    checkpoint(results)
    for spec in planned_profiles():
        if time.monotonic() + spec.get("min_seconds", 2.0) >= deadline:
            break
        t0 = time.monotonic()
        profile = scan_profile(spec, rng, deadline)
        profile["wall_seconds"] = round(time.monotonic() - t0, 6)
        results["profiles"].append(profile)
        summarize(results)
        checkpoint(results)
        if profile.get("partial"):
            break
    results["finished_at_unix"] = time.time()
    summarize(results)
    checkpoint(results)
    print(json.dumps(results["summary"], indent=2, sort_keys=True))
    if results["summary"]["status"] == "PASS":
        print("PASS: PMA correlated-target search found no large spread residual alarm")
    else:
        print("FAIL: PMA correlated-target search found an alarm")
    return 0 if results["summary"]["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

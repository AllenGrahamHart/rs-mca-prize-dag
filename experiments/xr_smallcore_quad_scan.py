#!/usr/bin/env python3
"""Bounded XR small-core quadrilateral stress scan.

The triangle scan exercises the first small-core residual surface feeding
`xr_smallcore_spread_count`.  This companion scan probes the next natural
surface: four aligned supports with pairwise-small cores.  It is evidence only:
rank drops are treated as suspicious profiles to record, not as automatic
counterexamples to the live `16 n^3` count.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
import time
from pathlib import Path
from typing import Any

from xr_smallcore_triangle_scan import chart, rank


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "experiments" / "amber_stress" / "xr_smallcore_quad_scan_results.json"


def slope_probes(p: int) -> list[tuple[int, int, int, int]]:
    raw = [
        (1, 2, 3, 5),
        (1, 2, 5, 7),
        (1, 3, 7, 11),
        (2, 5, 11, 17),
        (3, 7, 13, 19),
        (5, 11, 17, 23),
    ]
    out: list[tuple[int, int, int, int]] = []
    for quad in raw:
        vals = tuple(((x - 1) % (p - 1)) + 1 for x in quad)
        if len(set(vals)) == 4:
            out.append(vals)  # type: ignore[arg-type]
    return out


def normal_form_k(
    bases: list[list[list[int]]],
    slopes: tuple[int, ...],
    union: list[int],
    p: int,
) -> list[list[int]]:
    rows: list[list[int]] = []
    for coord in union:
        rows.append([lam[coord] for b in bases for lam in b])
    for coord in union:
        rows.append([(z * lam[coord]) % p for z, b in zip(slopes, bases) for lam in b])
    return rows


def support_quads(
    supports: list[tuple[int, ...]],
    cap: int,
    rng: random.Random,
) -> tuple[bool, list[tuple[tuple[int, ...], ...]]]:
    total = len(supports) ** 4
    if total <= cap:
        return True, [tuple(q) for q in itertools.product(supports, repeat=4)]
    return False, [tuple(rng.choice(supports) for _ in range(4)) for _ in range(cap)]


def overlap_stats(sets: list[set[int]]) -> dict[str, int]:
    pair_sum = 0
    max_pair = 0
    for i, j in itertools.combinations(range(4), 2):
        overlap = len(sets[i] & sets[j])
        pair_sum += overlap
        max_pair = max(max_pair, overlap)
    triple_sum = sum(len(sets[i] & sets[j] & sets[k]) for i, j, k in itertools.combinations(range(4), 3))
    quad = len(sets[0] & sets[1] & sets[2] & sets[3])
    # Generalizes the triangle filter pair_sum - triple_intersection:
    # a point in exactly r supports contributes r-1.
    repeated_mass = pair_sum - triple_sum + quad
    return {
        "pair_sum": pair_sum,
        "triple_sum": triple_sum,
        "quad_intersection": quad,
        "repeated_mass": repeated_mass,
        "max_pair": max_pair,
    }


def scan_config(
    p: int,
    n: int,
    k: int,
    A: int,
    quad_cap: int,
    deadline: float,
    rng: random.Random,
) -> dict[str, Any]:
    t = A - k
    target_rank = 4 * t
    domain = list(range(1, n + 1))
    supports = [tuple(s) for s in itertools.combinations(range(n), A)]
    exact, quads = support_quads(supports, quad_cap, rng)
    probes = slope_probes(p)
    cache: dict[tuple[int, ...], list[list[int]] | None] = {}

    def getchart(T: tuple[int, ...]) -> list[list[int]] | None:
        if T not in cache:
            basis = chart(domain, k, T, p)
            cache[T] = basis if basis is not None and len(basis) == t else None
        return cache[T]

    profiles: dict[tuple[int, int, int, int], dict[str, Any]] = {}
    checked_quads = 0
    light_quads = 0
    slope_tests = 0
    rank_drop_tests = 0
    severe_rank_drop_tests = 0
    min_rank = target_rank
    stopped_for_time = False
    examples: list[dict[str, Any]] = []

    for quad in quads:
        if time.monotonic() >= deadline:
            stopped_for_time = True
            break
        checked_quads += 1
        sets = [set(T) for T in quad]
        stats = overlap_stats(sets)
        union = sorted(set().union(*sets))
        small_core = stats["max_pair"] < A - 1
        light = stats["repeated_mass"] <= 3 * k
        if not (small_core and light):
            continue
        light_quads += 1
        bases = [getchart(T) for T in quad]
        if any(b is None for b in bases):
            continue
        profile_key = (
            stats["repeated_mass"],
            stats["max_pair"],
            len(union),
            stats["quad_intersection"],
        )
        profile = profiles.setdefault(
            profile_key,
            {
                "seen_quads": 0,
                "slope_tests": 0,
                "full_rank_tests": 0,
                "rank_drop_tests": 0,
                "severe_rank_drop_tests": 0,
                "min_rank": target_rank,
                "max_rank": 0,
            },
        )
        profile["seen_quads"] += 1
        for slopes in probes:
            rk = rank(normal_form_k(bases, slopes, union, p), p)  # type: ignore[arg-type]
            slope_tests += 1
            profile["slope_tests"] += 1
            profile["min_rank"] = min(profile["min_rank"], rk)
            profile["max_rank"] = max(profile["max_rank"], rk)
            min_rank = min(min_rank, rk)
            if rk == target_rank:
                profile["full_rank_tests"] += 1
            else:
                rank_drop_tests += 1
                profile["rank_drop_tests"] += 1
                if rk <= target_rank - 2:
                    severe_rank_drop_tests += 1
                    profile["severe_rank_drop_tests"] += 1
                if len(examples) < 12:
                    examples.append(
                        {
                            "quad": [list(T) for T in quad],
                            "slopes": list(slopes),
                            "rank": rk,
                            "target_rank": target_rank,
                            **stats,
                            "union_size": len(union),
                        }
                    )

    no_full_rank_profiles = [
        {"profile": list(key), **value}
        for key, value in sorted(profiles.items())
        if value["full_rank_tests"] == 0
    ]
    return {
        "p": p,
        "n": n,
        "k": k,
        "A": A,
        "t": t,
        "target_rank": target_rank,
        "support_count": len(supports),
        "support_quad_space": len(supports) ** 4,
        "support_quads_exact": exact,
        "checked_support_quads": checked_quads,
        "stopped_for_time": stopped_for_time,
        "slope_probes": [list(s) for s in probes],
        "light_smallcore_quads": light_quads,
        "slope_tests": slope_tests,
        "rank_drop_tests": rank_drop_tests,
        "severe_rank_drop_tests": severe_rank_drop_tests,
        "rank_drop_rate": (rank_drop_tests / slope_tests) if slope_tests else 0.0,
        "min_rank_observed": min_rank if slope_tests else None,
        "profile_count": len(profiles),
        "profiles_without_full_rank_probe": no_full_rank_profiles[:20],
        "profiles_without_full_rank_probe_count": len(no_full_rank_profiles),
        "rank_drop_examples": examples,
    }


def checkpoint(results: dict[str, Any]) -> None:
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")


def summarize(results: dict[str, Any]) -> None:
    configs = results.get("configs", [])
    total_tests = sum(c.get("slope_tests", 0) for c in configs)
    total_drops = sum(c.get("rank_drop_tests", 0) for c in configs)
    results["summary"] = {
        "status": "PASS" if total_drops == 0 else "ATTENTION",
        "configs_checked": len(configs),
        "total_slope_tests": total_tests,
        "total_rank_drop_tests": total_drops,
        "total_severe_rank_drop_tests": sum(c.get("severe_rank_drop_tests", 0) for c in configs),
        "configs_with_rank_drops": sum(1 for c in configs if c.get("rank_drop_tests", 0) > 0),
        "configs_with_profiles_without_full_rank_probe": sum(
            1 for c in configs if c.get("profiles_without_full_rank_probe_count", 0) > 0
        ),
        "max_rank_drop_rate": max((c.get("rank_drop_rate", 0.0) for c in configs), default=0.0),
        "min_rank_observed": min(
            (c["min_rank_observed"] for c in configs if c.get("min_rank_observed") is not None),
            default=None,
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-limit", type=float, default=55.0)
    parser.add_argument("--quad-cap", type=int, default=70_000)
    args = parser.parse_args()

    deadline = time.monotonic() + args.time_limit
    rng = random.Random(20260706)
    # The domain must be roomy enough for the light-surface filter
    # repeated_mass <= 3k to be non-vacuous.
    grid = [
        (17, 12, 2, 4),
        (19, 13, 2, 4),
        (23, 14, 3, 5),
        (29, 15, 3, 5),
    ]
    results: dict[str, Any] = {
        "started_at_unix": time.time(),
        "node": "xr_clean_residual_any_gate / xr_smallcore_spread_count",
        "time_limit_seconds": args.time_limit,
        "quad_cap": args.quad_cap,
        "configs": [],
    }
    checkpoint(results)
    for config in grid:
        if time.monotonic() + 2.0 >= deadline:
            break
        item = scan_config(*config, args.quad_cap, deadline, rng)
        results["configs"].append(item)
        summarize(results)
        checkpoint(results)
    results["finished_at_unix"] = time.time()
    summarize(results)
    checkpoint(results)
    print(json.dumps(results["summary"], indent=2, sort_keys=True))
    if results["summary"]["status"] == "PASS":
        print("PASS: XR small-core quadrilateral stress scan found no rank drops")
    else:
        print("ATTENTION: XR small-core quadrilateral stress scan found rank-drop profiles")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

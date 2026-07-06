#!/usr/bin/env python3
"""Bounded XR small-core spread stress scan.

This adapts the archived XR eliminant census helper into a local, checkpointed
test for the amber premise

    xr_clean_residual_any_gate <- xr_smallcore_spread_count.

It samples or exhausts small support triples, filters to the post-cascade
small-core/light-triangle surface, and checks the stacked normal-form rank for
several deterministic slope triples.  Rank drops are not automatically
falsifiers of the live target: the target is a 16 n^3-compatible count after
paid structures, not emptiness.  The scan is adversarial evidence: it looks for
profiles where stagnation is common or profile-wide under the tested slopes.
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
OUT = ROOT / "experiments" / "amber_stress" / "xr_smallcore_triangle_scan_results.json"


def inv(a: int, p: int) -> int:
    return pow(a % p, p - 2, p)


def rank(rows: list[list[int]], p: int) -> int:
    rows = [r[:] for r in rows]
    r = 0
    nc = len(rows[0]) if rows else 0
    for c in range(nc):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] % p), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        iv = inv(rows[r][c], p)
        rows[r] = [(x * iv) % p for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] % p:
                cc = rows[i][c]
                rows[i] = [(x - cc * y) % p for x, y in zip(rows[i], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r


def solve_square(A: list[list[int]], b: list[int], p: int) -> list[int] | None:
    aug = [row[:] + [rhs] for row, rhs in zip(A, b)]
    n = len(A)
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, n) if aug[i][c] % p), None)
        if piv is None:
            return None
        aug[r], aug[piv] = aug[piv], aug[r]
        iv = inv(aug[r][c], p)
        aug[r] = [(x * iv) % p for x in aug[r]]
        for i in range(n):
            if i != r and aug[i][c] % p:
                cc = aug[i][c]
                aug[i] = [(x - cc * y) % p for x, y in zip(aug[i], aug[r])]
        r += 1
    return [aug[i][n] for i in range(n)]


def chart(domain: list[int], k: int, T: tuple[int, ...], p: int) -> list[list[int]] | None:
    pivots = list(T[:k])
    free = list(T[k:])
    Vp = [[pow(domain[x], d, p) for x in pivots] for d in range(k)]
    basis: list[list[int]] = []
    for q in free:
        rhs = [(-pow(domain[q], d, p)) % p for d in range(k)]
        pv = solve_square(Vp, rhs, p)
        if pv is None:
            return None
        w = [0] * len(domain)
        for x, val in zip(pivots, pv):
            w[x] = val
        w[q] = 1
        basis.append(w)
    return basis


def normal_form(
    bases: list[list[list[int]]],
    slopes: tuple[int, int, int],
    union: list[int],
    p: int,
) -> list[list[int]]:
    rows: list[list[int]] = []
    for coord in union:
        rows.append([lam[coord] for b in bases for lam in b])
    for coord in union:
        rows.append([(z * lam[coord]) % p for z, b in zip(slopes, bases) for lam in b])
    return rows


def slope_probes(p: int) -> list[tuple[int, int, int]]:
    raw = [(1, 2, 3), (1, 2, 5), (1, 3, 7), (2, 5, 11), (3, 7, 13), (5, 11, 17)]
    out: list[tuple[int, int, int]] = []
    for triple in raw:
        vals = tuple(((x - 1) % (p - 1)) + 1 for x in triple)
        if len(set(vals)) == 3:
            out.append(vals)  # type: ignore[arg-type]
    return out


def support_triples(
    supports: list[tuple[int, ...]],
    cap: int,
    rng: random.Random,
) -> tuple[bool, list[tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]]]:
    total = len(supports) ** 3
    if total <= cap:
        return True, list(itertools.product(supports, repeat=3))
    sampled = [
        (rng.choice(supports), rng.choice(supports), rng.choice(supports))
        for _ in range(cap)
    ]
    return False, sampled


def scan_config(
    p: int,
    n: int,
    k: int,
    A: int,
    triple_cap: int,
    deadline: float,
    rng: random.Random,
) -> dict[str, Any]:
    t = A - k
    target_rank = 3 * t
    domain = list(range(1, n + 1))
    supports = [tuple(s) for s in itertools.combinations(range(n), A)]
    exact, triples = support_triples(supports, triple_cap, rng)
    probes = slope_probes(p)
    cache: dict[tuple[int, ...], list[list[int]] | None] = {}

    def getchart(T: tuple[int, ...]) -> list[list[int]] | None:
        if T not in cache:
            b = chart(domain, k, T, p)
            cache[T] = b if b is not None and len(b) == t else None
        return cache[T]

    profiles: dict[tuple[int, int, int, int], dict[str, Any]] = {}
    checked_triples = 0
    light_triples = 0
    slope_tests = 0
    rank_drop_tests = 0
    severe_rank_drop_tests = 0
    min_rank = target_rank
    examples: list[dict[str, Any]] = []
    stopped_for_time = False

    for triple in triples:
        if time.monotonic() >= deadline:
            stopped_for_time = True
            break
        checked_triples += 1
        sets = [set(T) for T in triple]
        pair_intersections = [
            len(sets[0] & sets[1]),
            len(sets[0] & sets[2]),
            len(sets[1] & sets[2]),
        ]
        pair_sum = sum(pair_intersections)
        trip = len(sets[0] & sets[1] & sets[2])
        max_pair = max(pair_intersections)
        union = sorted(set().union(*sets))
        # Post-cascade small-core surface: no pair shares A-1 or more points.
        small_core = max_pair < A - 1
        # E32 light-triangle filter: heavy triples are tangent/paid territory.
        light = pair_sum - trip <= 2 * k
        if not (small_core and light):
            continue
        light_triples += 1
        bases = [getchart(T) for T in triple]
        if any(b is None for b in bases):
            continue
        profile_key = (pair_sum, trip, len(union), max_pair)
        profile = profiles.setdefault(
            profile_key,
            {
                "seen_triples": 0,
                "slope_tests": 0,
                "full_rank_tests": 0,
                "rank_drop_tests": 0,
                "severe_rank_drop_tests": 0,
                "min_rank": target_rank,
                "max_rank": 0,
            },
        )
        profile["seen_triples"] += 1
        for slopes in probes:
            rk = rank(normal_form(bases, slopes, union, p), p)  # type: ignore[arg-type]
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
                if len(examples) < 8:
                    examples.append(
                        {
                            "triple": [list(T) for T in triple],
                            "slopes": list(slopes),
                            "rank": rk,
                            "target_rank": target_rank,
                            "pair_intersections": pair_intersections,
                            "triple_intersection": trip,
                            "union_size": len(union),
                        }
                    )

    no_full_rank_profiles = [
        {
            "profile": list(key),
            **value,
        }
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
        "support_triple_space": len(supports) ** 3,
        "support_triples_exact": exact,
        "checked_support_triples": checked_triples,
        "stopped_for_time": stopped_for_time,
        "slope_probes": [list(s) for s in probes],
        "light_smallcore_triples": light_triples,
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
    results["summary"] = {
        "status": "PASS",
        "configs_checked": len(configs),
        "total_slope_tests": sum(c.get("slope_tests", 0) for c in configs),
        "total_rank_drop_tests": sum(c.get("rank_drop_tests", 0) for c in configs),
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
    parser.add_argument("--triple-cap", type=int, default=220_000)
    args = parser.parse_args()

    deadline = time.monotonic() + args.time_limit
    rng = random.Random(20260706)
    grid = [
        (17, 8, 2, 4),
        (19, 9, 2, 4),
        (23, 10, 3, 5),
        (29, 12, 3, 5),
    ]
    results: dict[str, Any] = {
        "started_at_unix": time.time(),
        "node": "xr_clean_residual_any_gate / xr_smallcore_spread_count",
        "time_limit_seconds": args.time_limit,
        "triple_cap": args.triple_cap,
        "configs": [],
    }
    checkpoint(results)
    for config in grid:
        if time.monotonic() + 2.0 >= deadline:
            break
        item = scan_config(*config, args.triple_cap, deadline, rng)
        results["configs"].append(item)
        summarize(results)
        checkpoint(results)
    results["finished_at_unix"] = time.time()
    summarize(results)
    checkpoint(results)
    print(json.dumps(results["summary"], indent=2, sort_keys=True))
    print("PASS: XR small-core triangle stress scan completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

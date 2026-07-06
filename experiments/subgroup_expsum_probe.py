#!/usr/bin/env python3
"""Adversarial small-prime probes for the subgroup exponential-sum import.

The DAG node ``subgroup_expsum_input`` is only a named analytic import:
"subgroup ranges beyond N >= p^(3/7+eps)".  The repo does not pin a numerical
power-saving exponent here, so this harness does not certify the import.

What it does test:

* multiplicative subgroups H <= F_p^* with |H| just above p^(3/7), plus larger
  subgroup rows, looking for near-linear additive-character concentration;
* exact full-group cancellation as a sanity check;
* interval/singleton negative controls, proving that the detector would flag
  non-subgroup or below-range no-cancellation examples.

The falsifier recorded by this script is a subgroup row in the advertised range
with max_a |sum_{x in H} exp(2*pi*i*a*x/p)| / |H| above NEAR_LINEAR_THRESHOLD.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "experiments" / "amber_stress" / "subgroup_expsum_results.json"

RANGE_EXPONENT = 3 / 7
MAX_PRIME = 2800
NEAR_LINEAR_THRESHOLD = 0.72


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [i for i in range(2, limit + 1) if sieve[i]]


def factor_distinct(n: int) -> list[int]:
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out.append(n)
    return out


def divisors(n: int) -> list[int]:
    out = []
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def primitive_root(p: int) -> int:
    factors = factor_distinct(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g
    raise ValueError(f"no primitive root for {p}")


def subgroup(p: int, order: int) -> list[int]:
    gen = primitive_root(p)
    step = (p - 1) // order
    h = pow(gen, step, p)
    out = []
    x = 1
    for _ in range(order):
        out.append(x)
        x = (x * h) % p
    return out


def max_additive_ratio(p: int, points: list[int]) -> dict:
    cos = [math.cos(2 * math.pi * x / p) for x in range(p)]
    sin = [math.sin(2 * math.pi * x / p) for x in range(p)]
    max_abs = -1.0
    max_a = None
    for a in range(1, p):
        re = 0.0
        im = 0.0
        for x in points:
            y = (a * x) % p
            re += cos[y]
            im += sin[y]
        value = math.hypot(re, im)
        if value > max_abs:
            max_abs = value
            max_a = a
    size = len(points)
    ratio = max_abs / size if size else 0.0
    eta = -math.log(ratio) / math.log(p) if ratio > 0 else None
    return {
        "max_abs": max_abs,
        "max_character": max_a,
        "ratio": ratio,
        "eta_observed": eta,
        "sqrt_p_units": max_abs / math.sqrt(p),
    }


def candidate_rows(max_prime: int) -> list[tuple[int, int]]:
    rows: list[tuple[int, int]] = []
    seen = set()
    for p in primes_upto(max_prime):
        if p < 100:
            continue
        ds = [
            d
            for d in divisors(p - 1)
            if d < p - 1 and d >= p**RANGE_EXPONENT and d <= p**0.72
        ]
        if not ds:
            continue
        picks = {ds[0], ds[len(ds) // 2], ds[-1]}
        for d in sorted(picks):
            key = (p, d)
            if key not in seen:
                seen.add(key)
                rows.append(key)
    return rows


def checkpoint(payload: dict) -> None:
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-limit", type=float, default=55.0)
    parser.add_argument("--max-prime", type=int, default=MAX_PRIME)
    args = parser.parse_args()

    started = time.monotonic()
    deadline = started + args.time_limit
    payload = {
        "started_at_unix": time.time(),
        "time_limit_seconds": args.time_limit,
        "range_exponent": RANGE_EXPONENT,
        "near_linear_threshold": NEAR_LINEAR_THRESHOLD,
        "rows": [],
        "controls": [],
        "summary": {
            "rows_checked": 0,
            "near_linear_failures": 0,
            "max_ratio": 0.0,
            "min_eta_observed": None,
            "max_sqrt_p_units": 0.0,
            "controls_detected": 0,
            "controls_total": 0,
        },
    }
    checkpoint(payload)

    for p, order in candidate_rows(args.max_prime):
        if time.monotonic() >= deadline:
            payload["stopped_by_time_guard"] = True
            break
        H = subgroup(p, order)
        stats = max_additive_ratio(p, H)
        alpha = math.log(order) / math.log(p)
        item = {
            "p": p,
            "order": order,
            "alpha": alpha,
            **stats,
            "near_linear_failure": stats["ratio"] > NEAR_LINEAR_THRESHOLD,
        }
        payload["rows"].append(item)
        payload["summary"]["rows_checked"] += 1
        payload["summary"]["near_linear_failures"] += 1 if item["near_linear_failure"] else 0
        payload["summary"]["max_ratio"] = max(payload["summary"]["max_ratio"], stats["ratio"])
        payload["summary"]["max_sqrt_p_units"] = max(
            payload["summary"]["max_sqrt_p_units"], stats["sqrt_p_units"]
        )
        eta = stats["eta_observed"]
        if eta is not None:
            current = payload["summary"]["min_eta_observed"]
            payload["summary"]["min_eta_observed"] = eta if current is None else min(current, eta)
        checkpoint(payload)

    # Negative and sanity controls.
    for p in [257, 769, 1601]:
        if p > args.max_prime:
            continue
        threshold_order = min(d for d in divisors(p - 1) if d >= p**RANGE_EXPONENT)
        interval = list(range(1, threshold_order + 1))
        singleton = [1]
        full_group = list(range(1, p))
        for name, points, expect_near_linear in [
            ("interval_not_subgroup", interval, True),
            ("singleton_below_range", singleton, True),
            ("full_multiplicative_group", full_group, False),
        ]:
            stats = max_additive_ratio(p, points)
            detected = (stats["ratio"] > NEAR_LINEAR_THRESHOLD) == expect_near_linear
            payload["controls"].append(
                {
                    "name": name,
                    "p": p,
                    "size": len(points),
                    "expect_near_linear": expect_near_linear,
                    "detected": detected,
                    **stats,
                }
            )
            payload["summary"]["controls_total"] += 1
            payload["summary"]["controls_detected"] += 1 if detected else 0
        checkpoint(payload)

    payload["finished_at_unix"] = time.time()
    payload["wall_seconds"] = round(time.monotonic() - started, 6)
    checkpoint(payload)
    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    return 0 if (
        payload["summary"]["near_linear_failures"] == 0
        and payload["summary"]["controls_detected"] == payload["summary"]["controls_total"]
    ) else 1


if __name__ == "__main__":
    raise SystemExit(main())

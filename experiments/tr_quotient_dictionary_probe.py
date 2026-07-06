#!/usr/bin/env python3
"""TR quotient-row dictionary stress probe.

The amber seam is:

    stable per-character upstairs agreement
        <-> same-rate quotient-row exact-list agreement.

This script enumerates small quotient polynomial spaces exactly and checks that
agreement-support histograms transport fiber-by-fiber.  It also includes
negative controls for the two load-bearing hypotheses: stable fibers and a
fixed character.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
import sys
import time
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "experiments" / "amber_stress" / "tr_quotient_dictionary_probe_results.json"


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
    zeta = pow(primitive_root(p), (p - 1) // n, p)
    values = [pow(zeta, i, p) for i in range(n)]
    if len(set(values)) != n:
        raise AssertionError("subgroup generator has wrong order")
    return values


def poly_eval(coeffs: tuple[int, ...], x: int, p: int) -> int:
    value = 0
    for c in reversed(coeffs):
        value = (value * x + c) % p
    return value


def quotient_data(p: int, n: int, m: int) -> tuple[list[int], list[int], dict[int, list[int]], dict[int, int]]:
    h = subgroup(p, n)
    quotient = sorted({pow(x, m, p) for x in h})
    if len(quotient) != n // m:
        raise AssertionError((p, n, m, len(quotient), n // m))
    fibers = {y: [] for y in quotient}
    for x in h:
        fibers[pow(x, m, p)].append(x)
    if any(len(xs) != m for xs in fibers.values()):
        raise AssertionError("quotient map has nonuniform fibers")
    index = {y: i for i, y in enumerate(quotient)}
    return h, quotient, fibers, index


def word_values(kind: str, quotient: list[int], p: int, rng: random.Random) -> dict[int, int]:
    if kind == "zero":
        return {y: 0 for y in quotient}
    if kind == "constant":
        return {y: 1 for y in quotient}
    if kind == "linear":
        return {y: (3 + 5 * y) % p for y in quotient}
    if kind == "quadratic":
        return {y: (7 + 2 * y + 11 * y * y) % p for y in quotient}
    if kind == "random":
        return {y: rng.randrange(p) for y in quotient}
    raise ValueError(kind)


def coeff_iterator(p: int, kq: int):
    return itertools.product(range(p), repeat=kq)


def mask_down(coeffs: tuple[int, ...], word_q: dict[int, int], quotient: list[int], p: int) -> int:
    mask = 0
    for i, y in enumerate(quotient):
        if poly_eval(coeffs, y, p) == word_q[y]:
            mask |= 1 << i
    return mask


def mask_up_stable(
    coeffs: tuple[int, ...],
    word_q: dict[int, int],
    h: list[int],
    quotient_index: dict[int, int],
    p: int,
    m: int,
    r: int,
) -> tuple[int, bool]:
    quotient_mask = 0
    fiberwise = True
    by_fiber: dict[int, set[int]] = {}
    for x in h:
        y = pow(x, m, p)
        lhs = pow(x, r, p) * poly_eval(coeffs, y, p) % p
        rhs = pow(x, r, p) * word_q[y] % p
        bit = 1 if lhs == rhs else 0
        by_fiber.setdefault(y, set()).add(bit)
    for y, bits in by_fiber.items():
        if len(bits) != 1:
            fiberwise = False
        elif 1 in bits:
            quotient_mask |= 1 << quotient_index[y]
    return quotient_mask, fiberwise


def mask_up_unstable(
    coeffs: tuple[int, ...],
    word_up: dict[int, int],
    h: list[int],
    quotient_index: dict[int, int],
    p: int,
    m: int,
    r: int,
) -> tuple[int, bool]:
    quotient_mask = 0
    fiberwise = True
    by_fiber: dict[int, set[int]] = {}
    for x in h:
        y = pow(x, m, p)
        lhs = pow(x, r, p) * poly_eval(coeffs, y, p) % p
        bit = 1 if lhs == word_up[x] else 0
        by_fiber.setdefault(y, set()).add(bit)
    for y, bits in by_fiber.items():
        if len(bits) != 1:
            fiberwise = False
        elif 1 in bits:
            quotient_mask |= 1 << quotient_index[y]
    return quotient_mask, fiberwise


def sample_coefficients(p: int, kq: int, rng: random.Random, limit: int = 96) -> list[tuple[int, ...]]:
    samples = [tuple([0] * kq), tuple([1] + [0] * (kq - 1))]
    for i in range(min(p, limit // 4)):
        coeff = [0] * kq
        coeff[0] = i
        samples.append(tuple(coeff))
    while len(samples) < limit:
        samples.append(tuple(rng.randrange(p) for _ in range(kq)))
    seen = set()
    out = []
    for coeffs in samples:
        if coeffs not in seen:
            seen.add(coeffs)
            out.append(coeffs)
    return out


def scan_case(spec: dict[str, Any], rng: random.Random, deadline: float) -> dict[str, Any]:
    p = spec["p"]
    n = spec["n"]
    m = spec["M"]
    kq = spec["kq"]
    h, quotient, fibers, q_index = quotient_data(p, n, m)

    word_kinds = spec["words"]
    chars = list(range(m)) if spec.get("all_chars", True) else spec.get("chars", [0])
    coeff_samples = sample_coefficients(p, kq, rng, spec.get("direct_sample_limit", 96))

    total_coeffs = p**kq
    histograms: dict[str, dict[int, int]] = {}
    direct_checks = 0
    support_mismatches = []
    partial = False

    for word_kind in word_kinds:
        word_q = word_values(word_kind, quotient, p, rng)
        hist: dict[int, int] = {}
        threshold_counts = {a: 0 for a in range(len(quotient) + 1)}
        for coeffs in coeff_iterator(p, kq):
            mask = mask_down(coeffs, word_q, quotient, p)
            hist[mask] = hist.get(mask, 0) + 1
            agree = mask.bit_count()
            for a in range(agree + 1):
                threshold_counts[a] += 1
            if time.monotonic() >= deadline:
                partial = True
                break
        if partial:
            break
        if sum(hist.values()) != total_coeffs:
            raise AssertionError((spec["name"], word_kind, sum(hist.values()), total_coeffs))
        histograms[word_kind] = hist

        for r in chars:
            for coeffs in coeff_samples:
                down = mask_down(coeffs, word_q, quotient, p)
                up, fiberwise = mask_up_stable(coeffs, word_q, h, q_index, p, m, r)
                direct_checks += 1
                if up != down or not fiberwise:
                    support_mismatches.append(
                        {
                            "word": word_kind,
                            "r": r,
                            "coeffs": coeffs,
                            "down_mask": down,
                            "up_mask": up,
                            "fiberwise": fiberwise,
                        }
                    )

        # Histogram-level threshold transport is exact because each quotient
        # agreement bit becomes exactly M upstairs agreement points.
        threshold_failures = [
            a
            for a in range(len(quotient) + 1)
            if threshold_counts[a] != sum(count for mask, count in hist.items() if m * mask.bit_count() >= m * a)
        ]
        if threshold_failures:
            support_mismatches.append({"word": word_kind, "threshold_failures": threshold_failures})

    negative_controls = []
    zero_coeffs = tuple([0] * kq)
    zero_word_q = word_values("zero", quotient, p, rng)
    r = 1 if m > 1 else 0
    stable_zero_up = {x: pow(x, r, p) * zero_word_q[pow(x, m, p)] % p for x in h}
    x0 = fibers[quotient[0]][0]
    broken_up = dict(stable_zero_up)
    broken_up[x0] = (broken_up[x0] + 1) % p
    _, fiberwise = mask_up_unstable(zero_coeffs, broken_up, h, q_index, p, m, r)
    negative_controls.append({"name": "single_point_fiber_break", "detected": not fiberwise})

    one_coeffs = tuple([1] + [0] * (kq - 1))
    word_q = word_values("constant", quotient, p, rng)
    s = 1 if m > 1 else 0
    mismatched_char_word = {x: pow(x, s, p) * word_q[pow(x, m, p)] % p for x in h}
    _, fiberwise = mask_up_unstable(one_coeffs, mismatched_char_word, h, q_index, p, m, 0)
    negative_controls.append({"name": "wrong_character_twist", "detected": not fiberwise})

    return {
        "name": spec["name"],
        "p": p,
        "n": n,
        "M": m,
        "kq": kq,
        "quotient_size": len(quotient),
        "words": word_kinds,
        "characters_checked": chars,
        "total_coefficients_per_word": total_coeffs,
        "histogram_masks": {word: len(hist) for word, hist in histograms.items()},
        "direct_upstairs_checks": direct_checks,
        "support_mismatches": support_mismatches[:5],
        "negative_controls": negative_controls,
        "partial": partial,
    }


def planned_cases() -> list[dict[str, Any]]:
    return [
        {
            "name": "mu12_M3_quadratic_words",
            "p": 97,
            "n": 12,
            "M": 3,
            "kq": 2,
            "words": ["linear", "quadratic", "random"],
            "all_chars": True,
        },
        {
            "name": "mu16_M4_random_words",
            "p": 193,
            "n": 16,
            "M": 4,
            "kq": 2,
            "words": ["linear", "random"],
            "all_chars": True,
        },
        {
            "name": "mu24_M6_cubic_smallquot",
            "p": 97,
            "n": 24,
            "M": 6,
            "kq": 3,
            "words": ["linear", "random"],
            "all_chars": True,
            "direct_sample_limit": 64,
        },
        {
            "name": "mu32_M8_quadratic_smallquot",
            "p": 193,
            "n": 32,
            "M": 8,
            "kq": 2,
            "words": ["quadratic", "random"],
            "all_chars": True,
        },
    ]


def summarize(results: dict[str, Any]) -> None:
    cases = results.get("cases", [])
    failures = []
    for case in cases:
        if case.get("partial"):
            failures.append({"case": case["name"], "reason": "partial"})
        if case.get("support_mismatches"):
            failures.append({"case": case["name"], "reason": "support_mismatch", "items": case["support_mismatches"]})
        for control in case.get("negative_controls", []):
            if not control.get("detected"):
                failures.append({"case": case["name"], "reason": "missed_negative_control", "control": control})
    results["summary"] = {
        "status": "FAIL" if failures else "PASS",
        "cases_checked": len(cases),
        "total_coefficients_enumerated": sum(
            c["total_coefficients_per_word"] * len(c["words"]) for c in cases if not c.get("partial")
        ),
        "direct_upstairs_checks": sum(c.get("direct_upstairs_checks", 0) for c in cases),
        "negative_controls_detected": sum(
            1 for c in cases for control in c.get("negative_controls", []) if control.get("detected")
        ),
        "negative_controls_total": sum(len(c.get("negative_controls", [])) for c in cases),
        "failures": failures,
    }


def checkpoint(results: dict[str, Any]) -> None:
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-limit", type=float, default=55.0)
    parser.add_argument("--seed", type=int, default=20260706)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    deadline = time.monotonic() + args.time_limit
    results: dict[str, Any] = {
        "started_at_unix": time.time(),
        "node": "tr_perleaf_list_ident",
        "seed": args.seed,
        "time_limit_seconds": args.time_limit,
        "cases": [],
    }
    checkpoint(results)
    for spec in planned_cases():
        if time.monotonic() + 2.0 >= deadline:
            break
        t0 = time.monotonic()
        case = scan_case(spec, rng, deadline)
        case["wall_seconds"] = round(time.monotonic() - t0, 6)
        results["cases"].append(case)
        summarize(results)
        checkpoint(results)
        if case.get("partial"):
            break
    results["finished_at_unix"] = time.time()
    summarize(results)
    checkpoint(results)
    print(json.dumps(results["summary"], indent=2, sort_keys=True))
    if results["summary"]["status"] == "PASS":
        print("PASS: TR quotient dictionary probe found no stable-transport mismatch")
    else:
        print("FAIL: TR quotient dictionary probe found an alarm")
    return 0 if results["summary"]["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

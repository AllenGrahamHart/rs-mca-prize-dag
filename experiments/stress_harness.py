#!/usr/bin/env python3
"""Light adversarial stress tests for amber-node claims.

The harness is deliberately small enough for WSL.  It checkpoints JSON after
each subtest so a timeout still leaves partial evidence.
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
OUT = ROOT / "experiments" / "amber_stress" / "results.json"


def inv_mod(x: int, p: int) -> int:
    return pow(x % p, -1, p)


def factor_int(n: int) -> list[int]:
    factors: list[int] = []
    d = 2
    value = n
    while d * d <= value:
        if value % d == 0:
            factors.append(d)
            while value % d == 0:
                value //= d
        d += 1
    if value > 1:
        factors.append(value)
    return factors


def primitive_root(p: int) -> int:
    factors = factor_int(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // f, p) != 1 for f in factors):
            return g
    raise ValueError(f"no primitive root for {p}")


def subgroup(p: int, n: int) -> list[int]:
    if (p - 1) % n:
        raise ValueError(f"{n=} does not divide {p - 1=}")
    g = pow(primitive_root(p), (p - 1) // n, p)
    vals = [pow(g, i, p) for i in range(n)]
    if len(set(vals)) != n:
        raise AssertionError("subgroup generator has wrong order")
    return vals


def poly_eval(coeffs: tuple[int, ...], x: int, p: int) -> int:
    value = 0
    for c in reversed(coeffs):
        value = (value * x + c) % p
    return value


def locator(roots: list[int], p: int) -> tuple[int, ...]:
    poly = [1]
    for root in roots:
        new = [0] * (len(poly) + 1)
        for i, c in enumerate(poly):
            new[i] = (new[i] - c * root) % p
            new[i + 1] = (new[i + 1] + c) % p
        poly = new
    while poly and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def checkpoint(results: dict[str, Any]) -> None:
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")


def test_tr_perleaf_dictionary(rng: random.Random) -> dict[str, Any]:
    """Exact quotient/lift count equality for stable character-form words."""

    cases = [
        {"p": 97, "n": 12, "M": 3, "kq": 2, "trials": 5},
        {"p": 193, "n": 16, "M": 4, "kq": 2, "trials": 5},
    ]
    checked = 0
    negative_controls = 0
    examples: list[dict[str, Any]] = []

    for case in cases:
        p = case["p"]
        n = case["n"]
        M = case["M"]
        kq = case["kq"]
        H = subgroup(p, n)
        quotient = sorted({pow(x, M, p) for x in H})
        if len(quotient) != n // M:
            raise AssertionError((case, len(quotient), n // M))
        polynomials = list(itertools.product(range(p), repeat=kq))
        for trial in range(case["trials"]):
            if trial == 0:
                # A positive-control word with a guaranteed nonempty list.
                word_q = {y: (3 + 5 * y) % p for y in quotient}
            else:
                word_q = {y: rng.randrange(p) for y in quotient}
            threshold_q = max(1, len(quotient) - 1)
            count_q = 0
            by_poly: dict[tuple[int, ...], int] = {}
            for coeffs in polynomials:
                agree_q = sum(poly_eval(coeffs, y, p) == word_q[y] for y in quotient)
                by_poly[coeffs] = agree_q
                if agree_q >= threshold_q:
                    count_q += 1

            for r in range(M):
                count_up = 0
                for coeffs, agree_q in by_poly.items():
                    agree_up = 0
                    for x in H:
                        y = pow(x, M, p)
                        lhs = pow(x, r, p) * poly_eval(coeffs, y, p) % p
                        rhs = pow(x, r, p) * word_q[y] % p
                        if lhs == rhs:
                            agree_up += 1
                    if agree_up != M * agree_q:
                        raise AssertionError(
                            {
                                "case": case,
                                "trial": trial,
                                "r": r,
                                "coeffs": coeffs,
                                "agree_q": agree_q,
                                "agree_up": agree_up,
                            }
                        )
                    if agree_up >= M * threshold_q:
                        count_up += 1
                if count_up != count_q:
                    raise AssertionError((case, trial, r, count_q, count_up))
                checked += len(polynomials)
                examples.append(
                    {
                        "p": p,
                        "n": n,
                        "M": M,
                        "r": r,
                        "trial": trial,
                        "threshold_q": threshold_q,
                        "list_count": count_q,
                    }
                )

            # Negative control: start from an all-zero stable word, then break
            # one point in a fiber.  The dictionary should no longer behave
            # fiberwise for the zero quotient polynomial.
            r = 1 if M > 1 else 0
            x0 = H[0]
            zero_word_q = {y: 0 for y in quotient}
            broken_word = {
                x: pow(x, r, p) * zero_word_q[pow(x, M, p)] % p
                for x in H
            }
            broken_word[x0] = (broken_word[x0] + 1) % p
            coeffs = polynomials[0]
            agreements_by_fiber: dict[int, set[int]] = {}
            for x in H:
                y = pow(x, M, p)
                lhs = pow(x, r, p) * poly_eval(coeffs, y, p) % p
                agreements_by_fiber.setdefault(y, set()).add(1 if lhs == broken_word[x] else 0)
            if any(len(vals) > 1 for vals in agreements_by_fiber.values()):
                negative_controls += 1

    return {
        "status": "PASS",
        "node": "tr_perleaf_list_ident",
        "checked_lifted_polynomial_agreements": checked,
        "negative_controls_nonstable_detected": negative_controls,
        "sample_examples": examples[:8],
    }


def test_moment_trade_witness() -> dict[str, Any]:
    """Recompute the primitive moment-null witness in moment_trade_staircase."""

    p = 193
    base = 11
    exponents = [0, 1, 2, 4, 16, 45, 50, 60]
    block = [pow(base, e, p) for e in exponents]
    mu64 = set(subgroup(p, 64))
    if any(x not in mu64 for x in block):
        raise AssertionError("block is not contained in mu_64")
    power_sums = {r: sum(pow(x, r, p) for x in block) % p for r in range(1, 5)}
    if [power_sums[r] for r in (1, 2, 3)] != [0, 0, 0]:
        raise AssertionError(power_sums)
    loc = locator(block, p)
    degree = len(block)
    top_subleading = {
        i: loc[degree - i] % p
        for i in range(1, 4)
    }
    if any(v != 0 for v in top_subleading.values()):
        raise AssertionError(top_subleading)

    rotations = []
    reflections = []
    B = set(block)
    for z in mu64:
        if {z * x % p for x in B} == B:
            rotations.append(z)
        if {z * inv_mod(x, p) % p for x in B} == B:
            reflections.append(z)
    nontrivial_rot = [z for z in rotations if z != 1]
    if nontrivial_rot or reflections:
        raise AssertionError({"rotations": rotations, "reflections": reflections})

    return {
        "status": "PASS",
        "node": "moment_trade_staircase / x4_exactlist_staircase_split",
        "p": p,
        "base": base,
        "exponents": exponents,
        "power_sums_r1_to_r4": power_sums,
        "top_3_subleading_locator_coeffs": top_subleading,
        "rotation_stabilizers": rotations,
        "reflection_stabilizers": reflections,
    }


def test_e22_local_gate() -> dict[str, Any]:
    """Re-run the E22 local challenger gate as a callable subtest."""

    core = ROOT / "nodes" / "worst_word_challenger_pricing" / "notes"
    sys.path.insert(0, str(core))
    from e22_core import exact_cell_census  # type: ignore

    sigma1 = []
    for k in (1, 2, 4, 8):
        cell = exact_cell_census(16, k, 1, "cyclic_step_1", "linear")
        sigma1.append(cell)
    controls = []
    for k in (2, 4, 8):
        controls.append(exact_cell_census(16, k, 2, "cyclic_step_1", "linear"))

    if not all(c["unclassified"] == 0 for c in sigma1 + controls):
        raise AssertionError("unclassified third class found", sigma1, controls)
    if not all(c["classified_challenger"] > 0 and c["beats_planted"] for c in sigma1 if c["k"] in (2, 4, 8)):
        raise AssertionError("expected E15 challenger not reproduced")
    if any(c["classified_challenger"] for c in controls):
        raise AssertionError("sigma=2 control produced challenger")

    return {
        "status": "PASS",
        "node": "worst_word_planted / worst_word_challenger_pricing",
        "sigma1": [
            {
                "k": c["k"],
                "list_size": c["list_size"],
                "planted_count": c["planted_count"],
                "classified_challenger": c["classified_challenger"],
                "unclassified": c["unclassified"],
                "beats_planted": c["beats_planted"],
                "class_counts": c["class_counts"],
            }
            for c in sigma1
        ],
        "sigma2_controls": [
            {
                "k": c["k"],
                "list_size": c["list_size"],
                "planted_count": c["planted_count"],
                "classified_challenger": c["classified_challenger"],
                "unclassified": c["unclassified"],
                "beats_planted": c["beats_planted"],
            }
            for c in controls
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-limit", type=float, default=55.0)
    parser.add_argument("--seed", type=int, default=20260706)
    args = parser.parse_args()

    start = time.monotonic()
    rng = random.Random(args.seed)
    results: dict[str, Any] = {
        "started_at_unix": time.time(),
        "time_limit_seconds": args.time_limit,
        "seed": args.seed,
        "tests": {},
    }
    checkpoint(results)

    tests = [
        ("tr_perleaf_dictionary", lambda: test_tr_perleaf_dictionary(rng)),
        ("moment_trade_witness", test_moment_trade_witness),
        ("e22_local_gate", test_e22_local_gate),
    ]
    for name, fn in tests:
        if time.monotonic() - start > args.time_limit:
            results["tests"][name] = {"status": "SKIPPED_TIMEOUT_BUDGET"}
            checkpoint(results)
            break
        t0 = time.monotonic()
        try:
            item = fn()
            item["wall_seconds"] = round(time.monotonic() - t0, 6)
            results["tests"][name] = item
        except Exception as exc:  # checkpoint falsifier details before raising
            results["tests"][name] = {
                "status": "FAIL",
                "error": repr(exc),
                "wall_seconds": round(time.monotonic() - t0, 6),
            }
            checkpoint(results)
            raise
        checkpoint(results)

    results["finished_at_unix"] = time.time()
    results["total_wall_seconds"] = round(time.monotonic() - start, 6)
    checkpoint(results)
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

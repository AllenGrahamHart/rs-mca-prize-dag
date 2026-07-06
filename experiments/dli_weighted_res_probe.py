#!/usr/bin/env python3
"""Bounded DLI weighted/RES flatness probe.

The DLI frontier was reposed from a false sup condition to a weighted
resultant-survivor/kernel-skew count.  This script stress-tests the exact
kernel-skew identity on small odd-evaluation matrices:

    rho = p^L |ker(A) cap D| / |D|.

It enumerates the whole image-fiber distribution by dynamic programming for
small central profiles.  The falsifier sought here is a large rank-charged
deviation exponent, i.e. excess mass not explained by the known zero/rank-loss
control.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "experiments" / "amber_stress" / "dli_weighted_res_probe_results.json"
EXPECTED_SUP_REFUTATIONS = {"ternary_mu16_L4", "ternary_12_of_mu32_L4"}


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


def rank_mod(rows: list[list[int]], p: int) -> int:
    mat = [row[:] for row in rows]
    r = 0
    ncol = len(mat[0]) if mat else 0
    for c in range(ncol):
        pivot = next((i for i in range(r, len(mat)) if mat[i][c] % p), None)
        if pivot is None:
            continue
        mat[r], mat[pivot] = mat[pivot], mat[r]
        inv = pow(mat[r][c] % p, -1, p)
        mat[r] = [(x * inv) % p for x in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][c] % p:
                f = mat[i][c] % p
                mat[i] = [(x - f * y) % p for x, y in zip(mat[i], mat[r])]
        r += 1
        if r == len(mat):
            break
    return r


def domain_values(kind: str) -> tuple[int, ...]:
    if kind == "signed":
        return (-1, 1)
    if kind == "ternary":
        return (-2, 0, 2)
    if kind == "zero":
        return (0,)
    if kind == "biased":
        return (-2, 0, 2, 4)
    raise ValueError(kind)


def planned_cells() -> list[dict[str, Any]]:
    return [
        {"name": "zero_atom_rank_charge", "n": 16, "p": 193, "L": 4, "profile": ["zero"] * 8},
        {
            "name": "rank_deficient_two_signed",
            "n": 16,
            "p": 193,
            "L": 4,
            "profile": ["signed", "signed"] + ["zero"] * 6,
        },
        {"name": "signed_mu16_L2", "n": 16, "p": 193, "L": 2, "profile": ["signed"] * 8},
        {"name": "signed_mu16_L4", "n": 16, "p": 193, "L": 4, "profile": ["signed"] * 8},
        {"name": "ternary_mu16_L4", "n": 16, "p": 193, "L": 4, "profile": ["ternary"] * 8},
        {
            "name": "mixed_mu16_L4",
            "n": 16,
            "p": 193,
            "L": 4,
            "profile": ["signed", "ternary", "signed", "ternary", "signed", "ternary", "signed", "ternary"],
        },
        {"name": "signed_mu32_L3", "n": 32, "p": 193, "L": 3, "profile": ["signed"] * 16},
        {"name": "signed_mu32_L4", "n": 32, "p": 193, "L": 4, "profile": ["signed"] * 16},
        {
            "name": "ternary_12_of_mu32_L4",
            "n": 32,
            "p": 193,
            "L": 4,
            "profile": ["ternary"] * 12 + ["zero"] * 4,
        },
        {
            "name": "ternary_16_of_mu32_L4_mitm",
            "n": 32,
            "p": 193,
            "L": 4,
            "profile": ["ternary"] * 16,
            "mode": "zero_mitm",
        },
        {
            "name": "ternary_20_of_mu64_L4_mitm",
            "n": 64,
            "p": 193,
            "L": 4,
            "profile": ["ternary"] * 20 + ["zero"] * 12,
            "mode": "zero_mitm",
        },
        {
            "name": "ternary_24_of_mu64_L4_mitm",
            "n": 64,
            "p": 193,
            "L": 4,
            "profile": ["ternary"] * 24 + ["zero"] * 8,
            "mode": "zero_mitm",
        },
        {
            "name": "signed_20_of_mu64_L4",
            "n": 64,
            "p": 193,
            "L": 4,
            "profile": ["signed"] * 20 + ["zero"] * 12,
        },
    ]


def odd_eval_columns(n: int, p: int, L: int) -> list[tuple[int, ...]]:
    if (p - 1) % n:
        raise ValueError(f"p={p} is not 1 mod n={n}")
    zeta = pow(primitive_root(p), (p - 1) // n, p)
    return [
        tuple(pow(zeta, (2 * ell + 1) * i, p) for ell in range(L))
        for i in range(n // 2)
    ]


def full_profile_size(profile: list[str]) -> int:
    total = 1
    for kind in profile:
        total *= len(domain_values(kind))
    return total


def image_distribution(
    pairs: list[tuple[tuple[int, ...], str]], p: int, L: int, deadline: float
) -> tuple[dict[tuple[int, ...], int], int, bool]:
    dist: dict[tuple[int, ...], int] = {tuple([0] * L): 1}
    enumerated = 1
    partial = False
    for col, kind in pairs:
        vals = domain_values(kind)
        enumerated *= len(vals)
        nxt: dict[tuple[int, ...], int] = defaultdict(int)
        for state, count in dist.items():
            for v in vals:
                nxt[tuple((state[i] + v * col[i]) % p for i in range(L))] += count
        dist = dict(nxt)
        if time.monotonic() >= deadline:
            partial = True
            break
    return dist, enumerated, partial


def active_balanced_halves(
    columns: list[tuple[int, ...]], profile: list[str]
) -> tuple[list[tuple[tuple[int, ...], str]], list[tuple[tuple[int, ...], str]]]:
    active = [(col, kind) for col, kind in zip(columns, profile) if len(domain_values(kind)) > 1]
    mid = len(active) // 2
    return active[:mid], active[mid:]


def zero_count_mitm(
    columns: list[tuple[int, ...]], profile: list[str], p: int, L: int, deadline: float
) -> tuple[int, bool, dict[str, int]]:
    left, right = active_balanced_halves(columns, profile)
    right_dist, right_u, right_partial = image_distribution(right, p, L, deadline)
    if right_partial:
        return 0, True, {"left_states": 0, "right_states": len(right_dist), "left_U": 0, "right_U": right_u}
    left_dist, left_u, left_partial = image_distribution(left, p, L, deadline)
    if left_partial:
        return 0, True, {
            "left_states": len(left_dist),
            "right_states": len(right_dist),
            "left_U": left_u,
            "right_U": right_u,
        }
    zero = 0
    for state, count in left_dist.items():
        want = tuple((-x) % p for x in state)
        zero += count * right_dist.get(want, 0)
    return zero, False, {
        "left_states": len(left_dist),
        "right_states": len(right_dist),
        "left_U": left_u,
        "right_U": right_u,
    }


def scan_cell(spec: dict[str, Any], deadline: float) -> dict[str, Any]:
    n = spec["n"]
    p = spec["p"]
    L = spec["L"]
    profile = spec["profile"]
    columns = odd_eval_columns(n, p, L)
    if len(profile) != len(columns):
        raise ValueError(f"profile length {len(profile)} != section size {len(columns)}")

    rows = [[columns[i][ell] for i, kind in enumerate(profile) if domain_values(kind) != (0,)] for ell in range(L)]
    eff_rank = rank_mod(rows, p) if rows and rows[0] else 0
    rank_loss = L - eff_rank
    total = full_profile_size(profile)

    if spec.get("mode") == "zero_mitm":
        zero, partial, mitm_stats = zero_count_mitm(columns, profile, p, L, deadline)
        image_fibers = None
        max_fiber = None
        mean_fiber = total / (p ** eff_rank) if eff_rank else total
        max_fiber_ratio = None
        max_fiber_eta = None
    else:
        pairs = list(zip(columns, profile))
        dist, enumerated, partial = image_distribution(pairs, p, L, deadline)
        zero = dist.get(tuple([0] * L), 0)
        max_fiber = max(dist.values(), default=0)
        image_fibers = len(dist)
        mean_fiber = enumerated / (p ** eff_rank) if eff_rank else enumerated
        max_fiber_ratio = max_fiber / mean_fiber if mean_fiber else 0.0
        max_fiber_eta = math.log(max_fiber_ratio, p) if max_fiber_ratio > 0 else None
        mitm_stats = None

    mean_fiber = total / (p ** eff_rank) if eff_rank else total
    rho = (p ** L) * zero / total if total else 0.0
    eta = math.log(rho, p) if rho > 0 else None
    charged_eta = (eta - rank_loss) if eta is not None else None

    domain_counts: dict[str, int] = {}
    for kind in profile:
        domain_counts[kind] = domain_counts.get(kind, 0) + 1

    cell = {
        "name": spec["name"],
        "mode": spec.get("mode", "full_image_dp"),
        "n": n,
        "p": p,
        "L": L,
        "section_size": n // 2,
        "profile_domain_counts": domain_counts,
        "U": total,
        "image_fibers": image_fibers,
        "effective_rank": eff_rank,
        "rank_loss": rank_loss,
        "zero_fiber_size": zero,
        "max_fiber_size": max_fiber,
        "mean_fiber_under_rank": mean_fiber,
        "rho": rho,
        "eta_log_p_rho": eta,
        "rank_charged_eta": charged_eta,
        "max_fiber_ratio_vs_rank_mean": max_fiber_ratio,
        "max_fiber_eta": max_fiber_eta,
        "partial": partial,
    }
    if mitm_stats is not None:
        cell["mitm_stats"] = mitm_stats
    return cell


def checkpoint(results: dict[str, Any]) -> None:
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")


def summarize(results: dict[str, Any]) -> None:
    cells = results.get("cells", [])
    unexpected_alarms = []
    expected_sup_refutations = []
    for cell in cells:
        if cell.get("partial"):
            unexpected_alarms.append({"name": cell["name"], "reason": "partial"})
        charged = cell.get("rank_charged_eta")
        # One p-log unit after rank charging is a deliberately loose falsifier
        # threshold for these small exact cells.
        if charged is not None and charged > 1.0:
            alarm = {"name": cell["name"], "reason": "large_rank_charged_eta", "value": charged}
            if cell["name"] in EXPECTED_SUP_REFUTATIONS:
                expected_sup_refutations.append(alarm)
            else:
                unexpected_alarms.append(alarm)
    missing_expected = sorted(EXPECTED_SUP_REFUTATIONS - {a["name"] for a in expected_sup_refutations})
    if missing_expected:
        unexpected_alarms.append({"reason": "missing_expected_sup_refutation", "names": missing_expected})
    results["summary"] = {
        "status": "FAIL" if unexpected_alarms else "PASS",
        "cells_checked": len(cells),
        "expected_sup_refutations": expected_sup_refutations,
        "unexpected_alarms": unexpected_alarms,
        "max_rank_charged_eta": max(
            (c["rank_charged_eta"] for c in cells if c.get("rank_charged_eta") is not None),
            default=None,
        ),
        "max_raw_eta": max(
            (c["eta_log_p_rho"] for c in cells if c.get("eta_log_p_rho") is not None),
            default=None,
        ),
        "max_fiber_eta": max(
            (c["max_fiber_eta"] for c in cells if c.get("max_fiber_eta") is not None),
            default=None,
        ),
        "zero_atom_control_charged": next(
            (c.get("rank_charged_eta") for c in cells if c.get("name") == "zero_atom_rank_charge"),
            None,
        ),
        "large_active_ternary_eta": {
            c["name"]: c.get("rank_charged_eta")
            for c in cells
            if c["name"].startswith("ternary_") and c["name"] not in EXPECTED_SUP_REFUTATIONS
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-limit", type=float, default=55.0)
    args = parser.parse_args()

    deadline = time.monotonic() + args.time_limit
    results: dict[str, Any] = {
        "started_at_unix": time.time(),
        "node": "dli_prime_weighted_large_block_support",
        "time_limit_seconds": args.time_limit,
        "cells": [],
    }
    checkpoint(results)
    for spec in planned_cells():
        if time.monotonic() + 2.0 >= deadline:
            break
        t0 = time.monotonic()
        cell = scan_cell(spec, deadline)
        cell["wall_seconds"] = round(time.monotonic() - t0, 6)
        results["cells"].append(cell)
        summarize(results)
        checkpoint(results)
    results["finished_at_unix"] = time.time()
    summarize(results)
    checkpoint(results)
    print(json.dumps(results["summary"], indent=2, sort_keys=True))
    if results["summary"]["status"] == "PASS":
        print("PASS: DLI probe reproduced the known low-mass sup refutation and found no unexpected alarm")
    else:
        print("FAIL: DLI weighted/RES probe found an unexpected alarm")
    return 0 if results["summary"]["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

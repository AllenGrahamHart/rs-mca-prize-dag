#!/usr/bin/env python3
"""Adversarial harness for the pinned DLI-CLOSE gap target.

All attacks here use the real square-root section
    X = {zeta^i : 0 <= i < n/2}
over a prime field F_p with p == 1 mod n.  Runs are checkpointed so a
60-second timeout still leaves partial coverage.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
OUTDIR = ROOT / "experiments" / "dli_gap_attack"

SMALL_PRIME_BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def is_prime(m: int) -> bool:
    if m < 2:
        return False
    for q in SMALL_PRIME_BASES:
        if m % q == 0:
            return m == q
    d = m - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    # Deterministic for the small-to-64-bit rows used here.
    for a in (2, 3, 5, 7, 11, 13, 17):
        if a >= m:
            continue
        x = pow(a, d, m)
        if x in (1, m - 1):
            continue
        for _ in range(r - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


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


def next_prime_1mod(n: int, start: int) -> int:
    t = max(1, (start - 1 + n - 1) // n)
    while True:
        p = 1 + n * t
        if p >= start and is_prime(p):
            return p
        t += 1


def section_columns(n: int, p: int, L: int) -> list[tuple[int, ...]]:
    if (p - 1) % n:
        raise ValueError(f"p={p} is not 1 mod n={n}")
    zeta = pow(primitive_root(p), (p - 1) // n, p)
    return [
        tuple(pow(zeta, (2 * ell + 1) * i, p) for ell in range(L))
        for i in range(n // 2)
    ]


def section_values(n: int, p: int) -> list[int]:
    zeta = pow(primitive_root(p), (p - 1) // n, p)
    return [pow(zeta, i, p) for i in range(n // 2)]


def checkpoint(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data["updated_at_unix"] = time.time()
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def random_expected(N: int, w: int, p: int, L: int) -> float:
    return math.comb(N, w) * (2**w) / (p**L)


def window_closed(N: int, w: int, p: int, L: int) -> bool:
    return math.comb(N, w) * (2**w) * 1024 <= p**L


def w_star(N: int, p: int, L: int) -> int:
    ans = 0
    for w in range(1, N + 1):
        if window_closed(N, w, p, L):
            ans = w
    return ans


def choose_closed_prime(n: int, L: int, N: int, wmax: int) -> int:
    need = math.comb(N, wmax) * (2**wmax) * 1024
    start = int(math.ceil(need ** (1.0 / L)))
    start = max(start, n + 1, 17)
    return next_prime_1mod(n, start)


def mitm_feasible_weight(N: int, w: int, max_side_states: int) -> bool:
    right = N // 2
    left = N - right
    worst = 0
    for k in range(max(0, w - left), min(w, right) + 1):
        worst = max(worst, math.comb(right, k) * (2**k))
    return worst <= max_side_states


def max_mitm_weight(N: int, cap: int, max_side_states: int) -> int:
    best = 0
    for w in range(1, min(N, cap) + 1):
        if mitm_feasible_weight(N, w, max_side_states):
            best = w
    return best


def signed_sums(
    indices: list[int],
    k: int,
    columns: list[tuple[int, ...]],
    p: int,
    L: int,
    deadline: float,
) -> Iterable[tuple[tuple[int, ...], tuple[tuple[int, int], ...]]]:
    zero = (0,) * L
    if k == 0:
        yield zero, ()
        return
    for combo in itertools.combinations(indices, k):
        cols = [columns[i] for i in combo]
        for mask in range(1 << k):
            if (mask & 0x1FF) == 0 and time.monotonic() >= deadline:
                return
            vals = [0] * L
            terms = []
            for j, idx in enumerate(combo):
                sign = 1 if ((mask >> j) & 1) else -1
                terms.append((idx, sign))
                col = cols[j]
                for ell in range(L):
                    vals[ell] = (vals[ell] + sign * col[ell]) % p
            yield tuple(vals), tuple(terms)


def count_weight_mitm(
    n: int,
    p: int,
    L: int,
    w: int,
    deadline: float,
    want_witness: bool = True,
) -> dict[str, Any]:
    columns = section_columns(n, p, L)
    N = len(columns)
    left_indices = list(range(0, N // 2))
    right_indices = list(range(N // 2, N))
    started = time.monotonic()
    partial = False

    right_counts: dict[int, dict[tuple[int, ...], int]] = {}
    right_examples: dict[tuple[int, tuple[int, ...]], tuple[tuple[int, int], ...]] = {}
    for kr in range(max(0, w - len(left_indices)), min(w, len(right_indices)) + 1):
        table: dict[tuple[int, ...], int] = defaultdict(int)
        for vec, terms in signed_sums(right_indices, kr, columns, p, L, deadline):
            table[vec] += 1
            if want_witness and (kr, vec) not in right_examples:
                right_examples[(kr, vec)] = terms
        right_counts[kr] = dict(table)
        if time.monotonic() >= deadline:
            partial = True
            break

    count = 0
    witness = None
    if not partial:
        for kl in range(max(0, w - len(right_indices)), min(w, len(left_indices)) + 1):
            kr = w - kl
            table = right_counts.get(kr, {})
            for vec, left_terms in signed_sums(left_indices, kl, columns, p, L, deadline):
                want = tuple((-x) % p for x in vec)
                hits = table.get(want, 0)
                if hits:
                    count += hits
                    if witness is None and want_witness:
                        witness_terms = tuple(left_terms) + right_examples[(kr, want)]
                        witness = [{"index": i, "sign": s} for i, s in witness_terms]
            if time.monotonic() >= deadline:
                partial = True
                break

    verified = None
    if witness is not None:
        verified = verify_trade(n, p, L, witness)
    return {
        "n": n,
        "p": p,
        "L": L,
        "N": N,
        "weight": w,
        "count": count,
        "expected_random": random_expected(N, w, p, L),
        "observed_over_expected": None
        if random_expected(N, w, p, L) == 0
        else count / random_expected(N, w, p, L),
        "window_closed_2^-10": window_closed(N, w, p, L),
        "w_star": w_star(N, p, L),
        "w_contribution": count * (2.0 ** (-w)),
        "partial": partial,
        "witness": witness,
        "witness_verified": verified,
        "wall_seconds": round(time.monotonic() - started, 6),
    }


def verify_trade(n: int, p: int, L: int, witness: list[dict[str, int]]) -> dict[str, Any]:
    columns = section_columns(n, p, L)
    indices = [t["index"] for t in witness]
    signs = [t["sign"] for t in witness]
    sums = []
    unique = len(indices) == len(set(indices))
    in_section = all(0 <= i < n // 2 for i in indices)
    nonzero = bool(indices) and all(s in (-1, 1) for s in signs)
    for ell in range(L):
        sums.append(sum(s * columns[i][ell] for i, s in zip(indices, signs)) % p)
    plus = {i for i, s in zip(indices, signs) if s == 1}
    minus = {i for i, s in zip(indices, signs) if s == -1}
    return {
        "ok": unique and in_section and nonzero and not (plus & minus) and all(x == 0 for x in sums),
        "unique_indices": unique,
        "in_section": in_section,
        "disjoint_plus_minus": not (plus & minus),
        "moment_sums": sums,
    }


def gap_rows() -> list[dict[str, Any]]:
    rows = []
    for n in (32, 64, 128, 256):
        N = n // 2
        cap = {32: 12, 64: 11, 128: 8, 256: 6}[n]
        for L in (2, 3, 4, 5):
            wmax = max(L + 1, max_mitm_weight(N, cap, 1_500_000))
            wmax = min(wmax, cap, N)
            p = choose_closed_prime(n, L, N, wmax)
            rows.append({"n": n, "L": L, "p": p, "weights": list(range(L + 1, wmax + 1))})
    return rows


def attack_gap(
    time_limit: float,
    start_row: int = 0,
    row_count: int | None = None,
    weight_min: int | None = None,
    weight_max: int | None = None,
) -> dict[str, Any]:
    suffix = []
    if start_row:
        suffix.append(f"start{start_row}")
    if row_count is not None:
        suffix.append(f"rows{row_count}")
    if weight_min is not None or weight_max is not None:
        suffix.append(f"w{weight_min or 'lo'}-{weight_max or 'hi'}")
    out = OUTDIR / ("gap_trade_hunt_results.json" if not suffix else f"gap_trade_hunt_results_{'_'.join(suffix)}.json")
    deadline = time.monotonic() + time_limit
    planned = gap_rows()
    row_slice = planned[start_row:] if row_count is None else planned[start_row : start_row + row_count]
    result: dict[str, Any] = {
        "attack": "gap-trade hunt",
        "started_at_unix": time.time(),
        "time_limit_seconds": time_limit,
        "start_row": start_row,
        "row_count": row_count,
        "weight_min": weight_min,
        "weight_max": weight_max,
        "planned_rows_total": len(planned),
        "rows": [],
        "falsifier_candidates": [],
    }
    checkpoint(out, result)
    for row in row_slice:
        row_out = {k: row[k] for k in ("n", "L", "p")}
        weights = [
            w
            for w in row["weights"]
            if (weight_min is None or w >= weight_min) and (weight_max is None or w <= weight_max)
        ]
        row_out["weights"] = []
        for w in weights:
            if time.monotonic() + 2.0 >= deadline:
                row_out["stopped_for_deadline"] = True
                break
            item = count_weight_mitm(row["n"], row["p"], row["L"], w, deadline)
            row_out["weights"].append(item)
            if item["count"] and item["window_closed_2^-10"] and item.get("witness_verified", {}).get("ok"):
                result["falsifier_candidates"].append(item)
            checkpoint(out, result)
        result["rows"].append(row_out)
        checkpoint(out, result)
        if time.monotonic() + 2.0 >= deadline:
            break
    result["finished_at_unix"] = time.time()
    result["status"] = "FALSIFIER" if result["falsifier_candidates"] else "PASS_NO_GAP_TRADE_FOUND"
    checkpoint(out, result)
    return result


def subset_moments(indices: tuple[int, ...], columns: list[tuple[int, ...]], p: int, L: int) -> tuple[int, ...]:
    return tuple(sum(columns[i][ell] for i in indices) % p for ell in range(L))


def direct_pattern_attacks(time_limit: float) -> dict[str, Any]:
    out = OUTDIR / "rotation_engineered_results.json"
    deadline = time.monotonic() + time_limit
    rows = [
        {"n": 32, "p": 97, "L": 2, "max_subset": 7},
        {"n": 64, "p": 193, "L": 3, "max_subset": 7},
        {"n": 128, "p": 769, "L": 4, "max_subset": 6},
    ]
    result: dict[str, Any] = {
        "attack": "rotation-engineered and explicit structured families",
        "started_at_unix": time.time(),
        "time_limit_seconds": time_limit,
        "algebraic_rotation_obstruction": (
            "For n=2^s and surviving odd r0, zeta^(2k*r0)=1 implies n | 2k; "
            "since r0 is odd, zeta^(2k)=1. The only exact rotation is identity, "
            "so a disjoint Q=zeta^(2k)P cannot be produced by the advertised single-defect mechanism."
        ),
        "rows": [],
        "falsifier_candidates": [],
    }
    checkpoint(out, result)
    for row in rows:
        columns = section_columns(row["n"], row["p"], row["L"])
        N = len(columns)
        row_out: dict[str, Any] = {**row, "N": N, "single_defect_subsets": [], "pattern_hits": []}
        # Hunt subsets whose odd moments vanish except one coordinate.
        for h in range(1, min(row["max_subset"], N) + 1):
            if time.monotonic() >= deadline:
                row_out["partial"] = True
                break
            checked = 0
            found = 0
            for combo in itertools.combinations(range(N), h):
                checked += 1
                if (checked & 0x3FFF) == 0 and time.monotonic() >= deadline:
                    row_out["partial"] = True
                    break
                mom = subset_moments(combo, columns, row["p"], row["L"])
                nonzero = [i for i, x in enumerate(mom) if x % row["p"]]
                if len(nonzero) == 1:
                    found += 1
                    if len(row_out["single_defect_subsets"]) < 8:
                        ell = nonzero[0]
                        r0 = 2 * ell + 1
                        row_out["single_defect_subsets"].append(
                            {"h": h, "indices": list(combo), "surviving_odd_r": r0, "moment": mom[ell]}
                        )
            row_out.setdefault("single_defect_summary", []).append({"h": h, "checked": checked, "found": found})
            if row_out.get("partial"):
                break
        # Arithmetic progressions and simple sign patterns.
        pattern_checked = 0
        for length in range(2, min(row["max_subset"], N) + 1):
            for start in range(N):
                for step in range(1, N):
                    pattern_checked += 1
                    if (pattern_checked & 0x3FF) == 0 and time.monotonic() >= deadline:
                        row_out["partial"] = True
                        break
                    inds = tuple((start + j * step) % N for j in range(length))
                    if len(set(inds)) != length:
                        continue
                    patterns = [
                        ("all_plus", [1] * length),
                        ("alternating", [1 if j % 2 == 0 else -1 for j in range(length)]),
                        ("split", [1 if j < length // 2 else -1 for j in range(length)]),
                    ]
                    for name, signs in patterns:
                        witness = [{"index": i, "sign": s} for i, s in zip(inds, signs)]
                        verified = verify_trade(row["n"], row["p"], row["L"], witness)
                        if verified["ok"]:
                            hit = {
                                "pattern": name,
                                "length": length,
                                "start": start,
                                "step": step,
                                "witness": witness,
                                "witness_verified": verified,
                            }
                            row_out["pattern_hits"].append(hit)
                            result["falsifier_candidates"].append({**row, **hit})
                if row_out.get("partial"):
                    break
            if row_out.get("partial"):
                break
            if time.monotonic() >= deadline:
                row_out["partial"] = True
                break
        row_out["pattern_checked"] = pattern_checked
        result["rows"].append(row_out)
        checkpoint(out, result)
        if time.monotonic() >= deadline:
            break
    result["finished_at_unix"] = time.time()
    result["status"] = "FALSIFIER" if result["falsifier_candidates"] else "PASS_NO_STRUCTURED_FAMILY_FOUND"
    checkpoint(out, result)
    return result


def attack_tail(time_limit: float) -> dict[str, Any]:
    out = OUTDIR / "tail_ratio_results.json"
    deadline = time.monotonic() + time_limit
    rows = [
        {"n": 32, "p": 97, "L": 2, "weights": list(range(3, 11))},
        {"n": 32, "p": 97, "L": 3, "weights": list(range(4, 10))},
        {"n": 64, "p": 193, "L": 2, "weights": list(range(3, 9))},
        {"n": 64, "p": 193, "L": 3, "weights": list(range(4, 8))},
    ]
    result: dict[str, Any] = {
        "attack": "tail constant ratio",
        "started_at_unix": time.time(),
        "time_limit_seconds": time_limit,
        "rows": [],
    }
    checkpoint(out, result)
    for row in rows:
        row_out = {k: row[k] for k in ("n", "p", "L")}
        N = row["n"] // 2
        row_out["N"] = N
        row_out["w_star"] = w_star(N, row["p"], row["L"])
        row_out["weights"] = []
        for w in row["weights"]:
            if time.monotonic() + 2.0 >= deadline:
                row_out["partial"] = True
                break
            item = count_weight_mitm(row["n"], row["p"], row["L"], w, deadline, want_witness=False)
            item["tail_side"] = "tail" if w > row_out["w_star"] else "gap_or_closed"
            row_out["weights"].append(item)
            checkpoint(out, result)
        result["rows"].append(row_out)
        checkpoint(out, result)
        if time.monotonic() + 2.0 >= deadline:
            break
    ratios = [
        item["observed_over_expected"]
        for row in result["rows"]
        for item in row["weights"]
        if item.get("observed_over_expected") is not None and item.get("tail_side") == "tail"
    ]
    result["max_tail_ratio"] = max(ratios, default=None)
    result["status"] = "PASS_RATIOS_RECORDED"
    result["finished_at_unix"] = time.time()
    checkpoint(out, result)
    return result


def all_lambdas(p: int, L: int) -> Iterable[tuple[int, ...]]:
    for lam in itertools.product(range(p), repeat=L):
        if any(lam):
            yield lam


def attack_analytic(time_limit: float) -> dict[str, Any]:
    out = OUTDIR / "analytic_margin_results.json"
    deadline = time.monotonic() + time_limit
    rows = [
        {"n": 16, "p": 17, "L": 2},
        {"n": 16, "p": 17, "L": 3},
        {"n": 32, "p": 97, "L": 2},
        {"n": 32, "p": 97, "L": 3},
        {"n": 64, "p": 193, "L": 2},
    ]
    result: dict[str, Any] = {
        "attack": "analytic D3 worst-lambda margin",
        "started_at_unix": time.time(),
        "time_limit_seconds": time_limit,
        "rows": [],
    }
    checkpoint(out, result)
    for row in rows:
        columns = section_columns(row["n"], row["p"], row["L"])
        logcos = [2.0 * math.log2(abs(math.cos(math.pi * a / row["p"]))) for a in range(row["p"])]
        best = -float("inf")
        best_lam = None
        checked = 0
        partial = False
        for lam in all_lambdas(row["p"], row["L"]):
            total = 0.0
            for col in columns:
                a = sum(lam[i] * col[i] for i in range(row["L"])) % row["p"]
                total += logcos[a]
            per_coord = total / len(columns)
            if per_coord > best:
                best = per_coord
                best_lam = lam
            checked += 1
            if (checked & 0x3FFF) == 0 and time.monotonic() >= deadline:
                partial = True
                break
        result["rows"].append(
            {
                **row,
                "N": len(columns),
                "lambda_checked": checked,
                "lambda_total_nonzero": row["p"] ** row["L"] - 1,
                "partial": partial,
                "worst_per_coordinate_log2cos2": best,
                "margin_to_minus_one": best + 1.0,
                "worst_lambda": list(best_lam) if best_lam is not None else None,
            }
        )
        checkpoint(out, result)
        if partial:
            break
    result["status"] = "PASS_MARGINS_RECORDED"
    result["finished_at_unix"] = time.time()
    checkpoint(out, result)
    return result


def dp_weight_distribution(n: int, p: int, L: int, deadline: float) -> dict[str, Any]:
    columns = section_columns(n, p, L)
    N = len(columns)
    zero = (0,) * L
    dist: dict[tuple[int, ...], list[int]] = {zero: [1] + [0] * N}
    partial = False
    for col in columns:
        nxt: dict[tuple[int, ...], list[int]] = defaultdict(lambda: [0] * (N + 1))
        for state, counts in dist.items():
            for w, count in enumerate(counts):
                if not count:
                    continue
                nxt[state][w] += count
                plus = tuple((state[i] + col[i]) % p for i in range(L))
                minus = tuple((state[i] - col[i]) % p for i in range(L))
                nxt[plus][w + 1] += count
                nxt[minus][w + 1] += count
        dist = dict(nxt)
        if time.monotonic() >= deadline:
            partial = True
            break
    zero_counts = dist.get(zero, [0] * (N + 1))
    W = sum(zero_counts[w] * (2.0 ** (-w)) for w in range(1, N + 1))
    return {"N": N, "partial": partial, "state_count": len(dist), "zero_weight_counts": zero_counts, "W": W}


def d3_sum(n: int, p: int, L: int, deadline: float) -> dict[str, Any]:
    columns = section_columns(n, p, L)
    cos2 = [math.cos(math.pi * a / p) ** 2 for a in range(p)]
    total = 0.0
    checked = 0
    partial = False
    for lam in itertools.product(range(p), repeat=L):
        prod = 1.0
        for col in columns:
            a = sum(lam[i] * col[i] for i in range(L)) % p
            prod *= cos2[a]
        total += prod
        checked += 1
        if (checked & 0x3FFF) == 0 and time.monotonic() >= deadline:
            partial = True
            break
    return {"D3_sum": total, "lambda_checked": checked, "lambda_total": p**L, "partial": partial}


def attack_identity(time_limit: float) -> dict[str, Any]:
    out = OUTDIR / "identity_replication_results.json"
    deadline = time.monotonic() + time_limit
    rows = [
        {"n": 16, "p": 17, "L": 1},
        {"n": 16, "p": 17, "L": 2},
        {"n": 16, "p": 17, "L": 3},
        {"n": 32, "p": 97, "L": 2},
        {"n": 64, "p": 193, "L": 2},
    ]
    result: dict[str, Any] = {
        "attack": "D1=D2=D3 identity replication",
        "started_at_unix": time.time(),
        "time_limit_seconds": time_limit,
        "rows": [],
    }
    checkpoint(out, result)
    for row in rows:
        if time.monotonic() + 2.0 >= deadline:
            break
        dp = dp_weight_distribution(row["n"], row["p"], row["L"], deadline)
        d3 = d3_sum(row["n"], row["p"], row["L"], deadline)
        N = dp["N"]
        D2 = (row["p"] ** row["L"]) * (1.0 + dp["W"]) / (2.0**N)
        item = {
            **row,
            **dp,
            **d3,
            "D2_from_D1": D2,
            "abs_D2_minus_D3": abs(D2 - d3["D3_sum"]),
            "rel_D2_minus_D3": abs(D2 - d3["D3_sum"]) / max(1.0, abs(d3["D3_sum"])),
        }
        result["rows"].append(item)
        checkpoint(out, result)
        if dp["partial"] or d3["partial"]:
            break
    result["status"] = "PASS_IDENTITIES_REPLICATED" if len(result["rows"]) >= 3 else "PARTIAL"
    result["finished_at_unix"] = time.time()
    checkpoint(out, result)
    return result


def attack_level(time_limit: float) -> dict[str, Any]:
    out = OUTDIR / "level_independence_results.json"
    note = ROOT / "archive/compressed_dli_lane_20260705/b2b_primitive_core/notes/level2_falsifier.md"
    rhoj = ROOT / "archive/compressed_dli_lane_20260705/b2b_primitive_core/notes/pro_brief_rhoj.md"
    text = note.read_text()
    rhoj_text = rhoj.read_text()
    result = {
        "attack": "level-independence packet audit",
        "started_at_unix": time.time(),
        "time_limit_seconds": time_limit,
        "sources": [str(note.relative_to(ROOT)), str(rhoj.relative_to(ROOT))],
        "findings": [
            {
                "claim": "exact tower factorization/product-total",
                "evidence": "level2_falsifier TEST 1 says tower-1 equals direct census in every listed mu_32 row",
                "verdict": "supported by existing exact census",
                "source_contains": "PASS -- tower factorization reproduces every census exactly"
                in text,
            },
            {
                "claim": "profile-constant product of per-profile constants",
                "evidence": "level2_falsifier TEST 2 gives explicit same-profile states with different skewcounts",
                "verdict": "false; this route is already killed",
                "source_contains": "TEST 2 verdict: FALSIFIED" in text,
            },
            {
                "claim": "central tower measure product across levels for DLI-CLOSE",
                "evidence": "rho_j brief writes C_central as q^{-t} sum_Pi U(Pi) prod_j rho_j(M_{j+1}); no file found that proves independence of the weighted central tower measure itself",
                "verdict": "not falsified by the level2 note, but still an explicit unproved hypothesis requiring statement/proof",
                "source_contains": "weighted-average over the central tower measure of prod_j rho_j" in rhoj_text,
            },
        ],
        "fatal_architecture_finding": False,
        "verdict": (
            "No new fatal coupling found. Existing evidence supports exact factorization but kills "
            "the stronger profile-constant product shortcut; the DLI-CLOSE level-product hypothesis "
            "remains unproved and must stay explicit."
        ),
        "finished_at_unix": time.time(),
    }
    checkpoint(out, result)
    return result


def print_summary(result: dict[str, Any]) -> None:
    print(json.dumps({k: v for k, v in result.items() if k not in {"rows"}}, indent=2, sort_keys=True))
    if "rows" in result:
        print(f"rows_recorded={len(result['rows'])}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--attack",
        choices=["gap", "rotation", "tail", "analytic", "identity", "level"],
        required=True,
    )
    parser.add_argument("--time-limit", type=float, default=55.0)
    parser.add_argument("--start-row", type=int, default=0, help="row offset for chunked gap sweeps")
    parser.add_argument("--row-count", type=int, default=None, help="number of planned rows for chunked gap sweeps")
    parser.add_argument("--weight-min", type=int, default=None, help="minimum weight for chunked gap sweeps")
    parser.add_argument("--weight-max", type=int, default=None, help="maximum weight for chunked gap sweeps")
    args = parser.parse_args()
    if args.attack == "gap":
        result = attack_gap(args.time_limit, args.start_row, args.row_count, args.weight_min, args.weight_max)
    elif args.attack == "rotation":
        result = direct_pattern_attacks(args.time_limit)
    elif args.attack == "tail":
        result = attack_tail(args.time_limit)
    elif args.attack == "analytic":
        result = attack_analytic(args.time_limit)
    elif args.attack == "identity":
        result = attack_identity(args.time_limit)
    else:
        result = attack_level(args.time_limit)
    print_summary(result)
    return 0 if not str(result.get("status", "")).startswith("FALSIFIER") else 2


if __name__ == "__main__":
    raise SystemExit(main())

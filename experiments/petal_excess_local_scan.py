#!/usr/bin/env python3
"""Bounded petal-growth falsification scan.

This is a local, laptop-safe version of the archived petal_excess_induction
Modal scan.  It attacks the live red premise behind the amber node `imgfib`:
full-petal growth should be uniformly polynomial after quotient/paid families
are accounted for.

The scan deliberately separates three facts:

* Lemma-13 kernel ceiling: dim K <= c+1.  A violation would contradict the
  proved fixed-excess machinery.
* Ambient kernel growth in c.  Growth here is an obstruction to the old
  "flat kernel" induction premise, but is not by itself a falsifier of the
  corrected paid/classified route.
* Exact realizable squarefree locator counts in small coset-chart cells.  These
  are the adversarial counts most directly relevant to full-petal extras.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "experiments" / "amber_stress" / "petal_excess_local_scan_results.json"


def trim_poly(coeffs: list[int] | tuple[int, ...]) -> tuple[int, ...]:
    out = list(coeffs)
    while out and out[-1] == 0:
        out.pop()
    return tuple(out)


def poly_degree(coeffs: list[int] | tuple[int, ...]) -> int:
    return len(trim_poly(coeffs)) - 1


def poly_add(left: list[int] | tuple[int, ...], right: list[int] | tuple[int, ...], p: int) -> tuple[int, ...]:
    size = max(len(left), len(right))
    out = [0] * size
    for i in range(size):
        out[i] = ((left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0)) % p
    return trim_poly(out)


def poly_scale(coeffs: list[int] | tuple[int, ...], scalar: int, p: int) -> tuple[int, ...]:
    return trim_poly([(scalar * c) % p for c in coeffs])


def multiply_by_linear(coeffs: list[int] | tuple[int, ...], root: int, p: int) -> tuple[int, ...]:
    values = tuple(coeffs)
    out = [0] * (len(values) + 1)
    for i, c in enumerate(values):
        out[i] = (out[i] - root * c) % p
        out[i + 1] = (out[i + 1] + c) % p
    return trim_poly(out)


def interpolate_polynomial(xs: list[int], ys: list[int], p: int) -> tuple[int, ...]:
    if len(set(xs)) != len(xs):
        raise ValueError("interpolation points must be distinct")
    result: tuple[int, ...] = ()
    for j, x_j in enumerate(xs):
        basis: tuple[int, ...] = (1,)
        denom = 1
        for m, x_m in enumerate(xs):
            if m == j:
                continue
            basis = multiply_by_linear(basis, x_m, p)
            denom = (denom * (x_j - x_m)) % p
        result = poly_add(result, poly_scale(basis, ys[j] * pow(denom, -1, p), p), p)
    return result


def eval_poly(coeffs: list[int] | tuple[int, ...], x: int, p: int) -> int:
    out = 0
    for c in reversed(tuple(coeffs)):
        out = (out * x + c) % p
    return out


def matrix_rref(matrix: list[list[int]], p: int) -> tuple[list[list[int]], list[int]]:
    rows = [row[:] for row in matrix]
    pivots: list[int] = []
    pr = 0
    ncol = len(rows[0]) if rows else 0
    for col in range(ncol):
        piv = next((r for r in range(pr, len(rows)) if rows[r][col] % p), None)
        if piv is None:
            continue
        rows[pr], rows[piv] = rows[piv], rows[pr]
        inv = pow(rows[pr][col] % p, -1, p)
        rows[pr] = [(v * inv) % p for v in rows[pr]]
        for ri, row in enumerate(rows):
            if ri == pr:
                continue
            f = row[col] % p
            if f:
                rows[ri] = [(e - f * pe) % p for e, pe in zip(row, rows[pr])]
        pivots.append(col)
        pr += 1
        if pr == len(rows):
            break
    return rows, pivots


def locator(roots: list[int] | tuple[int, ...], p: int) -> tuple[int, ...]:
    poly: tuple[int, ...] = (1,)
    for root in roots:
        poly = multiply_by_linear(poly, root, p)
    return trim_poly(poly)


def crt_residue_degree(petals: list[list[int]], scalars: list[int], target_poly: tuple[int, ...], p: int) -> int:
    xs: list[int] = []
    ys: list[int] = []
    for petal, c in zip(petals, scalars):
        for x in petal:
            xs.append(x)
            ys.append((c * eval_poly(target_poly, x, p)) % p)
    return poly_degree(interpolate_polynomial(xs, ys, p))


def rank_general(p: int, petals: list[list[int]], scalars: list[int], d: int) -> int:
    """Residue-line count = rank(pi_{>d} R_{I,d})."""
    n_petal = sum(len(petal) for petal in petals)
    xs = [x for petal in petals for x in petal]
    rows: list[list[int]] = []
    for j in range(d + 1):
        ys = []
        for petal, c in zip(petals, scalars):
            for x in petal:
                ys.append((c * pow(x, j, p)) % p)
        w = list(interpolate_polynomial(xs, ys, p))
        w = w + [0] * (n_petal - len(w))
        rows.append(w[d + 1 : n_petal])
    _, pivots = matrix_rref(rows, p)
    return len(pivots)


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
        if all(pow(g, (p - 1) // r, p) != 1 for r in factors):
            return g
    raise AssertionError(f"no primitive root for {p}")


def is_prime(m: int) -> bool:
    if m < 2:
        return False
    if m % 2 == 0:
        return m == 2
    d = 3
    while d * d <= m:
        if m % d == 0:
            return False
        d += 2
    return True


def next_prime_1mod(ell: int, target: int) -> int:
    p = max(2, target)
    while p % ell != 1:
        p += 1
    while not is_prime(p):
        p += ell
    return p


def subgroup_coset_petals(p: int, ell: int, t: int) -> tuple[list[list[int]], list[int]]:
    """t distinct cosets of the order-ell subgroup of F_p^*."""
    if (p - 1) % ell:
        raise ValueError(f"no order-{ell} subgroup in F_{p}^*")
    g = primitive_root(p)
    h = pow(g, (p - 1) // ell, p)
    sub = [pow(h, i, p) for i in range(ell)]
    petals: list[list[int]] = []
    used: set[int] = set()
    reps = 0
    while len(petals) < t and reps < p:
        rep = pow(g, reps, p)
        coset = sorted((rep * s) % p for s in sub)
        if len(set(coset)) == ell and not (set(coset) & used):
            petals.append(coset)
            used |= set(coset)
        reps += 1
    if len(petals) < t:
        raise ValueError(f"only found {len(petals)} cosets")
    core_pool = [x for x in range(1, p) if x not in used]
    return petals, core_pool


def exact_realizable_count(
    p: int,
    petals: list[list[int]],
    scalars: list[int],
    core_pool: list[int],
    d: int,
    combo_cap: int,
    deadline: float,
) -> dict[str, Any]:
    core_cap = min(len(core_pool), d + 6)
    core = core_pool[:core_cap]
    total = math.comb(len(core), d) if 0 <= d <= len(core) else 0
    if total > combo_cap:
        return {"status": "SKIPPED_COMBO_CAP", "core_size": len(core), "candidates": total}
    count = 0
    checked = 0
    for D in itertools.combinations(core, d):
        if time.monotonic() >= deadline:
            return {
                "status": "PARTIAL_TIME_GUARD",
                "count": count,
                "core_size": len(core),
                "checked": checked,
                "candidates": total,
            }
        loc_d = locator(D, p)
        if poly_degree(loc_d) == d and crt_residue_degree(petals, scalars, loc_d, p) <= d:
            count += 1
        checked += 1
    return {"status": "EXACT", "count": count, "core_size": len(core), "checked": checked, "candidates": total}


def run_gate() -> dict[str, Any]:
    fails: list[str] = []

    p, ell, t, d = 19, 3, 3, 3
    petals = [[1, 7, 11], [4, 9, 6], [16, 17, 5]]
    predicted = min(d + 1, t * ell - d - 1)
    route_cut_rows = []
    for scalars in ([1, 2, 3], [2, 5, 7], [1, 3, 17], [6, 10, 15]):
        r = rank_general(p, petals, list(scalars), d)
        route_cut_rows.append(
            {
                "scalars": list(scalars),
                "rank": r,
                "refuted_exact_rank_prediction": predicted,
                "exact_rank_formula_failed": r < predicted,
                "lemma13_floor_ok": r >= ell,
            }
        )
    if not all(row["exact_rank_formula_failed"] for row in route_cut_rows):
        fails.append("route-cut exact-rank formula did not fail in every control row")
    if not all(row["lemma13_floor_ok"] for row in route_cut_rows):
        fails.append("route-cut violated Lemma-13 floor")

    witness_rows = []
    witness_specs = [
        (
            "A",
            1009,
            [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
            [1, 2, 3],
            [558, 784, 852, 874, 900],
            5,
        ),
        (
            "B",
            1009,
            [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]],
            [1, 2, 3, 4, 5],
            [69, 453, 512, 670, 682, 855, 864, 917],
            8,
        ),
    ]
    for label, prime, w_petals, scalars, missed_core, defect in witness_specs:
        loc = locator(missed_core, prime)
        crt_degree = crt_residue_degree(w_petals, scalars, loc, prime)
        ok = poly_degree(loc) == defect and crt_degree <= defect
        witness_rows.append(
            {
                "label": label,
                "p": prime,
                "t": len(w_petals),
                "ell": len(w_petals[0]),
                "d": defect,
                "c": defect - len(w_petals[0]),
                "crt_residue_degree": crt_degree,
                "realizable_by_crt_shortcut": ok,
            }
        )
        if not ok:
            fails.append(f"witness {label} failed CRT realizability shortcut")
    return {"gate_pass": not fails, "gate_fails": fails, "route_cut": route_cut_rows, "witnesses": witness_rows}


def checkpoint(results: dict[str, Any]) -> None:
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")


def summarize(results: dict[str, Any]) -> None:
    rows: list[dict[str, Any]] = []
    for cfg in results.get("configs", []):
        for row in cfg.get("by_c", []):
            enriched = dict(row)
            enriched["p"] = cfg["p"]
            enriched["ell"] = cfg["ell"]
            enriched["t"] = cfg["t"]
            enriched["top_defect"] = (cfg["t"] - 1) * cfg["ell"]
            rows.append(enriched)
    exact_rows = [
        row for row in rows if row.get("exact_realizable_extras", {}).get("status") == "EXACT"
    ]
    below_top = [row for row in rows if row["d"] < row["top_defect"]]
    top_band = [row for row in rows if row["d"] >= row["top_defect"]]
    exact_below_top = [
        row for row in below_top if row.get("exact_realizable_extras", {}).get("status") == "EXACT"
    ]
    exact_top_band = [
        row for row in top_band if row.get("exact_realizable_extras", {}).get("status") == "EXACT"
    ]
    lemma_violations = [row for row in below_top if row["dim_K"] > row["lemma13_bound_c_plus_1"]]
    dim_growth = []
    below_top_dim_growth = []
    exact_growth = []
    below_top_exact_growth = []
    top_band_exact_growth = []
    for cfg in results.get("configs", []):
        top_defect = (cfg["t"] - 1) * cfg["ell"]
        seq = [(row["c"], row["dim_K"]) for row in cfg.get("by_c", [])]
        below_seq = [(row["c"], row["dim_K"]) for row in cfg.get("by_c", []) if row["d"] < top_defect]
        exact_seq = [
            (row["c"], row["exact_realizable_extras"]["count"])
            for row in cfg.get("by_c", [])
            if row.get("exact_realizable_extras", {}).get("status") == "EXACT"
        ]
        below_exact_seq = [
            (row["c"], row["exact_realizable_extras"]["count"])
            for row in cfg.get("by_c", [])
            if row["d"] < top_defect and row.get("exact_realizable_extras", {}).get("status") == "EXACT"
        ]
        top_exact_seq = [
            (row["c"], row["exact_realizable_extras"]["count"])
            for row in cfg.get("by_c", [])
            if row["d"] >= top_defect and row.get("exact_realizable_extras", {}).get("status") == "EXACT"
        ]
        if len(seq) >= 2 and seq[-1][1] > seq[0][1]:
            dim_growth.append({"p": cfg["p"], "ell": cfg["ell"], "t": cfg["t"], "seq": seq})
        if len(below_seq) >= 2 and below_seq[-1][1] > below_seq[0][1]:
            below_top_dim_growth.append({"p": cfg["p"], "ell": cfg["ell"], "t": cfg["t"], "seq": below_seq})
        if len(exact_seq) >= 2 and exact_seq[-1][1] > exact_seq[0][1]:
            exact_growth.append({"p": cfg["p"], "ell": cfg["ell"], "t": cfg["t"], "seq": exact_seq})
        if len(below_exact_seq) >= 2 and below_exact_seq[-1][1] > below_exact_seq[0][1]:
            below_top_exact_growth.append(
                {"p": cfg["p"], "ell": cfg["ell"], "t": cfg["t"], "seq": below_exact_seq}
            )
        if len(top_exact_seq) >= 2 and top_exact_seq[-1][1] > top_exact_seq[0][1]:
            top_band_exact_growth.append(
                {"p": cfg["p"], "ell": cfg["ell"], "t": cfg["t"], "seq": top_exact_seq}
            )
    results["summary"] = {
        "status": "FAIL" if lemma_violations else "PASS",
        "configs_checked": len(results.get("configs", [])),
        "rows_checked": len(rows),
        "below_top_rows": len(below_top),
        "top_or_beyond_rows": len(top_band),
        "exact_realizable_rows": len(exact_rows),
        "exact_below_top_rows": len(exact_below_top),
        "exact_top_or_beyond_rows": len(exact_top_band),
        "lemma13_applicable_violations": len(lemma_violations),
        "configs_with_dimK_growth": len(dim_growth),
        "configs_with_below_top_dimK_growth": len(below_top_dim_growth),
        "configs_with_exact_count_growth": len(exact_growth),
        "configs_with_below_top_exact_count_growth": len(below_top_exact_growth),
        "configs_with_top_band_exact_count_growth": len(top_band_exact_growth),
        "max_dim_K": max((row["dim_K"] for row in rows), default=0),
        "max_below_top_dim_K": max((row["dim_K"] for row in below_top), default=0),
        "max_exact_realizable_count": max(
            (row["exact_realizable_extras"]["count"] for row in exact_rows),
            default=0,
        ),
        "max_below_top_exact_realizable_count": max(
            (row["exact_realizable_extras"]["count"] for row in exact_below_top),
            default=0,
        ),
        "max_top_band_exact_realizable_count": max(
            (row["exact_realizable_extras"]["count"] for row in exact_top_band),
            default=0,
        ),
        "dimK_growth_examples": dim_growth[:6],
        "below_top_dimK_growth_examples": below_top_dim_growth[:6],
        "exact_count_growth_examples": exact_growth[:6],
        "below_top_exact_count_growth_examples": below_top_exact_growth[:6],
        "top_band_exact_count_growth_examples": top_band_exact_growth[:6],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-limit", type=float, default=55.0)
    parser.add_argument("--combo-cap", type=int, default=250_000)
    parser.add_argument("--targets", type=str, default="109,211,401,809")
    parser.add_argument("--c-min", type=int, default=2)
    parser.add_argument("--c-max", type=int, default=8)
    args = parser.parse_args()

    deadline = time.monotonic() + args.time_limit
    results: dict[str, Any] = {
        "started_at_unix": time.time(),
        "node": "imgfib / petal_growth",
        "time_limit_seconds": args.time_limit,
        "combo_cap": args.combo_cap,
        "target_primes": [int(x) for x in args.targets.split(",") if x],
        "excess_range_c": [args.c_min, args.c_max],
        "gate": run_gate(),
        "configs": [],
    }
    checkpoint(results)
    if not results["gate"]["gate_pass"]:
        results["status"] = "GATE_FAILED"
        summarize(results)
        checkpoint(results)
        print(json.dumps(results["summary"], indent=2, sort_keys=True))
        return 1

    for ell in (2, 3):
        for t in (3, 5):
            for target in results["target_primes"]:
                if time.monotonic() + 1.0 >= deadline:
                    break
                p = next_prime_1mod(ell, target)
                petals, core_pool = subgroup_coset_petals(p, ell, t)
                scalars = list(range(1, t + 1))
                cfg = {
                    "p": p,
                    "ell": ell,
                    "t": t,
                    "n_petal": t * ell,
                    "petals": petals,
                    "scalars": scalars,
                    "by_c": [],
                }
                for c in range(args.c_min, args.c_max + 1):
                    if time.monotonic() + 0.5 >= deadline:
                        break
                    d = ell + c
                    if d > t * ell - 1:
                        continue
                    residue_lines = rank_general(p, petals, scalars, d)
                    dim_k = d + 1 - residue_lines
                    exact_count = exact_realizable_count(
                        p,
                        petals,
                        scalars,
                        core_pool,
                        d,
                        args.combo_cap,
                        deadline,
                    )
                    cfg["by_c"].append(
                        {
                            "c": c,
                            "d": d,
                            "top_defect": (t - 1) * ell,
                            "top_defect_band": d >= (t - 1) * ell,
                            "residue_line_count": residue_lines,
                            "dim_K": dim_k,
                            "lemma13_bound_c_plus_1": c + 1,
                            "lemma13_applicable": d < (t - 1) * ell,
                            "lemma13_ok": d >= (t - 1) * ell or dim_k <= c + 1,
                            "refuted_exact_formula_rank": min(d + 1, t * ell - d - 1),
                            "exact_realizable_extras": exact_count,
                        }
                    )
                    summarize(results)
                    checkpoint(results)
                results["configs"].append(cfg)
                summarize(results)
                checkpoint(results)

    results["finished_at_unix"] = time.time()
    summarize(results)
    results["status"] = results["summary"]["status"]
    checkpoint(results)
    print(json.dumps(results["summary"], indent=2, sort_keys=True))
    if results["summary"]["lemma13_applicable_violations"]:
        print("FAIL: Lemma-13 kernel ceiling violated below top defect")
        return 1
    print("PASS: no below-top Lemma-13 violation; see growth summaries for stress evidence")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

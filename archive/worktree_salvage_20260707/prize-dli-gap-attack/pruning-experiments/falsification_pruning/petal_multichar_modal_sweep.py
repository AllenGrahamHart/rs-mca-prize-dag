#!/usr/bin/env python3
"""Modal sweep for Petal/PRK multi-character actual-locus realizability.

The abstract PRK multi-character budget is already too large to leave
uncharged.  The remaining premise below the amber cofactor-chargeability chain
is sharper:

    do those multi-character families actually occur in the split-squarefree
    CRT-realizable locator locus?

This script expands the previous single-row test over several small parameter
rows and many sampled petal/scalar charts.  A CRT hit is a concrete premise
counterexample candidate.  A no-hit result is only bounded falsification
evidence for actual-locus exclusion.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import random
import sys
import time
from pathlib import Path
from typing import Any

import modal


sys.dont_write_bytecode = True

APP_NAME = "rs-mca-petal-multichar-sweep-20260705"
app = modal.App(APP_NAME)

DEFAULT_CONFIGS = (
    (127, 3, 5),
    (127, 3, 6),
    (127, 3, 7),
    (97, 4, 5),
    (193, 4, 5),
    (101, 5, 5),
)


def parse_config(text: str) -> tuple[int, int, int]:
    parts = text.split(",")
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("config must be p,M,t")
    return tuple(map(int, parts))  # type: ignore[return-value]


def write_checkpoint(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    tmp.replace(path)


@app.function(image=modal.Image.debian_slim(), cpu=2, memory=2048, timeout=58)
def run_remote(
    configs: list[tuple[int, int, int]],
    random_samples_per_config: int,
    coeff_density: float,
    chart_samples: int,
    random_scalar_modes: int,
    seed: int,
    seconds: float,
    max_examples: int,
) -> dict[str, Any]:
    started = time.time()
    deadline = started + seconds
    rng = random.Random(seed)

    def trim_poly(coeffs: tuple[int, ...] | list[int], p: int) -> tuple[int, ...]:
        out = [c % p for c in coeffs]
        while out and out[-1] == 0:
            out.pop()
        return tuple(out)

    def poly_degree(coeffs: tuple[int, ...] | list[int], p: int) -> int:
        return len(trim_poly(coeffs, p)) - 1

    def poly_add(left: tuple[int, ...], right: tuple[int, ...], p: int) -> tuple[int, ...]:
        size = max(len(left), len(right))
        out = [0] * size
        for idx in range(size):
            out[idx] = (
                (left[idx] if idx < len(left) else 0)
                + (right[idx] if idx < len(right) else 0)
            ) % p
        return trim_poly(out, p)

    def poly_scale(poly: tuple[int, ...], scalar: int, p: int) -> tuple[int, ...]:
        return trim_poly([scalar * coeff for coeff in poly], p)

    def multiply_by_linear(poly: tuple[int, ...], root: int, p: int) -> tuple[int, ...]:
        out = [0] * (len(poly) + 1)
        for idx, coeff in enumerate(poly):
            out[idx] = (out[idx] - root * coeff) % p
            out[idx + 1] = (out[idx + 1] + coeff) % p
        return trim_poly(out, p)

    def interpolate_polynomial(xs: list[int], ys: list[int], p: int) -> tuple[int, ...]:
        result: tuple[int, ...] = ()
        for j, x_j in enumerate(xs):
            basis: tuple[int, ...] = (1,)
            denom = 1
            for m, x_m in enumerate(xs):
                if m == j:
                    continue
                basis = multiply_by_linear(basis, x_m, p)
                denom = (denom * (x_j - x_m)) % p
            term = poly_scale(basis, ys[j] * pow(denom, -1, p), p)
            result = poly_add(result, term, p)
        return result

    def eval_poly(poly: tuple[int, ...], x: int, p: int) -> int:
        value = 0
        for coeff in reversed(poly):
            value = (value * x + coeff) % p
        return value

    def crt_residue_degree(
        petals: list[list[int]], scalars: list[int], target_poly: tuple[int, ...], p: int
    ) -> int:
        xs: list[int] = []
        ys: list[int] = []
        for petal, scalar in zip(petals, scalars):
            for x in petal:
                xs.append(x)
                ys.append((scalar * eval_poly(target_poly, x, p)) % p)
        return poly_degree(interpolate_polynomial(xs, ys, p), p)

    def factor_int(n: int) -> list[int]:
        factors = []
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
        for candidate in range(2, p):
            if all(pow(candidate, (p - 1) // factor, p) != 1 for factor in factors):
                return candidate
        raise ValueError("no primitive root")

    def all_subgroup_cosets(p: int, ell: int) -> list[list[int]]:
        if (p - 1) % ell:
            raise ValueError(f"ell={ell} does not divide p-1={p - 1}")
        g = primitive_root(p)
        h = pow(g, (p - 1) // ell, p)
        subgroup = [pow(h, i, p) for i in range(ell)]
        cosets: list[list[int]] = []
        used: set[int] = set()
        for rep_index in range(p - 1):
            rep = pow(g, rep_index, p)
            coset = sorted((rep * x) % p for x in subgroup)
            if not (set(coset) & used):
                cosets.append(coset)
                used.update(coset)
        return cosets

    def roots_of(poly: tuple[int, ...], p: int) -> list[int]:
        return [x for x in range(1, p) if eval_poly(poly, x, p) == 0]

    def coeff_poly(d: int, p: int, entries: dict[int, int]) -> tuple[int, ...]:
        coeff = [0] * (d + 1)
        for idx, value in entries.items():
            coeff[idx] = value % p
        return tuple(coeff)

    def coeff_support(poly: tuple[int, ...], p: int) -> list[int]:
        return [idx for idx, coeff in enumerate(poly) if coeff % p]

    def charged_like_reason(poly: tuple[int, ...], p: int, d: int) -> str | None:
        support = coeff_support(poly, p)
        if support == [0, d]:
            return "binomial_coset_locator"
        return None

    def scalar_sets(p: int, t: int) -> list[list[int]]:
        out = [list(range(1, t + 1))]
        for base in (5, 7):
            vals = []
            value = 1
            for _ in range(t):
                vals.append(value)
                value = (value * base) % p
            if len(set(vals)) == t:
                out.append(vals)
        for _ in range(random_scalar_modes):
            out.append(rng.sample(range(1, p), t))
        return out

    def chart_sets(
        cosets: list[list[int]], roots: set[int], t: int, chart_count: int
    ) -> list[list[list[int]]]:
        disjoint = [coset for coset in cosets if not (set(coset) & roots)]
        if len(disjoint) < t:
            return []
        charts: list[list[list[int]]] = [
            disjoint[:t],
            disjoint[-t:],
            [disjoint[(i * len(disjoint)) // t] for i in range(t)],
        ]
        seen = {tuple(tuple(c) for c in chart) for chart in charts}
        attempts = 0
        while len(charts) < chart_count and attempts < 10 * chart_count:
            attempts += 1
            chart = rng.sample(disjoint, t)
            key = tuple(tuple(c) for c in chart)
            if key in seen:
                continue
            seen.add(key)
            charts.append(chart)
        return charts

    def check_poly(
        poly: tuple[int, ...],
        *,
        p: int,
        d: int,
        t: int,
        cosets: list[list[int]],
        scalars: list[list[int]],
    ) -> dict[str, Any]:
        roots = roots_of(poly, p)
        if len(roots) != d:
            return {"split": False, "root_count": len(roots)}
        hits = []
        charts_tested = 0
        for petals in chart_sets(cosets, set(roots), t, chart_samples):
            for scalar_row in scalars:
                charts_tested += 1
                degcrt = crt_residue_degree(petals, scalar_row, poly, p)
                if degcrt <= d:
                    hits.append(
                        {
                            "degcrt": degcrt,
                            "petals": petals,
                            "scalars": scalar_row,
                        }
                    )
                    if len(hits) >= max_examples:
                        break
            if len(hits) >= max_examples:
                break
        return {
            "split": True,
            "roots": roots,
            "charts_tested": charts_tested,
            "crt_hits": hits,
        }

    def narrow_family(
        p: int, m: int, t: int, d: int, cosets: list[list[int]], scalars: list[list[int]]
    ) -> dict[str, Any]:
        split_count = 0
        hit_count = 0
        charged_like_hit_count = 0
        unclassified_hit_count = 0
        examples = []
        nohit_examples = []
        complete = True
        for a in range(p):
            for b in range(1, p):
                if time.time() > deadline - 1:
                    complete = False
                    return {
                        "family": "X^d + a X^(d-M) + b",
                        "evaluated": a * (p - 1) + (b - 1),
                        "split_count": split_count,
                        "crt_hit_count": hit_count,
                        "charged_like_crt_hit_count": charged_like_hit_count,
                        "unclassified_crt_hit_count": unclassified_hit_count,
                        "hit_examples": examples,
                        "split_examples_without_crt": nohit_examples,
                        "complete": complete,
                    }
                poly = coeff_poly(d, p, {0: b, d - m: a, d: 1})
                checked = check_poly(poly, p=p, d=d, t=t, cosets=cosets, scalars=scalars)
                if checked["split"]:
                    split_count += 1
                    reason = charged_like_reason(poly, p, d)
                    record = {
                        "a": a,
                        "b": b,
                        "poly_support": coeff_support(poly, p),
                        "charged_like_reason": reason,
                        **checked,
                    }
                    if checked["crt_hits"]:
                        hit_count += 1
                        if reason:
                            charged_like_hit_count += 1
                        else:
                            unclassified_hit_count += 1
                        if len(examples) < max_examples:
                            examples.append(record)
                    elif len(nohit_examples) < max_examples:
                        nohit_examples.append(record)
        return {
            "family": "X^d + a X^(d-M) + b",
            "evaluated": p * (p - 1),
            "split_count": split_count,
            "crt_hit_count": hit_count,
            "charged_like_crt_hit_count": charged_like_hit_count,
            "unclassified_crt_hit_count": unclassified_hit_count,
            "hit_examples": examples,
            "split_examples_without_crt": nohit_examples,
            "complete": complete,
        }

    def random_family(
        p: int, m: int, t: int, d: int, cosets: list[list[int]], scalars: list[list[int]]
    ) -> dict[str, Any]:
        active_degrees = [degree for degree in range(d + 1) if degree % m in {0, m - 1}]
        free_degrees = [degree for degree in active_degrees if degree != d]
        zero_degrees = [degree for degree in free_degrees if degree % m == 0]
        mminus_degrees = [degree for degree in free_degrees if degree % m == m - 1]
        out: dict[str, Any] = {
            "family": "random active residues {0,M-1}",
            "active_degrees": active_degrees,
            "samples_requested": random_samples_per_config,
            "evaluated": 0,
            "split_count": 0,
            "crt_hit_count": 0,
            "charged_like_crt_hit_count": 0,
            "unclassified_crt_hit_count": 0,
            "hit_examples": [],
            "split_examples_without_crt": [],
            "complete": True,
        }
        for _ in range(random_samples_per_config):
            if time.time() > deadline - 1:
                out["complete"] = False
                out["skipped_reason"] = "deadline"
                return out
            entries = {d: 1}
            for degree in free_degrees:
                if rng.random() < coeff_density:
                    entries[degree] = rng.randrange(1, p)
            if not any(deg % m == 0 for deg in entries) and zero_degrees:
                entries[rng.choice(zero_degrees)] = rng.randrange(1, p)
            if not any(deg % m == m - 1 for deg in entries) and mminus_degrees:
                entries[rng.choice(mminus_degrees)] = rng.randrange(1, p)
            poly = coeff_poly(d, p, entries)
            out["evaluated"] += 1
            checked = check_poly(poly, p=p, d=d, t=t, cosets=cosets, scalars=scalars)
            if checked["split"]:
                out["split_count"] += 1
                reason = charged_like_reason(poly, p, d)
                record = {
                    "poly": list(poly),
                    "poly_support": coeff_support(poly, p),
                    "charged_like_reason": reason,
                    **checked,
                }
                if checked["crt_hits"]:
                    out["crt_hit_count"] += 1
                    if reason:
                        out["charged_like_crt_hit_count"] += 1
                    else:
                        out["unclassified_crt_hit_count"] += 1
                    if len(out["hit_examples"]) < max_examples:
                        out["hit_examples"].append(record)
                elif len(out["split_examples_without_crt"]) < max_examples:
                    out["split_examples_without_crt"].append(record)
        return out

    rows = []
    for p, m, t in configs:
        if time.time() > deadline - 1:
            break
        d = (t - 1) * m - 1
        cosets = all_subgroup_cosets(p, m)
        scalars = scalar_sets(p, t)
        row: dict[str, Any] = {
            "p": p,
            "M": m,
            "ell": m,
            "t": t,
            "d": d,
            "c": d - m,
            "coset_count": len(cosets),
            "scalar_mode_count": len(scalars),
            "chart_samples": chart_samples,
            "narrow_family": None,
            "random_two_character": None,
        }
        row["narrow_family"] = narrow_family(p, m, t, d, cosets, scalars)
        if time.time() < deadline - 1:
            row["random_two_character"] = random_family(p, m, t, d, cosets, scalars)
        rows.append(row)
        if (
            int(row["narrow_family"].get("unclassified_crt_hit_count", 0))
            or (
                row["random_two_character"]
                and int(row["random_two_character"].get("unclassified_crt_hit_count", 0))
            )
        ):
            break

    narrow_hits = sum(int(row["narrow_family"].get("crt_hit_count", 0)) for row in rows)
    random_hits = sum(
        int(row["random_two_character"].get("crt_hit_count", 0))
        for row in rows
        if row.get("random_two_character")
    )
    unclassified_hits = sum(
        int(row["narrow_family"].get("unclassified_crt_hit_count", 0))
        + (
            int(row["random_two_character"].get("unclassified_crt_hit_count", 0))
            if row.get("random_two_character")
            else 0
        )
        for row in rows
    )
    charged_like_hits = narrow_hits + random_hits - unclassified_hits
    complete = len(rows) == len(configs) and all(
        row["narrow_family"].get("complete", True)
        and (not row.get("random_two_character") or row["random_two_character"].get("complete", True))
        for row in rows
    )
    if unclassified_hits:
        verdict = "UNCLASSIFIED_SPLIT_MULTICHAR_REALIZABLE_CANDIDATE_FOUND"
    elif charged_like_hits:
        verdict = "ONLY_CHARGED_LIKE_SPLIT_MULTICHAR_CRT_HITS"
    elif not complete:
        verdict = "TIMEOUT_PARTIAL_NO_SPLIT_MULTICHAR_CRT_HIT"
    else:
        verdict = "NO_SPLIT_MULTICHAR_CRT_HIT_IN_PARAMETER_SWEEP"
    return {
        "node": "petal_squarefree_classification_ledger_payload",
        "downstream_amber_nodes": [
            "petal_squarefree_kernel_classification_payload",
            "petal_cofactor_chargeability",
        ],
        "obligation_attacked": (
            "whether two-character PRK obstruction families occur in the "
            "actual split-squarefree CRT-realizable locator locus across "
            "multiple parameter rows and sampled petal/scalar charts"
        ),
        "app_name": APP_NAME,
        "parameters": {
            "configs": [list(config) for config in configs],
            "random_samples_per_config": random_samples_per_config,
            "coeff_density": coeff_density,
            "chart_samples": chart_samples,
            "random_scalar_modes": random_scalar_modes,
            "seed": seed,
            "seconds": seconds,
        },
        "rows": rows,
        "hit_summary": {
            "total_crt_hits": narrow_hits + random_hits,
            "charged_like_crt_hits": charged_like_hits,
            "unclassified_crt_hits": unclassified_hits,
        },
        "elapsed_seconds": time.time() - started,
        "complete": complete,
        "verdict": verdict,
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    configs = args.config or list(DEFAULT_CONFIGS)
    initial = {
        "node": "petal_squarefree_classification_ledger_payload",
        "obligation_attacked": "multi-character actual-locus realizability parameter sweep",
        "requested_configs": [list(config) for config in configs],
        "verdict": "RUNNING",
    }
    write_checkpoint(args.output, initial)
    with app.run():
        payload = run_remote.remote(
            configs,
            args.random_samples_per_config,
            args.coeff_density,
            args.chart_samples,
            args.random_scalar_modes,
            args.seed,
            args.seconds,
            args.max_examples,
        )
    write_checkpoint(args.output, payload)
    return payload


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=50.0)
    parser.add_argument("--config", action="append", type=parse_config)
    parser.add_argument("--random-samples-per-config", type=int, default=20000)
    parser.add_argument("--coeff-density", type=float, default=0.45)
    parser.add_argument("--chart-samples", type=int, default=64)
    parser.add_argument("--random-scalar-modes", type=int, default=2)
    parser.add_argument("--seed", type=int, default=7206)
    parser.add_argument("--max-examples", type=int, default=4)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/falsification_pruning/results/petal_multichar_modal_sweep.json"),
    )
    return parser


def main() -> None:
    print(json.dumps(run(make_parser().parse_args()), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

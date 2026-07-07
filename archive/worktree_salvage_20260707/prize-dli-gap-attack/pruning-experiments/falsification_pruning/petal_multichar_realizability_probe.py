#!/usr/bin/env python3
"""Targeted Petal multi-character realizability probe.

The PRK repair premise says multi-character residue-kernel families are either
paid or excluded/bounded on the actual squarefree-realizable locus.  The budget
probe shows the abstract character-block model is too large to leave uncharged;
this script asks a sharper question in the executable split-locator chart:

    Do simple two-character coefficient supports produce split-squarefree
    missed-core locators satisfying the CRT degree condition?

This is deliberately not a proof attempt.  A hit would be a concrete premise
counterexample candidate for the current paid menu.  No hit means only that this
particular split-locator realization of the Pro-style two-character obstruction
did not land in the tested charts.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
import time
from pathlib import Path
from typing import Any


sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "experiments" / "falsification_pruning"))

import petal_squarefree_ledger_scope_probe as base  # noqa: E402


def all_subgroup_cosets(p: int, ell: int) -> list[list[int]]:
    g = base.primitive_root(p)
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
    return [x for x in range(1, p) if base.eval_poly(poly, x, p) == 0]


def coeff_support(poly: tuple[int, ...], p: int) -> list[int]:
    return [idx for idx, coeff in enumerate(poly) if coeff % p]


def coeff_poly(d: int, p: int, entries: dict[int, int]) -> tuple[int, ...]:
    coeff = [0] * (d + 1)
    for idx, value in entries.items():
        coeff[idx] = value % p
    return tuple(coeff)


def scalar_modes(p: int, t: int, rng: random.Random) -> list[list[int]]:
    geometric = []
    value = 1
    for _ in range(t):
        geometric.append(value)
        value = (value * 5) % p
    random_mode = rng.sample(range(1, p), t)
    return [list(range(1, t + 1)), geometric, random_mode]


def chart_candidates(
    cosets: list[list[int]], roots: set[int], t: int, rng: random.Random
) -> list[list[list[int]]]:
    disjoint = [coset for coset in cosets if not (set(coset) & roots)]
    if len(disjoint) < t:
        return []
    out: list[list[list[int]]] = [
        disjoint[:t],
        disjoint[-t:],
        [disjoint[(i * len(disjoint)) // t] for i in range(t)],
    ]
    for _ in range(3):
        out.append(rng.sample(disjoint, t))
    return out


def check_poly(
    poly: tuple[int, ...],
    *,
    p: int,
    d: int,
    t: int,
    cosets: list[list[int]],
    scalar_sets: list[list[int]],
    rng: random.Random,
    max_hit_examples: int,
) -> dict[str, Any]:
    roots = roots_of(poly, p)
    if len(roots) != d:
        return {"split": False, "root_count": len(roots)}
    root_set = set(roots)
    hits = []
    charts_tested = 0
    for petals in chart_candidates(cosets, root_set, t, rng):
        for scalars in scalar_sets:
            charts_tested += 1
            degcrt = base.crt_residue_degree(petals, scalars, poly, p)
            if degcrt <= d:
                hits.append(
                    {
                        "degcrt": degcrt,
                        "petals": petals,
                        "scalars": scalars,
                    }
                )
                if len(hits) >= max_hit_examples:
                    break
        if len(hits) >= max_hit_examples:
            break
    return {
        "split": True,
        "roots": roots,
        "charts_tested": charts_tested,
        "crt_hits": hits,
    }


def narrow_family_rows(args: argparse.Namespace, cosets: list[list[int]], scalar_sets: list[list[int]], rng: random.Random) -> dict[str, Any]:
    d = (args.t - 1) * args.M - 1
    rows = []
    split_count = 0
    hit_count = 0
    for a in range(args.p):
        for b in range(1, args.p):
            poly = coeff_poly(
                d,
                args.p,
                {
                    0: b,
                    args.M - 1 + args.M * (args.t - 3): a,
                    d: 1,
                },
            )
            checked = check_poly(
                poly,
                p=args.p,
                d=d,
                t=args.t,
                cosets=cosets,
                scalar_sets=scalar_sets,
                rng=rng,
                max_hit_examples=args.max_hit_examples,
            )
            if checked["split"]:
                split_count += 1
                if checked["crt_hits"]:
                    hit_count += 1
                    rows.append({"a": a, "b": b, "poly_support": coeff_support(poly, args.p), **checked})
                    if len(rows) >= args.max_hit_examples:
                        break
        if len(rows) >= args.max_hit_examples:
            break
    return {
        "family": "X^d + a X^(d-M) + b",
        "split_count": split_count,
        "crt_hit_count": hit_count,
        "hit_examples": rows,
    }


def random_two_character_rows(
    args: argparse.Namespace,
    cosets: list[list[int]],
    scalar_sets: list[list[int]],
    rng: random.Random,
    deadline: float,
) -> dict[str, Any]:
    d = (args.t - 1) * args.M - 1
    active_degrees = [
        degree
        for degree in range(d + 1)
        if degree % args.M in {0, args.M - 1}
    ]
    free_degrees = [degree for degree in active_degrees if degree != d]
    out: dict[str, Any] = {
        "family": "random active residues {0,M-1}",
        "active_degrees": active_degrees,
        "samples_requested": args.random_samples,
        "evaluated": 0,
        "split_count": 0,
        "crt_hit_count": 0,
        "hit_examples": [],
        "split_examples_without_crt": [],
        "complete": True,
    }
    while out["evaluated"] < args.random_samples:
        if time.time() > deadline - 1:
            out["complete"] = False
            out["skipped_reason"] = "deadline"
            return out
        entries = {d: 1}
        for degree in free_degrees:
            # Bias to sparse-but-not-single-character polynomials.
            if rng.random() < args.coeff_density:
                entries[degree] = rng.randrange(1, args.p)
        if not any(deg % args.M == 0 for deg in entries):
            entries[rng.choice([deg for deg in free_degrees if deg % args.M == 0])] = rng.randrange(1, args.p)
        poly = coeff_poly(d, args.p, entries)
        out["evaluated"] += 1
        checked = check_poly(
            poly,
            p=args.p,
            d=d,
            t=args.t,
            cosets=cosets,
            scalar_sets=scalar_sets,
            rng=rng,
            max_hit_examples=args.max_hit_examples,
        )
        if checked["split"]:
            out["split_count"] += 1
            record = {"poly": list(poly), "poly_support": coeff_support(poly, args.p), **checked}
            if checked["crt_hits"]:
                out["crt_hit_count"] += 1
                if len(out["hit_examples"]) < args.max_hit_examples:
                    out["hit_examples"].append(record)
            elif len(out["split_examples_without_crt"]) < args.max_hit_examples:
                out["split_examples_without_crt"].append(record)
    return out


def write_checkpoint(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    tmp.replace(path)


def run(args: argparse.Namespace) -> dict[str, Any]:
    started = time.time()
    deadline = started + args.seconds
    rng = random.Random(args.seed)
    d = (args.t - 1) * args.M - 1
    ell = args.M
    cosets = all_subgroup_cosets(args.p, ell)
    scalar_sets = scalar_modes(args.p, args.t, rng)
    payload: dict[str, Any] = {
        "node": "petal_squarefree_classification_ledger_payload",
        "downstream_amber_nodes": [
            "petal_squarefree_kernel_classification_payload",
            "petal_cofactor_chargeability",
        ],
        "obligation_attacked": (
            "whether multi-character PRK obstruction families occur in the "
            "actual split-squarefree CRT-realizable locator locus"
        ),
        "parameters": {
            "p": args.p,
            "M": args.M,
            "ell": ell,
            "t": args.t,
            "d": d,
            "c": d - ell,
            "seconds": args.seconds,
            "seed": args.seed,
            "random_samples": args.random_samples,
            "coeff_density": args.coeff_density,
        },
        "narrow_family": None,
        "random_two_character": None,
        "verdict": "RUNNING",
    }
    write_checkpoint(args.output, payload)
    payload["narrow_family"] = narrow_family_rows(args, cosets, scalar_sets, rng)
    write_checkpoint(args.output, payload)
    if time.time() < deadline - 1:
        payload["random_two_character"] = random_two_character_rows(args, cosets, scalar_sets, rng, deadline)
    narrow_hits = int(payload["narrow_family"]["crt_hit_count"]) if payload["narrow_family"] else 0
    random_hits = int(payload["random_two_character"]["crt_hit_count"]) if payload["random_two_character"] else 0
    if narrow_hits or random_hits:
        payload["verdict"] = "SPLIT_MULTICHAR_REALIZABLE_CANDIDATE_FOUND"
    elif payload["random_two_character"] and not payload["random_two_character"].get("complete", True):
        payload["verdict"] = "TIMEOUT_PARTIAL_NO_SPLIT_MULTICHAR_CRT_HIT"
    else:
        payload["verdict"] = "NO_SPLIT_MULTICHAR_CRT_HIT_IN_TESTED_CHARTS"
    payload["elapsed_seconds"] = time.time() - started
    write_checkpoint(args.output, payload)
    return payload


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=55.0)
    parser.add_argument("--p", type=int, default=127)
    parser.add_argument("--M", type=int, default=3)
    parser.add_argument("--t", type=int, default=6)
    parser.add_argument("--random-samples", type=int, default=50000)
    parser.add_argument("--coeff-density", type=float, default=0.45)
    parser.add_argument("--seed", type=int, default=7205)
    parser.add_argument("--max-hit-examples", type=int, default=5)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/falsification_pruning/results/petal_multichar_realizability_probe.json"),
    )
    return parser


def main() -> None:
    print(json.dumps(run(make_parser().parse_args()), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

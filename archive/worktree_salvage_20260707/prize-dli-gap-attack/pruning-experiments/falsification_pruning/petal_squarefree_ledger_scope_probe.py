#!/usr/bin/env python3
"""Scope probe for the Petal squarefree classification ledger.

The live Petal descendant of the refuted PRK route is
`petal_squarefree_classification_ledger_payload`: classify squarefree
realizable locator points in residue-line kernels into charged records or
uniformly bounded uncharged records.

This probe attacks a concrete falsifier shape:

    generic missed-core locators of growing degree are squarefree-realizable
    in the residue-line kernel, producing raw mass too large to leave
    uncharged.

It uses the same CRT-realizability predicate as the banked petal Modal helper,
but runs locally on capped exact-prefix pools and random full-core samples.
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


sys.dont_write_bytecode = True


DEFAULT_CONFIGS = (
    (1009, 2, 3),
    (1009, 2, 5),
    (1009, 3, 5),
    (1009, 3, 6),
)


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
        term = poly_scale(basis, ys[j] * pow(denom, -1, p), p)
        result = poly_add(result, term, p)
    return result


def eval_poly(poly: tuple[int, ...], x: int, p: int) -> int:
    value = 0
    for coeff in reversed(poly):
        value = (value * x + coeff) % p
    return value


def locator(roots: tuple[int, ...] | list[int], p: int) -> tuple[int, ...]:
    poly: tuple[int, ...] = (1,)
    for root in roots:
        poly = multiply_by_linear(poly, root, p)
    return trim_poly(poly, p)


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


def subgroup_coset_petals(p: int, ell: int, t: int) -> tuple[list[list[int]], list[int]]:
    if (p - 1) % ell:
        raise ValueError(f"ell={ell} does not divide p-1={p - 1}")
    g = primitive_root(p)
    h = pow(g, (p - 1) // ell, p)
    subgroup = [pow(h, i, p) for i in range(ell)]
    petals: list[list[int]] = []
    used: set[int] = set()
    rep_index = 0
    while len(petals) < t:
        rep = pow(g, rep_index, p)
        coset = sorted((rep * x) % p for x in subgroup)
        if not (set(coset) & used):
            petals.append(coset)
            used |= set(coset)
        rep_index += 1
        if rep_index > p:
            raise ValueError("not enough disjoint cosets")
    core_pool = [x for x in range(1, p) if x not in used]
    return petals, core_pool


def realizable(petals: list[list[int]], scalars: list[int], roots: tuple[int, ...], p: int) -> bool:
    target = locator(roots, p)
    d = len(roots)
    return poly_degree(target, p) == d and crt_residue_degree(petals, scalars, target, p) <= d


def exact_prefix_scan(
    petals: list[list[int]],
    scalars: list[int],
    core_pool: list[int],
    p: int,
    d: int,
    core_slack: int,
    max_candidates: int,
    deadline: float,
    max_examples: int,
) -> dict[str, Any]:
    core = core_pool[: min(len(core_pool), d + core_slack)]
    total = math.comb(len(core), d) if 0 <= d <= len(core) else 0
    row: dict[str, Any] = {
        "core_size": len(core),
        "candidate_count": total,
        "evaluated": 0,
        "realizable_count": 0,
        "examples": [],
        "complete": total <= max_candidates,
    }
    if total > max_candidates:
        row["skipped_reason"] = "candidate_limit"
        return row
    for roots in itertools.combinations(core, d):
        if time.time() > deadline - 1:
            row["complete"] = False
            row["skipped_reason"] = "deadline"
            return row
        row["evaluated"] += 1
        if realizable(petals, scalars, roots, p):
            row["realizable_count"] += 1
            if len(row["examples"]) < max_examples:
                row["examples"].append(list(roots))
    return row


def random_full_core_scan(
    petals: list[list[int]],
    scalars: list[int],
    core_pool: list[int],
    p: int,
    d: int,
    samples: int,
    rng: random.Random,
    deadline: float,
    max_examples: int,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "samples_requested": samples,
        "evaluated": 0,
        "realizable_count": 0,
        "examples": [],
        "complete": True,
    }
    if d > len(core_pool):
        row["complete"] = False
        row["skipped_reason"] = "d_exceeds_core_pool"
        return row
    for _ in range(samples):
        if time.time() > deadline - 1:
            row["complete"] = False
            row["skipped_reason"] = "deadline"
            return row
        roots = tuple(sorted(rng.sample(core_pool, d)))
        row["evaluated"] += 1
        if realizable(petals, scalars, roots, p):
            row["realizable_count"] += 1
            if len(row["examples"]) < max_examples:
                row["examples"].append(list(roots))
    return row


def parse_config(text: str) -> tuple[int, int, int]:
    parts = text.split(",")
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("config must be p,ell,t")
    return tuple(map(int, parts))  # type: ignore[return-value]


def write_checkpoint(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    tmp.replace(path)


def run(args: argparse.Namespace) -> dict[str, Any]:
    started = time.time()
    deadline = started + args.seconds
    rng = random.Random(args.seed)
    out: dict[str, Any] = {
        "node": "petal_squarefree_classification_ledger_payload",
        "obligation_attacked": (
            "generic squarefree-realizable missed-core mass in residue-line kernels"
        ),
        "configs": [],
        "verdict": "RUNNING",
    }
    write_checkpoint(args.output, out)

    for p, ell, t in args.config:
        if time.time() > deadline - 1:
            out["verdict"] = "TIMEOUT_PARTIAL"
            write_checkpoint(args.output, out)
            return out
        petals, core_pool = subgroup_coset_petals(p, ell, t)
        scalars = list(range(1, t + 1))
        cfg = {
            "p": p,
            "ell": ell,
            "t": t,
            "n_petal": ell * t,
            "petals": petals,
            "scalars": scalars,
            "core_pool_size": len(core_pool),
            "by_c": [],
        }
        # Petal ledger proof uses the in-regime corridor
        # d <= (t - 1) * ell - 1, with c = d - ell.
        # The weaker interpolation condition d < t*ell admits endpoint rows
        # where CRT degree <= d becomes nearly automatic and is not the node's
        # object.
        max_c = min(args.c_max, (t - 2) * ell - 1)
        for c in range(args.c_min, max_c + 1):
            d = ell + c
            row = {
                "c": c,
                "d": d,
                "exact_prefix": exact_prefix_scan(
                    petals,
                    scalars,
                    core_pool,
                    p,
                    d,
                    args.core_slack,
                    args.max_exact_candidates,
                    deadline,
                    args.max_examples,
                ),
                "random_full_core": random_full_core_scan(
                    petals,
                    scalars,
                    core_pool,
                    p,
                    d,
                    args.random_samples,
                    rng,
                    deadline,
                    args.max_examples,
                ),
            }
            cfg["by_c"].append(row)
            write_checkpoint(args.output, out)
            if time.time() > deadline - 1:
                out["configs"].append(cfg)
                out["verdict"] = "TIMEOUT_PARTIAL"
                write_checkpoint(args.output, out)
                return out
        out["configs"].append(cfg)
        write_checkpoint(args.output, out)

    random_hits = sum(
        row["random_full_core"]["realizable_count"]
        for cfg in out["configs"]
        for row in cfg["by_c"]
    )
    exact_hits_large = sum(
        row["exact_prefix"]["realizable_count"]
        for cfg in out["configs"]
        if cfg["ell"] * cfg["t"] >= 15
        for row in cfg["by_c"]
    )
    exact_hits_total = sum(
        row["exact_prefix"]["realizable_count"]
        for cfg in out["configs"]
        for row in cfg["by_c"]
    )
    out["totals"] = {
        "random_realizable_hits": random_hits,
        "exact_prefix_realizable_hits_total": exact_hits_total,
        "exact_prefix_realizable_hits_large_rows": exact_hits_large,
    }
    if random_hits:
        out["verdict"] = "GENERIC_REALIZABLE_MASS_CANDIDATE"
    elif exact_hits_large:
        out["verdict"] = "PREFIX_REALIZABLE_MASS_IN_LARGE_ROW_CANDIDATE"
    elif exact_hits_total:
        out["verdict"] = "TINY_ROW_RAW_JUMP_ONLY"
    else:
        out["verdict"] = "NO_GENERIC_REALIZABLE_MASS_FOUND"
    out["elapsed_seconds"] = time.time() - started
    write_checkpoint(args.output, out)
    return out


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=55.0)
    parser.add_argument("--config", action="append", type=parse_config, default=list(DEFAULT_CONFIGS))
    parser.add_argument("--c-min", type=int, default=2)
    parser.add_argument("--c-max", type=int, default=8)
    parser.add_argument("--core-slack", type=int, default=6)
    parser.add_argument("--max-exact-candidates", type=int, default=20_000)
    parser.add_argument("--random-samples", type=int, default=200)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--max-examples", type=int, default=4)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "experiments/falsification_pruning/results/"
            "petal_squarefree_ledger_scope_probe.json"
        ),
    )
    return parser


def main() -> None:
    payload = run(make_parser().parse_args())
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

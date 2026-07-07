#!/usr/bin/env python3
"""Budget pressure probe for the PRK multi-character repair.

`petal_primitive_residue_kernel_rank` is already falsified as stated: after the
current paid menu, multi-character kernel families leave unbounded primitive
dimension.  The proposed repair is to add multi-character paid classes.

This script attacks that repair direction, not the old absolute-bound claim. It
models the canonical mu_M character decomposition of a cofactor polynomial of
excess degree c:

    F(X) = sum_{r mod M} X^r B_r(X^M).

Single active characters are the existing quotient/isotypic paid shape.  Active
sets with at least two characters are the multi-character repair burden.  For
each (M,c), the script records:

- how many multi-character active sets exist;
- how much primitive dimension remains after peeling the largest single block;
- the minimum two-character residual, showing that even the smallest
  multi-character obstruction grows with c;
- the all-character residual, matching the generic "all blocks active" stress.

It is a structural budget falsifier: if the repair is phrased as a finite paid
menu, this shows the menu is not finite uniformly in M; if it is phrased as a
parameterized paid family, this records the exact mass/dimension it must price.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from pathlib import Path
from statistics import median
from typing import Any


DEFAULT_M = (3, 5, 7, 8, 16, 32, 64)
DEFAULT_C_MULTIPLES = (2, 4, 8)


def block_dims(M: int, c: int) -> list[int]:
    # Number of exponents d in [0,c] with d == r mod M.
    dims = []
    for r in range(M):
        if r > c:
            dims.append(0)
        else:
            dims.append(1 + (c - r) // M)
    return dims


def residual_for_active(dims: list[int], active: tuple[int, ...]) -> int:
    values = [dims[r] for r in active]
    return sum(values) - max(values)


def exact_subset_stats(M: int, c: int) -> dict[str, Any]:
    dims = block_dims(M, c)
    residuals = []
    by_size: dict[int, list[int]] = {}
    for size in range(2, M + 1):
        vals = []
        for active in itertools.combinations(range(M), size):
            r = residual_for_active(dims, active)
            residuals.append(r)
            vals.append(r)
        by_size[size] = vals
    size_stats = {
        str(size): {
            "count": len(vals),
            "min_residual": min(vals),
            "median_residual": median(vals),
            "max_residual": max(vals),
        }
        for size, vals in by_size.items()
    }
    return {
        "enumerated": True,
        "min_residual": min(residuals),
        "median_residual": median(residuals),
        "max_residual": max(residuals),
        "by_active_character_count": size_stats,
    }


def closed_stats(M: int, c: int, enumerate_limit: int) -> dict[str, Any]:
    dims = block_dims(M, c)
    type_count = (1 << M) - M - 1
    two_residuals = []
    for a, b in itertools.combinations(range(M), 2):
        two_residuals.append(min(dims[a], dims[b]))
    row: dict[str, Any] = {
        "M": M,
        "c": c,
        "block_dims": dims,
        "multi_character_type_count_decimal": str(type_count),
        "multi_character_type_count_log2": math.log2(type_count),
        "two_character_type_count": math.comb(M, 2),
        "two_character_min_residual": min(two_residuals),
        "two_character_median_residual": median(two_residuals),
        "two_character_max_residual": max(two_residuals),
        "all_character_residual": sum(dims) - max(dims),
        "largest_single_character_dim": max(dims),
        "total_all_character_dim": sum(dims),
    }
    if M <= enumerate_limit:
        row.update(exact_subset_stats(M, c))
    else:
        row["enumerated"] = False
    return row


def run(args: argparse.Namespace) -> dict[str, Any]:
    started = time.time()
    rows = []
    for M in args.M:
        for mult in args.c_multiple:
            c = mult * M - 1
            rows.append(closed_stats(M, c, args.enumerate_limit))
    out = {
        "node": "petal_primitive_residue_kernel_rank",
        "obligation_attacked": "multi-character paid-class chargeability repair",
        "model": "mu_M character block decomposition of degrees 0..c",
        "verdict": "COMPLETE_BUDGET_PRESSURE",
        "rows": rows,
        "elapsed_seconds": time.time() - started,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    return out


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--M", type=int, nargs="+", default=list(DEFAULT_M))
    parser.add_argument("--c-multiple", type=int, nargs="+", default=list(DEFAULT_C_MULTIPLES))
    parser.add_argument("--enumerate-limit", type=int, default=12)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/falsification_pruning/results/prk_multichar_chargeability_budget.json"),
    )
    return parser


def main() -> None:
    args = make_parser().parse_args()
    print(json.dumps(run(args), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

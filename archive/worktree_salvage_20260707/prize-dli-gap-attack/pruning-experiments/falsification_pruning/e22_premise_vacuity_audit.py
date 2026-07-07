#!/usr/bin/env python3
"""Audit literal versus pricing-useful E22 common-tail premises.

The downstream E22 amber chain consumes a premise A: an actual common-tail /
kernel-invariance or tail-removed quotient-factor certificate.  This script
stress-tests A itself, not the proved implications downstream from A.

The key adversarial issue is vacuity.  If the certificate allows M_i = n, then
any challenger whose touched support has size < n has a literal all-tail
certificate: take B to be every touched point and leave no non-tail quotient
fiber.  That satisfies the formal kernel-invariance statement but may be too
weak for the intended pricing premise.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
import time
from pathlib import Path
from typing import Any


sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[2]
CORE = ROOT / "nodes" / "worst_word_challenger_pricing" / "notes"
sys.path.insert(0, str(CORE))

from e22_core import classify_pattern, pattern, polynomial_through, sunflower_word  # noqa: E402


DEFAULT_ROWS = (
    (16, 2, 1),
    (16, 4, 1),
    (16, 8, 1),
    (16, 2, 2),
    (16, 4, 2),
    (16, 8, 2),
    (32, 2, 1),
    (32, 4, 1),
    (32, 2, 2),
)


def parse_row(text: str) -> tuple[int, int, int]:
    parts = text.split(",")
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("row must be n,k,sigma")
    return tuple(map(int, parts))  # type: ignore[return-value]


def poly_eval(poly: tuple[int, ...], x: int) -> int:
    value = 0
    for coeff in reversed(poly):
        value = (value * x + coeff) % 193
    return value


def cyclic_layouts(n: int, cap: int) -> list[str]:
    steps = [s for s in range(1, n) if math.gcd(s, n) == 1]
    chosen = steps[:cap]
    if 1 not in chosen:
        chosen.insert(0, 1)
    return [f"cyclic_step_{s}" for s in chosen]


def listed_polys(word: dict[str, Any], deadline: float) -> dict[tuple[int, ...], dict[str, Any]]:
    found: dict[tuple[int, ...], dict[str, Any]] = {}
    for serial, indices in enumerate(itertools.combinations(range(word["n"]), word["s"])):
        if (serial & 0x3FFF) == 0 and time.time() > deadline:
            raise TimeoutError
        poly = polynomial_through(list(indices), word["domain"], word["values"], word["k"])
        if poly is None:
            continue
        rec = pattern(poly, word)
        if rec["agreement"] >= word["s"]:
            found[poly] = rec
    return found


def touched_support(poly: tuple[int, ...], word: dict[str, Any]) -> tuple[int, ...]:
    out = []
    for petal in word["petals"]:
        for idx in petal:
            if poly_eval(poly, word["domain"][idx]) == word["values"][idx] % 193:
                out.append(idx)
    return tuple(sorted(out))


def dyadic_moduli(n: int, sigma: int) -> list[int]:
    out = []
    m = 1
    while m <= n:
        if n % m == 0 and m > sigma:
            out.append(m)
        m *= 2
    return out


def fiber_indices(n: int, M: int, idx: int) -> set[int]:
    step = n // M
    residue = idx % step
    return {residue + j * step for j in range(M)}


def retained_full_fiber_count(n: int, M: int, support: set[int]) -> int:
    seen: set[frozenset[int]] = set()
    for idx in support:
        fib = frozenset(fiber_indices(n, M, idx))
        if fib <= support:
            seen.add(fib)
    return len(seen)


def analyze_cell(
    n: int,
    k: int,
    sigma: int,
    layout: str,
    scalar_mode: str,
    deadline: float,
    max_examples: int,
) -> dict[str, Any]:
    word = sunflower_word(n, k, sigma, layout, scalar_mode)
    found = listed_polys(word, deadline)
    moduli = dyadic_moduli(n, sigma)
    rows = []
    counts = {
        "structured": 0,
        "literal_all_tail_available": 0,
        "has_any_retained_full_fiber": 0,
        "has_retained_full_fiber_at_proper_scale": 0,
        "all_tail_only": 0,
    }
    examples = []
    for poly, rec in found.items():
        cls = classify_pattern(rec, word["ell"])
        if cls not in {"mixed_petal", "full_petal"}:
            continue
        support = set(touched_support(poly, word))
        proper_moduli = [M for M in moduli if M < n]
        retained_any = max((retained_full_fiber_count(n, M, support) for M in moduli), default=0)
        retained_proper = max(
            (retained_full_fiber_count(n, M, support) for M in proper_moduli),
            default=0,
        )
        literal_all_tail = len(support) < n and n in moduli
        counts["structured"] += 1
        counts["literal_all_tail_available"] += int(literal_all_tail)
        counts["has_any_retained_full_fiber"] += int(retained_any > 0)
        counts["has_retained_full_fiber_at_proper_scale"] += int(retained_proper > 0)
        counts["all_tail_only"] += int(literal_all_tail and retained_proper == 0)
        row = {
            "poly": list(poly),
            "class": cls,
            "agreement": rec["agreement"],
            "petal_agreements": rec["petal_agreements"],
            "touched_support": sorted(support),
            "touched_size": len(support),
            "literal_all_tail_M": n if literal_all_tail else None,
            "max_retained_full_fibers_any_scale": retained_any,
            "max_retained_full_fibers_proper_scale": retained_proper,
        }
        rows.append(row)
        if len(examples) < max_examples and (literal_all_tail or retained_proper == 0):
            examples.append(row)
    return {
        "n": n,
        "k": k,
        "sigma": sigma,
        "layout": layout,
        "scalar_mode": scalar_mode,
        "s": word["s"],
        "ell": word["ell"],
        "list_size": len(found),
        "counts": counts,
        "examples": examples,
    }


def write_checkpoint(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    tmp.replace(path)


def run(args: argparse.Namespace) -> dict[str, Any]:
    started = time.time()
    deadline = started + args.seconds
    rows = args.row or list(DEFAULT_ROWS)
    out: dict[str, Any] = {
        "node": "e22_tail_removed_factor_manifest_payload",
        "downstream_amber_nodes": [
            "e22_common_tail_invariance_payload",
            "e22_cofactor_common_tail_kernel_invariance",
        ],
        "obligation_attacked": (
            "truth and nonvacuity of the common-tail/kernel-saturation premise A "
            "consumed by downstream amber implications"
        ),
        "rows": [],
        "verdict": "RUNNING",
    }
    write_checkpoint(args.output, out)
    for n, k, sigma in rows:
        layouts = args.layout or cyclic_layouts(n, args.layout_cap)
        for layout in layouts:
            for scalar_mode in args.scalar_mode:
                if time.time() > deadline - 2:
                    out["verdict"] = "TIMEOUT_PARTIAL"
                    out["elapsed_seconds"] = time.time() - started
                    write_checkpoint(args.output, out)
                    return out
                try:
                    out["rows"].append(
                        analyze_cell(n, k, sigma, layout, scalar_mode, deadline - 2, args.max_examples)
                    )
                except TimeoutError:
                    out["verdict"] = "TIMEOUT_PARTIAL"
                    out["elapsed_seconds"] = time.time() - started
                    write_checkpoint(args.output, out)
                    return out
                write_checkpoint(args.output, out)

    totals = {
        "cells": len(out["rows"]),
        "structured": 0,
        "literal_all_tail_available": 0,
        "has_any_retained_full_fiber": 0,
        "has_retained_full_fiber_at_proper_scale": 0,
        "all_tail_only": 0,
    }
    for row in out["rows"]:
        for key in totals:
            if key == "cells":
                continue
            totals[key] += int(row["counts"].get(key, 0))
    out["totals"] = totals
    if totals["structured"] and totals["literal_all_tail_available"] == totals["structured"]:
        if totals["has_retained_full_fiber_at_proper_scale"] == 0:
            out["verdict"] = "LITERAL_PREMISE_VACUOUS_ALL_TAIL_ONLY_IN_SCOPE"
        else:
            out["verdict"] = "LITERAL_PREMISE_ALWAYS_AVAILABLE_BUT_SOMETIMES_NONTRIVIAL"
    elif totals["structured"]:
        out["verdict"] = "LITERAL_PREMISE_NOT_AUTOMATIC_IN_SCOPE"
    else:
        out["verdict"] = "NO_STRUCTURED_CHALLENGERS_IN_SCOPE"
    out["elapsed_seconds"] = time.time() - started
    write_checkpoint(args.output, out)
    return out


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=55.0)
    parser.add_argument("--row", action="append", type=parse_row)
    parser.add_argument("--layout", action="append")
    parser.add_argument("--layout-cap", type=int, default=4)
    parser.add_argument("--scalar-mode", action="append", default=["linear", "geometric"])
    parser.add_argument("--max-examples", type=int, default=5)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/falsification_pruning/results/e22_premise_vacuity_audit.json"),
    )
    return parser


def main() -> None:
    payload = run(make_parser().parse_args())
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

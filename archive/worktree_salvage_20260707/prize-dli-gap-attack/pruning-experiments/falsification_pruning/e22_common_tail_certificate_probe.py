#!/usr/bin/env python3
"""E22 common-tail certificate falsification probe.

The earlier E22 source probe demanded pointwise covariance of the cofactor
polynomials H_i.  The current reduced payload is weaker and sharper:

    find one common tail B, dyadic local moduli M_i > t, |B| < min M_i,
    with T_i \\ B invariant under the M_i-kernel.

This script tests that certificate directly on actual listed E22 mixed/full
petal challengers from e22_core.py.  It also distinguishes vacuous all-tail
certificates from nontrivial certificates that retain at least one full quotient
fiber, because the all-tail option may be too weak for pricing.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
import time
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[2]
CORE = ROOT / "nodes" / "worst_word_challenger_pricing" / "notes"
sys.path.insert(0, str(CORE))

from e22_core import (  # noqa: E402
    classify_pattern,
    pattern,
    polynomial_through,
    sunflower_word,
)


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
        raise argparse.ArgumentTypeError("rows must have form n,k,sigma")
    return tuple(map(int, parts))  # type: ignore[return-value]


def listed_polys(word: dict[str, Any]) -> dict[tuple[int, ...], dict[str, Any]]:
    found: dict[tuple[int, ...], dict[str, Any]] = {}
    for indices in itertools.combinations(range(word["n"]), word["s"]):
        poly = polynomial_through(list(indices), word["domain"], word["values"], word["k"])
        if poly is None:
            continue
        rec = pattern(poly, word)
        if rec["agreement"] >= word["s"]:
            found[poly] = rec
    return found


def dyadic_moduli(n: int, t: int) -> list[int]:
    out = []
    m = 1
    while m <= n:
        if n % m == 0 and m > t:
            out.append(m)
        m *= 2
    return out


def fiber_indices(n: int, M: int, idx: int) -> set[int]:
    step = n // M
    residue = idx % step
    return {residue + j * step for j in range(M)}


def full_fiber_part(n: int, M: int, T: set[int]) -> set[int]:
    kept: set[int] = set()
    for idx in T:
        fib = fiber_indices(n, M, idx)
        if fib <= T:
            kept |= fib
    return kept


def petal_options(n: int, t: int, T: set[int]) -> list[dict[str, Any]]:
    opts = []
    for M in dyadic_moduli(n, t):
        kept = full_fiber_part(n, M, T)
        delete = T - kept
        opts.append(
            {
                "M": M,
                "delete": sorted(delete),
                "delete_size": len(delete),
                "kept": sorted(kept),
                "kept_size": len(kept),
                "all_tail": len(kept) == 0 and len(T) > 0,
            }
        )
    return opts


def certify_touched_sets(
    n: int,
    t: int,
    touched: list[dict[str, Any]],
    require_nonempty_somewhere: bool = False,
    require_nonempty_each: bool = False,
) -> tuple[bool, dict[str, Any]]:
    option_lists = [petal_options(n, t, set(item["T"])) for item in touched]
    best: dict[str, Any] | None = None
    checked = 0
    for combo in itertools.product(*option_lists):
        checked += 1
        B: set[int] = set()
        kept_total = 0
        min_M = min(opt["M"] for opt in combo) if combo else n
        for opt in combo:
            B.update(opt["delete"])
            kept_total += opt["kept_size"]
        each_nonempty = all(opt["kept_size"] > 0 for opt in combo)
        ok = len(B) < min_M
        if require_nonempty_somewhere:
            ok = ok and kept_total > 0
        if require_nonempty_each:
            ok = ok and each_nonempty
        candidate = {
            "tail": sorted(B),
            "tail_size": len(B),
            "min_M": min_M,
            "kept_total": kept_total,
            "each_touched_keeps_nonempty": each_nonempty,
            "options": [
                {
                    "petal_index": touched[i]["petal_index"],
                    "M": opt["M"],
                    "delete": opt["delete"],
                    "kept": opt["kept"],
                }
                for i, opt in enumerate(combo)
            ],
        }
        score = (
            candidate["tail_size"],
            -candidate["kept_total"],
            candidate["min_M"],
        )
        if best is None or score < (best["tail_size"], -best["kept_total"], best["min_M"]):
            best = candidate
        if ok:
            candidate["combinations_checked"] = checked
            return True, candidate
    return False, {"best": best, "combinations_checked": checked}


def challenger_payload(poly: tuple[int, ...], rec: dict[str, Any], word: dict[str, Any]) -> dict[str, Any]:
    touched = []
    agreement_by_petal = []
    for petal_index, petal in enumerate(word["petals"]):
        T = {
            idx
            for idx in petal
            if polynomial_value(poly, word, idx) == word["values"][idx] % 193
        }
        agreement_by_petal.append(len(T))
        if T:
            touched.append({"petal_index": petal_index, "T": sorted(T)})
    any_ok, any_cert = certify_touched_sets(word["n"], word["sigma"], touched)
    nontriv_ok, nontriv_cert = certify_touched_sets(
        word["n"], word["sigma"], touched, require_nonempty_somewhere=True
    )
    per_touched_ok, per_touched_cert = certify_touched_sets(
        word["n"], word["sigma"], touched, require_nonempty_each=True
    )
    return {
        "poly": list(poly),
        "class": classify_pattern(rec, word["ell"]),
        "agreement": rec["agreement"],
        "core_agreement": rec["core_agreement"],
        "background_agreement": rec["background_agreement"],
        "petal_agreements": agreement_by_petal,
        "touched": touched,
        "total_touched_points": sum(len(x["T"]) for x in touched),
        "any_common_tail_certificate": any_ok,
        "any_certificate": any_cert,
        "nontrivial_retained_fiber_certificate": nontriv_ok,
        "nontrivial_certificate": nontriv_cert,
        "per_touched_nonempty_certificate": per_touched_ok,
        "per_touched_certificate": per_touched_cert,
    }


def polynomial_value(poly: tuple[int, ...], word: dict[str, Any], idx: int) -> int:
    value = 0
    x = word["domain"][idx]
    for coeff in reversed(poly):
        value = (value * x + coeff) % 193
    return value


def analyze_cell(n: int, k: int, sigma: int, layout: str, scalar_mode: str, max_examples: int) -> dict[str, Any]:
    word = sunflower_word(n, k, sigma, layout, scalar_mode)
    found = listed_polys(word)
    structured_payloads = []
    counts = {
        "structured": 0,
        "any_certificate_pass": 0,
        "nontrivial_retained_pass": 0,
        "per_touched_nonempty_pass": 0,
    }
    examples: list[dict[str, Any]] = []
    for poly, rec in found.items():
        cls = classify_pattern(rec, word["ell"])
        if cls not in {"mixed_petal", "full_petal"}:
            continue
        counts["structured"] += 1
        payload = challenger_payload(poly, rec, word)
        if payload["any_common_tail_certificate"]:
            counts["any_certificate_pass"] += 1
        if payload["nontrivial_retained_fiber_certificate"]:
            counts["nontrivial_retained_pass"] += 1
        if payload["per_touched_nonempty_certificate"]:
            counts["per_touched_nonempty_pass"] += 1
        if len(examples) < max_examples and (
            not payload["nontrivial_retained_fiber_certificate"]
            or not payload["per_touched_nonempty_certificate"]
        ):
            examples.append(payload)
        structured_payloads.append(payload)

    return {
        "n": n,
        "k": k,
        "sigma": sigma,
        "s": word["s"],
        "ell": word["ell"],
        "layout": layout,
        "scalar_mode": scalar_mode,
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
    out: dict[str, Any] = {
        "node": "e22_tail_removed_factor_manifest_payload",
        "obligation_attacked": (
            "common-tail/kernel-invariance certificate for actual listed E22 "
            "mixed/full-petal challengers"
        ),
        "rows": [],
        "verdict": "RUNNING",
    }
    write_checkpoint(args.output, out)
    for n, k, sigma in args.row or DEFAULT_ROWS:
        if time.time() > deadline - 2:
            out["verdict"] = "TIMEOUT_PARTIAL"
            write_checkpoint(args.output, out)
            return out
        out["rows"].append(analyze_cell(n, k, sigma, args.layout, args.scalar_mode, args.max_examples))
        write_checkpoint(args.output, out)

    total = sum(row["counts"]["structured"] for row in out["rows"])
    any_pass = sum(row["counts"]["any_certificate_pass"] for row in out["rows"])
    nontriv = sum(row["counts"]["nontrivial_retained_pass"] for row in out["rows"])
    per_touched = sum(row["counts"]["per_touched_nonempty_pass"] for row in out["rows"])
    out["totals"] = {
        "structured": total,
        "any_certificate_pass": any_pass,
        "nontrivial_retained_pass": nontriv,
        "per_touched_nonempty_pass": per_touched,
    }
    if total and any_pass < total:
        out["verdict"] = "COMMON_TAIL_CERTIFICATE_FALSIFIER_CANDIDATE"
    elif total and nontriv == 0:
        out["verdict"] = "ONLY_VACUOUS_ALL_TAIL_CERTIFICATES_FOUND"
    elif total:
        out["verdict"] = "COMMON_TAIL_CERTIFICATES_FOUND"
    else:
        out["verdict"] = "NO_STRUCTURED_CHALLENGERS_IN_SCOPE"
    out["elapsed_seconds"] = time.time() - started
    write_checkpoint(args.output, out)
    return out


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=55.0)
    parser.add_argument("--row", action="append", type=parse_row)
    parser.add_argument("--layout", default="cyclic_step_1")
    parser.add_argument("--scalar-mode", default="linear")
    parser.add_argument("--max-examples", type=int, default=8)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/falsification_pruning/results/e22_common_tail_certificate_probe.json"),
    )
    return parser


def main() -> None:
    payload = run(make_parser().parse_args())
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

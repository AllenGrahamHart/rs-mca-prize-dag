#!/usr/bin/env python3
"""Check whether E22 all-tail certificates land in the pricing machinery.

Attempt 7 showed that the common-tail certificate is formal but vacuous on
small E22 challengers: all touched petal points can be deleted into the tail.
This probe asks the next falsifiable question:

    Are those all-tail supports still selected by the dyadic minimal-scale
    staircase machinery, or are they outside the pricing column?

It also checks whether several distinct codewords collapse to the same selected
support-scale representative, which would be a local injectivity/pricing warning.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
import time
from collections import Counter, defaultdict
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
        raise argparse.ArgumentTypeError("rows must have form n,k,sigma")
    return tuple(map(int, parts))  # type: ignore[return-value]


def poly_eval(poly: tuple[int, ...], x: int) -> int:
    value = 0
    for coeff in reversed(poly):
        value = (value * x + coeff) % 193
    return value


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


def fibers(n: int, M: int) -> list[frozenset[int]]:
    step = n // M
    return [frozenset(range(r, n, step)) for r in range(step)]


def recover_at_scale(n: int, M: int, support: set[int]) -> tuple[set[int], list[frozenset[int]]]:
    full = [fib for fib in fibers(n, M) if fib <= support]
    full_union = set().union(*full) if full else set()
    return set(support) - full_union, full


def selected_representative(n: int, t: int, support: set[int]) -> dict[str, Any] | None:
    admissible = []
    for M in dyadic_moduli(n, t):
        tail, full = recover_at_scale(n, M, support)
        if len(tail) < M:
            admissible.append((M, tail, full))
    if not admissible:
        return None
    M, tail, full = admissible[0]
    return {
        "M": M,
        "tail": sorted(tail),
        "tail_size": len(tail),
        "selected_fiber_count": len(full),
        "selected_fibers": [sorted(fib) for fib in full],
        "tail_only": len(full) == 0,
        "admissible_scales": [
            {"M": m, "tail_size": len(t), "selected_fiber_count": len(f)}
            for m, t, f in admissible
        ],
    }


def touched_support(poly: tuple[int, ...], word: dict[str, Any]) -> tuple[int, ...]:
    touched = []
    for petal in word["petals"]:
        for idx in petal:
            if poly_eval(poly, word["domain"][idx]) == word["values"][idx] % 193:
                touched.append(idx)
    return tuple(sorted(touched))


def full_agreement_support(poly: tuple[int, ...], word: dict[str, Any]) -> tuple[int, ...]:
    return tuple(
        idx
        for idx, x in enumerate(word["domain"])
        if poly_eval(poly, x) == word["values"][idx] % 193
    )


def analyze_cell(n: int, k: int, sigma: int, layout: str, scalar_mode: str, max_examples: int) -> dict[str, Any]:
    word = sunflower_word(n, k, sigma, layout, scalar_mode)
    found = listed_polys(word)
    representative_to_records: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    support_to_records: dict[tuple[int, ...], list[dict[str, Any]]] = defaultdict(list)
    class_counts = Counter()
    tail_size_counts = Counter()
    scale_counts = Counter()
    missing = []
    examples = []

    structured = 0
    tail_only = 0
    with_full_fibers = 0
    for poly, rec in found.items():
        cls = classify_pattern(rec, word["ell"])
        if cls not in {"mixed_petal", "full_petal"}:
            continue
        structured += 1
        class_counts[cls] += 1
        support = touched_support(poly, word)
        selected = selected_representative(n, sigma, set(support))
        if selected is None:
            if len(missing) < max_examples:
                missing.append({"poly": list(poly), "touched_support": list(support)})
            continue
        tail_size_counts[selected["tail_size"]] += 1
        scale_counts[selected["M"]] += 1
        if selected["tail_only"]:
            tail_only += 1
        else:
            with_full_fibers += 1
        rep_key = (
            selected["M"],
            tuple(selected["tail"]),
            tuple(tuple(fib) for fib in selected["selected_fibers"]),
        )
        record = {
            "poly": list(poly),
            "class": cls,
            "agreement": rec["agreement"],
            "petal_agreements": rec["petal_agreements"],
            "touched_support": list(support),
            "full_agreement_support": list(full_agreement_support(poly, word)),
        }
        representative_to_records[rep_key].append(record)
        support_to_records[support].append(record)
        if len(examples) < max_examples:
            examples.append(
                {
                    "poly": list(poly),
                    "class": cls,
                    "agreement": rec["agreement"],
                    "petal_agreements": rec["petal_agreements"],
                    "full_agreement_support": list(full_agreement_support(poly, word)),
                    "touched_support": list(support),
                    "selected": selected,
                }
            )

    rep_collisions = [
        {"representative": repr(key), "poly_count": len(records), "records": records[:max_examples]}
        for key, records in representative_to_records.items()
        if len(records) > 1
    ]
    support_collisions = [
        {"support": list(key), "poly_count": len(records), "records": records[:max_examples]}
        for key, records in support_to_records.items()
        if len(records) > 1
    ]
    return {
        "n": n,
        "k": k,
        "sigma": sigma,
        "s": word["s"],
        "ell": word["ell"],
        "layout": layout,
        "scalar_mode": scalar_mode,
        "list_size": len(found),
        "structured": structured,
        "class_counts": dict(class_counts),
        "selected_representatives": len(representative_to_records),
        "unique_touched_supports": len(support_to_records),
        "tail_only_representatives": tail_only,
        "with_full_fiber_representatives": with_full_fibers,
        "tail_size_counts": {str(k): v for k, v in sorted(tail_size_counts.items())},
        "selected_scale_counts": {str(k): v for k, v in sorted(scale_counts.items())},
        "missing_selected_representative": len(missing),
        "representative_collision_count": len(rep_collisions),
        "representative_collision_polynomial_excess": sum(
            item["poly_count"] - 1 for item in rep_collisions
        ),
        "support_collision_count": len(support_collisions),
        "support_collision_polynomial_excess": sum(
            item["poly_count"] - 1 for item in support_collisions
        ),
        "representative_collision_examples": rep_collisions[:max_examples],
        "support_collision_examples": support_collisions[:max_examples],
        "examples": examples,
        "missing_examples": missing,
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
        "node": "e22_challenger_staircase_pricing",
        "obligation_attacked": (
            "coverage and injectivity of all-tail E22 common-tail certificates "
            "by the dyadic minimal-scale staircase pricing machinery"
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

    total_structured = sum(row["structured"] for row in out["rows"])
    missing = sum(row["missing_selected_representative"] for row in out["rows"])
    collisions = sum(row["representative_collision_count"] for row in out["rows"])
    collision_excess = sum(
        row["representative_collision_polynomial_excess"] for row in out["rows"]
    )
    support_collisions = sum(row["support_collision_count"] for row in out["rows"])
    support_collision_excess = sum(
        row["support_collision_polynomial_excess"] for row in out["rows"]
    )
    full_fiber = sum(row["with_full_fiber_representatives"] for row in out["rows"])
    out["totals"] = {
        "structured": total_structured,
        "missing_selected_representative": missing,
        "representative_collision_count": collisions,
        "representative_collision_polynomial_excess": collision_excess,
        "support_collision_count": support_collisions,
        "support_collision_polynomial_excess": support_collision_excess,
        "with_full_fiber_representatives": full_fiber,
    }
    if missing:
        out["verdict"] = "TAIL_ONLY_PRICING_OMISSION_CANDIDATE"
    elif collisions:
        out["verdict"] = "SELECTED_REPRESENTATIVE_COLLISION_CANDIDATE"
    elif total_structured and full_fiber == 0:
        out["verdict"] = "ALL_STRUCTURED_CHALLENGERS_TAIL_ONLY_BUT_SELECTED"
    elif total_structured:
        out["verdict"] = "STRUCTURED_CHALLENGERS_SELECTED"
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
    parser.add_argument("--max-examples", type=int, default=6)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/falsification_pruning/results/e22_tail_only_pricing_coverage.json"),
    )
    return parser


def main() -> None:
    payload = run(make_parser().parse_args())
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Falsification probe for e22_mixed_petal_covariance.

The live E22 crux is source achievability:

    Does the actual E22/sunflower source supply BOTH pointwise covariance
    H_i(eta x)=eta^e H_i(x) and off-tail exhaustivity, after one bounded
    common tail, or were those clauses only identified as necessary?

This script uses the repo's executable E22 toy machinery
`nodes/worst_word_challenger_pricing/notes/e22_core.py`.  For every listed
mixed/full-petal challenger in selected local cells, it builds the actual
cofactor polynomials

    H_i = U L_{Z\\C} - a_i L_{C\\Z}

from `e22_agreement_cofactor_equations`, and searches for a certificate:

    - dyadic local moduli M_i | n with M_i > t;
    - character residues e_i mod M_i with pointwise covariance on mu_n;
    - one common tail B whose size is < min_i M_i;
    - off-tail exhaustivity on each touched petal:
        T_i \\ B = {x in P_i \\ B : H_i(x)=0}.

If no such package exists for a challenger, the source-achievability claim is
under adversarial pressure.  The run is local/toy-scale and is not a proof.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
CORE = ROOT / "nodes" / "worst_word_challenger_pricing" / "notes"
sys.path.insert(0, str(CORE))

from e22_core import (  # noqa: E402
    P,
    classify_pattern,
    locator,
    pattern,
    poly_add,
    poly_eval,
    poly_mul,
    poly_scale,
    polynomial_through,
    sunflower_word,
    trim,
)


DEFAULT_ROWS = (
    (16, 2, 1),
    (16, 4, 1),
    (16, 8, 1),
    (16, 2, 2),
    (16, 4, 2),
    (16, 8, 2),
)


def parse_row(text: str) -> tuple[int, int, int]:
    parts = text.split(",")
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("rows must have form n,k,sigma")
    n, k, sigma = map(int, parts)
    if n <= 0 or k <= 0 or sigma <= 0:
        raise argparse.ArgumentTypeError("need positive n,k,sigma")
    return n, k, sigma


def div_exact(poly: tuple[int, ...], divisor: tuple[int, ...]) -> tuple[int, ...]:
    rem = list(poly)
    den = list(divisor)
    if not den:
        raise ZeroDivisionError
    out = [0] * max(1, len(rem) - len(den) + 1)
    inv_lead = pow(den[-1], -1, P)
    while len(rem) >= len(den) and rem:
        coeff = rem[-1] * inv_lead % P
        shift = len(rem) - len(den)
        out[shift] = coeff
        for i, d in enumerate(den):
            rem[shift + i] = (rem[shift + i] - coeff * d) % P
        while rem and rem[-1] == 0:
            rem.pop()
    if rem:
        raise ValueError(f"nonzero remainder {rem}")
    return trim(out, P)


def poly_sub(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return poly_add(left, poly_scale(right, -1, P), P)


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


def is_covariant_on_domain(poly: tuple[int, ...], word: dict[str, Any], M: int, e: int) -> bool:
    n = word["n"]
    step = n // M
    eta_e = pow(word["domain"][step], e, P)
    for idx, x in enumerate(word["domain"]):
        y_idx = (idx + step) % n
        lhs = poly_eval(poly, word["domain"][y_idx], P)
        rhs = eta_e * poly_eval(poly, x, P) % P
        if lhs != rhs:
            return False
    return True


@dataclass(frozen=True)
class PetalOption:
    petal_index: int
    M: int
    e: int
    tail_needed: frozenset[int]


def petal_options(
    H: tuple[int, ...],
    word: dict[str, Any],
    petal_index: int,
    T: set[int],
    moduli: list[int],
) -> list[PetalOption]:
    petal = set(word["petals"][petal_index])
    zeros = {idx for idx in petal if poly_eval(H, word["domain"][idx], P) == 0}
    needed = frozenset(zeros ^ T)
    opts: list[PetalOption] = []
    for M in moduli:
        if len(needed) >= M:
            continue
        for e in range(M):
            if is_covariant_on_domain(H, word, M, e):
                opts.append(PetalOption(petal_index, M, e, needed))
    return opts


def choose_common_tail(option_lists: list[list[PetalOption]]) -> tuple[bool, dict[str, Any]]:
    if not option_lists:
        return True, {"tail": [], "options": []}
    if any(not opts for opts in option_lists):
        return False, {
            "reason": "some_touched_petal_has_no_covariant_exhaustive_option",
            "empty_option_petals": [i for i, opts in enumerate(option_lists) if not opts],
        }

    best: dict[str, Any] | None = None
    # Local cells have few touched petals.  Cap combinations defensively.
    checked = 0
    for combo in itertools.product(*option_lists):
        checked += 1
        if checked > 200_000:
            break
        tail: set[int] = set()
        min_M = min(opt.M for opt in combo)
        for opt in combo:
            tail.update(opt.tail_needed)
        candidate = {
            "tail": sorted(tail),
            "tail_size": len(tail),
            "min_M": min_M,
            "options": [
                {"petal_index": opt.petal_index, "M": opt.M, "e": opt.e, "tail_needed": sorted(opt.tail_needed)}
                for opt in combo
            ],
        }
        if best is None or (candidate["tail_size"], -candidate["min_M"]) < (best["tail_size"], -best["min_M"]):
            best = candidate
        if len(tail) < min_M:
            candidate["combinations_checked"] = checked
            return True, candidate
    return False, {
        "reason": "common_tail_bound_failed",
        "best": best,
        "combinations_checked": checked,
    }


def cofactor_payload(poly: tuple[int, ...], rec: dict[str, Any], word: dict[str, Any], t: int) -> dict[str, Any]:
    core = set(word["core"])
    zero_zone = set(word["core"]) | set(word["background"])
    Z = sorted(idx for idx in zero_zone if poly_eval(poly, word["domain"][idx], P) == 0)
    LZ = locator([word["domain"][idx] for idx in Z], P)
    U = div_exact(poly, LZ)
    Z_not_C = sorted(idx for idx in Z if idx not in core)
    C_not_Z = sorted(idx for idx in word["core"] if idx not in set(Z))
    L_z_not_c = locator([word["domain"][idx] for idx in Z_not_C], P)
    L_c_not_z = locator([word["domain"][idx] for idx in C_not_Z], P)
    moduli = dyadic_moduli(word["n"], t)

    option_lists: list[list[PetalOption]] = []
    petal_summaries = []
    for petal_index, (scalar, petal) in enumerate(zip(word["scalars"], word["petals"])):
        T = {
            idx
            for idx in petal
            if poly_eval(poly, word["domain"][idx], P) == word["values"][idx] % P
        }
        if not T:
            continue
        left = poly_mul(U, L_z_not_c, P)
        right = poly_scale(L_c_not_z, scalar, P)
        H = poly_sub(left, right)
        # Verify the divisor/evaluation part before testing stronger source clauses.
        divisor_ok = all(poly_eval(H, word["domain"][idx], P) == 0 for idx in T)
        opts = petal_options(H, word, petal_index, T, moduli)
        option_lists.append(opts)
        zeros = {
            idx for idx in petal if poly_eval(H, word["domain"][idx], P) == 0
        }
        petal_summaries.append(
            {
                "petal_index": petal_index,
                "T": sorted(T),
                "zeros_on_petal": sorted(zeros),
                "off_tail_symdiff": sorted(zeros ^ T),
                "divisor_evaluation_ok": divisor_ok,
                "option_count": len(opts),
                "candidate_moduli_with_covariance": sorted({opt.M for opt in opts}),
            }
        )

    passed, certificate = choose_common_tail(option_lists)
    return {
        "class": classify_pattern(rec, word["ell"]),
        "agreement": rec["agreement"],
        "petal_agreements": rec["petal_agreements"],
        "core_agreement": rec["core_agreement"],
        "background_agreement": rec["background_agreement"],
        "Z_zero_zone": Z,
        "t_used": t,
        "candidate_moduli": moduli,
        "petals": petal_summaries,
        "source_certificate_found": passed,
        "source_certificate": certificate,
    }


def analyze_cell(n: int, k: int, sigma: int, layout: str, scalar_mode: str, max_examples: int) -> dict[str, Any]:
    word = sunflower_word(n, k, sigma, layout, scalar_mode)
    t = sigma
    found = listed_polys(word)
    structured = []
    failures = []
    passes = 0
    for poly, rec in found.items():
        cls = classify_pattern(rec, word["ell"])
        if cls not in {"mixed_petal", "full_petal"}:
            continue
        payload = cofactor_payload(poly, rec, word, t)
        structured.append(payload)
        if payload["source_certificate_found"]:
            passes += 1
        elif len(failures) < max_examples:
            failures.append({"poly": list(poly), "payload": payload})

    return {
        "n": n,
        "k": k,
        "sigma": sigma,
        "s": word["s"],
        "ell": word["ell"],
        "layout": layout,
        "scalar_mode": scalar_mode,
        "list_size": len(found),
        "structured_challengers": len(structured),
        "source_certificate_passes": passes,
        "source_certificate_failures": len(structured) - passes,
        "failure_examples": failures,
    }


def write_checkpoint(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def run(args: argparse.Namespace) -> dict[str, Any]:
    started = time.time()
    deadline = started + args.seconds
    out: dict[str, Any] = {
        "node": "e22_mixed_petal_covariance",
        "obligation_attacked": "source achievability of pointwise covariance plus off-tail exhaustivity",
        "scope": "repo E22 local sunflower cells from e22_core.py",
        "rows": [],
        "verdict": "RUNNING",
    }
    for n, k, sigma in args.row or DEFAULT_ROWS:
        if time.time() > deadline - 2:
            out["verdict"] = "TIMEOUT_PARTIAL"
            write_checkpoint(args.output, out)
            return out
        out["rows"].append(analyze_cell(n, k, sigma, args.layout, args.scalar_mode, args.max_examples))
        write_checkpoint(args.output, out)

    total_structured = sum(row["structured_challengers"] for row in out["rows"])
    total_failures = sum(row["source_certificate_failures"] for row in out["rows"])
    out["elapsed_seconds"] = time.time() - started
    if total_structured and total_failures:
        out["verdict"] = "SOURCE_CERTIFICATE_FAILURES_FOUND"
    elif total_structured:
        out["verdict"] = "COMPLETE_NO_SOURCE_FAILURES_FOUND"
    else:
        out["verdict"] = "COMPLETE_NO_STRUCTURED_CHALLENGERS_IN_SCOPE"
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
        default=Path("experiments/falsification_pruning/results/e22_source_achievability_probe.json"),
    )
    return parser


def main() -> None:
    args = make_parser().parse_args()
    payload = run(args)
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

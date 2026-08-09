#!/usr/bin/env python3
"""E22 challenger-class census -- Modal app rs-mca-e22.

Pre-registered E22 spec (evidence_plan_codex.md, section E22), verbatim:

    TARGET    worst_word_planted (revised) / list_planted_arithmetic
    QUESTION  does planted + the E15 structured challenger class EXHAUST
              the extremal words, and what is the challenger's exact count
              formula?
    PRIOR     ~70% two classes suffice
    METHOD    extend the E15 search at sigma = 1..3, n = 16..64: enumerate
              all words beating 0.9 x planted list; classify against the
              two known classes; extract the challenger count formula
    INTERPRET two classes exhaust => QL.5's two-column arithmetic closes
              the repair | a THIRD class => iterate the E15 protocol
              (enlarge, price, re-census) -- the endgame absorbs it

Reconstruction: the E15 (#197) search code was NOT lost -- it survives
byte-identical (md5 b3561a606ff30a581dff1895ea9de2e9) as
`experimental/scripts/verify_e15_worst_word_challenge.py` in the rs-mca
worktrees.  The field/polynomial/sunflower machinery below is copied VERBATIM
from that verifier; only the census driver (E22 two-column classification +
the extended sigma=1..3, n=16..64 sweep) is new.

Toy cell: F_193 subgroup domain; core = first k-1 layout points; petals of
size ell=sigma+1; planted word value = scalar_p * L_core on petal p, 0 else;
planted codewords {scalar_p * L_core} (M = petal_count of them, each agreeing
on core (k-1) + one petal (ell) = k+sigma = s points).  The LIST at crossing
radius s is all deg-<k polys agreeing on >= s points.  A challenger is a
NON-planted codeword in that list; the E15 finding is that at sigma=1 the list
beats M via petal-structured (mixed/full petal) challengers.

E22 columns:  planted | challenger (mixed_petal + full_petal) | UNCLASSIFIED
UNCLASSIFIED (one_petal_nonplanted, background_or_core_only) = third-class alarm.
NOTE: the third-class alarm is meaningfully tested ONLY on cells searched
EXHAUSTIVELY.  Structured scans (used where exhaustive enumeration is
infeasible) only generate petal-structured candidates by construction and
therefore cannot detect an unstructured third class; they are secondary
evidence, exactly as in the original E15 packet.

Run:  ~/.venvs/modal/bin/modal run --detach e22_census_modal.py
"""

from __future__ import annotations

import itertools
import json
import math
import random
import time
from collections import Counter
from typing import Any

import modal

P = 193

# Exhaustive iff binom(n, s) <= this; else structured scan (E15-style).
EXHAUSTIVE_CAP = 30_000_000

app = modal.App("rs-mca-e22")
image = modal.Image.debian_slim(python_version="3.11")


# ========================================================================
#  VERBATIM E15 machinery
# ========================================================================

def inv_mod(x: int, p: int = P) -> int:
    return pow(x % p, -1, p)


def trim(poly: list[int], p: int = P) -> tuple[int, ...]:
    out = [x % p for x in poly]
    while out and out[-1] == 0:
        out.pop()
    return tuple(out)


def poly_mul(left, right, p: int = P):
    out = [0] * (len(left) + len(right) - 1)
    for i, ai in enumerate(left):
        for j, bj in enumerate(right):
            out[i + j] = (out[i + j] + ai * bj) % p
    return trim(out, p)


def poly_add(left, right, p: int = P):
    size = max(len(left), len(right))
    out = [0] * size
    for idx in range(size):
        out[idx] = ((left[idx] if idx < len(left) else 0)
                    + (right[idx] if idx < len(right) else 0)) % p
    return trim(out, p)


def poly_scale(poly, scalar, p: int = P):
    return trim([scalar * coeff for coeff in poly], p)


def poly_eval(poly, x, p: int = P):
    value = 0
    for coeff in reversed(poly):
        value = (value * x + coeff) % p
    return value


def interpolate(points, p: int = P):
    poly = ()
    for i, (x_i, y_i) in enumerate(points):
        basis = (1,)
        denom = 1
        for j, (x_j, _) in enumerate(points):
            if i == j:
                continue
            basis = poly_mul(basis, ((-x_j) % p, 1), p)
            denom = (denom * (x_i - x_j)) % p
        term = poly_scale(basis, y_i * inv_mod(denom, p), p)
        poly = poly_add(poly, term, p)
    return poly


def polynomial_through(indices, domain, values, k):
    if len(indices) < k:
        raise ValueError("need at least k interpolation points")
    base = indices[:k]
    poly = interpolate([(domain[idx], values[idx]) for idx in base], P)
    if len(poly) > k:
        return None
    if all(poly_eval(poly, domain[idx], P) == values[idx] % P for idx in indices):
        return poly
    return None


def factor_int(n: int):
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


def primitive_root(p: int = P) -> int:
    factors = factor_int(p - 1)
    for candidate in range(2, p):
        if all(pow(candidate, (p - 1) // factor, p) != 1 for factor in factors):
            return candidate
    raise ValueError("no primitive root")


def subgroup_domain(n: int, p: int = P):
    if (p - 1) % n:
        raise ValueError(f"n={n} does not divide p-1={p - 1}")
    generator = pow(primitive_root(p), (p - 1) // n, p)
    domain = [pow(generator, idx, p) for idx in range(n)]
    if len(set(domain)) != n:
        raise AssertionError("wrong subgroup order")
    return domain


def locator(roots, p: int = P):
    poly = (1,)
    for root in roots:
        poly = poly_mul(poly, ((-root) % p, 1), p)
    return poly


def cyclic_order(n: int, step: int):
    if not 0 <= step < n:
        raise ValueError(step)
    if step == 0:
        return list(range(n))
    if math.gcd(step, n) != 1:
        raise ValueError("step must be coprime to n")
    return [(step * idx) % n for idx in range(n)]


def shuffled_order(n: int, seed: int):
    out = list(range(n))
    random.Random(seed).shuffle(out)
    return out


def layout_order(n: int, mode: str):
    if mode.startswith("cyclic_step_"):
        return cyclic_order(n, int(mode.rsplit("_", 1)[1]))
    if mode.startswith("shuffle_"):
        return shuffled_order(n, int(mode.rsplit("_", 1)[1]))
    raise ValueError(mode)


def scalar_sequence(count: int, mode: str, p: int = P):
    if mode == "linear":
        return list(range(1, count + 1))
    if mode == "geometric":
        out = []
        value = 1
        for _ in range(count):
            out.append(value)
            value = (value * 5) % p
        if len(set(out)) != count:
            raise AssertionError("geometric scalars repeated")
        return out
    raise ValueError(mode)


def sunflower_word(n, k, sigma, layout, scalar_mode):
    domain = subgroup_domain(n, P)
    ell = sigma + 1
    order = layout_order(n, layout)
    core = sorted(order[: k - 1])
    rest = order[k - 1:]
    petal_count = len(rest) // ell
    petals = [sorted(rest[i * ell:(i + 1) * ell]) for i in range(petal_count)]
    background = sorted(rest[petal_count * ell:])
    core_locator = locator([domain[idx] for idx in core], P)
    scalars = scalar_sequence(petal_count, scalar_mode, P)
    values = [0] * n
    for scalar, petal in zip(scalars, petals):
        for idx in petal:
            values[idx] = scalar * poly_eval(core_locator, domain[idx], P) % P
    planted = {poly_scale(core_locator, scalar, P) for scalar in scalars}
    return {
        "n": n, "k": k, "sigma": sigma, "s": k + sigma, "ell": ell,
        "layout": layout, "scalar_mode": scalar_mode, "domain": domain,
        "core": core, "petals": petals, "background": background,
        "values": values, "core_locator": core_locator, "scalars": scalars,
        "planted_polynomials": planted,
    }


def agreement_set(poly, word):
    return tuple(idx for idx, x in enumerate(word["domain"])
                 if poly_eval(poly, x, P) == word["values"][idx] % P)


def pattern(poly, word):
    agreement = set(agreement_set(poly, word))
    return {
        "is_planted": poly in word["planted_polynomials"],
        "agreement": len(agreement),
        "core_agreement": len(agreement & set(word["core"])),
        "background_agreement": len(agreement & set(word["background"])),
        "petal_agreements": [len(agreement & set(petal)) for petal in word["petals"]],
    }


def classify_pattern(record, ell):
    if record["is_planted"]:
        return "planted"
    petal_counts = record["petal_agreements"]
    full = sum(1 for count in petal_counts if count == ell)
    touched = sum(1 for count in petal_counts if count)
    if full >= 2 and full == touched:
        return "full_petal"
    if touched >= 2:
        return "mixed_petal"
    if touched == 1:
        return "one_petal_nonplanted"
    return "background_or_core_only"


# ========================================================================
#  E22 census cells
# ========================================================================

CHALLENGER_CLASSES = {"full_petal", "mixed_petal"}
UNCLASSIFIED_CLASSES = {"one_petal_nonplanted", "background_or_core_only"}


def _finish(word, found, kind, extra):
    ell = word["ell"]
    class_counts = Counter(classify_pattern(rec, ell) for rec in found.values())
    planted_count = len(word["planted_polynomials"])
    classified_planted = class_counts.get("planted", 0)
    classified_challenger = sum(class_counts.get(c, 0) for c in CHALLENGER_CLASSES)
    unclassified = sum(class_counts.get(c, 0) for c in UNCLASSIFIED_CLASSES)
    examples = []
    for poly, rec in found.items():
        if poly in word["planted_polynomials"]:
            continue
        examples.append({
            "coeffs": list(poly),
            "class": classify_pattern(rec, ell),
            "petal_agreements": rec["petal_agreements"],
            "core_agreement": rec["core_agreement"],
        })
        if len(examples) >= 6:
            break
    out = {
        "kind": kind, "n": word["n"], "k": word["k"], "sigma": word["sigma"],
        "s": word["s"], "ell": ell, "layout": word["layout"],
        "scalar_mode": word["scalar_mode"], "petal_count_M": len(word["petals"]),
        "background_size": len(word["background"]),
        "list_size": len(found), "planted_count": planted_count,
        "nonplanted_count": len(found) - classified_planted,
        "classified_planted": classified_planted,
        "classified_challenger": classified_challenger,
        "unclassified": unclassified,
        "beats_planted": len(found) > planted_count,
        "beats_0p9_planted": len(found) > 0.9 * planted_count,
        "class_counts": dict(sorted(class_counts.items())),
        "nonplanted_examples": examples,
    }
    out.update(extra)
    return out


def exact_cell(n, k, sigma, layout, scalar_mode):
    word = sunflower_word(n, k, sigma, layout, scalar_mode)
    found = {}
    for indices in itertools.combinations(range(word["n"]), word["s"]):
        poly = polynomial_through(list(indices), word["domain"], word["values"], word["k"])
        if poly is None:
            continue
        rec = pattern(poly, word)
        if rec["agreement"] >= word["s"]:
            found[poly] = rec
    return _finish(word, found, "exact_all_agreement_sets",
                   {"exhaustive": True,
                    "agreement_sets_checked": math.comb(word["n"], word["s"])})


def structured_cell(n, k, sigma, layout, scalar_mode, max_excess=2):
    """E15-style structured scan: full-petal bounded-excess + two-petal pencil.
    Secondary evidence only -- generates petal-structured candidates by
    construction, so it CANNOT detect an unstructured third class."""
    word = sunflower_word(n, k, sigma, layout, scalar_mode)
    core, petals, ell = word["core"], word["petals"], word["ell"]
    domain = word["domain"]
    found = {}
    candidates = 0
    # The full-petal sub-scan ranges over subsets of petals (2^M) times core
    # combinations; at large M (e.g. n=64) this explodes, so guard it and fall
    # back to pencil-only, exactly as the original E15 n=64 cells did.
    dmax = min(len(core), ell + max_excess)
    fullpetal_estimate = (2 ** len(petals)) * math.comb(len(core), dmax) if len(core) else 0
    run_fullpetal = fullpetal_estimate <= 5_000_000
    # (a) full-petal bounded cofactor-excess scan
    for excess in range(max_excess + 1) if run_fullpetal else range(0):
        d = ell + excess
        if d > len(core):
            continue
        for touched_count in range(2, len(petals) + 1):
            if d > (touched_count - 1) * ell:
                continue
            for touched in itertools.combinations(range(len(petals)), touched_count):
                touched_points = sorted(pt for pi in touched for pt in petals[pi])
                for missed_core in itertools.combinations(core, d):
                    agreement = sorted((set(core) - set(missed_core)) | set(touched_points))
                    if len(agreement) < word["s"]:
                        continue
                    candidates += 1
                    poly = polynomial_through(agreement, domain, word["values"], word["k"])
                    if poly is None or poly in word["planted_polynomials"]:
                        continue
                    rec = pattern(poly, word)
                    if rec["agreement"] >= word["s"]:
                        found[poly] = rec
    # (b) minimal-defect two-petal locator pencil (only when core >= ell)
    pencil_checked = 0
    if len(core) >= ell:
        petal_locators = [locator([domain[i] for i in petal], P) for petal in petals]
        missed_core_locators = [
            (mc, locator([domain[i] for i in mc], P))
            for mc in itertools.combinations(core, ell)
        ]
        for i, j in itertools.combinations(range(len(petals)), 2):
            left, right = petal_locators[i], petal_locators[j]
            pencil = {
                poly_add(poly_scale(left, 1 + beta, P), poly_scale(right, -beta, P), P): beta
                for beta in range(P)
            }
            for mc, ld in missed_core_locators:
                pencil_checked += 1
                if ld in pencil:
                    # realize the pencil solution as an actual codeword & classify
                    beta = pencil[ld]
                    cand = poly_add(poly_scale(left, 1 + beta, P), poly_scale(right, -beta, P), P)
                    if len(cand) <= word["k"] and cand not in word["planted_polynomials"]:
                        rec = pattern(cand, word)
                        if rec["agreement"] >= word["s"]:
                            found[cand] = rec
    return _finish(word, found, "structured_full_petal_and_two_petal_pencil",
                   {"exhaustive": False, "max_excess": max_excess,
                    "fullpetal_scan_ran": run_fullpetal,
                    "fullpetal_candidates_checked": candidates,
                    "pencil_pairs_checked": pencil_checked})


def cell_task(spec):
    n, k, sigma, layout, scalar_mode = spec
    s = k + sigma
    t0 = time.time()
    if math.comb(n, s) <= EXHAUSTIVE_CAP:
        out = exact_cell(n, k, sigma, layout, scalar_mode)
    else:
        out = structured_cell(n, k, sigma, layout, scalar_mode)
    out["wall_seconds"] = round(time.time() - t0, 2)
    return out


def build_plan():
    """The E22 sweep: sigma=1..3, n=16..64, toy official rates k/n in
    {1/16,1/8,1/4,1/2}.  Cheap cells get 2 layouts x 2 scalars; heavier
    exhaustive cells get a single representative layout to bound cost."""
    plan = []
    RATE_K = {16: [1, 2, 4, 8], 32: [2, 4, 8, 16], 64: [4, 8, 16, 32]}
    layouts_by_n = {16: ["cyclic_step_1", "shuffle_1601"],
                    32: ["cyclic_step_1", "shuffle_3201"],
                    64: ["cyclic_step_1", "shuffle_6401"]}
    scalars = ["linear", "geometric"]
    for n in (16, 32, 64):
        for k in RATE_K[n]:
            for sigma in (1, 2, 3):
                s = k + sigma
                if s >= n:
                    continue
                comb = math.comb(n, s)
                # cost tier -> layout/scalar breadth
                if comb <= 1_000_000:
                    variants = [(lay, sc) for lay in layouts_by_n[n] for sc in scalars]
                elif comb <= EXHAUSTIVE_CAP:
                    variants = [("cyclic_step_1", "linear")]  # heavy exhaustive: one rep
                else:
                    # structured scan cells: E15 layout/scalar breadth (cheap)
                    variants = [(lay, sc) for lay in layouts_by_n[n] for sc in scalars]
                for lay, sc in variants:
                    plan.append((n, k, sigma, lay, sc))
    return plan


def gate_check():
    """Re-run the E15 reproduction gate before the census."""
    results = {}
    for k in (1, 2, 4, 8):
        cell = exact_cell(16, k, 1, "cyclic_step_1", "linear")
        results[k] = (cell["beats_planted"], cell["classified_challenger"],
                      cell["unclassified"])
    # gate passes iff a non-planted structured challenger beats planted at
    # sigma=1 for k in {2,4,8}, k=1 does not, and sigma=1 UNCLASSIFIED is 0.
    ok = (not results[1][0]
          and all(results[k][0] and results[k][1] > 0 for k in (2, 4, 8))
          and all(results[k][2] == 0 for k in (1, 2, 4, 8)))
    return ok, results


@app.function(image=image, cpu=8.0, memory=8192, timeout=6 * 3600)
def run_census():
    import multiprocessing as mp

    gate_ok, gate_results = gate_check()
    print(f"[modal] gate re-run: passed={gate_ok} details={gate_results}", flush=True)
    if not gate_ok:
        return {"gate_passed": False, "gate_results": gate_results,
                "interpretation": "GATE_FAILED_CENSUS_ABORTED"}

    plan = build_plan()
    print(f"[modal] census plan: {len(plan)} cells", flush=True)
    t0 = time.time()
    cells = []
    with mp.Pool(processes=8) as pool:
        for i, cell in enumerate(pool.imap_unordered(cell_task, plan), 1):
            cells.append(cell)
            if i % 10 == 0 or i == len(plan):
                print(f"[modal] {i}/{len(plan)} cells done "
                      f"(elapsed {time.time()-t0:.0f}s)", flush=True)

    exhaustive = [c for c in cells if c["exhaustive"]]
    structured = [c for c in cells if not c["exhaustive"]]
    # third-class alarm only meaningful on exhaustive cells
    total_unclassified_exhaustive = sum(c["unclassified"] for c in exhaustive)
    beating = [c for c in cells if c["beats_0p9_planted"]]

    # challenger-count grid for formula extraction (exhaustive cells only)
    challenger_grid = sorted(
        [{"n": c["n"], "k": c["k"], "sigma": c["sigma"], "ell": c["ell"],
          "M": c["petal_count_M"], "background": c["background_size"],
          "layout": c["layout"], "scalar_mode": c["scalar_mode"],
          "list_size": c["list_size"], "planted": c["planted_count"],
          "challenger": c["classified_challenger"], "unclassified": c["unclassified"]}
         for c in exhaustive],
        key=lambda r: (r["n"], r["k"], r["sigma"], r["layout"], r["scalar_mode"]))

    summary = {
        "cell_count": len(cells),
        "exhaustive_cells": len(exhaustive),
        "structured_cells": len(structured),
        "cells_beating_0p9_planted": len(beating),
        "cells_beating_planted": sum(1 for c in cells if c["beats_planted"]),
        "total_unclassified_on_exhaustive_cells": total_unclassified_exhaustive,
        "third_class_alarm": total_unclassified_exhaustive > 0,
        "wall_seconds": round(time.time() - t0, 1),
    }
    interpretation = ("THIRD_CLASS_ALARM_ITERATE_E15_PROTOCOL"
                      if total_unclassified_exhaustive > 0
                      else "TWO_CLASSES_EXHAUST_QL5_TWO_COLUMN_CLOSES")

    result = {
        "schema": "e22-challenger-census-v1",
        "roadmap_task": "E22 / worst_word_challenger_pricing / QL.5",
        "field": f"F_{P}",
        "exhaustive_cap_binom": EXHAUSTIVE_CAP,
        "gate_passed": True,
        "gate_results": gate_results,
        "summary": summary,
        "interpretation": interpretation,
        "challenger_count_grid": challenger_grid,
        "cells": cells,
    }
    print("E22_RESULTS " + json.dumps({
        "schema": result["schema"],
        "gate_passed": True,
        "summary": summary,
        "interpretation": interpretation,
        "challenger_count_grid": challenger_grid,
    }), flush=True)
    return result


@app.local_entrypoint()
def main():
    result = run_census.remote()
    print(json.dumps(result["summary"] if "summary" in result else result, indent=2))
    print("interpretation:", result.get("interpretation"))

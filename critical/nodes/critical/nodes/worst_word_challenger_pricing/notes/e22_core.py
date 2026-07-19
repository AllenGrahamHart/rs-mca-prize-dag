#!/usr/bin/env python3
"""E22 challenger-class census — shared core machinery.

RECONSTRUCTION NOTE.  The E22 task brief stated the E15 (#197) adversarial
search code was LOST and only prose survived.  It was NOT lost: the original
verifier `experimental/scripts/verify_e15_worst_word_challenge.py` survives
byte-identical (md5 b3561a606ff30a581dff1895ea9de2e9) in ~34 rs-mca worktrees.
The functions below are copied VERBATIM from that verifier (the ground-truth
E15 construction) so the census extends the exact same machinery.  Only the
census driver (classification into E22's two-column form + the extended
parameter sweep) is new.

E15 toy cell recap (F_193 subgroup domain):
  - domain D = order-n multiplicative subgroup of F_193*.
  - core   = first k-1 domain points (under a layout permutation).
  - petals = the remaining points cut into blocks of size ell = sigma+1.
  - planted word: value = scalar_p * L_core(x) on petal p, 0 on core/background,
    where L_core is the degree-(k-1) locator of the core.
  - planted codewords: {scalar_p * L_core : p} -- M = petal_count of them, each
    agreeing with the word on core (k-1) + one petal (ell) = k+sigma = s points.
  - the LIST at crossing radius s: all deg-<k polynomials agreeing on >= s pts.
  - planted_count = M ; a "challenger" = a NON-planted codeword in that list.
E15 finding (#197): at sigma=1, for k in {2,4,8}, n=16, the planted word's list
  size EXCEEDS M -- structured non-planted challengers (mixed-petal / full-petal
  petal-structured codewords) appear at the crossing radius, falsifying the
  planted-only worst-word heuristic.
"""

from __future__ import annotations

import itertools
import math
import random
from collections import Counter
from typing import Any

P = 193


# --- exact E15 field / polynomial machinery (verbatim) --------------------

def inv_mod(x: int, p: int = P) -> int:
    return pow(x % p, -1, p)


def trim(poly: list[int], p: int = P) -> tuple[int, ...]:
    out = [x % p for x in poly]
    while out and out[-1] == 0:
        out.pop()
    return tuple(out)


def poly_mul(left: tuple[int, ...], right: tuple[int, ...], p: int = P) -> tuple[int, ...]:
    out = [0] * (len(left) + len(right) - 1)
    for i, ai in enumerate(left):
        for j, bj in enumerate(right):
            out[i + j] = (out[i + j] + ai * bj) % p
    return trim(out, p)


def poly_add(left: tuple[int, ...], right: tuple[int, ...], p: int = P) -> tuple[int, ...]:
    size = max(len(left), len(right))
    out = [0] * size
    for idx in range(size):
        out[idx] = (
            (left[idx] if idx < len(left) else 0)
            + (right[idx] if idx < len(right) else 0)
        ) % p
    return trim(out, p)


def poly_scale(poly: tuple[int, ...], scalar: int, p: int = P) -> tuple[int, ...]:
    return trim([scalar * coeff for coeff in poly], p)


def poly_eval(poly: tuple[int, ...], x: int, p: int = P) -> int:
    value = 0
    for coeff in reversed(poly):
        value = (value * x + coeff) % p
    return value


def interpolate(points: list[tuple[int, int]], p: int = P) -> tuple[int, ...]:
    poly: tuple[int, ...] = ()
    for i, (x_i, y_i) in enumerate(points):
        basis: tuple[int, ...] = (1,)
        denom = 1
        for j, (x_j, _) in enumerate(points):
            if i == j:
                continue
            basis = poly_mul(basis, ((-x_j) % p, 1), p)
            denom = (denom * (x_i - x_j)) % p
        term = poly_scale(basis, y_i * inv_mod(denom, p), p)
        poly = poly_add(poly, term, p)
    return poly


def polynomial_through(indices: list[int], domain: list[int], values: list[int], k: int) -> tuple[int, ...] | None:
    if len(indices) < k:
        raise ValueError("need at least k interpolation points")
    base = indices[:k]
    poly = interpolate([(domain[idx], values[idx]) for idx in base], P)
    if len(poly) > k:
        return None
    if all(poly_eval(poly, domain[idx], P) == values[idx] % P for idx in indices):
        return poly
    return None


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


def primitive_root(p: int = P) -> int:
    factors = factor_int(p - 1)
    for candidate in range(2, p):
        if all(pow(candidate, (p - 1) // factor, p) != 1 for factor in factors):
            return candidate
    raise ValueError("no primitive root")


def subgroup_domain(n: int, p: int = P) -> list[int]:
    if (p - 1) % n:
        raise ValueError(f"n={n} does not divide p-1={p - 1}")
    generator = pow(primitive_root(p), (p - 1) // n, p)
    domain = [pow(generator, idx, p) for idx in range(n)]
    if len(set(domain)) != n:
        raise AssertionError("wrong subgroup order")
    return domain


def locator(roots: list[int], p: int = P) -> tuple[int, ...]:
    poly: tuple[int, ...] = (1,)
    for root in roots:
        poly = poly_mul(poly, ((-root) % p, 1), p)
    return poly


def cyclic_order(n: int, step: int) -> list[int]:
    if not 0 <= step < n:
        raise ValueError(step)
    if step == 0:
        return list(range(n))
    if math.gcd(step, n) != 1:
        raise ValueError("step must be coprime to n")
    return [(step * idx) % n for idx in range(n)]


def shuffled_order(n: int, seed: int) -> list[int]:
    out = list(range(n))
    random.Random(seed).shuffle(out)
    return out


def layout_order(n: int, mode: str) -> list[int]:
    if mode.startswith("cyclic_step_"):
        return cyclic_order(n, int(mode.rsplit("_", 1)[1]))
    if mode.startswith("shuffle_"):
        return shuffled_order(n, int(mode.rsplit("_", 1)[1]))
    raise ValueError(mode)


def scalar_sequence(count: int, mode: str, p: int = P) -> list[int]:
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


def sunflower_word(n: int, k: int, sigma: int, layout: str, scalar_mode: str) -> dict[str, Any]:
    domain = subgroup_domain(n, P)
    ell = sigma + 1
    order = layout_order(n, layout)
    core = sorted(order[: k - 1])
    rest = order[k - 1 :]
    petal_count = len(rest) // ell
    petals = [sorted(rest[i * ell : (i + 1) * ell]) for i in range(petal_count)]
    background = sorted(rest[petal_count * ell :])
    core_locator = locator([domain[idx] for idx in core], P)
    scalars = scalar_sequence(petal_count, scalar_mode, P)
    values = [0] * n
    for scalar, petal in zip(scalars, petals):
        for idx in petal:
            values[idx] = scalar * poly_eval(core_locator, domain[idx], P) % P
    planted = {
        poly_scale(core_locator, scalar, P)
        for scalar in scalars
    }
    return {
        "n": n, "k": k, "sigma": sigma, "s": k + sigma, "ell": ell,
        "layout": layout, "scalar_mode": scalar_mode,
        "domain": domain, "core": core, "petals": petals,
        "background": background, "values": values,
        "core_locator": core_locator, "scalars": scalars,
        "planted_polynomials": planted,
    }


def agreement_set(poly: tuple[int, ...], word: dict[str, Any]) -> tuple[int, ...]:
    return tuple(
        idx for idx, x in enumerate(word["domain"])
        if poly_eval(poly, x, P) == word["values"][idx] % P
    )


def pattern(poly: tuple[int, ...], word: dict[str, Any]) -> dict[str, Any]:
    agreement = set(agreement_set(poly, word))
    return {
        "is_planted": poly in word["planted_polynomials"],
        "agreement": len(agreement),
        "core_agreement": len(agreement & set(word["core"])),
        "background_agreement": len(agreement & set(word["background"])),
        "petal_agreements": [len(agreement & set(petal)) for petal in word["petals"]],
    }


def classify_pattern(record: dict[str, Any], ell: int) -> str:
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


# --- E22 census additions -------------------------------------------------

# Two known classes (E22): planted sunflower family, E15 structured challenger.
# The E15 structured challenger class = petal-structured non-planted codewords
# (mixed_petal + full_petal).  Anything else non-planted is UNCLASSIFIED and
# raises the third-class alarm.
CHALLENGER_CLASSES = {"full_petal", "mixed_petal"}
UNCLASSIFIED_CLASSES = {"one_petal_nonplanted", "background_or_core_only"}


def exact_cell_census(n: int, k: int, sigma: int, layout: str, scalar_mode: str,
                      example_cap: int = 8) -> dict[str, Any]:
    """Exhaustive over all agreement subsets of size s; classify the full list."""
    word = sunflower_word(n, k, sigma, layout, scalar_mode)
    found: dict[tuple[int, ...], dict[str, Any]] = {}
    for indices in itertools.combinations(range(word["n"]), word["s"]):
        poly = polynomial_through(list(indices), word["domain"], word["values"], word["k"])
        if poly is None:
            continue
        rec = pattern(poly, word)
        if rec["agreement"] >= word["s"]:
            found[poly] = rec
    class_counts = Counter(classify_pattern(rec, word["ell"]) for rec in found.values())
    planted_count = len(word["planted_polynomials"])
    classified_planted = class_counts.get("planted", 0)
    classified_challenger = sum(class_counts.get(c, 0) for c in CHALLENGER_CLASSES)
    unclassified = sum(class_counts.get(c, 0) for c in UNCLASSIFIED_CLASSES)
    examples = []
    for poly, rec in found.items():
        if poly in word["planted_polynomials"]:
            continue
        examples.append({
            "polynomial_coefficients": list(poly),
            "class": classify_pattern(rec, word["ell"]),
            "petal_agreements": rec["petal_agreements"],
            "core_agreement": rec["core_agreement"],
            "background_agreement": rec["background_agreement"],
            "agreement": rec["agreement"],
        })
        if len(examples) >= example_cap:
            break
    return {
        "kind": "exact_all_agreement_sets",
        "n": n, "k": k, "sigma": sigma, "s": word["s"], "ell": word["ell"],
        "layout": layout, "scalar_mode": scalar_mode,
        "petal_count_M": len(word["petals"]),
        "background_size": len(word["background"]),
        "agreement_sets_checked": math.comb(word["n"], word["s"]),
        "list_size": len(found),
        "planted_count": planted_count,
        "nonplanted_count": len(found) - classified_planted,
        "classified_planted": classified_planted,
        "classified_challenger": classified_challenger,
        "unclassified": unclassified,
        "beats_planted": len(found) > planted_count,
        "beats_0p9_planted": len(found) > 0.9 * planted_count,
        "class_counts": dict(sorted(class_counts.items())),
        "nonplanted_examples": examples,
    }

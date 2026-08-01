#!/usr/bin/env python3
"""Exact structural checks for the Brief-2 C2'' proof-program dossier.

This script verifies only elementary identities, counterexamples to unsafe
inference patterns, and printed arithmetic used by the planning dossier.  It
does NOT prove C2'', any DLI node, or any repository theorem.

All load-bearing checks use Python integers/Fractions.  Decimal/float output is
used only for display of the repository's rounded empirical headline numbers.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
import math


FAILURES: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    tag = "PASS" if condition else "FAIL"
    print(f"[{tag}] {name}" + (f" :: {detail}" if detail else ""))
    if not condition:
        FAILURES.append(name)


# ---------------------------------------------------------------------------
# 1. Official schedule, universal-row fence, and reserve arithmetic
# ---------------------------------------------------------------------------

def check_schedule_and_scope() -> None:
    t = 2**33
    levels = [2**e for e in range(32, 0, -1)] + [1, 1]
    check("official schedule has 34 levels", len(levels) == 34)
    check("official schedule has 33 junctions", len(levels) - 1 == 33)
    check("official level dimensions sum to t=2^33", sum(levels) == t)
    check("official dimensions are (2^32,...,2,1,1)",
          levels[:4] == [2**32, 2**31, 2**30, 2**29]
          and levels[-4:] == [4, 2, 1, 1])

    # q = 1 + k*2^41 and q < 2^256.
    candidate_k = (2**256 - 2) // 2**41
    check("candidate progression count is 2^215-1",
          candidate_k == 2**215 - 1,
          f"count={candidate_k}")
    check("candidate progression is far beyond finite census scale",
          candidate_k.bit_length() == 215)

    check("21-bit joint reserve times 100-bit marginal baseline is 121 bits",
          2**21 * 2**100 == 2**121)
    allowance = 2 ** (21 / 33)
    check("per-junction display rounds to 1.554",
          round(allowance, 3) == 1.554,
          f"2^(21/33)={allowance:.12f}")

    # A deliberately generous illustrative additive allocation.
    k_bulk = 2**10
    k_acc = 2**20
    check("illustrative 10-bit bulk + 20-bit absolute accident caps fit 21 bits",
          k_bulk + k_acc < 2**21,
          f"{k_bulk + k_acc} < {2**21}")


# ---------------------------------------------------------------------------
# 2. Exact tilted-measure telescoping identity
# ---------------------------------------------------------------------------

def expectation(prob: list[Fraction], values: list[Fraction]) -> Fraction:
    return sum((p * v for p, v in zip(prob, values)), Fraction(0))


def check_tilted_telescoping() -> None:
    # A non-product finite space with four nonnegative factors.
    prob = [Fraction(1, 10), Fraction(2, 10), Fraction(3, 10), Fraction(4, 10)]
    rho = [
        [Fraction(1), Fraction(2), Fraction(1), Fraction(3)],
        [Fraction(2), Fraction(1), Fraction(4), Fraction(1)],
        [Fraction(1), Fraction(3), Fraction(2), Fraction(2)],
        [Fraction(4), Fraction(1), Fraction(1), Fraction(2)],
    ]
    mus = [expectation(prob, r) for r in rho]
    check("all marginal means are positive", all(m > 0 for m in mus))
    y = [[v / mu for v in r] for r, mu in zip(rho, mus)]

    z = [Fraction(1)]
    prefix = [Fraction(1)] * len(prob)
    for j in range(len(y)):
        prefix = [a * b for a, b in zip(prefix, y[j])]
        z.append(expectation(prob, prefix))

    increments = [z[j + 1] / z[j] for j in range(len(y))]
    ratio_from_telescope = math.prod(increments, start=Fraction(1))

    raw_product = [Fraction(1)] * len(prob)
    for r in rho:
        raw_product = [a * b for a, b in zip(raw_product, r)]
    x = expectation(prob, raw_product)
    a = math.prod(mus, start=Fraction(1))
    ratio_direct = x / a

    check("first normalized increment is exactly one", increments[0] == 1)
    check("tilted increments telescope exactly", ratio_from_telescope == ratio_direct,
          f"ratio={ratio_direct}")
    check("number of nontrivial increments is factors-1",
          len(increments[1:]) == len(rho) - 1)


# ---------------------------------------------------------------------------
# 3. Exact Bellman recursion on a finite state tree
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Edge:
    prob: Fraction
    y: Fraction
    child: str


def check_bellman_recursion() -> None:
    # Three factor levels, state-dependent transitions.
    tree: dict[tuple[int, str], list[Edge]] = {
        (0, "root"): [
            Edge(Fraction(1, 3), Fraction(3, 2), "a"),
            Edge(Fraction(2, 3), Fraction(3, 4), "b"),
        ],
        (1, "a"): [
            Edge(Fraction(1, 2), Fraction(2), "c"),
            Edge(Fraction(1, 2), Fraction(1, 2), "d"),
        ],
        (1, "b"): [
            Edge(Fraction(1, 4), Fraction(3), "c"),
            Edge(Fraction(3, 4), Fraction(1, 3), "d"),
        ],
        (2, "c"): [Edge(Fraction(1), Fraction(5, 4), "end")],
        (2, "d"): [Edge(Fraction(1), Fraction(4, 5), "end")],
    }

    memo: dict[tuple[int, str], Fraction] = {}

    def value(level: int, state: str) -> Fraction:
        if level == 3:
            return Fraction(1)
        key = (level, state)
        if key not in memo:
            memo[key] = sum(
                (e.prob * e.y * value(level + 1, e.child)
                 for e in tree[key]),
                Fraction(0),
            )
        return memo[key]

    bellman = value(0, "root")

    direct = Fraction(0)
    for e0 in tree[(0, "root")]:
        for e1 in tree[(1, e0.child)]:
            for e2 in tree[(2, e1.child)]:
                direct += e0.prob * e1.prob * e2.prob * e0.y * e1.y * e2.y

    check("Bellman recursion equals full path enumeration", bellman == direct,
          f"value={bellman}")


# ---------------------------------------------------------------------------
# 4. Exact first-owner partition
# ---------------------------------------------------------------------------

def check_first_owner_partition() -> None:
    # Eight paths with exact path masses and accident labels by junction.
    paths = [
        (Fraction(1, 10), [None, None, None]),
        (Fraction(2, 10), ["A", None, "B"]),
        (Fraction(1, 10), [None, "B", None]),
        (Fraction(1, 10), [None, None, "A"]),
        (Fraction(1, 10), ["B", "A", None]),
        (Fraction(1, 10), [None, "A", "B"]),
        (Fraction(1, 10), [None, None, None]),
        (Fraction(1, 10), ["A", "A", "A"]),
    ]
    total = sum((mass for mass, _ in paths), Fraction(0))
    bulk = Fraction(0)
    owned: dict[tuple[int, str], Fraction] = {}
    assigned = 0
    for mass, labels in paths:
        owner = next(((j, label) for j, label in enumerate(labels)
                      if label is not None), None)
        if owner is None:
            bulk += mass
        else:
            owned[owner] = owned.get(owner, Fraction(0)) + mass
        assigned += 1
    recomposed = bulk + sum(owned.values(), Fraction(0))
    check("first-owner partition is exhaustive", assigned == len(paths))
    check("first-owner partition is disjoint and additive", recomposed == total,
          f"bulk={bulk}, owned={owned}")


# ---------------------------------------------------------------------------
# 5. One-junction class-correlation formula and exact threshold comparison
# ---------------------------------------------------------------------------

def check_class_correlation_formula() -> None:
    # Six k=2 supports. E(G)=even completions, S(G)=odd valid skews.
    e_values = [1, 2, 3, 4, 5, 7]
    s_values = [0, 1, 1, 2, 3, 5]
    h, k = 4, 2
    cn = sum(e_values)
    cs = sum(e * s for e, s in zip(e_values, s_values))
    an = math.comb(h, k) * 2 ** (h - k)
    asum = 2 ** (h - k) * sum(s_values)

    ratio_counts = Fraction(cs, cn) / Fraction(asum, an)
    ratio_functions = (
        Fraction(sum(e * s for e, s in zip(e_values, s_values)), sum(e_values))
        / Fraction(sum(s_values), len(s_values))
    )
    check("class ratio equals correlation of E(G) and S(G)",
          ratio_counts == ratio_functions,
          f"ratio={ratio_counts}")

    exact_accident = cs * an > 2 * cn * asum
    check("theta=2 accident decision is exact cross multiplication",
          exact_accident == (ratio_counts > 2))


# ---------------------------------------------------------------------------
# 6. Float threshold path can misclassify an exact accident
# ---------------------------------------------------------------------------

def check_float_threshold_hazard() -> None:
    cn = 2**60
    an = 2**60
    asum = 2**60
    cs = 2**61 + 1
    exact = cs * an > 2 * cn * asum
    # Mirrors Python's / path in the current experimental decompose_row.
    float_ratio = (cs / cn) / (asum / an)
    float_decision = float_ratio > 2.0
    check("constructed class is exactly above theta=2", exact)
    check("binary64 path rounds the exact excess away", not float_decision,
          f"float_ratio={float_ratio!r}")


# ---------------------------------------------------------------------------
# 7. Threshold-defined accidents depend on class granularity
# ---------------------------------------------------------------------------

def check_granularity_hazard() -> None:
    # Two canonical subtypes.  A is an accident if resolved; the merged class is not.
    weights = [Fraction(1, 100), Fraction(99, 100)]
    ratios = [Fraction(3), Fraction(1)]
    merged = sum((w * r for w, r in zip(weights, ratios)), Fraction(0))
    check("resolved subtype A exceeds theta=2", ratios[0] > 2)
    check("merged class falls below theta=2", merged < 2,
          f"merged_ratio={merged}")
    check("accident status is not invariant under regrouping",
          (ratios[0] > 2) != (merged > 2))


# ---------------------------------------------------------------------------
# 8. Pairwise independence can coexist with a 22-bit 33-fold excess
# ---------------------------------------------------------------------------

def parity(value: int) -> int:
    return value.bit_count() & 1


def check_pairwise_vs_joint_hazard() -> None:
    d = 11
    # Include a basis, then 22 other distinct nonzero forms.
    forms = [1 << i for i in range(d)]
    candidate = 1
    while len(forms) < 33:
        if candidate not in forms:
            forms.append(candidate)
        candidate += 1
    assert len(forms) == 33 and len(set(forms)) == 33

    space = range(1 << d)
    zeros = [sum(1 for x in space if parity(x & f) == 0) for f in forms]
    pair_zero = []
    for i in range(len(forms)):
        for j in range(i + 1, len(forms)):
            pair_zero.append(sum(
                1 for x in space
                if parity(x & forms[i]) == 0 and parity(x & forms[j]) == 0
            ))
    all_zero = sum(
        1 for x in space if all(parity(x & f) == 0 for f in forms)
    )

    check("all 33 factors have mean one after 2*indicator normalization",
          all(z == 2**(d - 1) for z in zeros))
    check("every factor pair is exactly independent",
          all(z == 2**(d - 2) for z in pair_zero))
    check("forms span all 11 base bits, so common zero set has size one",
          all_zero == 1)
    joint_ratio = Fraction(2**33 * all_zero, 2**d)
    check("33-fold normalized product has 22-bit excess",
          joint_ratio == 2**22,
          f"joint_ratio={joint_ratio}")
    check("pairwise-perfect data can still violate the 21-bit target",
          joint_ratio > 2**21)


# ---------------------------------------------------------------------------
# 9. Unique ownership implies a sum, not a single maximum charge
# ---------------------------------------------------------------------------

def check_sum_not_max_hazard() -> None:
    charges = [Fraction(1, 1000)] * 33
    total = sum(charges, Fraction(0))
    maximum = max(charges)
    check("33 distinct first-owned accidents add", total == Fraction(33, 1000))
    check("counting only the maximum once underprices distinct owners",
          total == 33 * maximum and total > maximum)


# ---------------------------------------------------------------------------
# 10. Exact additive composition with absolute accident mass
# ---------------------------------------------------------------------------

def check_absolute_accident_composition() -> None:
    # A >= 1 is the marginal D3 floor.  If bulk <= Kb*A and accidents <= Ka,
    # then X <= (Kb+Ka)A because Ka <= Ka*A.
    a = Fraction(7, 3)
    kb = 2**10
    ka = 2**20
    x_bulk = kb * a
    x_acc = Fraction(ka)
    x = x_bulk + x_acc
    check("marginal baseline A is at least one in the toy composition", a >= 1)
    check("absolute accident cap converts using A>=1",
          x <= (kb + ka) * a)
    check("illustrative caps imply C2's 21-bit inequality",
          x < 2**21 * a)


# ---------------------------------------------------------------------------
# 11. Printed evidence arithmetic (display-only)
# ---------------------------------------------------------------------------

def check_printed_evidence_display() -> None:
    x = 1.066159
    accident_bits = 0.0009
    bits = 33 * math.log2(x) + accident_bits
    usage = bits / 21
    check("printed Round-2 proxy uses about 3.05 bits",
          3.04 < bits < 3.06,
          f"bits={bits:.6f}")
    check("printed reserve usage is about 14.5 percent",
          0.144 < usage < 0.146,
          f"usage={100*usage:.4f}%")
    # This is deliberately only a display check: original exact Fraction is in repo.


def main() -> None:
    print("Brief-2 C2'' proof-program structural replay")
    print("NOTE: planning checks only; no C2'' proof is claimed.\n")
    check_schedule_and_scope()
    check_tilted_telescoping()
    check_bellman_recursion()
    check_first_owner_partition()
    check_class_correlation_formula()
    check_float_threshold_hazard()
    check_granularity_hazard()
    check_pairwise_vs_joint_hazard()
    check_sum_not_max_hazard()
    check_absolute_accident_composition()
    check_printed_evidence_display()

    if FAILURES:
        print("\nFAILED:", ", ".join(FAILURES))
        raise SystemExit(1)
    print("\nBRIEF2_C2PP_PROGRAM_ARITHMETIC_PASS")


if __name__ == "__main__":
    main()

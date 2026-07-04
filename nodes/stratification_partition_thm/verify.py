#!/usr/bin/env python3
"""
verify.py  --  machine-check for stratification_partition_thm

Claim: the T0-T7 first-match stratification (source:
wp_detail/wp2_3_stratification_case_tree.md sec.2), terminating in its named
residual leaf L, is a PARTITION -- total and pairwise disjoint -- of the pair
space.

Method (see proof.md):
  * Build a COMPLETE finite toy model of the pair space at the resolution the
    eight case-predicates read it: one record per combinatorial feature they
    inspect.
  * Enumerate the FULL Cartesian product (no sampling), and for every point
    evaluate the nine guard conjunctions G_T0..G_T7, G_L independently, then
    assert EXACTLY ONE is true.  This is a direct, exhaustive check of both
    partition axioms:  >=1 true == totality (no fall-through);
                       <=1 true == disjointness (no double-claim).
    Reproduces the source sec.4(ii) acceptance criterion exhaustively.
  * Plant the source sec.4(i) constructor pairs; check each lands in its
    intended stratum (first-match).
  * Exhibit inhabited residual leaf L (honesty gate, source sec.4/5 F1,F2).
  * Re-run exactly-one under randomized re-definitions of the slot predicates
    (incl. the interpretive P5) to show the partition property is structural,
    independent of the P5 reading.

Single process, no threads, ~1500 points; well under 1GB / no background jobs.
Exit 0 and print PASS on success; raise AssertionError otherwise.
"""

import itertools
import random

# ----------------------------------------------------------------------------
# Toy feature space.  A "pair type" is the tuple of combinatorial features that
# the eight T0-T7 predicates inspect.  Ranges are chosen to be COMPLETE for the
# predicate algebra (every truth-combination the predicates can distinguish is
# realized), and to straddle every threshold (fold M>1; rank r vs r0=12).
# ----------------------------------------------------------------------------

R0 = 12  # low-rank threshold r0 for the synthetic families (source T4)

FEATURE_DOMAINS = {
    "contained":     (0, 1),          # T0: exists locator l, H(u)_l=H(v)_l=0
    "degenerate":    (0, 1),          # T1: v=0 / u=0 / v=lambda u
    "tangent":       (0, 1),          # T2: exists Z0,c agreement=A0>A
    "M":             (1, 2, 3),       # T3: fold x->x^M, match iff M>1
    "rank":          (2, 12, 13, 20), # T4: match iff rank<=R0 (12,13 straddle)
    "regime_closes": (0, 1),          # T5: regime ledger fully prices the pair
    "regular":       (0, 1),          # T5 sub-tag: t>=j+1 (regular) vs deficiency
    "cross":         (0, 1),          # T6: kernel locator of degree < j
    "splitgate":     (0, 1),          # T7: surviving eliminant root passes gate
}
FEATURE_ORDER = list(FEATURE_DOMAINS.keys())


def all_points():
    """Exhaustively enumerate the complete toy pair space."""
    domains = [FEATURE_DOMAINS[k] for k in FEATURE_ORDER]
    for combo in itertools.product(*domains):
        yield dict(zip(FEATURE_ORDER, combo))


# ----------------------------------------------------------------------------
# The eight match-predicates P0..P7, transcribed from wp2_3 sec.2 (see proof.md
# sec.1).  Each returns a bool from the feature record.
# ----------------------------------------------------------------------------

def P0(f):  # T0 containment gate
    return bool(f["contained"])

def P1(f):  # T1 degenerate pairs
    return bool(f["degenerate"])

def P2(f):  # T2 tangent overlap
    return bool(f["tangent"])

def P3(f):  # T3 quotient periodicity: fold x->x^M with M>1
    return f["M"] > 1

def P4(f):  # T4 direction rank: r <= r0 -> low-rank ladder
    return f["rank"] <= R0

def P5(f):  # T5 regime split: regime ledger closes the pair (see proof.md sec.1)
    return bool(f["regime_closes"])

def P6(f):  # T6 cross-bucket dedup: kernel locator of degree < j
    return bool(f["cross"])

def P7(f):  # T7 split-locator gate: surviving eliminant root passes the gate
    return bool(f["splitgate"])


PREDICATES = [P0, P1, P2, P3, P4, P5, P6, P7]
GATE_LABELS = ["T0", "T1", "T2", "T3", "T4", "T5", "T6", "T7"]
LEAF_LABEL = "L"


# ----------------------------------------------------------------------------
# Guard conjunctions (proof.md sec.3):  G_i = (not P0 ... not P_{i-1}) and P_i,
# and the catch-all  G_L = not P0 ... not P7.  We compute these INDEPENDENTLY
# of the first-match classifier so the exactly-one check is a real cross-check,
# not a tautology of the control flow.
# ----------------------------------------------------------------------------

def guards(f, preds=PREDICATES):
    """Return the list of nine guard truth values [G_T0..G_T7, G_L]."""
    vals = [p(f) for p in preds]
    g = []
    for i in range(len(preds)):
        gi = (not any(vals[:i])) and vals[i]
        g.append(gi)
    gL = not any(vals)  # catch-all residual leaf
    g.append(gL)
    return g


def classify(f, preds=PREDICATES):
    """First-match-wins classifier; returns a label in {T0..T7, L}."""
    for i, p in enumerate(preds):
        if p(f):
            return GATE_LABELS[i]
    return LEAF_LABEL


LABELS = GATE_LABELS + [LEAF_LABEL]


# ----------------------------------------------------------------------------
# (A) EXHAUSTIVE partition check over the complete toy model.
# ----------------------------------------------------------------------------

def check_exhaustive_partition():
    n = 0
    populations = {lab: 0 for lab in LABELS}
    for f in all_points():
        n += 1
        g = guards(f)
        fired = sum(1 for x in g if x)
        assert fired == 1, (
            f"PARTITION VIOLATION: {fired} guards fired (expected 1) at {f}; "
            f"guards={dict(zip(LABELS, g))}"
        )
        # cross-check: the single true guard must match the first-match label
        idx = g.index(True)
        assert LABELS[idx] == classify(f), (
            f"guard/classifier mismatch at {f}: guard says {LABELS[idx]}, "
            f"classifier says {classify(f)}"
        )
        populations[LABELS[idx]] += 1
    return n, populations


# ----------------------------------------------------------------------------
# (B) Planted constructors (source sec.4(i)) -> expected first-match stratum.
# ----------------------------------------------------------------------------

def base(**overrides):
    """A feature record with everything 'off'/generic, then overrides applied.
    Defaults chosen so that with NO overrides the pair misses all eight
    predicates -> lands in the residual leaf L (the all-miss point)."""
    f = {
        "contained": 0, "degenerate": 0, "tangent": 0, "M": 1,
        "rank": 20, "regime_closes": 0, "regular": 0, "cross": 0, "splitgate": 0,
    }
    f.update(overrides)
    return f


PLANTED = [
    # (description, feature record, expected stratum)
    ("contained pair",                    base(contained=1),                 "T0"),
    ("v = 0 (degenerate)",                base(degenerate=1),                "T1"),
    ("proportional v = lambda u",         base(degenerate=1),                "T1"),
    ("planted tangent A0 > A",            base(tangent=1),                   "T2"),
    ("folded pair M = 2",                 base(M=2),                         "T3"),
    ("low-rank synthetic r = 2",          base(rank=2),                      "T4"),
    ("full-rank regime-closing generic",  base(rank=20, regime_closes=1,
                                               regular=1),                   "T5"),
    ("cross-bucket residual (deg<j)",     base(rank=20, regime_closes=0,
                                               cross=1),                     "T6"),
    ("surviving split eliminant root",    base(rank=20, regime_closes=0,
                                               cross=0, splitgate=1),        "T7"),
    ("all-miss residual pair",            base(),                            "L"),
    # dedup / priority checks: earlier gate must win when several predicates hold
    ("contained AND tangent AND folded",  base(contained=1, tangent=1, M=2), "T0"),
    ("tangent AND folded (T2<T3)",        base(tangent=1, M=2),              "T2"),
    ("folded AND low-rank (T3<T4)",       base(M=2, rank=2),                 "T3"),
]


def check_planted():
    for desc, f, expected in PLANTED:
        got = classify(f)
        assert got == expected, (
            f"planted constructor '{desc}': expected {expected}, got {got} "
            f"(features {f})"
        )
        # and it must satisfy exactly-one as well
        assert sum(guards(f)) == 1, f"planted '{desc}' fails exactly-one"
    return len(PLANTED)


# ----------------------------------------------------------------------------
# (C) Honesty gate: the residual leaf L is genuinely inhabited (source sec.5
#     F1/F2, GAP-1).  Confirm >=1 point in the complete model lands in L.
# ----------------------------------------------------------------------------

def check_leaf_inhabited():
    leaf_pts = [f for f in all_points() if classify(f) == LEAF_LABEL]
    assert len(leaf_pts) > 0, (
        "residual leaf L is EMPTY in the toy model -- contradicts source "
        "sec.5 F1/F2 (GAP-1 mass lands in L by design)"
    )
    # every leaf point must have all eight predicates false
    for f in leaf_pts:
        assert not any(p(f) for p in PREDICATES), \
            f"leaf point {f} unexpectedly matches a gate"
    return len(leaf_pts)


# ----------------------------------------------------------------------------
# (D) Structural robustness: the partition property must be invariant to the
#     interpretive choice of the slot predicates (esp. P5).  Randomly redefine
#     ALL eight predicates as arbitrary subsets of the feature space and confirm
#     exactly-one still holds everywhere -- demonstrating the Lemma's generality
#     (proof.md sec.2): first-match + catch-all partitions for ANY predicates.
# ----------------------------------------------------------------------------

def check_structural_robustness(trials=200, seed=20260704):
    rng = random.Random(seed)
    points = list(all_points())
    for _ in range(trials):
        # each random predicate is an arbitrary boolean function of the record,
        # realized by a random per-point coin keyed by a fresh salt.
        salts = [rng.randrange(1 << 30) for _ in range(8)]

        def make_pred(salt):
            def pred(f, salt=salt):
                h = salt
                for k in FEATURE_ORDER:
                    h = (h * 1000003) ^ (hash((k, f[k])) & 0xFFFFFFFF)
                return (h & 1) == 1
            return pred

        rand_preds = [make_pred(s) for s in salts]
        for f in points:
            g = guards(f, preds=rand_preds)
            assert sum(g) == 1, (
                "randomized-predicate PARTITION VIOLATION -- the partition "
                "property is NOT structural (should be impossible)"
            )
    return trials * len(points)


# ----------------------------------------------------------------------------
# Driver.
# ----------------------------------------------------------------------------

def main():
    n, pops = check_exhaustive_partition()
    n_planted = check_planted()
    n_leaf = check_leaf_inhabited()
    n_rand = check_structural_robustness()

    print("stratification_partition_thm -- verify.py")
    print("-" * 60)
    print(f"(A) exhaustive partition check : {n} feature points, "
          f"exactly one cell each -> PASS")
    print(f"    cell populations           : "
          f"{ {k: pops[k] for k in LABELS} }")
    print(f"(B) planted constructors       : {n_planted} pairs land in "
          f"intended stratum -> PASS")
    print(f"(C) residual leaf L inhabited  : {n_leaf} points in L "
          f"(honesty gate, GAP-1 mass) -> PASS")
    print(f"(D) structural robustness      : {n_rand} "
          f"(randomized-predicate) checks, exactly-one holds -> PASS")
    print("-" * 60)
    # partition sanity: populations sum to the model size, no cell overlaps
    assert sum(pops.values()) == n
    print(f"PASS: T0-T7 + residual leaf is a partition of {n} pair types "
          f"(total + disjoint, exhaustively verified).")


if __name__ == "__main__":
    main()

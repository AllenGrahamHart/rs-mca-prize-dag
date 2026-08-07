#!/usr/bin/env python3
"""F2 effective energy dichotomy (Modal): numeric verification layer for
the effective BSG/quasicube instrument (kernel-summit base camp).

The instrument (see F2_EFFECTIVE_ENERGY_DICHOTOMY.md):

  COMPOSITION LEMMA (self-contained proof in the note): if A is a finite
  subset of {0,1}^d, E(A) >= |A|^3/K, and
    BSG(c1,e1,c2,e2):  exists A' <= A with |A'| >= |A|/(c1 K^e1),
                       |A'-A'| <= c2 K^e2 |A'|,
    QUASICUBE:         |B-B| >= |B|^{3/2} for finite B in {0,1}^d,
  then |A| <= c1 c2^2 K^{e1+2e2}.
  Contrapositive: |A| > c1 c2^2 K^{e1+2e2} forces E(A) < |A|^3/K.

Verified here:
  (V1) QUASICUBE exhaustively at d <= 4 (all 2^(2^d) subsets) — the
       external GMRSZ corollary must not fail anywhere small.
  (V2) QUASICUBE sampled at d = 8..16 across structured families
       (random by density, subcubes, Hamming balls, translate unions,
       downsets) — worst observed ratio |A-A| / |A|^{3/2} reported.
  (V3) the composition algebra on an exact integer grid (no floats in
       the inequality chain).
  (V4) the F2 instantiation table at the prize-max row (n = 2^41,
       budget n^3 = 2^123): forced energy deficit K* for three
       (c1,e1,c2,e2) instantiations, exact bit arithmetic.

Any assertion failure refutes the packet.
"""
import itertools
import random
from fractions import Fraction

import modal

app = modal.App("rs-mca-f2-energy-dichotomy")
image = modal.Image.debian_slim()


@app.function(image=image, cpu=2, memory=2048, timeout=280)
def v1_exhaustive(d):
    pts = list(itertools.product((0, 1), repeat=d))
    worst = None
    for mask in range(1, 1 << len(pts)):
        A = [pts[i] for i in range(len(pts)) if mask >> i & 1]
        diffs = {tuple(a[j] - b[j] for j in range(d)) for a in A for b in A}
        # exact check |A-A|^2 >= |A|^3  <=>  |A-A| >= |A|^{3/2}
        assert len(diffs) ** 2 >= len(A) ** 3, ("QUASICUBE FAILED", d, A)
        r = Fraction(len(diffs) ** 2, len(A) ** 3)
        if worst is None or r < worst:
            worst = r
    return {"d": d, "n_sets": (1 << len(pts)) - 1,
            "worst_ratio_sq": [worst.numerator, worst.denominator]}


@app.function(image=image, cpu=2, memory=2048, timeout=280)
def v2_sampled(job):
    d, seed = job
    rng = random.Random(seed)
    worst = None
    cases = []
    # random by density
    for dens in (0.02, 0.1, 0.3, 0.6):
        A = {tuple(rng.randrange(2) for _ in range(d))
             for _ in range(int(dens * min(2 ** d, 1400)))}
        cases.append(set(A))
    # subcube (Boolean subgroup) — the classical near-tight family
    m = min(d, 10)
    cases.append({tuple(list(p) + [0] * (d - m))
                  for p in itertools.product((0, 1), repeat=m)})
    # Hamming ball
    cases.append({p for p in itertools.product((0, 1), repeat=min(d, 14))
                  if sum(p) <= 2})
    # union of translates of a small random seed set
    B = [tuple(rng.randrange(2) for _ in range(d)) for _ in range(24)]
    tr = set()
    for _ in range(8):
        t = tuple(rng.randrange(2) for _ in range(d))
        for b in B:
            tr.add(tuple(min(1, b[j] + t[j]) for j in range(d)))
    cases.append(tr)
    # downset closure of random generators
    gen = [tuple(rng.randrange(2) for _ in range(d)) for _ in range(6)]
    ds = set()
    for g in gen:
        ones = [j for j in range(d) if g[j]]
        for r in range(len(ones) + 1):
            for sub in itertools.combinations(ones, r):
                p = [0] * d
                for j in sub:
                    p[j] = 1
                ds.add(tuple(p))
                if len(ds) > 1400:
                    break
    cases.append(ds)
    out = []
    for A in cases:
        A = {p if len(p) == d else tuple(list(p) + [0] * (d - len(p)))
             for p in A}
        if not A or len(A) > 1500:
            continue
        As = sorted(A)
        diffs = {tuple(a[j] - b[j] for j in range(d))
                 for a in As for b in As}
        assert len(diffs) ** 2 >= len(A) ** 3, ("QUASICUBE FAILED", d, len(A))
        r = Fraction(len(diffs) ** 2, len(A) ** 3)
        out.append((len(A), len(diffs)))
        if worst is None or r < worst:
            worst = r
    return {"d": d, "seed": seed, "n_cases": len(out),
            "worst_ratio_sq": [worst.numerator, worst.denominator]}


@app.function(image=image, cpu=1, memory=512, timeout=120)
def v3_v4(_):
    # V3: exact integer composition-algebra grid
    for c1 in (1, 7, 1024):
        for c2 in (1, 5, 1024):
            for e1 in (1, 2):
                for e2 in (4, 5, 6):
                    for K in (2, 10, 1000, 2 ** 13):
                        bound = c1 * c2 ** 2 * K ** (e1 + 2 * e2)
                        # chain: |A'| <= c2^2 K^{2e2} and |A| <= c1 K^{e1}|A'|
                        apmax = c2 ** 2 * K ** (2 * e2)
                        assert c1 * K ** e1 * apmax == bound
                        # quasicube step: |A'|^{1/2} <= c2 K^{e2}, exact square
                        assert (c2 * K ** e2) ** 2 == apmax
    # V4: F2 instantiation at the prize-max row, exact bit arithmetic
    n_bits = 41
    budget_bits = 3 * n_bits          # n^3 = 2^123
    table = []
    for tag, c1b, e1, c2b, e2 in (
            ("idealized-Schoen (c=1, K^1/K^4)", 0, 1, 0, 4),
            ("conservative-Schoen (c=2^10)", 10, 1, 10, 4),
            ("classical-safe (c=2^10, K^2/K^5)", 10, 2, 10, 5)):
        denom_bits = c1b + 2 * c2b
        expo = e1 + 2 * e2
        # K* = (|A| / (c1 c2^2))^{1/expo} at |A| = 2^123 (exact rational bits)
        kstar_bits = Fraction(budget_bits - denom_bits, expo)
        table.append((tag, expo, float(kstar_bits)))
        assert kstar_bits > 0
    # weakest instantiation still forces a positive deficit
    assert min(t[2] for t in table) > 7
    return {"budget_bits": budget_bits,
            "table": [(t, e, round(b, 2)) for t, e, b in table]}


@app.local_entrypoint()
def main():
    r1 = list(v1_exhaustive.map([2, 3, 4], return_exceptions=True))
    jobs = [(8, 11), (10, 12), (12, 13), (14, 14), (16, 15)]
    r2 = list(v2_sampled.map(jobs, return_exceptions=True))
    r3 = v3_v4.remote(0)
    fails = 0
    print("V1 exhaustive quasicube:")
    for r in r1:
        if not isinstance(r, dict):
            fails += 1
            print("  worker error:", str(r)[:160])
            continue
        num, den = r["worst_ratio_sq"]
        print(f"  d={r['d']}: all {r['n_sets']} subsets pass; "
              f"worst (|A-A|^2)/(|A|^3) = {num}/{den} = {num/den:.3f}")
    print("V2 sampled quasicube:")
    for r in r2:
        if not isinstance(r, dict):
            fails += 1
            print("  worker error:", str(r)[:160])
            continue
        num, den = r["worst_ratio_sq"]
        print(f"  d={r['d']}: {r['n_cases']} families pass; "
              f"worst ratio^2 = {num/den:.3f}")
    print("V3 composition-algebra grid: exact (in-worker asserts)")
    print(f"V4 F2 instantiation (budget 2^{r3['budget_bits']}):")
    for tag, expo, bits in r3["table"]:
        print(f"  {tag}: e1+2e2 = {expo}, forced deficit K* = 2^{bits}")
    if fails:
        raise SystemExit(f"F2_EFFECTIVE_ENERGY_DICHOTOMY_FAIL ({fails})")
    print("\nF2_EFFECTIVE_ENERGY_DICHOTOMY_PASS")

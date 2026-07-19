#!/usr/bin/env python3
"""cg_petal_census: FIRST falsification attempt on petal_small_scale_staircase_census.

TARGET STATEMENT (dag.json, minted 2026-07-12): at official rows, per received
word U, the realized canonical class count of top-band full-petal contributors
with intrinsic scale 2 <= c(S) <= t fits <= 719 x planted column per consumed
profile. FALSIFIER: the banked engineered family exceeding the budgeted column
at scaled official-like rows, sustained.

OPERATIONAL DEFINITIONS (declared; all anchored to the banked 2026-07-10 g2
falsification machinery at critical/nodes/petal_growth/notes/g2_falsification_20260710/):

- Row: (n = 2^s, k, sigma = 1); domain D = the order-n subgroup of F_p^*,
  cyclically ordered dom[j] = g0^j. Primary rows use the banked machinery's
  shapes (8,3), (16,6), (32,12); secondary rate-1/2 rows (8,4), (16,8), (32,16).
- Received word U (E22/G4-dictionary sunflower word): core Z (|Z| = k-1),
  U = 0 on Z and on background; t petals T_i of size ell = sigma+1 = 2,
  U = c_i * L_Z(x) on T_i, scalars c_i in F_p^*. t = (n-(k-1))//2 is the
  chart-local petal count (catch #58 pin).
- Layouts: fiber_pairs (engineered fiber-aligned: petals are antipodal
  2-fibers {j, j+n/2}; witness-1 convention), quarter_pairs ({j, j+n/4}
  pairs), shuffled(seed) (witness-2 convention).
- Contributor: codeword f, deg < k, with agreement set
  S(f) = {j : f(dom[j]) = U[j]} of size >= k + sigma  (ImgFib_U(k+sigma)).
- Intrinsic scale c(S): the order of the translation stabilizer of S in
  Z_n = the largest dyadic M with S + n/M = S. c = 1 <=> aperiodic.
  By the stabilizer partition theorem (petal_g2_support_forcing, PROVED),
  c >= 2 => S is a union of full c-fibers with empty tail.
- Small-scale: 2 <= c(S) <= t.
- Full-petal: S∩T_i in {∅, T_i} for every petal (petal-saturated).
  Counts are reported BOTH with and without this filter (the banked witness-2
  class is small-scale but NOT petal-saturated, so the filter is load-bearing
  and both readings are shown).
- Band readings reported per contributor (P1 pin is unresolved, so all three
  nested readings are tabulated): EDGE |S| = k+sigma; OWN-SCALE
  |S| <= k+sigma+c(S)-1 (the g2-run fixed-M band at the contributor's own
  scale); ALL |S| >= k+sigma (widest; the attack-generous reading).
- Canonical class: the canonical support datum = S itself. (For periodic S
  the datum (scale c, selected fibers, empty tail) is equivalent to S by
  e22_fixed_scale_staircase_injectivity; realized class count per U = number
  of distinct agreement sets S realized.)
- Consumed profile: the cell (M, A) = (c(S), |S|).
- Planted column per profile: Q_M(A) = C(n/M - 1, A/M)
  (petal_g3_profile_conversion_identity's Q_M; the planted binomial column of
  v13_capf_planted_lower_count is the special cell A/M = k/M).
- Budget lines per profile (both scaled readings reported):
  B719 = 719 * Q_M(A)          (constant-719 reading)
  Bscaled = allow(n) * Q_M(A)  (allowance analog at the row's scale,
                                allow(n) = floor(n^6 / C(n+6,6)))
- FALSIFIER CHECK: realized class count > budget at a cell, sustained across
  scaled rows n = 8/16/32.

COMPLETENESS of the enumeration (proved, not sampled): any contributor with
c(S) >= 2 has S invariant under +n/2, hence S is a union of antipodal
2-fibers with |S| >= k+sigma, so S contains at least m0 = ceil((k+sigma)/2)
full 2-fibers; interpolating U through k points of any m0-subset of S's
fibers recovers f (deg < k through k points is unique). Enumerating ALL
m0-subsets of the n/2 fibers therefore finds EVERY periodic contributor.
"""
from __future__ import annotations

import itertools
import json
import sys
from math import comb

SCRATCH = ("/tmp/claude-1000/-home-u2470931-smooth-read-solomin/"
           "d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad")


# ---------------------------------------------------------------- field utils
def is_prime(m: int) -> bool:
    if m < 2:
        return False
    if m % 2 == 0:
        return m == 2
    d = 3
    while d * d <= m:
        if m % d == 0:
            return False
        d += 2
    return True


def order_n_domain(p: int, n: int) -> list[int]:
    assert (p - 1) % n == 0
    # find a generator of the order-n subgroup (element of exact order n)
    a = 2
    while True:
        g0 = pow(a, (p - 1) // n, p)
        if pow(g0, n // 2, p) != 1:
            break
        a += 1
    dom = [pow(g0, j, p) for j in range(n)]
    assert len(set(dom)) == n
    return dom


def locator_poly(roots: list[int], p: int) -> list[int]:
    loc = [1]
    for r in roots:
        new = [0] * (len(loc) + 1)
        for i, c in enumerate(loc):
            new[i] = (new[i] - r * c) % p
            new[i + 1] = (new[i + 1] + c) % p
        loc = new
    return loc


def ev(poly, x: int, p: int) -> int:
    v = 0
    for c in reversed(poly):
        v = (v * x + c) % p
    return v


def interpolate(xs: list[int], ys: list[int], k: int, p: int) -> tuple[int, ...]:
    """Lagrange through the k points (xs, ys); returns deg<k coeff tuple."""
    poly = [0] * k
    for i in range(k):
        num = [1]
        den = 1
        xi = xs[i]
        for j in range(k):
            if j == i:
                continue
            r = xs[j]
            new = [0] * (len(num) + 1)
            for d2, c in enumerate(num):
                new[d2] = (new[d2] - r * c) % p
                new[d2 + 1] = (new[d2 + 1] + c) % p
            num = new
            den = den * (xi - xs[j]) % p
        coef = ys[i] * pow(den, -1, p) % p
        for d2, c in enumerate(num):
            poly[d2] = (poly[d2] + coef * c) % p
    return tuple(poly)


# ---------------------------------------------------------------- word builds
def build_layout(n: int, k: int, layout: str, seed: int = 0):
    """Return (core_exps, petals, background) in exponent space."""
    half, quarter = n // 2, n // 4
    z = k - 1
    if layout == "fiber_pairs":
        order = []
        for j in range(half):
            order.extend([j, j + half])
    elif layout == "fiber_aligned":
        # TRUE fiber alignment at every row shape: core = floor((k-1)/2) full
        # antipodal fibers (+ one extra point if k-1 odd); petals = the
        # remaining FULL fibers; background = the leftover singleton(s).
        nf = (k - 1) // 2
        core = []
        for j in range(nf):
            core.extend([j, j + half])
        extra = []
        if (k - 1) % 2:
            core.append(nf)          # half of fiber nf
            extra = [nf + half]      # its partner goes to background
        petal_fibers = [j for j in range(nf + (1 if (k - 1) % 2 else 0), half)]
        petals = [sorted([j, j + half]) for j in petal_fibers]
        return sorted(core), petals, sorted(extra)
    elif layout == "quarter_pairs":
        order = []
        for j in range(quarter):
            order.extend([j, j + quarter])
        for j in range(quarter):
            order.extend([j + half, j + half + quarter])
    elif layout.startswith("shuffled"):
        import random
        rng = random.Random(seed)
        order = list(range(n))
        rng.shuffle(order)
    else:
        raise ValueError(layout)
    core = sorted(order[:z])
    rest = order[z:]
    t = len(rest) // 2
    petals = [sorted(rest[2 * i: 2 * i + 2]) for i in range(t)]
    background = sorted(rest[2 * t:])
    return core, petals, background


def build_word(n, k, p, dom, layout, scalars_mode, seed=0):
    core, petals, background = build_layout(n, k, layout, seed)
    t = len(petals)
    if scalars_mode == "geom5":
        scal, v = [], 1
        for _ in range(t):
            scal.append(v)
            v = v * 5 % p
    elif scalars_mode == "geom3":
        scal, v = [], 1
        for _ in range(t):
            scal.append(v)
            v = v * 3 % p
    elif scalars_mode == "consec":
        scal = [(i + 1) % p for i in range(t)]
    elif scalars_mode.startswith("rand"):
        import random
        rng = random.Random(1000 + seed)
        scal = [rng.randrange(1, p) for _ in range(t)]
    else:
        raise ValueError(scalars_mode)
    loc = locator_poly([dom[j] for j in core], p)
    values = [0] * n
    for c_i, petal in zip(scal, petals):
        for j in petal:
            values[j] = c_i * ev(loc, dom[j], p) % p
    return values, core, petals, background, scal


# ------------------------------------------------------------ periodic census
def stab_order(S: frozenset[int], n: int) -> int:
    c = 1
    M = 2
    while M <= n:
        s = n // M
        if all(((x + s) % n) in S for x in S):
            c = M
        else:
            break
        M *= 2
    return c


def periodic_contributors(n, k, sigma, p, dom, values):
    """All codewords deg<k agreeing with U on >= k+sigma points whose
    agreement set is periodic (c(S) >= 2). Returns dict poly -> S."""
    half = n // 2
    m0 = -(-(k + sigma) // 2)  # ceil
    found: dict[tuple[int, ...], frozenset[int]] = {}
    # cache interpolants by their defining first-k-point tuple ONLY (a poly
    # seen from a failing subset must still be re-verified on other subsets:
    # dedup on the poly alone is a completeness bug, caught by control C2)
    interp_cache: dict[tuple[int, ...], tuple[int, ...]] = {}
    for fibsub in itertools.combinations(range(half), m0):
        pts = []
        for j in fibsub:
            pts.append(j)
            pts.append(j + half)
        xs = [dom[j] for j in pts]
        ys = [values[j] for j in pts]
        key = tuple(pts[:k])
        poly = interp_cache.get(key)
        if poly is None:
            poly = interpolate(xs[:k], ys[:k], k, p)
            interp_cache[key] = poly
        if poly in found:
            continue
        if any(ev(poly, x, p) != y for x, y in zip(xs[k:], ys[k:])):
            continue
        S = frozenset(j for j in range(n) if ev(poly, dom[j], p) == values[j])
        if len(S) >= k + sigma and stab_order(S, n) >= 2:
            found[poly] = S
    return found


def brute_contributors(n, k, sigma, p, dom, values):
    """Independent cross-check: ALL contributors by (k+sigma)-subset
    interpolation (complete for every contributor, any scale)."""
    s = k + sigma
    found: dict[tuple[int, ...], frozenset[int]] = {}
    for idxs in itertools.combinations(range(n), s):
        xs = [dom[j] for j in idxs]
        ys = [values[j] for j in idxs]
        poly = interpolate(xs[:k], ys[:k], k, p)
        if poly in found:
            continue
        if any(ev(poly, x, p) != y for x, y in zip(xs[k:], ys[k:])):
            continue
        S = frozenset(j for j in range(n) if ev(poly, dom[j], p) == values[j])
        if len(S) >= s:
            found[poly] = S
    return found


# ------------------------------------------------------------------ reporting
def allow_scaled(n: int) -> int:
    return n**6 // comb(n + 6, 6)


def classify_cell(n, k, sigma, petals, contributors):
    """Group periodic contributors into canonical classes and profile cells."""
    t = len(petals)
    petal_sets = [frozenset(P) for P in petals]
    classes: dict[frozenset, dict] = {}
    for poly, S in contributors.items():
        c = stab_order(S, n)
        if not (2 <= c <= t):
            continue
        info = classes.setdefault(S, {"polys": [], "c": c, "A": len(S)})
        info["polys"].append(poly)
        info["full_petal"] = all(
            (S & P) in (frozenset(), P) for P in petal_sets)
        info["band_edge"] = len(S) == k + sigma
        info["band_own"] = len(S) <= k + sigma + c - 1
    return classes


def profile_table(n, k, classes, fp_filter, band):
    out: dict[tuple[int, int], dict] = {}
    for S, info in classes.items():
        if fp_filter and not info["full_petal"]:
            continue
        if band == "edge" and not info["band_edge"]:
            continue
        if band == "own" and not info["band_own"]:
            continue
        key = (info["c"], info["A"])
        cell = out.setdefault(key, {"classes": 0, "codewords": 0})
        cell["classes"] += 1
        cell["codewords"] += len(info["polys"])
    for (M, A), cell in out.items():
        h = A // M
        Q = comb(n // M - 1, h) if h <= n // M - 1 else 0
        cell["Q"] = Q
        cell["B719"] = 719 * Q
        cell["Bscaled"] = allow_scaled(n) * Q
        cell["excess719"] = cell["classes"] > cell["B719"]
        cell["ratio"] = (cell["classes"] / Q) if Q else float("inf")
    return out


def main():
    rows = [
        # (n, k, primes)   sigma = 1 throughout
        (8, 3, [17, 41, 73, 89, 97, 113]),
        (8, 4, [17, 73, 89, 97]),
        (16, 6, [97, 113, 257, 337, 353, 449]),
        (16, 8, [97, 257, 337]),
        (32, 12, [97, 193, 449, 577, 1153, 1249]),
        (32, 16, [97, 1153]),
    ]
    full_grid_primes = {8: set([17, 41, 73, 89, 97, 113]),
                        16: set([97, 113, 257, 337, 353, 449]),
                        32: set([97, 1153, 1249])}
    sigma = 1
    results = []
    for n, k, primes in rows:
        for p in primes:
            assert is_prime(p) and (p - 1) % n == 0, (n, p)
            dom = order_n_domain(p, n)
            if p in full_grid_primes[n] and k in (3, 6, 12):
                layouts = [("fiber_pairs", 0), ("fiber_aligned", 0),
                           ("quarter_pairs", 0),
                           ("shuffled", 1), ("shuffled", 2)]
                smodes = ["geom5", "geom3", "consec", "rand"]
            else:
                layouts = [("fiber_pairs", 0), ("fiber_aligned", 0),
                           ("shuffled", 1)]
                smodes = ["geom5", "consec"]
            for layout, seed in layouts:
                for smode in smodes:
                    values, core, petals, bg, scal = build_word(
                        n, k, p, dom, layout, smode, seed)
                    contr = periodic_contributors(n, k, sigma, p, dom, values)
                    classes = classify_cell(n, k, sigma, petals, contr)
                    cellrec = {
                        "n": n, "k": k, "p": p, "layout": layout,
                        "seed": seed, "scalars": smode, "t": len(petals),
                        "n_periodic_contributors": len(contr),
                        "n_smallscale_classes": len(classes),
                    }
                    for fp in (True, False):
                        for band in ("edge", "own", "all"):
                            tab = profile_table(n, k, classes, fp, band)
                            tag = f"fp{int(fp)}_{band}"
                            cellrec[tag] = {
                                f"{M},{A}": v for (M, A), v in
                                sorted(tab.items())}
                    results.append(cellrec)
    with open(f"{SCRATCH}/cg_petal_census_results.json", "w") as f:
        json.dump(results, f, indent=1, sort_keys=True)
    # compact summary
    n_excess = 0
    for r in results:
        for tag in ("fp1_all", "fp0_all"):
            for cell, v in r[tag].items():
                if v["excess719"]:
                    n_excess += 1
                    print("EXCESS719:", r["n"], r["k"], r["p"], r["layout"],
                          r["scalars"], tag, cell, v)
    print(f"cells run: {len(results)}; profile-cell budget excesses (719 line): {n_excess}")
    print("banked to cg_petal_census_results.json")


if __name__ == "__main__":
    main()

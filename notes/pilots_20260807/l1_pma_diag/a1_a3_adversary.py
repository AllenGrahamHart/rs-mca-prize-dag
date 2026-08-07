#!/usr/bin/env python3
"""A1 replication gate + A2 linearization + A3/A4/A5 adversarial word search.

Pre-registered in PREREG.md (section R2) BEFORE running.

A1: independently re-derive the N10 retained counts (43/33 at n=16, 2879/2857
    at n=32). Nothing downstream is reported unless this passes.
A2: for a candidate support S the retention condition is LINEAR in the petal
    scalar vector c = (c_1..c_t).  Derivation (hand, then machine-checked
    against A1): on the mu_n domain Z_dom = X^n - 1 = Z_S * Lam_E, so for
    x in S, Z_S'(x) = n x^{n-1} / Lam_E(x), and the (k+1)-point dual
    condition sum_{x in T} U(x)/Z_T'(x) = 0 becomes
        sum_{x in T} U(x) * x * Lam_{E'}(x) = 0.
    With U = 0 on core+background and U = c_i L_C on petal T_i this is
        sum_i c_i * gamma_i = 0,
        gamma_i = sum_{x in T_i \\ O} x L_C(x)^2 Lam_O(x) (x-x_bg)^{1-b'}
                                      / L_{K'}(x).
A3: exhaustive max over the whole legal word family at n=16.
A5: randomized + structured max at n=32.
"""
from __future__ import annotations

import itertools
import sys
from math import comb

import numpy as np

BANKED = {(16, 97, "consec"): 43, (16, 97, "geom5"): 33,
          (32, 97, "consec"): 2879, (32, 97, "geom5"): 2857}


def domain(p, n):
    """Mirror of domain() in the N10 generator (lines 58-68)."""
    for g in range(2, p):
        z = pow(g, (p - 1) // n, p)
        if pow(z, n, p) == 1 and pow(z, n // 2, p) != 1:
            xs = [1] * n
            for j in range(1, n):
                xs[j] = xs[j - 1] * z % p
            return xs
    raise RuntimeError("no domain generator")


def layout(n):
    """Mirror of layout() (lines 123-138)."""
    k, half = n // 2, n // 2
    nf = (k - 1) // 2
    core = []
    for j in range(nf):
        core += [j, j + half]
    core.append(nf)
    background = nf + half
    petals = [(j, j + half) for j in range(nf + 1, half)]
    return core, background, petals


def chart_scalars(n, p, mode, xs, petals):
    """The two banked scalar schedules (lines 140-163)."""
    out, geometric = [], 1
    for i in range(len(petals)):
        out.append((i + 1) % p if mode == "consec" else geometric)
        geometric = geometric * 5 % p
    return out


def word_from_scalars(n, p, xs, core, petals, scalars):
    values = [0] * n
    for i, (a, b) in enumerate(petals):
        for pt in (a, b):
            v = scalars[i]
            for r in core:
                v = v * ((xs[pt] - xs[r]) % p) % p
            values[pt] = v
    return values


def candidates(n):
    """Mirror of the census loop (lines 256-282); yields (K, use_bg, O, S)."""
    k = n // 2
    core, bg, petals = layout(n)
    petal_points = [pt for pr in petals for pt in pr]
    threshold = 2 * (len(petals) - 2)
    for cc in range(0, 4):
        if len(core) - cc < threshold:
            continue
        for K in itertools.combinations(core, cc):
            for use_bg in (0, 1):
                for om in (1, 2, 3):
                    if k + cc + use_bg - om < k + 1:
                        continue
                    for O in itertools.combinations(petal_points, om):
                        # mixed_omission: some petal hit exactly once
                        if not any(sum(pt in O for pt in pr) == 1
                                   for pr in petals):
                            continue
                        sup = [False] * n
                        for pt in petal_points:
                            sup[pt] = True
                        for pt in O:
                            sup[pt] = False
                        for pt in K:
                            sup[pt] = True
                        if use_bg:
                            sup[bg] = True
                        yield K, use_bg, O, [i for i in range(n) if sup[i]]


def gamma_matrix(n, p):
    """A2: the (num_candidates x t) matrix of linear forms over F_p."""
    k = n // 2
    xs = domain(p, n)
    core, bg, petals = layout(n)
    petal_index = {}
    for i, pr in enumerate(petals):
        for pt in pr:
            petal_index[pt] = i
    LC = {}
    for pt in list(petal_index) + [bg]:
        v = 1
        for r in core:
            v = v * ((xs[pt] - xs[r]) % p) % p
        LC[pt] = v
    alpha = {pt: xs[pt] * LC[pt] % p * LC[pt] % p for pt in petal_index}

    rows, meta = [], []
    for K, use_bg, O, S in candidates(n):
        cc, om = len(K), len(O)
        m = cc + use_bg - om            # support size = k + m
        # drop m-1 points of S from the core/background part -> a (k+1)-subset
        droppable = list(K) + ([bg] if use_bg else [])
        R = set(droppable[: m - 1])
        Kp = [x for x in K if x not in R]
        bp = use_bg - (1 if bg in R else 0)
        g = [0] * len(petals)
        for pt, pi in petal_index.items():
            if pt in O:
                continue
            v = alpha[pt]
            for y in O:
                v = v * ((xs[pt] - xs[y]) % p) % p
            if bp == 0:
                v = v * ((xs[pt] - xs[bg]) % p) % p
            den = 1
            for y in Kp:
                den = den * ((xs[pt] - xs[y]) % p) % p
            v = v * pow(den, p - 2, p) % p
            g[pi] = (g[pi] + v) % p
        rows.append(g)
        meta.append((K, use_bg, O, tuple(S), m))
    return np.array(rows, dtype=np.int64), meta, xs, core, bg, petals


def exact_retained(n, p, xs, values, meta, hits):
    """Full census semantics on the filtered survivors: interpolate from the
    first k points of S, require the complete agreement set to equal S."""
    k = n // 2
    kept, hist = 0, {}
    for idx in hits:
        S = meta[idx][3]
        pts = list(S[:k])
        # Lagrange evaluation at every domain point
        agree = []
        for target in range(n):
            acc = 0
            for j, pj in enumerate(pts):
                num, den = 1, 1
                for l, pl in enumerate(pts):
                    if l == j:
                        continue
                    num = num * ((xs[target] - xs[pl]) % p) % p
                    den = den * ((xs[pj] - xs[pl]) % p) % p
                acc = (acc + values[pj] * num % p * pow(den, p - 2, p)) % p
            if acc == values[target]:
                agree.append(target)
        if tuple(agree) == S:
            kept += 1
            hist[len(agree)] = hist.get(len(agree), 0) + 1
    return kept, hist


def count_for_scalars(G, c, p):
    return int(np.count_nonzero((G @ np.array(c, dtype=np.int64)) % p == 0))


def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else "16"
    print("=" * 78)
    print("A1 REPLICATION GATE (independent method: dual filter + exact check)")
    print("=" * 78)
    G_by_n = {}
    for n, p in (((16, 97),) if stage == "16" else ((32, 97),)):
        G, meta, xs, core, bg, petals = gamma_matrix(n, p)
        G_by_n[n] = (G, meta, xs, core, bg, petals, p)
        print(f"n={n}: {len(meta):,} candidates, gamma matrix {G.shape}")
        for mode in ("consec", "geom5"):
            sc = chart_scalars(n, p, mode, xs, petals)
            values = word_from_scalars(n, p, xs, core, petals, sc)
            prod = (G @ np.array(sc, dtype=np.int64)) % p
            hits = np.flatnonzero(prod == 0)
            kept, hist = exact_retained(n, p, xs, values, meta, hits)
            want = BANKED[(n, p, mode)]
            print(f"   {mode:7s}: dual-filter survivors {len(hits):6,d} -> "
                  f"exact retained {kept:6,d}  (banked {want})  "
                  f"{'PASS' if kept == want else '*** FAIL ***'}  hist={hist}")
            if kept != want:
                print("A1 FAILED -- stopping, nothing downstream is reported.")
                sys.exit(1)
    print(f"A1 PASS on the banked cells of stage {stage}.\n")
    if stage != "16":
        stage32(G_by_n)
        return

    print("=" * 78)
    print("A3 EXHAUSTIVE WORST WORD, n=16 (t=4, q=97: all 922,180 proj. words)")
    print("=" * 78)
    G, meta, xs, core, bg, petals, p = G_by_n[16]
    t = len(petals)
    # projective representatives: leading nonzero coordinate = 1
    best = []
    counts = np.zeros(0, dtype=np.int32)
    allc = []
    for lead in range(t):
        free = t - lead - 1
        block = np.zeros((p ** free, t), dtype=np.int64)
        block[:, lead] = 1
        for j in range(free):
            reps = p ** (free - 1 - j)
            block[:, lead + 1 + j] = np.tile(
                np.repeat(np.arange(p), reps), p ** j)
        allc.append(block)
    C = np.concatenate(allc, axis=0)
    print(f"   enumerating {C.shape[0]:,} projective scalar vectors")
    res = np.zeros(C.shape[0], dtype=np.int32)
    step = 1500
    for s in range(0, C.shape[0], step):
        blk = C[s:s + step]
        res[s:s + blk.shape[0]] = np.count_nonzero(
            (blk.astype(np.float64) @ G.T.astype(np.float64)) % p == 0, axis=1)
    order = np.argsort(-res)
    mean = res.mean()
    print(f"   dual-filter count over the family: mean {mean:.2f}, "
          f"median {np.median(res):.0f}, max {res.max()}")
    # legality: distinct nonzero scalars (genuine 2-point petals)
    legal = np.array([len(set(row.tolist())) == t and 0 not in row.tolist()
                      for row in C[order[:4000]]])
    print(f"   top-4000 by count: {int(legal.sum())} are LEGAL "
          f"(distinct nonzero scalars)")
    shown = 0
    MAX16 = 0
    for oi in order:
        row = C[oi].tolist()
        if len(set(row)) != t or 0 in row:
            continue
        values = word_from_scalars(16, p, xs, core, petals, row)
        prod = (G @ np.array(row, dtype=np.int64)) % p
        hits = np.flatnonzero(prod == 0)
        kept, hist = exact_retained(16, p, xs, values, meta, hits)
        MAX16 = max(MAX16, kept)
        print(f"   scalars {row}: filter {len(hits):4d} exact {kept:4d} {hist}")
        shown += 1
        if shown >= 6:
            break
    print(f"   MAX16 (exact retained, legal words) = {MAX16}")

    print()
    print("=" * 78)
    print("A4 THE DISTINGUISHED MINIMAL-DEGREE WORD (deg U = k+1)")
    print("=" * 78)
    # U must vanish on core+background (8 points = 4 antipodal pairs).
    # deg U = k+1 forces c_i ~ (x_i^2 - x_bg^2).  Verify and evaluate.
    xbg2 = xs[bg] * xs[bg] % p
    sc_min = [(xs[a] * xs[a] - xbg2) % p for (a, b) in petals]
    print(f"   derived scalars c_i = x_i^2 - x_bg^2 : {sc_min}")
    values = word_from_scalars(16, p, xs, core, petals, sc_min)
    # confirm deg U = k+1 by interpolating U over the whole domain
    coef = [0] * 16
    for j in range(16):
        acc = 0
        for i in range(16):
            acc = (acc + values[i] * pow(xs[i], -j % 16, p)) % p
        coef[j] = acc * pow(16, p - 2, p) % p
    deg = max([j for j in range(16) if coef[j]] + [-1])
    print(f"   deg U = {deg} (k+1 = 9 expected); U monic-scaled coeffs tail "
          f"{[coef[j] for j in range(7, 16)]}")
    prod = (G @ np.array(sc_min, dtype=np.int64)) % p
    hits = np.flatnonzero(prod == 0)
    kept, hist = exact_retained(16, p, xs, values, meta, hits)
    print(f"   minimal-degree word: filter {len(hits)} exact retained {kept} "
          f"{hist}   (random-word mean {mean:.1f})")

    print()
    print(f"   MAX16 recorded = {MAX16}; mean16 = {mean:.2f}")
    return


def stage32(G_by_n):
    print("=" * 78)
    print("A5 SCALE TEST, n=32 (t=8): randomized + structured max search")
    print("=" * 78)
    rng0 = np.random.default_rng(1)
    G32, meta32, xs32, core32, bg32, petals32, p32 = G_by_n[32]
    t32 = len(petals32)
    rng = np.random.default_rng(20260807)
    NR = 200000
    R = rng.integers(0, p32, size=(NR, t32)).astype(np.int64)
    R[:, 0] = 1
    best32, res32 = 0, np.zeros(NR, dtype=np.int32)
    for s in range(0, NR, 1200):
        blk = R[s:s + 1200]
        res32[s:s + blk.shape[0]] = np.count_nonzero(
            (blk.astype(np.float64) @ G32.T.astype(np.float64)) % p32 == 0,
            axis=1)
    print(f"   random words: mean {res32.mean():.1f}, max {res32.max()} "
          f"over {NR:,} samples")
    # RANSAC: solve for c killing t-1 randomly chosen forms simultaneously
    print("   RANSAC over (t-1)-subsets of forms (targets the max-cover point)")
    bestv, bestc = 0, None
    for trial in range(4000):
        idx = rng.choice(G32.shape[0], size=t32 - 1, replace=False)
        M = G32[idx] % p32
        # nullspace over F_p by Gaussian elimination
        A = M.copy()
        rows, cols = A.shape
        piv, where = 0, []
        for col in range(cols):
            sel = None
            for r in range(piv, rows):
                if A[r, col] % p32:
                    sel = r
                    break
            if sel is None:
                continue
            A[[piv, sel]] = A[[sel, piv]]
            A[piv] = A[piv] * pow(int(A[piv, col]), p32 - 2, p32) % p32
            for r in range(rows):
                if r != piv and A[r, col] % p32:
                    A[r] = (A[r] - A[r, col] * A[piv]) % p32
            where.append(col)
            piv += 1
            if piv == rows:
                break
        freecols = [c for c in range(cols) if c not in where]
        if not freecols:
            continue
        v = np.zeros(cols, dtype=np.int64)
        v[freecols[0]] = 1
        for i, col in enumerate(where):
            v[col] = (-A[i, freecols[0]]) % p32
        cnt = int(np.count_nonzero((G32 @ v) % p32 == 0))
        if cnt > bestv:
            bestv, bestc = cnt, v.copy()
    print(f"   RANSAC best dual-filter count = {bestv} "
          f"(random mean {res32.mean():.1f}, banked words "
          f"{count_for_scalars(G32, chart_scalars(32,p32,'consec',xs32,petals32), p32)}"
          f"/"
          f"{count_for_scalars(G32, chart_scalars(32,p32,'geom5',xs32,petals32), p32)})")
    if bestc is not None:
        row = [int(v) for v in bestc]
        legal = len(set(row)) == t32 and 0 not in row
        print(f"   best scalars {row}  legal={legal}")
        values32 = word_from_scalars(32, p32, xs32, core32, petals32, row)
        hits32 = np.flatnonzero((G32 @ bestc) % p32 == 0)
        kept32, hist32 = exact_retained(32, p32, xs32, values32, meta32, hits32)
        print(f"   exact retained for the RANSAC word = {kept32} {hist32}")
        MAX32 = kept32
    # structured: minimal-degree analogue at n=32
    xbg2 = xs32[bg32] * xs32[bg32] % p32
    sc_min32 = [(xs32[a] * xs32[a] - xbg2) % p32 for (a, b) in petals32]
    values32 = word_from_scalars(32, p32, xs32, core32, petals32, sc_min32)
    hits32 = np.flatnonzero(
        (G32 @ np.array(sc_min32, dtype=np.int64)) % p32 == 0)
    kept32b, hist32b = exact_retained(32, p32, xs32, values32, meta32, hits32)
    print(f"   minimal-degree word at n=32: exact retained {kept32b} {hist32b}")
    MAX32 = max(MAX32, kept32b, int(res32.max()))
    print()
    print("=" * 78)
    print("A5 SUMMARY (n=32)")
    print("=" * 78)
    mean16, mean32 = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0, res32.mean()
    MAX16 = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
    print(f"   MAX16 = {MAX16}   mean16 = {mean16:.2f}   ratio = {MAX16/mean16:.2f}")
    print(f"   MAX32 = {MAX32}   mean32 = {mean32:.2f}")
    lhs = (MAX32 / MAX16) if MAX16 else float("inf")
    rhs = 3 * (mean32 / mean16)
    print(f"   MAX32/MAX16 = {lhs:.2f}   vs   3*(mean32/mean16) = {rhs:.2f}")
    print(f"   escape test 1 (growth):      {'FIRES' if lhs > rhs else 'does NOT fire'}")
    print(f"   escape test 2 (MAX16 > 10*mean16 = {10*mean16:.1f}): "
          f"{'FIRES' if MAX16 > 10*mean16 else 'does NOT fire'}")


if __name__ == "__main__":
    main()

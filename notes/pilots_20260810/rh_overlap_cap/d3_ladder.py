#!/usr/bin/env python3
"""d3_ladder.py -- rh_overlap_cap (round 31), deliverable D3.

Scaled search for the MAXIMAL-CORE PENCIL across >= 3 rate-1/2 scales.

Question: is the max pairwise overlap of a column-far pair equal to the
column-far ceiling a-1, and does a-1 exceed the Fisher threshold a^2/n?

A witness is a pair (E, W):  E subset D with |E| = a-1 (the core),
W = span(d1,d2) <= F^T a 2-dim space with T = D \\ E, such that
  (i)  the pair (d1,d2) is column-far at radius r = n-a
       (no a-subset S with both d1|_S, d2|_S in C|_S),
  (ii) no coordinate of T is a common zero (so the core is exactly E),
  (iii) at least 2 projective directions of W have >= a-|E| zeros in T
       (each such direction is a CA-bad slope with witness codeword 0).
Then two bad slopes lam != mu have A_lam cap A_mu = E exactly:
  ">=" because both agreement sets contain E; "<=" because column-farness
  caps every codeword-pair joint agreement at a-1 = |E|.

PRE-REGISTERED (PREREG R5/R6, PR-7/PR-8) BEFORE this ran:
  refutation succeeds at every cell with GAP_FISHER = (k-1) - a^2/n > 0
  and fails at (8,4,5).  The exact-arithmetic run d1_exact.py showed the
  relevant gap is GAP_FAR = (a-1) - a^2/n, which is POSITIVE at (8,4,5)
  too (7/8) -- so PR-7's second half is registered-and-refuted, see REPORT.

Sampling is over W; a POSITIVE is a proof, a NEGATIVE has no power
(declared).  The (8,4,17) cell is settled exhaustively by d2_maxcore.py.
"""
import itertools
import random
import time

OUT = open("notes/pilots_20260810/rh_overlap_cap/d3_ladder_results.txt", "w")


def emit(s=""):
    print(s)
    OUT.write(s + "\n")
    OUT.flush()


T0 = time.time()
random.seed(20260810)

CELLS = [  # (n, k, a, q)  -- q prime, q = 1 mod n (multiplicative coset of order n)
    (8, 4, 5, 17), (8, 4, 5, 41), (8, 4, 6, 17),
    (10, 5, 6, 11), (10, 5, 6, 31),
    (12, 6, 7, 13), (12, 6, 7, 37),
    (16, 8, 9, 17), (16, 8, 10, 17),
]
SAMPLES = 400
WALL = 250.0


def field(n, q):
    for cand in range(2, q):
        seen, x = set(), 1
        for _ in range(q - 1):
            x = x * cand % q
            seen.add(x)
        if len(seen) == q - 1:
            g = cand
            break
    zeta = pow(g, (q - 1) // n, q)
    D, x = [], 1
    for _ in range(n):
        D.append(x)
        x = x * zeta % q
    assert len(set(D)) == n
    return D


def forms_for(n, k, a, q, D, inv):
    """per a-subset S: the (a-k) functionals detecting y|_S in C|_S"""
    out = []
    for S in itertools.combinations(range(n), a):
        basis = []
        for i in S:
            coef, den = [1], 1
            for j in S:
                if j == i:
                    continue
                den = den * (D[i] - D[j]) % q
                new = [0] * (len(coef) + 1)
                for d, c in enumerate(coef):
                    new[d + 1] = (new[d + 1] + c) % q
                    new[d] = (new[d] - c * D[j]) % q
                coef = new
            di = inv[den % q]
            basis.append([c * di % q for c in coef])
        rows = [[b[d] for b in basis] for d in range(k, a)]
        out.append((S, rows))
    return out


emit("=" * 78)
emit("D3 -- MAXIMAL-CORE PENCIL across the rate-1/2 scale ladder")
emit("=" * 78)
emit("cell (n,k,a,q)   a^2/n     k-1   a-1  GAP_ALG  GAP_FAR  BUDGET  witness?"
     "   density")
emit("-" * 78)

import math

results = []
for (n, k, a, q) in CELLS:
    if time.time() - T0 > WALL:
        emit("  [wall budget reached; remaining cells NOT MEASURED]")
        break
    D = field(n, q)
    inv = [0] + [pow(i, q - 2, q) for i in range(1, q)]
    FS = forms_for(n, k, a, q, D, inv)
    e = a - 1
    r = n - a
    need = a - e                      # zeros in T needed for a bad direction
    gap_alg = (k - 1) - a * a / n
    gap_far = (a - 1) - a * a / n
    budget = (a - k) * math.log(q, 2) - math.log(math.comb(n, a), 2)
    found = None
    hits = trials = 0
    Elist = list(itertools.combinations(range(n), e))
    random.shuffle(Elist)
    for Eidx in Elist:
        if found is not None and trials >= SAMPLES:
            break
        if time.time() - T0 > WALL:
            break
        Eset = set(Eidx)
        T = [i for i in range(n) if i not in Eset]
        mm = len(T)
        # restrict every functional to T once
        rest = []
        for S, rows in FS:
            pos = {i: t for t, i in enumerate(S)}
            rest.append([tuple(row[pos[i]] if i in pos else 0 for i in T)
                         for row in rows])
        for _ in range(max(1, SAMPLES // max(1, len(Elist) // 6))):
            trials += 1
            w0 = [random.randrange(q) for _ in range(mm)]
            w1 = [random.randrange(q) for _ in range(mm)]
            # rank 2 and no common zero
            if any(w0[j] == 0 and w1[j] == 0 for j in range(mm)):
                continue
            # column-far?
            close = False
            for fr in rest:
                ok = True
                for vec in fr:
                    if sum(vec[j] * w0[j] for j in range(mm)) % q:
                        ok = False
                        break
                    if sum(vec[j] * w1[j] for j in range(mm)) % q:
                        ok = False
                        break
                if ok:
                    close = True
                    break
            if close:
                continue
            # bad directions.  need == 1 here (e = a-1), and since W has no
            # common zero, each j in T kills exactly ONE direction of W:
            #   w1[j] != 0 -> the finite direction t = -w0[j]/w1[j];
            #   w1[j] == 0 -> the direction [w1] itself ("infinity").
            assert need == 1
            seen = set()
            for j in range(mm):
                if w1[j]:
                    seen.add((-w0[j] * inv[w1[j]]) % q)
                else:
                    seen.add("inf")
            nd = len(seen)
            if nd >= 2:
                hits += 1
                if found is None:
                    found = (list(Eidx), list(w0), list(w1), nd)
        if found is not None and trials >= SAMPLES:
            break
    dens = hits / trials if trials else 0.0
    emit("(%2d,%2d,%2d,%5d) %7.4f %6d %5d %8.4f %8.4f %7.2f  %-8s  %.4f  (%d/%d)"
         % (n, k, a, q, a * a / n, k - 1, a - 1, gap_alg, gap_far, budget,
            "YES" if found else "no", dens, hits, trials))
    if found:
        emit("      witness E=%s  d1|T=%s  d2|T=%s  bad directions=%d"
             % (found[0], found[1], found[2], found[3]))
        emit("      -> pairwise overlap = |E| = %d  >  a^2/n = %.4f : %s"
             % (e, a * a / n, e * n > a * a))
    results.append((n, k, a, q, gap_alg, gap_far, budget, found is not None, dens))

emit("-" * 78)
emit("BUDGET := (a-k)*log2 q - log2 C(n,a)  is the small-scale analogue of the")
emit("razor union bound  #(U0,U1) * q^{k-a} < 1  (NOT pre-registered; derived")
emit("from the razor proof and reported as a diagnostic, see REPORT).")
emit("")
emit("razor row for comparison:  n=2^41 k=2^40 a=k+2^34")
n, k = 2 ** 41, 2 ** 40
a = k + 2 ** 34
emit("   a^2/n = %d   k-1 = %d   a-1 = %d" % (a * a // n, k - 1, a - 1))
emit("   GAP_ALG = %d   GAP_FAR = %d" % (k - 1 - a * a // n, a - 1 - a * a // n))
emit("   BUDGET >= (a-k)*255 - n = %d  (hugely positive)" % ((a - k) * 255 - n))
emit("")
emit("[total %.1fs]" % (time.time() - T0))
emit("=" * 78)
OUT.close()

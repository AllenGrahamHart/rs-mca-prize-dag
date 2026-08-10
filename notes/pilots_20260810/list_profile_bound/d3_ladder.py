#!/usr/bin/env python3
"""d3_ladder.py -- list_profile_bound (round 29).

(A) EXACT F_LMAX(8,4,a) for a in {5,6,7} at q in {17,41,97}, by exhaustive
    enumeration of received words modulo the two exact symmetries
    (translation by a list member -> 0 is in the list; scaling by F_q^*).
    This decides the registered question PRED-16: is the scaled cell's
    decay a q-INDEPENDENT absolute constant, or does it scale with log2 q?

(B) B_CAFAR(8,4,a) lower bounds by sampling at the same q, i.e. the
    ACTUAL target object (slopes), not the list.

Named functionals: F_LMAX, B_CAFAR, CAP_COMB.  No mean-model quantity
is computed (F3).
"""
import itertools
import random
import sys

n = 8
k = 4
NPAIR = int(sys.argv[1]) if len(sys.argv) > 1 else 900


def field(q):
    g = None
    for cand in range(2, q):
        x, seen = 1, set()
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


def build(q, D, a):
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
            di = pow(den % q, q - 2, q)
            basis.append([c * di % q for c in coef])
        rows = []
        for d in range(k, a):
            w = [0] * n
            for t, i in enumerate(S):
                w[i] = basis[t][d]
            rows.append(w)
        out.append((S, rows, basis))
    return out


def list_size(y, supp, subs, q, D):
    """number of deg<k codewords agreeing with y on >= a positions"""
    found = set()
    for S, rows, basis in subs:
        ok = True
        for w in rows:
            s = 0
            for i in supp:
                s += w[i] * y[i]
            if s % q:
                ok = False
                break
        if not ok:
            continue
        poly = [0] * k
        for t, i in enumerate(S):
            v = y[i]
            if v:
                b = basis[t]
                for d in range(k):
                    poly[d] = (poly[d] + v * b[d]) % q
        found.add(tuple(poly))
    return len(found)


def exact_flmax(q, a):
    """exhaustive over y with >= a zeros, first nonzero normalised to 1"""
    D = field(q)
    subs = build(q, D, a)
    jmax = n - a                       # y has >= a zeros
    best, arg = 1, None
    pos = list(range(n))
    for j in range(2, jmax + 1):       # j <= 1 can never give L >= 2
        for supp in itertools.combinations(pos, j):
            vals = [0] * n
            for tail in itertools.product(range(1, q), repeat=j - 1):
                vals[supp[0]] = 1
                for t in range(1, j):
                    vals[supp[t]] = tail[t - 1]
                L = list_size(vals, supp, subs, q, D)
                if L > best:
                    best, arg = L, (supp, tuple(vals[i] for i in supp))
    return best, arg


def bcafar_sample(q, a, npair, seed=20260810):
    D = field(q)
    subs = build(q, D, a)
    inv = [0] + [pow(i, q - 2, q) for i in range(1, q)]
    rnd = random.Random(seed)

    def drops(w, S, rows):
        for row in rows:
            s = 0
            for i in S:
                if w[i]:
                    s += row[i] * w[i]
            if s % q:
                return False
        return True

    def far(y1, y2):
        for S, rows, basis in subs:
            if drops(y1, S, rows) and drops(y2, S, rows):
                return False
        return True

    def ev(p, x):
        acc = 0
        for d in range(k - 1, -1, -1):
            acc = (acc * x + p[d]) % q
        return acc

    best, nfar = 0, 0
    for it in range(npair):
        if it % 2 == 0:
            y1 = [rnd.randrange(q) for _ in range(n)]
            y2 = [rnd.randrange(q) for _ in range(n)]
        else:
            E = rnd.sample(range(n), a - 1)
            u = [rnd.randrange(q) for _ in range(k)]
            v = [rnd.randrange(q) for _ in range(k)]
            y1 = [rnd.randrange(q) for _ in range(n)]
            y2 = [rnd.randrange(q) for _ in range(n)]
            for i in E:
                y1[i] = ev(u, D[i])
                y2[i] = ev(v, D[i])
            lam = rnd.randrange(1, q)
            for i in [z for z in range(n) if z not in E][:2]:
                y2[i] = (ev(v, D[i]) + rnd.randrange(1, q)) % q
                y1[i] = (ev(u, D[i]) - lam * (y2[i] - ev(v, D[i]))) % q
        if not far(y1, y2):
            continue
        nfar += 1
        M = 0
        for lam in range(q):
            w = [(y1[i] + lam * y2[i]) % q for i in range(n)]
            hit = False
            for S, rows, basis in subs:
                if drops(w, S, rows):
                    hit = True
                    break
            if hit:
                M += 1
        if M > best:
            best = M
    return best, nfar


print("=" * 74)
print("(A) EXACT F_LMAX(n=8,k=4,a) -- exhaustive modulo translation+scaling")
print("=" * 74)
print("%-6s %-6s %-10s %-10s %-12s" % ("q", "a", "F_LMAX", "log2", "log2 q"))
import math
res = {}
for q in (17, 41, 97):
    for a in (5, 6, 7):
        L, arg = exact_flmax(q, a)
        res[(q, a)] = L
        print("%-6d %-6d %-10d %-10.4f %-12.4f   witness supp/vals %s"
              % (q, a, L, math.log2(L), math.log2(q), arg))
print()
print("decay of the exact max list profile, per unit of a:")
for q in (17, 41, 97):
    d56 = math.log2(res[(q, 5)]) - math.log2(res[(q, 6)])
    print("  q=%-6d  a:5->6  F_DECAY = %.4f bits   ratio to log2 q = %.4f"
          % (q, d56, d56 / math.log2(q)))
print()
print("(B) B_CAFAR(n=8,k=4,a) sampled lower bounds (%d candidate pairs/cell)"
      % NPAIR)
print("%-6s %-6s %-10s %-10s %-10s" % ("q", "a", "M_max", "n-a+1", "col-far"))
for q in (17, 41, 97):
    for a in (5, 6, 7):
        M, nf = bcafar_sample(q, a, NPAIR)
        print("%-6s %-6d %-10d %-10d %-10d" % (q, a, M, n - a + 1, nf))
print("=" * 74)

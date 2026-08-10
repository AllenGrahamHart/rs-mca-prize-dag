#!/usr/bin/env python3
"""d2_maxcore.py -- rh_overlap_cap (round 31).

EXHAUSTIVE maximal-core census at the round-29 validation cell
(n,k,q) = (8,4,17), for a in {5,6,7}.

What is being decided
---------------------
T3 (banked at critical/nodes/rate_half_band_crossing_location/statement.md
:358-362) assumes "pairwise overlaps <= theta < a^2/n".  The overlaps in
question are |A_lam cap A_mu| for CA-bad slopes of a COLUMN-FAR pair.
By T1(ii) each such overlap is the joint agreement of a codeword PAIR
(u,v) with (f1,f2), so column-farness caps it at a-1 -- NOT at the MDS
codeword-agreement cap k-1 that round-29's THETA_ALG uses
(notes/pilots_20260810/list_profile_bound/PREREG.md:135).

Up to translation by a codeword pair, a configuration is
    E  = the core (common zero set), T = D \\ E,
    W  = span(d1,d2) <= F^T, a 2-dimensional space,
because bad slopes, agreement sets and column-farness are invariant
under GL_2 acting on the pair.  We enumerate (E,W) EXACTLY at the
maximal core e = a-1.

Strategy: mark the column-CLOSE W's first (they are exactly the 2-dim
subspaces of the kernels K_S, one per a-subset S), then sweep all W.
"""
import itertools
import time

OUT = open("notes/pilots_20260810/rh_overlap_cap/d2_maxcore_results.txt", "w")


def emit(s=""):
    print(s)
    OUT.write(s + "\n")
    OUT.flush()


T0 = time.time()
q, n, k = 17, 8, 4

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
inv = [0] + [pow(i, q - 2, q) for i in range(1, q)]


def build(a):
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
        out.append((S, rows, basis))
    return out


SUBS = {a: build(a) for a in (5, 6, 7)}


def drops(word, S, rows):
    for row in rows:
        s = 0
        for t, i in enumerate(S):
            if word[i]:
                s += row[t] * word[i]
        if s % q:
            return False
    return True


def column_far(y1, y2, a):
    for S, rows, _ in SUBS[a]:
        if drops(y1, S, rows) and drops(y2, S, rows):
            return False
    return True


def codewords_at(word, a):
    found = {}
    for S, rows, basis in SUBS[a]:
        if not drops(word, S, rows):
            continue
        poly = [0] * a
        for t, i in enumerate(S):
            v = word[i]
            if v:
                b = basis[t]
                for d in range(a):
                    poly[d] = (poly[d] + v * b[d]) % q
        key = tuple(poly[:k])
        if key not in found:
            ev = []
            for idx in range(n):
                acc = 0
                for d in range(k - 1, -1, -1):
                    acc = (acc * D[idx] + key[d]) % q
                ev.append(acc)
            found[key] = frozenset(i for i in range(n) if ev[i] == word[i])
    return found


def rref_rows(rows, mm):
    """row-reduce; return list of pivot rows (canonical RREF)"""
    mat = [list(r) for r in rows]
    piv, res = 0, []
    for col in range(mm):
        sel = None
        for i in range(piv, len(mat)):
            if mat[i][col]:
                sel = i
                break
        if sel is None:
            continue
        mat[piv], mat[sel] = mat[sel], mat[piv]
        c = inv[mat[piv][col]]
        mat[piv] = [v * c % q for v in mat[piv]]
        for i in range(len(mat)):
            if i != piv and mat[i][col]:
                f = mat[i][col]
                mat[i] = [(mat[i][j] - f * mat[piv][j]) % q for j in range(mm)]
        piv += 1
        if piv == len(mat):
            break
    for rr in mat[:piv]:
        res.append(tuple(rr))
    return res


def kernel(rows, mm):
    """basis of the common kernel of the given linear forms on F^mm"""
    R = rref_rows(rows, mm) if rows else []
    pivots = []
    for rr in R:
        for j in range(mm):
            if rr[j]:
                pivots.append(j)
                break
    free = [j for j in range(mm) if j not in pivots]
    bas = []
    for f in free:
        v = [0] * mm
        v[f] = 1
        for idx, rr in enumerate(R):
            v[pivots[idx]] = (-rr[f]) % q
        bas.append(v)
    return bas


def sub2(mm):
    """every 2-dim subspace of F_q^mm as a canonical RREF pair of rows"""
    for p0 in range(mm):
        for p1 in range(p0 + 1, mm):
            free0 = [j for j in range(p0 + 1, mm) if j != p1]
            free1 = list(range(p1 + 1, mm))
            for v0 in itertools.product(range(q), repeat=len(free0)):
                r0 = [0] * mm
                r0[p0] = 1
                for j, val in zip(free0, v0):
                    r0[j] = val
                for v1 in itertools.product(range(q), repeat=len(free1)):
                    r1 = [0] * mm
                    r1[p1] = 1
                    for j, val in zip(free1, v1):
                        r1[j] = val
                    yield (tuple(r0), tuple(r1))


emit("=" * 74)
emit("PART B -- EXHAUSTIVE census at the MAXIMAL core e = a-1, cell (8,4,17)")
emit("=" * 74)
emit("")

for a in (5, 6, 7):
    e = a - 1
    r = n - a
    tot = far = far_nocz = witness = 0
    best = None
    for Eidx in itertools.combinations(range(n), e):
        Eset = set(Eidx)
        T = [i for i in range(n) if i not in Eset]
        mm = len(T)
        bad = set()
        for S, rows, _ in SUBS[a]:
            pos = {i: t for t, i in enumerate(S)}
            forms = []
            for row in rows:
                forms.append([row[pos[i]] if i in pos else 0 for i in T])
            K = kernel(forms, mm)
            kk = len(K)
            if kk < 2:
                continue
            for (c0, c1) in sub2(kk):
                w0 = [sum(c0[t] * K[t][j] for t in range(kk)) % q for j in range(mm)]
                w1 = [sum(c1[t] * K[t][j] for t in range(kk)) % q for j in range(mm)]
                key = rref_rows([w0, w1], mm)
                if len(key) == 2:
                    bad.add(tuple(key))
        for (r0, r1) in sub2(mm):
            tot += 1
            if (r0, r1) in bad:
                continue
            far += 1
            if any(r0[j] == 0 and r1[j] == 0 for j in range(mm)):
                continue
            far_nocz += 1
            need = a - e                      # zeros inside T required for wt<=r
            nd = 0
            for t in range(q):
                d = [(r0[j] + t * r1[j]) % q for j in range(mm)]
                if sum(1 for v in d if v == 0) >= need:
                    nd += 1
            if sum(1 for v in r1 if v == 0) >= need:
                nd += 1
            if nd < 2:
                continue
            witness += 1
            if best is None:
                best = (Eidx, r0, r1, nd)
    emit("a = %d   sigma=%d  r=%d  core e=a-1=%d  |T|=%d" % (a, a - k, r, e, n - e))
    emit("   a^2/n = %d/%d = %.4f     a-1 = %d     k-1 = %d"
         % (a * a, n, a * a / n, a - 1, k - 1))
    emit("   2-dim W enumerated ........ %d" % tot)
    emit("   column-FAR ................ %d" % far)
    emit("   ... core exactly E ........ %d" % far_nocz)
    emit("   ... and >= 2 bad slopes ... %d    <-- CAP VIOLATORS" % witness)
    viol = witness > 0 and (a - 1) * n > a * a
    emit("   overlap a-1 = %d  vs  a^2/n = %.4f  ->  T3 hypothesis %s"
         % (a - 1, a * a / n, "REFUTED at this cell" if viol else "not refuted"))
    if best:
        emit("   first witness: E=%s  W=[%s ; %s]  bad directions=%d"
             % (list(best[0]), list(best[1]), list(best[2]), best[3]))
    emit("   [%.1fs]" % (time.time() - T0))
    emit("")
    globals()["BEST_%d" % a] = best

emit("-" * 74)
emit("FULL VERIFICATION of one witness at a=5 (true agreement sets)")
emit("-" * 74)
a = 5
Eidx, r0, r1, _ = BEST_5
T = [i for i in range(n) if i not in set(Eidx)]
d1 = [0] * n
d2 = [0] * n
for j, i in enumerate(T):
    d1[i] = r0[j]
    d2[i] = r1[j]
emit("  E = %s   T = %s" % (list(Eidx), T))
emit("  d1 = %s" % d1)
emit("  d2 = %s" % d2)
emit("  column_far(d1,d2,a=5) = %s" % column_far(d1, d2, a))
slopes = {}
for lam in range(q):
    w = [(d1[i] + lam * d2[i]) % q for i in range(n)]
    cw = codewords_at(w, a)
    if cw:
        slopes[lam] = cw
emit("  CA-bad finite slopes: %s" % sorted(slopes))
emit("  witnesses per slope:  %s" % {l: len(slopes[l]) for l in sorted(slopes)})
lam_list = sorted(slopes)
prod = 1
for l in lam_list:
    prod *= len(slopes[l])
emit("  witness assignments: %d" % prod)
best_theta = None
if prod <= 300000:
    for pick in itertools.product(*[sorted(slopes[l].items()) for l in lam_list]):
        As = [p[1] for p in pick]
        th = 0
        for i in range(len(As)):
            for j in range(i + 1, len(As)):
                th = max(th, len(As[i] & As[j]))
        if best_theta is None or th < best_theta:
            best_theta = th
    emit("  THETA_MIN over ALL witness assignments = %d" % best_theta)
    emit("  a^2/n = %.4f  ->  T3 hypothesis (theta < a^2/n) holds: %s"
         % (a * a / n, best_theta * n < a * a))
emit("  T1(iv): m_P <= 1 + r/(a-e) = %d ; observed bad slopes = %d ; n-a+1 = %d"
     % (1 + (n - a) // 1, len(lam_list), n - a + 1))
emit("")
emit("[total %.1fs]" % (time.time() - T0))
emit("=" * 74)
OUT.close()

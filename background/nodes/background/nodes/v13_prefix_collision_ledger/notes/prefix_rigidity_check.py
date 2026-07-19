#!/usr/bin/env python3
"""Exact replay of upstream lem:capg-prefix-rigidity + thm:capg-second-moment
   (cap25_cap_v13_raw.tex lines 9480-9612) at small parameters.

   All arithmetic is exact integer table lookups in explicitly constructed
   finite fields (prime fields and GF(p^k) via irreducible polynomials).
   No floats anywhere.

   Definitions used (verbatim sources cited in the report):
   - locator  ell_S(X) = prod_{s in S} (X - s), monic, squarefree   [tex:6534]
   - prefix   Phi_w(M) = ([X^{m-h}] ell_M)_{h=1..w}                 [tex:9169]
   - fiber    Fib_w(z) = Phi_w^{-1}(z)                              [tex:9170]
   - RIGIDITY CLAIM [tex:9479-9487]: M != M' m-subsets, Phi_w(M)=Phi_w(M')
       ==> |M\\M'| = |M'\\M| >= w+1; and if = w+1 then
       ell_{M\\M'} - ell_{M'\\M} is a nonzero constant.
   - SECOND MOMENT [tex:9575-9593]: sum_z N_w(z)^2 = C(n,m) + sum_{e>=w+1} P_e,
       P_e = sum_{|R|=m-e} sp_w(e; D\\R),
       sp_w(e; D') = #{ordered (A,B): monic split over D', deg e,
                        disjoint roots, deg(A-B) <= e-w-1}
   - TOP STRATUM [tex:9591-9593]: sp_w(w+1;D') = #{(A,c): A monic split deg w+1,
       c != 0, A-c split over D'}
   - PROTOTYPE [tex:9646-9652]: (w+1)|n ==> sp_w(w+1; mu_n) >= (n/(w+1))(n/(w+1)-1)
"""
import sys
from itertools import combinations
from math import comb

# ---------- exact finite fields as integer-coded tables ----------
def make_prime_field(p):
    q = p
    add = [[(a + b) % p for b in range(p)] for a in range(p)]
    mul = [[(a * b) % p for b in range(p)] for a in range(p)]
    neg = [(-a) % p for a in range(p)]
    return q, add, mul, neg

def make_ext_field(p, k, irred):
    """GF(p^k); elements coded as ints sum(c_i p^i); irred = monic irreducible
       coeff list (low->high) of length k+1 over F_p, all exact ints."""
    q = p ** k
    def dec(x):
        return [(x // p**i) % p for i in range(k)]
    def enc(cs):
        return sum((c % p) * p**i for i, c in enumerate(cs))
    def polymulmod(a, b):
        prod = [0] * (2 * k - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    prod[i + j] = (prod[i + j] + ai * bj) % p
        # reduce mod irred (monic, degree k)
        for d in range(2 * k - 2, k - 1, -1):
            c = prod[d]
            if c:
                prod[d] = 0
                for i in range(k):
                    prod[d - k + i] = (prod[d - k + i] - c * irred[i]) % p
        return prod[:k]
    add = [[enc([(x + y) % p for x, y in zip(dec(a), dec(b))])
            for b in range(q)] for a in range(q)]
    mul = [[enc(polymulmod(dec(a), dec(b))) for b in range(q)] for a in range(q)]
    neg = [enc([(-x) % p for x in dec(a)]) for a in range(q)]
    return q, add, mul, neg

# ---------- exact polynomial helpers (coeff lists, low -> high) ----------
def ptrim(f):
    while f and f[-1] == 0:
        f.pop()
    return f

def pdeg(f):
    return len(f) - 1  # convention: only called on nonzero (asserted)

def psub(f, g, ADD, NEG):
    n = max(len(f), len(g))
    out = [0] * n
    for i in range(n):
        a = f[i] if i < len(f) else 0
        b = g[i] if i < len(g) else 0
        out[i] = ADD[a][NEG[b]]
    return ptrim(out)

def locator(points, ADD, MUL, NEG):
    f = [1]
    for x in points:
        nx = NEG[x]
        g = [0] * (len(f) + 1)
        for i, c in enumerate(f):
            g[i + 1] = ADD[g[i + 1]][c]          # X * f
            g[i] = ADD[g[i]][MUL[nx][c]]          # (-x) * f
        f = g
    return f  # monic, length len(points)+1

def peval(f, x, ADD, MUL):
    acc = 0
    for c in reversed(f):
        acc = ADD[MUL[acc][x]][c]
    return acc

# ---------- per-configuration exhaustive check ----------
def check_config(name, field, D, m, w, do_second_moment=True):
    q, ADD, MUL, NEG = field
    n = len(D)
    assert 1 <= w < m <= n
    D = tuple(sorted(D))
    loc = lambda pts: locator(pts, ADD, MUL, NEG)

    # bucket all m-subsets by prefix
    buckets = {}
    for M in combinations(D, m):
        f = loc(M)                      # length m+1, f[m] == 1 (monic)
        assert f[m] == 1
        z = tuple(f[m - h] for h in range(1, w + 1))   # Phi_w(M)  [tex:9169]
        buckets.setdefault(z, []).append(M)

    total_pairs = 0
    pairs_at_top = 0
    min_e = None
    violations = []
    for z, fam in buckets.items():
        if len(fam) < 2:
            continue
        sets = [frozenset(M) for M in fam]
        for i in range(len(sets)):
            for j in range(i + 1, len(sets)):
                Mi, Mj = sets[i], sets[j]
                dif_i, dif_j = Mi - Mj, Mj - Mi
                e = len(dif_i)
                assert e == len(dif_j)          # |M\M'| = |M'\M| (equal sizes)
                total_pairs += 1
                min_e = e if min_e is None else min(min_e, e)
                if e <= w:                       # (R1) violated
                    violations.append(("R1", z, tuple(sorted(Mi)), tuple(sorted(Mj)), e))
                    continue
                if e == w + 1:                   # (R2): difference = nonzero constant
                    pairs_at_top += 1
                    dpoly = psub(loc(tuple(sorted(dif_i))),
                                 loc(tuple(sorted(dif_j))), ADD, NEG)
                    if not (len(dpoly) == 1 and dpoly[0] != 0):
                        violations.append(("R2", z, tuple(sorted(Mi)),
                                           tuple(sorted(Mj)), dpoly))

    # (S) second-moment stratification via INDEPENDENT (R, A, B) enumeration
    sm_line = "S: skipped"
    if do_second_moment:
        lhs = sum(len(fam) ** 2 for fam in buckets.values())
        emax = min(m, n - m)
        rhs = comb(n, m)
        strata = {}
        top_census_match = True
        for e in range(w + 1, emax + 1):
            # precompute all e-subset locators of D once
            elocs = {S: loc(S) for S in combinations(D, e)}
            P_e = 0
            for R in combinations(D, m - e):
                Rs = frozenset(R)
                Dp = [x for x in D if x not in Rs]
                cnt = 0
                for Aset in combinations(Dp, e):
                    As = frozenset(Aset)
                    fA = elocs[Aset]
                    rest = [x for x in Dp if x not in As]
                    for Bset in combinations(rest, e):
                        d = psub(fA, elocs[Bset], ADD, NEG)
                        assert d, "A=B impossible for disjoint nonempty roots"
                        if pdeg(d) <= e - w - 1:
                            cnt += 1
                if e == w + 1:
                    # cross-check vs constant-shift census #{(A,c)} [tex:9591]
                    cs = 0
                    for Aset in combinations(Dp, e):
                        fA = elocs[Aset]
                        vals = {}
                        for x in Dp:
                            vals.setdefault(peval(fA, x, ADD, MUL), 0)
                            vals[peval(fA, x, ADD, MUL)] += 1
                        # A - c split over D' <=> A(X)=c at exactly e distinct
                        # points of D' (monic deg e with e roots in D')
                        for c, r in vals.items():
                            if c != 0 and r == e:
                                cs += 1
                    if cs != cnt:
                        top_census_match = False
                P_e += cnt
                strata[e] = strata.get(e, 0) + cnt
            rhs += P_e
        ok_sm = (lhs == rhs)
        sm_line = (f"S: lhs={lhs} rhs={rhs} {'OK' if ok_sm else 'MISMATCH'}; "
                   f"strata P_e={strata}; top-census {'OK' if top_census_match else 'MISMATCH'}")
        if not ok_sm:
            violations.append(("S", lhs, rhs))
        if not top_census_match:
            violations.append(("TOP-CENSUS",))

    status = "PASS" if not violations else "FAIL"
    print(f"[{status}] {name}: n={n} m={m} w={w} | colliding pairs={total_pairs} "
          f"(at e=w+1: {pairs_at_top}, min e seen: {min_e}) | {sm_line}")
    for v in violations:
        print("    VIOLATION:", v)
    return total_pairs, pairs_at_top, violations

# ---------- build the suite ----------
F5  = make_prime_field(5)
F7  = make_prime_field(7)
F13 = make_prime_field(13)
F17 = make_prime_field(17)
GF4 = make_ext_field(2, 2, [1, 1, 1])       # x^2 + x + 1
GF8 = make_ext_field(2, 3, [1, 1, 0, 1])    # x^3 + x + 1
GF9 = make_ext_field(3, 2, [1, 0, 1])       # x^2 + 1

def mu(field, order_check):
    """all x with x^ord = 1 -- brute force via tables"""
    q, ADD, MUL, NEG = field
    out = []
    for x in range(1, q):
        y = 1
        for _ in range(order_check):
            y = MUL[y][x]
        if y == 1:
            out.append(x)
    return out

suite_pairs = 0
suite_top = 0
all_viol = []

def run(name, field, D, m, w, sm=True):
    global suite_pairs, suite_top, all_viol
    tp, pt, v = check_config(name, field, D, m, w, sm)
    suite_pairs += tp; suite_top += pt; all_viol += v

# 1. F5, D = whole field INCLUDING 0 (lemma allows any D subset of F)
for m in range(2, 5):
    for w in range(1, m):
        run("F5 D=F5(with 0)", F5, list(range(5)), m, w)

# 2. F7, D = mu_3 = {1,2,4} and coset 3*mu_3 = {3,6,5}
for m in (2, 3):
    for w in range(1, m):
        run("F7 D=mu3", F7, [1, 2, 4], m, w)
        run("F7 D=3*mu3 coset", F7, [3, 5, 6], m, w)

# 3. F13, D = mu_12 (full multiplicative group, n=12), structured rows
run("F13 D=mu12", F13, list(range(1, 13)), 4, 1)
run("F13 D=mu12", F13, list(range(1, 13)), 4, 2)
run("F13 D=mu12", F13, list(range(1, 13)), 4, 3)
run("F13 D=mu12", F13, list(range(1, 13)), 6, 2)

# 4. F13, unstructured D including 0, all (m,w) with m <= 5
D_unstr = [0, 1, 2, 3, 5, 7, 11]
for m in range(2, 6):
    for w in range(1, m):
        run("F13 D=unstructured(with 0)", F13, D_unstr, m, w)

# 5. GF(4), whole field (char 2!)
for m in (2, 3):
    for w in range(1, m):
        run("GF4 D=GF4(with 0)", GF4, list(range(4)), m, w)

# 6. GF(8), D = mu_7 = GF(8)^* (char 2, structured)
for m in range(2, 6):
    for w in range(1, m):
        run("GF8 D=mu7", GF8, list(range(1, 8)), m, w)

# 7. GF(9), D = mu_8 (char 3)
for m in (3, 4):
    for w in range(1, m):
        run("GF9 D=mu8", GF9, list(range(1, 9)), m, w)

# 8. F17, D = mu_16, one bigger collision-rich row (rigidity + full S)
run("F17 D=mu16", F17, list(range(1, 17)), 4, 1)

# ---------- prototype lower bound check [tex:9646-9652] ----------
print("\n--- pullback prototype: sp_w(w+1; mu_n) >= (n/(w+1))(n/(w+1)-1), F13 mu_12 ---")
q, ADD, MUL, NEG = F13
D12 = tuple(range(1, 13))
proto_fail = []
for wp1 in (2, 3, 4, 6):   # divisors of 12 (w+1), i.e. w = 1,2,3,5
    w = wp1 - 1
    cnt = 0
    elocs = {S: locator(S, ADD, MUL, NEG) for S in combinations(D12, wp1)}
    for Aset in combinations(D12, wp1):
        As = frozenset(Aset)
        fA = elocs[Aset]
        rest = [x for x in D12 if x not in As]
        for Bset in combinations(rest, wp1):
            d = psub(fA, elocs[Bset], ADD, NEG)
            if len(d) == 1 and d[0] != 0:    # deg(A-B) <= 0, nonzero
                cnt += 1
    bound = (12 // wp1) * (12 // wp1 - 1)
    ok = cnt >= bound
    print(f"  w={w}: sp_w(w+1; mu_12) = {cnt} >= {bound} : {'OK' if ok else 'VIOLATION'}")
    if not ok:
        proto_fail.append((w, cnt, bound))

# ---------- verdict ----------
print("\n================ SUMMARY ================")
print(f"total colliding (unordered) pairs examined : {suite_pairs}")
print(f"pairs at the top stratum e = w+1           : {suite_top}")
assert suite_pairs > 0, "NON-VACUITY FAILURE: no colliding pairs examined"
assert suite_top > 0, "NON-VACUITY FAILURE: no e=w+1 pairs examined"
if all_viol or proto_fail:
    print("VERDICT: REFUTED -- violations found:", all_viol, proto_fail)
    sys.exit(1)
print("VERDICT: all rigidity, second-moment, top-census and prototype checks PASS")

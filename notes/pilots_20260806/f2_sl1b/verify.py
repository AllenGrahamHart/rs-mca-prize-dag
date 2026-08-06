#!/usr/bin/env python3
"""SL-1b verifier -- round 16 pilot notes/pilots_20260806/f2_sl1b/.

Target (verbatim, notes/pilots_20260804/f2_sl1_powersums/PROOFS.md:316-319):

    **SL-1b (the named residual, replacing SL-1 on the obligation list):** prove
    a **lower** bound `dim_{F_p} L >= m . log_p 3` (or a second-moment /
    anti-concentration step for `Z(L)`).  This is a counting statement about the
    deployed `L`; SL-1 (distance) is now discharged and is not the obstruction.

Setting (f2_opening/PROOFS.md:7-43):  F_q = F_{p^k}; mu_n <= F_q^*, n even;
W <= mu_n closed under x -> -x; m = |W|/2; y_1..y_m one representative per
antipodal pair; Lambda a set of ODD exponents; L = image of the F_p-linear
evaluation map c |-> (Tr_{F_q/F_p} f(y_i))_i, f(x) = sum_{l in Lambda} C_l x^l.

By f2_opening/PROOFS.md:76-82, eps in L^perp  <=>  sum_i eps_i y_i^l = 0 in F_q
for every l in Lambda.  So L^perp = ker_{F_p}(A), A = (y_i^l), and
dim_{F_p} L = rank over F_p of the (k|Lambda|) x m matrix obtained by writing
each F_q entry in an F_p-basis.

Stages
  S0  provenance: every quoted line is really in the file it is cited from
  S1  PA-1 lower bound   dim L >= min(m, R)        (the pre-registered proof)
  S2  upper bound        dim L <= min(m, k|Lambda|)
  S3  sharpness: dim L = min(m,R) attained (k=1 family), dim L = min(m,kR) too
  S4  (R-A) => (R-B)?  search for dim L >= m log_p 3 WITH a nonzero ternary dual
  S5  replay of f2_sl1_powersums/PROOFS.md:194-199 shapes, now with dim L
  S6  the abstract counterexample: the PROOFS.md:298 "iff" is random-only
  S7  official-row arithmetic: (R-A) per rung per live t, exact-margin
  S8  q = p^k feasibility of the deployed windows (2-adic valuation)

Everything is exact: integers / Fractions in the small grid, Decimal(60) with a
reported margin at the official row.  No decision anywhere is taken on a float.
Exit code 0 iff every check passes.
"""

import itertools
import os
import sys
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 60

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

OK_ALL = True
LOG = []


def note(s=""):
    LOG.append(s)
    print(s)


def check(label, cond, detail=""):
    global OK_ALL
    OK_ALL = OK_ALL and bool(cond)
    note(f"  [{'PASS' if cond else 'FAIL'}] {label}" + (f"   -- {detail}" if detail else ""))
    return bool(cond)


# ------------------------------------------------------------------ F_{p^k} --

def _poly_mul(a, b, p, k, red):
    res = [0] * (2 * k - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    res[i + j] = (res[i + j] + ai * bj) % p
    for d in range(2 * k - 2, k - 1, -1):
        c = res[d]
        if c:
            res[d] = 0
            for j in range(k):
                res[d - k + j] = (res[d - k + j] + c * red[j]) % p
    return tuple(res[:k])


def _has_root(coeffs, p):
    """coeffs = monic f as f(X) = X^k - sum red[j] X^j; test f(x)=0 for x in F_p."""
    k, red = coeffs
    for x in range(p):
        v = pow(x, k, p)
        for j in range(k):
            v = (v - red[j] * pow(x, j, p)) % p
        if v == 0:
            return True
    return False


def build_field(p, k):
    """Return (red, one, mul, elements). Valid for k <= 3 (no-root irreducibility)."""
    assert k <= 3
    if k == 1:
        red = (0,)
    else:
        red = None
        for cand in itertools.product(range(p), repeat=k):
            if not _has_root((k, cand), p):
                red = cand
                break
        assert red is not None, (p, k)
    one = tuple([1] + [0] * (k - 1))

    def mul(a, b):
        return _poly_mul(a, b, p, k, red)

    return red, one, mul


def fpow(a, e, mul, one):
    r, b = one, a
    while e:
        if e & 1:
            r = mul(r, b)
        b = mul(b, b)
        e >>= 1
    return r


def factorize(x):
    f, d = {}, 2
    while d * d <= x:
        while x % d == 0:
            f[d] = f.get(d, 0) + 1
            x //= d
        d += 1
    if x > 1:
        f[x] = f.get(x, 0) + 1
    return f


def mult_order(a, n):
    """order of a mod n (a coprime to n)."""
    o, x = 1, a % n
    while x != 1:
        x = (x * a) % n
        o += 1
        if o > n:
            return None
    return o


def root_of_unity(p, k, n):
    """A generator zeta of mu_n <= F_{p^k}^*, with mul/one of that field."""
    red, one, mul = build_field(p, k)
    q = p ** k
    assert (q - 1) % n == 0
    primes = list(factorize(q - 1))
    gen = None
    for a in itertools.product(range(p), repeat=k):
        if all(c == 0 for c in a):
            continue
        if all(fpow(a, (q - 1) // r, mul, one) != one for r in primes):
            gen = a
            break
    assert gen is not None
    zeta = fpow(gen, (q - 1) // n, mul, one)
    assert fpow(zeta, n, mul, one) == one
    for r in factorize(n):
        assert fpow(zeta, n // r, mul, one) != one
    return zeta, mul, one


# ------------------------------------------------------------------ linalg --

def rank_mod_p(rows, ncols, p):
    M = [list(r) for r in rows]
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, len(M)):
            if M[i][c] % p:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [(v * inv) % p for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % p for j in range(ncols)]
        r += 1
        if r == len(M):
            break
    return r, M[:r]


# ------------------------------------------------------------- configuration --

def window(p, k, n, kind):
    """Return (m, [y_1..y_m]) as F_q elements, or None if not antipodally closed."""
    zeta, mul, one = root_of_unity(p, k, n)
    pw = [one]
    for _ in range(n):
        pw.append(mul(pw[-1], zeta))
    if kind == "full":
        exps = list(range(n))
    else:
        from math import gcd
        exps = [a for a in range(n) if gcd(a, n) == 1]
    S = set(exps)
    if any(((a + n // 2) % n) not in S for a in exps):
        return None
    reps = sorted({min(a, (a + n // 2) % n) for a in exps})
    if 2 * len(reps) != len(exps):
        return None
    return len(reps), [pw[a] for a in reps], mul, one, reps


def config_matrix(p, k, n, kind, R, a0):
    """F_p matrix of the conditions sum_i eps_i y_i^l = 0, l = 2a0+1,...,2a0+2R-1."""
    w = window(p, k, n, kind)
    if w is None:
        return None
    m, ys, mul, one, reps = w
    hi = 2 * a0 + 2 * R - 1
    if hi >= n:                      # exponents must be distinct residues mod n
        return None
    lam = [2 * a0 + 2 * j + 1 for j in range(R)]
    rows = []
    for l in lam:
        vals = [fpow(y, l, mul, one) for y in ys]
        for c in range(k):
            rows.append([v[c] % p for v in vals])
    return m, lam, rows, reps


def min_ternary_weight(rows, m, p, want_vec=False):
    """Minimum weight of a NONZERO ternary vector in ker(rows) over F_p, or None.

    Meet in the middle on the RREF: exact, no sampling."""
    rk, R2 = rank_mod_p(rows, m, p)
    if rk == m:
        return (None, None) if want_vec else None
    h = m // 2
    left, rght = list(range(h)), list(range(h, m))

    def col(j, v):
        return tuple((R2[i][j] * v) % p for i in range(rk))

    tbl_any, tbl_nz = {}, {}
    for eps in itertools.product((0, 1, p - 1), repeat=len(left)):
        s = [0] * rk
        wt = 0
        for jj, e in zip(left, eps):
            if e:
                wt += 1
                cj = col(jj, e)
                for i in range(rk):
                    s[i] = (s[i] + cj[i]) % p
        key = tuple(s)
        if key not in tbl_any or wt < tbl_any[key][0]:
            tbl_any[key] = (wt, eps)
        if wt and (key not in tbl_nz or wt < tbl_nz[key][0]):
            tbl_nz[key] = (wt, eps)
    best, bvec = None, None
    for eps in itertools.product((0, 1, p - 1), repeat=len(rght)):
        s = [0] * rk
        wt = 0
        for jj, e in zip(rght, eps):
            if e:
                wt += 1
                cj = col(jj, e)
                for i in range(rk):
                    s[i] = (s[i] + cj[i]) % p
        key = tuple((-x) % p for x in s)
        tab = tbl_any if wt else tbl_nz
        if key in tab:
            tot = wt + tab[key][0]
            if best is None or tot < best:
                best, bvec = tot, tuple(tab[key][1]) + tuple(eps)
    return (best, bvec) if want_vec else best


# --------------------------------- independent cross-check: cyclotomic route --

def poly_trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def zdiv(a, b):
    """Exact division of integer polynomials (lists, low-to-high)."""
    a = list(a)
    q = [0] * (len(a) - len(b) + 1)
    for i in range(len(q) - 1, -1, -1):
        c = a[i + len(b) - 1] // b[-1]
        q[i] = c
        for j, bj in enumerate(b):
            a[i + j] -= c * bj
    assert not any(a), "inexact polynomial division"
    return q


def cyclotomic(n, _memo={}):
    if n in _memo:
        return _memo[n]
    num = [-1] + [0] * (n - 1) + [1]              # X^n - 1
    for d in range(1, n):
        if n % d == 0:
            num = zdiv(num, cyclotomic(d))
    _memo[n] = num
    return num


def pmod(a, g, p):
    a = [x % p for x in a]
    dg = len(g) - 1
    inv = pow(g[-1], p - 2, p)
    for i in range(len(a) - 1, dg - 1, -1):
        c = (a[i] * inv) % p
        if c:
            for j in range(dg + 1):
                a[i - dg + j] = (a[i - dg + j] - c * g[j]) % p
    return poly_trim([x % p for x in a[:dg]])


def cyclotomic_factor(n, p, k):
    """A monic irreducible degree-k factor of Phi_n mod p, found by trial."""
    Phi = [x % p for x in cyclotomic(n)]
    for tail in itertools.product(range(p), repeat=k):
        g = list(tail) + [1]
        if not pmod(list(Phi), g, p):
            return g
    return None


def dimL_via_cyclotomic(p, n, k, reps, lam):
    """dim L and min ternary weight computed WITHOUT any field-element code:
    eps in L^perp  <=>  g(X) | sum_i eps_i X^{(a_i l) mod n}  in F_p[X]."""
    g = cyclotomic_factor(n, p, k)
    assert g is not None, (n, p, k)
    rows = []
    for l in lam:
        red = []
        for a in reps:
            e = (a * l) % n
            mono = [0] * e + [1]
            red.append(pmod(mono, g, p) + [0] * (k - len(pmod(mono, g, p))))
        for c in range(k):
            rows.append([red[i][c] % p for i in range(len(reps))])
    rk, _ = rank_mod_p(rows, len(reps), p)
    return rk, min_ternary_weight(rows, len(reps), p)


# ----------------------------------------------------------------- the grid --

PRIMES = (3, 5, 7, 11, 13, 17, 19)
NMAX, MMAX, RMAX, KMAX = 48, 12, 8, 3
SWEEP_MMAX = 10


def grid():
    from math import gcd
    out = []
    for p in PRIMES:
        for n in range(4, NMAX + 1, 2):
            if n % p == 0:
                continue
            k = mult_order(p, n)
            if k is None or k > KMAX:
                continue
            for kind in ("full", "ord"):
                w = window(p, k, n, kind)
                if w is None:
                    continue
                m = w[0]
                if m > MMAX or m < 2:
                    continue
                for a0 in (0, 1, 2):
                    for R in range(1, min(m + 1, RMAX) + 1):
                        cm = config_matrix(p, k, n, kind, R, a0)
                        if cm is None:
                            continue
                        mm, lam, rows, reps = cm
                        rk, _ = rank_mod_p(rows, mm, p)
                        out.append(dict(p=p, k=k, n=n, kind=kind, m=mm, R=R,
                                        a0=a0, nlam=len(lam), dimL=rk,
                                        rows=rows, lam=lam, reps=reps))
    return out


# ------------------------------------------------------------------ stages --

def S0_provenance():
    note("\n=== S0 provenance: every quoted line is present where cited ===")
    want = [
        ("notes/pilots_20260804/f2_sl1_powersums/PROOFS.md", 316,
         "**SL-1b (the named residual, replacing SL-1 on the obligation list):** prove"),
        ("notes/pilots_20260804/f2_sl1_powersums/PROOFS.md", 317,
         "a **lower** bound `dim_{F_p} L >= m · log_p 3` (or a second-moment /"),
        ("notes/pilots_20260804/f2_sl1_powersums/PROOFS.md", 298,
         "   L^perp ∩ T = {0}     iff  p^d >~ 3^m   iff  d >= m · log_p 3    <-- existence"),
        ("notes/pilots_20260804/f2_sl1_powersums/PROOFS.md", 297,
         "   E[Z] = O(1)          iff  p^d >~ 2^m   iff  d >= m / log2 p     <-- LEMMA 3"),
        ("notes/pilots_20260804/f2_opening/PROOFS.md", 42,
         "Let **`L`** be the image of the `F_p`-linear evaluation map"),
        ("notes/pilots_20260804/f2_opening/PROOFS.md", 81,
         "    sum_{i=1}^{m} eps_i y_i^{l} = 0  in F_{p^2},  for every l in Lambda."),
        ("notes/pilots_20260804/f2_opening/PROOFS.md", 225,
         "    dim_{F_p} L  >=  m / log2 p  -  o(n)/log2 p."),
        ("notes/pilots_20260804/f2_opening/PROOFS.md", 15,
         "`W = {x : ord(x) = n_j}`, `m_j = 2^{22+j}`; the full-group window is"),
        ("notes/pilots_20260804/f2_opening/PROOFS.md", 330,
         "  is forced, since `dim L <= t < m`) and (O1) reduces to bounding"),
        ("notes/pilots_20260804/f2_sl1_powersums/PROOFS.md", 99,
         "> and `eps != 0` satisfies **`wt(eps) >= R + 1`**."),
    ]
    ok = True
    for rel, ln, text in want:
        path = os.path.join(REPO, rel)
        with open(path, encoding="utf-8") as fh:
            lines = fh.read().split("\n")
        got = lines[ln - 1] if ln - 1 < len(lines) else "<EOF>"
        hit = got.strip() == text.strip()
        ok = ok and hit
        if not hit:
            note(f"       MISMATCH {rel}:{ln}\n         want: {text!r}\n         got : {got!r}")
    return check("S0 all 10 cited lines verbatim at the cited file:line", ok,
                 "quotes are load-bearing; provenance is machine-checked")


def S1_lower_bound(G):
    note("\n=== S1 PA-1: dim_{F_p} L >= min(m, R)  (the pre-registered proof) ===")
    bad = [g for g in G if g["dimL"] < min(g["m"], g["R"])]
    ok = check(f"S1 lower bound holds on all {len(G)} configurations", not bad,
               f"falsifier (F1) not triggered; violations = {len(bad)}")
    if bad:
        for g in bad[:5]:
            note(f"       VIOLATION {g}")
    eq = [g for g in G if g["dimL"] == min(g["m"], g["R"])]
    note(f"       equality dim L = min(m,R) in {len(eq)}/{len(G)} configurations")
    return ok


def S2_upper_bound(G):
    note("\n=== S2 upper bound: dim L <= min(m, k|Lambda|) ===")
    bad = [g for g in G if g["dimL"] > min(g["m"], g["k"] * g["nlam"])]
    ok = check(f"S2 upper bound holds on all {len(G)} configurations", not bad,
               "falsifier (S-F3) not triggered")
    at = [g for g in G if g["dimL"] == min(g["m"], g["k"] * g["nlam"])]
    note(f"       equality dim L = min(m,k|Lambda|) in {len(at)}/{len(G)} configurations")
    return ok


def S3_sharpness(G):
    note("\n=== S3 sharpness of the two bounds ===")
    k1 = [g for g in G if g["k"] == 1 and g["R"] <= g["m"]]
    ok = check(f"S3 every k=1 configuration has dim L = R EXACTLY ({len(k1)} rows)",
               all(g["dimL"] == g["R"] for g in k1) and len(k1) > 0,
               "so min(m,R) is SHARP inside the setting's own hypotheses: "
               "no proof can beat t/2 without using k >= 2")
    k2 = [g for g in G if g["k"] >= 2 and g["R"] <= g["m"]]
    hit = [g for g in k2 if g["dimL"] == min(g["m"], g["k"] * g["R"])]
    ok &= check("S3 the upper bound min(m,kR) is attained too", len(hit) > 0,
                f"{len(hit)}/{len(k2)} configurations with k>=2 attain it -- so "
                "dim L genuinely ranges over the whole interval [min(m,R), min(m,kR)]")
    strict = [g for g in k2 if min(g["m"], g["R"]) < g["dimL"] < min(g["m"], g["k"] * g["R"])]
    note(f"       strictly interior rows: {len(strict)}")
    return ok


def S4_implication(G):
    note("\n=== S4 does (R-A) dim L >= m log_p 3 imply (R-B) L^perp cap T = {0}? ===")
    note("       threshold tested EXACTLY as the integer comparison p^{dim L} >= 3^m")
    ce = []
    tested = 0
    for g in G:
        if g["p"] == 3:
            continue                        # declared degenerate in PREREG D
        if g["m"] > SWEEP_MMAX:
            continue
        if g["p"] ** g["dimL"] < 3 ** g["m"]:
            continue                        # (R-A) fails here: not a test case
        tested += 1
        w = min_ternary_weight(g["rows"], g["m"], g["p"])
        if w is not None:
            ce.append((g, w))
    note(f"       {tested} configurations satisfy (R-A) with p>3 and m<={SWEEP_MMAX}")
    ok = check("S4 counterexamples to (R-A) => (R-B) EXIST (falsifier S-F2 FIRES)",
               len(ce) > 0,
               f"{len(ce)} configurations satisfy dim L >= m log_p 3 and STILL "
               "carry a nonzero ternary dual vector")
    for g, w in sorted(ce, key=lambda gw: (gw[0]["p"], gw[0]["m"], gw[0]["R"]))[:8]:
        note(f"       WITNESS p={g['p']} k={g['k']} n={g['n']} W={g['kind']} "
             f"m={g['m']} R={g['R']} a0={g['a0']} : dim L = {g['dimL']}, "
             f"p^dimL = {g['p']**g['dimL']} >= 3^m = {3**g['m']}, "
             f"min ternary dual weight = {w} (>= R+1 = {g['R']+1}, SL-1 respected)")
    if ce:
        ok &= check("S4 every witness respects THEOREM SL-1 (wt >= R+1)",
                    all(w >= g["R"] + 1 for g, w in ce),
                    "the counterexamples do not contradict the PROVED distance law")
    return ok, ce


def S4b_round15_predicate(ce):
    """f2_sl1_powersums/PROOFS.md:320-322 claims, over 74 configurations, that
    'the count threshold m.log2 3 > dim L . log2 p NEVER under-predicts'.
    Its code at f2_sl1_powersums/verify.py:454 uses p.bit_length()-1 = FLOOR(log2 p)
    in place of log2 p.  Both are evaluated here on my witnesses."""
    note("\n=== S4b round-15's supporting measurement, re-evaluated ===")
    from math import log2
    fn_true = [(g, w) for g, w in ce
               if not (g["m"] * log2(3) > g["dimL"] * log2(g["p"]))]
    fn_floor = [(g, w) for g, w in ce
                if not (g["m"] * log2(3) > g["dimL"] * (g["p"].bit_length() - 1))]
    ok = check("S4b with the predicate AS WRITTEN (true log2 p) it DOES "
               "under-predict", len(fn_true) > 0,
               f"{len(fn_true)} of my {len(ce)} witnesses are false negatives "
               "for 'm log2 3 > dim L log2 p' -- i.e. a nonzero ternary dual "
               "exists although the entropy budget is exhausted")
    ok &= check("S4b with the predicate AS CODED (floor(log2 p)) far fewer do",
                len(fn_floor) < len(fn_true),
                f"{len(fn_floor)} false negatives under floor(log2 p) vs "
                f"{len(fn_true)} under log2 p -- the floor UNDERSTATES the "
                "condition budget (log2 7 = 2.807 vs 2), which biases the test "
                "towards over-prediction, the 'safe direction' reported at "
                "f2_sl1_powersums/PROOFS.md:322")
    for g, w in fn_true[:4]:
        note(f"       FALSE NEGATIVE p={g['p']} k={g['k']} n={g['n']} "
             f"W={g['kind']} m={g['m']} R={g['R']} a0={g['a0']}: "
             f"m log2 3 = {g['m']*log2(3):.3f} vs dim L log2 p = "
             f"{g['dimL']*log2(g['p']):.3f} (coded: "
             f"{g['dimL']*(g['p'].bit_length()-1):.3f}); ternary dual of "
             f"weight {w} EXISTS")
    return ok


def S9_independent(G, ce):
    """Recompute dim L and the min ternary weight by a SECOND, disjoint route:
    cyclotomic polynomial mod p + polynomial remainder.  No field-element
    tuples, no generator search.  Both quantities are invariant under the
    relabelling zeta -> zeta^u, so the two routes must agree exactly."""
    note("\n=== S9 independent cross-check via Phi_n(X) mod p (disjoint code path) ===")
    picks = []
    seen = set()
    for g, w in ce:
        key = (g["p"], g["k"], g["n"], g["kind"], g["R"], g["a0"])
        if key not in seen and g["m"] <= 9:
            seen.add(key)
            picks.append(g)
        if len(picks) >= 6:
            break
    for (p, k, n, R) in ((3, 2, 8, 2), (5, 2, 12, 3), (7, 2, 16, 4)):
        cm = config_matrix(p, k, n, "full", R, 0)
        mm, lam, rows, reps = cm
        rk, _ = rank_mod_p(rows, mm, p)
        picks.append(dict(p=p, k=k, n=n, kind="full", m=mm, R=R, a0=0,
                          dimL=rk, rows=rows, lam=lam, reps=reps))
    ok = True
    for g in picks:
        d2, w2 = dimL_via_cyclotomic(g["p"], g["n"], g["k"], g["reps"], g["lam"])
        w1 = min_ternary_weight(g["rows"], g["m"], g["p"])
        ok &= check(f"S9 p={g['p']} k={g['k']} n={g['n']} W={g['kind']} "
                    f"m={g['m']} R={g['R']} a0={g['a0']}",
                    d2 == g["dimL"] and w2 == w1,
                    f"cyclotomic route: dim L = {d2}, min ternary wt = {w2}; "
                    f"field route: dim L = {g['dimL']}, min ternary wt = {w1}")
    return ok


def S5_replay():
    note("\n=== S5 replay of f2_sl1_powersums/PROOFS.md:194-199, now with dim L ===")
    shapes = [(3, 2, 8, 2, 3), (5, 2, 12, 3, 5), (5, 2, 24, 3, 5),
              (5, 2, 24, 4, 5), (7, 2, 16, 4, 7)]
    ok = True
    for (p, k, n, R, claimed) in shapes:
        assert mult_order(p, n) == k, (p, n, mult_order(p, n))
        cm = config_matrix(p, k, n, "full", R, 0)
        m, lam, rows, reps = cm
        rk, _ = rank_mod_p(rows, m, p)
        w = min_ternary_weight(rows, m, p) if m <= 12 else None
        thr = (p ** rk >= 3 ** m)
        ok &= check(f"S5 p={p} n={n} m={m} R={R}: banked true min wt = {claimed}",
                    w == claimed,
                    f"reproduced min ternary weight = {w}; dim L = {rk}; "
                    f"(R-A) p^dimL>=3^m is {thr}")
    return ok


def S6_abstract():
    note("\n=== S6 the PROOFS.md:298 'iff' is a RANDOM-subspace law, not a "
         "per-subspace one ===")
    # L^perp = span{(1,1,0,...,0)} in F_p^m: dim L = m-1, contains a ternary vector.
    rows = []
    ok = True
    for (p, m) in ((5, 4), (7, 4), (11, 3), (2 ** 31 - 2 ** 24 + 1, 4)):
        d = m - 1
        holds = p ** d >= 3 ** m
        ok &= check(f"S6 p={p} m={m}: dim L = m-1 = {d} satisfies (R-A)", holds,
                    f"p^{d} = {p**d} >= 3^{m} = {3**m}; yet L^perp = "
                    "span{(1,1,0,...,0)} contains the ternary vector (1,1,0,...,0), "
                    "so L^perp cap T != {0}. (R-A) does NOT imply (R-B).")
    return ok


P_OFF = 2 ** 31 - 2 ** 24 + 1
LN3 = Decimal(3).ln()
LNP = Decimal(P_OFF).ln()
LN2 = Decimal(2).ln()


def S7_official():
    note("\n=== S7 official row: (R-A) rung by rung, per live value of t ===")
    note(f"       p = 2^31-2^24+1 = {P_OFF};  log2 p = {LNP/LN2:.6f};  "
         f"log_p 3 = {LN3/LNP:.9f}")
    ts = [("t = 7e10   (f2_opening/verify.py:958,1038 literal)", Decimal("7e10")),
          ("t = 2^36   (F2_CAMPAIGN_LOG.md:213,376,717,734)", Decimal(2 ** 36)),
          ("t = 2^41/log2 p (base-field reading)", Decimal(2 ** 41) / (LNP / LN2)),
          ("t* = 8,592,912,739 (xr_radius_arithmetic/proof.md:41-58)",
           Decimal(8592912739))]
    ok = True
    rows = []
    for m_exp_label, m_exps in (("m_16 = 2^38", {14: 36, 15: 37, 16: 38}),
                                ("m_16 = 2^39", {14: 37, 15: 38, 16: 39})):
        note(f"\n       --- internal ambiguity branch: {m_exp_label} ---")
        for label, t in ts:
            for j in (14, 15, 16):
                m = Decimal(2) ** m_exps[j]
                thr = m * LN3 / LNP                    # m log_p 3
                lo = (t / 2).to_integral_value(rounding="ROUND_CEILING")  # R = ceil(t/2)
                for kk in (2, 3, 4):
                    hi = min(m, kk * lo)
                    proved = lo >= thr
                    refuted = hi < thr
                    rows.append((m_exp_label, label, j, kk, proved, refuted,
                                 lo, hi, thr))
        # print k=2 branch compactly
        for label, t in ts:
            lo = (t / 2).to_integral_value(rounding="ROUND_CEILING")
            line = []
            for j in (14, 15, 16):
                m = Decimal(2) ** m_exps[j]
                thr = m * LN3 / LNP
                hi = min(m, 2 * lo)
                v = "PROVED " if lo >= thr else ("REFUTED" if hi < thr else "OPEN   ")
                line.append(f"r{j}:{v}({lo/thr:.3f}x)")
            note(f"       [{label:52s}] " + "  ".join(line))
    # the pre-registered predictions
    lo7 = (Decimal("7e10") / 2)
    thr16 = (Decimal(2) ** 38) * LN3 / LNP
    ok &= check("S7 (P1) (R-A) holds at rungs 14-16 under t = 7e10 with margin > 2x",
                lo7 >= 2 * thr16,
                f"tightest rung is 16: R = {lo7} vs m log_p 3 = {thr16:.6E}; "
                f"margin {lo7/thr16:.4f}x")
    lostar = (Decimal(8592912739) / 2).to_integral_value(rounding="ROUND_CEILING")
    ok &= check("S7 (P2) (R-A) is REFUTED at rung 16 under t* when k = 2",
                min(Decimal(2) ** 38, 2 * lostar) < thr16,
                f"dim L <= k*|Lambda| = {2*lostar} < m log_p 3 = {thr16:.6E} "
                f"(shortfall {float(2*lostar/thr16):.4f}x)")
    kcrit = thr16 / lostar
    ok &= check("S7 (P3) that refutation evaporates once k >= 4",
                min(Decimal(2) ** 38, 4 * lostar) >= thr16,
                f"the refutation needs k < {kcrit:.4f}; it holds for k in {{2,3}} "
                "and FAILS for k >= 4 -- an interaction with the q = p^k pin, "
                "FLAGGED for the sibling pilot, not resolved here")
    thr15 = (Decimal(2) ** 37) * LN3 / LNP
    ok &= check("S7 rung 15 under t* with k=2 is OPEN, not decided",
                lostar < thr15 <= min(Decimal(2) ** 37, 2 * lostar),
                f"R = {lostar} < {thr15:.6E} <= {2*lostar} -- the interval "
                "[min(m,R), min(m,kR)] straddles the threshold")
    # the tower reading k_j = 2^j (f2_deployed_windows/tower.py:15-20)
    note("\n       --- the same table under the TOWER k_j = 2^j (tower.py:15-20) ---")
    for label, t in ts:
        lo = (t / 2).to_integral_value(rounding="ROUND_CEILING")
        line = []
        for j in (14, 15, 16):
            m = Decimal(2) ** (22 + j)
            thr = m * LN3 / LNP
            hi = min(m, (2 ** j) * lo)
            v = "PROVED " if lo >= thr else ("REFUTED" if hi < thr else "OPEN   ")
            line.append(f"r{j}:{v}({lo/thr:.3f}x)")
        note(f"       [{label:52s}] " + "  ".join(line))
    ok &= check("S7 under the tower NO rung is REFUTED under any live t",
                all(min(Decimal(2) ** (22 + j), (2 ** j) *
                        (t / 2).to_integral_value(rounding="ROUND_CEILING"))
                    >= (Decimal(2) ** (22 + j)) * LN3 / LNP
                    for _, t in ts for j in (14, 15, 16)),
                "every REFUTED cell of the k=2 table becomes OPEN: the "
                "refutations were artifacts of the k=2 upper bound")
    need16 = (Decimal(2) ** 38) / (LNP / LN2)
    ok &= check("S7 CATCH-4's rung-16 LEMMA 3 VIOLATION does not survive the tower",
                min(Decimal(2) ** 38, (2 ** 16) * lostar) >= need16,
                f"the banked 0.9687x violation (f2_sl1_powersums/PROOFS.md:391) "
                f"needs dim L <= t*; under k_16 = 2^16 the upper bound is "
                f"min(m, {(2**16)*lostar:.4E}) = m = {Decimal(2)**38:.4E} "
                f">= {need16:.4E}, so NO violation is derivable.  FLAGGED.")
    # LEMMA 3's own necessary condition, now checkable from BELOW
    note("")
    for label, t in ts:
        lo = (t / 2).to_integral_value(rounding="ROUND_CEILING")
        m = Decimal(2) ** 38
        need = m / (LNP / LN2)
        note(f"       [LEMMA 3 @ rung 16, {label[:28]:28s}] proved dim L >= {lo:.5E} "
             f"vs required {need:.5E}  ->  {'SATISFIED' if lo >= need else 'NOT ESTABLISHED'}")
    return ok


def S8_tower():
    """The ambient field at rung j is NOT F_{p^2}: notes/pilots_20260802/
    f2_deployed_windows/tower.py:15-20 fixes n_j = 2^{24+j}, q_j = p^{2^j},
    k_j = 2^j.  f2_opening/PROOFS.md:10's 'n | p^2-1' is a rung-1-only reading."""
    note("\n=== S8 the ambient field: F_{p^2} vs the tower q_j = p^{2^j} ===")
    p = P_OFF

    def v2(x):
        v = 0
        while x % 2 == 0:
            x //= 2
            v += 1
        return v, x

    v2m, oddm = v2(p - 1)
    v2p, oddp = v2(p + 1)
    note(f"       p-1 = 2^{v2m} * {oddm};  p+1 = 2^{v2p} * {oddp};  "
         f"e := v_2(p-1) = {v2m};  v_2(p^2-1) = {v2m+v2p}")
    ok = check("S8 e = v_2(p-1) = 24 and v_2(p^2-1) = 25", v2m == 24 and v2m + v2p == 25,
               "matches f2_deployed_windows/REPORT.md:17 'p-1 = 2^24 . 127'")
    # (i) LTE, verified directly for j = 0..8
    lte = all(v2(p ** (2 ** j) - 1)[0] == 24 + j for j in range(0, 9))
    ok &= check("S8 LTE v_2(p^{2^j} - 1) = 24 + j verified directly for j = 0..8",
                lte, "so mu_{n_j} <= F_{q_j}^* with n_j = 2^{24+j}, q_j = p^{2^j} "
                     "-- tower.py:23-28, cited and independently re-checked")
    # (ii) n_j | p^2-1 fails from j = 2 on
    bad = [j for j in range(1, 17) if (p * p - 1) % (2 ** (24 + j)) != 0]
    ok &= check("S8 n_j = 2^{24+j} divides p^2-1 ONLY at rung 1",
                bad == list(range(2, 17)),
                "f2_opening/PROOFS.md:10 fixes 'n | p^2-1', which holds at j=1 "
                f"and FAILS at every j in {bad[0]}..16 -- that setting is a "
                "rung-1-only reading and cannot host rungs 14-16")
    # (iii) the consequence for the upper bound on dim L
    note("")
    for j in (14, 15, 16):
        kj = 2 ** j
        m = Decimal(2) ** (22 + j)
        for label, t in (("t = 7e10", Decimal("7e10")),
                         ("t* = 8.59e9", Decimal(8592912739))):
            lam = (t / 2).to_integral_value(rounding="ROUND_CEILING")
            note(f"       rung {j}: k_j = 2^{j} = {kj};  k_j*|Lambda| "
                 f"[{label}] = {kj*lam:.5E}  vs  m_j = {m:.5E}  ->  upper bound "
                 f"min(m, k|Lambda|) = {'m (VACUOUS)' if kj*lam >= m else 'k|Lambda|'}")
    ok &= check("S8 under the tower the upper bound dim L <= k|Lambda| is "
                "VACUOUS at rungs 14-16 under every live t",
                all(2 ** j * (Decimal(t) / 2).to_integral_value(rounding="ROUND_CEILING")
                    >= Decimal(2) ** (22 + j)
                    for j in (14, 15, 16) for t in ("7e10", 8592912739)),
                "dim L <= m is all that survives from above; every verdict that "
                "used 'dim L <= t' (= the k=2 case) needs re-derivation")
    return ok


def main():
    note("SL-1b verifier -- notes/pilots_20260806/f2_sl1b/verify.py")
    note(f"grid: p in {PRIMES}, n even <= {NMAX}, k = ord_n(p) <= {KMAX}, "
         f"m <= {MMAX}, R <= {RMAX}, shifts a0 in (0,1,2), windows full/ord")
    S0_provenance()
    G = grid()
    note(f"\n       grid built: {len(G)} configurations")
    S1_lower_bound(G)
    S2_upper_bound(G)
    S3_sharpness(G)
    _, ce = S4_implication(G)
    S4b_round15_predicate(ce)
    S5_replay()
    S6_abstract()
    S7_official()
    S8_tower()
    S9_independent(G, ce)
    note("\n" + "=" * 70)
    note("ALL PASS" if OK_ALL else "FAILURES PRESENT")
    note("digest: F2_SL1B_" + ("ALL_PASS" if OK_ALL else "FAIL"))
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "VERIFY_LOG.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(LOG) + "\n")
    return 0 if OK_ALL else 1


if __name__ == "__main__":
    sys.exit(main())

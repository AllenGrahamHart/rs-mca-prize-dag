#!/usr/bin/env python3
"""The h_r dictionary, forced common support, LB1's forced T_1, and the
p*(d) law together with its NAMED failure.

Source: critical/nodes/rate_half_band_crossing_location/statement.md
        L4420-4505 (Round-36 R-HRLOW addendum, round 36 bank 3).
Model:  notes/pilots_20260811/r36_hrlow/f1_family.py:5-16 (anchor-2
        conventions), reproduced here by DUPLICATION -- nothing is imported.
Banked rows: notes/pilots_20260811/r36_hrlow/f1_results.txt:8-25 (H1),
        :95-171 (H2, including the five named p* failures at :103,120,137,
        154,171).

Two shapes x two fields, as the brief specifies:
  H1: n=20 k=10 R=10 rho=2 r=8 a=12       H2: n=22 k=11 R=11 rho=2 r=9 a=13
  q = 101, 349

Checks
  A. h_r = rho + deg(e_1/e_0) and dim K_0 = r+1-rho-d on every cell x field
     x family (the DICTIONARY);
  B. common support is FORCED: reconstruct e_0, e_1 from two bad slopes and
     their locators, and verify syn(e_0) = y_0, syn(e_1) = y_1;
  C. LB1: d = 1 forces |W| = r+1, an injective ratio, and T_1 = r+1
     structural slopes, each VERIFIED by exhibiting its locator;
  D. the p*(d) law p* = max(rho+d, floor((R+1+d)/2)) -- holds everywhere
     tested EXCEPT the symmetric-T quadratic at H2, where it fails at both
     fields (the named failure), and p* does NOT separate h_r = 3 from
     h_r = 4 (the refuted converse).

Run: tools/ramguard local -- python3 \
  background/nodes/rate_half_far_ca_hr_dictionary_common_support/verify.py
(RAMGUARD_TIMEOUT 300s)
"""

FAIL = []


def bad(m):
    FAIL.append(m)


def inv(a, q):
    return pow(a % q, q - 2, q)


def rref(M, q):
    M = [row[:] for row in M]
    rows = len(M)
    cols = len(M[0]) if rows else 0
    r = 0
    piv = []
    for c in range(cols):
        pr = None
        for i in range(r, rows):
            if M[i][c] % q:
                pr = i
                break
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        iv = inv(M[r][c], q)
        M[r] = [(x * iv) % q for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] % q:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % q for j in range(cols)]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return M, r, piv


def nullspace(M, q, cols):
    if not M:
        return [[1 if i == j else 0 for j in range(cols)] for i in range(cols)]
    Mr, _, piv = rref(M, q)
    free = [c for c in range(cols) if c not in piv]
    out = []
    for f in free:
        v = [0] * cols
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-Mr[i][f]) % q
        out.append(v)
    return out


def solve(A, b, q):
    rows, cols = len(A), len(A[0])
    M = [A[i][:] + [b[i] % q] for i in range(rows)]
    Mr, rk, piv = rref(M, q)
    if piv and piv[-1] == cols:
        return None
    z = [0] * cols
    for i, c in enumerate(piv):
        z[c] = Mr[i][cols] % q
    for i in range(rows):
        if sum(A[i][j] * z[j] for j in range(cols)) % q != b[i] % q:
            return None
    return z


def poly_from_roots(roots, q):
    p = [1]
    for a in roots:
        np_ = [0] * (len(p) + 1)
        for i, c in enumerate(p):
            np_[i + 1] = (np_[i + 1] + c) % q
            np_[i] = (np_[i] - c * a) % q
        p = np_
    return p


def polyeval(p, x, q):
    s = 0
    for c in reversed(p):
        s = (s * x + c) % q
    return s


def make_D(n, q):
    """the symmetric point set {+-1,...,+-n/2}"""
    D = []
    for i in range(1, n // 2 + 1):
        D.append(i % q)
        D.append((-i) % q)
    assert len(set(D)) == n
    return D


def make_v(D, q):
    v = {}
    for x in D:
        pr = 1
        for y in D:
            if y != x:
                pr = (pr * (x - y)) % q
        v[x] = inv(pr, q)
    return v


def syn_of(ev, D, v, q, R):
    y = [0] * R
    for x in D:
        e = ev.get(x, 0) % q
        if not e:
            continue
        c = (e * v[x]) % q
        xp = 1
        for mm in range(R):
            y[mm] = (y[mm] + c * xp) % q
            xp = (xp * x) % q
    return y


def hankel(y, rho, r, q):
    return [[y[i + j] % q for j in range(r + 1)] for i in range(rho)]


def pstar(H, r, q):
    """min i admitting P != 0, deg P <= i, with P*x^j in K_0 for j <= r-i."""
    for i in range(0, r + 1):
        rows = []
        for j in range(0, r - i + 1):
            for h in H:
                rows.append([h[t + j] for t in range(i + 1)])
        if nullspace(rows, q, i + 1):
            return i
    return None


CELLS = [("H1", 20, 10, 2), ("H2", 22, 11, 2)]
FIELDS = [101, 349]


def families(r):
    fams = [("d1-x", r + 1, [0, 1], "one"),
            ("d1-x+1", r + 1, [1, 1], "one"),
            ("d2-inj", r + 1, [0, 0, 1], "one"),
            ("d2-2to1", r + 1, [0, 0, 1], "sym"),
            ("d2-s+1inj", r + 2, [0, 0, 1], "one"),
            ("d2-s+1sym", r + 2, [0, 0, 1], "sym"),
            ("d1-s+1", r + 2, [0, 1], "one"),
            ("ctrl-s=r", r, [0, 1], "one")]
    return fams


def support(kind, s, n, q):
    pos = [i % q for i in range(1, n // 2 + 1)]
    if kind == "one":
        return pos[:s]
    T = []
    i = 1
    while len(T) < s:
        T.append(i % q)
        if len(T) < s:
            T.append((-i) % q)
        i += 1
    return T


rows_checked = 0
dict_ok = 0
pstar_ok = 0
pstar_fail_rows = []
lb1_rows = 0
recon_rows = 0
pstar_by_hr = {}

for tag, n, k, rho in CELLS:
    R = n - k
    r = R - rho
    a = n - r
    if not (4 * rho < R and a > R + 1 and a - 1 > r):
        bad("%s is not razor-faithful" % tag)
    for q in FIELDS:
        D = make_D(n, q)
        v = make_v(D, q)
        for fam, s, Lc, kind in families(r):
            T = support(kind, s, n, q)
            if len(set(T)) != s:
                bad("%s %s: support size" % (tag, fam))
                continue
            e0 = {x: 1 for x in T}
            e1 = {x: polyeval(Lc, x, q) for x in T}
            if any(e1[x] == 0 for x in T):
                continue
            d = max(i for i, c in enumerate(Lc) if c % q)
            y0 = syn_of(e0, D, v, q, R)
            y1 = syn_of(e1, D, v, q, R)
            M0 = hankel(y0, rho, r, q)
            M1 = hankel(y1, rho, r, q)
            H = M0 + M1
            _, hr, _ = rref(H, q)
            dimK0 = r + 1 - hr
            rows_checked += 1

            # ---- A. the dictionary
            if hr != rho + d:
                bad("%s q=%d %s: h_r = %d, dictionary predicts rho+d = %d"
                    % (tag, q, fam, hr, rho + d))
            elif dimK0 != r + 1 - rho - d:
                bad("%s q=%d %s: dim K_0 = %d, predicts %d"
                    % (tag, q, fam, dimK0, r + 1 - rho - d))
            else:
                dict_ok += 1

            # ---- D. the p*(d) law
            ps = pstar(H, r, q)
            pred = max(rho + d, (R + 1 + d) // 2)
            pstar_by_hr.setdefault((tag, q), {})[hr] = ps
            if ps == pred:
                pstar_ok += 1
            else:
                pstar_fail_rows.append((tag, q, fam, ps, pred))

            # ---- C. the structural slopes, each VERIFIED by its locator
            groups = {}
            for t in T:
                groups.setdefault((-inv(e1[t], q)) % q, []).append(t)
            struct = []
            for gsl, Z in sorted(groups.items()):
                supp = [x for x in T if x not in Z]
                if len(supp) > r:
                    continue
                extra = [x for x in D if x not in T][: r - len(supp)]
                S = supp + extra
                if len(S) != r:
                    continue
                sig = poly_from_roots(S, q)
                Hg = [[(M0[i][j] + gsl * M1[i][j]) % q for j in range(r + 1)]
                      for i in range(rho)]
                if all(sum(Hg[i][j] * sig[j] for j in range(r + 1)) % q == 0
                       for i in range(rho)):
                    struct.append((gsl, S))
                else:
                    bad("%s q=%d %s: claimed structural slope %d has no "
                        "annihilating locator" % (tag, q, fam, gsl))
            if d == 1 and s == r + 1:
                # LB1: injective ratio on a support of size exactly r+1
                if len(groups) != r + 1:
                    bad("%s q=%d %s: ratio not injective on T" % (tag, q, fam))
                elif len(struct) != r + 1:
                    bad("%s q=%d %s: T_1 = %d, LB1 forces r+1 = %d"
                        % (tag, q, fam, len(struct), r + 1))
                elif -((-(r + 1)) // d) != r + 1:
                    bad("%s q=%d %s: floor ceil((r+1)/d) != r+1"
                        % (tag, q, fam))
                else:
                    lb1_rows += 1

            # ---- B. common support is forced (reconstruction from 2 slopes)
            if len(struct) >= 2:
                (g1, S1), (g2, S2) = struct[0], struct[1]
                us = []
                okall = True
                for gsl, S in ((g1, S1), (g2, S2)):
                    A = [[(v[x] * pow(x, mm, q)) % q for x in S]
                         for mm in range(R)]
                    b = [(y0[mm] + gsl * y1[mm]) % q for mm in range(R)]
                    z = solve(A, b, q)
                    if z is None:
                        okall = False
                        break
                    us.append({S[i]: z[i] for i in range(len(S))})
                if okall:
                    idg = inv((g2 - g1) % q, q)
                    r0 = {}
                    r1 = {}
                    for x in D:
                        a1 = us[0].get(x, 0)
                        a2 = us[1].get(x, 0)
                        r0[x] = ((g2 * a1 - g1 * a2) * idg) % q
                        r1[x] = ((a2 - a1) * idg) % q
                    if (syn_of(r0, D, v, q, R) != [c % q for c in y0]
                            or syn_of(r1, D, v, q, R) != [c % q for c in y1]):
                        bad("%s q=%d %s: common-support reconstruction failed"
                            % (tag, q, fam))
                    else:
                        Wset = set(x for x in D if r0[x] or r1[x])
                        if not Wset <= set(S1) | set(S2):
                            bad("%s q=%d %s: reconstructed support escapes "
                                "S_1 u S_2" % (tag, q, fam))
                        else:
                            recon_rows += 1

# ---- D (continued): the named failure, and the refuted p* converse
named = [(t, q, f) for (t, q, f, ps, pr) in pstar_fail_rows]
want = [("H2", 101, "d2-2to1"), ("H2", 349, "d2-2to1")]
if sorted(named) != sorted(want):
    bad("p* law failures are %s; the source names exactly the H2 symmetric-T "
        "quadratic (5/5 fields; 2/2 of the fields tested here)" % (named,))
for (t, q, f, ps, pr) in pstar_fail_rows:
    if (ps, pr) != (6, 7):
        bad("named failure at %s q=%d %s is (%d,%d), banked (6,7)"
            % (t, q, f, ps, pr))
for key, byhr in pstar_by_hr.items():
    if key[0] == "H1" and byhr.get(3) is not None and byhr.get(4) is not None:
        if byhr[3] != byhr[4]:
            bad("p* separates h_r = 3 from h_r = 4 at %s -- the source "
                "records the converse as REFUTED (p* = 6 at both)" % (key,))

if FAIL:
    for m in FAIL:
        print("FAIL " + m)
    raise SystemExit(1)
print("HR_DICTIONARY_COMMON_SUPPORT_PASS dictionary h_r=rho+d and "
      "dimK0=r+1-rho-d on %d/%d rows (2 shapes x 2 fields x 8 families); "
      "common-support reconstruction exact on %d rows; LB1 d=1 forces "
      "T_1=r+1 on %d rows; p* law %d/%d with exactly the 2 named H2 "
      "symmetric-T quadratic failures (measured 6 vs predicted 7); p* does "
      "NOT separate h_r=3 from h_r=4"
      % (dict_ok, rows_checked, recon_rows, lb1_rows, pstar_ok, rows_checked))

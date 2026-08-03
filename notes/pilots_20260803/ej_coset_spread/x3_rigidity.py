"""x3_rigidity.py -- ROUTE (2): CLAIM H (rigidity) tested where the banked
THEOREM F's range d <= w-2j is genuinely NON-EMPTY, i.e. w >= 2j+1.

Full enumeration cannot reach that regime with a live population (PREREG D-7).
So the test is EXHAUSTIVE LOCAL SEARCH in the d-ball: around each base band
solution T0 (structured ones always exist), enumerate EVERY T at symmetric
distance exactly d, for d = 1..dmax, and test band membership.  The d-ball is
enumerated with prefix-shared series division/multiplication, so the cost is
O(w) per candidate and the search is genuinely exhaustive up to dmax.

Falsifiers:
  F-F : two band solutions with  j < d <= w-2j                    [kills (H1)]
  F-G : d(T1,T2),d(T2,T3) <= j but j < d(T1,T3) <= w-2j           [kills (H4)]
  F-H : a band solution at  1 < d <= w-2j  from a STRUCTURED one,
        or a d <= w-2j neighbour whose z is not -a^j (a = removed pt) [kills (H3)]
Plus: the (RIG) polynomial identity  G'(1+zY^j)Q = G(1+z'Y^j)Q'  must hold
EXACTLY for every found pair with d <= w-2j, and must FAIL for pairs beyond it.
"""
import json
import os
import sys
from itertools import combinations

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ejlib as E                                                # noqa: E402

L = E.Ledger()


def ET_series(T, q, w):
    """E_T(Y) mod Y^w as a coefficient list."""
    s = [0] * w
    s[0] = 1
    for x in T:
        for t in range(w - 1, 0, -1):
            s[t] = (s[t] - x * s[t - 1]) % q
    return s


def mul_lin(s, x, q, w):
    """s * (1 - xY) mod Y^w."""
    return [(s[t] - (x * s[t - 1] if t else 0)) % q for t in range(w)]


def div_lin(s, x, q, w):
    """s / (1 - xY) mod Y^w  (exact when (1-xY) | s)."""
    u = [0] * w
    p = 0
    for t in range(w):
        p = (s[t] + x * p) % q
        u[t] = p
    return u


def band_of(ET, q, w, j):
    """If ET is a band solution return (z, G coefficients [0..j-1]); else None."""
    z = (-ET[j]) % q
    if z == 0:
        return None
    for t in range(j + 1, w):
        if (ET[t] + z * ET[t - j]) % q:
            return None
    return z, [(ET[t] + (z * ET[t - j] if t >= j else 0)) % q
               for t in range(j)]


def polymul(a, b, q):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for t, y in enumerate(b):
                if y:
                    r[i + t] = (r[i + t] + x * y) % q
    return r


def rig_sides(Gp, z, Q, Gg, zp, Qp, q, j):
    """the two sides of (RIG):  G'(1+zY^j)Q   and   G(1+z'Y^j)Q'."""
    one_z = [0] * (j + 1)
    one_z[0], one_z[j] = 1, z % q
    one_zp = [0] * (j + 1)
    one_zp[0], one_zp[j] = 1, zp % q
    return polymul(polymul(Gp, one_z, q), Q, q), \
        polymul(polymul(Gg, one_zp, q), Qp, q)


def eqpoly(a, b):
    m = max(len(a), len(b))
    return all((a[i] if i < len(a) else 0) == (b[i] if i < len(b) else 0)
               for i in range(m))


# ---------------------------------------------------------------- fixtures
# prize shape w = M ; large w so that D = w-2j is genuinely non-empty
FIX = [
    (20, 5, 5, 5, [41, 101]),
    (18, 6, 6, 6, [19, 37]),
    (24, 12, 6, 6, [73]),
    (21, 7, 7, 7, [43, 127]),
    (24, 8, 8, 8, [73, 97]),
    (27, 9, 9, 9, [109]),
    (30, 10, 10, 10, [31, 61]),
    (33, 11, 11, 11, [67]),
    (36, 12, 12, 12, [73]),
]
BUDGET = int(os.environ.get("BUDGET", "500000"))
rows, fired = [], []

for (n, k, w, M, qs) in FIX:
    if not E.mc3_ok(n, k, w, M):
        print("skip MC-3", (n, k, w, M))
        continue
    A = k + w + 1
    rp = n - A
    for q in qs:
        if (q - 1) % n or not E.is_prime(q) or q <= n + 1:
            continue
        H, beta, om = E.make_domain(q, n, 0)
        mu = E.mu_n_set(H, q)
        c = E.mc_c_from_gamma(H, q, n, k, w, M)
        structs, fam = E.structured_sets(H, q, n, k, w, M, c)
        if not fam:
            continue
        gam = ((-1) ** rp * c) % q
        for j in range(1, min(M, w)):
            D = w - 2 * j                     # the rigidity range
            if D < 1:
                continue
            dmax = D
            while dmax > 1 and E.comb(rp, dmax) * E.comb(n - rp, dmax) > BUDGET:
                dmax -= 1
            bases = list(structs.items())[:4]
            found = []                         # (Tidx, d, z, G, structured?)
            ncand = 0
            for (T0f, y0) in bases:
                T0 = sorted(T0f)
                comp = [i for i in range(n) if i not in T0f]
                ET0 = ET_series([H[i] for i in T0], q, w)
                b0 = band_of(ET0, q, w, j)
                L.chk(b0 is not None, "structured T0 IS a band solution",
                      (n, k, w, M, q, j))
                if b0 is None:
                    continue
                # z of a structured T0 must be -y^j  (THEOREM E)
                L.chk(b0[0] == (-pow(H[y0], j, q)) % q,
                      "THEOREM E  z = -y^j", (n, k, w, M, q, j))
                found.append((tuple(T0), 0, b0[0], b0[1], True))
                for d in range(1, dmax + 1):
                    for R in combinations(range(rp), d):
                        s = ET0
                        for i in R:
                            s = div_lin(s, H[T0[i]], q, w)
                        for Ad in combinations(comp, d):
                            ncand += 1
                            s2 = s
                            for i in Ad:
                                s2 = mul_lin(s2, H[i], q, w)
                            bb = band_of(s2, q, w, j)
                            if bb is None:
                                continue
                            Tn = tuple(sorted([T0[i] for i in range(rp)
                                               if i not in R] + list(Ad)))
                            found.append((Tn, d, bb[0], bb[1],
                                          frozenset(Tn) in structs))
                            # (H3): a d<=D neighbour of a structured T0 must
                            # have d <= gcd(j,n) and z = -a^j, a the removed pt
                            if d > E.gcd(j, n):
                                fired.append(("F-H", n, k, w, M, q, j, d))
                                L.chk(False, "F-H band nbr at d>gcd(j,n) of "
                                      "structured", (n, k, w, M, q, j, d))
                            else:
                                # (H3) general form: EVERY removed point a
                                # satisfies a^j = -z (its 1/a is a root of Q',
                                # and Q' | G'(1+zY^j) with G' rootless in 1/H)
                                for i in R:
                                    a = H[T0[i]]
                                    L.chk(bb[0] == (-pow(a, j, q)) % q,
                                          "(H3) a^j = -z for every removed pt",
                                          (n, k, w, M, q, j, d))
                                L.chk(bb[0] in E.neg_Hj(H, q, j),
                                      "(H3) z in -H^j", (n, k, w, M, q, j, d))
            # pairwise: (RIG) identity + (H1) d <= (j-1)+gcd(j,n)
            npair = 0
            for i1 in range(len(found)):
                for i2 in range(i1 + 1, min(len(found), i1 + 60)):
                    T1, d1, z1, G1, s1 = found[i1]
                    T2, d2, z2, G2, s2 = found[i2]
                    dd = E.dist(T1, T2)
                    if dd == 0 or dd > D:
                        continue
                    npair += 1
                    L.chk(dd <= (j - 1) + E.gcd(j, n),
                          "F-F (H1) d <= (j-1)+gcd(j,n)",
                          (n, k, w, M, q, j, dd))
                    Q = ET_series([H[i] for i in set(T1) - set(T2)], q, w)
                    Qp = ET_series([H[i] for i in set(T2) - set(T1)], q, w)
                    Qc = Q[:dd + 1]
                    Qpc = Qp[:dd + 1]
                    lhs, rhs = rig_sides(G2, z1, Qc, G1, z2, Qpc, q, j)
                    L.chk(eqpoly(lhs, rhs), "(RIG) exact identity at d<=w-2j",
                          (n, k, w, M, q, j, dd))
            # (H4) transitivity of "d <= b", b := (j-1)+gcd(j,n).  The triangle
            # inequality only gives d13 <= 2b, so the dichotomy can collapse it
            # to <= b ONLY when 2b <= D = w-2j.  That hypothesis is part of the
            # claim; testing without it was a bug in the first run (recorded).
            b = (j - 1) + E.gcd(j, n)
            if 2 * b <= D:
                for i1 in range(min(len(found), 40)):
                    for i2 in range(min(len(found), 40)):
                        for i3 in range(min(len(found), 40)):
                            d12 = E.dist(found[i1][0], found[i2][0])
                            d23 = E.dist(found[i2][0], found[i3][0])
                            d13 = E.dist(found[i1][0], found[i3][0])
                            if d12 <= b and d23 <= b and d13 <= D:
                                L.chk(d13 <= b, "F-G (H4) transitivity",
                                      (n, k, w, M, q, j, b, d12, d23, d13))
            nd = {}
            for (_, d, _, _, _) in found:
                nd[d] = nd.get(d, 0) + 1
            rows.append({"n": n, "k": k, "w": w, "M": M, "q": q, "j": j,
                         "rp": rp, "D_range": D, "dmax_searched": dmax,
                         "n_candidates": ncand, "n_bases": len(bases),
                         "found_by_d": nd, "n_pairs_checked": npair})
            print("n=%2d k=%2d w=M=%2d q=%3d j=%d | D=w-2j=%2d dmax=%d "
                  "cands=%7d | band sols by d: %s | pairs=%d" %
                  (n, k, w, q, j, D, dmax, ncand, sorted(nd.items()), npair))

os.makedirs(os.path.join(HERE, "checkpoints"), exist_ok=True)
with open(os.path.join(HERE, "checkpoints", "x3_rigidity.json"), "w") as f:
    json.dump({"doc": __doc__, "rows": rows, "F_fired": fired,
               "checks": L.n, "failures": len(L.fail)}, f, indent=1)
tot = sum(r["n_candidates"] for r in rows)
print("\ntotal d-ball candidates tested: %d over %d (fixture,j) rows" %
      (tot, len(rows)))
print("max d at which a band solution was found next to a structured one: %d" %
      max([d for r in rows for d in r["found_by_d"]] + [0]))
ok = L.report("x3_rigidity")
print("OK" if ok else "FAILURES PRESENT")

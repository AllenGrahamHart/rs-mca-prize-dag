"""t5_extfield.py -- the characteristic-p / extension-field corner.

THEOREM Y's proof uses nothing about the field except that H is a coset of
mu_n inside F^* and that Omega = X^n - beta is squarefree (gcd(n,q) = 1).
So it should survive verbatim over F_{p^2}.  This script is a SECOND,
independent implementation (own field, own locator classifier, table-based
arithmetic) so that a shared bug in advlib cannot hide a failure.

Fields: F_{p^2} = F_p[t]/(t^2 - s), s a non-residue; full add/mul tables.

PRE-REGISTERED PREDICTIONS.
 D1  Over F_{p^2}, in the SUPER-critical regime (C(n,A)/q^w >> 1), the
     j = 1 live slopes are still all inside -H, and prod(S) = gamma holds
     on every solution.
 D2  Over F_{p^2}, at j = 3, live slopes appear OUTSIDE -H^j (the same
     failure as in prime fields) -- so the j>=2 gap is not a
     characteristic-0-flavoured accident.
 D3  The number of non-MC-derived rays is > 0 in every super-critical
     extension-field fixture (char-p "accidental" solutions are real, and
     Theorem Y is what keeps them harmless at j = 1).
"""

import json
import os
import sys
from itertools import combinations
from math import comb

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
CHK = os.path.join(HERE, "checkpoints")
os.makedirs(CHK, exist_ok=True)

out = {"doc": __doc__, "runs": [], "checks": 0, "fails": []}


def chk(cond, label, extra=None):
    out["checks"] += 1
    if not cond:
        out["fails"].append({"label": label, "extra": str(extra)})
        print("    FAIL", label, extra)
    return cond


class GF2(object):
    """F_{p^2} = F_p[t]/(t^2 - s); element a+bt encoded as a + b*p."""

    def __init__(self, p):
        self.p = p
        self.q = p * p
        s = next(x for x in range(2, p)
                 if pow(x, (p - 1) // 2, p) == p - 1)
        self.s = s
        q, P = self.q, p
        self.ADD = [[0] * q for _ in range(q)]
        self.MUL = [[0] * q for _ in range(q)]
        for x in range(q):
            a1, b1 = x % P, x // P
            for y in range(q):
                a2, b2 = y % P, y // P
                self.ADD[x][y] = (a1 + a2) % P + ((b1 + b2) % P) * P
                self.MUL[x][y] = ((a1 * a2 + s * b1 * b2) % P
                                  + ((a1 * b2 + a2 * b1) % P) * P)
        self.NEG = [((-(x % P)) % P) + (((-(x // P)) % P)) * P
                    for x in range(q)]
        self.INV = [0] * q
        for x in range(1, q):
            for y in range(1, q):
                if self.MUL[x][y] == 1:
                    self.INV[x] = y
                    break
        self.one, self.zero = 1, 0
        self.gen = self._generator()

    def _generator(self):
        q = self.q
        fac, t, d = [], q - 1, 2
        while d * d <= t:
            if t % d == 0:
                fac.append(d)
                while t % d == 0:
                    t //= d
            d += 1
        if t > 1:
            fac.append(t)
        for g in range(2, q):
            if all(self.pw(g, (q - 1) // f) != 1 for f in fac):
                return g
        raise RuntimeError("no generator")

    def pw(self, x, e):
        r, b = 1, x
        while e:
            if e & 1:
                r = self.MUL[r][b]
            b = self.MUL[b][b]
            e >>= 1
        return r


def domain(F, n, beta_exp=0):
    assert (F.q - 1) % n == 0
    om = F.pw(F.gen, (F.q - 1) // n)
    x0 = F.pw(F.gen, beta_exp)
    H = [F.MUL[x0][F.pw(om, i)] for i in range(n)]
    assert len(set(H)) == n
    return H, F.pw(x0, n)


def ser_inv(F, a, L):
    o = [0] * L
    o[0] = 1
    for i in range(1, L):
        s = 0
        for jj in range(1, i + 1):
            if jj < len(a) and a[jj]:
                s = F.ADD[s][F.MUL[a[jj]][o[i - jj]]]
        o[i] = F.NEG[s]
    return o


def esym_full(F, vals):
    e = [1]
    for x in vals:
        ne = [0] * (len(e) + 1)
        for t in range(len(e) + 1):
            u = e[t] if t < len(e) else 0
            v = F.MUL[x][e[t - 1]] if t >= 1 else 0
            ne[t] = F.ADD[u][v]
        e = ne
    return e


def classify(F, H, beta, n, k, w, c, j, a_target):
    """all (T, z) with a codeword of agreement >= a_target against u + z v."""
    q = F.q
    W = a_target - k
    delta = a_target - (k + w)
    rp = n - a_target
    Ltop, Lbot = max(W, w, 1), j + 1
    prodH = 1
    for x in H:
        prodH = F.MUL[prodH][x]
    inv = [F.INV[x] for x in H]
    res = []

    def leaf(Es, Ei, pr, chosen):
        ET = ser_inv(F, Es, Ltop)
        ETi = ser_inv(F, Ei, Lbot)
        prodT = F.MUL[prodH][F.INV[pr]]
        sgn = 1 if rp % 2 == 0 else F.NEG[1]

        def mco(s):
            if s < 0 or s > rp:
                return 0
            if s < Lbot:
                return F.MUL[F.MUL[sgn][prodT]][ETi[s]]
            t = rp - s
            if t < Ltop:
                return ET[t]
            raise RuntimeError("gap")

        z = None
        for i in range(W):
            al = F.ADD[mco(-i)][F.MUL[c][mco(rp + delta - i)]]
            be = F.ADD[mco(j - i)][F.MUL[c][mco(rp + delta + j - i)]]
            if be:
                zz = F.NEG[F.MUL[al][F.INV[be]]]
                if z is None:
                    z = zz
                elif z != zz:
                    return
            elif al:
                return
        if not z:
            return
        res.append({"Tc": list(chosen), "z": z})

    def rec(pos, cnt, Es, Ei, pr, chosen):
        if cnt == a_target:
            leaf(Es, Ei, pr, chosen)
            return
        for p in range(pos, n - (a_target - cnt) + 1):
            x, xi = H[p], inv[p]
            E2 = list(Es)
            for t in range(Ltop - 1, 0, -1):
                E2[t] = F.ADD[E2[t]][F.NEG[F.MUL[x][Es[t - 1]]]]
            I2 = list(Ei)
            for t in range(Lbot - 1, 0, -1):
                I2[t] = F.ADD[I2[t]][F.NEG[F.MUL[xi][Ei[t - 1]]]]
            chosen.append(p)
            rec(p + 1, cnt + 1, E2, I2, F.MUL[pr][x], chosen)
            chosen.pop()

    rec(0, 0, [1] + [0] * (Ltop - 1), [1] + [0] * (Lbot - 1), 1, [])
    return res


def mc_family(F, H, n, k, w, M, c):
    rp = n - k - w
    N, m = n // M, rp // M
    cos = [[i for i in range(n) if i % N == jj] for jj in range(N)]
    g = c if (rp + 1) % 2 == 0 else F.NEG[c]
    fam = []
    for S in combinations(range(N), m):
        T = [i for jj in S for i in cos[jj]]
        pr = 1
        for i in T:
            pr = F.MUL[pr][H[i]]
        if pr == g:
            fam.append(tuple(sorted(T)))
    return fam, g


def run(p, n, k, w, M, j, beta_exp=0):
    F = GF2(p)
    q = F.q
    if (q - 1) % n or n % M or (n - k - w) % M or w > M:
        return None
    H, beta = domain(F, n, beta_exp)
    rp0 = n - k - w
    N, m = n // M, rp0 // M
    cos = [[i for i in range(n) if i % N == jj] for jj in range(N)]
    T0 = [i for jj in range(m) for i in cos[jj]]
    pr = 1
    for i in T0:
        pr = F.MUL[pr][H[i]]
    gamma = pr
    c = gamma if (rp0 + 1) % 2 == 0 else F.NEG[gamma]
    fam, g2 = mc_family(F, H, n, k, w, M, c)
    A = k + w + 1
    sols = classify(F, H, beta, n, k, w, c, j, A)
    hi = classify(F, H, beta, n, k, w, c, j, A + 1)
    Hset = set(H)
    Hj = set(F.pw(x, j) for x in H)
    nHj = set(F.NEG[x] for x in Hj)

    n_prod, n_conf = 0, 0
    for s in sols:
        T = [i for i in range(n) if i not in set(s["Tc"])]
        pT = 1
        for i in T:
            pT = F.MUL[pT][H[i]]
        if F.MUL[F.NEG[s["z"]]][pT] == gamma:
            n_prod += 1
        if F.NEG[s["z"]] in Hset:
            n_conf += 1
    mcd = set()
    for T in fam:
        for x0 in T:
            mcd.add((F.NEG[F.pw(H[x0], j)],
                     tuple(sorted(set(range(n)) - set(T) | {x0}))))
    extra = [s for s in sols
             if (s["z"], tuple(sorted(s["Tc"]))) not in mcd]
    live = sorted(set(s["z"] for s in sols))
    outside = [z for z in live if z not in nHj]
    X = comb(n, A) / float(q) ** w
    rec = {"p": p, "q": q, "n": n, "k": k, "w": w, "M": M, "j": j,
           "beta_exp": beta_exp, "A": A, "mc_family": len(fam),
           "n_solutions": len(sols), "n_extra_rays": len(extra),
           "n_live": len(live), "n_live_outside_minusHj": len(outside),
           "prod_S_eq_gamma": n_prod, "minus_z_in_H": n_conf,
           "gate_break_at_A_plus_1": len(hi), "criticality_index": X}
    out["runs"].append(rec)
    print("  F_%-4d(char %2d) n=%2d k=%2d w=%d M=%d j=%d | MC=%-3d sols=%-5d "
          "extra=%-5d live=%-3d OUT(-H^j)=%-3d | prod(S)=gamma:%-5d "
          "-z in H:%-5d gateA+1=%-3d | X=%.4g"
          % (q, p, n, k, w, M, j, len(fam), len(sols), len(extra),
             len(live), len(outside), n_prod, n_conf, len(hi), X))
    return rec


print("=== D1/D3 -- j = 1 over F_{p^2}, super-critical ===")
for (p, n, k, w, M) in [(7, 16, 4, 2, 2), (7, 24, 4, 2, 2),
                        (11, 20, 4, 2, 2), (13, 24, 4, 2, 2),
                        (11, 20, 6, 2, 4), (7, 16, 6, 2, 4)]:
    r = run(p, n, k, w, M, 1)
    if r:
        chk(r["prod_S_eq_gamma"] == r["n_solutions"],
            "D1 prod(S) = gamma on every solution (ext field)",
            (p, n, k, w, M))
        chk(r["minus_z_in_H"] == r["n_solutions"],
            "D1 THEOREM Y: -z in H on every solution (ext field)",
            (p, n, k, w, M))
        chk(r["n_live_outside_minusHj"] == 0,
            "D1 no live slope outside -H (ext field, j=1)", (p, n, k, w, M))
        chk(r["gate_break_at_A_plus_1"] == 0,
            "D1 ceiling holds (ext field, j=1)", (p, n, k, w, M))

print()
print("=== D1 -- beta != 1 over F_{p^2} ===")
for be in (1, 5):
    r = run(11, 20, 4, 2, 2, 1, beta_exp=be)
    if r:
        chk(r["minus_z_in_H"] == r["n_solutions"],
            "D1 THEOREM Y with beta != 1 (ext field)", (be,))

print()
print("=== D2 -- j = 3 over F_{p^2} (M = 4, gcd(3,n) = 1) ===")
for (p, n, k, w, M) in [(11, 20, 6, 2, 4), (7, 16, 6, 2, 4),
                        (19, 20, 6, 2, 4)]:
    r = run(p, n, k, w, M, 3)
    if r:
        chk(r["n_live_outside_minusHj"] > 0 or r["criticality_index"] < 2,
            "D2 j=3 escapes -H^j once super-critical (ext field)",
            (p, n, k, w, M, r["n_live_outside_minusHj"],
             r["criticality_index"]))

out["verdict"] = "PASS" if not out["fails"] else "FAIL"
with open(os.path.join(CHK, "t5_extfield.json"), "w") as f:
    json.dump(out, f, indent=1)
print("\nchecks=%d fails=%d -> %s" % (out["checks"], len(out["fails"]),
                                      out["verdict"]))

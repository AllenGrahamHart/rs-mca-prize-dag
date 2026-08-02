"""t6_certify.py -- a stand-alone, theory-free CERTIFICATE for the headline
counterexample, using nothing but Lagrange interpolation.

No locator theory, no series inversion, no classifier: for every k-subset S
of H we interpolate u and v on S, which yields every codeword of agreement
>= k against every member of the pencil (because interp_S(u+zv) =
interp_S(u) + z interp_S(v)).  From that we recompute, from scratch:

  * the maximum agreement of every slope in P^1(F_q)  -> the tangent gate,
  * the joint-explanation maximum                     -> genericity,
  * Gamma = {slopes of maximum agreement exactly A},
  * Gamma \\ (-H^j)                                    -> the refutation,
  * the MC family and its forced slopes               -> the baseline.

INSTANCE (headline): n=20, k=6, w=2, M=4, j=3, q=41, beta=1.
CONTROL   (same shape, j=1): must show Gamma = -H exactly (Theorem Y).
"""

import json
import os
import sys
from itertools import combinations

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
CHK = os.path.join(HERE, "checkpoints")
os.makedirs(CHK, exist_ok=True)
out = {"doc": __doc__, "instances": [], "checks": 0, "fails": []}


def chk(cond, label, extra=None):
    out["checks"] += 1
    if not cond:
        out["fails"].append({"label": label, "extra": str(extra)})
        print("    FAIL", label, extra)
    return cond


def ev(c, x, q):
    a = 0
    for t in reversed(c):
        a = (a * x + t) % q
    return a


def lagrange(xs, ys, q):
    kk = len(xs)
    res = [0] * kk
    for i in range(kk):
        num, den = [1], 1
        for jj in range(kk):
            if jj == i:
                continue
            nn = [0] * (len(num) + 1)
            for t, cc in enumerate(num):
                nn[t + 1] = (nn[t + 1] + cc) % q
                nn[t] = (nn[t] - cc * xs[jj]) % q
            num = nn
            den = (den * (xs[i] - xs[jj])) % q
        s = (ys[i] * pow(den, q - 2, q)) % q
        for t in range(kk):
            res[t] = (res[t] + s * num[t]) % q
    return res


def certify(n, k, w, M, q, j, beta_exp=0):
    # ---- field, domain, word: all built here from scratch
    def proot(qq):
        t, fac, d = qq - 1, [], 2
        while d * d <= t:
            if t % d == 0:
                fac.append(d)
                while t % d == 0:
                    t //= d
            d += 1
        if t > 1:
            fac.append(t)
        for g in range(2, qq):
            if all(pow(g, (qq - 1) // f, qq) != 1 for f in fac):
                return g
    g = proot(q)
    om = pow(g, (q - 1) // n, q)
    x0 = pow(g, beta_exp, q)
    H = [(x0 * pow(om, i, q)) % q for i in range(n)]
    rp = n - k - w
    N, m = n // M, rp // M
    cos = [[i for i in range(n) if i % N == jj] for jj in range(N)]
    T0 = [i for jj in range(m) for i in cos[jj]]
    pr = 1
    for i in T0:
        pr = (pr * H[i]) % q
    gamma = pr
    c = (((-1) ** (rp + 1)) * gamma) % q
    uv = [(pow(x, n - 1, q) + c * pow(x, k + w - 1, q)) % q for x in H]
    vv = [(uv[i] * pow(pow(H[i], j, q), q - 2, q)) % q for i in range(n)]
    A = k + w + 1

    fam = []
    for S in combinations(range(N), m):
        T = [i for jj in S for i in cos[jj]]
        p2 = 1
        for i in T:
            p2 = (p2 * H[i]) % q
        if p2 == gamma:
            fam.append(tuple(sorted(T)))

    # ---- exhaustive: max agreement of EVERY slope, from scratch
    INF = "inf"
    maxa = dict((z, 0) for z in list(range(q)) + [INF])
    jointmax = 0
    seen = set()
    for S in combinations(range(n), k):
        xs = [H[i] for i in S]
        f = tuple(lagrange(xs, [uv[i] for i in S], q))
        gg = tuple(lagrange(xs, [vv[i] for i in S], q))
        if (f, gg) in seen:
            continue
        seen.add((f, gg))
        fa = [ev(f, H[i], q) for i in range(n)]
        ga = [ev(gg, H[i], q) for i in range(n)]
        nz, byz = 0, {}
        for i in range(n):
            a = (uv[i] - fa[i]) % q
            b = (vv[i] - ga[i]) % q
            if a == 0 and b == 0:
                nz += 1
            elif b == 0:
                byz[INF] = byz.get(INF, 0) + 1
            else:
                zz = (-a * pow(b, q - 2, q)) % q
                byz[zz] = byz.get(zz, 0) + 1
        jointmax = max(jointmax, nz)
        for z in maxa:
            maxa[z] = max(maxa[z], nz + byz.get(z, 0))

    Gamma = sorted([z for z, a in maxa.items() if a == A], key=str)
    over = {z: a for z, a in maxa.items() if a > A}
    nHj = set((-pow(x, j, q)) % q for x in H)
    outside = [z for z in Gamma if z == INF or z not in nHj]
    forced = sorted(set((-pow(H[i], j, q)) % q for T in fam for i in T))

    rec = {"n": n, "k": k, "w": w, "M": M, "q": q, "j": j,
           "beta_exp": beta_exp, "A": A, "c": c, "gamma": gamma,
           "H": H, "mc_family": [list(t) for t in fam],
           "n_distinct_codeword_pairs": len(seen),
           "joint_explanation_max": jointmax,
           "max_agreement_over_pencil": max(maxa.values()),
           "tangent_gate_ok": not over,
           "slopes_over_A": {str(z): a for z, a in over.items()},
           "Gamma_size": len(Gamma), "Gamma": [str(z) for z in Gamma],
           "minus_H_j": sorted(nHj),
           "MC_forced_slopes": forced,
           "Gamma_outside_minus_H_j": [str(z) for z in outside],
           "n_outside": len(outside), "Gamma_over_n": len(Gamma) / float(n)}
    out["instances"].append(rec)
    print("  n=%d k=%d w=%d M=%d q=%d j=%d beta_exp=%d" %
          (n, k, w, M, q, j, beta_exp))
    print("    distinct codeword pairs     : %d" % len(seen))
    print("    joint-explanation max       : %d   (A-1 = %d)"
          % (jointmax, A - 1))
    print("    max agreement over P^1      : %d   (A = %d)  gate %s"
          % (max(maxa.values()), A, "OK" if not over else "BROKEN"))
    print("    |Gamma| (max agreement = A) : %d   = %.2f n"
          % (len(Gamma), len(Gamma) / float(n)))
    print("    |-H^j|                      : %d" % len(nHj))
    print("    MC-forced slopes            : %d  %s"
          % (len(forced), forced if len(forced) <= 24 else ""))
    print("    Gamma OUTSIDE -H^j          : %d  %s"
          % (len(outside), outside if len(outside) <= 24 else ""))
    return rec


print("=== CONTROL (j=1): Theorem Y says Gamma = -H exactly ===")
r1 = certify(20, 6, 2, 4, 41, 1)
chk(r1["n_outside"] == 0, "control j=1: no live slope outside -H")
chk(r1["tangent_gate_ok"], "control j=1: tangent gate intact")
chk(r1["joint_explanation_max"] == r1["A"] - 1,
    "control j=1: joint explanation max = A-1")
chk(r1["Gamma_size"] == 20, "control j=1: |Gamma| = n")

print()
print("=== HEADLINE COUNTEREXAMPLE (j=3) ===")
r3 = certify(20, 6, 2, 4, 41, 3)
chk(r3["tangent_gate_ok"], "counterexample: tangent gate INTACT")
chk(r3["joint_explanation_max"] == r3["A"] - 1,
    "counterexample: joint explanation max = A-1 (generic branch)")
chk(r3["n_outside"] > 0, "counterexample: live slopes OUTSIDE -H^j exist")
chk(r3["Gamma_size"] > 20, "counterexample: |Gamma| EXCEEDS n",
    r3["Gamma_size"])
chk(set(r3["MC_forced_slopes"]) <= set(int(z) for z in r3["Gamma"]),
    "counterexample: the MC-forced slopes are still all live "
    "(MC-7 unaffected)")

print()
print("=== second counterexample, larger q (j=3, q=101) ===")
r4 = certify(20, 6, 2, 4, 101, 3)
chk(r4["tangent_gate_ok"] and r4["n_outside"] > 0 and r4["Gamma_size"] > 20,
    "second counterexample stands", (r4["Gamma_size"], r4["n_outside"]))

out["verdict"] = "CERTIFIED" if not out["fails"] else "FAIL"
with open(os.path.join(CHK, "t6_certificate.json"), "w") as f:
    json.dump(out, f, indent=1)
print("\nchecks=%d fails=%d -> %s" % (out["checks"], len(out["fails"]),
                                      out["verdict"]))

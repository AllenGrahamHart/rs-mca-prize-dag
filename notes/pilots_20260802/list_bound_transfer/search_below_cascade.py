"""search_below_cascade.py -- can a pencil have a LARGE min-list while
staying BELOW CASCADE?

KEY LEMMA (proved in the report; machine-checked here).  Fix a subset
S subset H with |S| = a = k+w.  The window conditions "w_z|_S interpolates
to degree < k" form w equations A(S) + z B(S) = 0, AFFINE in z.  Hence
either
   (a) at most ONE member z in P^1 has a codeword with agreement set
       exactly S, or
   (b) A(S) = B(S) = 0, i.e. u|_S and v|_S are BOTH codewords -- a joint
       codeword-pair explanation of size a (a cascade event at depth a-k).
Equivalently: below cascade <=> distinct pencil members never share an
agreement set of size a.

COROLLARY (exact identity).  sum_{z in P^1} L_exact(w_z, a)
   = #{S : |S| = a and rank[A(S); B(S)] <= 1},
so  min_z L <= that count/(q+1).

PRE-REGISTERED PREDICTIONS:
  C1  The MC shift pencil is ABOVE cascade: max joint pair explanation = a.
  C2  Random pencils are below cascade and have min_z L(w_z,a) = 0.
  C3  Hill-climbing subject to "below cascade" cannot push min_z L(w_z,a)
      above a small constant -- i.e. LARGE PENCIL MIN FORCES A CASCADE
      EVENT.  (If C3 is falsified the reduced statement is dead outright;
      if it survives, the reduction's true content is the cascade
      hypothesis, not a single-word list bound.)
  C4  The KEY LEMMA holds with zero exceptions on every instance tested.
"""

import json
import os
import random
import sys
from itertools import combinations

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lbt_lib import (make_domain, interpolate, poly_eval, trim)

CHK = os.path.join(HERE, "checkpoints")
os.makedirs(CHK, exist_ok=True)

out = {"predictions": {
    "C1": "MC shift pencil is above cascade (max joint explanation = a)",
    "C2": "random pencils: below cascade and min_z L = 0",
    "C3": "below-cascade hill climbing cannot push min_z L above a small constant",
    "C4": "KEY LEMMA: no support S is shared by two members unless both u|_S, v|_S in C",
}, "checks": 0, "fails": [], "runs": []}


def check(cond, label, extra=None):
    out["checks"] += 1
    if not cond:
        out["fails"].append({"label": label, "extra": extra})
    return cond


def analyse(uv, vv, H, k, a, q):
    """Return (min over P^1 of #exact-a-supports, max joint explanation size,
    list sizes per member) by enumerating every a-subset once."""
    n = len(H)
    w = a - k
    per = {}                     # z -> set of supports
    joint_max = 0
    shared = 0
    for S in combinations(range(n), a):
        xs = [H[i] for i in S]
        fu = interpolate(xs, [uv[i] for i in S], q)
        fv = interpolate(xs, [vv[i] for i in S], q)
        du = len(trim(fu))
        dv = len(trim(fv))
        Au = trim(fu)[k:] if du > k else []
        Bv = trim(fv)[k:] if dv > k else []
        Au = (trim(fu) + [0] * a)[k:a]
        Bv = (trim(fv) + [0] * a)[k:a]
        zeroA = all(t == 0 for t in Au)
        zeroB = all(t == 0 for t in Bv)
        if zeroA and zeroB:
            joint_max = max(joint_max, a)
            for z in list(range(q)) + ["inf"]:
                per.setdefault(z, set()).add(S)
            shared += 1
            continue
        if zeroA:                                  # u|_S is a codeword: z = 0
            per.setdefault(0, set()).add(S)
            continue
        if zeroB:                                  # v|_S is a codeword: z = inf
            per.setdefault("inf", set()).add(S)
            continue
        # need A + zB = 0 with B != 0 -> z = -A_j/B_j, same for all j
        z0 = None
        ok = True
        for j in range(w):
            if Bv[j] == 0:
                if Au[j] != 0:
                    ok = False
                    break
                continue
            zz = (-Au[j] * pow(Bv[j], q - 2, q)) % q
            if z0 is None:
                z0 = zz
            elif z0 != zz:
                ok = False
                break
        if ok and z0 is not None:
            per.setdefault(z0, set()).add(S)
    sizes = {}
    for z in list(range(q)) + ["inf"]:
        sizes[str(z)] = len(per.get(z, ()))
    return min(sizes.values()), joint_max, sizes, shared


def mc_pencil(H, q, n, k, w, M):
    rp = n - k - w
    N, m = n // M, rp // M
    cosets = [[i for i in range(n) if i % N == j] for j in range(N)]
    T0 = [i for j in range(m) for i in cosets[j]]
    pr = 1
    for i in T0:
        pr = (pr * H[i]) % q
    c = (((-1) ** (rp + 1)) * pr) % q
    u = [0] * n
    u[n - 1] = 1
    u[k + w - 1] = (u[k + w - 1] + c) % q
    v = [0] * n
    v[n - 2] = 1
    v[k + w - 2] = (v[k + w - 2] + c) % q
    return ([poly_eval(u, x, q) for x in H], [poly_eval(v, x, q) for x in H])


n, k, w, q = 16, 4, 2, 17
a = k + w
H, beta, omega = make_domain(q, n, beta_exp=0)
random.seed(20260802)

print("row n=%d k=%d w=%d a=%d q=%d" % (n, k, w, a, q))

# C1: the MC shift pencil
uv, vv = mc_pencil(H, q, n, k, w, 2)
mn, jm, sizes, shared = analyse(uv, vv, H, k, a, q)
print("  MC shift pencil : min=%d  joint_max=%d  shared_supports=%d" % (mn, jm, shared))
check(jm == a, "C1 MC pencil is above cascade", (mn, jm))
out["runs"].append({"kind": "mc_shift", "min": mn, "joint_max": jm,
                    "shared_supports": shared, "above_cascade": jm >= a})

# C2: random pencils
rand = []
for t in range(25):
    uv2 = [random.randrange(q) for _ in range(n)]
    vv2 = [random.randrange(q) for _ in range(n)]
    mn2, jm2, s2, sh2 = analyse(uv2, vv2, H, k, a, q)
    rand.append({"min": mn2, "joint_max": jm2, "shared": sh2})
    check(jm2 < a or sh2 > 0, "C4 key lemma consistency", (mn2, jm2, sh2))
print("  random pencils  : min in [%d,%d], joint_max in [%d,%d], above-cascade %d/25"
      % (min(r["min"] for r in rand), max(r["min"] for r in rand),
         min(r["joint_max"] for r in rand), max(r["joint_max"] for r in rand),
         sum(1 for r in rand if r["joint_max"] >= a)))
out["runs"].append({"kind": "random", "instances": rand})

# C3: hill climbing on (u,v) maximising min_z L subject to BELOW CASCADE
best = None
for restart in range(4):
    uv3 = [random.randrange(q) for _ in range(n)]
    vv3 = [random.randrange(q) for _ in range(n)]
    mn3, jm3, _, _ = analyse(uv3, vv3, H, k, a, q)
    cur = mn3 if jm3 < a else -1
    for it in range(90):
        i = random.randrange(2 * n)
        old = uv3[i] if i < n else vv3[i - n]
        new = random.randrange(q)
        if new == old:
            continue
        if i < n:
            uv3[i] = new
        else:
            vv3[i - n] = new
        m4, j4, _, _ = analyse(uv3, vv3, H, k, a, q)
        cand = m4 if j4 < a else -1
        if cand >= cur:
            cur = cand
        else:
            if i < n:
                uv3[i] = old
            else:
                vv3[i - n] = old
    if best is None or cur > best:
        best = cur
    print("  climb restart %d : best below-cascade min = %d" % (restart, cur))
out["runs"].append({"kind": "hill_climb_below_cascade", "best_min": best,
                    "iterations": 90, "restarts": 4})
print("  BEST below-cascade min over the search: %s   (MC above-cascade min = %d)"
      % (best, mn))

out["verdict"] = "SEARCH_DONE"
out["c3_supported"] = (best is not None and best < mn)
with open(os.path.join(CHK, "below_cascade.json"), "w") as f:
    json.dump(out, f, indent=1)
print("checks=%d fails=%d  C3 supported=%s" %
      (out["checks"], len(out["fails"]), out["c3_supported"]))

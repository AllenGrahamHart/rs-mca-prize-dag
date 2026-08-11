"""r34 D3b -- THE VALUE-COINCIDENCE BUDGET: why m=3 lands and m=4 does not
(for the (SPLIT-m)+sigma ansatz), measured rather than asserted.

The m=3 witness needs, from a single degree-3 pencil phi on D = mu_48:
  8 "self-coincidences" -- unordered pairs {x,x'} of D, x' != +-x, with
  phi(x) = phi(x') -- placed inside the 9 selected sigma-orbits, because each
  degree-2 vertex of the selected path H is exactly one such coincidence.

At m=4 the (SPLIT-m) budget deg_x G <= 3m-3 = 9 splits over m-1 = 3 factors.
With sigma = -1 the only sigma-compatible split is 3+3+(even <= 3) = 3+3+2:
two swapped degree-3 pencils phi, phi o sigma and ONE sigma-INVARIANT factor
chi = R(x^2)/S(x^2) with deg R,S <= 1 in u = x^2 -- a Moebius map in u, hence
INJECTIVE ON ORBITS.  So the 12 selected orbits produce 12 pairwise-distinct
chi-slopes for free, and the 24 phi-values must be squeezed into the SAME 15
type-2 slopes.  That costs:
  (i)  >= 9 phi self-coincidences inside the selection, and
  (ii) >= 15 CROSS-coincidences phi(x) = chi(y) (a value equality between two
       unrelated maps, i.e. an event of probability ~1/q each).

This script measures the SUPPLY of (i) and (ii) at both scales and both fields.
"""

import random
import sys

sys.path.insert(0, "notes/pilots_20260811/r34_bivcurve_m34")
from biv_core import mu_N
from m3_phi import cev

out = []
P = out.append
P("=" * 78)
P("r34 D3b -- VALUE-COINCIDENCE BUDGET (supply vs demand), two fields per scale")
P("=" * 78)


def measure(m, q, trials, seed):
    Nn = 16 * m
    D = mu_N(q, Nn)
    orb, seen = [], set()
    for x in D:
        if x in seen:
            continue
        y = (q - x) % q
        seen.add(x); seen.add(y)
        orb.append((x, y))
    rnd = random.Random(seed)
    selfc, orbc, crossc = [], [], []
    for _ in range(trials):
        A = [rnd.randrange(q) for _ in range(4)]
        B = [rnd.randrange(q) for _ in range(4)]
        ph, ok = {}, True
        for x in D:
            bx = cev(B, x, q)
            if bx == 0:
                ok = False
                break
            ph[x] = cev(A, x, q) * pow(bx, q - 2, q) % q
        if not ok:
            continue
        inv = {}
        for x in D:
            inv.setdefault(ph[x], []).append(x)
        sc = 0
        for v, xs in inv.items():
            for i in range(len(xs)):
                for j in range(i + 1, len(xs)):
                    if xs[j] != (q - xs[i]) % q:
                        sc += 1
        selfc.append(sc)
        # orbit-level: pairs of DISTINCT orbits sharing a phi-value
        oidx = {}
        for k, (x, y) in enumerate(orb):
            oidx[x] = k
            oidx[y] = k
        oc = set()
        for v, xs in inv.items():
            ks = sorted(set(oidx[x] for x in xs))
            for i in range(len(ks)):
                for j in range(i + 1, len(ks)):
                    oc.add((ks[i], ks[j]))
        orbc.append(len(oc))
        # cross-coincidences with a random sigma-invariant Moebius chi in u=x^2
        Rr = [rnd.randrange(q) for _ in range(2)]
        S = [rnd.randrange(q) for _ in range(2)]
        chv = {}
        bad = False
        for k, (x, y) in enumerate(orb):
            u = x * x % q
            s = cev(S, u, q)
            if s == 0:
                bad = True
                break
            chv[k] = cev(Rr, u, q) * pow(s, q - 2, q) % q
        if bad:
            continue
        cvals = set(chv.values())
        crossc.append(sum(1 for x in D if ph[x] in cvals))
    def stat(v):
        return (min(v), sum(v) / len(v), max(v)) if v else (0, 0, 0)
    return stat(selfc), stat(orbc), stat(crossc), len(orb)


for (m, q, tri) in ((3, 97, 4000), (3, 193, 4000), (4, 193, 4000), (4, 257, 4000)):
    s1, s2, s3, no = measure(m, q, tri, 990000 + 100 * m + q)
    Nn, rho, a = 16 * m, 4 * m - 1, 7 * m - 1
    need_self = {3: 8, 4: 9}[m]
    need_cross = {3: 0, 4: 15}[m]
    P("")
    P("-" * 78)
    P("m = %d, D = mu_%d < F_%d, %d sigma-orbits, a = %d, T_2 = rho = %d"
      % (m, Nn, q, no, a, rho))
    P("  SUPPLY  phi self-coincidences in ALL of D   min/mean/max = %d / %.2f / %d"
      % s1)
    P("          (analytic prediction |D|^2 (d-1) / (2q) = %.1f)"
      % (Nn * Nn * 2.0 / (2 * q)))
    P("  SUPPLY  distinct ORBIT pairs sharing a value min/mean/max = %d / %.2f / %d"
      % s2)
    P("  SUPPLY  cross-coincidences phi(x) in chi(orbits) = %d / %.2f / %d" % s3)
    P("          (analytic prediction |D| * #orbits / q = %.1f)"
      % (Nn * no * 1.0 / q))
    P("  DEMAND  self-coincidences needed INSIDE the selection : %d" % need_self)
    P("  DEMAND  cross-coincidences needed                     : %d" % need_cross)
    P("  VERDICT (this ansatz, this scale): self %s ; cross %s"
      % ("SUPPLY >= DEMAND in all of D" if s1[1] >= need_self else "SHORT",
         "n/a (m=3 has no third factor)" if m == 3 else
         ("SUPPLY >= DEMAND" if s3[1] >= need_cross else "SHORT BY ~%.1fx"
          % (need_cross / max(s3[1], 1e-9)))))

P("")
P("=" * 78)
print("\n".join(out))
with open("notes/pilots_20260811/r34_bivcurve_m34/m4_budget_results.txt", "w") as f:
    f.write("\n".join(out) + "\n")

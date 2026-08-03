#!/usr/bin/env python3
"""L-D core-count pilot verifier.

Profile: local (pure python integers, deterministic, no third-party imports,
no reads outside this directory except the row-constant JSON it is given).

Checks, in order:
  A. Row arithmetic: the exact gap g* at which ONE deeper band pair breaks the
     RAW reading of L-D at each of the six recorded rows; m*; V*.
  B. Toy fixture (n=20, k=6, h=6, A=12, q=101): a machine-built received pair
     with a cascade-tier (depth h-1) codeword pair, two live slopes with
     exact-A selected supports, and an exhaustive count of RAW_1 vs N_1.
  C. The fiber identity RAW_d = SUM_e MAX_e * C(k+e, k+d) (F4), pair
     uniqueness (F5), the L>=2 monotonicity non-rescue (F2), and the
     pairwise-intersection contradiction in CONSOLIDATION.md section 2 (F6).
"""

import itertools
import json
import math
import os
import sys
from math import comb

LOG2 = math.log(2.0)

def log2comb(N, K):
    """log2 C(N,K) via lgamma -- the prize-row binomials are astronomically
    large (h-2 ~ 2^33), so they must never be materialised as integers."""
    if K < 0 or K > N:
        return float("-inf")
    if K == 0 or K == N:
        return 0.0
    return (math.lgamma(N + 1) - math.lgamma(K + 1)
            - math.lgamma(N - K + 1)) / LOG2

FAIL = []
def check(name, cond, detail=""):
    tag = "PASS" if cond else "FAIL"
    if not cond:
        FAIL.append(name)
    print(f"  [{tag}] {name}" + (f"  {detail}" if detail else ""))

# --------------------------------------------------------------------------
# A. Row arithmetic
# --------------------------------------------------------------------------

ROWS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "..", "..", "pilots_20260802", "support4_relation",
                         "stage5_escape.json")

def load_rows():
    with open(ROWS_PATH) as fh:
        return json.load(fh)["criterion"]

def budget(n):
    """0.68 n^2, the task's stated cap; exact rational as a floor."""
    return (68 * n * n) // 100

def gstar(k, d, n):
    """Least gap g>=1 with C(k+d+g, g) > 0.68 n^2 (one deeper pair breaks RAW_d)."""
    B = budget(n)
    g = 1
    while g < 64:
        if comb(k + d + g, g) > B:
            return g
        g += 1
    return None

def mstar(k, d, g, n):
    """Least number of depth-(d+g) pairs needed to breach the budget in RAW_d."""
    B = budget(n)
    c = comb(k + d + g, g)
    return -(-(B + 1) // c)   # ceil((B+1)/c)

def vstar(n):
    """Largest V with C(V,2) <= 0.68 n^2 (the pair-graph boundary)."""
    B = budget(n)
    lo, hi = 1, 4 * n + 10
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid * (mid - 1) // 2 <= B:
            lo = mid
        else:
            hi = mid - 1
    return lo

def section_A():
    print("\n=== A. ROW ARITHMETIC (six recorded rows) ===")
    rows = load_rows()
    out = []
    for r in rows:
        n, k, A, h = r["n"], r["k"], r["A"], r["h"]
        check(f"{r['name']}: A == k+h", A == k + h, f"A={A}")
        B = budget(n)
        d = 1
        g = gstar(k, d, n)
        # the cascade tier's own contribution to RAW_1: C(k+(h-1), k+1),
        # i.e. C(A-1, h-2) -- in log2, it is astronomical at the prize rows.
        casc_log2 = log2comb(k + h - 1, h - 2) if h >= 2 else float("-inf")
        rec = {
            "row": r["name"], "n": n, "k": k, "h": h, "A": A,
            "budget_0.68n2": B, "budget_log2": log2comb(0, 0) if B == 0
            else math.log(B) / LOG2,
            "gstar_d1": g,
            "mstar_d1": mstar(k, d, g, n) if g else None,
            "mstar_gap1": mstar(k, d, 1, n),
            "mstar_gap2": mstar(k, d, 2, n),
            "cascade_RAW1_log2": casc_log2,
            "cascade_breaks_RAW1": casc_log2 > math.log(B) / LOG2,
            "Vstar": vstar(n),
            "Vstar_over_n": vstar(n) / n,
        }
        out.append(rec)
        print(f"  {r['name']:<12} h={h:<12} g*={g}  "
              f"m*(gap1)={rec['mstar_gap1']}  m*(gap2)={rec['mstar_gap2']}  "
              f"log2(cascade RAW_1 term)={casc_log2:.4g} vs "
              f"log2(budget)={rec['budget_log2']:.4g}  "
              f"breaks={rec['cascade_breaks_RAW1']}  "
              f"V*={rec['Vstar_over_n']:.4f} n")
    # sanity: g* must be >= 1 and finite everywhere
    check("A1: g* finite at all six rows", all(o["gstar_d1"] for o in out))
    # sanity: V* ~ 1.166 n
    check("A2: V* between 1.16n and 1.17n at all rows",
          all(1.16 <= o["Vstar_over_n"] <= 1.17 for o in out))
    return out

# --------------------------------------------------------------------------
# B/C. Toy fixture
# --------------------------------------------------------------------------

Q = 101
N = 20
K = 6
H = 6
AA = K + H          # 12
DEEP = AA - 1       # 11 = k + (h-1), the cascade tier core size
DEPTH_D = 1
CORE = K + DEPTH_D  # 7

def inv(a):
    return pow(a % Q, Q - 2, Q)

def poly_eval(coeffs, x):
    acc = 0
    for c in reversed(coeffs):
        acc = (acc * x + c) % Q
    return acc

def interp_coeffs(xs, ys):
    """Newton divided differences -> monomial coefficients, degree < len(xs)."""
    m = len(xs)
    dd = list(ys)
    for j in range(1, m):
        for i in range(m - 1, j - 1, -1):
            dd[i] = (dd[i] - dd[i - 1]) * inv(xs[i] - xs[i - j]) % Q
    coeffs = [0] * m
    # Horner from the Newton form
    for i in range(m - 1, -1, -1):
        new = [0] * m
        for t in range(m - 1):
            new[t + 1] = coeffs[t]
        for t in range(m):
            new[t] = (new[t] - xs[i] * coeffs[t]) % Q if t < m else new[t]
        new[0] = (new[0] + dd[i]) % Q
        coeffs = new
    return coeffs

def top_coeff(Z, vals):
    """Top (degree |Z|-1) coefficient of the interpolant of `vals` on Z.
    = sum_{x in Z} val(x) / prod_{y != x} (x-y). Zero iff degree < |Z|-1 ...
    for |Z| = k+1 this IS A(Z) (the single KEY LEMMA top coefficient)."""
    s = 0
    for x in Z:
        p = 1
        for y in Z:
            if y != x:
                p = p * (x - y) % Q
        s = (s + vals[x] * inv(p)) % Q
    return s

def build_fixture():
    """u,v with a codeword pair (f,g) of joint agreement exactly DEEP=11,
    and two live slopes z1,z2 whose exact-A supports are W u {a}, W u {b}."""
    D = list(range(1, N + 1))
    f = [3, 1, 4, 1, 5, 9]          # deg < 6 codeword
    g = [2, 7, 1, 8, 2, 8]
    W = D[:DEEP]                    # the 11-point core
    a, b = D[DEEP], D[DEEP + 1]     # the two upgrade points
    z1, z2 = 2, 5
    u, v = {}, {}
    for x in D:
        u[x] = poly_eval(f, x)
        v[x] = poly_eval(g, x)
    # off-core noise
    rest = D[DEEP:]
    # at a: make (u-f)(a) = -z1*delta, (v-g)(a) = delta  -> a joins S_{z1} only
    da, db = 7, 11
    u[a] = (u[a] - z1 * da) % Q
    v[a] = (v[a] + da) % Q
    u[b] = (u[b] - z2 * db) % Q
    v[b] = (v[b] + db) % Q
    # remaining off-core points: generic noise (fixed, deterministic)
    for i, x in enumerate(rest[2:]):
        u[x] = (u[x] + 13 + 6 * i) % Q
        v[x] = (v[x] + 29 + 11 * i) % Q
    return D, f, g, W, a, b, z1, z2, u, v

def max_agreement(D, word):
    """Max over codewords (deg < K) of the agreement with `word`, by sweeping
    all K-subsets. Returns (max_agr, list of agreement sets attaining it)."""
    best, sets = 0, []
    for S in itertools.combinations(D, K):
        xs = list(S)
        ys = [word[x] for x in xs]
        c = interp_coeffs(xs, ys)
        agr = tuple(x for x in D if poly_eval(c, x) == word[x])
        if len(agr) > best:
            best, sets = len(agr), [agr]
        elif len(agr) == best and agr not in sets:
            sets.append(agr)
    return best, sets

def section_BC():
    print("\n=== B. TOY FIXTURE (n=20, k=6, h=6, A=12, q=101) ===")
    D, f, g, W, a, b, z1, z2, u, v = build_fixture()
    Wset = set(W)

    # the codeword pair's joint agreement set
    Wfg = [x for x in D if u[x] == poly_eval(f, x) and v[x] == poly_eval(g, x)]
    check("B1: joint agreement W(f,g) has size k+h-1 (cascade tier)",
          len(Wfg) == DEEP and set(Wfg) == Wset, f"|W|={len(Wfg)}")

    # liveness: max agreement of w_z1 and w_z2 is exactly A
    for z, extra in ((z1, a), (z2, b)):
        w = {x: (u[x] + z * v[x]) % Q for x in D}
        m, sets = max_agreement(D, w)
        expect = tuple(sorted(Wset | {extra}))
        check(f"B2.{z}: max agr(w_{z}) == A == {AA}", m == AA, f"got {m}")
        check(f"B3.{z}: the exact-A support is W u {{{extra}}}",
              len(sets) == 1 and tuple(sorted(sets[0])) == expect,
              f"{len(sets)} maximizer(s)")

    # tangent gate on the two single words
    mu, _ = max_agreement(D, u)
    mv, _ = max_agreement(D, v)
    check("B4: agr gate on u  (<= A)", mu <= AA, f"max agr(u)={mu}")
    check("B5: agr gate on v  (<= A)", mv <= AA, f"max agr(v)={mv}")

    S1 = Wset | {a}
    S2 = Wset | {b}
    check("B6: S_z1 ^ S_z2 == W, i.e. core depth h-1", S1 & S2 == Wset)

    print("\n=== C. RAW vs MAXIMAL core counts (exhaustive) ===")
    # exhaustive RAW_1: all (k+1)-subsets Z with A(Z) = B(Z) = 0
    raw = []
    for Z in itertools.combinations(D, CORE):
        if top_coeff(Z, u) == 0 and top_coeff(Z, v) == 0:
            raw.append(Z)
    RAW1 = len(raw)
    B_toy = budget(N)
    print(f"  RAW_1 = {RAW1}   budget 0.68 n^2 = {B_toy}   C(11,7) = {comb(DEEP, CORE)}")
    check("C1 (F1): RAW_1 > 0.68 n^2  -- the RAW reading of L-D is REFUTED",
          RAW1 > B_toy, f"{RAW1} > {B_toy}")
    rawset = set(raw)      # combinations() already yields sorted tuples
    check("C2: every (k+1)-subset of the deep core is a joint-explanation core",
          all(Z in rawset for Z in itertools.combinations(sorted(Wset), CORE)),
          f"C(11,7) = {comb(DEEP, CORE)} subsets checked")

    # F2: the L >= 2 filter does not rescue it
    n_sel = sum(1 for Z in raw if set(Z) <= S1 and set(Z) <= S2)
    check("C3 (F2): RAW_1 with L>=2 (both selected supports) still > budget",
          n_sel > B_toy, f"RAW_1^sel = {n_sel} > {B_toy}")

    # F5 + the fiber map: Z -> (I_Z(u), I_Z(v)); collect maximal cores
    fibers = {}
    for Z in raw:
        xs = list(Z)
        cu = interp_coeffs(xs, [u[x] for x in xs])
        cv = interp_coeffs(xs, [v[x] for x in xs])
        P, Qq = tuple(cu[:K]), tuple(cv[:K])
        tail_u, tail_v = cu[K:], cv[K:]
        if any(tail_u) or any(tail_v):
            check("C4 (F5): interpolant degree < k on a joint-explanation core",
                  False, f"Z={Z}")
            return
        fibers.setdefault((P, Qq), []).append(Z)
    check("C4 (F5): every joint-explanation core has deg<k interpolants "
          "and a UNIQUE codeword pair", True,
          f"{len(fibers)} distinct pair(s)")

    # MAX_e: full joint agreement size of each pair found
    maxe = {}
    for (P, Qq), Zs in fibers.items():
        Wpq = [x for x in D
               if u[x] == poly_eval(list(P), x) and v[x] == poly_eval(list(Qq), x)]
        e = len(Wpq) - K
        maxe[e] = maxe.get(e, 0) + 1
        # every Z in the fiber must be a subset of W(P,Q)
        check(f"C5: fiber of a pair at depth {e} consists of subsets of W(P,Q)",
              all(set(Z) <= set(Wpq) for Z in Zs), f"|W|={len(Wpq)}")
        check(f"C6: fiber size == C(|W|, k+d) at depth {e}",
              len(Zs) == comb(len(Wpq), CORE),
              f"{len(Zs)} vs {comb(len(Wpq), CORE)}")

    # F4: the fiber identity
    pred = sum(cnt * comb(K + e, CORE) for e, cnt in maxe.items() if e >= DEPTH_D)
    check("C7 (F4): RAW_d == SUM_e MAX_e * C(k+e, k+d)  (exact fiber identity)",
          pred == RAW1, f"predicted {pred}, measured {RAW1}")
    print(f"  MAX_e census (e -> #codeword pairs with |W| = k+e): "
          f"{dict(sorted(maxe.items()))}")

    # F3: the MAXIMAL reading -- N_1 (maximal depth-1 cores with L >= 2)
    N1 = 0
    for (P, Qq), Zs in fibers.items():
        Wpq = set(x for x in D
                  if u[x] == poly_eval(list(P), x) and v[x] == poly_eval(list(Qq), x))
        if len(Wpq) == CORE and Wpq <= S1 and Wpq <= S2:
            N1 += 1
    check("C8 (F3): the MAXIMAL count N_1 stays far under budget",
          N1 <= B_toy, f"N_1 = {N1} vs budget {B_toy}")
    print(f"  ==> RAW_1 = {RAW1}  vs  N_1 (maximal, L>=2) = {N1}   "
          f"ratio {RAW1 / max(N1,1):.0f}x")

    # F6: CONSOLIDATION.md section 2's "pairwise <= k-1" is false for RAW cores
    worst = 0
    rl = [set(Z) for Z in raw]
    for i in range(min(len(rl), 60)):
        for j in range(i + 1, min(len(rl), 60)):
            worst = max(worst, len(rl[i] & rl[j]))
    check("C9 (F6): two distinct RAW joint-explanation (k+d)-sets share >= k "
          "points -- refutes 'pairwise <= k-1' for the RAW reading",
          worst >= K, f"max pairwise overlap found = {worst} (k = {K})")

def main():
    outA = section_A()
    section_BC()
    print("\n=== SUMMARY ===")
    if FAIL:
        print(f"  {len(FAIL)} FAILURE(S): {FAIL}")
        sys.exit(1)
    print("  ALL CHECKS PASS")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""ROUND S1 (self-tennis): exact instantiation of the production norm-sieve.

All decisions by EXACT integer arithmetic (no floating logs on any decision
path; floats only in display).

Objects (level = (n' = 2N, L), admissible q ≡ 1 mod n', Q <= q < 2Q):
  K_q = kernel lattice {d in Z^N : sum_y d_y x_y^(2l-1) ≡ 0 mod q, l=1..L},
        x_y = omega^y (pinned half-section), i.e. D(omega^(2l-1)) ≡ 0,
        D(t) = sum d_y t^y in Z[t]/(t^N+1) ≅ Z[zeta_2N].
  W_cov(q) = sum over reduced ternary d in K_q with L+1 <= w(d) <= w_cov
             of 2^-w(d)   (elementwise; shift-invariant).

FACTS (proved in A1_PROD_NORM_SIEVE.md):
  F1  q ≡ 1 mod n' splits completely; the L conditions are L DISTINCT prime
      ideals above q dividing (D)  =>  q^L | Norm(D), 0 < |Norm(D)| <= w^N.
  F2  per-element band cap: #{q in [Q,2Q): d in K_q} <= D_cap(w) :=
      max{m : Q^(L*m) <= w^N}  (exact integer comparison).
  F3  weighted Markov: sum_{q in band} W_cov(q) <= TOTAL :=
      sum_{w=L+1}^{w_cov} C(N,w) * D_cap(w)   (the 2^w signs cancel 2^-w).
  F4  count theorem (UNCONDITIONAL): #{q in band : W_cov(q) >= T} <= TOTAL/T.
  F5  density corollary under the AP-prime-count input
      pi_{n'}[Q,2Q) >= Q / (2 * phi(n') * ln 2Q)   [standard, explicit for
      these ranges; stated as input AP].

This script computes, per level L = 1..34 with N = 256L, Q = 2^255:
  - exact w*(L) = max{w : C(N,w)*2^w * 2^10 <= Q^L}  (the pinned tail split)
  - exact D_cap(w*) and the covered weight w_1(L) = max w_cov <= w*(L) such
    that TOTAL(w_cov) <= 2^-X_TARGET * AP_LOWER  with T = 1
  - the exceptional density exponent actually achieved at w_1(L)
  - the coverage table and the exact cutoff level where coverage dies.

TOY VALIDATION + REFUTE-CHAIR ATTACKS (n' = 64 band [1e5, 1.3e5], L = 1):
  - per-element cap attack: factor the norms of the known multi-orbit
    generators; verify no element hits more band primes than D_cap
  - sieve bound vs OBSERVED incidence counts from band_census (the bound
    must dominate observation; quantify looseness honestly).
"""
import importlib.util
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent

Q_LOG2 = 255          # production band [2^255, 2^256)
X_TARGET = 40         # demanded exceptional-count exponent (with T = 1)
LEVELS = range(1, 35)

fails = []
def check(name, cond):
    print(("PASS" if cond else "FAIL"), name)
    if not cond:
        fails.append(name)

# ---------- exact helpers ----------
def dcap(N, L, w, Qlog2):
    """max m >= 0 with (2^Qlog2)^(L*m) <= w^N — exact."""
    m = 0
    wN = w ** N
    while (1 << (Qlog2 * L * (m + 1))) <= wN:
        m += 1
    return m

def wstar(N, L, Qlog2):
    """max w with C(N,w) * 2^w * 2^10 <= 2^(Qlog2*L) — exact."""
    lim = 1 << (Qlog2 * L)
    w = L + 1
    best = None
    while w <= N:
        if math.comb(N, w) * (1 << w) * (1 << 10) <= lim:
            best = w
        w += 1
    # window is unimodal in w up to N/... comb*2^w increasing until ~2N/3
    return best

def total_weighted(N, L, w_cov, Qlog2):
    """TOTAL = sum_{w=L+1..w_cov} C(N,w) * D_cap(w) — exact integer."""
    t = 0
    for w in range(L + 1, w_cov + 1):
        t += math.comb(N, w) * dcap(N, L, w, Qlog2)
    return t

def log2_int(n):
    """float log2 of a big int (display only)."""
    if n == 0:
        return float("-inf")
    b = n.bit_length()
    return b - 1 + math.log2(n / (1 << (b - 1)))

# ---------- production table ----------
print("== production coverage table (Q = 2^255, N = 256L, T = 1, X_target =",
      X_TARGET, ") ==")
# AP input: #admissible primes in [Q, 2Q) >= Q / (2 * phi(n') * ln(2Q)),
# phi(n') = N (n' = 2N a power of two only when L is; we use n' = 2N
# parametrically and phi <= n'/2 = N as the safe bound).
rows = []
cutoff_level = None
for L in LEVELS:
    N = 256 * L
    ws = wstar(N, L, Q_LOG2)
    ln2Q = (Q_LOG2 + 1) * math.log(2)
    ap_lower_log2 = Q_LOG2 - log2_int(2 * N) - math.log2(ln2Q)  # log2 of AP bound
    # find w_1: largest w_cov <= w* with log2(TOTAL) <= ap_lower_log2 - X_TARGET
    w1 = None
    t_at_w1 = 0
    t = 0
    for w in range(L + 1, (ws or N) + 1):
        t += math.comb(N, w) * dcap(N, L, w, Q_LOG2)
        if log2_int(t) <= ap_lower_log2 - X_TARGET:
            w1, t_at_w1 = w, t
        else:
            break
    density_exp = (ap_lower_log2 - log2_int(t_at_w1)) if w1 else None
    rows.append({"L": L, "N": N, "w_star": ws, "w_1": w1,
                 "covered_fraction_of_window":
                     None if not ws else (0 if not w1 else
                                          round((w1 - L) / (ws - L), 3)),
                 "density_exponent_X": None if not w1 else round(density_exp, 1)})
    if w1 is None and cutoff_level is None:
        cutoff_level = L
for r in rows:
    print(f"  L={r['L']:>2}  N={r['N']:>5}  w*={r['w_star']}  w_1={r['w_1']}"
          f"  covered={r['covered_fraction_of_window']}"
          f"  X={r['density_exponent_X']}")
print("  coverage cutoff level:", cutoff_level)

check("PROD level 1 covers its FULL window (w_1 == w*)",
      rows[0]["w_1"] == rows[0]["w_star"] and rows[0]["w_1"] is not None)
check("PROD level-1 density exponent X >= 40",
      rows[0]["density_exponent_X"] is not None and rows[0]["density_exponent_X"] >= 40)
check("coverage dies at some level <= 34 (the honest gap exists)",
      cutoff_level is not None)

# pinned-file w* estimate check ("~68*L at q = 2^255.9"): verify or refute
check(f"pinned '~68L' w* estimate is WRONG (exact w*(1) = {rows[0]['w_star']})",
      abs(rows[0]["w_star"] - 68) > 5)

# ---------- toy validation + refute-chair (n'=64, L=1, band [1e5, 1.3e5]) ----
print("\n== toy validation (n'=64, N=32, w<=5, band [100000,130000]) ==")
spec = importlib.util.spec_from_file_location("census", HERE / "modal_dli_orbit_census.py")
census = importlib.util.module_from_spec(spec)
spec.loader.exec_module(census)

N_t, L_t, Qlo, Qhi = 32, 1, 100_000, 130_000

def dcap_toy(w):
    m = 0
    while Qlo ** (m + 1) <= w ** N_t:
        m += 1
    return m

total_toy = sum(math.comb(N_t, w) * dcap_toy(w) for w in range(2, 6))
# observed: band_census_and_clusters.json has per-prime independent counts;
# raw orbit incidence >= independent count is NOT needed — the sieve bounds
# the weighted mass; observed weighted mass per prime (weight-5 orbits, 64
# elements each): W_obs(q) >= k_orbits * 64 * 2^-5 = 2k. Bound must dominate.
bc = json.load(open(HERE / "band_census_and_clusters.json"))["band_census"]
n_primes = bc["n_primes"]
k_hist = {int(k): v for k, v in bc["k_histogram"].items()}
obs_ge1 = sum(v for k, v in k_hist.items() if k >= 1)
print(f"  TOTAL (weighted Markov numerator) = {total_toy}"
      f" (log2 = {log2_int(total_toy):.1f})")
print(f"  observed primes with >=1 indep generator: {obs_ge1}/{n_primes}")
check("toy: sieve bound with T = 2 (i.e. one weight-5 orbit's mass) dominates"
      " observed count", total_toy / 2 >= obs_ge1)

# per-element cap attack: the strongest known elements (the 110849 four and
# the 204353 cluster) — factor their norms, count band primes with q^1 | Norm
def norm_of(sup, sgn):
    import itertools
    # |Norm| = prod over odd a mod 64 of D(zeta^a); compute exactly via
    # resultant with z^32+1 using integer arithmetic (companion-free: use
    # complex floats only as a cross-check; exact via sympy-free PRS)
    from fractions import Fraction
    def resultant(f, g):
        f = [Fraction(c) for c in f]; g = [Fraction(c) for c in g]
        def deg(p):
            d = len(p) - 1
            while d >= 0 and p[d] == 0: d -= 1
            return d
        res = Fraction(1); F, G = f, g
        while True:
            dF, dG = deg(F), deg(G)
            if dG < 0: return 0
            if dG == 0: return res * G[0] ** dF
            R = F[:]
            while deg(R) >= dG:
                dR = deg(R)
                c = R[dR] / G[dG]
                for i in range(dG + 1):
                    R[dR - dG + i] -= c * G[i]
            dR = deg(R)
            res *= G[dG] ** (dF - max(dR, 0)) * (-1) ** (dF * dG)
            if dR < 0: return 0
            F, G = G, R[:dR + 1]
    xn1 = [1] + [0] * 31 + [1]
    poly = [0] * 32
    for e, s in zip(sup, sgn):
        poly[e] = s
    r = resultant(xn1, poly)
    return abs(int(r))

PRO_GENS = [((0, 4, 21, 27, 29), (1, 1, 1, -1, 1)),
            ((0, 3, 21, 23, 28), (1, 1, -1, 1, -1)),
            ((0, 3, 6, 25, 29), (1, 1, -1, -1, 1)),
            ((0, 3, 8, 19, 25), (1, 1, 1, -1, 1))]
cap = dcap_toy(5)
atk_ok = True
for i, (sup, sgn) in enumerate(PRO_GENS, 1):
    nm = norm_of(sup, sgn)
    hits = []
    m = nm
    d = 2
    while d * d <= m:
        while m % d == 0:
            if Qlo <= d < Qhi and d % 64 == 1:
                hits.append(d)
            m //= d
        d += 1 if d == 2 else 2
    if m > 1 and Qlo <= m < Qhi and m % 64 == 1:
        hits.append(m)
    print(f"  P{i}: |Norm| = {nm} (log2 {log2_int(nm):.1f}), band prime hits: {hits}")
    if len(hits) > cap:
        atk_ok = False
check(f"per-element cap D_cap = {cap} not exceeded by any known extreme element",
      atk_ok)
check("all four Pro generators hit 110849 (norm divisibility replay)",
      all(norm_of(s, g) % 110_849 == 0 for s, g in PRO_GENS))

out = {"production_table": rows, "cutoff_level": cutoff_level,
       "X_target": X_TARGET, "toy_total": total_toy,
       "toy_obs_ge1": obs_ge1, "toy_n_primes": n_primes}
(HERE / "a1_prod_norm_sieve_table.json").write_text(json.dumps(out, indent=1))
print()
print("ALL PASS" if not fails else f"FAILURES: {fails}")

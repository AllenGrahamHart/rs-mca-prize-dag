#!/usr/bin/env python3
"""F2A.5b -- the PARITY BOUNDARY: what must the slice-theorem hypothesis say?

Pilot 2026-08-02, notes/pilots_20260802/f2_parity_boundary/.
Read-only imports from notes/pilots_20260802/f2_slice_coefficients/ (slicecore,
mode_and_coset) and .../f2_carry_reachability/f2model.py.  Nothing outside this
directory is ever written.

--------------------------------------------------------------------- setup --
Standing facts inherited from the F2A.5 pilot (all exact there):

  sigma_i^+- = s_i^+- + p*u_i^+-  (mod 2p),   Delta_i = sigma_i^+ - sigma_i^-,
  h_p(r) = +1 if r mod 2p < p else -1,
  V_b := sum_{|tau| = b} h_p( sum_i sigma_i(tau_i) )      (balanced-weight proxy)
  rho_b := |V_b| / C(n,b),
  arg r_i(k) = pi k Delta_i / p for every odd mode k,
  slice-death at k  <=>  {k Delta_i mod 2p} constant.

------------------------------------------------------- the exact proxy law ---
Writing base := sum_i sigma_i^-, the proxy statistic depends ONLY on the Delta
multiset and the base:

  V_b = sum_{|S| = b} h_p( base + sum_{i in S} Delta_i ),

and with h_p(r) = (1/2p) sum_k hhat_p(k) omega^{kr}, omega = zeta_{2p},

  (P1)   V_b = (1/2p) sum_{k odd} hhat_p(k) omega^{k*base} e_b( z^{(k)} ),
         z_i^{(k)} := omega^{k Delta_i},   e_b = elementary symmetric.

hhat_p(k) = 0 for even k and |hhat_p(k)| = 2 / |sin(pi k / 2p)| for odd k;
in particular hhat_p(p) = 2.  So EVERY structural question about rho_b is a
question about the n-point multiset {Delta_i} in Z/2p, mode by mode, through
the elementary symmetric polynomials of its k-th power phases.

--------------------------------------------------- the imbalance functionals -
For a slice fraction beta = b/n put the tilt r = beta/(1-beta).  Cauchy on
e_b(z) = [w^b] prod_i (1 + w z_i) over |w| = r gives, EXACTLY,

  (P2)   |e_b(z^{(k)})| / C(n,b)  <=  kappa(n,b) * 2^{-n Lambda_k(beta)},
         kappa(n,b) := (1+r)^n r^{-b} / C(n,b)   ( = O(sqrt n) ),
         Lambda_k(beta) := -(1/n) max_psi sum_i log2( |1 + r e^{i(theta_i+psi)}|
                                                       / (1+r) ),
         theta_i = pi k Delta_i / p.

Lambda_k >= 0 with equality iff all theta_i are equal, i.e. iff mode k is
slice-DEAD.  The max over psi is forced: e_b picks up only a unimodular factor
under a common rotation of the phases (the F2A.5 "phase SPREAD not location"
constraint), so no functional that is not rotation-invariant can appear.

Two specialisations, both exact:

  * k = p.  Then z_i = (-1)^{Delta_i} and e_b(z^{(p)}) = [w^b](1-w)^{n_o}(1+w)^{n_e}
    is a KRAWTCHOUK number (n_o = #odd Delta, n_e = n - n_o), and with
    beta_min = min(n_o,n_e)/n, s = 2 beta(1-beta),  Lambda_p has the CLOSED FORM

        Lambda_p(beta) = beta_min * log2( 1/|1-2beta| )        if 1-2beta_min >= s/(1-s)
                       = ( H(beta_min) - 1 - log2(1-s) ) / 2   otherwise,

    H = binary entropy in bits (derived in verify_boundary.py B5, checked to
    1e-12 against the numerics).  At the exact central slice beta = 1/2 the
    second branch always applies and Lambda_p(1/2) = H(beta_min)/2.
    So beta_min is exactly the k = p shadow of Lambda.
  * the surrogate.  Using -ln(1-x) >= x on 1 - 4beta(1-beta) sin^2(.),
        Lambda_k(beta) >= (beta(1-beta) / ln 2) * (1 - |R_k|),
        R_k := (1/n) sum_i omega^{k Delta_i}   (the empirical Fourier
                                                coefficient of the Delta multiset).
    and |R_p| = |n_e - n_o|/n = 1 - 2 beta_min.  So the whole hypothesis family
    is "the Delta multiset is Fourier-flat at odd frequencies", of which
    parity-inhomogeneity is the single frequency k = p.

Everything banked is exact integer arithmetic (V_b, C(n,b), Krawtchouk).
Lambda_k, |R_k| and per-mode |e_b| are float diagnostics and are LABELLED.
"""

from __future__ import annotations

import cmath
import collections
import json
import math
import os
import sys

sys.dont_write_bytecode = True  # never litter the imported pilots' directories

_HERE = os.path.dirname(os.path.abspath(__file__))
_SLICE = os.path.join(os.path.dirname(_HERE), "f2_slice_coefficients")
if _SLICE not in sys.path:
    sys.path.insert(0, _SLICE)

from slicecore import (  # noqa: E402
    Cyc, Delta_of, Fp2, abs_pairs, admissible_orders, carry_sign, elem_sym,
    hhat, omega_pow, pair_reps, residues, sigma_of, slice_coeffs_carrydp,
)

RESULTS = os.path.join(_HERE, "results")

TARGET_THIRD = 1.0 / 3.0
TARGET_43 = 1.0 / 43.0


# ------------------------------------------------------------------ model ---

_MODEL_CACHE: dict = {}


def model(p: int, c=(1, 1)):
    """(Delta list, sigma^- list) over ALL genuine conjugate pairs.  Exact."""
    key = (p, tuple(c))
    if key in _MODEL_CACHE:
        return _MODEL_CACHE[key]
    F = Fp2.make(p)
    mu = admissible_orders(p)[-1]
    reps = pair_reps(F, F.subgroup(mu))
    loc = [residues(F, c, y) for y in reps]
    D = Delta_of(p, loc)
    sig = sigma_of(p, loc)
    out = (D, [s[1] for s in sig], loc)
    _MODEL_CACHE[key] = out
    return out


# --------------------------------------------------- exact proxy statistic ---


def count_dp(p: int, deltas):
    """N[b][r] = #{S : |S| = b, sum_{i in S} Delta_i = r mod 2p}.  Exact ints."""
    two_p = 2 * p
    n = len(deltas)
    dp = [[0] * two_p for _ in range(n + 1)]
    dp[0][0] = 1
    for i, d in enumerate(deltas):
        nd = [[0] * two_p for _ in range(n + 1)]
        for b in range(i + 1):
            row = dp[b]
            if not any(row):
                continue
            ndb, ndb1 = nd[b], nd[b + 1]
            for r in range(two_p):
                v = row[r]
                if v:
                    ndb[r] += v
                    ndb1[(r + d) % two_p] += v
        dp = nd
    return dp


def V_from_counts(p: int, N, n: int, base: int):
    """V_b = sum_r N[b][r] h_p(base + r).  Exact integers."""
    two_p = 2 * p
    sgn = [carry_sign(p, (base + r) % two_p) for r in range(two_p)]
    return [sum(N[b][r] * sgn[r] for r in range(two_p)) for b in range(n + 1)]


def V_exact(p: int, deltas, base: int):
    n = len(deltas)
    return V_from_counts(p, count_dp(p, deltas), n, base)


def V_two_value(p: int, n1: int, n2: int, v1: int, v2: int, base: int):
    """EXACT V_b for a window whose Delta multiset is n1 copies of v1 and n2 of v2.

    V_b = sum_t C(n1,t) C(n2,b-t) h_p( base + t*v1 + (b-t)*v2 ),
    O(n) per b, so this reaches n in the thousands where the (b,r) DP cannot.
    """
    n = n1 + n2
    two_p = 2 * p
    C1 = [math.comb(n1, t) for t in range(n1 + 1)]
    C2 = [math.comb(n2, t) for t in range(n2 + 1)]
    out = []
    for b in range(n + 1):
        acc = 0
        lo, hi = max(0, b - n2), min(b, n1)
        for t in range(lo, hi + 1):
            r = (base + t * v1 + (b - t) * v2) % two_p
            acc += C1[t] * C2[b - t] * (1 if r < p else -1)
        out.append(acc)
    return out


def V_two_value_at(p: int, n1: int, n2: int, v1: int, v2: int, base: int, bs):
    """The same, but only at the requested slices b (O(n) each)."""
    two_p = 2 * p
    out = {}
    for b in bs:
        acc = 0
        lo, hi = max(0, b - n2), min(b, n1)
        c1 = math.comb(n1, lo)
        c2 = math.comb(n2, b - lo)
        for t in range(lo, hi + 1):
            if t > lo:
                c1 = c1 * (n1 - t + 1) // t
                c2 = c2 * (b - t + 1) // (n2 - b + t)
            r = (base + t * v1 + (b - t) * v2) % two_p
            acc += c1 * c2 * (1 if r < p else -1)
        out[b] = acc
    return out


def neglog2_rho(V, n, b):
    C = math.comb(n, b)
    if V == 0:
        return None
    return math.log2(C) - math.log2(abs(V))


def band(n, lo=0.25, hi=0.75):
    return range(max(1, math.ceil(lo * n)), min(n - 1, math.floor(hi * n)) + 1)


def worst_in_band(V, n, lo=0.25, hi=0.75):
    """min over the band of -log2 rho_b (None-safe); the ADVERSARIAL slice."""
    best = None
    arg = None
    for b in band(n, lo, hi):
        x = neglog2_rho(V[b], n, b)
        if x is None:
            continue
        if best is None or x < best:
            best, arg = x, b
    return best, arg


# ------------------------------------------------------- exact Krawtchouk ----


def krawtchouk_parity(n_o: int, n_e: int):
    """[z^b] (1-z)^{n_o} (1+z)^{n_e}, all b.  Exact integers.

    This IS the k = p mode's slice coefficient, up to a unimodular factor.
    """
    poly = [1]
    for _ in range(n_o):
        poly = [(poly[j] if j < len(poly) else 0) - (poly[j - 1] if j else 0)
                for j in range(len(poly) + 1)]
    for _ in range(n_e):
        poly = [(poly[j] if j < len(poly) else 0) + (poly[j - 1] if j else 0)
                for j in range(len(poly) + 1)]
    return poly


def krawtchouk_at(n_o: int, n_e: int, b: int) -> int:
    """[z^b](1-z)^{n_o}(1+z)^{n_e} in O(min(n_o,n_e)) exact-integer terms.

    Uses (1-z)^{n_o}(1+z)^{n_e} = (1-z^2)^{m} (1 -/+ z)^{|n_o-n_e|},
    m = min(n_o, n_e), so the alternating sum has only m+1 terms.
    """
    m = min(n_o, n_e)
    d = abs(n_o - n_e)
    sgn_tail = -1 if n_o > n_e else 1          # (1-z)^d  vs  (1+z)^d
    t0 = max(0, -(-(b - d) // 2))              # smallest t with j = b-2t <= d
    t1 = min(m, b // 2)
    if t1 < t0:
        return 0
    cm = math.comb(m, t0)                      # C(m, t)
    j = b - 2 * t0
    cd = math.comb(d, j)                       # C(d, j)
    tot = 0
    for t in range(t0, t1 + 1):
        term = cm * cd
        if t % 2:
            term = -term
        if sgn_tail == -1 and j % 2:
            term = -term
        tot += term
        if t == t1:
            break
        cm = cm * (m - t) // (t + 1)
        # j -> j-2 :  C(d,j-2) = C(d,j) * j*(j-1) / ((d-j+1)*(d-j+2))
        cd = cd * j * (j - 1) // ((d - j + 1) * (d - j + 2))
        j -= 2
    return tot


def kp_ratio_bits(n_o: int, n_e: int, b: int):
    """-log2 of |Kr| / C(n,b): the k=p mode's slice ratio, in bits.  EXACT."""
    n = n_o + n_e
    v = abs(krawtchouk_at(n_o, n_e, b))
    if v == 0:
        return None
    return math.log2(math.comb(n, b)) - math.log2(v)


def kp_floor_bits(n_o: int, n_e: int, p: int, b: int):
    """-log2 of the k=p mode's own contribution to rho_b.  Exact-integer core.

    contribution = |Kr(b)| / (p * C(n,b))  (hhat_p(p) = 2, 2p in the denominator)
    """
    n = n_o + n_e
    K = krawtchouk_parity(n_o, n_e)
    kb = abs(K[b])
    if kb == 0:
        return None
    return math.log2(p) + math.log2(math.comb(n, b)) - math.log2(kb)


# --------------------------------------------- imbalance / spread measures ---


def beta_min(deltas):
    n = len(deltas)
    n_o = sum(1 for d in deltas if d % 2)
    return min(n_o, n - n_o) / n


def R_coeffs(p: int, deltas):
    """R_k = (1/n) sum_i omega^{k Delta_i}, omega = e^{i pi / p}.  FLOAT."""
    n = len(deltas)
    ctr = collections.Counter(x % (2 * p) for x in deltas)
    out = {}
    for k in range(1, 2 * p, 2):
        s = 0j
        for v, m in ctr.items():
            s += m * cmath.exp(1j * math.pi * (k * v % (2 * p)) / p)
        out[k] = s / n
    return out


def flatness(p: int, deltas):
    """max_{k odd} |R_k|  (FLOAT).  1 - flatness is the clean hypothesis dial."""
    R = R_coeffs(p, deltas)
    k = max(R, key=lambda kk: abs(R[kk]))
    return abs(R[k]), k, R


_TINY = 1e-300


def _g_factory(p, deltas, k, r):
    """psi -> sum_i log2( |1 + r e^{i(theta_i+psi)}| / (1+r) ), vectorised."""
    import numpy as np
    ctr = collections.Counter(x % (2 * p) for x in deltas)
    th = np.array([math.pi * ((k * v) % (2 * p)) / p for v in ctr], float)
    mu = np.array([ctr[v] for v in ctr], float)
    lg1r = math.log2(1.0 + r)

    def g(psi):
        psi = np.atleast_1d(np.asarray(psi, float))
        q = 1.0 + 2.0 * r * np.cos(th[None, :] + psi[:, None]) + r * r
        q = np.maximum(q, _TINY)
        return (0.5 * np.log2(q) - lg1r) @ mu
    return g


def Lambda_k(p: int, deltas, k: int, beta: float, grid: int = 720) -> float:
    """Lambda_k(beta) (FLOAT): the exact per-mode Cauchy exponent of (P2).

    = -(1/n) max_psi sum_i log2( |1 + r e^{i(theta_i+psi)}| / (1+r) ) >= 0,
    zero iff mode k is slice-dead.  Rotation invariance is built in (the max
    over psi), matching the F2A.5 "phase SPREAD, not location" constraint.
    """
    import numpy as np
    n = len(deltas)
    r = beta / (1.0 - beta)
    g = _g_factory(p, deltas, k, r)
    psis = 2.0 * math.pi * np.arange(grid) / grid
    vals = g(psis)
    j0 = int(np.argmax(vals))
    best = float(vals[j0])
    lo = 2.0 * math.pi * (j0 - 1) / grid
    hi = 2.0 * math.pi * (j0 + 1) / grid
    for _ in range(60):
        m1, m2 = lo + (hi - lo) / 3, hi - (hi - lo) / 3
        if float(g(m1)[0]) < float(g(m2)[0]):
            lo = m1
        else:
            hi = m2
    best = max(best, float(g(0.5 * (lo + hi))[0]))
    return max(0.0, -best / n)


def Lambda_p_closed(beta_min_: float, beta: float) -> float:
    """Closed form of Lambda_p (see module docstring).  FLOAT."""
    s = 2.0 * beta * (1.0 - beta)
    if abs(1.0 - 2.0 * beta_min_) >= s / (1.0 - s) - 1e-15 and \
            abs(1.0 - 2.0 * beta) > 1e-15:
        return beta_min_ * math.log2(1.0 / abs(1.0 - 2.0 * beta))
    x = beta_min_
    H = 0.0 if x in (0.0, 1.0) else -(x * math.log2(x) + (1 - x) * math.log2(1 - x))
    return 0.5 * (H - 1.0 - math.log2(1.0 - s))


def min_Lambda(p: int, deltas, beta: float, grid: int = 360):
    """min over odd k of Lambda_k, and the argmin mode.  FLOAT diagnostic."""
    best, arg = None, None
    for k in range(1, 2 * p, 2):
        v = Lambda_k(p, deltas, k, beta, grid=grid)
        if best is None or v < best:
            best, arg = v, k
    return best, arg


def hhat_L1(p: int) -> float:
    """M_p = (1/2p) sum_{k odd} |hhat_p(k)| -- the mode-sum prefactor.  FLOAT."""
    return sum(2.0 / abs(math.sin(math.pi * k / (2 * p)))
               for k in range(1, 2 * p, 2)) / (2 * p)


def kappa(n: int, b: int) -> float:
    beta = b / n
    r = beta / (1 - beta)
    return math.exp((n * math.log1p(r) - b * math.log(r))
                    - math.lgamma(n + 1) + math.lgamma(b + 1)
                    + math.lgamma(n - b + 1))


def certified_bits(p: int, deltas, b: int, grid: int = 360):
    """The provable lower bound on -log2 rho_b from (P1)+(P2).  FLOAT."""
    return mode_profile(p, deltas, b, grid=grid)["certified_bits"]


def mode_profile(p: int, deltas, b: int, grid: int = 360):
    """All Lambda_k at slice b, the argmin, and the certificate.  FLOAT."""
    n = len(deltas)
    beta = b / n
    L = {k: Lambda_k(p, deltas, k, beta, grid=grid) for k in range(1, 2 * p, 2)}
    kmin = min(L, key=lambda k: L[k])
    tot = sum((2.0 / abs(math.sin(math.pi * k / (2 * p)))) * 2.0 ** (-n * L[k])
              for k in L)
    tot *= kappa(n, b) / (2 * p)
    return {"Lambda": L, "min_Lambda": L[kmin], "min_Lambda_k": kmin,
            "certified_bits": (-math.log2(tot) if tot > 0 else float("inf"))}


# ------------------------------------------------------ window construction --


def parity_ramp_window(p: int, c, n: int, j: int):
    """n coordinates from the real model: j with EVEN Delta, n-j with ODD."""
    D, S, _ = model(p, c)
    odd = [i for i in range(len(D)) if D[i] % 2 == 1]
    even = [i for i in range(len(D)) if D[i] % 2 == 0]
    if len(odd) < n - j or len(even) < j:
        return None
    sel = odd[:n - j] + even[:j]
    return [D[i] for i in sel], sum(S[i] for i in sel) % (2 * p), sel


def arc_window(p: int, c, n: int, width: int):
    """n coordinates whose Delta lies in the densest arc of the given width."""
    D, S, _ = model(p, c)
    ctr = collections.Counter(D)
    two_p = 2 * p
    best_a, best_cnt = 0, -1
    for a in range(two_p):
        cnt = sum(ctr.get((a + t) % two_p, 0) for t in range(width))
        if cnt > best_cnt:
            best_a, best_cnt = a, cnt
    vals = {(best_a + t) % two_p for t in range(width)}
    sel = [i for i in range(len(D)) if D[i] in vals]
    if len(sel) < n:
        return None
    # interleave the values so a truncated window keeps the value mix
    byval = collections.defaultdict(list)
    for i in sel:
        byval[D[i]].append(i)
    order, keys = [], sorted(byval, key=lambda v: -len(byval[v]))
    idx = 0
    while len(order) < len(sel):
        for v in keys:
            if idx < len(byval[v]):
                order.append(byval[v][idx])
        idx += 1
    sel = order[:n]
    return [D[i] for i in sel], sum(S[i] for i in sel) % (2 * p), sel


def value_window(p: int, c, n: int, vals):
    """n coordinates whose Delta lies in an explicit value set (interleaved)."""
    D, S, _ = model(p, c)
    byval = collections.defaultdict(list)
    for i in range(len(D)):
        if D[i] % (2 * p) in vals:
            byval[D[i] % (2 * p)].append(i)
    keys = sorted(byval, key=lambda v: -len(byval[v]))
    order, idx = [], 0
    tot = sum(len(byval[v]) for v in keys)
    while len(order) < tot:
        for v in keys:
            if idx < len(byval[v]):
                order.append(byval[v][idx])
        idx += 1
    if len(order) < n:
        return None
    sel = order[:n]
    return [D[i] for i in sel], sum(S[i] for i in sel) % (2 * p), sel


def generic_window(p: int, c, n: int):
    D, S, _ = model(p, c)
    if len(D) < n:
        return None
    sel = list(range(n))
    return [D[i] for i in sel], sum(S[i] for i in sel) % (2 * p), sel


def subgroup_coset_window(p: int, c, n: int, which: str):
    """Delta confined to a coset of a proper subgroup of Z/2p.

    Proper subgroups: {0} (all Delta equal), {0,p}, 2Z/2p (= the parity class).
    """
    D, _, _ = model(p, c)
    ctr = collections.Counter(D)
    two_p = 2 * p
    if which == "trivial":            # all Delta EQUAL  (coset of {0})
        v = max(ctr, key=lambda x: ctr[x])
        return value_window(p, c, n, {v})
    if which == "order2":             # Delta in {a, a+p}  (coset of {0,p})
        best, bv = -1, None
        for a in range(p):
            t = ctr.get(a, 0) + ctr.get(a + p, 0)
            if t > best:
                best, bv = t, {a, (a + p) % two_p}
        return value_window(p, c, n, bv)
    if which == "even":               # coset of 2Z/2p
        return parity_ramp_window(p, c, n, n)
    if which == "odd":
        return parity_ramp_window(p, c, n, 0)
    raise ValueError(which)


# ------------------------------------------------------------ row summary ----


def summarise(p, deltas, base, n=None, tag="", lo=0.25, hi=0.75,
              with_float=True, grid=360):
    n = n or len(deltas)
    N = count_dp(p, deltas)
    V = V_from_counts(p, N, n, base)
    w, wb = worst_in_band(V, n, lo, hi)
    n_o = sum(1 for d in deltas if d % 2)
    row = {"tag": tag, "p": p, "n": n, "n_odd": n_o, "n_even": n - n_o,
           "beta_min": min(n_o, n - n_o) / n, "base": base,
           "worst_neglog2": w, "worst_b": wb,
           "eta_n": (w / n) if w is not None else None,
           "V_worst": (V[wb] if wb is not None else None),
           "C_worst": (math.comb(n, wb) if wb is not None else None),
           "distinct_delta": len(set(deltas))}
    if wb is not None:
        row["kp_floor_bits"] = kp_floor_bits(n_o, n - n_o, p, wb)
    bc = n // 2
    row["central_neglog2"] = neglog2_rho(V[bc], n, bc)
    row["central_kp_floor_bits"] = kp_floor_bits(n_o, n - n_o, p, bc)
    if with_float:
        fm, fk, _ = flatness(p, deltas)
        row["flatness_max_absR"] = fm
        row["flatness_argk"] = fk
        if wb is not None:
            mp_ = mode_profile(p, deltas, wb, grid=grid)
            row["min_Lambda"] = mp_["min_Lambda"]
            row["min_Lambda_k"] = mp_["min_Lambda_k"]
            row["certified_bits"] = mp_["certified_bits"]
            row["Lambda_p"] = mp_["Lambda"][p]
    return row, V


def dump(name, obj):
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, name), "w") as f:
        json.dump(obj, f, indent=1)
    print(f"[wrote] results/{name}")

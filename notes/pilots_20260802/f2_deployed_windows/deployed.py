#!/usr/bin/env python3
"""F2 DEPLOYED WINDOWS -- does the actual tower's own window satisfy (H-flat)?

Pilot 2026-08-02, notes/pilots_20260802/f2_deployed_windows/.
Read-only imports from the two banked F2 pilots; nothing is written outside
this directory (sys.dont_write_bytecode is set before any import).

---------------------------------------------------------------- the window --
The F2 first-descent object (f2_carry_reachability/f2model.py docstring;
f2_slice_coefficients/slicecore.py `instance`; f2_parity_boundary/boundary.py
`model`) is fixed by THREE data:

    p           odd prime, F_{p^2} = F_p(w), w^2 = N (N = least non-residue),
    n_ord       the order of the subgroup mu_{n_ord} <= F_{p^2}^*
                (n_ord | p^2-1, n_ord even, n_ord does not divide p-1),
    c           the frequency, c in F_{p^2}^*.

The DEPLOYED WINDOW is then NOT a free choice: it is the complete set of
genuine Frobenius conjugate pairs {y, y^p} of mu_{n_ord},

    m = (n_ord - gcd(n_ord, p-1)) / 2  coordinates,

one orientation variable tau_i per pair (f2model.py, FIRST-DESCENT
ABSTRACTION).  Coordinate i carries

    s_i^+ = Tr(c y_i), s_i^- = Tr(c y_i^p)      (least residues in [0,p))
    sigma_i^pm = s_i^pm + p*[2 s_i^pm > p]      (mod 2p)
    Delta_i = sigma_i^+ - sigma_i^-             (mod 2p)
    base    = sum_i sigma_i^-.

The prior pilots always instantiated n_ord = admissible_orders(p)[-1] = p^2-1
(the FULL group) and then CARVED sub-windows out of it (generic_window,
arc_window, value_window, ...).  Those carved windows are NOT deployed: the
tower processes the whole pair set of whatever mu_{n_ord} the row carries.
This module separates the two.

------------------------------------------------------- the exact flat bound --
For odd k, omega^{k(x+p)} = e^{i pi k} omega^{kx} = -omega^{kx}.  So the two
Delta values of any fixed residue class mod p CANCEL against each other in
R_k = (1/m) sum_i omega^{k Delta_i}, for EVERY odd k at once.  Grouping the
multiset by Delta mod p:

    R_k = (1/m) sum_{d in Z/p} c_d * omega^{k x_d},
    c_d := #{i : Delta_i = d mod p, Delta_i even}
         - #{i : Delta_i = d mod p, Delta_i odd},
    x_d := the even element of {d, d+p} in Z/2p.

Hence the EXACT, mode-uniform, integer certificate

    (DEF)   max_{k odd} |R_k|  <=  D/m,   D := sum_{d in Z/p} |c_d|,
    (FLAT)  flat := 1 - max_{k odd} |R_k|  >=  1 - D/m.

D is a nonnegative integer computed from the exact Delta multiset; no floats.
D/m is the "signed parity defect density" of the window.  Note c_p-classes
with c_d = 0 (a residue class split EXACTLY evenly between the two parities)
contribute nothing at any frequency -- perfect local cancellation.
"""

from __future__ import annotations

import cmath
import collections
import json
import math
import os
import sys
from fractions import Fraction

sys.dont_write_bytecode = True  # never litter the imported pilots' directories

_HERE = os.path.dirname(os.path.abspath(__file__))
_PILOTS = os.path.dirname(_HERE)
for _d in (os.path.join(_PILOTS, "f2_slice_coefficients"),
           os.path.join(_PILOTS, "f2_parity_boundary"),
           os.path.join(_PILOTS, "f2_carry_reachability")):
    if _d not in sys.path:
        sys.path.append(_d)

from slicecore import (  # noqa: E402
    Fp2, admissible_orders, pair_reps, residues, sigma_of, Delta_of,
    divisors, half_flag,
)

RESULTS = os.path.join(_HERE, "results")

TARGET_THIRD = Fraction(1, 3)
TARGET_43 = Fraction(1, 43)
# (H-flat) thresholds from F2A.5b: flat >= eta*ln2/(beta(1-beta)); at the
# adversarial slice beta = 1/4 that is eta / 0.270517...
BETA_ADV = 0.25


# --------------------------------------------------------------- the window --

_CACHE: dict = {}


def deployed_window(p: int, n_ord: int, c):
    """Exact (Delta list, base, m, reps) for the deployed window (p, n_ord, c).

    The FULL pair set of mu_{n_ord} -- no selection whatsoever.
    """
    key = (p, n_ord, tuple(c))
    if key in _CACHE:
        return _CACHE[key]
    F = Fp2.make(p)
    mu = F.subgroup(n_ord)
    reps = pair_reps(F, mu)
    loc = [residues(F, c, y) for y in reps]
    D = Delta_of(p, loc)
    sig = sigma_of(p, loc)
    base = sum(s[1] for s in sig) % (2 * p)
    out = (D, base, len(reps), reps, loc)
    _CACHE[key] = out
    return out


def deployed_orders(p: int) -> list[int]:
    """Every admissible subgroup order: n even, n | p^2-1, n does not divide p-1."""
    return admissible_orders(p)


# ---------------------------------------------------- exact flat certificate --


def parity_classes(p: int, deltas):
    """c_d for d in Z/p (exact integers) and the even representative x_d."""
    two_p = 2 * p
    cd = [0] * p
    for x in deltas:
        x %= two_p
        d = x % p
        cd[d] += 1 if x % 2 == 0 else -1
    xd = [(d if d % 2 == 0 else d + p) for d in range(p)]
    return cd, xd


def defect(p: int, deltas) -> int:
    """D = sum_d |c_d|.  EXACT integer.  max_k |R_k| <= D/n."""
    cd, _ = parity_classes(p, deltas)
    return sum(abs(v) for v in cd)


def flat_bound(p: int, deltas) -> Fraction:
    """1 - D/n as an EXACT rational lower bound on flat."""
    n = len(deltas)
    return Fraction(n - defect(p, deltas), n)


# --------------------------------------------------- measured flatness (float) --


def R_coeffs(p: int, deltas):
    """R_k = (1/n) sum_i omega^{k Delta_i}, omega = e^{i pi/p}.  FLOAT."""
    n = len(deltas)
    ctr = collections.Counter(x % (2 * p) for x in deltas)
    items = list(ctr.items())
    out = {}
    for k in range(1, 2 * p, 2):
        s = 0j
        for v, mm in items:
            s += mm * cmath.exp(1j * math.pi * ((k * v) % (2 * p)) / p)
        out[k] = s / n
    return out


def measured_flat(p: int, deltas):
    """(flat, argmax k, max|R_k|).  FLOAT diagnostic."""
    R = R_coeffs(p, deltas)
    k = max(R, key=lambda kk: abs(R[kk]))
    return 1.0 - abs(R[k]), k, abs(R[k])


def beta_min(deltas):
    n = len(deltas)
    n_o = sum(1 for d in deltas if d % 2)
    return Fraction(min(n_o, n - n_o), n)


# -------------------------------------------------------- Lambda (float, B6) --

_TINY = 1e-300


def Lambda_k(p: int, ctr, n: int, k: int, beta: float, grid: int = 720) -> float:
    """Per-mode Cauchy exponent (f2_parity_boundary/boundary.py P2).  FLOAT."""
    import numpy as np
    r = beta / (1.0 - beta)
    th = np.array([math.pi * ((k * v) % (2 * p)) / p for v in ctr], float)
    mu = np.array([ctr[v] for v in ctr], float)
    lg1r = math.log2(1.0 + r)

    def g(psi):
        psi = np.atleast_1d(np.asarray(psi, float))
        q = 1.0 + 2.0 * r * np.cos(th[None, :] + psi[:, None]) + r * r
        q = np.maximum(q, _TINY)
        return (0.5 * np.log2(q) - lg1r) @ mu

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


def min_Lambda(p: int, deltas, beta: float, grid: int = 360):
    """min over odd k of Lambda_k = eta, and the argmin.  FLOAT diagnostic."""
    two_p = 2 * p
    ctr = collections.Counter(x % two_p for x in deltas)
    n = len(deltas)
    best, arg = None, None
    for k in range(1, two_p, 2):
        v = Lambda_k(p, ctr, n, k, beta, grid=grid)
        if best is None or v < best:
            best, arg = v, k
    return best, arg


def M_p(p: int) -> float:
    return sum(2.0 / abs(math.sin(math.pi * k / (2 * p)))
               for k in range(1, 2 * p, 2)) / (2 * p)


def M_p_asym(p: int) -> float:
    """(2 ln2/pi) log2 p + 0.9626 -- the banked asymptotic (F2A.5b B8)."""
    return (2.0 * math.log(2) / math.pi) * math.log2(p) + 0.96257


def kappa(n: int, b: int) -> float:
    beta = b / n
    r = beta / (1 - beta)
    return math.exp((n * math.log1p(r) - b * math.log(r))
                    - math.lgamma(n + 1) + math.lgamma(b + 1)
                    + math.lgamma(n - b + 1))


def startup_deficit(p: int, n: int, b: int | None = None) -> float:
    """log2 M_p + log2 kappa(n,b) -- the bits the linear term must repay."""
    b = b if b is not None else n // 4
    return math.log2(M_p_asym(p)) + math.log2(kappa(n, b))


# ------------------------------------------------------------------- io -----


def dump(name, obj):
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, name), "w") as f:
        json.dump(obj, f, indent=1, default=str)
    print(f"[wrote] results/{name}")

"""lp_lib -- a self-contained two-phase dense simplex (numpy only) plus the
two LP builders of D3.  Round-22 f2_rlocality pilot, DRAFT ONLY.

scipy.optimize is unusable in this sandbox (import does not complete inside
the ramguard wall limit), so the LP solver here is written from scratch and
smoke-tested against closed-form optima in verify_d3.py.
"""

import math
import numpy as np
from itertools import product


# --------------------------------------------------------------- the simplex
def _pivot(T, basis, r, c):
    T[r] /= T[r, c]
    col = T[:, c].copy()
    col[r] = 0.0
    T -= np.outer(col, T[r])
    basis[r] = c


def _run(T, basis, nvar, tol=1e-11, maxit=200000):
    m = T.shape[0] - 1
    stall = 0
    last = np.inf
    for it in range(maxit):
        red = T[m, :nvar]
        neg = np.where(red < -tol)[0]
        if neg.size == 0:
            return True
        if stall > 60:                       # Bland's rule: guaranteed finite
            c = int(neg[0])
        else:
            c = int(neg[np.argmin(red[neg])])
        colv = T[:m, c]
        pos = np.where(colv > tol)[0]
        if pos.size == 0:
            return False                     # unbounded
        ratios = T[:m, -1][pos] / colv[pos]
        r = int(pos[np.argmin(ratios)])
        _pivot(T, basis, r, c)
        obj = T[m, -1]
        if abs(obj - last) < 1e-14:
            stall += 1
        else:
            stall = 0
        last = obj
    raise RuntimeError("simplex iteration limit")


def solve_max(cobj, A, b, tol=1e-11):
    """max cobj.x  s.t.  A x = b, x >= 0.  Returns (value, x)."""
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float).copy()
    cobj = np.asarray(cobj, dtype=float)
    m, n = A.shape
    A = A.copy()
    flip = b < 0
    A[flip] *= -1.0
    b[flip] *= -1.0

    T = np.zeros((m + 1, n + m + 1))
    T[:m, :n] = A
    T[:m, n:n + m] = np.eye(m)
    T[:m, -1] = b
    T[m, :n] = -A.sum(axis=0)
    T[m, -1] = -b.sum()
    basis = list(range(n, n + m))
    if not _run(T, basis, n + m, tol):
        raise RuntimeError("phase 1 failed")
    if T[m, -1] < -1e-7:
        raise RuntimeError("infeasible (phase-1 residual %.3e)" % (-T[m, -1]))

    # phase 2: minimise -cobj over the original columns only
    c2 = np.zeros(n + m)
    c2[:n] = -cobj
    T[m, :] = 0.0
    T[m, :n + m] = c2
    for i, bi in enumerate(basis):
        if c2[bi] != 0.0:
            T[m, :] -= c2[bi] * T[i, :]
    if not _run(T, basis, n, tol):
        raise RuntimeError("phase 2 unbounded")
    x = np.zeros(n)
    for i, bi in enumerate(basis):
        if bi < n:
            x[bi] = T[i, -1]
    # phase 2 minimises c2.x = -cobj.x, and the tableau's RHS entry carries
    # MINUS the current objective, so T[m,-1] = -min(-cobj.x) = max cobj.x
    return T[m, -1], x


# ------------------------------------------------- D3 builder 1: the FULL LP
def fold_classes(p):
    """Folded value classes of F_p under c ~ -c (d is even), with weights."""
    nc = (p + 1) // 2
    w = [1.0 / p] + [2.0 / p] * (nc - 1)
    dv = [-2.0 * math.log2(abs(math.cos(math.pi * j / p))) for j in range(nc)]
    return nc, w, dv


def _compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in _compositions(total - first, parts - 1):
            yield (first,) + rest


def _ff(n, k):
    r = 1.0
    for i in range(k):
        r *= (n - i)
    return r


def build_full(p, S, k):
    """Constraint system of the FULL k-LOCAL LP at (p,S), independent of c.

    Only the types with sum(t) = k are imposed: summing such a constraint
    over one coordinate gives the corresponding sum(t) = k-1 constraint, so
    the lower orders are implied.  The normalisation is added explicitly.
    Returns (A, b, cost, nstates).
    """
    nc, w, dv = fold_classes(p)
    states = np.array(list(_compositions(S, nc)), dtype=np.int64)
    ns = states.shape[0]
    cost = states @ np.array(dv)

    FF = np.zeros((k + 1, S + 1))            # FF[j, n] = (n)_j
    for j in range(k + 1):
        for n in range(S + 1):
            FF[j, n] = _ff(n, j)

    types = list(_compositions(k, nc))
    m = len(types) + 1
    A = np.zeros((m, ns))
    b = np.zeros(m)
    A[0, :] = 1.0                            # normalisation
    b[0] = 1.0
    fS = _ff(S, k)
    for ti, t in enumerate(types):
        v = np.ones(ns)
        rhs = 1.0
        for j in range(nc):
            if t[j]:
                v *= FF[t[j], states[:, j]]
                rhs *= w[j] ** t[j]
        A[ti + 1, :] = v / fS
        b[ti + 1] = rhs
    return A, b, cost, ns


def full_lp_at(A, b, cost, S, c):
    """OPT_k(c) = max Pr[cost <= (1-c)S] for a pre-built constraint system."""
    obj = (cost <= (1.0 - c) * S + 1e-12).astype(float)
    val, x = solve_max(obj, A, b)
    return val


# ---------------------------------------------- D3 builder 2: the PATTERN LP
def pattern_lp(S, k, rho):
    """OPTPAT_k(rho,S) = max{ Pr[N=S] : E[(N)_j/(S)_j] = rho^j, j = 0..k }
    over laws of N on {0..S}.  By the LIFTING LEMMA (PROOFS section 5) every
    feasible point lifts to a k-wise-uniform law on F_p^S with
    Pr[all coordinates in A] = Pr[N=S], rho = |A|/p."""
    ns = S + 1
    A = np.zeros((k + 1, ns))
    b = np.zeros(k + 1)
    for j in range(k + 1):
        fS = _ff(S, j)
        b[j] = rho ** j
        for n in range(ns):
            A[j, n] = _ff(n, j) / fS
    obj = np.zeros(ns)
    obj[S] = 1.0
    val, x = solve_max(obj, A, b)
    return val

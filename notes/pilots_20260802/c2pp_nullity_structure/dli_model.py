#!/usr/bin/env python3
"""C2'' pilot -- the DLI b2b nested tower, reconstructed from first principles.

SETTING (from C2PP_POSED_20260710.md and the archived level-2 falsifier
`archive/.../b2b_primitive_core/notes/verify_level2_tower.py`):

  q prime, n = 2^s, n | q-1, zeta = primitive n-th root in F_q.
  A subset of Z/n (indicator x in {0,1}^n) is t-NULL iff
      p_r(x) = sum_i x_i zeta^{r i} = 0   for r = 1..t.

DYADIC DESCENT.  h_j = n/2^j.  m_0 = x, and for j >= 0
      m_{j+1}(i) = m_j(i) + m_j(i + h_{j+1}),      i in Z/h_{j+1}
      d_j(i)     = m_j(i) - m_j(i + h_{j+1}).
Because zeta_{h_j}^{r(i+h_{j+1})} = (-1)^r zeta_{h_j}^{r i}:
  * r EVEN  ->  the constraint descends verbatim to level j+1;
  * r ODD   ->  the constraint becomes  sum_i d_j(i) zeta_{h_j}^{r i} = 0.
Iterating, constraint r is consumed at level j = v_2(r).  Hence

  BLOCK j (the pose's "level j") owns  U_j = {odd u : u*2^j <= t},
  L_j = |U_j| = ceil(floor(t/2^j)/2) = the pose's ell_j,  sum_j L_j = t,
  and it is a linear system in the level-j skew d_j on Z/h_{j+1} with matrix
  columns v_i = (zeta_{h_j}^{u i})_{u in U_j}.
  x is t-null  <=>  every block constraint holds.            (exact, tested)

STATE-DEPENDENT DOMAIN.  Given m_{j+1}, the pair (m_j(i), m_j(i+h_{j+1})) is
determined by (m_{j+1}(i), d_j(i)); admissibility 0 <= m_j <= 2^j forces
    d_j(i) in {-c_i, -c_i+2, ..., c_i},  c_i = min(M_i, 2^{j+1}-M_i),
so the junction-j domain is a product of (c_i + 1)-element sets, and the
EFFECTIVE SUPPORT is
    S_j = { i : 0 < m_{j+1}(i) < 2^{j+1} }        (the unsaturated cells).
At j = 0 this is exactly the archived "singleton set G" and the domain is
{+-1}^G, i.e. skewcount(G).

CROSS-JUNCTION NULLITY.  Local rank r_j = rank{v_i : i in S_j};
delta_j = L_j - r_j; delta = sum_j delta_j.
"""

from __future__ import annotations

from fractions import Fraction

import sympy

from nullity import rref_rank


# ---------------------------------------------------------------- field helpers
def get_zeta(q, n):
    """Deterministic primitive n-th root (same rule as the archived verifier)."""
    g = int(sympy.primitive_root(q))
    z = pow(g, (q - 1) // n, q)
    assert pow(z, n, q) == 1 and pow(z, n // 2, q) != 1
    return int(z)


def blocks(t):
    """U_j = odd u with u*2^j <= t, for every block j that owns a constraint."""
    out = []
    j = 0
    while 2**j <= t:
        out.append([u for u in range(1, t // 2**j + 1, 2)])
        j += 1
    return out


def block_matrix(q, n, t, j):
    """Junction-j column set: v_i = (zeta_{h_j}^{u i})_{u in U_j}, i in Z/h_{j+1}."""
    U = blocks(t)[j]
    zeta = get_zeta(q, n)
    zj = pow(zeta, 2**j, q)               # primitive h_j-th root
    hj1 = n // 2**(j + 1)
    return [tuple(pow(zj, (u * i) % (n // 2**j), q) for u in U) for i in range(hj1)]


# ---------------------------------------------------------------- descent
def levels_of(x, n, depth):
    """m_0..m_depth as tuples, from the indicator bitmask x."""
    m = [ (x >> i) & 1 for i in range(n) ]
    out = [tuple(m)]
    h = n
    for _ in range(depth):
        h //= 2
        m = [m[i] + m[i + h] for i in range(h)]
        out.append(tuple(m))
    return out


def supports(x, n, t):
    """|S_j| for every block j (S_j = unsaturated level-(j+1) cells)."""
    B = blocks(t)
    lev = levels_of(x, n, len(B))
    return [sum(1 for M in lev[j + 1] if 0 < M < 2**(j + 1)) for j in range(len(B))]


def delta_of(x, n, t):
    B = blocks(t)
    S = supports(x, n, t)
    return sum(max(0, len(B[j]) - min(len(B[j]), S[j])) for j in range(len(B)))


def delta_from_supports(S, t):
    B = blocks(t)
    return sum(max(0, len(B[j]) - S[j]) for j in range(len(B)))


# ---------------------------------------------------------------- power sums
def psums(x, n, t, q, zeta):
    out = [0] * t
    for i in range(n):
        if (x >> i) & 1:
            for r in range(1, t + 1):
                out[r - 1] = (out[r - 1] + pow(zeta, (r * i) % n, q)) % q
    return tuple(out)


def half_table(n, t, q, zeta, idx):
    """All partial power-sum vectors over the coordinates in idx (2^|idx| rows)."""
    rows = [((0,) * t, 0)]
    for i in idx:
        c = tuple(pow(zeta, (r * i) % n, q) for r in range(1, t + 1))
        bit = 1 << i
        rows = rows + [(tuple((a + b) % q for a, b in zip(v, c)), msk | bit)
                       for v, msk in rows]
    return rows


def count_null(n, t, q, rows_wanted=None, collect=False):
    """#{x in {0,1}^n : p_r(x)=0 for r in rows_wanted} by meet-in-the-middle.

    rows_wanted = 1-based list of r's (default: all of 1..t).  If collect,
    also return the list of solution bitmasks.
    """
    zeta = get_zeta(q, n)
    sel = [r - 1 for r in (rows_wanted if rows_wanted else range(1, t + 1))]
    L = half_table(n, t, q, zeta, range(0, n // 2))
    R = half_table(n, t, q, zeta, range(n // 2, n))
    d = {}
    for v, msk in L:
        key = tuple(v[s] for s in sel)
        d.setdefault(key, []).append(msk)
    total = 0
    sols = []
    for v, msk in R:
        key = tuple((-v[s]) % q for s in sel)
        lst = d.get(key)
        if not lst:
            continue
        total += len(lst)
        if collect:
            sols.extend(m | msk for m in lst)
    return (total, sols) if collect else total


# ---------------------------------------------------------------- junction counts
def junction_domain_and_count(q, n, t, j, Mvec):
    """(domain size, #admissible d satisfying junction j) for level-(j+1) state Mvec."""
    U = blocks(t)[j]
    L = len(U)
    cols = block_matrix(q, n, t, j)
    dom = 1
    dp = {(0,) * L: 1}
    for i, M in enumerate(Mvec):
        c = min(M, 2**(j + 1) - M)
        vals = list(range(-c, c + 1, 2))
        dom *= len(vals)
        nxt = {}
        for key, w in dp.items():
            for dv in vals:
                nk = tuple((key[a] + dv * cols[i][a]) % q for a in range(L))
                nxt[nk] = nxt.get(nk, 0) + w
        dp = nxt
    return dom, dp.get((0,) * L, 0)


def junction_rho(q, n, t, j, Mvec):
    dom, cnt = junction_domain_and_count(q, n, t, j, Mvec)
    L = len(blocks(t)[j])
    return Fraction(cnt * q**L, dom)


def local_rank(q, n, t, j, S):
    """rank{v_i : i in S} over F_q."""
    cols = block_matrix(q, n, t, j)
    return rref_rank([cols[i] for i in S], q)

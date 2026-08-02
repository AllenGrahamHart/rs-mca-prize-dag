#!/usr/bin/env python3
"""C2'' pilot -- exact cross-junction nullity core.

Model (abstract prototype, exactly as the Brief-2 adversarial audit states it):

  * latent U uniform on F_q^m;
  * J local constraint systems, junction j carrying a set of linear forms
    Lam_j subset (F_q^m)^*, with local rank r_j = dim span(Lam_j);
  * local factor  Y_j = q^{r_j} * 1[ l(U) = 0 for every l in Lam_j ];
    E[Y_j] = q^{r_j} q^{-r_j} = 1;
  * delta = sum_j r_j - rank( union_j Lam_j )  >= 0;
  * R = E[prod_j Y_j] = q^{sum r_j} q^{-rank(union)} = q^delta.       (IDENTITY)

The rank-1 case (every junction a single nonzero form) is the audit's
"E[prod q 1[l_i=0]] = q^(m-rank)" prototype.  Everything here is exact
integer / Fraction arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


# --------------------------------------------------------------- F_q linear algebra
def rref_rank(rows, q):
    """Exact rank over F_q (q prime) of a list of row vectors (tuples of int)."""
    rows = [list(r) for r in rows]
    if not rows:
        return 0
    ncols = len(rows[0])
    piv = 0
    for c in range(ncols):
        sel = None
        for i in range(piv, len(rows)):
            if rows[i][c] % q:
                sel = i
                break
        if sel is None:
            continue
        rows[piv], rows[sel] = rows[sel], rows[piv]
        inv = pow(rows[piv][c], q - 2, q)
        rows[piv] = [(v * inv) % q for v in rows[piv]]
        for i in range(len(rows)):
            if i != piv and rows[i][c] % q:
                f = rows[i][c]
                rows[i] = [(a - f * b) % q for a, b in zip(rows[i], rows[piv])]
        piv += 1
        if piv == len(rows):
            break
    return piv


def gf2_rank(values):
    """Exact rank over F_2 of a list of bitmask-encoded vectors."""
    basis = {}
    rank = 0
    for x0 in values:
        x = x0
        while x:
            p = x.bit_length() - 1
            if p in basis:
                x ^= basis[p]
            else:
                basis[p] = x
                rank += 1
                break
    return rank


# --------------------------------------------------------------- abstract model
class JunctionSystem:
    """J local constraint systems on a common latent F_q^m."""

    def __init__(self, q, m, locals_):
        self.q = q
        self.m = m
        self.locals = [list(map(tuple, L)) for L in locals_]

    def local_ranks(self):
        return [rref_rank(L, self.q) for L in self.locals]

    def global_rank(self):
        allrows = [r for L in self.locals for r in L]
        return rref_rank(allrows, self.q)

    def delta(self):
        return sum(self.local_ranks()) - self.global_rank()

    def R_bruteforce(self):
        """R = E[prod_j Y_j], exhaustively over F_q^m.  Exact Fraction."""
        q, m = self.q, self.m
        rs = self.local_ranks()
        hits = 0
        for u in product(range(q), repeat=m):
            ok = True
            for L in self.locals:
                for row in L:
                    if sum(a * b for a, b in zip(row, u)) % q:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                hits += 1
        return Fraction(q ** sum(rs) * hits, q ** m)

    def R_identity(self):
        return Fraction(self.q) ** self.delta()


def moment_curve_columns(q, dim, nodes):
    """Columns (1, a, a^2, ..., a^{dim-1}) for a in nodes -- as ROW forms."""
    return [tuple(pow(a, e, q) for e in range(dim)) for a in nodes]

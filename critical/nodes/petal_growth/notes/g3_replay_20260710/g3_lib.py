"""Fresh replay library for the fifth E22 branch (minimal-scale accounting).

Independent implementation (do not import repo code).

Conventions (matching background/nodes/e22_dyadic_minimal_scale_selector/verify.py):
- domain = Z_n, n = 2^m
- an M-fiber (M | n) is an arithmetic progression {r, r+n/M, ...} of size M;
  there are n/M of them (residue classes mod step, step = n/M)
- B_M(R) = R minus the union of full M-fibers contained in R
- eligible scales: dyadic M with t < M <= n
- admissible at M: |B_M(R)| < M
"""

from __future__ import annotations

from functools import lru_cache
from math import comb


def dyadic_scales(n: int) -> list[int]:
    out, m = [], 1
    while m <= n:
        out.append(m)
        m *= 2
    return out


def eligible_scales(n: int, t: int) -> list[int]:
    return [m for m in dyadic_scales(n) if m > t]


@lru_cache(maxsize=None)
def fiber_masks(n: int, M: int) -> tuple[int, ...]:
    step = n // M
    out = []
    for r in range(step):
        f = 0
        for x in range(r, n, step):
            f |= 1 << x
        out.append(f)
    return tuple(out)


def full_fiber_masks(n: int, M: int, mask: int) -> list[int]:
    return [f for f in fiber_masks(n, M) if mask & f == f]


def tail_mask(n: int, M: int, mask: int) -> int:
    u = 0
    for f in fiber_masks(n, M):
        if mask & f == f:
            u |= f
    return mask & ~u


def tail_size(n: int, M: int, mask: int) -> int:
    return tail_mask(n, M, mask).bit_count()


def admissible(n: int, M: int, mask: int) -> bool:
    return tail_size(n, M, mask) < M


def admissible_set(n: int, t: int, mask: int) -> list[int]:
    return [M for M in eligible_scales(n, t) if admissible(n, M, mask)]


def minimal_scale(n: int, t: int, mask: int) -> int | None:
    a = admissible_set(n, t, mask)
    return min(a) if a else None


def tail_criterion(n: int, t: int, mask: int, M: int) -> bool:
    """Statement of e22_minimal_scale_tail_criterion, ELIGIBLE-scale reading."""
    if not admissible(n, M, mask):
        return False
    return all(
        tail_size(n, Mp, mask) >= Mp
        for Mp in eligible_scales(n, t)
        if Mp < M
    )


def residual_stats(n: int, Mi: int, Mj: int, mask: int) -> tuple[int, int, int]:
    """(c, r, b): #complete Mj-parents, #selected Mi-fibers in incomplete
    parents, |B_Mi|.  Parent of Mi-fiber residue r (mod n/Mi) is the Mj-fiber
    residue r mod n/Mj."""
    stepi, stepj = n // Mi, n // Mj
    sel = [r for r in range(stepi)
           if mask & fiber_masks(n, Mi)[r] == fiber_masks(n, Mi)[r]]
    selset = set(sel)
    q = Mj // Mi
    complete_parents = 0
    r_incomplete = 0
    for pr in range(stepj):
        children = [pr + k * stepj for k in range(q)]
        nsel = sum(1 for c in children if c in selset)
        if nsel == q:
            complete_parents += 1
        else:
            r_incomplete += nsel
    b = tail_size(n, Mi, mask)
    return complete_parents, r_incomplete, b


# ---------- generating function of e22_residual_profile_generating_function

def gf_counts(n: int, Mi: int, Mj: int) -> dict[tuple[int, int, int], int]:
    """coefficient formula: [(c,r,b)] -> [u^c z^r] G_q(u,z)^P * [x^b] H_i(x)^(Pq-cq-r)."""
    P, q = n // Mj, Mj // Mi
    # G_q(u,z)^P as dict (c, r) -> coeff
    G: dict[tuple[int, int], int] = {}
    # single parent: u  or  z^s with binom(q,s), s in 0..q-1
    single = {(1, 0): 1}
    for s in range(q):
        single[(0, s)] = single.get((0, s), 0) + comb(q, s)
    acc = {(0, 0): 1}
    for _ in range(P):
        nxt: dict[tuple[int, int], int] = {}
        for (c1, r1), v1 in acc.items():
            for (c2, r2), v2 in single.items():
                k = (c1 + c2, r1 + r2)
                nxt[k] = nxt.get(k, 0) + v1 * v2
        acc = nxt
    G = acc
    # H_i(x)^e coefficients, e up to P*q
    H = [comb(Mi, a) for a in range(Mi)]  # a = 0..Mi-1

    @lru_cache(maxsize=None)
    def hpow(e: int) -> tuple[int, ...]:
        if e == 0:
            return (1,)
        prev = hpow(e - 1)
        out = [0] * (len(prev) + Mi - 1)
        for i, v in enumerate(prev):
            if v:
                for a, h in enumerate(H):
                    out[i + a] += v * h
        return tuple(out)

    out: dict[tuple[int, int, int], int] = {}
    for (c, r), g in G.items():
        e = P * q - c * q - r
        hp = hpow(e)
        for b, hv in enumerate(hp):
            if hv:
                out[(c, r, b)] = out.get((c, r, b), 0) + g * hv
    return out


# ---------- weights

def w_one(mask: int, n: int) -> int:
    return 1


def w_pseudo(mask: int, n: int) -> int:
    # deterministic, nonconstant, nonnegative
    x = mask * 2654435761 % (1 << 32)
    return 1 + (x % 13)


def w_toy(mask: int, n: int) -> int:
    # the toy weight from the payload verifier
    alternating = sum(1 << i for i in range(0, n, 2))
    return 1 + mask.bit_count() + 2 * (mask & alternating).bit_count() + mask % 7


WEIGHTS = {"w1": w_one, "wpseudo": w_pseudo, "wtoy": w_toy}

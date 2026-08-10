#!/usr/bin/env python3
"""c2pp_falsifier_redesign -- shared library (round 25).

REUSES the round-24 instrument verbatim (PREREG P0-g): every census
primitive is imported from notes/pilots_20260808/c2pp_gb_probe/gb_probe.py.
Nothing in that directory is written or modified.

Adds only: the closed forms registered in PREREG P3 (C-1..C-3), the
telescoping-lemma evaluation of R3_W (PREREG P1), and the cost model.
Stdlib only.  Run under tools/ramguard.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# ROUND-26 PIN (freeze_tail_law): absolute path to round 24's instrument, as
# briefed.  Nothing in that directory, nor in round 25's, is written.
R24 = "/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260808/c2pp_gb_probe"
sys.path.insert(0, R24)

from gb_probe import (                                          # noqa: E402
    blocks, level_vectors, junction_vectors, mitm_null_count,
    binom_alpha, skew_alpha, subset_alpha, flat_alpha, get_zeta,
    is_prime, log2_int, log2_ratio, positive_control, BANKED_F2B_NULL,
)

# ------------------------------------------------------------------ closed forms


def sigma(u, M):
    """sigma(u,M) = sum_{c=0}^{u} C(u,c)^M   (PREREG P2)."""
    return sum(math.comb(u, c) ** M for c in range(u + 1))


def Zinf(n, t, lev):
    """C-1: the e-PERIODIC frozen stratum, e = n/(2t)."""
    e = n // (2 * t)
    T = t // 2 ** lev
    u = 2 ** lev
    assert T >= 1 and n % (2 * t) == 0
    return sigma(u, 2 * T) ** e


def Cinf(n, t):
    """C-1: the frozen coset/subset census = 2^e."""
    return 2 ** (n // (2 * t))


def Binf(n, t, j):
    """C-2: the block marginal has only the zero skew frozen."""
    u = 2 ** (j + 1)
    h1 = n // 2 ** (j + 1)
    return math.comb(u, u // 2) ** h1


def c_k(k):
    """c_k = 2^k - log2 C(2^k, 2^{k-1}); c_0 := 1  (PREREG P2).

    Exact for k <= 20; beyond that the exact binomial is unrepresentable and
    we use  C(2u,u) = 4^u/sqrt(pi u) * (1 - 1/(8u) + ...),  u = 2^{k-1}."""
    if k == 0:
        return 1.0
    if k <= 20:
        return 2 ** k - log2_int(math.comb(2 ** k, 2 ** (k - 1)))
    u = 2.0 ** (k - 1)
    return 0.5 * math.log2(math.pi * u) - math.log2(1 - 1 / (8 * u))


def log2_sigma(u, M):
    """log2 sum_{c=0}^{u} C(u,c)^M, valid for u far beyond math.comb's reach.

    Factor out the central term and sum the (rapidly decaying) ratios in log
    space using lgamma; the summation window is where the ratio exceeds
    2^-80, so the truncation error is below the printing precision."""
    if u == 1:
        return 1.0
    if u <= 4096 and M <= 64:
        return log2_int(sum(math.comb(u, c) ** M for c in range(u + 1)))
    L2 = math.log(2.0)

    def lg2C(uu, c):
        return (math.lgamma(uu + 1) - math.lgamma(c + 1)
                - math.lgamma(uu - c + 1)) / L2
    cen = lg2C(u, u // 2)
    tot, d = 1.0, 1
    while True:
        r = M * (lg2C(u, u // 2 + d) - cen)
        if r < -80 or u // 2 + d > u:
            break
        tot += 2.0 * (2.0 ** r)
        d += 1
        if d > 4_000_000:
            break
    return M * cen + math.log2(tot)


def S_m(m):
    return sum(c_k(k) * 2.0 ** (-k) for k in range(1, m + 1))


def R3inf_full(n, t):
    """C-3: exact closed form of the FULL-tower saturated junction sum."""
    e = n // (2 * t)
    m = t.bit_length() - 1
    return e * (1.0 - log2_int(math.comb(2 * t, t))) + n * S_m(m)


def R3inf_window(n, t, W):
    """Closed-form R3 over an arbitrary window, from the telescoping lemma."""
    J = len(W)
    tot = log2_int(Zinf(n, t, W[0])) - log2_int(Zinf(n, t, W[-1] + 1)) + J * n
    for j in W:
        tot -= log2_int(Binf(n, t, j))
    return tot


def LamStar(n, t, lev):
    """Predicted level crossover: (n - log2 Zinf)/T."""
    T = t // 2 ** lev
    return (n - log2_int(Zinf(n, t, lev))) / T


# ------------------------------------------------------------------ cost model


def cost_Z(n, lev):
    """MITM half size for a level census (round-24 P5 model)."""
    return (2 ** lev + 1) ** ((n // 2 ** lev + 1) // 2)


def cost_window(n, W):
    return cost_Z(n, W[0])


# ------------------------------------------------------------------ q ladders


def primes_mod(n, lo_k, hi_k, per_octave=1):
    """Least prime q = 1 mod n at each grid point 2^(k + i/per_octave).

    2-power backbone when per_octave == 1 (CATCH-Z6); quarter-octave
    refinement (per_octave = 4) only inside a predicted transition, as
    registered in PREREG P6."""
    out = []
    steps = int(round((hi_k - lo_k) * per_octave))
    for s in range(steps + 1):
        x = lo_k + s / per_octave
        q = int(math.ceil(2.0 ** x))
        q = ((q + n - 1) // n) * n + 1
        while not is_prime(q):
            q += n
        if q not in out:
            out.append(q)
    return out


# ------------------------------------------------------------------ censuses


def Zlev(q, n, t, lev):
    """Exact weighted level census (round-24 Z[lev])."""
    h, T, vecs = level_vectors(q, n, t, lev)
    assert T >= 1 and h >= 2, "CATCH-19B"
    return mitm_null_count(vecs, binom_alpha(2 ** lev), q, T)


def Csub(q, n, t, lev):
    h, T, vecs = level_vectors(q, n, t, lev)
    return mitm_null_count(vecs, subset_alpha(), q, T)


def Blk(q, n, t, j):
    """Exact block-marginal census (round-24 Pblk_count)."""
    hj1, Lj, wv = junction_vectors(q, n, t, j)
    assert Lj >= 1 and hj1 >= 2, "CATCH-19B"
    return mitm_null_count(wv, skew_alpha(2 ** (j + 1)), q, Lj)


def R3_window(q, n, t, W, Zcache=None, Bcache=None):
    """R3_W by the TELESCOPING LEMMA (PREREG P1) -- two level censuses and
    J block censuses, instead of round-24's per-junction reconstruction.
    Returns (R3_W, per-junction terms, raw integers)."""
    Zc = {} if Zcache is None else Zcache
    Bc = {} if Bcache is None else Bcache

    def Z(lev):
        if lev not in Zc:
            Zc[lev] = Zlev(q, n, t, lev)
        return Zc[lev]

    def B(j):
        if j not in Bc:
            Bc[j] = Blk(q, n, t, j)
        return Bc[j]

    terms = []
    for j in W:
        terms.append(log2_ratio(Z(j), Z(j + 1)) + n - log2_int(B(j)))
    tele = (log2_int(Z(W[0])) - log2_int(Z(W[-1] + 1)) + len(W) * n
            - sum(log2_int(B(j)) for j in W))
    assert abs(tele - sum(terms)) < 1e-6, "TELESCOPING LEMMA violated"
    return sum(terms), terms, {"Z": dict(Zc), "B": dict(Bc)}

#!/usr/bin/env python3
"""The single scan core used IDENTICALLY by the h=8 calibration and the
h=64 / h=128 hunts (PREREG P4/P6).  No dimension-specific branch exists."""
import sys
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K


def process(w, order, band_lo, band_hi, rho_budget=0, rng=None):
    """One box vector -> (lognorm_bits, [accepted primes]).

    Identical code path at every h.  `order` = N' (the quotient order); an
    accepted prime must be = 1 mod order and lie in [band_lo, band_hi].
    """
    n = K.tower_norm(w)
    if n == 0:
        return 0, []
    n = abs(n)
    bits = n.bit_length()
    rough, fac = K.strip_small(n)
    hits = []
    # (a) stripped small primes that happen to lie in the band
    for p in fac:
        if band_lo <= p <= band_hi and p % order == 1:
            hits.append(p)
    # (b) the rough part itself
    if rough > 1 and band_lo <= rough <= band_hi and rough % order == 1:
        if K.is_probable_prime(rough):
            hits.append(rough)
            return bits, hits
    # (c) registered secondary: bounded Brent rho on a composite rough part
    if rho_budget and rough > 1 and not K.is_probable_prime(rough):
        f = K.pollard_brent(rough, rho_budget, rng or K.random.Random(0))
        if f:
            for cand in (f, rough // f):
                if (band_lo <= cand <= band_hi and cand % order == 1
                        and K.is_probable_prime(cand)):
                    hits.append(cand)
    return bits, hits


def verify_hit(w, p, order, mr_rounds=64):
    """Full fail-closed verification of one (w, p).  PREREG P5."""
    rep = {}
    rep["w_nonzero"] = any(t != 0 for t in w)
    rep["w_in_box"] = all(-2 <= t <= 2 for t in w)
    rep["l1"] = K.l1(w)
    rep["S"] = K.sq(w)
    rep["p_mod_order"] = p % order
    rep["p_bits"] = p.bit_length()
    rep["p_lt_2_256"] = p < 2 ** 256
    # SELF-CORRECTION: the PROVED emptiness ceiling is dimension-dependent.
    # It is (4(h-1)+1)^(h/2): 253^32 at h=64 (the PROVED node), 509^64 at h=128.
    h = len(w)
    rep["odd_ceiling"] = (4 * (h - 1) + 1) ** (h // 2)
    rep["p_le_253_32"] = p <= rep["odd_ceiling"]
    rep["v2_p_minus_1"] = (p - 1 & -(p - 1)).bit_length() - 1
    rep["bpsw_mr64"] = K.is_probable_prime(p, mr_rounds)
    n = abs(K.tower_norm(list(w)))
    rep["norm_bits"] = n.bit_length()
    rep["divides"] = (n % p == 0)
    rep["cofactor"] = n // p
    km = K.kernel_membership(list(w), p, order)
    rep["kernel_membership"] = km
    rep["ok"] = bool(rep["w_nonzero"] and rep["w_in_box"]
                     and rep["p_mod_order"] == 1 and rep["bpsw_mr64"]
                     and rep["divides"] and km is not None
                     and rep["p_le_253_32"])
    return rep

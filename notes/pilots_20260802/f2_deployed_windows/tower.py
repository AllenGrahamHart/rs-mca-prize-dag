#!/usr/bin/env python3
"""The OFFICIAL F2 tower's deployed windows -- reconstruction and the exact law.

------------------------------------------------------------ reconstruction --
Sources (quoted in REPORT):
  notes/f2_campaign/F2_CAMPAIGN_LOG.md:1394-1410 (entry #75, sector split)
  notes/f2_campaign/F2_CAMPAIGN_LOG.md:1412-1430 (entry #76, the tower)
  notes/pro_briefs_20260801/responses/verify_brief5_f2_myerson_program_arithmetic.py:24-27
  notes/floor_campaign/pro_briefs/PRO_FLOOR_2_F2_SUMMIT_V4.md:12-31

Official row: n a 2-power, p KoalaBear-shaped with p - 1 = 2^24 * 127, so
e := v_2(p-1) = 24; gcd(n, p-1) = 2^24 = the FIXED sector; the Frobenius orbit
of an element of order exactly 2^{24+j} has size ord_{2^{24+j}}(p) = 2^j, so

    RUNG j (j = 1..16):  n_j = 2^{24+j},  q_j = p^{2^j},  k_j = 2^j,
    the descent step is the quadratic extension F_{q_j} / F_{q_{j-1}},
    the moving coordinates are the elements of order EXACTLY 2^{24+j},
    m_j = (n_j - n_{j-1}) / 2 = 2^{22+j} conjugate pairs.

j = 1 is the pilots' instance: n_1 = 2^25, q_1 = p^2, m_1 = 2^23 pairs.

-------------------------------------------------------- THE ANTIPODAL LAW ----
LEMMA (exact; verified in verify.py A1).  p odd with e = v_2(p-1) >= 2,
n_j = 2^{e+j}, q_j = p^{2^j}.  Then

  (i)   v_2(q_j - 1) = e + j            for every j >= 0   [LTE],
  (ii)  mu_{n_j} <= F_{q_j}^*  and  mu_{n_j} cap F_{q_{j-1}} = mu_{n_{j-1}},
  (iii) every y of order exactly n_j satisfies  y^{q_{j-1}} = -y.

Proof of (iii): v_2(q_{j-1} - 1) = e+j-1, so q_{j-1} - 1 = 2^{e+j-1} * odd, and
y^{2^{e+j-1}} = -1 because y has order 2^{e+j}; hence y^{q_{j-1}-1} = -1.  QED

CONSEQUENCE.  The rung-j Frobenius conjugate pairs are the ANTIPODAL pairs
{y, -y}.  For the linear character x -> psi(c x) of the banked model,
s_i^- = Tr(c(-y_i)) = -Tr(c y_i) = -s_i^+ in F_p, hence sigma_i^- = -sigma_i^+
in Z/2p and

    Delta_i = sigma_i^+ - sigma_i^- = 2 sigma_i^+   ==   EVEN,   every i.

So EVERY deployed window is parity-homogeneous (beta_min = 0) at EVERY
frequency and EVERY rung: the mode k = p is exactly slice-DEAD, Lambda_p = 0,
|R_p| = 1, flat = 0.  (H-flat) and (H-spread) fail identically, and no
coordinate SELECTION can repair it -- every sub-window inherits all-even Delta.
"""
from __future__ import annotations

import math


def v2(x: int) -> int:
    return (x & -x).bit_length() - 1


def is_prime(m: int) -> bool:
    if m < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if m % q == 0:
            return m == q
    d, r = m - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, m)
        if x in (1, m - 1):
            continue
        for _ in range(r - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def official_shaped_prime(e: int, start_odd: int = 1) -> int:
    """Smallest prime p with v_2(p-1) == e exactly."""
    k = start_odd
    while True:
        p = (1 << e) * k + 1
        if is_prime(p) and v2(p - 1) == e:
            return p
        k += 2


KOALABEAR = (1 << 31) - (1 << 24) + 1          # 2130706433, p-1 = 2^24 * 127
OFFICIAL_E = 24
OFFICIAL_RUNGS = tuple(range(1, 17))           # j = 1..16, n_j = 2^25..2^40


def rung_params(e: int, j: int) -> dict:
    """n_j, m_j (pair count) at rung j for a prime with v_2(p-1) = e."""
    n_j = 1 << (e + j)
    n_prev = 1 << (e + j - 1)
    return {"rung": j, "n_ord": n_j, "n_prev": n_prev,
            "m_pairs": (n_j - n_prev) // 2, "k_ext": 1 << j}


def lte_v2_pow2(p: int, j: int) -> int:
    """v_2(p^{2^j} - 1) predicted by LTE: v2(p-1)+v2(p+1)+j-1 (j>=1)."""
    if j == 0:
        return v2(p - 1)
    return v2(p - 1) + v2(p + 1) + j - 1

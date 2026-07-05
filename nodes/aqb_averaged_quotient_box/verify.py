#!/usr/bin/env python3
"""Lightweight arithmetic verifier for aqb_averaged_quotient_box.

This checks only the finite constants in the AQB-I packet.  It uses Robbins
Stirling bounds with high-precision arithmetic to certify an interval for the
binomial term.  It does not prove the averaged-family existence claim.
"""

from __future__ import annotations

import mpmath as mp


N = 2**40
BASE = 2**39
D = 4_296_456_369
M = BASE + D
Q_MAX = 256.0
CLAIMED_BITS = 429_645_547


def log_factorial_bounds(n: int) -> tuple[mp.mpf, mp.mpf]:
    """Robbins bounds for log(n!) for n >= 1."""
    x = mp.mpf(n)
    base = (x + mp.mpf("0.5")) * mp.log(x) - x + mp.mpf("0.5") * mp.log(2 * mp.pi)
    return base + 1 / (12 * x + 1), base + 1 / (12 * x)


def main() -> None:
    mp.mp.dps = 80
    log2 = mp.log(2)

    n_lo, n_hi = log_factorial_bounds(N)
    m_lo, m_hi = log_factorial_bounds(M)
    r_lo, r_hi = log_factorial_bounds(N - M)

    log_c_lo = n_lo - m_hi - r_hi
    log_c_hi = n_hi - m_lo - r_lo

    deficit_lo = mp.mpf(D) * Q_MAX - 40 - log_c_hi / log2
    deficit_hi = mp.mpf(D) * Q_MAX - 40 - log_c_lo / log2
    qcrit_lo = (log_c_lo / log2 + 40) / D
    qcrit_hi = (log_c_hi / log2 + 40) / D
    per_fiber = mp.mpf(CLAIMED_BITS) / N

    assert mp.mpf("429645546.7") < deficit_lo < deficit_hi < mp.mpf("429645546.9")
    assert mp.mpf(CLAIMED_BITS) > deficit_hi
    assert mp.mpf("255.9000000") < qcrit_lo < qcrit_hi < mp.mpf("255.9000001")
    assert 0.0003907603 < per_fiber < 0.0003907604, per_fiber

    print("AQB arithmetic constants verified")
    print(f"N={N}")
    print(f"d={D}")
    print(f"m={M}")
    print(f"deficit_bits_interval=[{mp.nstr(deficit_lo, 30)}, {mp.nstr(deficit_hi, 30)}]")
    print(f"claimed_bits={CLAIMED_BITS}")
    print(f"certified_margin_bits={mp.nstr(mp.mpf(CLAIMED_BITS) - deficit_hi, 30)}")
    print(f"per_fiber_bits={mp.nstr(per_fiber, 20)}")
    print(f"qcrit_interval=[{mp.nstr(qcrit_lo, 30)}, {mp.nstr(qcrit_hi, 30)}]")


if __name__ == "__main__":
    main()

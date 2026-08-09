#!/usr/bin/env python3
"""pincer_formalization (round 27) -- ESCAPE TESTS E1..E4, E6.

Own code, stdlib only (math.lgamma).  Reimplements the decision cores of
  critical/nodes/rate_half_band_closure/notes/verify_floor_depth_modal.py   (E2)
  critical/nodes/rate_half_band_closure/notes/verify_q_threshold_modal.py   (E4)
  critical/nodes/rate_half_band_closure/notes/f6a2_fullscale_sweep_modal.py (E6)
  background/nodes/xr_radius_arithmetic/proof.md  (T*)                      (E1)
without modal/mpmath (banked scripts are Modal-only; this is a from-scratch
local re-implementation, not an edited banked copy).

PRECISION NOTE (registered): math.lgamma at N = 2^41 has absolute error
~0.02 bits; every integer crossing below moves the decision functional by
~L = 256 bits per unit step, so the crossing integer is unambiguous.
"""
from math import lgamma, log

LOG2 = log(2.0)
N_EXP, K_EXP = 41, 40
n, k = 1 << N_EXP, 1 << K_EXP


def log2C(N, m):
    if m < 0 or m > N:
        return float("-inf")
    return (lgamma(N + 1) - lgamma(m + 1) - lgamma(N - m + 1)) / LOG2


# ---------------------------------------------------------------- E1: t*
def t_star(L, nn, kk):
    """min { t : t*L >= log2 C(nn, nn-kk-t) + 128 }  -- (T*) of xr_radius_arithmetic."""
    lo, hi = 1, nn - kk
    while lo < hi:
        mid = (lo + hi) // 2
        if mid * L >= log2C(nn, nn - kk - mid) + 128.0:
            hi = mid
        else:
            lo = mid + 1
    return lo


def e1():
    L = 255.9
    want = {2: 8592912739, 4: 7014660390, 8: 4722556392, 16: 2943177800}
    out = []
    for r, expect in want.items():
        kk = n // r
        t = t_star(L, n, kk)
        out.append((r, t, expect, t == expect, t - 1))
    return out


# ------------------------------------------------- E2: cap reach (floor depth)
def max_reach(lq, trig, e_lo=12, e_hi=40, want_rows=False):
    rows, best = [], (0, None, None)
    for e in range(e_lo, e_hi):
        c = 1 << e
        if k % c:
            continue
        N = n // c
        base = k // c
        if base + 1 > N:
            continue
        lo, hi, dmax = 1, N - base, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if log2C(N, base + mid) - lq * (mid - 1) > trig:
                dmax, lo = mid, mid + 1
            else:
                hi = mid - 1
        if dmax == 0:
            continue
        depth = dmax * c
        if want_rows:
            m = log2C(N, base + dmax) - lq * (dmax - 1) - trig
            rows.append((e, c, dmax, depth, round(m, 3)))
        if depth > best[0]:
            best = (depth, e, dmax)
    return (best, rows) if want_rows else best


# ---------------------------------------------------------- E4: q-threshold
def q_threshold(SIGMA=8592912738):
    lo, hi = 128.0, 256.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if max_reach(mid, mid - 40.0)[0] >= SIGMA:
            lo = mid
        else:
            hi = mid
    return (round(lo, 6), max_reach(lo, lo - 40.0)[0],
            max_reach(hi, hi - 40.0)[0], max_reach(256.0, 216.0)[0])


# --------------------------------------------------------------- E6: f6a2
def f6a2_cell(lq):
    trig = lq - 40.0
    lo, hi = 1, n - k
    while lo <= hi:
        mid = (lo + hi) // 2
        if log2C(n, k + mid) - lq * mid > trig:
            lo = mid + 1
        else:
            hi = mid - 1
    sigma_star = hi
    PLATEAU = 1 << 33
    best_reach, best_scale, hits = 0, None, 0
    for j in range(1, N_EXP):
        c = 1 << j
        if k % c:
            continue
        N, base = n // c, k // c
        a, b, dmax = 1, N - base, 0
        while a <= b:
            mid = (a + b) // 2
            if log2C(N, base + mid) - lq * (mid - 1) > trig:
                dmax, a = mid, mid + 1
            else:
                b = mid - 1
        cov = dmax * c
        if cov > best_reach:
            best_reach, best_scale = cov, j
        if PLATEAU < cov <= sigma_star:
            hits += 1
    return sigma_star, best_reach, best_scale, hits


if __name__ == "__main__":
    print("== E1  t* / s* at L = 255.9 (T*) ==")
    for r, t, expect, ok, s in e1():
        print(f"  rate 1/{r:<3} t* = {t:>13,}  expect {expect:>13,}  "
              f"{'MATCH' if ok else 'MISMATCH'}   s* = {s:,}")

    print("\n== E2  cap reach at L = 256, trigger 2^216 ==")
    best, rows = max_reach(256.0, 216.0, want_rows=True)
    print(f"  max reach = {best[0]:,}  (2^33 = {1<<33:,})  "
          f"{'MATCH' if best[0] == 1 << 33 else 'MISMATCH'}  best e = {best[1]}, d = {best[2]}")
    plateau = sorted(e for (e, c, d, dep, m) in rows if dep == 1 << 33)
    print(f"  plateau scales e with depth exactly 2^33: {plateau[0]}..{plateau[-1]} "
          f"(count {len(plateau)})")

    print("\n== E3  band width ==")
    sstar = 8592912738
    print(f"  s* - 2^33 = {sstar - (1<<33):,}   expect 2,978,146   "
          f"{'MATCH' if sstar - (1<<33) == 2978146 else 'MISMATCH'}")

    print("\n== E4  q-threshold ==")
    thr, dat, dab, s256 = q_threshold()
    print(f"  threshold log2 q = {thr}   depth@thr = {dat:,}   depth just above = {dab:,}")
    print(f"  sanity max reach at L=256 = {s256:,}   open slice = {round(256-thr,6)} bits")

    print("\n== E6  f6a2 cells ==")
    for lq, exp_ss, exp_reach in ((255.90000002, 8592912736, 8592912738),
                                  (255.92, 8592241265, 8592241266)):
        ss, br, bs, hits = f6a2_cell(lq)
        print(f"  lq={lq}: sigma*={ss:,} (banked {exp_ss:,}) "
              f"{'MATCH' if ss == exp_ss else 'MISMATCH'} | "
              f"reach={br:,} (banked {exp_reach:,}) "
              f"{'MATCH' if br == exp_reach else 'MISMATCH'} | "
              f"scale=2^{bs} band_hits={hits}")

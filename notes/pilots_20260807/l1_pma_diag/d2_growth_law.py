#!/usr/bin/env python3
"""D2: exact closed form of the N10 census box + random-word growth law + reserve.

Registered as P1/P2/P3/P4/P5 in PREREG.md BEFORE running. Pure arithmetic.
"""
from math import comb, log2

BANKED = {
    # (n,k,p,mode): (candidates, retained, agreement_hist)
    (16, 8, 97, "consec"): (5096, 43, {9: 43}),
    (16, 8, 97, "geom5"): (5096, 33, {9: 33}),
    (32, 16, 97, "consec"): (386640, 2879, {17: 2871, 18: 8}),
    (32, 16, 97, "geom5"): (386640, 2857, {17: 2850, 18: 7}),
    (64, 32, 193, "consec"): (27152032, 109391, {33: 109329, 34: 62}),
    (64, 32, 193, "geom5"): (27152032, 108600, {33: 108547, 34: 53}),
}


def layout_params(n):
    """Mirror of layout() in l1_balanced_mixed_growth_census_modal.py:123-138."""
    k = n // 2
    half = n // 2
    nf = (k - 1) // 2
    core = 2 * nf + 1          # k-1 for even k
    background = 1
    petals = half - (nf + 1)   # k/2
    assert core + background + 2 * petals == n, (core, petals, n)
    return k, core, background, petals


def omission_count(k, t, om):
    """#omissions of size om from the k petal points hitting some petal exactly once.

    om=1: every singleton hits its petal once.
    om=2: all pairs except the t full petal pairs.
    om=3: every 3-subset (parts are 2+1 or 1+1+1, so some petal is hit once).
    """
    if om == 1:
        return k
    if om == 2:
        return comb(k, 2) - t
    if om == 3:
        return comb(k, 3)
    raise ValueError(om)


def census_box(n):
    """Exact candidate count, split by support size s = k+m."""
    k, core, bg_pts, t = layout_params(n)
    threshold = 2 * (t - 2)
    by_size = {}
    total = 0
    for cc in range(0, 4):
        if core - cc < threshold:
            continue
        for b in (0, 1):
            for om in (1, 2, 3):
                if k + cc + b - om < k + 1:
                    continue
                cnt = comb(core, cc) * omission_count(k, t, om)
                m = cc + b - om          # s = k + m
                by_size[m] = by_size.get(m, 0) + cnt
                total += cnt
    return total, by_size, (k, core, bg_pts, t, threshold)


def sigma_min(n, k, q, eps):
    """Least sigma with sigma*log2(q) >= (1+eps)*log2 C(n, k+sigma)."""
    for s in range(1, n - k + 1):
        if s * log2(q) >= (1 + eps) * log2(comb(n, k + s)):
            return s
    return None


print("=" * 78)
print("P1/P2 -- exact closed form of the N10 candidate box")
print("=" * 78)
for n in (16, 32, 64):
    total, by_size, (k, core, bgp, t, thr) = census_box(n)
    banked = [v[0] for kk, v in BANKED.items() if kk[0] == n][0]
    lead = comb(k, 3) * comb(core, 3)
    print(f"n={n:3d} k={k:2d} |core|={core:2d} t={t:2d} band d>={thr:2d} "
          f"-> core_sel<=3, omitted<=3")
    print(f"   closed form = {total:12,d}   banked = {banked:12,d}   "
          f"{'MATCH' if total == banked else 'MISMATCH'}")
    print(f"   by support size k+m: " +
          ", ".join(f"m={m}: {c:,}" for m, c in sorted(by_size.items())))
    print(f"   leading term C(k,3)*C(|core|,3) = {lead:,} "
          f"({100.0*lead/total:.1f}% of box); n^6/2304 = {n**6/2304:,.0f}")
print()
print("degree check log2(box) vs 6*log2(n):")
for n in (16, 32, 64):
    total, _, _ = census_box(n)
    print(f"   n={n:3d}: log_n(box) = {log2(total)/log2(n):.4f}")

print()
print("=" * 78)
print("P3/P4 -- random-word (Schwartz-Zippel) prediction vs the banked counts")
print("=" * 78)
print(f"{'row':>16} {'m=1 pred':>10} {'m=2 pred':>9} {'total':>9} "
      f"{'consec':>8} {'geom5':>8} {'err_c':>8} {'err_g':>8}")
preds = {}
for (n, k, q) in ((16, 8, 97), (32, 16, 97), (64, 32, 193)):
    _, by_size, _ = census_box(n)
    parts = {}
    for m, cnt in sorted(by_size.items()):
        parts[m] = cnt * q ** (-m) * (1 - 1.0 / q) ** (n - k - m)
    tot = sum(parts.values())
    preds[n] = (parts, tot)
    c = BANKED[(n, k, q, "consec")][1]
    g = BANKED[(n, k, q, "geom5")][1]
    print(f"{f'({n},{k},{q})':>16} {parts.get(1,0):10.1f} {parts.get(2,0):9.2f} "
          f"{tot:9.1f} {c:8d} {g:8d} "
          f"{100*(c-tot)/tot:7.1f}% {100*(g-tot)/tot:7.1f}%")

print()
print("agreement-(k+2) sub-counts: predicted vs banked")
for (n, k, q) in ((16, 8, 97), (32, 16, 97), (64, 32, 193)):
    parts, _ = preds[n]
    c = BANKED[(n, k, q, "consec")][2].get(k + 2, 0)
    g = BANKED[(n, k, q, "geom5")][2].get(k + 2, 0)
    print(f"   ({n},{k},{q}): pred {parts.get(2,0):8.2f}   banked {c:4d} / {g:4d}")

print()
print("P4 -- the 'doubling factor about 38'")
p16 = preds[16][1]
p32 = preds[32][1]
p64 = preds[64][1]
print(f"   predicted 16->32 ratio = {p32/p16:7.2f}   "
       f"banked: consec {2879/43:.2f}, geom5 {2857/33:.2f}")
print(f"   predicted 32->64 ratio = {p64/p32:7.2f}   "
       f"banked: consec {109391/2879:.4f}, geom5 {108600/2857:.4f}")
_, b32, _ = census_box(32)
_, b64, _ = census_box(64)
print(f"   pure box ratio N_(k+1): {b64[1]/b32[1]:.2f}; "
      f"field factor 97/193 = {97/193:.4f}; product = "
      f"{b64[1]/b32[1]*97/193:.2f}")

print()
print("=" * 78)
print("P5 -- where the census mass sits relative to the CORRECTED RESERVE")
print("=" * 78)
print("reserve: sigma*log2(q_D) >= (1+eps)*log2 C(n, k+sigma)  [imgfib statement.md:9]")
for eps in (0.0, 0.05):
    print(f"  eps={eps}:")
    for (n, k, q) in ((16, 8, 97), (32, 16, 97), (64, 32, 193)):
        s = sigma_min(n, k, q, eps)
        obs = sorted(BANKED[(n, k, q, "consec")][2])
        obs_sigma = [a - k for a in obs]
        print(f"    ({n:2d},{k:2d},{q:3d}): sigma_min = {s}   "
              f"observed retained sigma = {obs_sigma}   "
              f"{'ALL BELOW RESERVE' if max(obs_sigma) < s else 'some at/above'}")
print()
print("sigma=1 reserve gap (bits by which the entropy condition fails at sigma=1):")
for (n, k, q) in ((16, 8, 97), (32, 16, 97), (64, 32, 193)):
    need = log2(comb(n, k + 1))
    have = log2(q)
    print(f"    ({n:2d},{k:2d},{q:3d}): have {have:6.2f} bits, "
          f"need {need:6.2f} bits -> short by {need-have:6.2f} bits")

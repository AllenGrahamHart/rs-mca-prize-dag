#!/usr/bin/env python3
"""nf_quotient_price: S3 (prescribed-sum quotient census) + D4 (price check).

S3 tests the C1-mechanism flank freedom: the poly-side analysis fixes the
quotient sum e_1 = 0 (Lam-Leung => antipodal unions => the plateau). A flank
word may prescribe ANY value v. Registered prediction P4 (char 0, N a 2-power,
h-subsets of mu_N, power basis {1, zeta, ..., zeta^(N/2-1)}):
    #{S : sum(S) = v} = C(N/2 - |J|, (h - |J|)/2)   if v has coordinates in
    {0,+-1} with |J| nonzero coordinates and |J| = h mod 2, else 0;
    hence max_v = C(N/2, h/2), attained ONLY at v = 0.
Exhaustive in char 0 (integer power-basis coordinates) at N = 8, 16; exact
mod-q probes at N = 32.  Plus the sporadic ladder (~200 primes to 2^40).

D4 re-derives the banked ~2^-5.2 / ~2^-5.3 razor-row price from
rh_c1_c2_zerosum_n64.py:194 with exact integer arithmetic.
"""
import json, sys
from itertools import combinations
from math import comb, log2

def lg(x):
    if x <= 0: return float("-inf")
    b = x.bit_length()
    return b - 53 + log2(x >> (b - 53)) if b > 53 else log2(x)

def is_prime(m):
    if m < 2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if m % p == 0: return m == p
    d, s = m-1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(a, d, m)
        if x in (1, m-1): continue
        for _ in range(s-1):
            x = x*x % m
            if x == m-1: break
        else: return False
    return True

def primes_1mod(mod, count, start):
    out, x = [], start + 1
    while len(out) < count:
        if x % mod == 1 and is_prime(x): out.append(x)
        x += 1
    return out

# ---------- S3a: exhaustive char-0 prescribed-sum law (N = 8, 16) ----------
def char0_census(N):
    """exact multiplicities of subset sums of mu_N in the power basis."""
    h = N//2; half = N//2
    vecs = []
    for j in range(N):
        v = [0]*half
        if j < half: v[j] = 1
        else: v[j-half] = -1
        vecs.append(tuple(v))
    cnt = {}
    for S in combinations(range(N), h):
        acc = [0]*half
        for j in S:
            vj = vecs[j]
            for i in range(half): acc[i] += vj[i]
        key = tuple(acc)
        cnt[key] = cnt.get(key, 0) + 1
    pred_ok = True
    fails = []
    for key, c in cnt.items():
        J = sum(1 for x in key if x != 0)
        okcoords = all(x in (-1, 0, 1) for x in key)
        pred = comb(half - J, (h - J)//2) if (okcoords and (h - J) % 2 == 0
                                              and h >= J and half >= J) else None
        if pred != c:
            pred_ok = False; fails.append((key, c, pred))
    mx = max(cnt.values())
    argmax_zero = (cnt.get(tuple([0]*half), 0) == mx)
    nz = max((c for k, c in cnt.items() if any(k)), default=0)
    return dict(N=N, h=h, distinct_sums=len(cnt), max_mult=mx,
                mult_at_zero=cnt.get(tuple([0]*half), 0),
                pred_max=comb(half, h//2), argmax_is_zero=argmax_zero,
                max_mult_nonzero_v=nz, P4_exact=pred_ok,
                P4_failures=fails[:5])

# ---------- S3b: sporadic ladder (banked instrument-1 shape) ----------
def sporadic_ladder(N, h, qs):
    """mu_N minus one antipodal pair; zero-sum h-subsets; sporadic = excess
    over the char-0 antipodal floor C(N/2-1, h/2). Also max over v."""
    rows = []
    floor = comb(N//2 - 1, h//2)
    for q in qs:
        co = (q-1)//N
        g = None
        for g0 in range(2, 100000):
            c = pow(g0, co, q)
            if pow(c, N//2, q) != 1 and pow(c, N, q) == 1:
                if len({pow(c, i, q) for i in range(N)}) == N: g = c; break
        pts = [pow(g, i, q) for i in range(N)]
        b = pts[0]; mb = (q-b) % q
        avail = [x for x in pts if x not in (b, mb)]
        cnt = {}
        for S in combinations(avail, h):
            s = 0
            for x in S: s = (s + x) % q
            cnt[s] = cnt.get(s, 0) + 1
        z = cnt.get(0, 0)
        mx = max(cnt.values())
        rows.append(dict(q=q, zerosum=z, floor=floor, sporadic=z-floor,
                         max_over_v=mx, sporadic_v=mx-floor,
                         argmax_is_zero=(z == mx),
                         starved=(q > comb(N-2, h)),
                         first_moment=comb(N-2, h)/q))
    return rows

# ---------- S3c: N = 32 probes (meet in the middle, mod large q) ----------
def probe_n32(q, N=32, h=16, n_rand=8):
    co = (q-1)//N
    g = None
    for g0 in range(2, 100000):
        c = pow(g0, co, q)
        if pow(c, N//2, q) != 1 and pow(c, N, q) == 1:
            if len({pow(c, i, q) for i in range(N)}) == N: g = c; break
    pts = [pow(g, i, q) for i in range(N)]
    H1, H2 = pts[:16], pts[16:]
    def halfdp(P):
        d = {(0, 0): 1}
        for x in P:
            add = {}
            for (s, v), c in d.items():
                key = (s+1, (v+x) % q)
                add[key] = add.get(key, 0) + c
            for key, c in add.items(): d[key] = d.get(key, 0) + c
        return d
    d1, d2 = halfdp(H1), halfdp(H2)
    idx2 = {}
    for (s, v), c in d2.items(): idx2.setdefault(s, {})[v] = c
    def mult(v):
        tot = 0
        for (s1, u), c1 in d1.items():
            s2 = h - s1
            if s2 < 0 or s2 > 16: continue
            c2 = idx2.get(s2, {}).get((v-u) % q)
            if c2: tot += c1*c2
        return tot
    import random
    rng = random.Random(4242)
    res = dict(N=N, h=h, q=q, pred_zero=comb(16, 8),
               mult_zero=mult(0),
               mult_single_root=[mult(pts[j]) for j in (0, 1, 5)],
               mult_two_roots=[mult((pts[0]+pts[j]) % q) for j in (1, 3, 7)],
               mult_random=[mult(rng.randrange(q)) for _ in range(n_rand)])
    res["pred_single_root"] = comb(16-1, (16-1)//2) if (16-1) % 2 == 0 else 0
    return res

# ---------- D4: the razor price ----------
def d4():
    C255 = comb(255, 128); C254 = comb(254, 128)
    C127 = comb(127, 64)
    out = dict(source="critical/nodes/rate_half_band_closure/notes/"
                      "witness_hunt_20260712/rh_c1_c2_zerosum_n64.py:194",
               quoted_script="at razor q ~ 2^256 expected ~ C(255,128)/q ~ 2^-5.3",
               quoted_quality="q-sporadic hatch priced ~2^-5.2/row",
               lg_C255_128=lg(C255), lg_C254_128=lg(C254),
               lg_C127_64=lg(C127))
    for lab, lgq in (("razor bottom lg q = 255.900", 255.900),
                     ("razor top    lg q = 256.000", 256.000)):
        out["price_%s" % lab] = lg(C255) - lgq
        out["price_C254_%s" % lab] = lg(C254) - lgq
    # deficit replay
    for lab, lgneed in (("bottom (need = 2^127.900)", 127.900),
                        ("top    (need = 2^128.000)", 128.000)):
        out["deficit_bits_%s" % lab] = lgneed - lg(C127)
        out["members_needed_%s" % lab] = lgneed - lg(1)  # log2 of the need
    out["hatch_to_deficit_gap_bits_top"] = (128.000 - lg(C127)) - (lg(C255)-256.0)
    out["note"] = ("the price is the FIRST MOMENT of the NUMBER of sporadic "
                   "members per row; closing the band needs need-supply members")
    out["members_needed_top"] = lg((1 << 128) - C127)
    out["members_needed_bottom"] = lg(int(2**127.9) - C127)
    return out

def main():
    res = {}
    res["S3a_char0"] = [char0_census(8), char0_census(16)]
    qs8 = primes_1mod(8, 200, 8)
    qs16 = primes_1mod(16, 200, 16)
    big8 = primes_1mod(8, 3, 1 << 40)
    big16 = primes_1mod(16, 3, 1 << 40)
    res["S3b_ladder_N8"] = sporadic_ladder(8, 4, qs8 + big8)
    res["S3b_ladder_N16"] = sporadic_ladder(16, 8, qs16[:60] + big16)
    res["S3c_N32"] = [probe_n32(q) for q in primes_1mod(32, 1, 1 << 40)]
    res["D4"] = d4()
    print(json.dumps({k: (v if k not in ("S3b_ladder_N8", "S3b_ladder_N16")
                          else {"n_primes": len(v),
                                "sporadic_total": sum(r["sporadic"] for r in v),
                                "sporadic_v_total": sum(r["sporadic_v"] for r in v),
                                "first_moment_total": sum(r["first_moment"] for r in v),
                                "n_rows_argmax_zero": sum(1 for r in v if r["argmax_is_zero"]),
                                "n_starved": sum(1 for r in v if r["starved"]),
                                "max_sporadic_any_row": max(r["sporadic"] for r in v),
                                "max_sporadic_v_any_row": max(r["sporadic_v"] for r in v),
                                "rows_with_sporadic": [r for r in v if r["sporadic"]][:8],
                                "rows_with_sporadic_v": [r for r in v if r["sporadic_v"]][:8]})
                      for k, v in res.items()}, indent=1))
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f: json.dump(res, f, indent=1)

if __name__ == "__main__":
    main()

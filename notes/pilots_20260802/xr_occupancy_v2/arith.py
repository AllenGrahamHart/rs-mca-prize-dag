#!/usr/bin/env python3
"""STAGE D -- exact six-row arithmetic for the two-slope cost theorem.

D1  the six rows, the two-slope DESIGN CEILING (2R-1)/(2h) and
    (2R-1)/(2h-2), the sunflower cost ceiling (2R-1)/h, the sunflower
    point-budget law max_d floor((R+1)/(h-d)) over d <= (h-1)/2, and the
    ledger column each of them implies against the 13n^3 headroom and the
    0.68n^2 per-depth requirement.

D2  the FIRST-MOMENT / CODIMENSION identity
        E[N_d] = (1/2) C(n,k+d) C(R-d,h-d)^2 q^{-(2h-2)},
    whose q-exponent is EXACTLY the free-slope codimension of the
    two-slope datum -- independent of d.  Evaluated at the official cap.

D3  how weak a cost floor suffices: the occupancy lemma follows from
    "rank >= c.M" for c as small as (2R-1)/(0.68 n^2).

D4  the MC quantisation: admissible (w, M) with M | n, M | r' = n-k-w,
    w <= M; the depth MC occupies is exactly w; the largest in-band w;
    and the per-live-slope coincidence cost h-w at that w.

Run: tools/ramguard local -- python3 arith.py
"""
from __future__ import annotations

import json
import math
import os
import sys
from math import comb, gcd, log2

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))

FAIL, CHECKS = [], [0]


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    print(("PASS " if ok else "FAIL ") + label + (f"  [{detail}]" if detail else ""))
    if not ok:
        FAIL.append(label + " " + detail)
    return ok


def lg_binom(a, b):
    """log2 C(a,b) exactly for small a, Stirling for huge a."""
    if b < 0 or b > a:
        return float("-inf")
    if a <= 4000:
        c = comb(a, b)
        if c == 0:
            return float("-inf")
        bl = c.bit_length()
        if bl <= 900:
            return log2(c)
        return bl - 1 + log2(c / (1 << (bl - 1)))
    lg = math.lgamma
    return (lg(a + 1) - lg(b + 1) - lg(a - b + 1)) / math.log(2)


ROWS = []
for name, n, rate, scale in [("RowC 1/4", 1024, 4, 256),
                             ("RowC 1/8", 1024, 8, 256),
                             ("RowC 1/16", 1024, 16, 512),
                             ("prize 1/4", 2 ** 41, 4, 256),
                             ("prize 1/8", 2 ** 41, 8, 256),
                             ("prize 1/16", 2 ** 41, 16, 512)]:
    k = n // rate
    A = k + n // scale + 1
    ROWS.append(dict(name=name, n=n, k=k, A=A, h=A - k, R=n - k, r=n - A))

BANKED_A = [261, 133, 67, 558345748481, 283467841537, 141733920769]
Q_CAP = 1 << 256                     # official field-size cap
Q_PIN = 1 << 250                     # banked lower pin

OUT = {}


def d1():
    print("\n=== D1  two-slope ceilings at the six rows ===")
    print(f"{'row':<11}{'h':>13}{'R':>15}{'ceil 2h':>10}{'ceil 2h-2':>11}"
          f"{'ceil h':>9}{'sunflower':>11}{'0.68n^2':>12}")
    rows = []
    for i, r in enumerate(ROWS):
        n, k, A, h, R = r["n"], r["k"], r["A"], r["h"], r["R"]
        assert A == BANKED_A[i], (A, BANKED_A[i])
        c_fixed = (2 * R - 1) // (2 * h)
        c_free = (2 * R - 1) // (2 * h - 2)
        c_sun = (2 * R - 1) // h
        # sunflower point-budget law, maximised over d <= (h-1)//2
        # (R+1)//(h-d) is non-decreasing in d, so the max over the sunflower
        # range d <= (h-1)//2 is attained at d = (h-1)//2.
        dmax = (h - 1) // 2
        sun = ((R + 1) // (h - dmax), dmax) if dmax >= 1 else (0, 0)
        need = 0.68 * n * n
        rows.append(dict(name=r["name"], n=n, k=k, A=A, h=h, R=R,
                         ceiling_slopes_fixed=c_fixed,
                         ceiling_slopes_free=c_free,
                         ceiling_sunflower_cost=c_sun,
                         sunflower_law=sun[0], sunflower_arg_d=sun[1],
                         requirement_0p68n2=need,
                         margin_free_vs_requirement=need / max(c_free, 1)))
        print(f"{r['name']:<11}{h:>13}{R:>15}{c_fixed:>10}{c_free:>11}"
              f"{c_sun:>9}{sun[0]:>11}{need:>12.3e}")
    # ledger column implied by the free ceiling
    print("\n  ledger column  sum_d N_d L(d)  under N_d <= ceiling(2h-2):")
    for rec, r in zip(rows, ROWS):
        n, k, h, R = r["n"], r["k"], r["h"], r["R"]
        # sum_{d=1}^{h-2} floor((R-d)/(h-d)) by divisor blocks
        tot = 0
        d = 1
        while d <= h - 2:
            v = (R - d) // (h - d)
            if v == 0:
                break
            # largest d' with floor((R-d')/(h-d')) == v
            # (R-d)/(h-d) decreasing in d for R>h
            lo, hi = d, h - 2
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if (R - mid) // (h - mid) == v:
                    lo = mid
                else:
                    hi = mid - 1
            tot += v * (lo - d + 1)
            d = lo + 1
        col = rec["ceiling_slopes_free"] * tot
        head = 13 * n ** 3
        rec["sum_L"] = tot
        rec["column_under_ceiling"] = col
        rec["headroom_13n3"] = head
        rec["column_fits"] = col <= head
        rec["column_margin_log2"] = log2(head / col) if col else float("inf")
        print(f"   {r['name']:<11} sum_d L(d) = {tot:.6e}   column = {col:.6e}"
              f"   13n^3 = {head:.6e}   fits={col <= head}  "
              f"margin 2^{log2(head/col):.1f}")
        chk(f"D1 {r['name']}: designed two-slope ceiling fits the 13n^3 "
            f"headroom", col <= head)
        chk(f"D1 {r['name']}: designed ceiling {rec['ceiling_slopes_free']} "
            f"<< 0.68n^2", rec["ceiling_slopes_free"] <= 0.68 * n * n)
    OUT["d1"] = rows
    return rows


def d2():
    print("\n=== D2  first moment == (designs) x q^{-codim}, codim = 2h-2 ===")
    res = []
    for r in ROWS:
        n, k, A, h, R = r["n"], r["k"], r["A"], r["h"], r["R"]
        per = []
        for d in ([1, 2, h // 2, h - 3, h - 2] if h > 6 else
                  list(range(1, h - 1))):
            if not (1 <= d <= h - 2):
                continue
            lg = (lg_binom(n, k + d) + 2 * lg_binom(R - d, h - d)
                  - (2 * h - 2) * 256 - 1)
            per.append(dict(d=d, log2_E_Nd=lg))
        res.append(dict(row=r["name"], h=h, codim=2 * h - 2, per_depth=per))
        print(f"  {r['name']:<11} codim=2h-2={2*h-2}: " +
              "  ".join(f"d={x['d']}: log2 E[N_d]={x['log2_E_Nd']:.4g}"
                        for x in per))
    OUT["d2"] = res
    # exponent identity: q-exponent of the first moment = free-slope codim
    for r in ROWS:
        h = r["h"]
        chk(f"D2 {r['name']}: first-moment q-exponent 2d + 2(h-d-1) = "
            f"2h-2 = {2*h-2} independent of d",
            all(2 * d + 2 * (h - d - 1) == 2 * h - 2
                for d in [1, 2, h // 3, h // 2, h - 3, h - 2]
                if 1 <= d <= h - 2))
    return res


def d3():
    print("\n=== D3  how weak a cost floor suffices ===")
    res = []
    for r in ROWS:
        n, k, h, R = r["n"], r["k"], r["h"], r["R"]
        need = 0.68 * n * n
        c_needed = (2 * R - 1) / need
        # aggregate form
        agg = 13 * n ** 3
        res.append(dict(row=r["name"], per_depth_requirement=need,
                        cost_floor_needed=c_needed,
                        pairs_per_single_condition=1 / c_needed))
        print(f"  {r['name']:<11} N_d <= 0.68n^2 = {need:.4e} follows from "
              f"rank >= {c_needed:.4e} * M, i.e. ONE fresh condition per "
              f"{1/c_needed:.4e} pairs")
    OUT["d3"] = res
    return res


def d4():
    print("\n=== D4  MC quantisation: admissible (w, M) and the band ===")
    res = []
    for r in ROWS:
        n, k, h, R = r["n"], r["k"], r["h"], r["R"]
        adm = []
        # w must satisfy: exists M with M|n, M|(n-k-w), w<=M
        # -> M | gcd(n, k+w) and M >= w.  Since n and k are powers of two
        # here, gcd(n,k+w) = 2^{v_2(k+w)} = 2^{v_2(w)} for w < k, so the
        # condition is exactly "w is a power of two" -- but we enumerate the
        # divisors of n honestly (M | n) rather than assume it.
        divs = []
        m_ = 1
        while m_ * m_ <= n:
            if n % m_ == 0:
                divs.append(m_)
                if m_ != n // m_:
                    divs.append(n // m_)
            m_ += 1
        for M in sorted(divs):
            # need 1 <= w <= min(M, h-1) and w = (n-k) mod M
            w0 = (n - k) % M
            w = M if w0 == 0 else w0
            if 1 <= w <= min(M, h - 1):
                adm.append(dict(w=w, max_M=M, in_band=(1 <= w <= h - 2)))
        seen = {}
        for x in adm:
            if x["w"] not in seen or x["max_M"] > seen[x["w"]]["max_M"]:
                seen[x["w"]] = x
        adm = [seen[w] for w in sorted(seen)]
        inband = [x for x in adm if x["in_band"]]
        top_band = max((x["w"] for x in inband), default=0)
        rec = dict(row=r["name"], h=h, n_admissible_w=len(adm),
                   admissible_w_sample=[x["w"] for x in adm[:12]],
                   max_admissible_w=max((x["w"] for x in adm), default=0),
                   max_in_band_w=top_band,
                   cascade_w=h - 1,
                   cascade_admissible=any(x["w"] == h - 1 for x in adm),
                   coincidences_per_live_slope_at_top_band=h - top_band)
        # MC size and the expected two-slope count at the top in-band w
        if top_band:
            w = top_band
            M = gcd(n, k + w)
            N, m = n // M, (n - k - w) // M
            lgMC = lg_binom(N, m) - log2(N) if N else 0
            e = h - w                       # points needed per live slope
            lg_one = lg_binom(n - k - w, e) - (e - 1) * 256
            rec.update(top_band_M=M, top_band_N=N, top_band_m=m,
                       log2_MC_size=lgMC,
                       log2_E_two_slope=lgMC + 2 * lg_one - 1)
        res.append(rec)
        print(f"  {r['name']:<11} h={h}: admissible w = "
              f"{[x['w'] for x in adm[:10]]}{'...' if len(adm)>10 else ''}  "
              f"cascade w=h-1={h-1} admissible={rec['cascade_admissible']}  "
              f"max in-band w={top_band} -> {h-top_band} coincidences per "
              f"live slope")
        if top_band:
            print(f"                log2|MC| = {rec['log2_MC_size']:.4g}, "
                  f"log2 E[N_w with 2 live slopes] = "
                  f"{rec['log2_E_two_slope']:.6g}")
        chk(f"D4 {r['name']}: MC's cascade-tier w = h-1 is admissible",
            rec["cascade_admissible"])
        chk(f"D4 {r['name']}: every in-band admissible w leaves >= "
            f"(h+1)/2 coincidences per live slope",
            rec["coincidences_per_live_slope_at_top_band"] >= (h + 1) // 2,
            f"h-w = {rec['coincidences_per_live_slope_at_top_band']}")
    OUT["d4"] = res
    return res


if __name__ == "__main__":
    d1()
    d2()
    d3()
    d4()
    OUT["_checks"] = CHECKS[0]
    OUT["_failures"] = FAIL
    with open(os.path.join(HERE, "arith.json"), "w") as f:
        json.dump(OUT, f, indent=1, default=str)
    print(f"\nchecks={CHECKS[0]} failures={len(FAIL)}")
    if FAIL:
        print("\n".join(FAIL[:20]))

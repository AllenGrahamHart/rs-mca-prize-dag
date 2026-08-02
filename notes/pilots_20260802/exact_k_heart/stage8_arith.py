#!/usr/bin/env python3
r"""STAGE 8 -- exact six-row arithmetic for the d = 0 stratum, the moment
analysis, the coset/2-adic transfer, and the toy-blindness threshold.

A1  the d=0 caps: single-sunflower point budget R/h (== the banked
    sunflower cap (n-k)/(t-d) at d=0) and the design ceiling (2R-1)/h.
A2  margins against the P-A1 budget 8n^3, and the moment thresholds.
A3  the extremal moment M_0 (two maximal sunflowers) vs the 4n^3 that the
    moment route would need.
A4  BP transfer: at d = 0 a coset construction needs g = h-d = h to be a
    power of two; h is ODD at all six rows -> no live coset ray.
A5  toy-blindness threshold: the expected noise live-ray count
    (q+1) C(n,A) q^{-h}; where the toys sit and what scale would see the
    heart.
"""
from __future__ import annotations

import json
import math
import os
import random
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import dzlib as Z                                              # noqa: E402
import tslib as T                                              # noqa: E402

OUT = {"checks": [], "fail": 0, "pass": 0, "rows": [], "data": {}}


def chk(name, cond, info=None):
    OUT["checks"].append(dict(name=name, ok=bool(cond), info=info))
    if cond:
        OUT["pass"] += 1
    else:
        OUT["fail"] += 1
        print("  FAIL", name, info)
    return cond


def lg2(x):
    if x <= 0:
        return float("-inf")
    return math.log2(x) if x < (1 << 900) else x.bit_length() - 1 + \
        math.log2(x / (1 << (x.bit_length() - 1)))


def lgbinom(a, b):
    if b < 0 or b > a:
        return float("-inf")
    return (math.lgamma(a + 1) - math.lgamma(b + 1) -
            math.lgamma(a - b + 1)) / math.log(2)


def main():
    print(f"{'row':<11}{'h':>12}{'R':>15}{'R/h':>7}{'(2R-1)/h':>10}"
          f"{'lg 8n^3':>9}{'lg margin':>11}{'lg M0*':>9}{'lg 4n^3':>9}")
    for r in Z.ROWS:
        n, k, A, h, R = r["n"], r["k"], r["A"], r["h"], r["R"]
        sun = R // h                      # single-sunflower point budget
        ceil_ = (2 * R - 1) // h          # d=0 design ceiling
        b8 = 8 * n ** 3
        b4 = 4 * n ** 3
        # extremal moment: two maximal sunflowers of sizes ceil/2
        v1 = ceil_ // 2
        v2 = ceil_ - v1
        M0 = v1 * (v1 - 1) // 2 + v2 * (v2 - 1) // 2
        # sanity: the banked d-adaptive sunflower cap at d=0 is (n-k)/(t-d)
        chk(f"A1 sunflower cap == (n-k)/h  {r['name']}",
            sun == (n - k) // h, (sun, (n - k) // h))
        chk(f"A1 ceiling = 2x sunflower (+-1) {r['name']}",
            abs(ceil_ - 2 * sun) <= 2, (ceil_, sun))
        chk(f"A2 ceiling << 8n^3 {r['name']}", ceil_ < b8)
        chk(f"A3 extremal moment << 4n^3 {r['name']}", M0 < b4)
        chk(f"A4 h is odd (no power-of-two g=h) {r['name']}", h % 2 == 1, h)
        # noise threshold: expected live rays from coincidence
        lgnoise = lg2(n) * 0 + lgbinom(n, A) - (h - 1) * lg2(1 << 250)
        rec = dict(name=r["name"], n=n, k=k, A=A, h=h, R=R,
                   sunflower_cap=sun, ceiling=ceil_,
                   lg_8n3=lg2(b8), lg_margin=lg2(b8) - lg2(max(ceil_, 1)),
                   extremal_M0=M0, lg_M0=lg2(max(M0, 1)), lg_4n3=lg2(b4),
                   lg_noise_at_q2p250=lgnoise,
                   A_over_n=A / n, h_over_A=h / A, k_over_A=k / A)
        OUT["rows"].append(rec)
        print(f"{r['name']:<11}{h:>12}{R:>15}{sun:>7}{ceil_:>10}"
              f"{lg2(b8):>9.1f}{lg2(b8)-lg2(ceil_):>11.1f}"
              f"{lg2(max(M0,1)):>9.1f}{lg2(b4):>9.1f}")

    print("\n  geometry ratios (why the stage-3/5 toys were the wrong shape):")
    for rec in OUT["rows"]:
        print(f"   {rec['name']:<11} A/n={rec['A_over_n']:.4f} "
              f"k/A={rec['k_over_A']:.4f} h/A={rec['h_over_A']:.5f}")

    print("\n  A5 toy blindness: lg E[#noise live rays] = lg((q+1)C(n,A)q^-h)")
    toys = [(16, 6, 3, 61), (18, 6, 3, 43), (20, 6, 3, 53), (20, 6, 3, 1201),
            (16, 6, 3, 601), (48, 12, 3, 3001), (64, 16, 3, 4001),
            (20, 9, 3, 41)]
    a5 = []
    for (n, k, h, q) in toys:
        A = k + h
        lgE = lg2(q + 1) + lgbinom(n, A) - h * lg2(q)
        a5.append(dict(n=n, k=k, h=h, q=q, A=A, lgE=lgE))
        print(f"   n={n:<3}k={k:<3}h={h} q={q:<5} A={A:<3} "
              f"lg E[noise live] = {lgE:+.2f}"
              f"   {'NOISE-DOMINATED' if lgE > 0 else 'structural'}")
    OUT["data"]["a5"] = a5
    for rec in OUT["rows"]:
        print(f"   {rec['name']:<11} lg E[noise live] at q=2^250: "
              f"{rec['lg_noise_at_q2p250']:.3e}")

    # ---------------- A4 toy: coset domain, h odd vs h a power of two
    print("\n  A4 coset toy (multiplicative domain, coset-union supports):")
    a4 = []
    for (n, k, h, q) in [(16, 8, 3, 97), (16, 8, 4, 97), (12, 6, 3, 73),
                         (12, 6, 2, 73), (20, 10, 5, 41), (20, 10, 4, 41)]:
        if (q - 1) % n:
            continue
        xs, om = T.mult_domain(q, n)
        row = Z.make_row(n, k, h, q, xs=xs)
        # mu_M-orbits of the domain, M | n a power of two
        res = []
        for M in (2, 4, 8):
            if n % M or k % M:
                continue
            step = n // M
            orb = [tuple(sorted((i + j * step) % n for j in range(M)))
                   for i in range(step)]
            # a coset-union k-set and a coset-union A-set need M | A
            res.append(dict(M=M, divides_A=(row.A % M == 0),
                            h_pow2=(h & (h - 1)) == 0))
        a4.append(dict(n=n, k=k, h=h, A=row.A, orbits=res))
        print(f"   n={n} k={k} h={h} A={row.A}: h power of two? "
              f"{(h & (h-1)) == 0};  M | A for M in "
              f"{[d['M'] for d in res if d['divides_A']]}")
    OUT["data"]["a4"] = a4

    json.dump(OUT, open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "stage8.json"), "w"), indent=1)
    print(f"\nstage8: PASS={OUT['pass']} FAIL={OUT['fail']}")


if __name__ == "__main__":
    main()

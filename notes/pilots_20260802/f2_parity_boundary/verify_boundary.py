#!/usr/bin/env python3
"""Exact validation of the parity-boundary machinery (F2A.5b).

Run: tools/ramguard local -- python3 \
       notes/pilots_20260802/f2_parity_boundary/verify_boundary.py

B1  Delta-only DP == the F2A.5 sigma DP (cross-implementation, exact ints)
B2  (P1) the Delta/base mode law, exact in Z[zeta_p]
B3  the k = p term IS the Krawtchouk number, exact
B4  slice death: all Delta equal  =>  |V_b| = C(n,b) for every b, exact
B5  Lambda_p(beta) two-branch closed form vs the numeric maximisation
B6  the Cauchy bound (P2) holds on every tested (window, mode, b)
B7  the Fourier surrogate Lambda_k >= beta(1-beta)(1-|R_k|)/ln2 holds
B8  certified_bits() really lower-bounds the measured -log2 rho_b
"""

from __future__ import annotations

import cmath
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import boundary as B  # noqa: E402
from slicecore import (  # noqa: E402
    Cyc, elem_sym, hhat, omega_pow, sigma_of,
)
from mode_and_coset import V_of, slice_count_sigma  # noqa: E402

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print(f"  !! FAIL {msg}")


# ------------------------------------------------------------------- B1 -----
def b1():
    rows = 0
    for p in (7, 11, 13, 19, 23):
        for c in ((1, 1), (2, 3), (1, 2)):
            c = (c[0] % p, c[1] % p)
            D, S, loc = B.model(p, c)
            for n in (6, 9, 12):
                if n > len(loc):
                    continue
                sub = loc[:n]
                sig = sigma_of(p, sub)
                Vref = V_of(p, slice_count_sigma(p, sig), n)
                base = sum(x[1] for x in sig) % (2 * p)
                Vmine = B.V_exact(p, D[:n], base)
                check(Vref == Vmine, f"B1 p={p} c={c} n={n}")
                rows += 1
    print(f"F2A5B_B1_DELTA_DP_PASS            rows={rows} "
          f"(Delta-only DP == sigma DP, exact integers)")


# ------------------------------------------------------------------- B2 -----
def b2():
    rows = 0
    for p in (7, 11, 13):
        for c in ((1, 1), (2, 3)):
            D, S, loc = B.model(p, c)
            for n in (4, 6, 8):
                if n > len(loc):
                    continue
                dl = D[:n]
                base = sum(S[:n]) % (2 * p)
                V = B.V_exact(p, dl, base)
                tot = [Cyc.zero(p) for _ in range(n + 1)]
                for k in range(1, 2 * p, 2):
                    H = hhat(p, k) * omega_pow(p, k * base)
                    e = elem_sym([(omega_pow(p, k * d), Cyc.one(p)) for d in dl])
                    for b in range(n + 1):
                        tot[b] = tot[b] + H * e[b]
                for b in range(n + 1):
                    lhs = Cyc.one(p) * (2 * p * V[b])
                    check((tot[b] - lhs).is_zero(), f"B2 p={p} c={c} n={n} b={b}")
                    rows += 1
                # even modes must contribute nothing
                for k in range(0, 2 * p, 2):
                    check(hhat(p, k).is_zero(), f"B2even p={p} k={k}")
    print(f"F2A5B_B2_MODE_LAW_PASS            rows={rows} "
          f"(2p V_b = sum_k hhat(k) omega^{{k base}} e_b(omega^{{k Delta}}); "
          f"exact in Z[zeta_p])")


# ------------------------------------------------------------------- B3 -----
def b3():
    rows = 0
    for p in (7, 11, 13, 19):
        for c in ((1, 1), (2, 3)):
            D, S, loc = B.model(p, c)
            for n in (4, 6, 8, 10):
                if n > len(loc):
                    continue
                dl = D[:n]
                base = sum(S[:n]) % (2 * p)
                n_o = sum(1 for d in dl if d % 2)
                K = B.krawtchouk_parity(n_o, n - n_o)
                e = elem_sym([(omega_pow(p, p * d), Cyc.one(p)) for d in dl])
                for b in range(n + 1):
                    check((e[b] - Cyc.one(p) * K[b]).is_zero(),
                          f"B3 kraw p={p} n={n} b={b}")
                    rows += 1
                # and the k=p contribution to V_b is (-1)^base K[b] / p
                Hp = hhat(p, p)
                check((Hp - Cyc.one(p) * 2).is_zero(), f"B3 hhat_p(p)=2 p={p}")
                sgn = -1 if base % 2 else 1
                for b in range(n + 1):
                    term = Cyc.one(p) * (2 * sgn * K[b])
                    got = Hp * omega_pow(p, p * base) * e[b]
                    check((got - term).is_zero(), f"B3 term p={p} n={n} b={b}")
    print(f"F2A5B_B3_KRAWTCHOUK_PASS          rows={rows} "
          f"(e_b at k=p == [z^b](1-z)^{{n_o}}(1+z)^{{n_e}}; hhat_p(p)=2)")


# ------------------------------------------------------------------- B4 -----
def b4():
    rows = 0
    for p in (11, 13, 19, 23):
        for c in ((1, 1), (2, 3)):
            for n in (8, 10):
                w = B.subgroup_coset_window(p, c, n, "trivial")
                if w is None:
                    continue
                dl, base, _ = w
                check(len(set(dl)) == 1, f"B4 not constant p={p}")
                V = B.V_exact(p, dl, base)
                for b in range(n + 1):
                    check(abs(V[b]) == math.comb(n, b),
                          f"B4 p={p} c={c} n={n} b={b} V={V[b]}")
                    rows += 1
    print(f"F2A5B_B4_TOTAL_DEATH_PASS         rows={rows} "
          f"(all Delta equal => |V_b| = C(n,b) exactly, EVERY b: rho = 1)")


# ------------------------------------------------------------------- B5 -----
def b5():
    rows = 0
    worst = 0.0
    for p in (11, 23, 41):
        for n in (24, 32):
            for j in (0, 1, 2, 4, 8, n // 2):
                w = B.parity_ramp_window(p, (1, 1), n, j)
                if w is None:
                    continue
                dl = w[0]
                bm = B.beta_min(dl)
                for b in (n // 4, n // 3, 3 * n // 8, n // 2, 5 * n // 8):
                    beta = b / n
                    closed = B.Lambda_p_closed(bm, beta)
                    num = B.Lambda_k(p, dl, p, beta, grid=4096)
                    worst = max(worst, abs(closed - num))
                    check(abs(closed - num) < 1e-9,
                          f"B5 p={p} n={n} j={j} b={b} {closed} vs {num}")
                    rows += 1
    print(f"F2A5B_B5_LAMBDA_P_CLOSED_PASS     rows={rows} "
          f"max|closed-numeric| = {worst:.2e}  "
          f"(two-branch closed form for Lambda_p)")


# ------------------------------------------------------------------- B6/B7 --
def _e_b_abs(p, deltas, k, b):
    """|e_b(omega^{k Delta})| by complex polynomial product.  FLOAT."""
    poly = [1.0 + 0j]
    for d in deltas:
        z = cmath.exp(1j * math.pi * ((k * d) % (2 * p)) / p)
        poly = [(poly[j] if j < len(poly) else 0) +
                (poly[j - 1] * z if j else 0) for j in range(len(poly) + 1)]
    return abs(poly[b])


def b67():
    rows = 0
    slack6, slack7 = [], []
    for p in (11, 23):
        for c in ((1, 1), (2, 3)):
            for n in (16, 24):
                for maker in (lambda: B.generic_window(p, c, n),
                              lambda: B.parity_ramp_window(p, c, n, 0),
                              lambda: B.parity_ramp_window(p, c, n, 3),
                              lambda: B.arc_window(p, c, n, 2)):
                    w = maker()
                    if w is None:
                        continue
                    dl = w[0]
                    R = B.R_coeffs(p, dl)
                    for b in (n // 4, n // 2, 3 * n // 4):
                        beta = b / n
                        kap = B.kappa(n, b)
                        C = math.comb(n, b)
                        for k in range(1, 2 * p, 2):
                            L = B.Lambda_k(p, dl, k, beta, grid=1024)
                            lhs = _e_b_abs(p, dl, k, b) / C
                            rhs = kap * 2.0 ** (-n * L)
                            check(lhs <= rhs * (1 + 1e-9),
                                  f"B6 p={p} n={n} k={k} b={b} {lhs} > {rhs}")
                            slack6.append(rhs / max(lhs, 1e-300))
                            sur = (beta * (1 - beta) / math.log(2)) * \
                                  (1 - abs(R[k]))
                            check(L >= sur - 1e-9,
                                  f"B7 p={p} n={n} k={k} b={b} {L} < {sur}")
                            slack7.append(L - sur)
                            rows += 1
    print(f"F2A5B_B6_CAUCHY_BOUND_PASS        rows={rows} "
          f"median overshoot factor {sorted(slack6)[len(slack6)//2]:.2f}")
    print(f"F2A5B_B7_FOURIER_SURROGATE_PASS   rows={rows} "
          f"min slack {min(slack7):.3e} (Lambda_k >= b(1-b)(1-|R_k|)/ln2)")


# ------------------------------------------------------------------- B8 -----
def b8():
    rows = 0
    gaps = []
    for p in (11, 23, 41):
        for c in ((1, 1), (2, 3)):
            for n in (16, 24, 32):
                for maker in (lambda: B.generic_window(p, c, n),
                              lambda: B.parity_ramp_window(p, c, n, 0),
                              lambda: B.parity_ramp_window(p, c, n, 2),
                              lambda: B.arc_window(p, c, n, 2),
                              lambda: B.arc_window(p, c, n, 3)):
                    w = maker()
                    if w is None:
                        continue
                    dl, base, _ = w
                    V = B.V_exact(p, dl, base)
                    for b in (n // 4, n // 2, 3 * n // 4):
                        meas = B.neglog2_rho(V[b], n, b)
                        if meas is None:
                            continue
                        cert = B.certified_bits(p, dl, b, grid=512)
                        check(meas >= cert - 1e-6,
                              f"B8 p={p} n={n} b={b} meas={meas} cert={cert}")
                        gaps.append(meas - cert)
                        rows += 1
    gaps.sort()
    print(f"F2A5B_B8_CERTIFICATE_SOUND_PASS   rows={rows} "
          f"median (measured - certified) = {gaps[len(gaps)//2]:.2f} bits, "
          f"min = {gaps[0]:.2f}")


if __name__ == "__main__":
    b1(); b2(); b3(); b4(); b5(); b67(); b8()
    print()
    if FAIL:
        print(f"F2A5B_VALIDATION_FAILURES = {len(FAIL)}")
        for m in FAIL[:20]:
            print("   ", m)
        sys.exit(1)
    print("F2A5B_VALIDATION_ALL_PASS  (8/8)")

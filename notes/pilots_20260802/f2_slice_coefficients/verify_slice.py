#!/usr/bin/env python3
"""Exact validations of the b-resolved slice machinery (F2A.5).

Run:  tools/ramguard local -- python3 \
        notes/pilots_20260802/f2_slice_coefficients/verify_slice.py

Every check below is EXACT (zero-testing in Z[zeta_p]) except V7, which
deliberately cross-checks against the already-audited float computation of
the F2A.2 pilot (validate.py V9) to tie the two implementations together.
"""

from __future__ import annotations

import cmath
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from slicecore import (  # noqa: E402
    Cyc, RESULTS, abs_pairs, admissible_orders, carry_sign, deltas_of,
    degree_profile_modes, elem_sym, half_flag, hhat, instance,
    krawtchouk_matrix, mode_pairs, nus_of, omega_pow, phase_index,
    slice_coeffs_bruteforce, slice_coeffs_carrydp, slice_coeffs_modes,
    slice_count_dp, two_cos,
)

FAIL = []


def require(cond, msg):
    if not cond:
        FAIL.append(msg)
        raise AssertionError(msg)


# ---------------------------------------------------------------- V1 ring --

def v1_ring():
    for p in (5, 7, 11, 13):
        require(Cyc.zeta(p, p) == Cyc.one(p), f"zeta^p=1 p={p}")
        s = Cyc.zero(p)
        for i in range(p):
            s = s + Cyc.zeta(p, i)
        require(s.is_zero(), f"sum zeta^i = 0 p={p}")
        require(omega_pow(p, p) == -Cyc.one(p), f"omega^p=-1 p={p}")
        require(omega_pow(p, 2) == Cyc.zeta(p, 1), f"omega^2=zeta p={p}")
        require(omega_pow(p, 0) == Cyc.one(p), "omega^0")
        import mpmath
        mpmath.mp.dps = 60
        for s_ in range(p):
            v = two_cos(p, s_).tocomplex()
            ref = 2 * mpmath.cos(mpmath.pi * s_ / p)
            require(abs(v - ref) < mpmath.mpf(10) ** -50,
                    f"2cos p={p} s={s_}")
            # exact: (2cos)^2 - (2 + zeta^s' + zeta^-s') = 0
            t = two_cos(p, s_)
            require((t * t - (Cyc.one(p) * 2 + Cyc.zeta(p, s_)
                              + Cyc.zeta(p, -s_))).is_zero(), "2cos square")
    print("F2A5_V1_RING_PASS            Z[zeta_p] exact; omega=zeta_2p; 2cos exact")


# ------------------------------------------------- V2 sign bookkeeping ------

def v2_sign_bookkeeping():
    """prod 2cos(pi s/p) == (-1)^{sum u} prod |2cos| exactly (U drops out)."""
    rows = 0
    for p in (7, 11, 13):
        _, _, loc = instance(p, n=6)
        aps = abs_pairs(p, loc)
        for mask in range(1 << len(loc)):
            lhs = Cyc.one(p)
            rhs = Cyc.one(p)
            u = 0
            for i in range(len(loc)):
                ch = (mask >> i) & 1
                s = loc[i][0] if ch else loc[i][1]
                lhs = lhs * two_cos(p, s)
                rhs = rhs * (aps[i][0] if ch else aps[i][1])
                u ^= half_flag(p, s)
            if u:
                rhs = -rhs
            require(lhs == rhs, f"sign bookkeeping p={p} mask={mask}")
            rows += 1
    print(f"F2A5_V2_SIGNS_PASS           (-1)^U cancels the cosine signs; "
          f"rows={rows}")


# ------------------------------------------------ V3 brute == carry DP ------

def v3_brute_vs_dp():
    rows = 0
    for p, n in ((5, 7), (7, 8), (11, 7), (13, 6)):
        for c in ((1, 1), (2, 3), (0, 1)):
            _, _, loc = instance(p, c=(c[0] % p, c[1] % p), n=n)
            if len(loc) < n:
                continue
            a = slice_coeffs_bruteforce(p, loc)
            b = slice_coeffs_carrydp(p, loc)
            require(all(x == y for x, y in zip(a, b)),
                    f"brute vs carryDP p={p} c={c}")
            rows += 1
    print(f"F2A5_V3_SLICE_DP_PASS        brute force == graded carry DP "
          f"(exact); rows={rows}")


# --------------------------------- V4 the b-resolved mode-product identity --

def v4_mode_identity():
    rows = 0
    for p, n in ((5, 6), (7, 7), (11, 6), (13, 5)):
        for c in ((1, 1), (2, 3), (1, 2)):
            _, _, loc = instance(p, c=(c[0] % p, c[1] % p), n=n)
            if len(loc) < n:
                continue
            for k in range(0, 2 * p, 2):
                require(hhat(p, k).is_zero(), f"even mode hhat p={p} k={k}")
            A = slice_coeffs_carrydp(p, loc)
            tot, _ = slice_coeffs_modes(p, loc)
            for b in range(n + 1):
                require((tot[b] - A[b] * (2 * p)).is_zero(),
                        f"mode identity p={p} c={c} b={b}")
            rows += 1
    print(f"F2A5_V4_MODE_IDENTITY_PASS   2p*A_b == sum_k hhat(k) e_b(A(k);B(k)) "
          f"EXACT (b-resolved); rows={rows}")


# --------------------------------------------- V5 per-mode absolute values --

def v5_mode_moduli():
    rows = 0
    for p in (7, 11, 13):
        _, _, loc = instance(p, n=6)
        aps = abs_pairs(p, loc)
        for k in range(2 * p):
            for i, (A, B) in enumerate(mode_pairs(p, k, loc)):
                require((A * A.conj() - aps[i][0] * aps[i][0]).is_zero(),
                        f"|A_i(k)| = a_i^+ p={p} k={k} i={i}")
                require((B * B.conj() - aps[i][1] * aps[i][1]).is_zero(),
                        f"|B_i(k)| = a_i^- p={p} k={k} i={i}")
                rows += 1
    print(f"F2A5_V5_MODE_MODULI_PASS     |A_i(k)| = a_i^+ for EVERY mode "
          f"(so the annealed slice mass E_b is mode-independent); rows={rows}")


# ------------------------------------------------- V6 Krawtchouk identity ---

def v6_krawtchouk():
    rows = 0
    for p, n in ((5, 6), (7, 6), (11, 5)):
        _, _, loc = instance(p, n=n)
        A = slice_coeffs_carrydp(p, loc)
        D = degree_profile_modes(p, loc)   # = 2^n * 2p * D_j
        K = krawtchouk_matrix(n)
        for b in range(n + 1):
            acc = Cyc.zero(p)
            for j in range(n + 1):
                if K[b][j]:
                    acc = acc + D[j] * K[b][j]
            require((acc - A[b] * ((1 << n) * 2 * p)).is_zero(),
                    f"Krawtchouk p={p} b={b}")
            rows += 1
    print(f"F2A5_V6_KRAWTCHOUK_PASS      A_b == sum_j D_j K_j(n-b;n) EXACT "
          f"(slice coeffs = Krawtchouk transform of the degree profile); "
          f"rows={rows}")


# ----------------------------------------- V7 tie-in to the audited pilot ---

def v7_tie_to_f2a2():
    worst = 0.0
    rows = 0
    for p in (5, 7, 11, 13):
        for c in ((0, 1), (1, 1), (1, 0)):
            _, _, loc = instance(p, c=(c[0] % p, c[1] % p), n=7)
            if len(loc) < 7:
                continue
            # audited float route (validate.py V9 style)
            direct = 0.0
            for mask in range(1 << len(loc)):
                r = 0
                par = 0
                wt = 1.0
                for i in range(len(loc)):
                    s = loc[i][0] if (mask >> i) & 1 else loc[i][1]
                    r += s
                    par ^= half_flag(p, s)
                    wt *= 2 * abs(math.cos(math.pi * s / p))
                direct += carry_sign(p, r) * ((-1) ** par) * wt
            exact = sum(x.tocomplex() for x in slice_coeffs_carrydp(p, loc))
            worst = max(worst, abs(complex(exact) - direct)
                        / max(1.0, abs(direct)))
            rows += 1
    require(worst < 1e-9, f"tie-in {worst}")
    print(f"F2A5_V7_TIEIN_PASS           sum_b A_b == the F2A.2 V9 alignment; "
          f"rows={rows} max_rel_err={worst:.1e}")


# -------------------------------------------- V8 the slice-death criterion --

def v8_slice_death():
    """rho_b(k) = 1 for every b  <=>  all phase indices phi_i(k) coincide."""
    hits = 0
    tested = 0
    for p, c in ((11, (1, 1)), (11, (2, 3)), (7, (0, 1)), (13, (0, 1))):
        # c = (0, b) is the trace-zero line: k = p is a KNOWN dead mode
        _, _, loc = instance(p, c=c, n=5)
        aps = abs_pairs(p, loc)
        E = elem_sym(aps)
        d = deltas_of(p, loc)
        nu = nus_of(p, loc)
        for k in range(2 * p):
            phis = {phase_index(p, k, d[i], nu[i]) for i in range(len(loc))}
            e = elem_sym(mode_pairs(p, k, loc))
            allsat = all((e[b] * e[b].conj() - E[b] * E[b]).is_zero()
                         for b in range(len(loc) + 1))
            require(allsat == (len(phis) == 1),
                    f"slice-death p={p} c={c} k={k} phis={phis} sat={allsat}")
            tested += 1
            hits += allsat
    # explicit synthetic witness: all phi_i equal to a COMMON NONZERO value
    print(f"F2A5_V8_SLICEDEATH_PASS      |e_b(k)| == E_b for all b IFF the "
          f"phase indices coincide; modes tested={tested} dead={hits}")


# ------------------------- V9 the two death classes differ (the new fence) --

def v9_two_death_classes():
    """Full-window death needs phi == 0; slice death only needs phi constant.

    Synthetic exact witness in the same ring: pick residues so that every
    phi_i(k) equals the same NONZERO value.  Then the full window contracts
    strictly while every slice ratio is exactly 1.
    """
    p = 7
    # r_i = t_i * omega^{phi}: take A_i = omega^{phi} * B_i with |B_i| free.
    phi = 3
    Bs = [two_cos(p, 1), two_cos(p, 2), two_cos(p, 3), two_cos(p, 1)]
    pairs = [(omega_pow(p, phi) * B, B) for B in Bs]
    absp = []
    for B in Bs:
        absp.append((B, B))   # |A_i| = |B_i| here; both are positive reals
    E = elem_sym(absp)
    e = elem_sym(pairs)
    for b in range(len(Bs) + 1):
        require((e[b] * e[b].conj() - E[b] * E[b]).is_zero(),
                f"common-phase slice ratio 1 at b={b}")
    # full window: |prod (A_i + B_i)| < prod (|A_i| + |B_i|) strictly
    full = Cyc.one(p)
    for A, B in pairs:
        full = full * (A + B)
    ann = Cyc.one(p)
    for a, b_ in absp:
        ann = ann * (a + b_)
    lhs = abs(complex(full.tocomplex()))
    rhs = abs(complex(ann.tocomplex()))
    require(lhs < rhs * 0.999, f"full window must contract: {lhs} vs {rhs}")
    print(f"F2A5_V9_TWO_CLASSES_PASS     common phase {phi}!=0: every slice "
          f"ratio == 1 EXACTLY while the full window contracts "
          f"({lhs:.4f} < {rhs:.4f}) -- slice death class is STRICTLY larger")


# ------------------------------------------------------ V10 counting DP -----

def v10_counting():
    rows = 0
    for p, n in ((7, 8), (11, 7)):
        _, _, loc = instance(p, n=n)
        N = slice_count_dp(p, loc)
        C = [math.comb(n, b) for b in range(n + 1)]
        for b in range(n + 1):
            require(sum(N[b]) == C[b], f"counting DP mass p={p} b={b}")
        # cross-check against brute force
        brute = [[0] * (2 * p) for _ in range(n + 1)]
        for mask in range(1 << n):
            r = 0
            bb = 0
            for i in range(n):
                if (mask >> i) & 1:
                    r += loc[i][0]
                    bb += 1
                else:
                    r += loc[i][1]
            brute[bb][r % (2 * p)] += 1
        require(brute == N, f"counting DP p={p}")
        rows += 1
    print(f"F2A5_V10_COUNTING_PASS       slice x carry counting DP == brute "
          f"force; rows={rows}")


# ------------------------------ V11 the exact k = p slice floor -------------

def v11_kp_floor():
    """hhat_p(p) = 2, and on an all-odd-Delta window |e_b(p)| = E_b EXACTLY,
    so the k = p term alone contributes E_b / p to A_b at EVERY slice b."""
    from slicecore import Delta_of, Fp2, admissible_orders, pair_reps, residues
    rows = 0
    for p in (7, 11, 13, 19):
        require(hhat(p, p) == Cyc.one(p) * 2, f"hhat_p(p) = 2 (p={p})")
        F = Fp2.make(p)
        reps = pair_reps(F, F.subgroup(admissible_orders(p)[-1]))
        for c in ((1, 1), (2, 3)):
            allloc = [residues(F, c, y) for y in reps]
            Dl = Delta_of(p, allloc)
            sel = [i for i in range(len(Dl)) if Dl[i] % 2 == 1][:8]
            if len(sel) < 8:
                continue
            loc = [allloc[i] for i in sel]
            E = elem_sym(abs_pairs(p, loc))
            e = elem_sym(mode_pairs(p, p, loc))
            for b in range(len(loc) + 1):
                # |hhat(p) e_b(p) / 2p| = E_b / p, exactly
                lhs = (e[b] * 2) * (e[b] * 2).conj()
                rhs = (E[b] * 2) * (E[b] * 2)
                require((lhs - rhs).is_zero(), f"k=p floor p={p} c={c} b={b}")
            rows += 1
    print(f"F2A5_V11_KP_FLOOR_PASS       hhat_p(p) = 2 and |e_b(p)| = E_b on "
          f"all-odd-Delta windows: the k=p mode alone puts E_b/p into EVERY "
          f"slice; rows={rows}")


def main():
    os.makedirs(RESULTS, exist_ok=True)
    v1_ring()
    v2_sign_bookkeeping()
    v3_brute_vs_dp()
    v4_mode_identity()
    v5_mode_moduli()
    v6_krawtchouk()
    v7_tie_to_f2a2()
    v8_slice_death()
    v9_two_death_classes()
    v10_counting()
    v11_kp_floor()
    print("F2A5_VALIDATION_ALL_PASS")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""C1'-r3 F-ROUND 2 census (c1r3b). Runs on Modal via tools/modal_run_script.py
(2CPU/16GiB/280s worker; one mode per shard) except the marked LOCAL modes
(ramguard tiny). Pose FROZEN per c1r3_pose.md; falsifiers c1r3b_falsifiers.md
(written first). Exact-rational verdict path throughout; floats are display.

MODES (argv):
  family QMIN QMAX      LOCAL: enumerate gated Proth primes (odd c, k>=20) in
                        [QMIN,QMAX) with v2/octave; asserts vs round-1 counts.
  bench                 benchmark + C-REP worst row q=246415361: T-A/T-B/T-C
                        kernels all timed + asserted against banked E-1; full
                        ledger w2..8 == 0; prints rates for envelope setting.
  controls              C-REP-2 (81788929), C-GROUND (7937), MUT-1 (63361,
                        gate-dropped r2 window must fire) + enumerator revali-
                        dation vs banked orbit counts (w2..6 + w7=131).
  rowA Q1,Q2,...        Tier-A rows: T-A uint64 exact DP -> exact E-1, env,
                        verdict tag (ledger-free; bound (i) certification).
  dpB Q P               Tier-B shard: P=0 -> uint32-wrap (A mod 2^32);
                        else uint32 mod-P. Prints residue + mass check.
  dpC Q P               Tier-C shard: P=0 -> uint16-wrap (A mod 2^16);
                        else uint16 mod-P (P < 2^14).
  assemble Q M1:R1,M2:R2,...   LOCAL: CRT -> exact A, E-1, env, verdict.
  ledger Q              full W_ext ledger w2..8 (fast enumerator + verbatim
                        orbit_key); prints per-weight orbit counts + W_ext.
  l2ladder N QMAX VMIN  LOCAL: L=2 ladder primes q = 1 mod 2N, v2 >= VMIN.
  l2grid Q N [P]        L=2 direct (q,q) grid A_total: N=32 -> uint64 exact
                        single shard; N=64 -> requires P (int64 mod-P shard,
                        3 primes over separate shards, CRT in assemble2).
  l2dirs Q N D0 D1      L=2 strategy-C direction chunk [D0,D1): prints exact
                        partial sum of N_d (python int).
  l2asm Q N S           LOCAL: strategy-C assembly A = (S - 4^N)/q with exact
                        divisibility assert; E-1, env.
  l2ledger Q N          level-2 primitive orbit ledger, window w in [3,9].

Kernels attributed: primitive_root/orbit_key/verbatim enumerator shapes from
m2_c1prime_level_scaled_modal.py via c1r2/c1r3; fast enumerator from
c1r3_census_modal.py; strategy-C identity from m1_dli_m1_tower_census_modal.py
(sum_{d in P^1} [u.d=0] = 1 + q[u=0]).
"""
from __future__ import annotations
import itertools
import sys
import time
from fractions import Fraction
import numpy as np

N32 = 32
GATE = 20
LIT_KILL = Fraction(4)
AMBER2 = Fraction(2)

# banked round-1 exact fractions (c1r3_results.md)
BANKED_EM1 = {
    7937:   Fraction(15584479363607, 144115188075855872),
    63361:  Fraction(2029645184561543, 288230376151711744),
    65921:  Fraction(723593725193615, 144115188075855872),
    204353: Fraction(1498428331827445, 144115188075855872),
}
BANKED_KP_AMBER = {   # W_ext = 0 rows: E-1 = K' * r
    246415361: Fraction(1058880560632659, 1033540934303744),
    81788929:  Fraction(2766759940242725, 2744381056483328),
}
BANKED_ORBITS_W26 = {
    63361:  {2: 0, 3: 1, 4: 3, 5: 10, 6: 36},
}
BANKED_W7 = {63361: 131}
BANKED_WCL = {63361: 76}


def v2(m):
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1
    return k


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def least_primitive_root(q):
    x, d, fac = q - 1, 2, []
    while d * d <= x:
        while x % d == 0:
            fac.append(d)
            x //= d
        d += 1
    if x > 1:
        fac.append(x)
    fac = sorted(set(fac))
    return next(c for c in range(2, q) if all(pow(c, (q - 1) // r, q) != 1 for r in fac))


def get_zeta(q, n):
    assert (q - 1) % n == 0
    z = pow(least_primitive_root(q), (q - 1) // n, q)
    assert pow(z, n, q) == 1 and pow(z, n // 2, q) != 1
    return z


def fmt(fr):
    return f"{fr.numerator}/{fr.denominator}"


# =========================== L=1 DP kernels ===========================
# step polynomial (2 + x^s + x^-s) = (1+x^s)(1+x^-s); factored sub-steps as
# out-of-place slice adds on two preallocated arrays (no temporaries).
def _substep_fwd(src, dst, s, q):
    # dst[i] = src[i] + src[(i-s) mod q]
    np.add(src[s:], src[:q - s], out=dst[s:])
    np.add(src[:s], src[q - s:], out=dst[:s])


def _substep_bwd(src, dst, s, q):
    # dst[i] = src[i] + src[(i+s) mod q]
    np.add(src[:q - s], src[s:], out=dst[:q - s])
    np.add(src[q - s:], src[:s], out=dst[q - s:])


def dp_L1(q, dtype, mod=None):
    """A_total residue DP at L=1, N=32. dtype uint64/uint32/uint16.
    mod=None -> natural wraparound (exact mod 2^{bits}; for uint64 the values
    never exceed 4^step so it is unconditionally exact). mod=p -> A mod p."""
    z = get_zeta(q, 2 * N32)
    dp = np.zeros(q, dtype=dtype)
    dp[0] = 1
    nd = np.empty(q, dtype=dtype)
    for i in range(N32):
        s = pow(z, i, q)
        assert 0 < s < q, "L=1 shift must be a unit"
        _substep_fwd(dp, nd, s, q)
        _substep_bwd(nd, dp, s, q)
        if mod is not None:
            dp %= dtype(mod)
    # mass invariant: total true mass 4^32 = 2^64; wrap kernels check mod 2^bits
    # (4^32 = 0 mod 2^16/2^32/2^64); mod-p kernels check the nontrivial residue.
    tot = int(dp.sum(dtype=np.uint64))   # wraps mod 2^64 for uint64 (fine)
    if mod is None:
        bits = dtype().itemsize * 8
        assert tot % (1 << min(bits, 64)) == 0, f"wrap mass invariant fail q={q}"
    else:
        assert tot % mod == pow(4, N32, mod), f"mod-{mod} mass invariant fail q={q}"
    return int(dp[0])


def em1_env(q, A):
    em1 = Fraction(q * A - (1 << 64), 1 << 64)
    r = Fraction(q, 1 << 32)
    assert em1 > 0, f"E-1 <= 0 at q={q} (integrity)"
    return em1, em1 / r


def find_primes_below(bound, count):
    ps, n = [], bound - 1
    while len(ps) < count:
        if is_prime(n):
            ps.append(n)
        n -= 2
    return ps


# =========================== ledger kernels ===========================
def orbit_key(vector, N):
    best = None
    for shift in range(2 * N):
        moved = [0] * N
        for exponent, coefficient in enumerate(vector):
            if coefficient == 0:
                continue
            target = (exponent + shift) % (2 * N)
            if target >= N:
                moved[target - N] -= coefficient
            else:
                moved[target] += coefficient
        key = tuple(moved)
        if best is None or key < best:
            best = key
    return best


def combo_chunks(N, w, chunk):
    combos = itertools.combinations(range(N), w)
    while True:
        block = list(itertools.islice(combos, chunk))
        if not block:
            return
        yield np.asarray(block, dtype=np.int64)


def primitive_orbit_count_fast(q, weight, N=32):
    omega = get_zeta(q, 2 * N)
    pw = np.array([pow(omega, e, q) for e in range(N)], dtype=np.int64)
    signs = np.array(list(itertools.product((1, -1), repeat=weight - 1)), dtype=np.int64)
    signs = np.hstack([np.ones((len(signs), 1), dtype=np.int64), signs])
    masks = np.arange(1 << weight, dtype=np.int64)
    subset = ((masks[:, None] >> np.arange(weight)) & 1).astype(np.int64)
    proper = (masks != 0) & (masks != (1 << weight) - 1)
    reps = set()
    for supports in combo_chunks(N, weight, 100_000):
        vals = pw[supports]
        hit = (vals @ signs.T) % q == 0
        idx = np.argwhere(hit)
        if len(idx) == 0:
            continue
        hv = vals[idx[:, 0]] * signs[idx[:, 1]]
        ss = (hv @ subset.T) % q
        prim = ~np.any(ss[:, proper] == 0, axis=1)
        for si, gi in idx[prim]:
            support = supports[si]
            signed = signs[gi]
            vector = [0] * N
            for e, c in zip(support, signed):
                vector[int(e)] = int(c)
            reps.add(orbit_key(tuple(vector), N))
    return len(reps)


def ledger_of(counts, N):
    return sum(Fraction(counts[w] * 2 * N, 2 ** w) for w in counts)


# level-2 joint-vanishing primitive orbit enumerator (chars 1 and 3)
def primitive_orbit_count_L2(q, weight, N=32):
    omega = get_zeta(q, 2 * N)
    pw1 = np.array([pow(omega, e, q) for e in range(N)], dtype=np.int64)
    # omega has order 2N so omega^(3e) = omega^(3e mod 2N) (verbatim-equal)
    pw3 = np.array([pow(omega, (3 * e) % (2 * N), q) for e in range(N)], dtype=np.int64)
    signs = np.array(list(itertools.product((1, -1), repeat=weight - 1)), dtype=np.int64)
    signs = np.hstack([np.ones((len(signs), 1), dtype=np.int64), signs])
    masks = np.arange(1 << weight, dtype=np.int64)
    subset = ((masks[:, None] >> np.arange(weight)) & 1).astype(np.int64)
    proper = (masks != 0) & (masks != (1 << weight) - 1)
    reps = set()
    for supports in combo_chunks(N, weight, 100_000):
        v1 = pw1[supports]
        v3 = pw3[supports]
        hit = ((v1 @ signs.T) % q == 0) & ((v3 @ signs.T) % q == 0)
        idx = np.argwhere(hit)
        if len(idx) == 0:
            continue
        hv1 = v1[idx[:, 0]] * signs[idx[:, 1]]
        hv3 = v3[idx[:, 0]] * signs[idx[:, 1]]
        ss1 = (hv1 @ subset.T) % q
        ss3 = (hv3 @ subset.T) % q
        prim = ~np.any((ss1[:, proper] == 0) & (ss3[:, proper] == 0), axis=1)
        for si, gi in idx[prim]:
            support = supports[si]
            signed = signs[gi]
            vector = [0] * N
            for e, c in zip(support, signed):
                vector[int(e)] = int(c)
            reps.add(orbit_key(tuple(vector), N))
    return len(reps)


# =========================== L=2 kernels ===========================
def dp_L2_grid(q, N, mod=None):
    """Direct (q,q) joint DP, steps (z^i, z^{3i}), i in 0..N-1.
    mod=None: uint64 (exact for N=32: mass 4^32 = 2^64, A < 2^64 strictly).
    mod=p (int64, p < 2^49): residue for N=64 CRT (row sums stay < 2^63)."""
    assert 16 * q * q <= 15_000_000_000, f"L2 grid q={q} exceeds memory law"
    assert q * q <= (1 << N), "H2 violated at L=2"
    z = get_zeta(q, 2 * N)
    dtype = np.uint64 if mod is None else np.int64
    if mod is not None:
        assert mod < (1 << 49)
    dp = np.zeros((q, q), dtype=dtype)
    dp[0, 0] = 1
    nd = np.empty((q, q), dtype=dtype)

    def sub2(src, dst, a, b):
        # dst[i,j] = src[i,j] + src[(i-a) mod q, (j-b) mod q]
        np.add(src[a:, b:], src[:q - a, :q - b], out=dst[a:, b:])
        np.add(src[a:, :b], src[:q - a, q - b:], out=dst[a:, :b])
        np.add(src[:a, b:], src[q - a:, :q - b], out=dst[:a, b:])
        np.add(src[:a, :b], src[q - a:, q - b:], out=dst[:a, :b])

    for i in range(N):
        a = pow(z, i, q)
        b = pow(z, (3 * i) % (2 * N), q)
        assert 0 < a < q and 0 < b < q
        sub2(dp, nd, a, b)                      # (1 + X^a Y^b)
        sub2(nd, dp, (q - a) % q, (q - b) % q)  # (1 + X^-a Y^-b)
        if mod is not None:
            dp %= mod
    if mod is None:
        tot = int(dp.sum(dtype=np.uint64))      # wraps mod 2^64
        assert tot == pow(4, N, 1 << 64), f"L2 grid mass invariant fail q={q}"
    else:
        # per-row sums fit uint64 (q * p < 2^63.5 for p < 2^49, q <= 20000)
        rows = dp.sum(axis=1, dtype=np.uint64)
        tot = sum(int(x) for x in rows)
        assert tot % mod == pow(4, N, mod), f"L2 grid mod-{mod} mass fail q={q}"
    return int(dp[0, 0])


def dp_L2_dirs(q, N, d0, d1):
    """Strategy-C: sum over projective directions index in [d0,d1) of N_d.
    Directions: index t in [0, q) -> d = (1, t); index q -> d = (0, 1).
    N_d = #{walks: sum eps_y sigma_y(d) = 0 mod q}, sigma_y = d0*z^y + d1*z^{3y}.
    uint64 wraparound exact for N=32 (N_d < 2^64: at most one zero shift)."""
    assert N == 32, "strategy-C uint64 path is N=32 only this round"
    z = get_zeta(q, 2 * N)
    zp = [pow(z, i, q) for i in range(N)]
    zp3 = [pow(z, (3 * i) % (2 * N), q) for i in range(N)]
    total = 0
    dp = np.empty(q, dtype=np.uint64)
    nd = np.empty(q, dtype=np.uint64)
    for t in range(d0, d1):
        if t == q:
            sig = [zp3[i] for i in range(N)]
        else:
            sig = [(zp[i] + t * zp3[i]) % q for i in range(N)]
        dp[:] = 0
        dp[0] = 1
        nzero = 0
        for i in range(N):
            s = sig[i]
            if s == 0:
                nzero += 1
                dp *= np.uint64(4)
                continue
            _substep_fwd(dp, nd, s, q)
            _substep_bwd(nd, dp, s, q)
        assert nzero <= 1, f"more than one zero shift at q={q} d={t}"
        assert int(dp.sum(dtype=np.uint64)) == pow(4, N, 1 << 64), \
            f"strategy-C mass fail q={q} d={t}"
        total += int(dp[0])
    return total


# =========================== modes ===========================
def do_family(qmin, qmax):
    fam = []
    k = GATE
    while (1 << k) < qmax:
        c = 1
        while c * (1 << k) + 1 < qmax:
            q = c * (1 << k) + 1
            if v2(q - 1) == k and is_prime(q):
                fam.append((q, k, c))
            c += 2
        k += 1
    fam.sort()
    below = [t for t in fam if t[0] < (1 << 28)]
    seg = [t for t in fam if (1 << 28) <= t[0] < (1 << 32)]
    print(f"# gated Proth family q<2^32: {len(fam)} primes; below 2^28: {len(below)}; segment: {len(seg)}")
    assert len(fam) == 401 and len(below) == 33 and len(seg) == 368, \
        f"family counts {len(fam)}/{len(below)}/{len(seg)} != banked 401/33/368"
    out = [t for t in fam if qmin <= t[0] < qmax]
    octs = {}
    for q, k, c in out:
        o = q.bit_length() - 1
        octs.setdefault(o, []).append(q)
        print(f"q={q:>12}  c={c:>7}  v2={k:>2}  octave=2^{o}")
    print("# octaves:", {o: len(v) for o, v in sorted(octs.items())})
    assert out, "NONEMPTINESS: requested family window empty"


def _timed_dp(q, tag, dtype, mod):
    t0 = time.time()
    a = dp_L1(q, dtype, mod)
    dt = time.time() - t0
    passes = 6 + (2 if mod is not None else 0)
    rate = passes * dtype().itemsize * q * N32 / dt / 1e9
    print(f"  [{tag}] q={q} res={a} time={dt:.1f}s eff-rate={rate:.2f}GB/s")
    return a, dt


def do_bench():
    q = 246415361
    print(f"# BENCH + C-REP-1 at q={q} (round-1 worst row)")
    A, tA = _timed_dp(q, "T-A uint64", np.uint64, None)
    em1, env = em1_env(q, A)
    exp = BANKED_KP_AMBER[q] * Fraction(q, 1 << 32)
    assert em1 == exp, f"C-REP-1 FAIL: E-1 {fmt(em1)} != banked {fmt(exp)}"
    print(f"  C-REP-1 PASS: E-1 == banked; env={float(env):.9f} K'_r3(banked)={float(BANKED_KP_AMBER[q]):.9f}")
    r32, t32 = _timed_dp(q, "T-B uint32-wrap", np.uint32, None)
    assert r32 == A % (1 << 32), "uint32-wrap mismatch"
    p30 = find_primes_below(1 << 30, 2)
    rp1, tp1 = _timed_dp(q, f"T-B mod-{p30[0]}", np.uint32, p30[0])
    assert rp1 == A % p30[0], "uint32 mod-p mismatch"
    rp2, tp2 = _timed_dp(q, f"T-B mod-{p30[1]}", np.uint32, p30[1])
    assert rp2 == A % p30[1], "uint32 mod-p2 mismatch"
    # CRT assemble check for T-B trio
    x = crt([(1 << 32, r32), (p30[0], rp1), (p30[1], rp2)])
    assert x == A, "T-B CRT reconstruction != exact A"
    print(f"  T-B trio CRT == exact A  PASS (modulus 2^32*{p30[0]}*{p30[1]})")
    r16, t16 = _timed_dp(q, "T-C uint16-wrap", np.uint16, None)
    assert r16 == A % (1 << 16), "uint16-wrap mismatch"
    p14 = find_primes_below(1 << 14, 4)
    res16 = []
    tC = t16
    for p in p14:
        rp, tp = _timed_dp(q, f"T-C mod-{p}", np.uint16, p)
        assert rp == A % p, f"uint16 mod-{p} mismatch"
        res16.append((p, rp))
        tC = max(tC, tp)
    M = (1 << 16)
    for p, _ in res16:
        M *= p
    assert M > (1 << 64), "T-C modulus insufficient"
    x = crt([(1 << 16, r16)] + res16)
    assert x == A, "T-C CRT reconstruction != exact A"
    print(f"  T-C quint CRT == exact A  PASS (modulus {M} > 2^64)")
    t0 = time.time()
    counts = {w: primitive_orbit_count_fast(q, w) for w in range(2, 9)}
    tl = time.time() - t0
    assert all(c == 0 for c in counts.values()), f"C-REP-1 ledger not empty: {counts}"
    print(f"  C-REP-1 ledger w2..8 all ZERO == banked W_ext=0  PASS  ({tl:.1f}s)")
    print(f"# RATES: uint64 {tA:.1f}s  u32wrap {t32:.1f}s  u32modp {max(tp1, tp2):.1f}s  "
          f"u16 worst {tC:.1f}s  ledger {tl:.1f}s at q={q}")
    print(f"# envelope guide (235s): Q_A^time ~ {int(q * 235 / tA)}  "
          f"Q_B^time ~ {int(q * 235 / max(tp1, tp2))}  Q_C^time ~ {int(q * 235 / tC)}")


def crt(pairs):
    M = 1
    for m, _ in pairs:
        M *= m
    x = 0
    for m, r in pairs:
        Mm = M // m
        x = (x + r * Mm * pow(Mm, -1, m)) % M
    return x


def do_controls():
    # C-REP-2
    q = 81788929
    A = dp_L1(q, np.uint64, None)
    em1, env = em1_env(q, A)
    exp = BANKED_KP_AMBER[q] * Fraction(q, 1 << 32)
    assert em1 == exp, f"C-REP-2 FAIL at {q}"
    counts = {w: primitive_orbit_count_fast(q, w) for w in range(2, 9)}
    assert all(c == 0 for c in counts.values()), f"C-REP-2 ledger not empty: {counts}"
    print(f"C-REP-2 PASS: q={q} E-1 == banked, W_ext == 0, K'_r3={float(env):.9f}")
    # C-GROUND
    A = dp_L1(7937, np.uint64, None)
    em1, env = em1_env(7937, A)
    assert em1 == BANKED_EM1[7937], "C-GROUND FAIL"
    print(f"C-GROUND PASS: q=7937 E-1 == banked; env={float(env):.6f}")
    # MUT-1 + enumerator revalidation at 63361 (gate-dropped, r2 window [2,6])
    q = 63361
    assert v2(q - 1) < GATE  # out of hypothesis - mutation row
    A = dp_L1(q, np.uint64, None)
    em1, env = em1_env(q, A)
    assert em1 == BANKED_EM1[q], "MUT-1 E-1 mismatch"
    counts = {w: primitive_orbit_count_fast(q, w) for w in range(2, 8)}
    assert {w: counts[w] for w in range(2, 7)} == BANKED_ORBITS_W26[q], f"orbit mismatch {counts}"
    assert counts[7] == BANKED_W7[q], f"w7 mismatch {counts[7]}"
    led = ledger_of({w: counts[w] for w in range(2, 7)}, N32)
    assert led == BANKED_WCL[q], "W_cl mismatch"
    r = Fraction(q, 1 << 32)
    kp = em1 / (r * (1 + led))
    fired = em1 > LIT_KILL * r * (1 + led)
    assert fired and float(kp) > 6.19, "MUT-1 FAILED TO FIRE"
    print(f"MUT-1 PASS: q=63361 gate-dropped r2-window K'={float(kp):.6f} > 4 fires; "
          f"enumerator revalidated (w2..6 + w7 == banked)")
    print("CONTROLS ALL PASS")


def do_rowA(qs):
    for q in qs:
        assert v2(q - 1) >= GATE and q < (1 << 32), f"row q={q} out of hypothesis"
        t0 = time.time()
        A = dp_L1(q, np.uint64, None)
        dt = time.time() - t0
        em1, env = em1_env(q, A)
        assert env > Fraction(1, 10 ** 6), f"MUT-2 FAIL at q={q}"
        tag = ("survives(env<1)" if env < 1 else
               "LEGACY-BAND-CANDIDATE(needs ledger)" if env < 2 else
               "AMBER2-CANDIDATE(NEEDS LEDGER)" if env <= 4 else
               "LITERAL-CANDIDATE(NEEDS LEDGER)")
        print(f"ROW q={q} v2={v2(q - 1)} A={A} time={dt:.1f}s")
        print(f"    E-1={fmt(em1)}")
        print(f"    env={fmt(env)} float={float(env):.9f} -> {tag}")


def do_dpB(qs, p):
    for q in qs:
        assert v2(q - 1) >= GATE and q < (1 << 32)
        if p == 0:
            a, dt = _timed_dp(q, "u32wrap", np.uint32, None)
            print(f"DPB q={q} mod={1 << 32} res={a}")
        else:
            assert is_prime(p) and p <= (1 << 30)
            a, dt = _timed_dp(q, f"u32mod{p}", np.uint32, p)
            print(f"DPB q={q} mod={p} res={a}")


def do_dpC(qs, p):
    for q in qs:
        assert v2(q - 1) >= GATE and q < (1 << 32)
        if p == 0:
            a, dt = _timed_dp(q, "u16wrap", np.uint16, None)
            print(f"DPC q={q} mod={1 << 16} res={a}")
        else:
            assert is_prime(p) and p < (1 << 14)
            a, dt = _timed_dp(q, f"u16mod{p}", np.uint16, p)
            print(f"DPC q={q} mod={p} res={a}")


def do_dpBrow2(q):
    """One Tier-B row, shard 1 of 2: uint32-wrap + mod-p1 together."""
    assert v2(q - 1) >= GATE and q < (1 << 32)
    p1 = find_primes_below(1 << 30, 1)[0]
    a, _ = _timed_dp(q, "u32wrap", np.uint32, None)
    print(f"DPB q={q} mod={1 << 32} res={a}")
    a, _ = _timed_dp(q, f"u32mod{p1}", np.uint32, p1)
    print(f"DPB q={q} mod={p1} res={a}")


def do_row918():
    """The mandated deferred accident row: q=918552577 (v2=22, the unique
    in-gate w<=6 carrier below 2^32). Full pipeline in one shard: T-A uint64
    exact DP + independent uint32 mod-p cross-shard + FULL ledger w2..8 +
    exact K'_r3 verdict."""
    q = 918552577
    assert v2(q - 1) == 22 and is_prime(q)
    A, tA = _timed_dp(q, "T-A uint64", np.uint64, None)
    p = find_primes_below(1 << 30, 1)[0]
    rp, tp = _timed_dp(q, f"xcheck mod-{p}", np.uint32, p)
    assert rp == A % p, f"918552577 mod-p CROSS-CHECK FAIL: {rp} != A mod {p}"
    print(f"  cross-check A mod {p} agrees (independent uint32 kernel)")
    em1, env = em1_env(q, A)
    t0 = time.time()
    counts = {w: primitive_orbit_count_fast(q, w) for w in range(2, 9)}
    led = ledger_of(counts, N32)
    r = Fraction(q, 1 << 32)
    kp = em1 / (r * (1 + led))
    lit = em1 > LIT_KILL * r * (1 + led)
    amb2 = kp >= AMBER2
    verdict = "LITERAL-KILL" if lit else ("AMBER-2" if amb2 else
              ("legacy-band[1,2)" if kp >= 1 else "survives"))
    w6mass = Fraction(counts[6] * 2 * N32, 2 ** 6)
    print(f"ROW918 q={q} v2=22 A={A} ledger_time={time.time() - t0:.1f}s")
    print(f"    E-1={fmt(em1)}")
    print(f"    env={fmt(env)} float={float(env):.9f}")
    print(f"    orbits w2..8={counts}  W_ext={fmt(led)}  w6 orbit mass={fmt(w6mass)}")
    print(f"    K'_r3={fmt(kp)} float={float(kp):.9f} -> {verdict}")
    assert kp > Fraction(1, 10 ** 6), "MUT-2 FAIL at 918552577"


def do_assemble(q, pairs):
    M = 1
    for m, _ in pairs:
        M *= m
    assert M > (1 << 64), f"assemble modulus {M} insufficient"
    A = crt(pairs)
    assert A < (1 << 64), "reconstructed A out of proved range"
    em1, env = em1_env(q, A)
    assert env > Fraction(1, 10 ** 6), f"MUT-2 FAIL at q={q}"
    tag = ("survives(env<1)" if env < 1 else
           "LEGACY-BAND-CANDIDATE(needs ledger)" if env < 2 else
           "AMBER2-CANDIDATE(NEEDS LEDGER)" if env <= 4 else
           "LITERAL-CANDIDATE(NEEDS LEDGER)")
    print(f"ROW q={q} v2={v2(q - 1)} A={A} [CRT modulus {M}]")
    print(f"    E-1={fmt(em1)}")
    print(f"    env={fmt(env)} float={float(env):.9f} -> {tag}")


def do_ledger(qs):
    for q in qs:
        t0 = time.time()
        counts = {w: primitive_orbit_count_fast(q, w) for w in range(2, 9)}
        led = ledger_of(counts, N32)
        print(f"LEDGER q={q} v2={v2(q - 1)} orbits w2..8={counts} W_ext={fmt(led)} "
              f"({time.time() - t0:.1f}s)")


def do_l2ladder(N, qmax, vmin):
    rows = []
    for q in range(2 * N + 1, qmax + 1, 2 * N):
        if is_prime(q) and v2(q - 1) >= vmin:
            rows.append((v2(q - 1), q))
    rows.sort(reverse=True)
    print(f"# L=2 ladder N={N} (q = 1 mod {2 * N}, q <= {qmax}, v2 >= {vmin}): {len(rows)} rows")
    for v, q in rows:
        print(f"q={q:>8} v2={v:>2} qq={q * q} grid_bytes_x2={16 * q * q}")
    assert rows, "NONEMPTINESS: L=2 ladder empty"


def do_l2grid(q, N, p=None):
    t0 = time.time()
    if N == 32:
        A = dp_L2_grid(q, 32, None)
        em1 = Fraction(q * q * A - (1 << 64), 1 << 64)
        assert em1 > 0, f"E-1 <= 0 at L2 q={q}"
        r = Fraction(q * q, 1 << 32)
        env = em1 / r
        print(f"L2GRID q={q} N=32 A={A} time={time.time() - t0:.1f}s")
        print(f"    E-1={fmt(em1)} env={fmt(env)} float={float(env):.9f}")
    else:
        assert N == 64 and p is not None and is_prime(p) and p < (1 << 49)
        res = dp_L2_grid(q, 64, p)
        print(f"L2GRID q={q} N=64 mod={p} res={res} time={time.time() - t0:.1f}s")


def do_l2crt(q, N, pairs):
    M = 1
    for m, _ in pairs:
        M *= m
    assert M > 4 ** N, f"L2 CRT modulus insufficient ({M} <= 4^{N})"
    A = crt(pairs)
    em1 = Fraction(q * q * A, 4 ** N) - 1
    assert em1 > 0, f"E-1 <= 0 at L2 q={q}"
    r = Fraction(q * q, 1 << N)
    env = em1 / r
    print(f"L2CRT q={q} N={N} A={A} [modulus {M}]")
    print(f"    E-1={fmt(em1)} env={fmt(env)} float={float(env):.9f}")


def do_l2dirs(q, N, d0, d1):
    assert 0 <= d0 < d1 <= q + 1, "direction chunk out of range"
    t0 = time.time()
    s = dp_L2_dirs(q, N, d0, d1)
    print(f"L2DIRS q={q} N={N} dirs=[{d0},{d1}) partial_sum={s} time={time.time() - t0:.1f}s")


def do_l2asm(q, N, S):
    num = S - 4 ** N
    assert num % q == 0, f"strategy-C divisibility FAIL at q={q} (integrity)"
    A = num // q
    assert A >= 0
    em1 = Fraction(q * q * A, 4 ** N) - 1
    r = Fraction(q * q, 1 << N)
    env = em1 / r
    print(f"L2ASM q={q} N={N} A={A} (divisibility exact PASS)")
    print(f"    E-1={fmt(em1)} env={fmt(env)} float={float(env):.9f}")


def do_l2ledger(q, N):
    t0 = time.time()
    counts = {w: primitive_orbit_count_L2(q, w, N=N) for w in range(3, 10)}
    led = sum(Fraction(counts[w] * 2 * N, 2 ** w) for w in counts)
    print(f"L2LEDGER q={q} N={N} orbits w3..9={counts} W_ext={fmt(led)} "
          f"({time.time() - t0:.1f}s)")


def do_smoke():
    """LOCAL (ramguard tiny): kernel algebra validation at toy scale, no Modal
    spend. T-A/T-B/T-C agreement at q=7937 vs banked E-1; L2 grid == strategy-C
    at q in {193, 257} (N=32)."""
    A = dp_L1(7937, np.uint64, None)
    em1, env = em1_env(7937, A)
    assert em1 == BANKED_EM1[7937], f"smoke T-A FAIL {fmt(em1)}"
    r32 = dp_L1(7937, np.uint32, None)
    p30 = find_primes_below(1 << 30, 2)
    rp = [dp_L1(7937, np.uint32, p) for p in p30]
    assert crt([(1 << 32, r32), (p30[0], rp[0]), (p30[1], rp[1])]) == A, "smoke T-B FAIL"
    r16 = dp_L1(7937, np.uint16, None)
    p14 = find_primes_below(1 << 14, 4)
    rq = [dp_L1(7937, np.uint16, p) for p in p14]
    assert crt([(1 << 16, r16)] + list(zip(p14, rq))) == A, "smoke T-C FAIL"
    print(f"smoke T-A/T-B/T-C PASS at q=7937 (E-1 == banked, env={float(env):.6f})")
    for q in (193, 257):
        Ag = dp_L2_grid(q, 32, None)
        S = dp_L2_dirs(q, 32, 0, q + 1)
        num = S - 4 ** 32
        assert num % q == 0, f"smoke L2 divisibility FAIL q={q}"
        assert num // q == Ag, f"smoke L2 strategy-C != grid at q={q}"
        em1 = Fraction(q * q * Ag - (1 << 64), 1 << 64)
        print(f"smoke L2 PASS q={q}: grid == strategy-C, A={Ag}, "
              f"env={float(em1 / Fraction(q * q, 1 << 32)):.6f}")
    print("SMOKE ALL PASS")


def main():
    mode = sys.argv[1]
    if mode == "smoke":
        do_smoke()
    elif mode == "family":
        do_family(int(sys.argv[2]), int(sys.argv[3]))
    elif mode == "bench":
        do_bench()
    elif mode == "controls":
        do_controls()
    elif mode == "rowA":
        do_rowA([int(x) for x in sys.argv[2].split(",") if x])
    elif mode == "dpB":
        do_dpB([int(x) for x in sys.argv[2].split(",") if x], int(sys.argv[3]))
    elif mode == "dpC":
        do_dpC([int(x) for x in sys.argv[2].split(",") if x], int(sys.argv[3]))
    elif mode == "row918":
        do_row918()
    elif mode == "dpBrow2":
        do_dpBrow2(int(sys.argv[2]))
    elif mode == "assemble":
        pairs = [tuple(int(v) for v in t.split(":")) for t in sys.argv[3].split(",")]
        do_assemble(int(sys.argv[2]), pairs)
    elif mode == "ledger":
        do_ledger([int(x) for x in sys.argv[2].split(",") if x])
    elif mode == "l2ladder":
        do_l2ladder(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif mode == "l2grid":
        do_l2grid(int(sys.argv[2]), int(sys.argv[3]),
                  int(sys.argv[4]) if len(sys.argv) > 4 else None)
    elif mode == "l2grids":
        for qq in (int(x) for x in sys.argv[2].split(",") if x):
            do_l2grid(qq, int(sys.argv[3]), None)
    elif mode == "l2dirs":
        do_l2dirs(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
    elif mode == "l2asm":
        do_l2asm(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif mode == "l2crt":
        pairs = [tuple(int(v) for v in t.split(":")) for t in sys.argv[4].split(",")]
        do_l2crt(int(sys.argv[2]), int(sys.argv[3]), pairs)
    elif mode == "l2ledger":
        do_l2ledger(int(sys.argv[2]), int(sys.argv[3]))
    else:
        raise SystemExit(f"unknown mode {mode}")


if __name__ == "__main__":
    main()

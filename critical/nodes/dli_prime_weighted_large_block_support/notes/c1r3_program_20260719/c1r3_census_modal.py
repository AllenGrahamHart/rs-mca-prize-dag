#!/usr/bin/env python3
"""C1'-r3 F-ROUND 1 census (runs on Modal via tools/modal_run_script.py, single
2CPU/16GiB/280s worker; shard per mode). RAW ledger, L=1 analogue rows, gate
v_2(q-1) >= 20 (Proth family), EXTENDED window w in [L+1, L+7]. Exact-rational
verdict path. Pose: c1r3_pose.md; falsifiers: c1r3_falsifiers.md (frozen first).

MODES (argv):
  family KMIN QMAX     : enumerate gated Proth primes q=c*2^k+1 (odd c, k>=KMIN,
                         q<QMAX) with v_2 and octave. (local-tiny safe)
  ground               : local grounding — q=7937 A_total DP vs banked E-1.
  controls             : PC1 (verbatim w2..6 ledger, r2 window, rows 7937/63361/
                         65921/204353, exact-fraction asserts) + PC2 (gate
                         excludes killers) + M1 mutation (must fire).
  reprice Q1,Q2,...    : PC3 — killers under the r3 extended ledger w2..8, gate
                         ignored; xval optimized-vs-verbatim w2..6 + w7 vs the
                         banked window-probe counts; exact K'_ext.
  row Q1,Q2,...        : full r3 row evaluation at in-gate rows: DP E, optimized
                         W_ext (w2..8), exact K'_r3, verdict, M2/M3 mutations.
  dpx Q                : two-path A_total check (my DP vs verbatim
                         signed_all_census) at one gated row.
  w3census             : analogue weight-3 norm census: all 19,840 reduced signed
                         weight-3 polys at order 64, exact CRT-certified
                         Res(X^32+1,P), full factorization, max v_2(p-1).
  accscan KMIN         : direct vanisher scan (w=3,4,5,6 presence counts) over
                         ALL gated Proth primes q < 2^32.
  aspect Q1,Q2         : N=64 aspect probe — exact (E-1)/r via CRT-DP + PARTIAL
                         ledger w2..6 (survival-only instrument).

Kernels reused (attributed):
  * primitive_orbit_count, primitive_root, orbit_key  <- VERBATIM from
    critical/nodes/dli_prime_weighted_large_block_support/notes/
    m2_c1prime_level_scaled_modal.py via c1r2_census_modal.py / c1r2_verify_kill.py
  * signed_all_census, fiber_contribs, get_zeta, least_primitive_root
    <- VERBATIM from m1_dli_m1_tower_census_modal.py via c1r2_verify_kill.py
  * A_total DP  <- c1r2_census_modal.py (memory-lean variant, exact hi/lo mass
    invariant added).
"""
from __future__ import annotations
import itertools
import sys
from fractions import Fraction
import numpy as np

N32 = 32
GATE = 20                 # analogue official-admissibility gate v_2(q-1) >= 20
LIT_KILL = Fraction(4)    # E-1 > 4 r (1+W_ext)  <=>  K'_r3 > 4  (allowance unchanged)
AMBER = Fraction(1)

# banked r2/probe constants (kill packet c1r2_fround2_20260713)
BANKED_EM1 = {
    7937:   Fraction(15584479363607, 144115188075855872),
    63361:  Fraction(2029645184561543, 288230376151711744),
    65921:  Fraction(723593725193615, 144115188075855872),
    204353: Fraction(1498428331827445, 144115188075855872),
}
BANKED_ORBITS_W26 = {
    7937:   {2: 0, 3: 2, 4: 8, 5: 31, 6: 126},
    63361:  {2: 0, 3: 1, 4: 3, 5: 10, 6: 36},
    65921:  {2: 0, 3: 1, 4: 3, 5: 9, 6: 34},
    204353: {2: 0, 3: 1, 4: 3, 5: 6, 6: 18},
}
BANKED_WCL = {7937: 236, 63361: 76, 65921: 72, 204353: 50}
BANKED_W7 = {63361: 131, 65921: 119, 204353: 45}        # window-probe w7 orbit counts
BANKED_K_W7 = {63361: 3.3497, 65921: 2.4689, 204353: 2.9732}  # float display refs


def v2(m):
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1
    return k


def is_prime(n):
    """Deterministic Miller-Rabin for n < 3.3e24 (covers all q < 2^64 here)."""
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


# ---- field helpers (verbatim shape) ----
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


# ---- exact E via A_total DP (L=1, memory-lean; exact mass invariant) ----
def a_total_L1(q, N):
    z = get_zeta(q, 2 * N)
    dp = np.zeros(q, dtype=np.int64)
    dp[0] = 1
    for i in range(N):
        s = pow(z, i % (2 * N), q)
        nd = dp * 2
        t = np.roll(dp, s); nd += t; del t
        t = np.roll(dp, (q - s) % q); nd += t; del t
        assert int(nd.max()) < (1 << 62), f"int64 headroom guard tripped q={q}"
        dp = nd
    lo = int((dp & 0xFFFFFFFF).sum(dtype=np.int64))
    hi = int((dp >> 32).sum(dtype=np.int64))
    total = lo + (hi << 32)
    assert total == 4 ** N, f"MASS INVARIANT FAIL q={q}: {total} != 4^{N}"
    return int(dp[0])


def a_total_L1_crt(q, N):
    """Exact A_total for large 4^N (N=64) via CRT over int64-safe prime moduli."""
    PRIMES = [(1 << 60) - 93, (1 << 60) - 107, (1 << 60) - 173]  # verified primes < 2^60
    assert all(is_prime(p) for p in PRIMES)
    z = get_zeta(q, 2 * N)
    residues = []
    for p in PRIMES:
        dp = np.zeros(q, dtype=np.int64)
        dp[0] = 1
        for i in range(N):
            s = pow(z, i % (2 * N), q)
            nd = dp * 2
            t = np.roll(dp, s); nd += t; del t
            t = np.roll(dp, (q - s) % q); nd += t; del t
            nd %= p
            dp = nd
        lo = int((dp & 0xFFFFFFFF).sum(dtype=np.int64))
        hi = int((dp >> 32).sum(dtype=np.int64))
        assert (lo + (hi << 32)) % p == pow(4, N, p), f"mod-{p} mass invariant fail q={q}"
        residues.append(int(dp[0]))
    M = 1
    for p in PRIMES:
        M *= p
    assert M > 4 ** N, "CRT modulus insufficient"
    x = 0
    for p, r in zip(PRIMES, residues):
        Mp = M // p
        x = (x + r * Mp * pow(Mp, -1, p)) % M
    return x


def em1_r(q, N, A):
    em1 = Fraction(q * A, 4 ** N) - 1
    r = Fraction(q, 2 ** N)
    assert em1 > 0, f"E-1 <= 0 at q={q} (integrity)"
    return em1, r


# ===== VERBATIM kernels (m2 via c1r2) =====
def primitive_root(q):
    remaining = q - 1
    factors = set()
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors.add(divisor)
            remaining //= divisor
        divisor += 1
    if remaining > 1:
        factors.add(remaining)
    candidate = 2
    while any(pow(candidate, (q - 1) // factor, q) == 1 for factor in factors):
        candidate += 1
    return candidate


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


def primitive_orbit_count_verbatim(q, level, weight, N=32):
    omega = pow(primitive_root(q), (q - 1) // (2 * N), q)
    odd_powers = [
        np.array([pow(omega, (2 * ell - 1) * exponent, q) for exponent in range(N)], dtype=np.int64)
        for ell in range(1, level + 1)
    ]
    signs = np.array(list(itertools.product((1, -1), repeat=weight - 1)), dtype=np.int64)
    signs = np.hstack([np.ones((len(signs), 1), dtype=np.int64), signs])
    combinations = itertools.combinations(range(N), weight)
    representatives = set()
    chunk_size = 100_000
    while True:
        chunk = list(itertools.islice(combinations, chunk_size))
        if not chunk:
            break
        supports = np.asarray(chunk, dtype=np.int64)
        hit_mask = np.ones((len(supports), len(signs)), dtype=bool)
        for powers in odd_powers:
            hit_mask &= (powers[supports] @ signs.T) % q == 0
        for support_index, sign_index in np.argwhere(hit_mask):
            support = tuple(int(value) for value in supports[support_index])
            signed = tuple(int(value) for value in signs[sign_index])
            primitive = True
            for subset_mask in range(1, (1 << weight) - 1):
                if all(sum(signed[index] * pow(omega, (2 * ell - 1) * support[index], q)
                           for index in range(weight) if (subset_mask >> index) & 1) % q != 0
                       for ell in range(1, level + 1)):
                    continue
                if all(sum(signed[index] * pow(omega, (2 * ell - 1) * support[index], q)
                           for index in range(weight) if (subset_mask >> index) & 1) % q == 0
                       for ell in range(1, level + 1)):
                    primitive = False
                    break
            if not primitive:
                continue
            vector = [0] * N
            for exponent, coefficient in zip(support, signed):
                vector[exponent] = coefficient
            representatives.add(orbit_key(tuple(vector), N))
    return len(representatives)


# ===== VERBATIM kernels (m1 via c1r2_verify_kill) =====
def fiber_contribs(q, n, t):
    h, e, o = n // 2, t // 2, (t + 1) // 2
    zeta = get_zeta(q, n)
    out = []
    for i in range(h):
        w = [pow(zeta, (2 * s * i) % n, q) for s in range(1, e + 1)]
        v = [pow(zeta, ((2 * s + 1) * i) % n, q) for s in range(o)]
        cN = tuple([0] * t)
        cB = tuple([2 * x % q for x in w] + [0] * o)
        cP = tuple(w + v)
        cM = tuple(w + [(q - x) % q for x in v])
        out.append((cN, cB, cP, cM))
    return out


def signed_all_census(q, n, t):
    h, e, o = n // 2, t // 2, (t + 1) // 2
    fib = fiber_contribs(q, n, t)
    axes = tuple(range(o))
    dp = np.zeros((q,) * o + (h + 1,), dtype=np.int64)
    dp[(0,) * o + (0,)] = 1
    for (cN, cB, cP, cM) in fib:
        new = 2 * dp
        tp = np.roll(dp, cP[e:], axis=axes)
        new[..., 1:] += tp[..., :-1]
        tm = np.roll(dp, cM[e:], axis=axes)
        new[..., 1:] += tm[..., :-1]
        dp = new
        assert int(dp.max()) < (1 << 61)
    return [int(x) for x in dp[(0,) * o]]


# ===== OPTIMIZED L=1 primitive-orbit enumerator (numpy subset-sum primitivity).
# Cross-validated in `reprice` mode against the verbatim kernel (w2..6) and the
# banked window-probe w7 counts before its output is trusted anywhere. =====
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
    subset = ((masks[:, None] >> np.arange(weight)) & 1).astype(np.int64)  # (2^w, w)
    proper = (masks != 0) & (masks != (1 << weight) - 1)
    reps = set()
    for supports in combo_chunks(N, weight, 100_000):
        vals = pw[supports]                                  # (m, w)
        hit = (vals @ signs.T) % q == 0                      # (m, 2^{w-1})
        idx = np.argwhere(hit)
        if len(idx) == 0:
            continue
        hv = vals[idx[:, 0]] * signs[idx[:, 1]]              # (h, w) signed values
        ss = (hv @ subset.T) % q                             # (h, 2^w)
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


def fmt(fr):
    return f"{fr.numerator}/{fr.denominator}"


# ===== modes =====
def do_family(kmin, qmax):
    fam = []
    k = kmin
    while (1 << k) < qmax:
        c = 1
        while c * (1 << k) + 1 < qmax:
            q = c * (1 << k) + 1
            if v2(q - 1) == k and is_prime(q):  # v2 condition keeps each q listed once
                fam.append((q, k, c))
            c += 2
        k += 1
    fam.sort()
    print(f"# gated Proth family: q=c*2^k+1, k>={kmin}, q<{qmax}  ->  {len(fam)} primes")
    octaves = {}
    for q, k, c in fam:
        octv = q.bit_length() - 1
        octaves.setdefault(octv, []).append(q)
        print(f"q={q:>12}  c={c:>5}  v2={k:>2}  octave=2^{octv}")
    print("# octaves populated:", sorted(octaves))
    assert fam, "NONEMPTINESS: gated family empty"
    return fam


def do_ground():
    A = a_total_L1(7937, N32)
    em1, r = em1_r(7937, N32, A)
    assert em1 == BANKED_EM1[7937], f"ground E-1 mismatch: {fmt(em1)}"
    print(f"GROUND PASS: q=7937 A_total={A} E-1={fmt(em1)} == banked; (E-1)/r={float(em1/r):.4f}")


def do_controls():
    rows = [7937, 63361, 65921, 204353]
    # PC2: gate excludes the killers
    for q in (63361, 65921, 204353):
        assert v2(q - 1) < GATE, f"PC2 FAIL: v2({q}-1)={v2(q-1)} >= {GATE}"
        print(f"PC2: v2({q}-1)={v2(q-1)} < {GATE}  -> OUT of r3 hypothesis")
    assert v2(63360) == 7 and v2(65920) == 7 and v2(204352) == 6, "PC2 exact v2 mismatch"
    # PC1: verbatim r2-window reproduction
    for q in rows:
        A = a_total_L1(q, N32)
        em1, r = em1_r(q, N32, A)
        assert em1 == BANKED_EM1[q], f"PC1 E-1 mismatch at {q}: {fmt(em1)}"
        counts = {w: primitive_orbit_count_verbatim(q, 1, w) for w in range(2, 7)}
        assert counts == BANKED_ORBITS_W26[q], f"PC1 orbit mismatch at {q}: {counts}"
        led = ledger_of(counts, N32)
        assert led == BANKED_WCL[q], f"PC1 W_cl mismatch at {q}: {fmt(led)}"
        kp = em1 / (r * (1 + led))
        verdict = "LITERAL-KILL(r2)" if em1 > 4 * r * (1 + led) else "survives(r2)"
        print(f"PC1: q={q:>7} r2-window K'={float(kp):.6f} W_cl={fmt(led)} orbits={counts} -> {verdict}")
        if q == 7937:
            assert abs(float(kp) - 0.246909432) < 1e-8
        if q == 63361:
            assert em1 > 4 * r * (1 + led) and float(kp) > 6.19, "PC1: r2 top kill lost"
            # M1 mutation: r2 window + gate dropped MUST fire on the r3 code path
            fired = em1 > LIT_KILL * r * (1 + led)
            assert fired, "M1 MUTATION FAILED: detector did not fire at q=63361 r2-window"
            print(f"M1 PASS: q=63361 gate-dropped r2-window K'={float(kp):.6f}>4 -> detector fires")
    print("CONTROLS PASS (PC1 exact fractions + PC2 gate exclusion + M1).")


def do_reprice(qs):
    for q in qs:
        A = a_total_L1(q, N32)
        em1, r = em1_r(q, N32, A)
        cv = {w: primitive_orbit_count_verbatim(q, 1, w) for w in range(2, 7)}
        cf = {w: primitive_orbit_count_fast(q, w) for w in range(2, 9)}
        for w in range(2, 7):
            assert cv[w] == cf[w], f"XVAL FAIL q={q} w={w}: verbatim {cv[w]} vs fast {cf[w]}"
        if q in BANKED_ORBITS_W26:
            assert cv == BANKED_ORBITS_W26[q], f"banked w2..6 mismatch at {q}"
        if q in BANKED_W7:
            assert cf[7] == BANKED_W7[q], f"w7 probe mismatch at {q}: {cf[7]} vs {BANKED_W7[q]}"
        led_ext = ledger_of(cf, N32)
        led_w7 = ledger_of({w: cf[w] for w in range(2, 8)}, N32)
        k_ext = em1 / (r * (1 + led_ext))
        k_w7 = em1 / (r * (1 + led_w7))
        assert k_ext <= k_w7, "window monotonicity violated (impossible)"
        print(f"PC3: q={q:>7} (gate ignored) orbits w2..8={cf}")
        print(f"     W_r2={fmt(ledger_of({w: cf[w] for w in range(2,7)}, N32))}"
              f"  W_w<=7={fmt(led_w7)}  W_ext={fmt(led_ext)}")
        print(f"     K'(r2 window)={float(em1/(r*(1+ledger_of({w: cf[w] for w in range(2,7)}, N32)))):.6f}"
              f"  K'(w<=7)={float(k_w7):.6f} (probe ref {BANKED_K_W7.get(q)})"
              f"  K'_ext={float(k_ext):.6f}  exact={fmt(k_ext)}")
        print(f"     -> repriced under r3 ledger: {'BELOW 4' if k_ext <= 4 else 'STILL > 4 (finding)'}"
              f" — row remains OUT of r3 hypothesis (PC2)")
    print("REPRICE/XVAL COMPLETE (optimized enumerator validated w2..6 verbatim + w7 probe).")


def do_row(qs):
    worst = None
    for q in qs:
        assert v2(q - 1) >= GATE, f"row q={q} fails gate (not in r3 family)"
        assert q < 2 ** N32 and N32 >= 16, "H2 violated"
        A = a_total_L1(q, N32)
        em1, r = em1_r(q, N32, A)
        env = em1 / r
        cf = {w: primitive_orbit_count_fast(q, w) for w in range(2, 9)}
        led = ledger_of(cf, N32)
        kp = em1 / (r * (1 + led))
        lit = em1 > LIT_KILL * r * (1 + led)
        amb = kp >= AMBER
        verdict = "LITERAL-KILL" if lit else ("AMBER" if amb else "survives")
        print(f"ROW q={q:>10} v2={v2(q-1):>2}: (E-1)/r={float(env):.9f} orbits={cf} "
              f"W_ext={fmt(led)} K'_r3={float(kp):.9f} -> {verdict}")
        print(f"    exact E-1={fmt(em1)} r={fmt(r)} K'_r3={fmt(kp)}")
        # M2: detector liveness on the gated path (allowance 1e-6)
        assert em1 > Fraction(1, 10 ** 6) * r * (1 + led) or kp <= Fraction(1, 10 ** 6), "impossible"
        m2_fired = kp > Fraction(1, 10 ** 6)
        assert m2_fired, f"M2 FAIL at q={q}: K'_r3={float(kp)} not > 1e-6 (E-1>0 must give K'>0)"
        # M3: ledger deletion at rows with (E-1)/r > 4
        if env > 4:
            assert em1 > LIT_KILL * r, f"M3 FAIL at q={q}"
            print(f"    M3: (E-1)/r={float(env):.3f}>4 and W_ext:=0 fires detector -> ledger load-bearing here")
        if worst is None or kp > worst[1]:
            worst = (q, kp, env)
    if worst:
        print(f"# WORST in batch: q={worst[0]} K'_r3={float(worst[1]):.9f} (E-1)/r={float(worst[2]):.6f}; M2 fired at all rows")


def do_dpx(q):
    A = a_total_L1(q, N32)
    asum = signed_all_census(q, 2 * N32, 2)     # t=2 -> o=1 (L=1)
    A2 = sum(asum)
    assert A == A2, f"DPX FAIL q={q}: DP={A} signed_all={A2}"
    print(f"DPX PASS: q={q} A_total={A} == banked signed_all_census marginal (two independent E paths)")


def do_w3census():
    from sympy import factorint
    # CRT primes p = 1 mod 64 above 2^30
    ps = []
    p = (1 << 30) + 1
    while len(ps) < 3:
        if (p - 1) % 64 == 0 and is_prime(p):
            ps.append(p)
        p += 64
    M = ps[0] * ps[1] * ps[2]
    assert M > 2 * 3 ** 32, "CRT modulus insufficient"
    supports = np.asarray(list(itertools.combinations(range(32), 3)), dtype=np.int64)  # (4960,3)
    signs = np.array([[1, s2, s3] for s2 in (1, -1) for s3 in (1, -1)], dtype=np.int64)  # (4,3)
    npolys = len(supports) * len(signs)
    assert npolys == 19840, npolys
    norms_mod = []
    for p in ps:
        z = get_zeta(p, 64)
        Z = np.array([[pow(z, (u * e) % 64, p) for e in range(32)] for u in range(1, 64, 2)],
                     dtype=np.int64)                       # (32 roots, 32 exps)
        acc = np.ones((len(supports), len(signs)), dtype=np.int64)
        for t in range(32):
            vals = (Z[t][supports] @ signs.T) % p          # (4960, 4)
            acc = (acc * vals) % p
        norms_mod.append(acc.reshape(-1))
    x = np.zeros(19840, dtype=object)
    for p, res in zip(ps, norms_mod):
        Mp = M // p
        coef = (Mp * pow(Mp, -1, p)) % M
        x = (x + res.astype(object) * coef) % M
    norms = [int(v) for v in x]
    assert all(0 < v <= 3 ** 32 for v in norms), "norm out of root-product bound (or zero)"
    uniq = sorted(set(norms))
    print(f"# w3census: 19840 polys, {len(uniq)} unique norms, CRT mod {ps} (> 2*3^32)")
    prime_depth = {}
    for v in uniq:
        for pr in factorint(v):
            prime_depth[pr] = v2(pr - 1)
    mx = max(prime_depth.values())
    mxp = max(prime_depth, key=lambda t: prime_depth[t])
    print(f"# distinct prime divisors: {len(prime_depth)}; MAX v2(p-1) = {mx} at p={mxp}")
    deep = sorted((pr for pr, d in prime_depth.items() if d >= 10))
    print("# divisors with v2>=10:", [(pr, prime_depth[pr]) for pr in deep] or "(none)")
    for q in (63361, 65921, 204353):
        print(f"# consistency: r2 killer {q} divides a weight-3 norm: {q in prime_depth}")
        assert q in prime_depth, f"killer {q} missing from w3 census (integrity)"
    gate_break = [pr for pr, d in prime_depth.items() if d >= GATE]
    print(f"# GATE-MIRROR verdict: divisors with v2 >= {GATE}: {gate_break or 'NONE'}")
    if not gate_break:
        print("# => analogue weight-3 channel PROVABLY EMPTY at every gated prime (any size) — mirror HOLDS")


def do_accscan(kmin):
    QMAX = 1 << 32
    combos = {w: np.asarray(list(itertools.combinations(range(32), w)), dtype=np.int64)
              for w in (3, 4, 5, 6)}
    signsets = {}
    for w in (3, 4, 5, 6):
        s = np.array(list(itertools.product((1, -1), repeat=w - 1)), dtype=np.int64)
        signsets[w] = np.hstack([np.ones((len(s), 1), dtype=np.int64), s])
    fam = []
    k = kmin
    while (1 << k) < QMAX:
        c = 1
        while c * (1 << k) + 1 < QMAX:
            q = c * (1 << k) + 1
            if v2(q - 1) == k and is_prime(q):
                fam.append(q)
            c += 2
        k += 1
    fam.sort()
    print(f"# accscan: {len(fam)} gated primes (k>={kmin}) below 2^32")
    assert fam, "NONEMPTINESS"
    nonempty = 0
    for q in fam:
        z = get_zeta(q, 64)
        pw = np.array([pow(z, e, q) for e in range(32)], dtype=np.int64)
        counts = {}
        for w in (3, 4, 5, 6):
            sup, sg = combos[w], signsets[w]
            tot = 0
            for lo in range(0, len(sup), 200_000):
                blk = sup[lo:lo + 200_000]
                tot += int(np.count_nonzero((pw[blk] @ sg.T) % q == 0))
            counts[w] = tot
        if any(counts.values()):
            nonempty += 1
            print(f"ACCIDENT q={q:>12} v2={v2(q-1):>2} signed-vanisher counts w3..6 = {counts}")
    print(f"# gated primes with ANY w<=6 vanisher: {nonempty} / {len(fam)}")
    print("# family below 2^28 (full-spectrum slice):", [q for q in fam if q < (1 << 28)])


def do_aspect(qs):
    N = 64
    for q in qs:
        assert v2(q - 1) >= GATE and q < 2 ** 32
        A = a_total_L1_crt(q, N)
        em1 = Fraction(q * A, 4 ** N) - 1
        r = Fraction(q, 2 ** N)
        env = em1 / r
        cf = {w: primitive_orbit_count_fast(q, w, N=N) for w in range(2, 7)}
        led = ledger_of(cf, N)     # PARTIAL ledger (w<=6) — survival-only bound
        kub = em1 / (r * (1 + led))
        print(f"ASPECT N=64 q={q:>10}: (E-1)/r={float(env):.9f} partial-orbits w2..6={cf} "
              f"W_partial={fmt(led)} K'_r3<= {float(kub):.9f} (partial-ledger UPPER bound)")
        print(f"    exact E-1={fmt(em1)}  A_total={A}")
        print(f"    -> {'SURVIVAL confirmed at aspect 64 (bound < 1)' if kub < 1 else 'needs full ledger (NOT a kill; pre-registered)'}")


def main():
    mode = sys.argv[1]
    if mode == "family":
        do_family(int(sys.argv[2]), int(sys.argv[3]))
    elif mode == "ground":
        do_ground()
    elif mode == "controls":
        do_controls()
    elif mode == "reprice":
        do_reprice([int(x) for x in sys.argv[2].split(",") if x])
    elif mode == "row":
        do_row([int(x) for x in sys.argv[2].split(",") if x])
    elif mode == "dpx":
        do_dpx(int(sys.argv[2]))
    elif mode == "w3census":
        do_w3census()
    elif mode == "accscan":
        do_accscan(int(sys.argv[2]))
    elif mode == "aspect":
        do_aspect([int(x) for x in sys.argv[2].split(",") if x])
    else:
        raise SystemExit(f"unknown mode {mode}")


if __name__ == "__main__":
    main()

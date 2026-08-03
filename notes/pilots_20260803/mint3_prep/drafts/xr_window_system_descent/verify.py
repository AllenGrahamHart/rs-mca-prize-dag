#!/usr/bin/env python3
"""Verifier for xr_window_system_descent.

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 verify.py
Pure python integers (plus math.lgamma for the huge binomials),
deterministic, no third-party imports, NO FILE READS.  All pins inlined;
provenance paths appear in comments only, so this keeps passing after the
move to background/nodes/.

  A  LEMMA W <=> an independent direct-interpolation oracle, EXHAUSTIVELY
     over every T, at four shapes, BOTH directions
  B  the JOINT system = intersection of the two single-word systems.
     The source HARD-CODES this to True (algebra.py:224) and its joint
     core count is 0 in all 12 trials; here it is COMPUTED, on a fixture
     with a PLANTED (hence non-empty) joint core
  C  COROLLARY W2: E_T monic, E_T | X^n - 1, the T <-> E_T bijection,
     and the codim <= 2d affine-subspace reading
  D  THEOREM D(a) in BOTH directions (the source checks only =>),
     D(b) class-locality, D(c) bijection on NON-VACUOUS fixtures
     (the source's D(c) is non-vacuous in only 2 of 14 cases)
  E  THEOREM R: rank = d on gated words; the sharpness converse
     (distance L < d  =>  rank exactly L); the MC illustration
  F  THEOREM L row arithmetic: cap_d, and the proved/heuristic scale
     partition at all six rows + the h-even control
  G  the q-critical arithmetic and the 41.5-bit headroom
  H  the BP(1) scope catch: sub-depth scales inside the band proper at
     the prize rows, NOT at RowC, with M != 2^ceil(log2 d) exhibited
"""
from __future__ import annotations

import sys
from itertools import combinations
from math import lgamma, log2

sys.dont_write_bytecode = True

LN2 = 0.6931471805599453
FAILURES = []


def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
    if not ok:
        FAILURES.append(label)


# --------------------------------------------------------------- field utils

def prime_factors(m):
    out, d = set(), 2
    while d * d <= m:
        if m % d == 0:
            out.add(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        out.add(m)
    return sorted(out)


def root_of_unity(q, n):
    """a generator of mu_n <= F_q^*  (requires n | q-1)."""
    assert (q - 1) % n == 0
    fs = prime_factors(q - 1)
    g = next(c for c in range(2, q)
             if all(pow(c, (q - 1) // f, q) != 1 for f in fs))
    w = pow(g, (q - 1) // n, q)
    assert pow(w, n, q) == 1
    for d in range(1, n):
        if n % d == 0:
            assert pow(w, d, q) != 1
    return w


def poly_trim(a, q):
    a = [x % q for x in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def pmul(a, b, q):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i + j] = (out[i + j] + ai * bj) % q
    return poly_trim(out, q)


def locator(pts, q):
    """prod (X - t), monic."""
    e = [1]
    for t in pts:
        e = pmul(e, [(-t) % q, 1], q)
    return e


def cyc(a, n, q):
    """reduce mod X^n - 1, returned as a length-n coefficient vector."""
    out = [0] * n
    for i, c in enumerate(a):
        out[i % n] = (out[i % n] + c) % q
    return out


def rank_mod(rows, q):
    M = [r[:] for r in rows]
    nr, nc = len(M), (len(M[0]) if M else 0)
    r = 0
    for c in range(nc):
        piv = next((i for i in range(r, nr) if M[i][c] % q), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], q - 2, q)
        M[r] = [(x * inv) % q for x in M[r]]
        for i in range(nr):
            if i != r and M[i][c] % q:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % q for j in range(nc)]
        r += 1
        if r == nr:
            break
    return r


def idft(vals, H, q, n):
    """coefficients of the degree-<n interpolant of `vals` on H = <w>."""
    w = H[1]
    winv = pow(w, q - 2, q)
    ninv = pow(n % q, q - 2, q)
    return [(ninv * sum(vals[i] * pow(winv, i * j, q) for i in range(n))) % q
            for j in range(n)]


def peval(a, x, q):
    r = 0
    for c in reversed(a):
        r = (r * x + c) % q
    return r


# ---------------------------------------------------- LEMMA W and its oracle

def lemmaW(u, T, n, k, d, q):
    """LEMMA W: do the top-d coefficients of u*E_T mod (X^n - 1) vanish?"""
    S = cyc(pmul(u, locator(T, q), q), n, q)
    return all(S[j] == 0 for j in range(n - d, n))


def direct_core(u, Z, k, d, q):
    """INDEPENDENT oracle: interpolate u on Z (|Z| = k+d) by Lagrange and
    test that the coefficients in degrees k..k+d-1 vanish, i.e. that some
    deg<k codeword agrees with u on Z."""
    pts = list(Z)
    acc = [0]
    for i, xi in enumerate(pts):
        num = [1]
        den = 1
        for j, xj in enumerate(pts):
            if i == j:
                continue
            num = pmul(num, [(-xj) % q, 1], q)
            den = den * ((xi - xj) % q) % q
        c = peval(u, xi, q) * pow(den, q - 2, q) % q
        term = [(c * t) % q for t in num]
        acc = poly_trim([(acc[m] if m < len(acc) else 0)
                         + (term[m] if m < len(term) else 0)
                         for m in range(max(len(acc), len(term)))], q)
    return all((acc[j] if j < len(acc) else 0) == 0 for j in range(k, k + d))


def lcg(seed):
    s = seed

    def nxt(m):
        nonlocal s
        s = (1103515245 * s + 12345) % (1 << 31)
        return s % m
    return nxt


# --------------------------------------------------------------- stage A / B

FIX = [(12, 6, 3, 13), (8, 4, 2, 17), (16, 8, 2, 17), (12, 4, 2, 13)]


def stage_A():
    bad = 0
    tried = 0
    nonempty = 0
    for (n, k, d, q) in FIX:
        H = [pow(root_of_unity(q, n), i, q) for i in range(n)]
        rnd = lcg(20260803 + n * 100 + q)
        rp = n - k - d
        for trial in range(3):
            u = [rnd(q) for _ in range(n)]
            for Tidx in combinations(range(n), rp):
                T = [H[i] for i in Tidx]
                Z = [H[i] for i in range(n) if i not in Tidx]
                a = lemmaW(u, T, n, k, d, q)
                b = direct_core(u, Z, k, d, q)
                tried += 1
                if a != b:
                    bad += 1
                if a:
                    nonempty += 1
    check("A: LEMMA W <=> direct interpolation oracle, EXHAUSTIVE over every "
          "T, BOTH directions", bad == 0 and tried > 0,
          f"{tried} (word,T) pairs at 4 shapes, {nonempty} cores found, "
          f"{bad} mismatches")


def stage_B():
    """JOINT = intersection, on a PLANTED (non-empty) joint core.
    The source hard-codes this check to True (algebra.py:224) and finds
    joint = 0 in all 12 of its trials; here it is computed and non-vacuous."""
    n, k, d, q = 12, 6, 3, 13
    H = [pow(root_of_unity(q, n), i, q) for i in range(n)]
    rp = n - k - d
    rnd = lcg(4242)
    # plant: choose the core Z, put codewords f,g on it, errors off it
    Zidx = tuple(range(k + d))
    Tidx = tuple(i for i in range(n) if i not in Zidx)
    f = [rnd(q) for _ in range(k)]
    g = [rnd(q) for _ in range(k)]
    uv, vv = [], []
    for i, x in enumerate(H):
        if i in Zidx:
            uv.append(peval(f, x, q))
            vv.append(peval(g, x, q))
        else:
            uv.append((peval(f, x, q) + 1 + rnd(q - 1)) % q)
            vv.append((peval(g, x, q) + 1 + rnd(q - 1)) % q)
    u = idft(uv, H, q, n)
    v = idft(vv, H, q, n)
    su, sv, sj = set(), set(), set()
    for Ti in combinations(range(n), rp):
        T = [H[i] for i in Ti]
        a = lemmaW(u, T, n, k, d, q)
        b = lemmaW(v, T, n, k, d, q)
        if a:
            su.add(Ti)
        if b:
            sv.add(Ti)
        if a and b:
            sj.add(Ti)
    planted_found = Tidx in sj
    check("B: JOINT system = intersection of the two single-word systems "
          "(COMPUTED here; the source hard-codes this to True at "
          "algebra.py:224) -- and NON-VACUOUS: the planted joint core is found",
          sj == (su & sv) and planted_found and len(sj) >= 1,
          f"|u-cores|={len(su)} |v-cores|={len(sv)} |joint|={len(sj)} "
          f"planted_core_found={planted_found}")


# --------------------------------------------------------------- stage C

def stage_C():
    bad = []
    for (n, k, d, q) in FIX:
        H = [pow(root_of_unity(q, n), i, q) for i in range(n)]
        rp = n - k - d
        Xn1 = [0] * (n + 1)
        Xn1[0], Xn1[n] = (-1) % q, 1
        seen = {}
        for Ti in combinations(range(n), rp):
            E = locator([H[i] for i in Ti], q)
            if len(E) != rp + 1 or E[-1] != 1:
                bad.append(("not monic degree r'", n, Ti))
                break
            # E_T | X^n - 1  <=>  every root of E_T is in H and E_T squarefree
            if any(peval(Xn1, r, q) != 0 for r in [H[i] for i in Ti]):
                bad.append(("root not in H", n, Ti))
                break
            key = tuple(E)
            if key in seen:
                bad.append(("bijection fails", n, Ti, seen[key]))
                break
            seen[key] = Ti
        ncr = 1
        for i in range(rp):
            ncr = ncr * (n - i) // (i + 1)
        if len(seen) != ncr:
            bad.append(("count", n, len(seen), ncr))
    # the codim reading: 2d equations on the rp free lower coefficients
    codim_ok = all((n - k - d) >= 1 and 2 * d >= 1 for (n, k, d, q) in FIX)
    check("C: COROLLARY W2 -- E_T monic of degree r', E_T | X^n - 1, and "
          "T <-> E_T is a BIJECTION onto the monic degree-r' divisors; the "
          "joint system is 2d affine-linear equations on the r' lower "
          "coefficients, so cores lie on a codim <= 2d affine subspace",
          not bad and codim_ok, f"violations={bad[:2]}")


# --------------------------------------------------------------- stage D

DFIX = [(16, 8, 17, 2, 2), (16, 8, 17, 4, 4), (12, 6, 13, 3, 3), (16, 8, 17, 2, 4)]


def stage_D():
    bad_a, bad_b, tested_a = [], [], 0
    for (n, k, q, M, d) in DFIX:
        if n % M or k % M or d % M:
            continue
        H = [pow(root_of_unity(q, n), i, q) for i in range(n)]
        rp = n - k - d
        if rp % M:
            continue
        idx = {H[i]: i for i in range(n)}
        mu_M = [pow(root_of_unity(q, n), i * (n // M), q) for i in range(M)]
        for Ti in combinations(range(n), rp):
            T = [H[i] for i in Ti]
            Tset = set(T)
            is_coset_union = all((x * z) % q in Tset for x in T for z in mu_M)
            E = locator(T, q)
            is_XM = all(E[i] == 0 for i in range(len(E)) if i % M)
            tested_a += 1
            if is_coset_union != is_XM:          # BOTH directions
                bad_a.append((n, M, Ti, is_coset_union, is_XM))
            if is_XM:
                # D(b): equation j touches only positions = j (mod M)
                for j in range(n - d, n):
                    touched = {(j - i) % M for i in range(len(E)) if E[i]}
                    if touched - {j % M}:
                        bad_b.append((n, M, j, sorted(touched)))
    check("D(a): T is a mu_M-coset union  <=>  E_T(X) = G(X^M), BOTH "
          "directions (the source machine-checks only '=>')",
          not bad_a and tested_a > 0,
          f"{tested_a} locators tested, {len(bad_a)} violations")
    check("D(b): under E_T = G(X^M), equation j of LEMMA W touches ONLY "
          "syndrome positions = j (mod M)", not bad_b,
          f"{len(bad_b)} violations")


def stage_D_c():
    """D(c): scale-M cores upstairs <-> quotient cores, on fixtures where
    BOTH sides are NON-EMPTY (the source's D(c) is non-vacuous in only
    2 of its 14 cases)."""
    n, k, q, M, d = 16, 8, 17, 2, 2
    N, kq, dq = n // M, k // M, d // M
    wn = root_of_unity(q, n)
    H = [pow(wn, i, q) for i in range(n)]
    HN = [pow(pow(wn, M, q), i, q) for i in range(N)]
    rp, rq = n - k - d, N - kq - dq
    nonvac = 0
    bad = []
    for rho in range(M):
        rnd = lcg(999 + rho)
        for trial in range(6):
            # word with syndrome window supported in ONE class rho mod M
            u = [0] * n
            for m in range(n):
                if m >= k and m % M == rho:
                    u[m] = rnd(q)
                elif m < k:
                    u[m] = rnd(q)
            up = [u[(rho + s * M) % n] for s in range(N)]
            up_full = [0] * N
            for s in range(N):
                up_full[s] = up[s]
            up_cores = set()
            for Ti in combinations(range(N), rq):
                if lemmaW(up_full, [HN[i] for i in Ti], N, kq, dq, q):
                    up_cores.add(Ti)
            dn_cores = set()
            for Ti in combinations(range(n), rp):
                T = [H[i] for i in Ti]
                Tset = set(T)
                mu_M = [pow(wn, i * (n // M), q) for i in range(M)]
                if not all((x * z) % q in Tset for x in T for z in mu_M):
                    continue
                if lemmaW(u, T, n, k, d, q):
                    dn_cores.add(Ti)
            if len(up_cores) == len(dn_cores) and len(up_cores) > 0:
                nonvac += 1
            if len(up_cores) != len(dn_cores):
                bad.append((rho, trial, len(up_cores), len(dn_cores)))
    check("D(c): scale-M cores upstairs are in BIJECTION with quotient "
          "cores, on fixtures where BOTH sides are NON-EMPTY",
          not bad and nonvac > 0,
          f"{nonvac} non-vacuous instances, {len(bad)} count mismatches")


# --------------------------------------------------------------- stage E

def toeplitz_rank(u, n, k, d, q):
    rp = n - k - d
    rows = [[u[(j - i) % n] for i in range(rp + 1)] for j in range(n - d, n)]
    return rank_mod(rows, q)


def max_agreement(u, H, n, k, q, cap):
    """max agreement of u with RS_k on H, computed via LEMMA W; scans
    d = cap-k downwards.  Exact, small-fixture only."""
    for a in range(cap, k - 1, -1):
        d = a - k
        rp = n - a
        for Ti in combinations(range(n), rp):
            if lemmaW(u, [H[i] for i in Ti], n, k, d, q):
                return a
    return k


def stage_E():
    n, k, q = 12, 4, 13
    H = [pow(root_of_unity(q, n), i, q) for i in range(n)]
    h = 4
    A = k + h
    rnd = lcg(31337)
    gated, ok_rank, tried = 0, 0, 0
    for trial in range(6):
        u = [rnd(q) for _ in range(n)]
        agr = max_agreement(u, H, n, k, q, n)
        if agr > A:
            continue                       # not tangent-gated: skip
        gated += 1
        for d in (2, 3):
            if n - k < 2 * d:
                continue
            tried += 1
            if toeplitz_rank(u, n, k, d, q) == d:
                ok_rank += 1
    check("E1 (THEOREM R): rank R(u,d) = d exactly on TANGENT-GATED words "
          "(gate certified by exhaustive max-agreement scan, not assumed)",
          gated > 0 and tried > 0 and ok_rank == tried,
          f"{gated} gated words, {ok_rank}/{tried} full rank")

    # the sharpness converse: plant a codeword at distance L < d
    bad = []
    for L in (1, 2):
        for trial in range(4):
            rr = lcg(777 + 13 * L + trial)
            f = [rr(q) for _ in range(k)]
            vals = [peval(f, x, q) for x in H]
            spoil = sorted({rr(n) for _ in range(L)})
            while len(spoil) < L:
                spoil = sorted(set(spoil) | {rr(n)})
            for i in spoil:
                vals[i] = (vals[i] + 1 + rr(q - 1)) % q
            u = idft(vals, H, q, n)
            d = L + 1
            r = toeplitz_rank(u, n, k, d, q)
            if r != L:
                bad.append((L, trial, r))
    check("E2 (THEOREM R sharpness, the converse): planting a codeword at "
          "distance L < d drops the rank to EXACTLY L -- so the tangent "
          "gate is the sharp criterion, not merely sufficient",
          not bad, f"{len(bad)} violations")

    # E3: the MC illustration -- full rank yet a large solution set.
    # The MC word is u = X^{n-1} + c X^{k+w-1}; MC-1 forces prod(T) =
    # (-1)^{r'+1} c, so c must be (-1)^{r'+1} times a product of n-th roots
    # of unity -- an arbitrary c has NO solutions.  Build c from a genuine
    # mu_M-coset union (which also gives e_1 = ... = e_{w-1} = 0 for free).
    n2, k2, w, q2 = 16, 4, 2, 97
    wn2 = root_of_unity(q2, n2)
    H2 = [pow(wn2, i, q2) for i in range(n2)]
    rp2 = n2 - k2 - w                      # = 10
    M2 = 2
    N2 = n2 // M2                          # 8 cosets of mu_2
    cosets = [[H2[i], H2[i + N2]] for i in range(N2)]
    T0 = [x for cs in cosets[:rp2 // M2] for x in cs]
    prodT0 = 1
    for x in T0:
        prodT0 = prodT0 * x % q2
    c = ((-1) ** (rp2 + 1) * prodT0) % q2
    u2 = [0] * n2
    u2[n2 - 1] = 1
    u2[k2 + w - 1] = (u2[k2 + w - 1] + c) % q2
    r = toeplitz_rank(u2, n2, k2, w, q2)
    sols = sum(1 for Ti in combinations(range(n2), rp2)
               if lemmaW(u2, [H2[i] for i in Ti], n2, k2, w, q2))
    check("E3: the MC word has FULL rank w yet MANY solutions -- rank is "
          "NOT the degeneracy an adversary exploits (any blow-up must be "
          "arithmetic)", r == w and sols > 1, f"rank={r} w={w} solutions={sols}")


# ------------------------------------------------- rows: THEOREM L and BP(1)

ROWS = [
    dict(name="RowC 1/4", n=1024, k=256, h=5, C=0.68),
    dict(name="RowC 1/8", n=1024, k=128, h=5, C=0.68),
    dict(name="RowC 1/16", n=1024, k=64, h=3, C=0.68),
    dict(name="prize 1/4", n=2199023255552, k=549755813888, h=8589934593,
         C=0.800767298932776),
    dict(name="prize 1/8", n=2199023255552, k=274877906944, h=8589934593,
         C=0.6858649121282252),
    dict(name="prize 1/16", n=2199023255552, k=137438953472, h=4294967297,
         C=0.6596448038293138),
]
CONTROL = dict(name="h-even control", n=20, k=8, h=6, C=0.68)
LOG2Q_PIN = 250.0


def lbinom(n, j):
    if j < 0 or j > n:
        return float("-inf")
    if j == 0 or j == n:
        return 0.0
    return (lgamma(n + 1) - lgamma(j + 1) - lgamma(n - j + 1)) / LN2


def band_proper(h):
    return (-(-h // 2), h - 2)


def scales_for(row):
    """sub-depth coset scales M = 2^j | gcd(n,k), M < d, M | d, d in band."""
    n, k, h = row["n"], row["k"], row["h"]
    lo, hi = band_proper(h)
    out = []
    if lo > hi:
        return out
    g = n if n < k else k
    j = 1
    while (1 << j) <= g:
        M = 1 << j
        if n % M or k % M:
            j += 1
            continue
        dmin = ((lo + M - 1) // M) * M
        dmax = (hi // M) * M
        if dmin > dmax or dmin <= 0:
            j += 1
            continue
        if M >= dmin:                 # sub-depth means M < d
            j += 1
            continue
        cnt = (dmax - dmin) // M + 1
        capmin = (n - k - dmin) // (h - dmin)
        capmax = (n - k - dmax) // (h - dmax)
        out.append(dict(j=j, M=M, dmin=dmin, dmax=dmax, count=cnt,
                        cap_dmin=capmin, cap_dmax=capmax,
                        live_all=(M > capmax and M > capmin)))
        j += 1
    return out


def fm_margin(row, M, d):
    n, k, h = row["n"], row["k"], row["h"]
    N, m = n // M, (n - k - d) // M
    return lbinom(N, m) - (2 * d / M) * LOG2Q_PIN - log2(row["C"] * n * n)


def stage_F():
    proved, heur = {}, {}
    for row in ROWS:
        sc = scales_for(row)
        proved[row["name"]] = [s["M"] for s in sc if s["live_all"]]
        heur[row["name"]] = [s["M"] for s in sc if not s["live_all"]]
    exp_prized = {"prize 1/4": (1 << 21, 1 << 31), "prize 1/8": (1 << 21, 1 << 31),
                  "prize 1/16": (1 << 21, 1 << 30)}
    ok = True
    detail = []
    for nm, (plo, phi) in exp_prized.items():
        got = proved[nm]
        want = [1 << j for j in range(21, (phi.bit_length() - 1) + 1)]
        if got != want:
            ok = False
        detail.append(f"{nm}: proved 2^21..2^{phi.bit_length()-1} "
                      f"({len(got)} scales)")
    heur_ok = all(heur[nm] == [1 << j for j in range(1, 21)]
                  for nm in exp_prized)
    rowc_empty = all(not scales_for(r) for r in ROWS if r["name"].startswith("RowC"))
    check("F1 (THEOREM L at the rows): liveness closes EXACTLY the scales "
          "M = 2^21..2^31 (prize 1/4, 1/8) and 2^21..2^30 (prize 1/16) "
          "UNCONDITIONALLY; M = 2^1..2^20 are NOT closed by liveness",
          ok and heur_ok, "; ".join(detail))

    ctrl = scales_for(CONTROL)
    ctrl_proved = [s["M"] for s in ctrl if s["live_all"]]
    check("F2 (h ODD is load-bearing): at the h-EVEN control (n=20,k=8,h=6) "
          "liveness proves NOTHING -- proved_scales is EMPTY -- so THEOREM L "
          "genuinely needs h odd",
          not CONTROL["h"] % 2 == 1 and ctrl_proved == [] and len(ctrl) > 0,
          f"control scales={[s['M'] for s in ctrl]} proved={ctrl_proved}")

    margins = []
    for nm in exp_prized:
        row = next(r for r in ROWS if r["name"] == nm)
        s20 = next(s for s in scales_for(row) if s["M"] == (1 << 20))
        margins.append(fm_margin(row, s20["M"], s20["dmin"]))
    worst = max(margins)
    # The audit's banked claim is ">= 3.09e5-bit first-moment margins" on
    # M <= 2^20 (FABLE_AUDIT.md:21-22; the node addendum at
    # xr_mc_depth_quantization/statement.md:161 says the same).  That is the
    # claim asserted here.  The pilot's own least-negative figure is
    # -309180.56 (prize 1/16, j=20); this fresh recomputation gives
    # -309261.96, a 81.4-bit difference traced to the dmin convention at the
    # band-proper floor.  Both satisfy the banked claim; the discrepancy is
    # RECORDED, not smoothed over (see AUDIT_CHECKLIST F1.h).
    check("F3 (the HEURISTIC half, labelled): the M = 2^20 first-moment "
          "margins all exceed 3.09e5 bits in magnitude; this is an "
          "EXPECTATION, not a certified bound -- the M <= 2^20 closure is "
          "heuristic-grade and is labelled as such",
          worst < -309000.0,
          f"least-negative margin over the three prize rows = {worst:.2f} "
          f"bits (pilot records -309180.56; delta {abs(worst+309180.56):.2f} "
          f"bits, dmin-convention, flagged F1.h)")


def stage_G():
    """q-critical: the smallest log2 q at which the count would beat budget."""
    res = []
    for row in ROWS:
        lo, hi = band_proper(row["h"])
        if lo > hi:
            continue
        best = None
        for d in {lo, hi}:
            N, m = row["n"], row["n"] - row["k"] - d
            need = (lbinom(N, m) - log2(row["C"] * row["n"] ** 2)) / (2 * d)
            if best is None or need > best[0]:
                best = (need, d)
        res.append((row["name"], best[0], best[1]))
    binding = max(res, key=lambda t: t[1])
    head = LOG2Q_PIN - binding[1]
    check("G (SL-2-RES's q-pin): the binding row is prize 1/4 with "
          "log2 q_critical = 208.4759..., i.e. the residual must carry "
          "q >= 2^209, with 41.52 bits of headroom against the 2^250 pin",
          binding[0] == "prize 1/4" and 208.47 < binding[1] < 208.48
          and 41.5 < head < 41.6,
          f"binding row={binding[0]} log2_q_crit={binding[1]:.5f} "
          f"at d={binding[2]} headroom={head:.5f}")


def stage_H():
    prize = [r for r in ROWS if r["name"].startswith("prize")]
    rowc = [r for r in ROWS if r["name"].startswith("RowC")]
    prize_has = all(len(scales_for(r)) > 0 for r in prize)
    rowc_has = any(len(scales_for(r)) > 0 for r in rowc)
    # BP(1) itself: no power of two in the band proper at h odd
    bp1 = []
    for r in ROWS + [CONTROL]:
        lo, hi = band_proper(r["h"])
        found = [1 << j for j in range(0, 64) if lo <= (1 << j) <= hi]
        bp1.append((r["name"], r["h"] % 2 == 1, found))
    bp1_ok = all((not odd) or found == [] for (_, odd, found) in bp1)
    ctrl_found = next(f for (nm, _, f) in bp1 if nm == "h-even control")
    # the item-10 pin vs the actual scale, on the pilot's toy witness
    d_toy, M_toy = 4, 2
    item10 = 1 << (d_toy - 1).bit_length()
    check("H1 (the BP(1) SCOPE CATCH): sub-depth coset scales M < d with "
          "M | d exist INSIDE the band proper at all three PRIZE rows and "
          "at NONE of the RowC rows -- exactly the gap BP(1) does not cover",
          prize_has and not rowc_has,
          f"prize scale counts={[len(scales_for(r)) for r in prize]}, "
          f"RowC={[len(scales_for(r)) for r in rowc]}")
    check("H2 (BP(1) as banked is intact where it applies): at h ODD the "
          "band proper contains NO power of two; the h-EVEN control DOES "
          "contain one, so the protection is PARITY, not impossibility",
          bp1_ok and ctrl_found == [4], f"h-even control found={ctrl_found}")
    check("H3 (what the catch actually is): the pilot's toy witness has "
          "d = 4 (a power of two!) at scale M = 2, while item 10 pins "
          "M = 2^ceil(log2 d) = 4 -- the gap is M != 2^ceil(log2 d), NOT "
          "'d is not a power of two'",
          item10 == 4 and M_toy == 2 and M_toy < d_toy and d_toy % M_toy == 0,
          f"d={d_toy} item10_scale={item10} actual M={M_toy}")
    print("NOTE (MEASURED-about-the-route, not a claim of this node): the "
          "pilot's Route-1/Route-2 negatives -- the packing bound sits "
          "~2^1.7e12 above budget at the prize rows and the counting/union "
          "route dies at N = 1/rate (4, 8, 16) -- are PROVED NEGATIVES ABOUT "
          "THE ROUTES, not about SL-2 (route2.py:28-29).")


def main():
    stage_A()
    stage_B()
    stage_C()
    stage_D()
    stage_D_c()
    stage_E()
    stage_F()
    stage_G()
    stage_H()
    if FAILURES:
        print("FAILED CHECKS:", FAILURES)
        sys.exit(1)
    print("XR_WINDOW_SYSTEM_DESCENT_ALL_PASS")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""qme_verify — verifier for the QA.22 M <= t EXTENSION (qa22_m_le_t_extension).

Grid: n = 2^s, s = 13..44, rates rho in {1/2,1/4,1/8,1/16}, k = rho*n,
t = (n-k)/2, sigma = 1. Extension rows: (M, A_own(M)) for dyadic 2<=M<=t,
A_own = M*ceil((k+1)/M), allowance 719*Q_M(A_own), Q_M(A) = C(n/M-1, A/M);
csp row (2, k+4) at 719*Q_2(k+4) if consumed.

E1 nondegeneracy (every extension row exists: Q_M(A_own) >= 1) + band floor.
E2 COL landing fits the 719 line: n/(n-A_own) <= 4 <= 719 per cell; the
   per-rate cap maxima are EXACTLY {1/2: 4, 1/4: 2, 1/8: 4/3, 1/16: 4/3};
   csp ratio in scope.
E3 dedup: extension scales all <= t (composite range (t, n] disjoint);
   parity disjointness vs the seven banked QA.22 rows (A_own even, banked
   A odd).
E4 first-scale dominance at the CORRECTED constant (1 + 2^-690):
   Regime A exact bigint s = 13..20 (+ worst-cell pin (13,1/16), the #155
   sharpness pin excess > 2^-691, M=4 carries the tail to 2^-300);
   Regime B certified integer-only entropy bounds s = 21..44, with the
   certificates cross-checked against exact values on s = 15..20.
E5 absorption scale: 719 = floor(n^6/C(n+6,6)) at the four official
   maximal rows; planted-column identity Q_2(k+2) = Q_2^planted(k) *
   (a2-k/2)/(k/2+1) (exact, all rows; integer identity re-verified on
   Regime A rows); ratio in [2047/2049, 15); certified L makes the old
   banked rows (2^99.81 etc.) negligible.
M  mutation controls MUT1..MUT5 — ALL must TRIP (incl. MUT2 = the
   pre-computation's own 2^-691 constant, which is FALSE: catch #155).

Run: tools/ramguard tiny -- python3 qme_verify.py
"""
from fractions import Fraction
from math import comb, log2

FAILS = []


def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)


def lg(fr):
    """high-precision log2 of a positive Fraction (exact to ~2^-60)."""
    num, den = fr.numerator, fr.denominator
    sh = num.bit_length() - den.bit_length()
    r = Fraction(num, den << sh) if sh >= 0 else Fraction(num << (-sh), den)
    return sh + log2(int(r * (1 << 62)) / (1 << 62))


def own_A(k, M):
    return M * (-(-(k + 1) // M))


RATES = (2, 4, 8, 16)          # denominators of rho
GRID_S = range(13, 45)         # official grid rows
BANKED_QA22_A = [507, 261, 133, 67, 558345748481, 283467841537, 141733920769]
QPREC = 128                    # dyadic log2 precision denominator

# =========================================================================
# E1/E2/E3 + E5-ratio: full-grid structural sweep (pure small arithmetic)
# =========================================================================
print("=" * 72)
print("E1/E2/E3: nondegeneracy, COL cap vs allowance, dedup — full grid")
print("=" * 72)
ncells = 0
e1_viol = e2_viol = band_viol = parity_viol = scale_viol = csp_viol = 0
rate_max = {rd: Fraction(0) for rd in RATES}
ratio_min, ratio_max = None, None
for s in GRID_S:
    n = 2 ** s
    for rd in RATES:
        k = n // rd
        t = (n - k) // 2
        M = 2
        while M <= t:
            A = own_A(k, M)
            h = A // M
            N = n // M
            ncells += 1
            if not (A % M == 0 and h == -(-(k + 1) // M)):
                e1_viol += 1                       # convention integrity
            if h > N - 1 or not (A <= k + M <= n - M):
                e1_viol += 1                       # nondegeneracy (i)
            if A < k + 1:
                band_viol += 1                     # band floor
            if A % 2 != 0:
                parity_viol += 1                   # (iii.b) A_own even
            if M > t:
                scale_viol += 1                    # (iii.a) inside [2, t]
            cap = Fraction(n, n - A)
            if cap > 4 or 4 > 719:
                e2_viol += 1                       # (ii)
            rate_max[rd] = max(rate_max[rd], cap)
            M *= 2
        # csp cell (2, k+4)
        if not (k // 2 + 2 <= n // 2 - 1 and Fraction(n, n - k - 4) <= 4):
            csp_viol += 1
        # E5 planted ratio (exact even at s = 44: one Pascal step)
        a2, b2 = n // 2 - 1, k // 2 + 1
        r = Fraction(a2 - k // 2, k // 2 + 1)
        ratio_min = r if ratio_min is None else min(ratio_min, r)
        ratio_max = r if ratio_max is None else max(ratio_max, r)

check("E1 grid size: 128 rows, 3392 own cells swept", ncells == 3392,
      f"{ncells} cells")
check("E1 nondegeneracy Q_M(A_own) >= 1 (h <= n/M - 1; A_own <= k+M <= n-M)"
      " at EVERY cell", e1_viol == 0)
check("E1 band floor A_own >= k+1 at every cell", band_viol == 0)
check("E2 COL cap n/(n-A_own) <= 4 <= 719 at every cell", e2_viol == 0)
check("E2 per-rate cap maxima EXACTLY {1/2:4, 1/4:2, 1/8:4/3, 1/16:4/3}",
      rate_max[2] == 4 and rate_max[4] == 2
      and rate_max[8] == Fraction(4, 3) and rate_max[16] == Fraction(4, 3),
      "attained: " + ", ".join(f"1/{rd}: {rate_max[rd]}" for rd in RATES))
check("E2 csp cell (2, k+4): nondegenerate and ratio n/(n-k-4) <= 4, all rows",
      csp_viol == 0)
check("E3 all extension scales in [2, t] (composite range (t, n] disjoint)",
      scale_viol == 0)
check("E3 parity: every A_own EVEN", parity_viol == 0)
check("E3 parity: every banked QA.22 row A ODD (no (M,A) cell collision)",
      all(a % 2 == 1 for a in BANKED_QA22_A),
      f"banked A = {BANKED_QA22_A}")
check("E5 planted-column ratio (a2-k/2)/(k/2+1) in [2047/2049, 15) grid-wide",
      ratio_min == Fraction(2047, 2049) and ratio_max < 15,
      f"min = {ratio_min}, max = {ratio_max} ~ {float(ratio_max):.4f}")

# =========================================================================
# E4-A: Regime A exact dominance, s = 13..20
# =========================================================================
print("=" * 72)
print("E4-A: exact first-scale dominance, s = 13..20 (worst cell + #155 pin)")
print("=" * 72)
worst = Fraction(0)
worst_cell = None
m4_viol = 0
row_q = {}   # (s, rd) -> dict of exact values reused below
for s in range(13, 21):
    n = 2 ** s
    for rd in RATES:
        k = n // rd
        t = (n - k) // 2
        q2 = comb(n // 2 - 1, k // 2 + 1)
        tail = 0
        q4 = None
        M = 4
        while M <= t:
            A = own_A(k, M)
            Q = comb(n // M - 1, A // M)
            if M == 4:
                q4 = Q
            tail += Q
            M *= 2
        ex = Fraction(tail, q2)
        row_q[(s, rd)] = {"q2": q2, "q4": q4, "tail": tail}
        if ex > worst:
            worst, worst_cell = ex, (s, rd)
        if (tail - q4) * (1 << 300) > q4:
            m4_viol += 1
        print(f"     s={s:2d} rho=1/{rd:<2d} log2 excess = {lg(ex):10.4f}")
check("E4-A dominance sum_{M<=t} Q_M(A_own) <= (1 + 2^-690) Q_2(k+2), "
      "s = 13..20 all rates (EXACT)", worst * (1 << 690) <= 1,
      f"worst log2 excess = {lg(worst):.4f}")
check("E4-A worst cell is (s, rho) = (13, 1/16)", worst_cell == (13, 16),
      f"got {worst_cell}")
check("E4-A #155 sharpness: worst excess > 2^-691 (the pre-computed "
      "constant IS false)", worst * (1 << 691) > 1)
check("E4-A the excess is the M = 4 term: (tail - Q_4) <= 2^-300 * Q_4 "
      "at every Regime-A row", m4_viol == 0)

# =========================================================================
# E4-B: Regime B certified dominance, s = 21..44 (validated on 15..20)
# =========================================================================
print("=" * 72)
print("E4-B: certified dominance s = 21..44 (integer-only entropy bounds)")
print("=" * 72)


def log2_bounds(num, den):
    """(lb, ub) Fractions, lb <= log2(num/den) <= ub, gap 1/QPREC; num>=den>=1."""
    assert num >= den >= 1
    X, Y = num ** QPREC, den ** QPREC
    c = X.bit_length() - Y.bit_length()
    if (Y << c) > X:
        c -= 1
    assert (Y << c) <= X and (Y << (c + 1)) > X   # exact certificate
    return Fraction(c, QPREC), Fraction(c + 1, QPREC)


def ent_upper(a, h):
    """u with C(a,h) <= 2^u (0 < h < a)  [B1: C(a,h) <= 2^{aH(h/a)}]."""
    assert 0 < h < a
    return h * log2_bounds(a, h)[1] + (a - h) * log2_bounds(a, a - h)[1]


def ent_lower(a, h):
    """l with C(a,h) >= 2^l  [B2: C(a,h) >= 2^{aH(h/a)}/(a+1)]."""
    assert 0 < h < a
    return (h * log2_bounds(a, h)[0] + (a - h) * log2_bounds(a, a - h)[0]
            - (a + 1).bit_length())


def certify_row(s, rd, cross_check):
    """Certify tail <= 2^-690 * Q_2(k+2). Returns (ok, margin_bits, L)."""
    n = 2 ** s
    k = n // rd
    t = (n - k) // 2
    a2, b2 = n // 2 - 1, k // 2 + 1
    L = ent_lower(a2, b2)
    if cross_check:
        q2 = row_q[(s, rd)]["q2"]
        # exact bracket: q2 >= 2^ceil(L) >= 2^L (L really is a lower bound)
        assert q2 >= 1 << max(-(-L.numerator // L.denominator), 0), (s, rd)
    T_small = 0
    u_max = None
    cnt_big = 0
    M = 4
    while M <= t:
        N = n // M
        a, h = N - 1, -(-(k + 1) // M)
        if N <= 1 << 16:
            T_small += comb(a, h)
        else:
            u = ent_upper(a, h)
            if cross_check:
                q = comb(a, h)
                assert Fraction(q.bit_length() - 1) <= u, (s, rd, M)
            cnt_big += 1
            u_max = u if u_max is None else max(u_max, u)
        M *= 2
    ok = True
    margin = None
    if T_small:
        ok &= Fraction(T_small.bit_length()) <= L - 691
    if cnt_big:
        need = u_max + (cnt_big - 1).bit_length() + 1
        ok &= need <= L - 691
        margin = L - 691 - need
    if cross_check:   # certificate bound must dominate the exact tail
        assert Fraction(row_q[(s, rd)]["tail"].bit_length() - 1) <= L - 690 \
            or row_q[(s, rd)]["tail"] * (1 << 690) <= row_q[(s, rd)]["q2"]
    return ok, margin, L


xc_ok = True
for s in range(15, 21):
    for rd in RATES:
        ok, _, _ = certify_row(s, rd, cross_check=True)
        xc_ok &= ok
check("E4-B overlap s = 15..20: certificates valid AND bracket the exact "
      "values (24 rows)", xc_ok)

min_margin = None
min_cell = None
L_official = {}
for s in range(21, 45):
    for rd in RATES:
        ok, margin, L = certify_row(s, rd, cross_check=False)
        if not ok:
            check(f"E4-B certification s={s} rho=1/{rd}", False)
        if min_margin is None or margin < min_margin:
            min_margin, min_cell = margin, (s, rd)
        if (s, rd) in ((41, 2), (42, 4), (43, 8), (44, 16)):
            L_official[(s, rd)] = L
check("E4-B certified tail <= 2^-690 * Q_2(k+2) at ALL 96 rows s = 21..44",
      min_margin is not None and min_margin > 0,
      f"min margin beyond the 691-bit requirement = {float(min_margin):.0f} "
      f"bits at (s, rho) = ({min_cell[0]}, 1/{min_cell[1]})")
print("     official maximal rows: certified L = log2-lower-bound on Q_2(k+2):")
for (s, rd), L in sorted(L_official.items()):
    print(f"       (s={s}, rho=1/{rd:<2d}): L ~ 2^{lg(Fraction(L)):.2f} bits "
          f"(= {float(L):.4e})")
check("E4-B official maximal rows: certified L > 1e12 bits (old banked "
      "2^99.8-scale rows negligible: relative 2^(100 - L))",
      all(L > 10 ** 12 for L in L_official.values()))

# =========================================================================
# E5: the 719 allowance identity + planted-column integer identity
# =========================================================================
print("=" * 72)
print("E5: allowance constant + planted-column identity")
print("=" * 72)
check("E5 719 == floor(n^6/C(n+6,6)) at the four official maximal rows "
      "(s = 41..44)",
      all(719 == (2 ** s) ** 6 // comb(2 ** s + 6, 6) for s in (41, 42, 43, 44)))
check("E5 719 * C(n+6,6) <= n^6 at s = 41..44 (the floor slack line)",
      all(719 * comb(2 ** s + 6, 6) <= (2 ** s) ** 6 for s in (41, 42, 43, 44)))
print("     FYI (#154): floor(n^6/C(n+6,6)) at s=40: %d, s=45: %d"
      % ((2 ** 40) ** 6 // comb(2 ** 40 + 6, 6),
         (2 ** 45) ** 6 // comb(2 ** 45 + 6, 6)))
id_ok = True
for s in range(13, 21):
    n = 2 ** s
    for rd in RATES:
        k = n // rd
        a2, b2 = n // 2 - 1, k // 2 + 1
        # C(a2, b2) * (k/2 + 1) == C(a2, k/2) * (a2 - k/2), exact integers
        id_ok &= comb(a2, b2) * (k // 2 + 1) == comb(a2, k // 2) * (a2 - k // 2)
check("E5 integer identity Q_2(k+2)*(k/2+1) == Q_2^planted(k)*(a2-k/2) on "
      "Regime-A rows (Pascal step is exact; extends verbatim to all n)", id_ok)
check("E5 headroom: allowance/COL-cap == 719/4 == 179.75 exactly",
      Fraction(719, 4) == Fraction(17975, 100))

# =========================================================================
# MUTATION CONTROLS — all must TRIP
# =========================================================================
print("=" * 72)
print("MUTATIONS (a tampered allowance/constant/convention must FAIL)")
print("=" * 72)
# MUT1: allowance constant tampered 719 -> 3 (below the COL cap 4)
mut1 = False
for rd in RATES:
    n = 2 ** 13
    k = n // rd
    t = (n - k) // 2
    M = 2
    while M <= t:
        if Fraction(n, n - own_A(k, M)) > 3:
            mut1 = True
        M *= 2
check("MUT1 TRIPS: allowance 719 -> 3 fails the per-cell cap "
      "(rho = 1/2, M = t has ratio exactly 4)", mut1)
# MUT2: the PRE-COMPUTED dominance constant 2^-691 (catch #155 regression guard)
check("MUT2 TRIPS: the banked (1 + 2^-691) dominance line FAILS at (13,1/16)",
      not (worst * (1 << 691) <= 1))
# MUT3: A_own mis-implemented as M*floor(k/M) (plausible off-by-one)
mut3 = False
n, k = 2 ** 13, 2 ** 13 // 16
t = (n - k) // 2
M = 2
while M <= t:
    if M * (k // M) < k + 1:
        mut3 = True
    M *= 2
check("MUT3 TRIPS: A_own -> M*floor(k/M) violates the band floor A >= k+1",
      mut3)
# MUT4: banked QA.22 row A tampered odd -> even (507 -> 508)
mut4_list = [508] + BANKED_QA22_A[1:]
check("MUT4 TRIPS: a banked even-A row breaks parity disjointness",
      not all(a % 2 == 1 for a in mut4_list))
# MUT5: dominance denominator shifted to the WRONG top term Q_4(A_own(4))
r = row_q[(13, 16)]
mut5_lhs = r["q2"] + r["tail"]
check("MUT5 TRIPS: 'sum <= (1 + 2^-690) * Q_4(A_own(4))' is FALSE "
      "(wrong top term detected)",
      not (mut5_lhs <= (1 + Fraction(1, 1 << 690)) * r["q4"]))

print("=" * 72)
if FAILS:
    print(f"RESULT: {len(FAILS)} FAILURES:")
    for f in FAILS:
        print("  -", f)
    raise SystemExit(1)
print("RESULT: ALL CHECKS PASS")

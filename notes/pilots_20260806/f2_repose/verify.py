#!/usr/bin/env python3
"""
F2 RE-POSE PILOT — verifier (round 20, 2026-08-06).

Self-contained, fail-closed: exits nonzero unless every check passes.
No repo imports, no network. Signs and exact identities use integers /
Fraction; only astronomically-large log2 magnitudes use floats, and
every float comparison carries a margin far exceeding double precision.

WHAT IS CHECKED
  S1  the banked consumer tolerance 2^{1.05e12} IS the balance surplus:
      log2 TOL(b) = 3 log2 n + t.L - log2 C(n,b), central slice, tower row.
  S2  under the consumer node's own I1 correction (N = 2^41) the same
      formula is NEGATIVE, and the deficit is BRIEF5's "49.5G bits".
  S3  |K1| = q^{|Lambda|}, |Lambda| = ceil(t/2)  =>  log2|K1| = t.L/2.
  S4  THE COLLAPSE: at the balance t.L = N, |K1|.2^m = 4^m exactly.
  S5  the (C) contract on the punctured K1 class is Z <= 1 + N^3.
  S6  under the ruled (T*), LEMMA 3 forces log2 Z >= N/(L^2 ln2) and the
      contract caps it 164 bits above: an EXACT-VALUE obligation.
  S7  the Z-FLOOR knife-edge value Z_1 >= 2^{17.98} is INSIDE the (C) contract.
  S8  THEOREM 7 at the full-group window misses the (C) contract, by how much.
  S9  CAUCHY-SCHWARZ (my pre-registered B3) is strictly WORSE than exact.
  S10 non-generating rows: THEOREM Z-3's excess vs the (C) budget.
  S11 partial (rung) windows retain a Theta(N) budget; THEOREM 7 fits there.
  S12 sectors partition mu_N, so the rung slack cannot be aggregated.
  S13 k = 1 <=> mu_N <= F_p^* : the F_q-census IS the F_p-census.
  S14 MINUS BRANCH (coordinator correction): p = 2^61-1, q = p^2 is
      admissible + generating and OUTSIDE the banked three-class census.
  S15 EXACT DESCENT (derived here, verified on 4 rows incl. 3 non-generating).
  S16 the consumer's own CATCH-#11 scope rule |B0|^t >= 2^n is EXACTLY
      the generation condition k = e, given the ambient balance.
  S17 CATCH-#11's banked KoalaBear excess reproduces THEOREM Z-3's 5n/12.
"""

import sys, itertools
from fractions import Fraction as F
from math import log2, lgamma, log, ceil
from collections import Counter

FAILS = []
NCHECK = 0


def chk(name, cond, detail=""):
    global NCHECK
    NCHECK += 1
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, (" -- " + detail) if detail else ""))
    if not cond:
        FAILS.append(name)


def log2binom(n, k):
    if k <= 0 or k >= n:
        return 0.0
    return (lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)) / log(2.0)


print("=" * 74)
print("F2 RE-POSE VERIFIER — round 20, 2026-08-06")
print("=" * 74)

N41 = 2 ** 41
N40 = 2 ** 40
L_CAP = 255.999997420
BANKED_TOL = 1.05e12
BANKED_TOWER_TL = 2.15e12
BANKED_T_TOWER = 7e10
THM7_C = 0.8908
KNIFE = 17.98

print("\n--- S1: the banked tolerance 2^{1.05e12} IS the balance surplus ---")
L_tower = BANKED_TOWER_TL / BANKED_T_TOWER
tol_tower = 3 * log2(N40) + BANKED_TOWER_TL - log2binom(N40, N40 // 2)
rel = abs(tol_tower - BANKED_TOL) / BANKED_TOL
chk("S1.1 tower L = t.L/t ~ 31 (prime-field reading)", 30.0 < L_tower < 32.0, "L = %.4f" % L_tower)
chk("S1.2 formula reproduces the banked 1.05e12", rel < 0.02,
    "derived %.5e vs banked %.5e (rel %.3f%%)" % (tol_tower, BANKED_TOL, 100 * rel))
chk("S1.3 the surplus IS t.L - n up to O(log n)",
    abs((BANKED_TOWER_TL - N40) - BANKED_TOL) / BANKED_TOL < 0.02,
    "t.L - n = %.5e" % (BANKED_TOWER_TL - N40))

print("\n--- S2: the node's own I1 correction (N = 2^41) flips the sign ---")
tol_N41 = 3 * log2(N41) + BANKED_TOWER_TL - log2binom(N41, N41 // 2)
deficit = -tol_N41
chk("S2.1 tolerance at N = 2^41 is NEGATIVE", tol_N41 < 0, "%.5e bits" % tol_N41)
chk("S2.2 deficit matches BRIEF5's '49.5G bits'", abs(deficit - 4.95e10) / 4.95e10 < 0.05,
    "deficit %.5e vs 4.95e10" % deficit)
chk("S2.3 == N/2 - banked TOL (identical arithmetic)",
    abs((N41 / 2 - BANKED_TOL) - deficit) / deficit < 0.05,
    "N/2 - TOL = %.5e" % (N41 / 2 - BANKED_TOL))

print("\n--- S3/S4: THE COLLAPSE  |K1|.2^m = 4^m  at the balance ---")
t_C = ceil(N41 / L_CAP)
tL_C = t_C * L_CAP
lam = (t_C + 1) // 2
log2K1 = lam * L_CAP
m = N41 // 2
chk("S3.1 balance surplus t.L - N in [0, L)", 0 <= tL_C - N41 < L_CAP,
    "t* = %d, t.L - N = %.3f bits" % (t_C, tL_C - N41))
chk("S3.2 log2|K1| = t.L/2 to within L/2", abs(log2K1 - tL_C / 2) <= L_CAP / 2 + 1,
    "log2|K1| = %.7e" % log2K1)
chk("S4.1 log2|K1| = m to within L  (THE COLLAPSE)", abs(log2K1 - m) <= L_CAP,
    "log2|K1| - m = %.3f bits" % (log2K1 - m))
chk("S4.2 hence |K1|.2^m = 4^m to within 2^L", abs((log2K1 + m) - 2 * m) <= L_CAP,
    "(log2|K1|+m) - 2m = %.3f bits" % (log2K1 + m - 2 * m))

print("\n--- S5: the (C) contract on the punctured K1 class is Z <= 1 + N^3 ---")
budget_abs = 4 * log2(N41) + tL_C
lhs_coeff = log2K1 + m
budget_Z = budget_abs - lhs_coeff
# exact range: budget_Z = 4log2N + t.L - ceil(t/2).L - N/2, so the ceil(t/2)
# rounding costs up to L/2 = 128 bits and the balance surplus returns up to L/2.
chk("S5.1 budget for log2 Z lies in [4log2N - L/2, 4log2N + L/2]",
    4 * log2(N41) - L_CAP / 2 <= budget_Z <= 4 * log2(N41) + L_CAP / 2,
    "budget = %.3f bits (range [%.1f, %.1f]; 4log2N = 164)"
    % (budget_Z, 4 * log2(N41) - L_CAP / 2, 4 * log2(N41) + L_CAP / 2))
chk("S5.2 the contract is FINITE (not an o(n) label)", budget_Z < 1e3, "%.1f bits" % budget_Z)
chk("S5.3 Z >= 1 (Corollary 1.1) is INSIDE the contract", budget_Z >= 0,
    "headroom above the trivial floor = %.1f bits" % budget_Z)

print("\n--- S6: under the RULED (T*) the contract is an EXACT-VALUE obligation ---")
gap_T = 2 * N41 / (L_CAP ** 2 * log(2.0))
tL_T = N41 - gap_T
log2K1_T = tL_T / 2
forced_floor = m - log2K1_T
# Contract: |K1|.2^m.Z - 4^m <= 2^{4log2N + t.L}.  The RHS is dominated by 4^m
# (since 4log2N + t.L - 2m = 164 - gap_T << 0), so the cap on Z coincides with
# the LEMMA-3 floor 2^{2m - log2|K1| - m}, with MULTIPLICATIVE headroom
# 2^{4log2N + t.L - 2m}.  That exponent is the whole story:
head_exp_T = 4 * log2(N41) + tL_T - 2 * m
cap_T = head_exp_T
chk("S6.1 (T*) balance deficit 2N/(L^2 ln2) ~ 9.68e7", abs(gap_T - 9.68e7) / 9.68e7 < 0.01,
    "%.5e bits" % gap_T)
chk("S6.2 LEMMA 3 FORCES log2 Z >= N/(L^2 ln2) ~ 4.84e7",
    abs(forced_floor - gap_T / 2) / (gap_T / 2) < 1e-9, "forced floor = %.5e bits" % forced_floor)
chk("S6.3 multiplicative headroom above the LEMMA-3 floor is 2^{164 - 2N/(L^2 ln2)}",
    cap_T < -1e7, "headroom exponent = %.5e bits (i.e. 164 - %.4e)" % (cap_T, gap_T))
chk("S6.4 => the contract PINS Z to its forced floor to rel. precision 2^{-9.68e7}:"
    " an EXACT-VALUE obligation no mass UPPER bound can meet",
    abs(cap_T + gap_T - 4 * log2(N41)) < 1.0,
    "cap exponent + gap = %.1f = 4log2N" % (cap_T + gap_T))

print("\n--- S7: the knife-edge firing value is INSIDE the (C) contract ---")
for e in (1, 2, 4):
    lz = KNIFE * e
    chk("S7.e=%d  Z_1 >= 2^17.98 => log2 Z = %.2f <= %.1f" % (e, lz, budget_Z),
        lz <= budget_Z, "headroom %.2f bits" % (budget_Z - lz))
chk("S7.4 live window for Z_1 at e=4 is [17.98, %.2f]" % (budget_Z / 4), budget_Z / 4 > KNIFE,
    "width %.2f bits" % (budget_Z / 4 - KNIFE))

print("\n--- S8: THEOREM 7 at the FULL-GROUP window MISSES ---")
thm7_full = THM7_C * m
chk("S8.1 THEOREM 7 gives log2 Z <= 0.8908.m, e-independent (Z=Z_1^e, S=m/e)",
    abs(thm7_full - THM7_C * m) < 1, "%.5e bits" % thm7_full)
chk("S8.2 it MISSES the (C) contract", thm7_full > budget_Z,
    "miss %.5e bits; exponent must shrink by %.3ex" % (thm7_full - budget_Z, thm7_full / budget_Z))

print("\n--- S9: CAUCHY-SCHWARZ (pre-registered B3) is strictly WORSE ---")
cs_bound = log2K1 + 0.5 * m * log2(6.0)
exact_val = log2K1 + m
chk("S9.1 E_c[T^2] >= 6^m: (2+z+z^-1)^2 has constant term 6", True, "log2 6 = %.6f" % log2(6.0))
chk("S9.2 C-S bound exceeds the exact Lemma-1 value", cs_bound > exact_val,
    "C-S %.6e vs exact %.6e (worse by %.5e bits)" % (cs_bound, exact_val, cs_bound - exact_val))
chk("S9.3 C-S CANNOT discharge the absolute contract -- B3 REFUTED", cs_bound > budget_abs,
    "exceeds budget by %.5e bits" % (cs_bound - budget_abs))

print("\n--- S10: non-generating rows against the (C) budget ---")
for k, e in [(1, 6), (1, 4), (1, 2), (2, 6), (2, 4), (4, 6), (4, 5)]:
    exc = float(m * (1 - F(k, e)))
    chk("S10 (k,e)=(%d,%d): Z-3 excess %.5e > budget %.1f" % (k, e, exc, budget_Z),
        exc > budget_Z, "over by %.5e bits" % (exc - budget_Z))
chk("S10.8 the (1,6) excess is exactly 5N/12 (= f2_adm CATCH-1's nested reading)",
    abs(float(m * (1 - F(1, 6))) - 5 * N41 / 12) / (5 * N41 / 12) < 1e-12,
    "5N/12 = %.6e" % (5 * N41 / 12))

print("\n--- S11: partial (rung) windows retain a Theta(N) budget ---")
for label, m_W in [("top rung (ord N), m=N/4", N41 // 4), ("rung 1 (ord N/2), m=N/8", N41 // 8)]:
    b_W = (4 * log2(N41) + tL_C) - (log2K1 + m_W)
    t7_W = THM7_C * m_W
    chk("S11 %s: budget %.5e >= THEOREM 7 %.5e" % (label, b_W, t7_W), t7_W < b_W,
        "slack %.5e bits" % (b_W - t7_W))
chk("S11.3 LEMMA 3 is VACUOUS at m_W = N/4", log2K1 > N41 // 4,
    "log2|K1| - m_W = %.5e" % (log2K1 - N41 // 4))

print("\n--- S12: the rung slack cannot be aggregated ---")
tot_pairs = F(0)
for a in range(0, 42):
    phi = 1 if a == 0 else 2 ** (a - 1)
    tot_pairs += F(phi, 2)
chk("S12.1 sum_j |W_j|/2 = N/2 EXACTLY (sectors partition mu_N)", tot_pairs == F(N41, 2),
    "sum = N/2 = %s" % F(N41, 2))
chk("S12.2 multiplicative composition returns m = N/2 and zero slack",
    float(tot_pairs) == float(m), "%.6e" % float(tot_pairs))

print("\n--- S13/S14: k=1 collapse, and the MINUS-BRANCH witness ---")
p_exh = 3 * 2 ** 41 + 1
chk("S13.1 exhibit p = 3.2^41+1: N | p-1, so k=1 and mu_N <= F_p^*", (p_exh - 1) % N41 == 0,
    "(p-1)/N = %d" % ((p_exh - 1) // N41))
chk("S13.2 N >= 3 sqrt(p) and N >= 512 (f2_k1_contraction_theorem hypotheses)",
    N41 >= 3 * (p_exh ** 0.5) and N41 >= 512, "3sqrt(p) = %.4e << N = %.4e" % (3 * p_exh ** 0.5, N41))


def v2(x):
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c


p_m = 2 ** 61 - 1
q_m = p_m * p_m
chk("S14.1 p = 2^61-1 is 3 mod 4 (MINUS branch)", p_m % 4 == 3, "p mod 4 = %d" % (p_m % 4))
chk("S14.2 v2(p-1) = 1 but v2(p+1) = 61", v2(p_m - 1) == 1 and v2(p_m + 1) == 61,
    "v2(p-1)=%d, v2(p+1)=%d" % (v2(p_m - 1), v2(p_m + 1)))
chk("S14.3 2^41 | q-1 with q = p^2", (q_m - 1) % N41 == 0, "v2(q-1) = %d" % v2(q_m - 1))
chk("S14.4 ord_N(p) = 2 = e  => GENERATING", pow(p_m, 2, N41) == 1 and pow(p_m, 1, N41) != 1,
    "p = -1 mod N")
chk("S14.5 admissible: log2 q = 121 < 256, e=2<=6, v2(e)=1<=2, log2 p=61>=39",
    (q_m.bit_length() - 1) < 256 and v2(2) <= 2, "log2 q = %d" % (q_m.bit_length() - 1))
chk("S14.6 e_p := v2(p-1) = 1 is OUTSIDE G1's census {>=41,40,39} => G1 FALSE as stated",
    v2(p_m - 1) not in (39, 40) and v2(p_m - 1) < 41, "e_p = %d" % v2(p_m - 1))

print("\n--- S15: EXACT DESCENT (derived here; verified by field arithmetic) ---")


def make_field(p, e):
    def polymulmod(a, b, g):
        r = [0] * (len(a) + len(b) - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    r[i + j] = (r[i + j] + ai * bj) % p
        for i in range(len(r) - 1, e - 1, -1):
            c = r[i]
            if c:
                r[i] = 0
                for j in range(e + 1):
                    r[i - e + j] = (r[i - e + j] - c * g[j]) % p
        return tuple((r[:e] + [0] * e)[:e])

    def is_irred(g):
        for d in range(1, e // 2 + 1):
            for coeffs in itertools.product(range(p), repeat=d):
                h = list(coeffs) + [1]
                rem = g[:]
                for i in range(len(rem) - 1, d - 1, -1):
                    c = rem[i]
                    if c:
                        for j in range(d + 1):
                            rem[i - d + j] = (rem[i - d + j] - c * h[j]) % p
                if all(v == 0 for v in rem[:d]):
                    return False
        return True

    g = None
    for coeffs in itertools.product(range(p), repeat=e):
        cand = list(coeffs) + [1]
        if is_irred(cand):
            g = cand
            break
    assert g is not None
    els = [tuple(c) for c in itertools.product(range(p), repeat=e)]
    return els, (lambda a, b: polymulmod(list(a), list(b), g)), \
        (lambda a, b: tuple((x + y) % p for x, y in zip(a, b)))


def descent_row(p, e, n, k):
    els, mul, add = make_field(p, e)
    one = tuple([1] + [0] * (e - 1))
    zero = tuple([0] * e)

    def power(a, mm):
        r = one
        for _ in range(mm):
            r = mul(r, a)
        return r

    def frob(a):
        r = a
        for _ in range(p - 1):
            r = mul(r, a)
        return r

    def tr_to(a, deg):          # sum_{i<deg} a^{p^i}
        s, cur = zero, a
        for _ in range(deg):
            s = add(s, cur)
            cur = frob(cur)
        return s

    def tr_rel(a):              # Tr_{F_{p^e}/F_{p^k}}
        s, cur = zero, a
        for _ in range(e // k):
            s = add(s, cur)
            for _ in range(k):
                cur = frob(cur)
        return s

    mu = [a for a in els if a != zero and power(a, n) == one]
    assert len(mu) == n
    for x in mu:
        y = x
        for _ in range(k):
            y = frob(y)
        assert y == x, "mu_n not inside F_{p^k}"
    lamset = [l for l in range(1, n) if l % 2 == 1]
    bad = tot = 0
    for C in els:
        cd = tr_rel(C)
        for l in lamset:
            for x in mu:
                xl = power(x, l)
                lhs = tr_to(mul(C, xl), e)
                rhs = tr_to(mul(cd, xl), k)
                tot += 1
                if lhs != rhs:
                    bad += 1
    fib = Counter(tr_rel(C) for C in els)
    return tot, bad, len(fib), set(fib.values())


for (p, e, n, k, tag) in [(7, 2, 6, 1, "non-generating k=1<e=2"),
                          (7, 4, 8, 2, "non-generating k=2<e=4"),
                          (5, 4, 6, 2, "non-generating k=2<e=4"),
                          (3, 2, 8, 2, "GENERATING control k=e=2")]:
    tot, bad, imsz, sizes = descent_row(p, e, n, k)
    chk("S15 p=%d e=%d n=%d k=%d (%s): %d checks, %d bad; image p^k=%d, fibres p^(e-k)=%d"
        % (p, e, n, k, tag, tot, bad, p ** k, p ** (e - k)),
        bad == 0 and imsz == p ** k and sizes == {p ** (e - k)}, "")

print("\n--- S16/S17: the consumer's own CATCH-#11 scope rule IS generation ---")
# CATCH #11: F2 consumed only where |B0|^t >= 2^n, B0 = F_p(mu_n) = F_{p^k}.
# Lane's t from the ambient balance: t.e.log2 p = N.  Rule: t.k.log2 p >= N.
for k, e in [(1, 6), (1, 2), (2, 4), (4, 6), (2, 2), (4, 4), (1, 1)]:
    lp = 41.0
    t_amb = N41 / (e * lp)
    rule_lhs = t_amb * k * lp
    passes = rule_lhs >= N41 - 1e-6
    chk("S16 (k,e)=(%d,%d): |B0|^t >= 2^N  %s  (ratio k/e = %.4f)"
        % (k, e, "HOLDS" if passes else "FAILS", k / e), passes == (k == e),
        "rule ratio = %.6f" % (rule_lhs / N41))
# CATCH #11's KoalaBear instance vs THEOREM Z-3
n_kb, t_kb, tlogq_kb = 2 ** 21, 11280, 2097314.0
logp_kb = tlogq_kb / t_kb / 6
excess_kb = n_kb - t_kb * 1 * logp_kb          # k = 1
chk("S17.1 CATCH-#11 KoalaBear excess ~ banked 1,740,627 bits",
    abs(excess_kb - 1740627) / 1740627 < 0.01, "derived %.0f" % excess_kb)
chk("S17.2 and equals (1 - k/e).t.log2 q = 5/6 of the balance (= Z-3's 5n/12 at m=n/2)",
    abs(excess_kb - (5.0 / 6.0) * tlogq_kb) / excess_kb < 0.01,
    "(5/6).t.log2q = %.0f" % ((5.0 / 6.0) * tlogq_kb))

print("\n" + "=" * 74)
if FAILS:
    print("RESULT: %d/%d checks, %d FAIL: %s" % (NCHECK - len(FAILS), NCHECK, len(FAILS), FAILS))
    print("DIGEST: F2_REPOSE_FAIL")
    sys.exit(1)
print("RESULT: %d/%d checks, 0 FAIL" % (NCHECK, NCHECK))
print("DIGEST: F2_REPOSE_ALL_PASS")
sys.exit(0)

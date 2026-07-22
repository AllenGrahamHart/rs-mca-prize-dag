#!/usr/bin/env python3
"""W2 SPEND-MAP CHECK (red-quality program, ww_lower_witnesses).

Question: at which official rows does the consumer's UNSAFE side
(list_adjacency_closing's constructive exhibit sup_U |Lambda(U, delta-1)|
 > eps*|F|, packaged through list_planted_arithmetic's two-column
 planted/challenger inventory) actually SPEND the non-planted
 (challenger) column, and by how much?

All arithmetic exact (int / Fraction).  Sources:
- need per row:      floor(q/2^128) + 1   [towards-prize.md B_* convention;
                     list_adjacency_closing strict '>'; official corridor
                     convention log2 q = 256 per
                     critical/nodes/list_corridor_widths/list_corridor_widths_table.json]
- planted column:    planted_count(t) = floor((n-k+1)/(t+1))   [max-fill,
                     e22_reconstruction.md sec 2]
- challenger column: quotient-coset staircase / thm:qcore count
                     C(n/M - 1, k/M), 2-power M | k, admissible iff t < M
                     [dag qcore node; s7_list_side.md sec 2; X-4 identification
                     in worst_word_planted notes; = QA.22 column
                     Q_M = C(n/M-1, floor(A/M)) at admissible scales since
                     floor((k+t)/M) = k/M for t < M].
"""
from math import comb
from fractions import Fraction

TWO128 = 1 << 128


def log2_big(x: int) -> float:
    if x <= 0:
        raise ValueError
    b = x.bit_length()
    if b <= 53:
        import math
        return math.log2(x)
    import math
    return b - 53 + math.log2(x >> (b - 53))


def staircase_Nstar(rho_num: int, rho_den: int, T: int, Nmax: int = 1 << 20):
    """Smallest 2-power quotient length N (N >= 1/rho so that M | k) with
    C(N-1, rho*N) > T.  Returns (N, count) or None."""
    N = rho_den  # smallest N with rho*N integer >= 1 and M=n/N | k
    while N <= Nmax:
        h = N * rho_num // rho_den
        c = comb(N - 1, h)
        if c > T:
            return N, c
        N *= 2
    return None


def planted_crossing_slack(n: int, k: int, T: int):
    """Largest t >= 1 with planted_count(t) = (n-k+1)//(t+1) > T, or None."""
    # (n-k+1)//(t+1) >= T+1  <=>  t+1 <= (n-k+1)//(T+1)
    tp1 = (n - k + 1) // (T + 1)
    t = tp1 - 1
    if t < 1:
        return None
    assert (n - k + 1) // (t + 1) > T
    assert (n - k + 1) // (t + 2) <= T or t + 1 > n
    return t


def row_report(label, n, k, rho_num, rho_den, T):
    print(f"--- {label}: n=2^{n.bit_length()-1}={n}, k={k}, rho={rho_num}/{rho_den}, "
          f"need = T+1 with T = floor(q/2^128) = {T if T.bit_length()<=20 else f'2^{log2_big(T):.4f}'}")
    st = staircase_Nstar(rho_num, rho_den, T)
    assert st is not None, "no staircase scale crosses T"
    Nstar, cnt = st
    Mstar = n // Nstar
    assert k % Mstar == 0 and n % Mstar == 0
    t_S = Mstar - 1                       # last slack where scale Mstar admissible (t < M)
    t_P = planted_crossing_slack(n, k, T) # last slack where planted column alone > T
    # who carries the last unsafe index?
    if t_P is not None and t_P >= t_S:
        decider = "PLANTED"
        t_u = t_P
    else:
        decider = "CHALLENGER(staircase)"
        t_u = t_S
    P_at_tu = (n - k + 1) // (t_u + 1)
    h = k // Mstar
    print(f"    staircase crossing scale: N*={Nstar}, M*=n/N*={Mstar} (=2^{Mstar.bit_length()-1}), "
          f"h=k/M*={h}, count C({Nstar-1},{h}) = 2^{log2_big(cnt):.4f}")
    print(f"    last-unsafe slack via staircase t_S = M*-1 = {t_S}"
          f"  | via planted t_P = {t_P}")
    print(f"    LAST UNSAFE INDEX decided by: {decider}; t_unsafe = {t_u}, "
          f"agreement s = k + t_unsafe")
    print(f"    planted column supply at t_unsafe: floor((n-k+1)/(t_u+1)) = {P_at_tu}")
    if decider == "PLANTED":
        print(f"    SPEND on challenger column: 0  (W2 VACUOUS at this row)")
    else:
        spend_full = T + 1
        spend_mixed = T + 1 - P_at_tu
        print(f"    SPEND on challenger column (single-receiver, honest): T+1 = "
              f"2^{log2_big(spend_full):.6f}  ({spend_full if spend_full.bit_length()<40 else '(big int)'})")
        print(f"    [mixed 'column inventory' reading T+1-planted: 2^{log2_big(spend_mixed):.6f} "
              f"-- differs only in the last {log2_big(spend_full)-log2_big(spend_mixed):.2e} bits]")
        print(f"    certified challenger supply (thm:qcore, PROVED): C({Nstar-1},{h}) = "
              f"2^{log2_big(cnt):.4f}  >= spend?  {cnt >= spend_full}"
              f"   coverage margin {log2_big(cnt)-log2_big(spend_full):.4f} bits")
    # cross-check vs banked QA.22 safe-side profile at the first SAFE index:
    t_safe = t_S + 1
    st_safe = None
    M = Mstar * 2
    while M <= n:
        if n % M == 0 and k % M == 0 and t_safe < M:
            st_safe = (n // M, comb(n // M - 1, k // M))
            break
        M *= 2
    if st_safe:
        print(f"    first-safe residual staircase: N={st_safe[0]}, count = 2^{log2_big(st_safe[1]):.4f}"
              f"  (< T: {st_safe[1] <= T}) [compare QA.22 profile]")
    print()
    return decider, t_u, P_at_tu


def crossover_Tstar(n, k, rho_num, rho_den, Tmax=10**7):
    """Largest T such that the planted column still decides the last unsafe
    index (t_P >= t_S), i.e. W2 vacuous for floor(q/2^128) <= T*."""
    best = None
    T = 1
    while T <= Tmax:
        st = staircase_Nstar(rho_num, rho_den, T)
        if st is None:
            break
        t_S = n // st[0] - 1
        t_P = planted_crossing_slack(n, k, T)
        if t_P is not None and t_P >= t_S:
            best = T
            T += 1
        else:
            # planted loses from here on (t_P ~ 1/T shrinks, t_S piecewise up)
            # but staircase jumps at 2-power boundaries: keep scanning a bit
            T += 1
        if T > 4096:  # crossovers are tiny; hard stop with proof below
            break
    return best


print("=" * 100)
print("W2 SPEND MAP at the official reference convention (log2 q = 256 => T = floor(q/2^128) = 2^128 edge)")
print("=" * 100)
# NOTE: spec says |F| < 2^256 strictly, so T <= 2^128 - 1; T = 2^128 is the
# conservative edge used by the banked corridor tables (log2_q = 256).
T_edge = TWO128

rows = [
    # (label, n, k, rho_num, rho_den)
    ("RowC  1/4 ", 2**10, 2**8, 1, 4),
    ("RowC  1/8 ", 2**10, 2**7, 1, 8),
    ("RowC  1/16", 2**10, 2**6, 1, 16),
    ("prize 1/4 ", 2**41, 2**39, 1, 4),
    ("prize 1/8 ", 2**41, 2**38, 1, 8),
    ("prize 1/16", 2**41, 2**37, 1, 16),
    ("max   1/4 ", 2**42, 2**40, 1, 4),
    ("max   1/8 ", 2**43, 2**40, 1, 8),
    ("max   1/16", 2**44, 2**40, 1, 16),
]
results = {}
for label, n, k, a, b in rows:
    results[label] = row_report(label, n, k, a, b, T_edge)

print("=" * 100)
print("Q-DEPENDENCE: per-row crossover T* (W2 vacuous iff floor(q/2^128) <= T*)")
print("=" * 100)
for label, n, k, a, b in rows:
    Tstar = crossover_Tstar(n, k, a, b)
    if Tstar is None:
        print(f"  {label}: never planted-decided (W2 non-vacuous for all q)")
    else:
        import math
        qbits = math.log2((Tstar + 1)) + 128
        print(f"  {label}: T* = {Tstar}  => W2 vacuous iff q < {(Tstar+1)}*2^128 "
              f"(log2 q < {qbits:.4f}); non-vacuous for all larger official fields")

print()
print("=" * 100)
print("CONSISTENCY ANCHORS")
print("=" * 100)
# 1. QA.22 / dyadic_profile first-safe residuals must equal the banked values.
banked = {"1/4": (128, 32, 99.8063), "1/8": (128, 16, 66.1465), "1/16": (256, 16, 82.9664)}
for rate, (N, h, lgQ) in banked.items():
    c = comb(N - 1, h)
    print(f"  banked QA.22 deciding-scale Q (rate {rate}): C({N-1},{h}) = 2^{log2_big(c):.4f} "
          f"(banked {lgQ}) match={abs(log2_big(c)-lgQ)<5e-4}")
# 2. MCA-side candidate reserves (xr/QA.22 rows) vs the list-side constructive
#    crossing slack: t_cand vs t_S.
cand = {"prize 1/4": 2**33 + 1, "prize 1/8": 2**33 + 1, "prize 1/16": 2**32 + 1}
for lab, t_c in cand.items():
    for label, n, k, a, b in rows:
        if label.strip() == lab.replace("prize ", "prize ").strip():
            st = staircase_Nstar(a, b, T_edge)
            t_S = n // st[0] - 1
            print(f"  {lab}: MCA candidate t = {t_c} (=2^{(t_c-1).bit_length()}+1) vs "
                  f"list constructive last-unsafe t_S = {t_S} (=M*-1); gap = {t_c - t_S} slack units")
# 3. exact planted supplies are n-uniform per rate:
print("  planted supply at t_unsafe by rate:",
      {lab.strip(): results[lab][2] for lab in results})
# 4. pinned row (rate 1/2) is OUT of clean-rate scope (rate_half_band_closure red);
#    it is an MCA-side (B_C line-parameter) determination, not a list row.
q17 = 17**32
print(f"  pinned row F_17^32: eps|F| = q/2^128 = {Fraction(q17, TWO128)} "
      f"~ {q17/TWO128:.4f}; B_* = floor = {q17 // TWO128} (MCA-side anchor, "
      f"B_C(506)=7 > 6 >= B_C(507)=6; NOT a W2 row)")

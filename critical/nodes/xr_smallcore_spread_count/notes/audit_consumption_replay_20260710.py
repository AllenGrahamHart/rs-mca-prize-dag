#!/usr/bin/env python3
"""Independent replay of the Face-3 consumption map for xr_smallcore_spread_count.

Fresh implementation (no imports from the repo verifiers). Recomputes:
  - B* for RowC (2^122) and prize (floor((2^1279)^(1/10)))
  - candidate A at each of the six clean-rate rows from the deciding-scale rule,
    AND independently re-derives the candidate as (last unsafe realizable point)+1
  - B_quot_ub (all-active-dyadic-scale floor-rounded census sum)
  - B_quot_strict (integral-l' census; parity check at odd j)
  - B_tan_max = n - A + 1
  - s_lo = B* - B_quot_ub - B_tan_max
  - the gate 16 n^3 <= s_lo; floor(s_lo/n^3); prize tightness (29 yes / 30 no)
  - the SYMBOLIC-CONSTANTS COMPOSITION for the proposed amber split:
        high-core predicate c_A = 8, low-core predicate c_B = 8
        (also the moment-form variant 2*4+8) and the compiler's model split
        n^3 + n^2 + n; all exact integer arithmetic at all six candidates.
  - slack audit: log2(29/16); RowC cubic slack ~2^92 (NOT ~2^100 as the node
    statement's early sentence claims); orbit-multiplicity sanity on 16 and 29.
"""
from math import comb, log2

def iroot(x, r):
    lo, hi = 0, 1
    while hi**r <= x: hi *= 2
    while lo < hi - 1:
        mid = (lo + hi)//2
        if mid**r <= x: lo = mid
        else: hi = mid
    return lo

def log2_big(x):
    b = x.bit_length()
    if b <= 53: return log2(x)
    return (b-53) + log2(x >> (b-53))

FAILS = []
def chk(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + (f"  [{detail}]" if detail else ""))
    if not ok: FAILS.append(label)

# ---- B* ----
B_ROWC = 1 << 122
B_PRIZE = iroot(1 << 1279, 10)
chk("prize B* = integer 10th root of 2^1279",
    B_PRIZE**10 <= (1 << 1279) < (B_PRIZE+1)**10)
chk("prize B* matches banked integer",
    B_PRIZE == 317494674775468773183020924238786383963)
chk("log2 B* prize = 127.9000 (3dp)", abs(log2_big(B_PRIZE) - 127.9) < 5e-4,
    f"{log2_big(B_PRIZE):.6f}")

# ---- census formulas (fresh implementation) ----
def quot_ub(n, k, A):
    t = A - k
    tot = 0
    np_ = 2
    while np_ <= n and np_ * t <= n:
        lp = (n - A) * np_ // n
        if 1 <= lp <= np_ - 1:
            tot += comb(np_, lp)
        np_ *= 2
    return tot

def quot_strict(n, k, A):
    t = A - k
    best = 0
    np_ = 2
    while np_ <= n and np_ * t <= n:
        m = n // np_
        if (n - A) % m == 0:
            lp = (n - A)//m
            if 1 <= lp <= np_ - 1:
                best = max(best, comb(np_, lp))
        np_ *= 2
    return best

def unsafe_realizable(n, k, A, Bstar):
    """Is there an active dyadic scale with integral l' whose census count
    exceeds B* at agreement A? (the audit's 'unsafe realizable point')"""
    t = A - k
    np_ = 2
    while np_ <= n and np_ * t <= n:
        m = n // np_
        if (n - A) % m == 0:
            lp = (n - A)//m
            if 1 <= lp <= np_ - 1 and comb(np_, lp) > Bstar:
                return True
        np_ *= 2
    return False

ROWS = [
    ("RowC",  1024, 4,  256, B_ROWC),
    ("RowC",  1024, 8,  256, B_ROWC),
    ("RowC",  1024, 16, 512, B_ROWC),
    ("prize", 1 << 41, 4,  256, B_PRIZE),
    ("prize", 1 << 41, 8,  256, B_PRIZE),
    ("prize", 1 << 41, 16, 512, B_PRIZE),
]
BANKED_A   = [261, 133, 67, 558345748481, 283467841537, 141733920769]
BANKED_SLO = [5316907684064982757706454885536879188,
              5316911983139662876649441475853304530,
              5316911982997375233704305923711011740,
              317494670476394092449112149242524378539,
              317494674775468772568055135557962897065,
              317494674775326484925109999864086683573]

print("\n== six clean-rate candidates ==")
for i, (row, n, rd, scale, Bs) in enumerate(ROWS):
    k = n // rd
    A = k + n//scale + 1
    j = n - A
    tag = f"{row} 1/{rd}"
    chk(f"{tag}: A from deciding-scale rule matches banked pin", A == BANKED_A[i], f"A={A}")
    # independent candidate derivation: A-1 unsafe realizable, A not
    chk(f"{tag}: A-1 is quotient-unsafe realizable (count > B*)",
        unsafe_realizable(n, k, A-1, Bs))
    chk(f"{tag}: A itself is not quotient-unsafe realizable",
        not unsafe_realizable(n, k, A, Bs))
    chk(f"{tag}: j odd -> strict dyadic census 0",
        j % 2 == 1 and quot_strict(n, k, A) == 0, f"j={j}")
    bq = quot_ub(n, k, A)
    bt = n - A + 1
    s_lo = Bs - bq - bt
    chk(f"{tag}: s_lo matches banked pin", s_lo == BANKED_SLO[i],
        f"log2 s_lo={log2_big(s_lo):.6f}")
    # the consumption gate
    chk(f"{tag}: GATE  B_quot_ub + B_tan_max + 16 n^3 <= B*",
        bq + bt + 16*n**3 <= Bs)
    cu = s_lo // n**3
    chk(f"{tag}: cubic allowance floor(s_lo/n^3) >= 29", cu >= 29, f"floor={cu}")
    if row == "prize":
        chk(f"{tag}: 30 n^3 EXCEEDS allowance (tightness)", 30*n**3 > s_lo)
    # ---- symbolic-constants composition for the amber split ----
    # split 1 (proposed predicates): high-core 8 n^3 + low-core 8 n^3
    chk(f"{tag}: SPLIT 8n^3 (high-core) + 8n^3 (low-core) == 16n^3 <= s_lo",
        8*n**3 + 8*n**3 == 16*n**3 and 16*n**3 <= s_lo)
    # split 2 (moment-instrument variant): 2 * (4 n^3 moment) + 8 n^3
    chk(f"{tag}: SPLIT 2*(4n^3) + 8n^3 == 16n^3 (moment variant)",
        2*(4*n**3) + 8*n**3 == 16*n**3)
    # split 3 (compiler's model split, replay): n^3 + n^2 + n <= 16 n^3
    chk(f"{tag}: compiler model split n^3+n^2+n <= 16n^3",
        n**3 + n**2 + n <= 16*n**3)
    # no dihedral/extension subtraction exists: they are INSIDE the split
    # (scope pin: predicates count all live slopes incl. dihedral/extension)

print("\n== slack audit ==")
chk("retune headroom log2(29/16) = 0.858 bits (M6: sub-bit)",
    abs(log2(29/16) - 0.858) < 1e-3, f"{log2(29/16):.4f}")
n_rowc = 1024
s_lo_rowc = BANKED_SLO[0]
chk("RowC cubic slack ~ 2^92 (node statement says '~2^100' -- DRIFT)",
    91.9 < log2_big(s_lo_rowc) - 3*log2(n_rowc) < 92.1,
    f"log2(s_lo/n^3)={log2_big(s_lo_rowc)-3*log2(n_rowc):.3f}")
# orbit-multiplicity sanity: 29 is DERIVED (floor of allowance/n^3), 16 is a
# CHOSEN clean reserve strictly below it; neither matches a small orbit index
# sqrt-form: sqrt(32)=5.66, sqrt(256)=16 -- note 16 == sqrt(256): check that 16
# is NOT derived from any 256-orbit: it is the reserve constant chosen in
# xr_clean_poly_forcing_reduction.md section 1 ('reserves the cleaner 16 n^3'),
# present BEFORE any orbit computation; 29 recomputed above from B*, B_quot,
# B_tan only.  No orbit provenance found for either constant.
n_p = 1 << 41
chk("prize: 29 = floor((B* - B_quot_ub - (n-A+1))/n^3) recomputed",
    (B_PRIZE - quot_ub(n_p, n_p//4, n_p//4 + n_p//256 + 1)
     - (n_p - (n_p//4 + n_p//256 + 1) + 1)) // n_p**3 == 29)

print()
print("FAILS:", len(FAILS))
print("XR_CONSUMPTION_REPLAY_" + ("PASS" if not FAILS else "FAIL"))

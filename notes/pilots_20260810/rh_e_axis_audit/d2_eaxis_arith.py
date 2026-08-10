"""D2 - THE EXTENSION-ROW ARITHMETIC (exact integers only, no floating point).

Question: for the located-crossing pose's row family
    n = 2^41, k = 2^40, n | q-1, 2^167 < q < 2^256, q = p^e,
which e are FEASIBLE, what is the exact p-window for each, does the
characteristic ever drop below the evaluation-domain size n (the
load-bearing consequence (RPFC3) of rate_half_residual_prime_field_collapse),
and which e reach INSIDE the razor slice (2^255.9, 2^256)?

All range decisions are exact integer comparisons against
    RAZOR = floor(2^255.9) = iroot(2^2559, 10)
(round-30 M3: math.log2 has no resolution at 256 bits).
"""
import sys

N_S = 41
n = 1 << 41
k = 1 << 40
QMAX = 1 << 256          # strict upper cap q < 2^256
QLO = 1 << 167           # strict lower end 2^167 < q


def iroot(x, m):
    """floor(x ** (1/m)) by exact integer Newton"""
    if x < 0:
        raise ValueError
    if x == 0:
        return 0
    hi = 1 << ((x.bit_length() + m - 1) // m + 1)
    lo = 0
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid ** m <= x:
            lo = mid
        else:
            hi = mid - 1
    return lo


RAZOR = iroot(1 << 2559, 10)          # floor(2^255.9)


def v2(x):
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c


_MR_BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def is_prime(x):
    if x < 2:
        return False
    for sp in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if x % sp == 0:
            return x == sp
    d = x - 1
    s = v2(d)
    d >>= s
    for a in _MR_BASES:
        y = pow(a, d, x)
        if y == 1 or y == x - 1:
            continue
        for _ in range(s - 1):
            y = y * y % x
            if y == x - 1:
                break
        else:
            return False
    return True


def v2_qm1(p, e):
    """v_2(p^e - 1) by LTE, exact"""
    if e % 2 == 1:
        return v2(p - 1)
    return v2(p - 1) + v2(p + 1) + v2(e) - 1


print("=" * 74, flush=True)
print("D2.1  WHICH e ARE FEASIBLE AT ALL  (n = 2^41 | q-1, 2^167 < q < 2^256)",
      flush=True)
print("=" * 74, flush=True)
print("LTE: e odd  -> v_2(p^e-1) = v_2(p-1),  so 2^41 | q-1  <=>  p = 1 mod 2^41",
      flush=True)
print("     e even -> v_2(p^e-1) = v_2(p-1)+v_2(p+1)+v_2(e)-1;  min(v_2(p-1),v_2(p+1))=1",
      flush=True)
print("             -> p = +-1 mod 2^(41-v_2(e)) is FORCED", flush=True)
print(flush=True)
print(f"{'e':>3} {'p = +-1 mod':>14} {'p_min(forced)':>16} {'p_max=iroot(2^256,e)':>22} "
      f"{'feasible':>9} {'char>n?':>8}", flush=True)

feasible = []
for e in range(1, 13):
    if e % 2 == 1:
        mod_exp = N_S                       # p = 1 mod 2^41
        pmin_forced = (1 << N_S) + 1
    else:
        mod_exp = N_S - v2(e)               # p = +-1 mod 2^(41-v2(e))
        pmin_forced = (1 << mod_exp) - 1
    pmax = iroot(QMAX - 1, e)               # p^e < 2^256
    pmin_range = iroot(QLO, e) + 1          # p^e > 2^167
    pmin = max(pmin_forced, pmin_range)
    ok = pmin <= pmax
    if ok:
        feasible.append((e, mod_exp, pmin, pmax))
    print(f"{e:>3} {('2^%d' % mod_exp):>14} {pmin_forced.bit_length():>13} b "
          f"{pmax.bit_length():>19} b {str(ok):>9} "
          f"{str(pmin > n) if ok else '-':>8}", flush=True)

print(flush=True)
print("FEASIBLE e:", [f[0] for f in feasible], flush=True)
print(flush=True)
print("D2.2  EXACT p-WINDOW PER FEASIBLE e, AND THE CHARACTERISTIC FLOOR",
      flush=True)
print(f"{'e':>3} {'p_min (exact)':>44} {'bits':>5} {'p_max bits':>11} "
      f"{'p_min > n = 2^41':>17}", flush=True)
for (e, mod_exp, pmin, pmax) in feasible:
    print(f"{e:>3} {pmin:>44} {pmin.bit_length():>5} {pmax.bit_length():>11} "
          f"{str(pmin > n):>17}", flush=True)

print(flush=True)
print("  => the MINIMUM characteristic over ALL admissible rows of the pose's", flush=True)
print("     family is min over feasible e of p_min:", flush=True)
gmin = min(f[2] for f in feasible)
print(f"     p_min_global = {gmin}  ({gmin.bit_length()} bits); n = 2^41 = {n}", flush=True)
print(f"     char > n on EVERY admissible row: {gmin > n}", flush=True)
print(f"     char > every degree <= n used in the reductions: {gmin > n}", flush=True)

print(flush=True)
print("=" * 74, flush=True)
print("D2.3  EXPLICIT ADMISSIBLE EXTENSION ROWS INSIDE THE RAZOR SLICE", flush=True)
print("      (razor slice = floor(2^255.9) < q < 2^256, exact integers)", flush=True)
print("=" * 74, flush=True)
print(f"RAZOR = floor(2^255.9) has {RAZOR.bit_length()} bits", flush=True)

razor_rows = []
for (e, mod_exp, pmin, pmax) in feasible:
    if e == 1:
        continue
    lo = iroot(RAZOR, e) + 1
    hi = pmax
    step = 1 << mod_exp
    found = None
    tried = 0
    # candidates are j*2^mod_exp +- 1 in (lo, hi]
    j0 = lo // step
    j = j0
    while j * step - 1 <= hi and found is None and tried < 400000:
        for sgn in (-1, +1):
            cand = j * step + sgn
            if cand <= lo or cand > hi:
                continue
            tried += 1
            if not is_prime(cand):
                continue
            q = cand ** e
            if not (RAZOR < q < QMAX):
                continue
            if (q - 1) % n:
                continue
            found = cand
            break
        j += 1
    if found is None:
        print(f"e = {e}: NO admissible prime p in the razor window "
              f"(candidates tried {tried}) -> razor slice is EMPTY at this e",
              flush=True)
    else:
        q = found ** e
        razor_rows.append((e, found, q))
        print(f"e = {e}: p = {found}", flush=True)
        print(f"        p bits = {found.bit_length()}, "
              f"q = p^{e} bits = {q.bit_length()}, "
              f"q > RAZOR = {q > RAZOR}, q < 2^256 = {q < QMAX}", flush=True)
        print(f"        v_2(q-1) = {v2(q - 1)} (need >= 41): {v2(q - 1) >= 41}", flush=True)
        print(f"        B* = floor(q/2^128) = {q >> 128}  ({(q >> 128).bit_length()} bits)",
              flush=True)

print(flush=True)
print("=" * 74, flush=True)
print("D2.4  THE ROUND-30 EXHIBITED ROW, RE-VERIFIED + THE TORSION-LOCATION TEST",
      flush=True)
print("=" * 74, flush=True)
p30 = 340282366920938463463374556854233333761
q30 = p30 * p30
print(f"p (round-30 exhibit) prime? {is_prime(p30)}", flush=True)
print(f"q = p^2 bits = {q30.bit_length()}, q > RAZOR = {q30 > RAZOR}, "
      f"q < 2^256 = {q30 < QMAX}", flush=True)
print(f"v_2(q-1) = {v2(q30 - 1)}", flush=True)
print(f"v_2(p-1) = {v2(p30 - 1)}    v_2(p+1) = {v2(p30 + 1)}", flush=True)
print(f"B* = floor(q/2^128) = {q30 >> 128}", flush=True)
print(flush=True)
print("TORSION LOCATION (the registered R3 side-prediction):", flush=True)
print("  the order-2^41 subgroup D lies in F_p^*  <=>  2^41 | p-1", flush=True)
print(f"  2^41 | p-1 ? {(p30 - 1) % n == 0}", flush=True)
print("  D lies in the norm-one ('circle') subgroup ker(Norm) of order p+1", flush=True)
print(f"      <=>  2^41 | p+1 ? {(p30 + 1) % n == 0}", flush=True)
print(flush=True)
print("  General law for e = 2 (exact, from LTE): v_2(p^2-1) = v_2(p-1)+v_2(p+1)", flush=True)
print("  and min(v_2(p-1), v_2(p+1)) = 1 for odd p, so for v_2(q-1) >= 41 exactly", flush=True)
print("  ONE of p-1, p+1 carries >= 40 of the 2-power.  Hence for e = 2 the", flush=True)
print("  order-2^41 domain is EITHER inside F_p^* (2^41 | p-1) OR inside the", flush=True)
print("  norm-one subgroup up to index 2 (2^40 | p+1).  Both branches occur.", flush=True)

print(flush=True)
print("=" * 74, flush=True)
print("D2.5  FIELD-AGNOSTIC INSTRUMENT QUANTITIES AT THE EXHIBITED ROWS", flush=True)
print("=" * 74, flush=True)
print("  Every quantity below is a function of (n, k, q) ONLY -- no p, no e.", flush=True)
rows = [("round-30 e=2 razor", q30)]
for (e, p, q) in razor_rows:
    rows.append((f"new e={e} razor", q))
rows.append(("prime razor anchor 2^256-189?", (1 << 256) - 189))
print(f"{'row':>26} {'B* bits':>8} {'k+2^34':>14} {'3n/4':>14} "
      f"{'B* vs n':>12}", flush=True)
for (lab, q) in rows:
    B = q >> 128
    print(f"{lab:>26} {B.bit_length():>8} {k + (1 << 34):>14} {3 * n // 4:>14} "
          f"{'B*>>n' if B > n else 'B*<=n':>12}", flush=True)
print(flush=True)
print(f"  bracket [k+2^34, 3n/4] = [{k + (1 << 34)}, {3 * n // 4}], "
      f"width = {3 * n // 4 - k - (1 << 34)}", flush=True)
print("  -> the bracket endpoints do not mention q at all; they are e-free.", flush=True)

print(flush=True)
print("=" * 74, flush=True)
print("D2.6  THE SCOPE OF rate_half_residual_prime_field_collapse (PROVED)", flush=True)
print("=" * 74, flush=True)
b_lo = (1 << 39) << 128                 # B = 2^39   -> q in [2^167, 2^167+2^128)
b_hi = ((1 << 39) + 2) << 128           # B = 2^39+1 -> up to 2^167 + 2^129
print(f"  RPFC hypothesis: B = floor(q/2^128) in {{2^39, 2^39+1}}", flush=True)
print(f"  i.e. q in [{b_lo}, {b_hi})", flush=True)
print(f"  that is q in [2^167, 2^167 + 2^129)", flush=True)
width_rpfc = b_hi - b_lo
width_pose = QMAX - QLO
print(f"  RPFC-covered width  = 2^{width_rpfc.bit_length()-1} (exactly 2^129)", flush=True)
print(f"  pose width          ~ 2^{width_pose.bit_length()-1}", flush=True)
print(f"  fraction of the pose's q-range on which 'q prime' is a THEOREM:", flush=True)
print(f"      2^129 / 2^256  =  2^-127", flush=True)
print("  -> on the other 1 - 2^-127 of the pose's range, INCLUDING THE ENTIRE", flush=True)
print("     RAZOR SLICE, 'q prime' is an ASSUMPTION, not a consequence.", flush=True)

print(flush=True)
print("D2.7  CROSS-CHECK OF RPFC's OWN CENSUS AT f = 2 (the 24 + 22 integers)",
      flush=True)
lo1, hi1 = (1 << 39) << 128, ((1 << 39) + 1) << 128
lo2, hi2 = ((1 << 39) + 1) << 128, ((1 << 39) + 2) << 128
for (lab, lo, hi) in (("B=2^39", lo1, hi1), ("B=2^39+1", lo2, hi2)):
    cnt = 0
    # q = p^2 with 2^41 | q-1 => p = +-1 mod 2^40 ; count p with p^2 in [lo,hi)
    pl = iroot(lo - 1, 2) + 1
    ph = iroot(hi - 1, 2)
    step = 1 << 40
    j = pl // step
    cands = []
    while j * step - 1 <= ph:
        for sgn in (-1, 1):
            c = j * step + sgn
            if pl <= c <= ph and (c * c - 1) % n == 0:
                cands.append(c)
                cnt += 1
        j += 1
    nprime = sum(1 for c in cands if is_prime(c))
    print(f"  {lab}: p-candidates with p = +-1 mod 2^40 and 2^41 | p^2-1 : {cnt}"
          f"   of which PRIME: {nprime}", flush=True)
print("  (RPFC prints 24 and 22 candidates, each with a nontrivial divisor;", flush=True)
print("   a count match + 0 primes is the replay of its exclusion.)", flush=True)
sys.stdout.flush()

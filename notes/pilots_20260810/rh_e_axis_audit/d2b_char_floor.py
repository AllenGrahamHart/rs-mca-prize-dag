"""D2b - the two arithmetic facts the widen/child decision turns on.

(1) Is there ANY admissible row (n = 2^41 | q-1, 2^167 < q = p^e < 2^256)
    whose characteristic p is <= n = 2^41?   ((RPFC3)'s load-bearing
    consequence is "the characteristic exceeds the evaluation-domain size
    and every degree in the Hankel and pair-Lagrange reductions".)
(2) The contrapositive of rate_half_residual_prime_field_collapse (PROVED):
    every admissible EXTENSION row has B* = floor(q/2^128) outside the two
    residual budgets {2^39, 2^39+1}.
Plus the subfield lattice per feasible e, and one explicit e = 6 row.
"""
import sys

n = 1 << 41
QMAX = 1 << 256
QLO = 1 << 167


def iroot(x, m):
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


def v2(x):
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c


def is_prime(x):
    if x < 2:
        return False
    for sp in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if x % sp == 0:
            return x == sp
    d, s = x - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        y = pow(a, d, x)
        if y in (1, x - 1):
            continue
        for _ in range(s - 1):
            y = y * y % x
            if y == x - 1:
                break
        else:
            return False
    return True


print("=" * 78, flush=True)
print("D2b.1  CAN THE CHARACTERISTIC EVER DROP TO OR BELOW n = 2^41 ?", flush=True)
print("=" * 78, flush=True)
print("Per-e congruence floor (LTE) and the floor forced by q > 2^167:", flush=True)
print(f"{'e':>3} {'congruence floor on p':>24} {'q>2^167 floor on p':>21} "
      f"{'binding floor':>15} {'<= n ?':>7}", flush=True)
risky = []
for e in range(1, 7):
    if e % 2:
        cong = (1 << 41) + 1
        cong_txt = "p = 1 mod 2^41"
    else:
        j = v2(e)
        cong = (1 << (41 - j)) - 1
        cong_txt = f"p = +-1 mod 2^{41 - j}"
    rng = iroot(QLO, e) + 1
    binding = max(cong, rng)
    le = binding <= n
    if le:
        risky.append((e, cong, rng))
    print(f"{e:>3} {cong_txt:>24} {('~2^%.2f' % (rng.bit_length())):>21} "
          f"{binding.bit_length():>13} b {str(le):>7}", flush=True)

print(flush=True)
print("Only these e can even in principle have char <= n; enumerate them EXACTLY:",
      flush=True)
for (e, cong, rng) in risky:
    j = v2(e)
    step = 1 << (41 - j)
    lo = max(cong, rng)
    print(f"  e = {e}: candidates p = j*2^{41-j} +- 1 with p <= n = 2^41 "
          f"and p^{e} > 2^167", flush=True)
    any_prime = False
    jj = 1
    while jj * step - 1 <= n:
        for sgn in (-1, 1):
            c = jj * step + sgn
            if c < 3 or c > n:
                continue
            if c ** e <= QLO or c ** e >= QMAX:
                continue
            pr = is_prime(c)
            any_prime = any_prime or pr
            print(f"      p = {c:<16} prime? {pr}", flush=True)
        jj += 1
    print(f"      -> any admissible row with char <= n at e = {e}: {any_prime}",
          flush=True)

print(flush=True)
print("VERDICT: an admissible row with characteristic <= the evaluation-domain",
      flush=True)
print("size n = 2^41 exists iff one of the integers printed above is prime.",
      flush=True)

print(flush=True)
print("=" * 78, flush=True)
print("D2b.2  q IS ALWAYS ODD, AND THE SUBFIELD LATTICE PER e", flush=True)
print("=" * 78, flush=True)
print("2^41 | q-1 forces q odd, so every 'odd characteristic' hypothesis in the",
      flush=True)
print("far-CA subtree is satisfied on every admissible row, prime or not.",
      flush=True)
print(flush=True)
print(f"{'e':>3} {'proper subfields':>20} {'largest proper subfield size':>30}",
      flush=True)
for e in (1, 2, 3, 4, 5, 6):
    divs = [d for d in range(1, e) if e % d == 0]
    if not divs:
        print(f"{e:>3} {'none (prime field)':>20} {'-':>30}", flush=True)
    else:
        dmax = max(divs)
        print(f"{e:>3} {str(['F_p^%d' % d for d in divs]):>20} "
              f"{('p^%d = q^(%d/%d)' % (dmax, dmax, e)):>30}", flush=True)

print(flush=True)
print("In the RAZOR SLICE the largest proper subfield of an admissible row is:",
      flush=True)
RAZOR = iroot(1 << 2559, 10)
for e in (2, 3, 4, 5):
    plo = iroot(RAZOR, e) + 1
    dmax = max(d for d in range(1, e) if e % d == 0)
    print(f"  e = {e}: p ~ 2^{plo.bit_length()}, largest proper subfield "
          f"F_(p^{dmax}) has ~2^{(plo ** dmax).bit_length()} elements "
          f"(target scale 2^128)", flush=True)

print(flush=True)
print("=" * 78, flush=True)
print("D2b.3  THE RPFC CONTRAPOSITIVE (this is the load-bearing one)", flush=True)
print("=" * 78, flush=True)
print("rate_half_residual_prime_field_collapse (PROVED) statement.md:11-20:", flush=True)
print("   N=2^41, q=p^f, B=floor(q/2^128) in {2^39, 2^39+1}, N | q-1  ==>  f=1.",
      flush=True)
print(flush=True)
print("CONTRAPOSITIVE: on the admissible family, f >= 2  ==>  B not in", flush=True)
print("{2^39, 2^39+1}, i.e. every admissible EXTENSION row has", flush=True)
print("   q  outside  [2^167, 2^167 + 2^129).", flush=True)
lo = (1 << 39) << 128
hi = ((1 << 39) + 2) << 128
print(f"   excluded interval = [2^167, 2^167 + 2^129) "
      f"= [{lo}, {hi})", flush=True)
print(flush=True)
print("Consequence for the audit: the ONLY residual-budget territory in the", flush=True)
print("pose's range -- the two open budgets {2^39, 2^39+1}, which is where the", flush=True)
print("A=1 / A=3 exceptional core and its prime-field instruments live -- is", flush=True)
print("EMPTY of extension rows, by a PROVED node.  Widening the pose therefore", flush=True)
print("cannot import extension rows into the prime-field-dependent machinery.",
      flush=True)

print(flush=True)
print("Direct check: for each feasible e >= 2, is there any p with", flush=True)
print("2^167 <= p^e < 2^167 + 2^129 and 2^41 | p^e - 1 ?", flush=True)
for e in (2, 3, 4, 5, 6):
    j = v2(e) if e % 2 == 0 else None
    step = (1 << (41 - j)) if j is not None else (1 << 41)
    plo = iroot(lo - 1, e) + 1
    phi = iroot(hi - 1, e)
    cnt = 0
    prm = 0
    jj = plo // step
    while jj * step - 1 <= phi:
        for sgn in ((-1, 1) if e % 2 == 0 else (1,)):
            c = jj * step + sgn
            if c < plo or c > phi:
                continue
            if (c ** e - 1) % n:
                continue
            cnt += 1
            if is_prime(c):
                prm += 1
        jj += 1
    print(f"  e = {e}: {cnt} integer candidates in the window, of which PRIME: {prm}",
          flush=True)

print(flush=True)
print("=" * 78, flush=True)
print("D2b.4  AN EXPLICIT e = 6 ADMISSIBLE ROW (the largest feasible e)", flush=True)
print("=" * 78, flush=True)
lo6 = max((1 << 40) - 1, iroot(QLO, 6) + 1)
hi6 = iroot(QMAX - 1, 6)
step = 1 << 40
jj = max(1, lo6 // step)
found = 0
while jj * step - 1 <= hi6 and found < 3:
    for sgn in (-1, 1):
        c = jj * step + sgn
        if c < lo6 or c > hi6:
            continue
        if not is_prime(c):
            continue
        q = c ** 6
        if not (QLO < q < QMAX) or (q - 1) % n:
            continue
        print(f"  p = {c}  ({c.bit_length()} bits, p > n = 2^41: {c > n})", flush=True)
        print(f"  q = p^6 has {q.bit_length()} bits, v_2(q-1) = {v2(q - 1)}, "
              f"B* = floor(q/2^128) has {(q >> 128).bit_length()} bits", flush=True)
        found += 1
    jj += 1
if not found:
    print("  none found in the scanned prefix of the window", flush=True)
sys.stdout.flush()

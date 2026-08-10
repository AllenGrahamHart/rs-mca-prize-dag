"""D3b - the DECISIVE cells the first ladder ran out of wall before reaching.

The round-30 exhibited razor row has v_2(p-1) = 41 (measured in D2), so its
evaluation domain D lies INSIDE THE PRIME SUBFIELD F_p.  The first ladder
found F_LMAX(8,4,5) = 8 (vs the prime-field constant 7) at exactly the two
fields q = 9 and q = 81, and in BOTH of those D = F_9^* is the FULL
multiplicative group of a subfield.  Two hypotheses are still open:

  H-SUBFIELD : the excess comes from D lying in a PROPER subfield
               (the branch the exhibited razor row is in)  -> pro-CHILD
  H-FULLGROUP: the excess comes from D being the WHOLE multiplicative
               group of a field (impossible at n = 2^41 unless 2^41+1 is
               a prime power)                               -> pro-WIDEN

These separate at q = 289 = 17^2 (D inside F_17, index 2 in F_17^*, so a
proper subfield but NOT the whole group) and q = 625 = 5^4 (D inside F_25,
index 3).  q = 361 = 19^2 is the matched control (D in no proper subfield).
"""
import sys
from math import isqrt

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import ffq
from d3_subfield_supply import flmax, domain_subfield, key_flags


def prime_power(x):
    return ffq.factor_pe(x)


print("=" * 92, flush=True)
print("D3b.0  IS THE FULL-GROUP DEGENERACY REACHABLE AT THE OFFICIAL ROW?", flush=True)
print("=" * 92, flush=True)
N = (1 << 41) + 1
print(f"  D = F_(q')^* requires q' = n+1 = 2^41+1 = {N} to be a prime power.",
      flush=True)
pp = prime_power(N)
print(f"  2^41+1 is a prime power? {pp is not None}   (factor_pe -> {pp})", flush=True)
d = 2
fac = []
m = N
while d * d <= m and len(fac) < 6:
    while m % d == 0:
        fac.append(d)
        m //= d
    d += 1
if m > 1:
    fac.append(m)
print(f"  2^41+1 = {' * '.join(str(f) for f in fac)}", flush=True)
print("  => at n = 2^41 the evaluation domain can NEVER be the whole", flush=True)
print("     multiplicative group of any field.", flush=True)

n_s, K = 8, 4
CELLS = [289, 361, 625]
print(flush=True)
print("=" * 92, flush=True)
print("D3b.1  THE DISCRIMINATING CELLS", flush=True)
print("=" * 92, flush=True)
print(f"{'q':>5} {'p':>4} {'e':>2} {'D<=F_p^d':>9} {'D = whole F_p^d^*?':>19} "
      f"{'B_s':>5} {'FL(5)':>6} {'FL(6)':>6} {'FL(7)':>6} {'sigma_L':>8} "
      f"{'#argmax':>8} {'argmax flags':>26}", flush=True)
for q in CELLS:
    if (q - 1) % n_s:
        print(f"{q:>5}  skipped ({n_s} does not divide q-1)", flush=True)
        continue
    F = ffq.GF(q)
    D = F.subgroup(n_s)
    dsub = domain_subfield(F, D)
    whole = (F.p ** dsub - 1 == n_s)
    vals, nargs, flags = {}, {}, {}
    for a in (5, 6, 7):
        m, hist = flmax(F, n_s, K, a, want_keys=True)
        vals[a] = m
        arg = [kk for kk, v in hist.items() if v == m]
        nargs[a] = len(arg)
        flags[a] = key_flags(F, list(arg[0])) if arg else ("-", "-")
    vals[8] = 1
    Bs = isqrt(q)
    sig = 0
    for a in range(K + 1, n_s + 1):
        if vals[a] > Bs:
            sig = a - K
    print(f"{q:>5} {F.p:>4} {F.e:>2} {dsub:>9} {str(whole):>19} {Bs:>5} "
          f"{vals[5]:>6} {vals[6]:>6} {vals[7]:>6} {sig:>8} {nargs[5]:>8} "
          f"{(flags[5][0] + '/' + flags[5][1]):>26}", flush=True)
    sys.stdout.flush()

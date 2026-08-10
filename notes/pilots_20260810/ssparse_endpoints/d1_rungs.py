"""D1 / P1-P2-P5: exact rung lattice of the quotient-window floor family.

Family (rotated-prefix, PROVED node rate_half_cyclic_rotated_prefix_floor):
  c | n/2, N = n/c, 1 <= d <= N/2-1, m = N/2+d, s = c-1,
  list count L(N,d) >= C(N-1,m) / (N q^(d-1)),  reach sigma = (d+1)c - 1.
Family (fixed-tail, background rate_half_fixed_tail_prefix_floor):
  same c,N; d >= 0, m = k/c + d = N/2 + d, L >= C(N-1,m)/q^d,
  reach sigma = d*c + (c-1) = (d+1)c - 1  (SAME reach formula).

MCA floor (simple-pole conversion, PROVED): bad slopes
  M >= L(q-n)/(q-n+kL),  unsafe iff M > B* = floor(q/2^128), and
  1/E = N q^d / C(N-1,m) + k q/(q-n) < 2^128 suffices for every q < 2^256.

Everything below is exact integer arithmetic at the artificial endpoint
q = Q = 2^256 (the condition only strengthens as q decreases -- proof.md).
"""
import math

n = 1 << 41
k = 1 << 40
Q = 1 << 256
BUD = 1 << 128


def log2_int(x):
    """exact-ish log2 of a positive big int (float precision on the mantissa)"""
    if x <= 0:
        return float('-inf')
    b = x.bit_length()
    if b <= 60:
        return math.log2(x)
    return (b - 60) + math.log2(x >> (b - 60))


def rot_margin(N, d):
    """log2( 2^128 * C(N-1,m) ) - log2( N * Q^d ), rotated family, d>=1."""
    m = N // 2 + d
    if not (1 <= d <= N // 2 - 1):
        return None
    if m > N - 1:
        return None
    C = math.comb(N - 1, m)
    if C == 0:
        return float('-inf')
    return (128 + log2_int(C)) - (log2_int(N) + 256 * d)


def tail_margin(N, d):
    """SELF-CORRECTION 1 (2026-08-10): the admissibility test is
    q/L < 2^128 with L = C(N-1,m)/q^d, i.e. q^(d+1)/C < 2^128 -- one
    more factor of q than my first draft, which wrongly declared an
    L=1 rung admissible.  Anchor: N=128,d=0 must give -4.8286 bits
    (the banked deficit vs C(127,64)=2^123.1714)."""
    m = N // 2 + d
    if d < 0 or m > N - 1:
        return None
    C = math.comb(N - 1, m)
    return (128 + log2_int(C)) - (256 * (d + 1))


def reach(N, d):
    c = n // N
    return (d + 1) * c - 1


print("=== D1 rung lattice: exhaustive scan, N = 2^i (2..256), all legal d ===")
print(f"{'N':>6} {'d':>5} {'fam':>4} {'reach':>14} {'log2reach':>10} {'margin_bits':>13} {'adm':>4}")
best = []
rows = []
for i in range(1, 9):                       # N = 2 .. 256
    N = 1 << i
    c = n // N
    if c > k:                               # need c | n/2
        continue
    # fixed-tail d = 0 .. and rotated d = 1 ..
    for d in range(0, N // 2):
        mt = tail_margin(N, d)
        if mt is not None:
            rows.append((N, d, 'tail', reach(N, d), mt))
        if d >= 1:
            mr = rot_margin(N, d)
            if mr is not None:
                rows.append((N, d, 'rot', reach(N, d), mr))
for (N, d, fam, R, mar) in sorted(rows, key=lambda t: (-t[3], t[0], t[1])):
    adm = 'YES' if mar > 0 else 'no'
    print(f"{N:>6} {d:>5} {fam:>4} {R:>14} {log2_int(R):>10.4f} {mar:>13.4f} {adm:>4}")
    if mar > 0:
        best.append((R, N, d, fam, mar))

print()
if best:
    best.sort(reverse=True)
    R, N, d, fam, mar = best[0]
    print(f"MAX ADMISSIBLE REACH over N<=256: sigma = {R} = 2^{log2_int(R):.6f}")
    print(f"   attained at (N,d,family) = ({N},{d},{fam}), margin {mar:.4f} bits")
    print(f"   2^34-1 = {(1<<34)-1};  match = {R == (1<<34)-1}")

print()
print("=== first reach-improving rung (reach 2^35-1) ===")
for (N, d, fam) in [(128, 1, 'rot'), (128, 1, 'tail'), (64, 0, 'tail')]:
    mar = rot_margin(N, d) if fam == 'rot' else tail_margin(N, d)
    print(f"  N={N:<5} d={d} {fam:<5} reach={reach(N,d):>13} margin={mar:>10.4f} bits")

print()
print("=== pruning theorem for N >= 512 (no binomials needed) ===")
print("admissibility needs 256d < N-1+128-log2 N  =>  d <= floor((N+127)/256)")
print("so reach <= (floor((N+127)/256)+1)*n/N - 1")
worst = 0.0
for i in range(9, 42):
    N = 1 << i
    if n // N < 1:
        break
    dmax = (N + 127) // 256
    Rmax = (dmax + 1) * (n // N) - 1
    worst = max(worst, Rmax)
    if i <= 14 or i in (16, 20, 24, 30, 41):
        print(f"  N=2^{i:<2} dmax={dmax:<7} reach_ceiling={Rmax:>13} "
              f"(2^{log2_int(max(Rmax,1)):.4f})  < 2^34-1: {Rmax < (1<<34)-1}")
print(f"  SUP over all N>=512 of the reach ceiling = {int(worst)} "
      f"= 2^{log2_int(int(worst)):.4f}  < 2^34-1 = {(1<<34)-1}: {worst < (1<<34)-1}")

print()
print("=== P2: non-2-power scale c ===")
divs = set()
x = k
j = 0
while (1 << j) <= k:
    divs.add(1 << j)
    j += 1
print(f"  n/2 = 2^40; every divisor of 2^40 is a 2-power -> |non-2-power c| = "
      f"{len([d for d in divs if (d & (d-1))])}")
print("  S-SCALE surface is EMPTY at the razor row (not merely unpromising).")

print()
print("=== P5: fixed-tail vs rotated denominator ratio ===")
print(f"  q^d / (N q^(d-1)) = q/N = 2^256/256 = 2^248 at N=256 "
      f"-> rotated dominates fixed-tail by 248 bits at every d>=1")

print()
print("=== P0: payload of the PROVED floor at reach 2^34-1 (far-CA pair) ===")
N, d = 256, 1
L = -(-math.comb(N - 1, N // 2 + d) // N)           # ceil
print(f"  L_cyc = ceil(C(255,129)/256) = 2^{log2_int(L):.4f}")
for qq, tag in [(Q, "q=2^256 (cap)"), (int(2 ** 255.9), "q~2^255.9 (razor low)")]:
    M = L * (qq - n) // (qq - n + k * L)
    Bstar = qq >> 128
    print(f"  {tag:<22} M >= 2^{log2_int(M):.4f}   B* = 2^{log2_int(Bstar):.4f}   "
          f"M/B* = 2^{log2_int(M)-log2_int(Bstar):.4f}")
print("  (M is a count of CA-bad slopes of a COLUMN-FAR pair -> lands in B_ca^far)")

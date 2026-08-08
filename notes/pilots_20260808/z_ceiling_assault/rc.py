#!/usr/bin/env python3
"""THEOREM RC (resultant ceiling) -- proof-checks and the exact gate.
tools/ramguard local -- python3 ...

THEOREM RC.  Let n = 2N be a power of two, p == 1 mod n prime, th of exact
order n in F_p, and eps in {0,+-1}^N nonzero of weight U, with
f(x) = sum_j eps_j x^j (so deg f < N = deg Phi_n = phi(n)).  If f(th) = 0 in
F_p then

    p | Res(Phi_n, f)   and   1 <= |Res(Phi_n, f)| <= U^{N/2},

hence  p <= U^{N/2} <= N^{N/2}.  Consequences:
  (i)   UMIN(N,p) >= p^{2/N}  at every cell with a nonempty ternary kernel;
  (ii)  TMASS(N,p) = 1 EXACTLY for every admissible p > N^{N/2};
  (iii) sum over ALL admissible p of (TMASS(p) - 1) <= (N/2) log2(N) (2^N - 1),
        so on each N-line the excess mass is summably finite and sup_p CRATIO
        is a MAXIMUM over a finite set of primes.

PROOF.  Res(Phi_n,f) = prod over the phi(n) = N primitive n-th roots z of
f(z); it is a nonzero rational integer because Phi_n is irreducible over Q and
0 <= deg f < deg Phi_n.  Parseval over ALL n = 2N roots of unity gives
sum_{z^n=1}|f(z)|^2 = n*U.  Over the N-th roots of unity (exactly the
NON-primitive n-th roots, since n = 2N) it gives sum_{z^N=1}|f(z)|^2 = N*U,
with no folding because deg f < N.  Subtracting, the N primitive roots carry
sum |f(z)|^2 = 2NU - NU = NU.  AM-GM on those N non-negative terms gives
|Res|^2 = prod|f(z)|^2 <= (NU/N)^N = U^N, i.e. |Res| <= U^{N/2}.  Since
f(th) = 0 mod p makes Phi_n and f share a root mod p and Phi_n is monic,
p | Res(Phi_n, f).  QED.  (ii): U <= N always.  (iii): a fixed f lies in the
kernel for at most log2|Res| <= (N/2)log2 U primes; sum 2^{-U} C(N,U) 2^U
over U = 2^N - 1.
"""
import itertools, math, os, random, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zcore import *   # noqa


def _bareiss(M, d):
    sign = 1
    prev = 1
    for k in range(d - 1):
        if M[k][k] == 0:
            for r in range(k + 1, d):
                if M[r][k]:
                    M[k], M[r] = M[r], M[k]
                    sign = -sign
                    break
            else:
                return 0
        mk = M[k][k]
        for i in range(k + 1, d):
            mik = M[i][k]
            Mi = M[i]
            Mkr = M[k]
            for j in range(k + 1, d):
                Mi[j] = (Mi[j] * mk - mik * Mkr[j]) // prev
        prev = mk
    return sign * M[d - 1][d - 1]


def res_negacyclic(f, N):
    """Res(x^N + 1, f), deg f < N: det of multiplication-by-f on Z[x]/(x^N+1)."""
    M = [[(f[i - j] if i >= j else -f[i - j + N]) for j in range(N)] for i in range(N)]
    return _bareiss(M, N)


def res_general(phi, f):
    """Res(Phi, f) = det of mult-by-f on Z[x]/(Phi), Phi monic, deg f < deg Phi."""
    d = len(phi) - 1
    cols = []
    for j in range(d):
        v = ([0] * j) + list(f) + [0] * d
        for t in range(len(v) - 1, d - 1, -1):
            c = v[t]
            if c:
                for s in range(d + 1):
                    v[t - d + s] -= c * phi[s]
        cols.append(v[:d])
    M = [[cols[j][i] for j in range(d)] for i in range(d)]
    return _bareiss(M, d)


print("=" * 104)
print("RC-A -- |Res(Phi_{2N}, f)| <= U^{N/2} and Res != 0, EXHAUSTIVE over ternary f (N=4,8)")
print("=" * 104)
print("%4s %8s | %12s %14s %14s %10s" % ("N", "#f", "max|Res|", "N^{N/2}", "worst ratio", "Res=0 seen"))
for N in [4, 8]:
    mr = 0
    mx = 0.0
    zero = False
    cnt = 0
    for f in itertools.product((0, 1, -1), repeat=N):
        if not any(f):
            continue
        cnt += 1
        U = sum(1 for x in f if x)
        r = abs(res_negacyclic(list(f), N))
        if r == 0:
            zero = True
        mr = max(mr, r)
        mx = max(mx, r / U ** (N / 2.0))
    print("%4d %8d | %12d %14.5g %14.6f %10s" % (N, cnt, mr, N ** (N / 2.0), mx, zero))
    check("RC-A |Res| <= U^{N/2}, exhaustive N=%d (%d ternary f)" % (N, cnt), mx <= 1 + 1e-12,
          "worst ratio %.6f" % mx)
    check("RC-A Res != 0 (2-power gate), exhaustive N=%d" % N, not zero)
    check("RC-A max|Res| <= N^{N/2} = %g, N=%d" % (N ** (N / 2.0), N), mr <= N ** (N / 2.0))

random.seed(20260808)
mx16 = 0.0
zero16 = False
t = time.time()
for _ in range(4000):
    f = [random.choice((0, 1, -1)) for _ in range(16)]
    if not any(f):
        continue
    U = sum(1 for x in f if x)
    r = abs(res_negacyclic(f, 16))
    if r == 0:
        zero16 = True
    mx16 = max(mx16, r / U ** 8.0)
check("RC-A |Res| <= U^{N/2}, 4000 random ternary f at N=16", mx16 <= 1 + 1e-12,
      "worst ratio %.6f  [%.1fs]" % (mx16, time.time() - t))
check("RC-A Res != 0, 4000 random ternary f at N=16", not zero16)

print()
print("=" * 104)
print("RC-B -- THE EXACT GATE.  A nonzero ternary f of degree < n/2 with Res(Phi_n,f)=0")
print("        exists iff n is NOT a 2-power (deg Phi_n = phi(n) < n/2).  = banked CZ-M.")
print("=" * 104)
print("%5s %5s %8s %8s | %s" % ("n", "n/2", "phi(n)", "RELDIM", "least weight of a ternary f with Res=0"))
for n in [8, 16, 32, 12, 24, 18, 20, 30, 36]:
    h = n // 2
    ph = cyclotomic(n)
    phn = len(ph) - 1
    best = None
    if h <= 8:
        for f in itertools.product((0, 1, -1), repeat=h):
            if not any(f):
                continue
            if res_general(ph, f) == 0:
                U = sum(1 for x in f if x)
                if best is None or U < best:
                    best = U
    else:
        # search the relation lattice (spanned by x^i Phi_n) for ternary points
        m, c, sh = pfree_mass(n)
        if sh > 0 and c > 1:
            bw = None
            dph = phn
            for co in itertools.product((0, 1, -1), repeat=sh):
                if not any(co):
                    continue
                v = [0] * h
                for s in range(sh):
                    if co[s]:
                        for j in range(dph + 1):
                            v[s + j] += co[s] * ph[j]
                if all(abs(x) <= 1 for x in v):
                    U = sum(1 for x in v if x)
                    if bw is None or U < bw:
                        bw = U
            best = bw
    print("%5d %5d %8d %8d | %s" % (n, h, phn, h - phn,
                                    best if best is not None else "NONE  (gate HOLDS)"))
    if n & (n - 1) == 0:
        check("RC-B gate HOLDS at 2-power n=%d" % n, best is None)
    else:
        check("RC-B gate FAILS at composite n=%d" % n, best is not None, "least weight %s" % best)

print()
print("=" * 104)
print("RC-C -- CONSEQUENCE (ii): TMASS = 1 EXACTLY for every admissible p > N^{N/2}")
print("=" * 104)
print("%4s %12s %9s | %8s %8s %8s | %s" %
      ("N", "N^{N/2}", "PMAX", "#cells", "#p>bound", "#TMASS>1", "verdict"))
for (N, pmax) in [(4, 1 << 16), (8, 1 << 17)]:
    bnd = N ** (N / 2.0)
    tot = above = bad = 0
    lastgt1 = 0
    for p in primes_upto(pmax):
        if p <= 2 * N or (p - 1) % (2 * N):
            continue
        tm = tmass_exact(rows_M4(N, p), p)
        tot += 1
        if tm != 1:
            lastgt1 = p
        if p > bnd:
            above += 1
            if tm != 1:
                bad += 1
    print("%4d %12.6g %9d | %8d %8d %8d | %s   (largest p with TMASS>1: %d)" %
          (N, bnd, pmax, tot, above, bad,
           "RC(ii) HOLDS" if bad == 0 else "RC(ii) VIOLATED", lastgt1))
    check("RC(ii) TMASS = 1 for all admissible p > N^{N/2} at N=%d (%d cells above the bound)"
          % (N, above), bad == 0, "violations: %d" % bad)

print()
print("RC-D -- CONSEQUENCE (i): UMIN >= p^{2/N} at every cell with a nonempty kernel")
bad = seen = 0
worst = None
for (N, pmax) in [(8, 1 << 14), (16, 1 << 15)]:
    for p in primes_upto(pmax):
        if p <= 2 * N or (p - 1) % (2 * N):
            continue
        d = cell(rows_M4(N, p), p, want_AU=True)
        if d["UMIN"] is None:
            continue
        seen += 1
        lb = p ** (2.0 / N)
        sl = d["UMIN"] / lb
        if worst is None or sl < worst[0]:
            worst = (sl, N, p, d["UMIN"], lb)
        if d["UMIN"] < lb - 1e-9:
            bad += 1
check("RC(i) UMIN >= p^{2/N} at every nonempty-kernel cell (%d cells)" % seen, bad == 0,
      "violations: %d ; tightest: N=%d p=%d UMIN=%d vs p^{2/N}=%.4f (slack x%.3f)"
      % (bad, worst[1], worst[2], worst[3], worst[4], worst[0]))

sys.exit(summary())

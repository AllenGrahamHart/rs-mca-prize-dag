#!/usr/bin/env python3
"""D3 -- THE N-LADDER VERDICT.  tools/ramguard local -- python3 ... analyze.py"""
import glob
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

rows = []
for fn in sorted(glob.glob(os.path.join(HERE, "CELLS*.tsv"))):
    for ln in open(fn):
        f = ln.rstrip("\n").split("\t")
        if len(f) < 12 or f[0] == "family":
            continue
        rows.append(dict(fam=f[0], N=int(f[1]), k=int(f[2]), p=int(f[3]),
                         sig=float(f[4]), TNUM=int(f[5]), NKER=int(f[6]),
                         TMASS=float(f[7]), CR=float(f[8]), EX=float(f[9]),
                         ZF=float(f[10]), tag=f[12] if len(f) > 12 else ""))
print("cells loaded: %d" % len(rows))


def band(N, k=None, fam=None):
    return [r for r in rows if r["N"] == N and -2.0 <= r["sig"] <= 2.0
            and (k is None or r["k"] == k) and (fam is None or r["fam"] == fam)]


print()
print("=" * 104)
print("D2 -- THE REACHED GRID  (all cells are sigma in [-2,2], 2-power grid 2N)")
print("=" * 104)
print("%-5s %-3s %-4s %-6s %-7s | %-12s %-10s %-10s %-12s" %
      ("fam", "N", "kap", "cells", "cover", "max CRATIO", "at p", "sigma", "mean CRATIO"))
groups = []
for (fam, N, k) in sorted(set((r["fam"], r["N"], r["k"]) for r in rows)):
    g = [r for r in band(N, k, fam)]
    if not g:
        continue
    b = max(g, key=lambda r: r["CR"])
    cov = {("M4", 8, 1): "EXHAUSTIVE", ("M4", 16, 1): "EXHAUSTIVE",
           ("M2", 32, 4): "EXHAUSTIVE", ("M2", 32, 3): "EXHAUSTIVE",
           ("M2", 32, 2): "sample", ("M4", 32, 1): "sample"}.get((fam, N, k), "?")
    print("%-5s %-3d %-4d %-6d %-7s | %-12.10f %-10d %-10.4f %-12.8f" %
          (fam, N, k, len(g), cov, b["CR"], b["p"], b["sig"],
           sum(r["CR"] for r in g) / len(g)))
    groups.append((fam, N, k, g, b))

print()
print("=" * 104)
print("D3 -- THE N-LADDER, sigma-MATCHED and M-MATCHED (family M4 / I2 RSET, kappa=1)")
print("=" * 104)
L = {}
for N in (8, 16, 32):
    g = band(N, 1, "M4")
    if g:
        L[N] = g
if 32 in L and 16 in L:
    M32 = len(L[32])
    print("N=8  in-band cells %4d (EXHAUSTIVE)   max CRATIO %.10f" %
          (len(L.get(8, [])), max(r["CR"] for r in L[8]) if 8 in L else float("nan")))
    print("N=16 in-band cells %4d (EXHAUSTIVE)   max CRATIO %.10f   at p=%d" %
          (len(L[16]), max(r["CR"] for r in L[16]),
           max(L[16], key=lambda r: r["CR"])["p"]))
    print("N=32 in-band cells %4d (SAMPLE of ~2.1e7 admissible primes)  max CRATIO %.10f  at p=%d"
          % (M32, max(r["CR"] for r in L[32]), max(L[32], key=lambda r: r["CR"])["p"]))
    print()
    print("--- M-MATCHED NULL:  max CRATIO over random %d-subsets of the exhaustive lines ---"
          % M32)
    random.seed(20260809)
    for N in (8, 16):
        if N not in L:
            continue
        pool = [r["CR"] for r in L[N]]
        if len(pool) < M32:
            print("N=%-3d pool %d < M=%d -- whole line is the subset, max %.6f"
                  % (N, len(pool), M32, max(pool)))
            continue
        mm = sorted(max(random.sample(pool, M32)) for _ in range(4000))
        q = lambda f: mm[int(f * (len(mm) - 1))]
        print("N=%-3d MMATCH(%d): min %.6f  p05 %.6f  median %.6f  p95 %.6f  max %.6f"
              % (N, M32, mm[0], q(.05), q(.5), q(.95), mm[-1]))
        m32 = max(r["CR"] for r in L[32])
        below = sum(1 for x in mm if x <= m32) / float(len(mm))
        print("      N=32 measured max %.6f sits at quantile %.4f of this null;"
              " M-matched ratio (MAXCR-1) = %.5f"
              % (m32, below, (m32 - 1) / (q(.5) - 1) if q(.5) > 1 else float("nan")))
    print()
    print("--- registered growth model:  MAXCR-1 = A sqrt2 2^{-sN} g(sig) sqrt(2 ln M) ---")
    for N in sorted(L):
        g = L[N]
        mx = max(r["CR"] for r in g)
        print("N=%-3d M=%-5d  MAXCR-1 = %.6f   log2(MAXCR-1) = %+.4f" %
              (N, len(g), mx - 1, math.log2(mx - 1) if mx > 1 else float("nan")))
    if 8 in L and 16 in L and 32 in L:
        # M-normalise to a common M before fitting the N-exponent
        pts = []
        for N in (8, 16, 32):
            g = L[N]
            mx = max(r["CR"] for r in g) - 1
            if mx <= 0:
                continue
            pts.append((N, math.log2(mx / math.sqrt(2 * math.log(len(g))))))
        if len(pts) >= 2:
            n = len(pts)
            sx = sum(x for x, _ in pts)
            sy = sum(y for _, y in pts)
            sxx = sum(x * x for x, _ in pts)
            sxy = sum(x * y for x, y in pts)
            slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
            print("fitted N-exponent (M-normalised, %d points): %+.5f"
                  " [round-24 fit -0.22532, model -0.20752]" % (n, slope))
            print("VERDICT DIRECTION: %s" %
                  ("DECAY (exponent < 0) -- supports an absolute C" if slope < 0
                   else "GROWTH (exponent >= 0) -- the DEATH direction (P4a)"))
    # extreme-value band extrapolation
    m32 = max(r["CR"] for r in L[32])
    nadm = 0
    lo, hi = 1 << 30, 1 << 34
    nadm = (hi - lo) / (32.0 * math.log(hi))     # primes == 1 mod 64, phi(64)=32
    evx = math.sqrt(math.log(nadm) / math.log(M32))
    print()
    print("band extrapolation: ~%.3g admissible primes in [2^30,2^34];"
          " EVX(%d -> %.3g) = %.4f" % (nadm, M32, nadm, evx))
    print("   extrapolated N=32 band max = 1 + %.4f*%.6f = %.6f"
          % (evx, m32 - 1, 1 + evx * (m32 - 1)))
    print("   (HEURISTIC, registered as such in P-Z4)")

print()
print("=" * 104)
print("CROSS-FAMILY: every N=32 cell computed, worst first")
print("=" * 104)
n32 = [r for r in rows if r["N"] == 32]
n32.sort(key=lambda r: -r["CR"])
print("%-5s %-3s %-13s %-9s %-14s %-11s %-9s %-9s" %
      ("fam", "k", "p", "sigma", "CRATIO", "TMASS", "EXCESS", "NKER"))
for r in n32[:14]:
    print("%-5s %-3d %-13d %+9.5f %-14.10f %-11.7f %-9.4f %-9d" %
          (r["fam"], r["k"], r["p"], r["sig"], r["CR"], r["TMASS"], r["EX"], r["NKER"]))
print("   ... %d N=32 cells total; min CRATIO %.10f" %
      (len(n32), min(r["CR"] for r in n32)))
print()
print("EZ7 (diagnostic) mean TMASS vs 1+H per N=32 group:")
for (fam, N, k, g, b) in groups:
    if N != 32:
        continue
    mt = sum(r["TMASS"] for r in g) / len(g)
    mh = sum(1 + (2.0 ** 32 - 1) / float(r["p"]) ** r["k"] for r in g) / len(g)
    print("   %-4s k=%d  %3d cells  mean TMASS %.6f  mean(1+H) %.6f  ratio %.5f"
          % (fam, k, len(g), mt, mh, mt / mh))
print()
print("P-Z5 check (NKER vs 3^32/p^kappa) on N=32:")
for r in n32[:6] + n32[-3:]:
    print("   %-4s k=%d p=%-13d NKER %-10d  3^32/p^k = %-12.0f  ratio %.4f"
          % (r["fam"], r["k"], r["p"], r["NKER"], 3.0 ** 32 / r["p"] ** r["k"],
             r["NKER"] / (3.0 ** 32 / r["p"] ** r["k"])))


print()
print("=" * 104)
print("D3-SD -- THE LOW-NOISE LADDER: sd(CRATIO) in matched sigma bins")
print("        (registered model R4: SD(CRATIO) = sqrt2 * 2^{-sN} * g(sigma),")
print("         g(sigma) = 2^{sigma/2}/(1+2^sigma).  A 47-cell max is noisy;")
print("         a 47-cell sd is not.)")
print("=" * 104)


def gfun(s):
    return 2.0 ** (s / 2.0) / (1.0 + 2.0 ** s)


def sd(xs):
    if len(xs) < 2:
        return float("nan")
    m = sum(xs) / len(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


print("%-5s %-3s %-4s %-6s %-8s | %-12s %-12s %-10s %-10s" %
      ("fam", "N", "kap", "cells", "|sig|<=", "sd(CRATIO)", "model sd", "ratio", "log2 sd/g"))
lad = {}
for (fam, N, k) in sorted(set((r["fam"], r["N"], r["k"]) for r in rows)):
    for cut in (2.0,):
        g = [r for r in band(N, k, fam) if abs(r["sig"]) <= cut]
        if len(g) < 4:
            continue
        s_meas = sd([r["CR"] for r in g])
        gm = sum(gfun(r["sig"]) for r in g) / len(g)
        s_mod = math.sqrt(2.0) * 2.0 ** (-0.20752 * N) * gm
        print("%-5s %-3d %-4d %-6d %-8.1f | %-12.4e %-12.4e %-10.4f %-10.4f" %
              (fam, N, k, len(g), cut, s_meas, s_mod, s_meas / s_mod,
               math.log2(s_meas / gm)))
        if fam == "M4" and k == 1:
            lad[N] = (s_meas, gm, len(g))
if len(lad) >= 2:
    Ns = sorted(lad)
    pts = [(N, math.log2(lad[N][0] / lad[N][1])) for N in Ns]
    n = len(pts)
    sx = sum(x for x, _ in pts); sy = sum(y for _, y in pts)
    sxx = sum(x * x for x, _ in pts); sxy = sum(x * y for x, y in pts)
    sl = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    print()
    print("M4/kappa=1 sd-ladder over N = %s : fitted exponent %+.5f per unit N"
          % (Ns, sl))
    print("   [registered model -0.20752 ; round-24 max-based fit -0.22532]")
    print("   VERDICT (P4a form): %s" %
          ("DECAY -- the CRATIO fluctuation scale shrinks in N" if sl < 0
           else "GROWTH -- the DEATH direction"))
    for a, b in zip(Ns, Ns[1:]):
        print("   sd ratio N=%d -> N=%d : %.5f   (model 2^{-0.20752*%d} = %.5f)"
              % (a, b, (lad[b][0] / lad[b][1]) / (lad[a][0] / lad[a][1]), b - a,
                 2.0 ** (-0.20752 * (b - a))))


print()
print("=" * 104)
print("2-WAY VERIFICATION SUMMARY (PREREG Z3)")
print("=" * 104)
import glob as _g
for mode in ("alt", "umitm"):
    tot = ag = 0
    bad = []
    for fn in _g.glob(os.path.join(HERE, "VERIFY.%s.*.tsv" % mode)):
        for ln in open(fn):
            fl = ln.rstrip().split("\t")
            if len(fl) < 7:
                continue
            tot += 1
            if fl[6] == "AGREE":
                ag += 1
            else:
                bad.append((fl[0], fl[2], fl[3]))
    print("  ALG-2 mode %-6s : %d/%d cells re-derived, EXACT integer agreement on TNUM and NKER"
          % (mode, ag, tot))
    if bad:
        print("  *** DISAGREEMENTS: %s" % bad)
n32set = set((r["fam"], r["k"], r["p"]) for r in rows if r["N"] == 32)
ver = set()
for fn in _g.glob(os.path.join(HERE, "VERIFY.*.tsv")):
    for ln in open(fn):
        fl = ln.rstrip().split("\t")
        if len(fl) >= 7 and fl[6] == "AGREE":
            ver.add((fl[0], int(fl[2]), int(fl[3])))
print("  N=32 cells with >=1 independent re-derivation: %d / %d" % (len(n32set & ver), len(n32set)))
un = sorted(n32set - ver)
if un:
    print("  NOT yet re-derived (%d): %s" % (len(un), un[:12]))

print()
print("=" * 104)
print("EXACT TMASS at the leading N=32 cells (TMASS = TNUM / 2^32)")
print("=" * 104)
from fractions import Fraction as _F
for r in sorted([x for x in rows if x["N"] == 32], key=lambda x: -x["CR"])[:8]:
    fr = _F(r["TNUM"], 1 << 32)
    print("  %-4s k=%d p=%-12d sig=%+7.4f  TMASS = %s = %.10f   CRATIO = %.10f"
          % (r["fam"], r["k"], r["p"], r["sig"], fr, float(fr), r["CR"]))

print()
print("kappa axis at N=32 (sigma in [-2,2]); RC(i) floor UMIN >= p^{2/N}:")
for k in (1, 2, 3, 4):
    g = [r for r in rows if r["N"] == 32 and r["k"] == k]
    if not g:
        continue
    b = max(g, key=lambda r: r["CR"])
    pm = sum(r["p"] for r in g) / len(g)
    print("  kappa=%d  %3d cells  max CRATIO %.10f at p=%-12d sig=%+7.4f   RC floor %.3f"
          % (k, len(g), b["CR"], b["p"], b["sig"], b["p"] ** (2.0 / 32)))


print()
print("=" * 104)
print("D3-STRAT -- SIGMA-STRATIFIED, M-MATCHED NULL  (the fair comparison)")
print("   My N=32 sample is DESIGNED (a sigma grid plus a dense sigma~0 cluster);")
print("   the N=16 line is every admissible prime.  A plain random N=16 subsample")
print("   would therefore be an unfair opponent.  Here each N=32 cell is matched")
print("   to a random N=16 cell drawn from the SAME sigma bin (width 0.5).")
print("=" * 104)
random.seed(20260809)
g32 = band(32, 1, "M4")
g16 = band(16, 1, "M4")
if g32 and g16:
    bins = {}
    for r in g16:
        bins.setdefault(round(r["sig"] * 2) / 2.0, []).append(r["CR"])
    keys = sorted(bins)

    def pick(sig):
        b = round(sig * 2) / 2.0
        if b not in bins:
            b = min(keys, key=lambda k: abs(k - sig))
        return random.choice(bins[b])
    sims = []
    for _ in range(20000):
        sims.append(max(pick(r["sig"]) for r in g32))
    sims.sort()
    def q(fq):
        return sims[int(fq * (len(sims) - 1))]
    m32 = max(r["CR"] for r in g32)
    below = sum(1 for x in sims if x <= m32) / float(len(sims))
    print("  N=32 M4 kappa=1 sample: %d cells, max CRATIO %.10f" % (len(g32), m32))
    print("  sigma-stratified N=16 null (same %d sigma values, 20000 draws):" % len(g32))
    print("     p05 %.6f   median %.6f   p95 %.6f   max %.6f" %
          (q(.05), q(.5), q(.95), sims[-1]))
    print("  => the N=32 max sits at quantile %.4f of the sigma-matched N=16 null" % below)
    if below < 0.05:
        v = "DECAY, significant at the 5%% level"
    elif below > 0.95:
        v = "GROWTH, significant at the 5%% level -- the DEATH direction"
    elif below < 0.5:
        v = "mild DECAY, NOT significant"
    else:
        v = "mild GROWTH, NOT significant"
    print("  => %s" % v)
    print("  raw comparison (unmatched M): N=16 exhaustive band max %.6f over %d cells"
          % (max(r["CR"] for r in g16), len(g16)))

    # sigma-matched mean/sd comparison too
    def sdv(xs):
        m = sum(xs) / len(xs)
        return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))
    print()
    print("  sigma-stratified sd comparison (low-noise):")
    s32 = sdv([r["CR"] for r in g32])
    ssim = [sdv([pick(r["sig"]) for r in g32]) for _ in range(4000)]
    ssim.sort()
    bl = sum(1 for x in ssim if x <= s32) / float(len(ssim))
    print("     sd(CRATIO) at N=32 = %.6f ; sigma-matched N=16 null median %.6f"
          " (p05 %.6f p95 %.6f) ; quantile %.4f"
          % (s32, ssim[len(ssim) // 2], ssim[int(.05 * len(ssim))],
             ssim[int(.95 * len(ssim))], bl))

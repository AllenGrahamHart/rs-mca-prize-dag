#!/usr/bin/env python3
"""D2 -- THE CONSTANT'S LAW.  Registered model (PREREG R4):
      SD(CRATIO) = sqrt(2) * 2^{-0.20752 N} * g(SIGMA),  g(s) = 2^{s/2}/(1+2^s)
      MAXCR - 1 ~= A * SD * sqrt(2 ln M)
Tests: P4a (N-exponent / DEATH condition), P4b (SDTEST), P4c (out-of-sample).
Plus the deep-SIGMA tail at N=16 (sampled) against THEOREM RC.
tools/ramguard local -- python3 ...
"""
import math, os, random, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zcore import *   # noqa

HERE = os.path.dirname(os.path.abspath(__file__))
EXPO = -0.20752


def g(s):
    return 2 ** (s / 2) / (1 + 2 ** s)


def model_sd(N, s):
    return math.sqrt(2) * 2 ** (EXPO * N) * g(s)


rows = []
for line in open(os.path.join(HERE, "SWEEP.tsv")).read().splitlines()[1:]:
    a = line.split("\t")
    rows.append((a[0], int(a[1]), int(a[2]), int(a[3]), float(a[4]), float(a[5]),
                 float(a[6]), float(a[7]), float(a[8])))
deep = []
for line in open(os.path.join(HERE, "DEEP16.tsv")).read().splitlines()[1:]:
    a = line.split("\t")
    deep.append(("M4", 16, 1, int(a[0]), float(a[1]), float(a[2]), float(a[3]), float(a[4]), float(a[5])))
allrows = [r for r in rows if not (r[0] == "M4" and r[1] == 16)] + deep
print("cells loaded: SWEEP %d + DEEP16 %d -> %d used" % (len(rows), len(deep), len(allrows)))

print()
print("=" * 104)
print("P4b SDTEST -- measured sd(CRATIO) vs model, per (family, N, kappa, unit-SIGMA bin), >= 8 cells")
print("=" * 104)
print("LIVE := fraction of cells in the bin with TMASS > 1 (a nonempty ternary kernel).")
print("PRECISION FLOOR: bins with sd < 1e-12 are double-precision-limited, not physical.")
print("%4s %3s %3s %10s %6s %6s | %11s %11s %7s | %9s" %
      ("fam", "N", "k", "SIGMA bin", "#", "LIVE", "sd measured", "sd model", "RSD", "maxCRATIO"))
bins = {}
for r in allrows:
    bins.setdefault((r[0], r[1], r[2], math.floor(r[4])), []).append(r)
ok = tot = 0
okL = totL = 0
fitpts = []
for key in sorted(bins, key=lambda k: (k[0], k[1], k[2], k[3])):
    v = bins[key]
    if len(v) < 8:
        continue
    cr = [x[6] for x in v]
    n = len(cr)
    live = sum(1 for x in v if x[5] > 1.0 + 1e-12) / n
    mu = sum(cr) / n
    sd = (sum((x - mu) ** 2 for x in cr) / (n - 1)) ** .5
    ms = model_sd(key[1], key[3] + .5)
    rsd = sd / ms if ms > 0 else float("nan")
    tot += 1
    good = 0.5 <= rsd <= 2.0
    ok += good
    usable = live >= 0.2 and sd > 1e-12
    if usable:
        totL += 1
        okL += good
        fitpts.append((key[0], key[1], key[2], key[3] + .5, n, sd, live))
    if key[1] == 16 or live >= 0.2 or key[1] in (4, 32, 64):
        print("%4s %3d %3d %10s %6d %6.2f | %11.3e %11.3e %7.2f | %9.6f  %s%s" %
              (key[0], key[1], key[2], "[%d,%d)" % (key[3], key[3] + 1), n, live, sd, ms, rsd,
               max(cr), "" if good else "   <-- outside [0.5,2]", "  [LIVE]" if usable else ""))
print()
check("P4b SDTEST as REGISTERED: RSD in [0.5,2.0] for >= 80%% of ALL bins", ok >= 0.8 * tot,
      "REGISTERED >=80%% ; measured %d / %d bins = %.1f%%" % (ok, tot, 100.0 * ok / tot))
check("P4b SDTEST restricted to LIVE bins (LIVE >= 0.2, above the precision floor)",
      okL >= 0.8 * totL, "%d / %d LIVE bins = %.1f%%" % (okL, totL, 100.0 * okL / max(totL, 1)))
print()
print("   DIAGNOSIS (registered model REFUTED in the SIGMA << 0 half, CONSERVATIVELY):")
print("   the random-code null assumes every ternary eps is in the kernel with prob p^-kappa.")
print("   THEOREM RC forbids this: for p > N^{N/2} the kernel is EMPTY, so TMASS == 1 and the")
print("   only residual spread in CRATIO = 1/(1+H) comes from H itself.  Reality fluctuates")
print("   LESS than the model everywhere the kernel is dead -- the model is an UPPER bound.")

print()
print("=" * 104)
print("P4a -- the N-exponent (DEATH condition: exponent >= 0 kills Z-CEILING)")
print("=" * 104)
print("   regression of log2( sd_measured / g(SIGMA) ) on N, over LIVE bins only")
print("   (LIVE bins by N: %s)" % {k: sum(1 for p in fitpts if p[1] == k) for k in sorted(set(p[1] for p in fitpts))})
xs = [p[1] for p in fitpts]
ys = [math.log2(p[5] / g(p[3])) for p in fitpts]
nn = len(xs)
mx = sum(xs) / nn
my = sum(ys) / nn
sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
sxx = sum((x - mx) ** 2 for x in xs)
slope = sxy / sxx
inter = my - slope * mx
print("   %d bins, N in %s" % (nn, sorted(set(xs))))
print("   fitted:  log2(sd/g) = %.5f * N + %.5f      (model: %.5f * N + %.5f)"
      % (slope, inter, EXPO, 0.5))
check("P4a fitted N-exponent in the REGISTERED window [-0.30, -0.12]", -0.30 <= slope <= -0.12,
      "REGISTERED [-0.30,-0.12] ; model -0.20752 ; measured %.5f" % slope)
check("P4a DEATH condition NOT met (exponent < 0: the record constant decays in N)", slope < 0,
      "slope %.5f" % slope)
A_fit = 2 ** inter / math.sqrt(2)
print("   implied prefactor A = %.4f  (model 1.0)" % A_fit)

print()
print("=" * 104)
print("P4c -- OUT-OF-SAMPLE.  Fit on N = 8 and N = 16 only; predict N = 4 and N = 32.")
print("=" * 104)
sub = [(p, y) for p, y in zip(fitpts, ys) if p[1] in (8, 16)]
xs2 = [p[1] for p, _ in sub]
ys2 = [y for _, y in sub]
n2 = len(xs2)
mx2 = sum(xs2) / n2
my2 = sum(ys2) / n2
sl2 = sum((x - mx2) * (y - my2) for x, y in zip(xs2, ys2)) / sum((x - mx2) ** 2 for x in xs2)
in2 = my2 - sl2 * mx2
print("   in-sample fit (N=8,16 only): log2(sd/g) = %.5f * N + %.5f" % (sl2, in2))


def pred_max(N, band, M):
    s = sum(band) / 2.0
    sd = 2 ** (sl2 * N + in2) * g(s)
    return sd * math.sqrt(2 * math.log(max(M, 2)))


print("%4s %3s %12s %7s | %13s %13s %8s" %
      ("fam", "N", "SIGMA band", "#cells", "pred MAXCR-1", "meas MAXCR-1", "ratio"))
for (fam, N, kap, blo, bhi) in [("M4", 4, 1, -3, 3), ("M4", 32, 1, 17, 25), ("M4", 64, 1, 50, 60)]:
    v = [r for r in allrows if r[0] == fam and r[1] == N and r[2] == kap and blo <= r[4] < bhi]
    if not v:
        continue
    meas = max(x[6] for x in v) - 1
    pr = pred_max(N, (blo, bhi), len(v))
    print("%4s %3d %12s %7d | %13.3e %13.3e %8s" %
          (fam, N, "[%d,%d)" % (blo, bhi), len(v), pr, meas,
           ("%.2f" % (meas / pr)) if pr > 0 and meas > 0 else "meas<=0"))
    if N == 32:
        check("P4c out-of-sample at N=32 within a factor 2 on (MAXCR-1)",
              meas > 0 and 0.5 <= meas / pr <= 2.0, "pred %.3e meas %.3e ratio %.2f" % (pr, meas, meas / pr))
    if N == 4:
        check("P4c out-of-sample at N=4 within a factor 1.5 on (MAXCR-1)",
              meas > 0 and (1 / 1.5) <= meas / pr <= 1.5,
              "pred %.3e meas %.3e  -- N=4 has NO nonzero ternary kernel at any admissible p "
              "(THEOREM RC: p > N^{N/2} = 16 always), so MAXCR - 1 < 0 identically" % (pr, meas))

print()
print("=" * 104)
print("DEEP-SIGMA TAIL at N=16 (sampled): does the record decay for SIGMA < -6, as RC demands?")
print("=" * 104)
random.seed(20260808)
print("%12s %9s %7s | %11s %11s %11s %9s" %
      ("p band", "SIGMA mid", "#sampled", "maxCRATIO", "sd", "model sd", "RSD"))
for j in range(22, 33):
    lo, hi = 1 << j, 1 << (j + 1)
    got = []
    tries = 0
    while len(got) < 400 and tries < 60000:
        tries += 1
        q = random.randrange(lo, hi)
        q += (1 - q) % 32
        if q >= hi or not is_prime(q):
            continue
        got.append(q)
    if not got:
        continue
    crs = []
    for q in got:
        d = cell(rows_M4(16, q), q)
        assert d["ZFRATIO"] >= 1 - 1e-12
        crs.append(d["CRATIO"])
    n = len(crs)
    mu = sum(crs) / n
    sd = (sum((x - mu) ** 2 for x in crs) / (n - 1)) ** .5
    s = 16 - (j + .5)
    ms = model_sd(16, s)
    print("%12s %9.1f %7d | %11.6f %11.3e %11.3e %9.2f" %
          ("2^%d-2^%d" % (j, j + 1), s, n, max(crs), sd, ms, sd / ms))
print("   THEOREM RC(ii): at N=16 the ternary kernel is EMPTY for every p > 16^8 = 2^32,")
print("   so CRATIO = 1/(1+H) < 1 for all p > 2^32 -- the N=16 line is FINITE, proved.")

sys.exit(summary())

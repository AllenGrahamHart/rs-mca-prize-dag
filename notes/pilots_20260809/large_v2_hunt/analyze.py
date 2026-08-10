#!/usr/bin/env python3
"""Final analysis: the suppression curve, the per-prime V1 test at h = 64,
the turbo rung ladder with Poisson bounds, and CSTAR / VSTAR."""
import glob
import json
import math
import sys
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K  # noqa: E402

D = "notes/pilots_20260809/large_v2_hunt/state/"
ORDER = 128


def merge(files, keys):
    out = {k: {} for k in keys}
    scal = {}
    for f in files:
        d = json.load(open(f))
        for k in keys:
            for kk, vv in d.get(k, {}).items():
                out[k][kk] = out[k].get(kk, 0) + vv
        for k, v in d.items():
            if isinstance(v, int):
                scal[k] = scal.get(k, 0) + v
    return out, scal


lad, ladS = merge(sorted(glob.glob(D + "lad_*.json")),
                  ["gate", "small", "v2", "v212"])
tur, turS = merge(sorted(glob.glob(D + "turbo_*.json")),
                  ["rung", "rungwin", "rungprime", "v2", "v212", "smallp",
                   "gate", "small"])
r24, r24S = merge(sorted(glob.glob(
    "notes/pilots_20260808/kernel_window_hunt/state/v2hunt_*.json")),
    ["v2hist"])

print("=== COVERAGE ===")
print("round-25 lad   : %d odd-norm samples, %d admissible hits"
      % (ladS.get("n", 0), ladS.get("hits", 0)))
print("round-25 turbo : %d odd-norm samples, %d subsampled-pipeline hits"
      % (turS.get("n", 0), turS.get("hits", 0)))
print("round-24 banked: %d samples, %d hits" % (r24S.get("n", 0),
                                                r24S.get("hits", 0)))

# ------------------------------------------------ the v_2(p-1) suppression curve
print("\n=== LADDER: v_2(p-1) of admissible-window prime hits (W_ADM) ===")
comb = {}
for src in (lad["v2"], tur["v2"], r24["v2hist"]):
    for k, v in src.items():
        comb[int(k)] = comb.get(int(k), 0) + v
tot = sum(comb.values())
print("total admissible hits pooled: %d" % tot)
print("  v   count    P(v2=v)    P(v2>=v)   K=P(>=v)*2^(v-7)   LADRATIO")
tail = {}
s = 0
for v in sorted(comb, reverse=True):
    s += comb[v]
    tail[v] = s
prev = None
for v in sorted(comb):
    kk = tail[v] / tot * 2 ** (v - 7)
    rr = "" if prev is None else "%.4f" % (tail[v] / prev)
    print("%3d %8d   %.6f   %.3e      %.4f            %s"
          % (v, comb[v], comb[v] / tot, tail[v] / tot, kk, rr))
    prev = tail[v]
MAXV2HIT = max(comb)
print("MAXV2HIT = %d" % MAXV2HIT)

comb12 = {}
for src in (lad["v212"], tur["v212"]):
    for k, v in src.items():
        comb12[int(k)] = comb12.get(int(k), 0) + v
t12 = sum(comb12.values())
print("\nrestricted to the brief's COFAC <= 2^12 (%d hits): max v_2 = %d"
      % (t12, max(comb12)))
s = 0
for v in sorted(comb12, reverse=True):
    s += comb12[v]
    if v in (8, 12, 16, 20, 24):
        print("   P(v2 >= %2d | hit, cof<=2^12) = %.3e" % (v, s / t12))

# --------------------------------------------- V1 at h = 64: per-prime control
print("\n=== V1 AT h = 64: is badness independent of v_2(p-1)? ===")
print("per-prime incidence vs the null n*(1-(1-1/p)^64), binned by v_2(p-1)")
n64 = turS.get("n", 0)
if n64 and tur["smallp"]:
    bins = {}
    for k, c in tur["smallp"].items():
        p = int(k)
        v = ((p - 1) & -(p - 1)).bit_length() - 1
        exp = n64 * (1 - (1 - 1.0 / p) ** 64)
        a, b = bins.get(v, (0.0, 0.0))
        bins[v] = (a + c, b + exp)
    print("  v   #primes   observed     expected      RATIO    z")
    for v in sorted(bins):
        o, e = bins[v]
        np_ = sum(1 for k in tur["smallp"]
                  if ((int(k) - 1) & -(int(k) - 1)).bit_length() - 1 == v)
        z = (o - e) / math.sqrt(e) if e > 0 else 0.0
        print("%3d %8d %11d %12.1f    %.4f  %+7.1f" % (v, np_, o, e, o / e, z))
    tо = sum(b[0] for b in bins.values())
    te = sum(b[1] for b in bins.values())
    print("  ALL          %11d %12.1f    %.4f" % (tо, te, tо / te))
    # V1 test: is the ratio the SAME constant in every v bin?
    rbar = tо / te
    chi2 = sum((o - rbar * e) ** 2 / (rbar * e) for o, e in bins.values())
    df = len(bins) - 1
    print("  V1 TEST (homogeneity of RATIO across v): chi2 = %.2f on %d df"
          % (chi2, df))
    # and the trend: weighted LS slope with its Poisson standard error
    sw = sx = sy = sxx = sxy = 0.0
    for v, (o, e) in bins.items():
        wt = e * e / max(o, 1.0)                    # 1/Var(o/e)
        x, y = v - 7.0, o / e
        sw += wt; sx += wt * x; sy += wt * y
        sxx += wt * x * x; sxy += wt * x * y
    den = sw * sxx - sx * sx
    b = (sw * sxy - sx * sy) / den
    sb = math.sqrt(sw / den)
    print("  V1 TREND: d(RATIO)/dv = %+.5f +- %.5f  (%.1f sigma from 0)"
          % (b, sb, abs(b) / sb))

# ------------------------------------------- per-family measured hit rates
print("\n=== per-family measured admissible-hit rates (for CSTAR) ===")
fam = {}
for f in sorted(glob.glob(D + "lad_*.json") + glob.glob(D + "turbo_*.json")):
    d = json.load(open(f))
    key = d["fam"]
    a, b_ = fam.get(key, (0, 0))
    fam[key] = (a + d.get("nsub", d["n"]), b_ + d["hits"])
for k in sorted(fam):
    n_, h_ = fam[k]
    print("   %-4s pipeline samples %10d  admissible hits %8d  RATE %.4f"
          % (k, n_, h_, h_ / n_))

# ------------------------------------------------- turbo rung ladder + Poisson
print("\n=== TURBO RUNGS (cofactor-congruence test, c = N mod 2^L) ===")
print("  L   c-congruence   in W_ADM   p PRIME   rate/sample   95%% Poisson UB")
for L in (8, 12, 16, 24, 32, 41):
    a = tur["rung"].get(str(L), 0)
    b = tur["rungwin"].get(str(L), 0)
    c = tur["rungprime"].get(str(L), 0)
    rate = c / n64 if n64 else 0
    ub = 3.0 / n64 if (c == 0 and n64) else 0
    print("%3d %10d %12d %9d   %.3e   %s"
          % (L, a, b, c, rate,
             "%.2e (0 seen)" % ub if c == 0 else "-"))
# power analysis: fit E[rung L] = A * 2^-(L-8) * (L-8) on rungs 16 and 24
r16 = tur["rung"].get("16", 0)
r24 = tur["rung"].get("24", 0)
if r16 and n64:
    A = r16 / (2 ** -8 * 8)
    print("\n  POWER at the achieved coverage (%d odd-norm samples):" % n64)
    print("   L   expected (fit on rung16)   observed   P(0 | expected)   deficit")
    for L in (24, 32, 41):
        e = A * 2.0 ** -(L - 8) * (L - 8)
        o = tur["rung"].get(str(L), 0)
        print("  %3d   %20.3f %10d   %13.3f   %s"
              % (L, e, o, math.exp(-e),
                 "-" if e > 3 else "need %.0fx more samples for 3 expected"
                 % (3 / e)))

# ------------------------------------------------------------ CSTAR / VSTAR
print("\n=== CSTAR / VSTAR (the decision number) ===")
KPOOL = tail.get(12, 0) / tot * 2 ** 5 if 12 in tail else 0.64
# SELF-CORRECTION: the pooled K < 1 is an ARTIFACT of the acceptance rule.
# d2_split.py: FAM-B cofactor-1 acceptances are FORCED to v_2(p-1) = 7 by
# LAW 2 (2947/2947); restricted to cofactor > 1 the law is K = 1.00 +- 0.06
# over v = 8..13, and the independent small-prime channel is flat.  The
# POPULATION law for bad primes is therefore P(v2>=v) = 2^-(v-7), K = 1.
KFIT = 1.0
print("K pooled (instrument, cofactor-1 artefact) = %.4f ; K population = %.2f"
      % (KPOOL, KFIT))
ORB = 2 * 64 * 64
RB = fam["B"][1] / fam["B"][0]
RA = fam["A"][1] / fam["A"][0]
print("h=8 validation of this estimator: INCIDENCE/ORBIT = 485888/128 = 3796 "
      "vs 536 true -> over-predicts by 7.1x = 2^2.83 (state it, do not hide it)")
for name, logsize, rate in (
        ("FAM-B sub-box  (64*2*2^63 = 2^70)", 70.0, RB),
        ("full box, odd-norm half (5^64/2)", 64 * math.log2(5) - 1, RA)):
    nbad = logsize + math.log2(rate) - math.log2(ORB)
    vstar = nbad + 7 + math.log2(KFIT)
    print("%-36s  log2 #bad(W_ADM) = %6.2f   VSTAR = %6.2f" %
          (name, nbad, vstar))
    for v in (41, 92, 97, 200):
        print("      predicted # with v_2 >= %3d : 2^%.1f"
              % (v, nbad + math.log2(KFIT) - (v - 7)))

print("\n=== the same count by window (pure lattice heuristic, cross-check) ===")
print("  #bad(W) = (5^64/2)*64*Sum_{p in W, p=1 mod 128} 1/p / 2h^2,")
print("  Sum 1/p = (1/64)*(lnln B - lnln A)   [Mertens for the progression]")
LB = 64 * math.log2(5) - 1
for nm, a, b in (("W_ADM  2^128 .. 253^32", 128.0, 32 * math.log2(253)),
                 ("W_DEP  2^166 .. 253^32", 166.0, 32 * math.log2(253)),
                 ("deployed band 2^166..2^172", 166.0, 172.0),
                 ("W_TOP  2^244 .. 253^32", 244.0, 32 * math.log2(253))):
    S = (math.log(math.log(2) * b) - math.log(math.log(2) * a)) / 64
    lg = LB + 6 + math.log2(S) - 13
    print("  %-28s log2 #bad = %6.2f   ; with v_2>=41: 2^%.1f ; >=92: 2^%.1f"
          % (nm, lg, lg + math.log2(KFIT) - 34, lg + math.log2(KFIT) - 85))

"""D1 at the prize cell: the counting bound on bad-prime density, with the
v_2-graded form, the retired-proof reproduction, and the N'-scope check.

Pure arithmetic (mpmath-free): Li(x) by its asymptotic series, which at
ln x >= 88 is accurate to far better than the 1-bit resolution used here.
Draft-only; writes to this dir.
"""
import json, math

L2 = math.log(2)


def li(log2x, K=12):
    """log2 Li(x) for x = 2^log2x, via Li(x) ~ x/ln x * sum_k k!/(ln x)^k."""
    lnx = log2x * L2
    s = sum(math.factorial(k) / lnx ** k for k in range(K))
    return log2x - math.log2(lnx) + math.log2(s)


def lgsub(a, b):
    """log2(2^a - 2^b) for a > b."""
    return a + math.log2(1 - 2 ** (b - a))


def pi_ap(lo2, hi2, phi):
    """log2 #{p in (2^lo2, 2^hi2] : p = 1 mod N'}, N' with Euler phi = phi."""
    return lgsub(li(hi2), li(lo2)) - math.log2(phi)


def report(Nprime, lo2, hi2, label, log2classes, rprime):
    phi = Nprime // 2
    P = pi_ap(lo2, hi2, phi)
    bnd = log2classes + math.log2(rprime) - P
    print("  %-28s PI=2^%7.2f  bound 2^%+8.2f %s"
          % (label, P, bnd, "" if bnd < 0 else "  <-- VACUOUS"))
    return P, bnd


out = {}
print("=" * 74)
print("PRIZE CELL  N' = 128, h = 64")
print("=" * 74)
h, Np = 64, 128
lgCEIL = (h / 2) * math.log2(4 * h)                 # (4h)^{h/2} = 256^32
lgCEIL_odd = (h / 2) * math.log2(4 * h - 3)         # 253^32, odd norms only
lgbox = h * math.log2(5)
ORB = 2 * h * h
lgburn = math.log2(5 ** h / ORB + 5 ** (h // 2))
print("CEIL  = (4h)^{h/2}   = 2^%.4f      (PROVED: LN4 energy ceiling, E<=4h)" % lgCEIL)
print("CEILodd=(4h-3)^{h/2} = 2^%.4f      (odd-norm box vectors only)" % lgCEIL_odd)
print("      round-22 addendum's 'plausible sharpening' base 4(h-1)=252: 2^%.4f"
      % ((h / 2) * math.log2(4 * (h - 1))))
print("pigeonhole threshold CEIL^{1/2} = 2^%.4f   vs W_ADM floor 2^128"
      % (lgCEIL / 2))
print("   -> margin %+.4f bits; RPRIME = 1 on (2^128, CEIL] %s"
      % (128 - lgCEIL / 2, "(strict-inequality argument needed at margin 0)"))
print("box classes 5^h = 2^%.4f ; Burnside orbit bound = 2^%.4f (saves %.2f bits)"
      % (lgbox, lgburn, lgbox - lgburn))

print()
print("PROVED density bounds  BADDENS(W) <= RPRIME * CLASSBOUND / PI(W):")
for cb, tag in ((lgbox, "bulletproof 5^h"), (lgburn, "Burnside orbit")):
    print(" using CLASSBOUND = 2^%.2f (%s)" % (cb, tag))
    out[tag] = {}
    for lab, lo2, hi2 in (("W_ADM  (2^128, 2^256]", 128, lgCEIL),
                          ("W_TOP  [2^244, 2^255.46]", 244, lgCEIL_odd),
                          ("W_DEP  [2^166, 2^172)", 166, 172)):
        P, b = report(Np, lo2, hi2, lab, cb, 1)
        out[tag][lab] = [P, b]

print()
print("v_2-GRADED (the pose's uniformity clause), Burnside bound, W = W_ADM:")
P_adm = pi_ap(128, lgCEIL, 64)
print("   v     PI_v          proved bound      heuristic BADDENS (flat)")
vsparse = None
for v in (7, 8, 16, 32, 64, 92, 97, 100, 106, 110, 113, 114, 120, 200):
    P_v = P_adm - (v - 7)
    b = lgburn - P_v
    if b < 0:
        vsparse = v
    print("  %3d   2^%7.2f      2^%+8.2f %s" % (v, P_v, b, "" if b < 0 else " VACUOUS"))
# exact VSPARSE
vst = 7 + (P_adm - lgburn)
print("VSPARSE(128) = %.2f   (largest v_2 level with a non-vacuous proved bound)" % vst)
out["VSPARSE"] = vst
print("   deployed Proth rows v_2 = 92,93,95,97 -> inside, margin %.1f bits each"
      % (vst - 97))
print("   E1-128 pinned field  v_2 = 200        -> OUTSIDE (per-row certificate)")

print()
print("=" * 74)
print("ESCAPE TEST: reproduce round-25's W_TOP density ~2^-112 from its own inputs")
P_top = pi_ap(244, lgCEIL_odd, 64)
print("  round-25 log2 BADCOUNT(W_TOP) = 130.2 (measured) ; my PI(W_TOP) = 2^%.2f" % P_top)
print("  => BADDENS(W_TOP) = 2^%.2f   (round-25 addendum: ~2^-112)" % (130.2 - P_top))
P_admr = pi_ap(128, lgCEIL_odd, 64)
print("  round-25 log2 BADCOUNT(W_ADM) = 132.0 ; PI = 2^%.2f => 2^%.2f"
      % (P_admr, 132.0 - P_admr))
out["wtop_density"] = 130.2 - P_top

print()
print("=" * 74)
print("PRIOR ART REPRODUCTION: retired_proof.md (e1_folded_..._256_payload)")
for Npr, d in ((128, 64), (256, 128)):
    lgN = d * math.log2(Npr)                       # their height bound N'^d
    lgE = (d / 2) * math.log2(4 * d)               # LN4 energy ceiling
    P = 250.0
    rN_their = math.floor(lgN / P)
    rN_mine = max(1, math.floor(lgE / P))
    ES = d * math.log2(5) + math.log2(max(rN_their, 1)) + math.log2(d * P * L2) - P
    ESm = d * math.log2(5) - math.log2(2 * d * d) + math.log2(rN_mine) \
        + math.log2(d * P * L2) - P
    print(" N'=%3d d=%3d: their height 2^%.1f r_N=%d -> E S_p = 2^%.1f  (paper: %s)"
          % (Npr, d, lgN, rN_their, ES, "2^-87.4" if Npr == 128 else "2^64.2"))
    print("              LN4 height 2^%.1f r_N=%d + orbit -> E S_p = 2^%.1f  %s"
          % (lgE, rN_mine, ESm, "" if ESm < 0 else "STILL VACUOUS"))
    out["retired_N%d" % Npr] = [ES, ESm]

print()
print("=" * 74)
print("SCOPE: is 'o(1) as N' -> infinity' available?  (two window readings)")
print(" (A) window capped by the PRIZE at 2^256 (|F| < 2^256), floor 2^128:")
for Npr in (32, 64, 128, 256, 512):
    d = Npr // 2
    lgcb = math.log2(5 ** d / (2 * d * d) + 5 ** (d // 2))
    lgE = (d / 2) * math.log2(4 * d)
    rN = max(1, math.floor(lgE / 128))
    P = pi_ap(128, 256, d)
    print("   N'=%3d  CLASSBOUND 2^%8.2f  RPRIME %d  PI 2^%.2f  bound 2^%+9.2f %s"
          % (Npr, lgcb, rN, P, lgcb + math.log2(rN) - P,
             "" if lgcb + math.log2(rN) - P < 0 else "VACUOUS"))
print(" (B) window = the natural (2^{N'}, MAXNORM] one:")
for Npr in (16, 32, 64, 128, 256, 512, 1024):
    d = Npr // 2
    lgcb = math.log2(5 ** d / (2 * d * d) + 5 ** (d // 2))
    lgE = (d / 2) * math.log2(4 * d)
    rN = max(1, math.ceil(lgE / Npr))
    P = pi_ap(Npr, lgE, d)
    print("   N'=%4d CLASSBOUND 2^%9.2f RPRIME %d PI 2^%.2f  bound 2^%+10.2f %s"
          % (Npr, lgcb, rN, P, lgcb + math.log2(rN) - P,
             "" if lgcb + math.log2(rN) - P < 0 else "VACUOUS"))

json.dump(out, open("notes/pilots_20260809/b_sparsity_pose/state_d1_prize.json", "w"),
          indent=1)
print("\nwrote state_d1_prize.json")

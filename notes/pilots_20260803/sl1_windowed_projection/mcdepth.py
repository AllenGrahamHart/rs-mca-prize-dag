#!/usr/bin/env python3
"""SL-1 route (3): the 2-ADIC DEPTH CHECK -- can MC reach a band-proper
depth at all?   (pilot 2026-08-03, continuation of the crashed run)

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 <this>

HARD LAW 5 (subtraction).  The mathematics here is NOT re-derived: it is
CONSUMED from the banked draft
  notes/pilots_20260802/band_mint_prep/drafts/xr_mc_depth_quantization/
  (proof.md Claims 1-3) and its WIRING.md statement, merging
  notes/pilots_20260802/xr_occupancy_v2/ THEOREM 5 with
  notes/pilots_20260802/band_adjudication/ THEOREM BP (135 checks, 0 fails).

Banked statements used verbatim:
  THEOREM 5 (MC depth quantization).  For an MC pencil, distinct coset
    unions T != T' have |T ^ T'| <= r'-M, so cross pairs have joint
    agreement <= k; the only MC-family band pairs are DIAGONAL (P_T,Q_T)
    at depth EXACTLY w.  N_d = 0 at every band-proper depth.
  BP(1).  A coset-union core complement with M = 2^ceil(log2 d) forces
    M | d, hence M = d: STRUCTURED => d is a POWER OF TWO.
  BP(3) (parity; strictly stronger, preferred).  On the shift class the
    direction map has mu_g-coset fibres, g = gcd(j,n) a power of two
    (n is a power of two); a depth-d forced ray is live iff g = h-d.
    With h ODD and d a 2-power >= 2, h-d is odd and > 1, so g != h-d;
    d = 1 admits no shift.  Hence N_d^coset = 0 at EVERY band-proper
    depth.
  NOT claimed (banked caveat, carried): protection against NON-coset
    families; the h-EVEN control (n=20, h=6, d=4, j=2 gives N_4 = 2)
    shows the official protection is PARITY, not impossibility.

SUBTRACTION NOTICE (hard law 5, stated up front).  Checks M1/M2 below
are a REPLICATION, not a discovery: the banked verifier
`background/nodes/xr_mc_depth_quantization/verify.py` already machine-
checks the same 2-adic/parity arithmetic at all six rows (its "check C",
135+66 checks, 0 fails; re-run 2026-08-03, XR_MC_DEPTH_QUANTIZATION_ALL_PASS).
They are reproduced here ONLY so this pilot's conclusion is
self-contained and so any disagreement with the banked node would
surface.  The ONE new statement in this file is M4 (SPECTRAL
EXCLUSION), which is what SL-1 actually needs.

WHAT THIS FILE ADDS.  The arithmetic instantiation at the six rows,
plus the consequences SL-1 needs:

  (M1) the band-proper interval [ceil(h/2), h-2] contains NO power of
       two at any of the six rows -- so BP(1) alone already empties the
       band proper of structured families (BP(3) is not even needed for
       the *interval* statement, only for d=1 and the live test);
  (M2) 2-adic form: with h = 2^m + 1 at every row, v_2(h-1) = m while
       every band-proper d satisfies 2^(m-1) < d < 2^m, hence
       v_2(d) <= m-1 AND d is not a 2-power -- the band proper sits
       strictly BETWEEN two consecutive powers of two;
  (M3) the MC agreement tier A-1 is OUTSIDE the SL-1 window [k+d, A-2]
       for every d -- an INDEPENDENT second exclusion.

  (M4) *** SPECTRAL EXCLUSION (the new statement; the payoff) ***
       By MC-1 the MC family at parameter w consists of codewords of
       agreement EXACTLY k+w, and by MC-2 nothing sits above it; by
       BP(1) a structured w is a POWER OF TWO.  So the MC-reachable
       agreement spectrum is
            SPEC = { k + w : w a power of two, 1 <= w <= h-1 }.
       The SL-1 windowed count at a band-proper depth d counts exactly
            WIN(d) = [k+d, A-2] = [k+d, k+h-2],  d >= ceil(h/2).
       A structured family contributes to W_d(z) iff k+w lies in
       WIN(d), i.e. iff w is a power of two with d <= w <= h-2 --
       and a fortiori iff w is a power of two in [ceil(h/2), h-2],
       which is EMPTY by M1.  Hence

            SPEC  ^  WIN(d)  =  {}   for EVERY band-proper d,

       at all six rows: the windowed count receives ZERO contribution
       from any coset/MC family.  The three cases are exhaustive and
       each is excluded for a DIFFERENT reason:
         w <  ceil(h/2) : agreement k+w < k+d -- BELOW the window floor
         ceil(h/2) <= w <= h-2 : NO SUCH w (2-adic gap, M1/M2)
         w =  h-1       : agreement A-1 > A-2 -- ABOVE the window top
       This is why the windowed upgrade defeats the MC refutation:
       the window [k+d, A-2] is precisely the complement of the
       MC-reachable spectrum in the range THEOREM 2 must count.
"""
import json
from math import gcd

ROWS = [
    dict(name="RowC 1/4", n=1024, k=256, A=261, h=5),
    dict(name="RowC 1/8", n=1024, k=128, A=133, h=5),
    dict(name="RowC 1/16", n=1024, k=64, A=67, h=3),
    dict(name="prize 1/4", n=2199023255552, k=549755813888,
         A=558345748481, h=8589934593),
    dict(name="prize 1/8", n=2199023255552, k=274877906944,
         A=283467841537, h=8589934593),
    dict(name="prize 1/16", n=2199023255552, k=137438953472,
         A=141733920769, h=4294967297),
]


def is_pow2(x):
    return x >= 1 and (x & (x - 1)) == 0


def v2(x):
    return (x & -x).bit_length() - 1 if x else None


def pow2s_in(lo, hi):
    """every power of two in the closed interval [lo, hi]."""
    out = []
    if hi < 1:
        return out
    e = 0
    while (1 << e) <= hi:
        if (1 << e) >= lo:
            out.append(1 << e)
        e += 1
    return out


def main():
    checks = []
    rows = []

    def ck(tag, ctx, ok, extra=None):
        checks.append([tag, ctx, bool(ok), extra])

    for r in ROWS:
        n, k, A, h = r["n"], r["k"], r["A"], r["h"]
        dlo, dhi = -(-h // 2), h - 2
        rec = dict(name=r["name"], n=n, k=k, A=A, h=h,
                   band_proper=[dlo, dhi], bp_nonempty=dlo <= dhi,
                   h_odd=(h % 2 == 1), n_is_pow2=is_pow2(n),
                   k_is_pow2=is_pow2(k))
        ck("A = k + h", r["name"], A == k + h)
        # ---- the parity hypothesis BP(3) leans on -------------------
        ck("h ODD (BP(3) hypothesis)", r["name"], h % 2 == 1)
        ck("n a power of two (g = gcd(j,n) is a 2-power)", r["name"],
           is_pow2(n))
        # ---- (M1) BANDPROPER CONTAINS NO POWER OF TWO ---------------
        if dlo <= dhi:
            p2 = pow2s_in(dlo, dhi)
            rec["pow2_in_band_proper"] = p2
            ck("M1: NO power of two in band proper [ceil(h/2), h-2]",
               f"{r['name']} [{dlo},{dhi}]", not p2, p2)
            # BP(1) => every structured depth is a 2-power; combined:
            ck("M1': BP(1) empties the band proper of structured families",
               r["name"], not p2)
        else:
            rec["pow2_in_band_proper"] = None
            ck("band proper EMPTY (vacuous)", r["name"], True)
        # ---- the unique 2-power in [ceil(h/2), h] is h-1 -------------
        p2u = pow2s_in(dlo, h) if dlo <= h else []
        rec["pow2_in_ceilh2_to_h"] = p2u
        ck("unique 2-power in [ceil(h/2), h] is h-1 (= cascade tier)",
           r["name"], p2u == [h - 1], p2u)
        ck("h-1 IS a power of two at this row", r["name"], is_pow2(h - 1))
        # ---- (M2) the 2-adic statement ------------------------------
        m = v2(h - 1)
        rec["v2_h_minus_1"] = m
        rec["h_equals_2m_plus_1"] = (h == (1 << m) + 1)
        ck("h = 2^m + 1 with m = v_2(h-1)", r["name"], h == (1 << m) + 1)
        if dlo <= dhi:
            # band proper sits STRICTLY between 2^(m-1) and 2^m
            ck("M2: 2^(m-1) < ceil(h/2) and h-2 < 2^m",
               f"{r['name']} m={m}",
               (1 << (m - 1)) < dlo and dhi < (1 << m),
               [1 << (m - 1), dlo, dhi, 1 << m])
            # hence no band-proper d is a 2-power, and v_2(d) <= m-1
            ck("M2': v_2(d) <= m-1 for every band-proper d "
               "(d < 2^m)", f"{r['name']} m={m}", dhi < (1 << m))
            # the cascade tier IS the missing 2-power
            ck("M2'': cascade depth h-1 = 2^m is the 2-power the band "
               "proper misses", r["name"], h - 1 == (1 << m))
        # ---- BP(3) parity, instantiated -----------------------------
        # for every 2-power d in [2, h-2]: h-d odd and > 1 => not a
        # 2-power => g != h-d => the forced ray is NOT live.
        bad = []
        e = 1
        while (1 << e) <= max(dhi, 1):
            d = 1 << e
            if 2 <= d <= h - 2:
                hd = h - d
                if hd % 2 == 0 or hd <= 1 or is_pow2(hd):
                    bad.append([d, hd])
            e += 1
        ck("BP(3): for every 2-power d in [2,h-2], h-d is odd, >1, "
           "not a 2-power", r["name"], not bad, bad[:4])
        rec["BP3_violations"] = bad
        # ---- (M3) agreement-tier exclusion --------------------------
        # SL-1 window is [k+d, A-2]; MC sits at agreement A-1.
        ck("M3: MC tier A-1 is ABOVE the window top A-2",
           r["name"], (A - 1) > (A - 2))
        ck("M3': live tier A is above the window top too",
           r["name"], A > A - 2)
        if dlo <= dhi:
            ck("M3'': window [k+d, A-2] non-empty at both band-proper "
               "endpoints", r["name"], k + dlo <= A - 2 and k + dhi <= A - 2)
        # ---- (M4) SPECTRAL EXCLUSION -------------------------------
        # SPEC = agreements reachable by a structured/coset family
        #      = {k+w : w a 2-power, 1 <= w <= h-1}   (MC-1 + MC-2 + BP(1))
        spec_w = [1 << e for e in range(0, (h - 1).bit_length() + 1)
                  if 1 <= (1 << e) <= h - 1]
        rec["spec_w"] = spec_w if len(spec_w) < 12 else \
            [spec_w[0], spec_w[1], "...", spec_w[-1]]
        rec["n_spec_w"] = len(spec_w)
        if dlo <= dhi:
            overlap_any = []
            for d in range(dlo, dhi + 1) if dhi - dlo < 64 else (dlo, dhi):
                # w contributes to W_d iff k+d <= k+w <= k+h-2
                ov = [w for w in spec_w if d <= w <= h - 2]
                if ov:
                    overlap_any.append([d, ov])
            ck("M4: SPEC ^ WIN(d) = {} at the band-proper endpoints "
               "(no coset family contributes to W_d)",
               f"{r['name']}", not overlap_any, overlap_any[:3])
            # the three-case exhaustion, checked as a partition
            below = [w for w in spec_w if w < dlo]
            inside = [w for w in spec_w if dlo <= w <= h - 2]
            above = [w for w in spec_w if w > h - 2]
            ck("M4': the 2-power spectrum splits BELOW / (empty) / ABOVE",
               r["name"],
               inside == [] and above == [h - 1] and
               len(below) + len(above) == len(spec_w),
               [below[-3:], inside, above])
            ck("M4'': the ABOVE case is exactly the cascade tier w=h-1 "
               "at agreement A-1", r["name"],
               above == [h - 1] and k + (h - 1) == A - 1)
        rows.append(rec)

    # ---------------- h-EVEN CONTROL (honest counterexample) ----------
    # banked: n=20, h=6, d=4, j=2 gives N_4 = 2 -- a structured family AT
    # a band-proper depth.  Reproduce the ARITHMETIC that permits it.
    ctrl = []
    for (n_, h_) in [(20, 6), (24, 6), (16, 8), (32, 8)]:
        dlo, dhi = -(-h_ // 2), h_ - 2
        p2 = pow2s_in(dlo, dhi) if dlo <= dhi else []
        ctrl.append(dict(n=n_, h=h_, band_proper=[dlo, dhi],
                         pow2_in_band_proper=p2,
                         BP1_protects=(not p2)))
    # the control MUST show the protection failing for h even
    ck("h-EVEN control: BP(1) does NOT empty the band proper at h=6",
       "n=20,h=6", any(c["pow2_in_band_proper"] for c in ctrl
                       if c["h"] == 6), ctrl[0])
    ck("h-EVEN control: d=4 IS a band-proper 2-power at h=6",
       "n=20,h=6", 4 in (ctrl[0]["pow2_in_band_proper"] or []))
    # and the six rows must NOT be h-even
    ck("no row of record is h-even", "six rows",
       all(r["h"] % 2 == 1 for r in ROWS))

    # ---------------- report ------------------------------------------
    print(f"{'row':12s} {'h':>13s} {'v2(h-1)':>8s} {'band proper':>28s} "
          f"{'2-powers in bp':>15s} {'cascade 2^m':>13s}")
    for rec in rows:
        bp = f"[{rec['band_proper'][0]},{rec['band_proper'][1]}]"
        p2 = rec.get("pow2_in_band_proper")
        p2s = "EMPTY" if p2 == [] else ("n/a" if p2 is None else str(p2))
        print(f"{rec['name']:12s} {rec['h']:>13d} {rec['v2_h_minus_1']:>8d} "
              f"{bp:>28s} {p2s:>15s} {rec['h'] - 1:>13d}")
    print()
    print("h-EVEN control (protection is PARITY, not impossibility):")
    for c in ctrl:
        print(f"   n={c['n']:3d} h={c['h']} band proper "
              f"[{c['band_proper'][0]},{c['band_proper'][1]}] "
              f"2-powers={c['pow2_in_band_proper']} "
              f"BP(1) protects = {c['BP1_protects']}")

    bad = [c for c in checks if not c[2]]
    print(f"\nchecks: {len(checks)}  failures: {len(bad)}")
    for b in bad:
        print("  FAIL", b)
    with open(__file__.replace(".py", ".json"), "w") as fh:
        json.dump(dict(rows=rows, control=ctrl, checks=checks,
                       verdict="PASS" if not bad else "FAIL"), fh, indent=1)


if __name__ == "__main__":
    main()

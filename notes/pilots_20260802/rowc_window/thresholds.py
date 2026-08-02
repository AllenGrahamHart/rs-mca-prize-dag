#!/usr/bin/env python3
"""RowC window pilot -- part 1: the exact admissibility-gate / supply ladder.

Lane P-B, pilot rowc_window (2026-08-02).  REPORT ONLY.  Nothing outside this
directory is written; every import is read-only.

    tools/ramguard local -- python3 \
        notes/pilots_20260802/rowc_window/thresholds.py

WHAT THIS COMPUTES
------------------
For each of the six clean-rate rows, the five q-thresholds that decide whether
a UNIFORMLY RANDOM received pair (u,v) over D = mu_n < F_q^* is

  (a) admissible for P-B  -- i.e. it survives the T0-T4 strips and sits in the
      globally generic branch -- and simultaneously
  (b) a counterexample to P-B's |Gamma_lo| <= 8 n^3.

First moments, word model, exact.  Write C = C(n,A), h = A - K.

  E[# witness pairs (S,z)]                        = C q^{1-h}          =: mu
  E[# rays with agreement >= A+1]  (T2 tangent)   = C(n,A+1) q^{-h}
  E[# joint codeword-pair A-explanations] (T0/GG) = C q^{-2h}
  E[# joint (A-1)-explanations]  (below cascade)  = C(n,A-1) q^{-2(h-1)}

so the thresholds (log2 q) are

  G_T2   = log2 C(n,A+1) / h              random pair passes the tangent gate
  G_GG   = log2 C(n,A)   / (2h)           random pair is globally generic
  G_CASC = log2 C(n,A-1) / (2(h-1))       random pair is below cascade
  L3     = (log2 C(n,A) - log2 8n^3)/(h-1)   P-B's own first moment fits 8n^3
  L1     = (log2 C(n,A) + 128)/h          mean live slopes <= B* = floor(q/2^128)
  F0     = 128 + log2(16 n^3)             B* >= 16n^3, i.e. the consumer's own
                                          budget arithmetic is non-vacuous
                                          (xr_smallcore_spread_count: R_post
                                          <= 16n^3 must fit inside B*)

EXPOSURE = the q-interval on which a random pair is admissible and mu > 8n^3:

    bare      band = ( max(G_T2, G_GG, G_CASC),                L3 )
    program   band = ( max(G_T2, G_GG, G_CASC, F0),            L3 )

Exact integers wherever n <= 4096; rigorous high-precision Stirling (mpmath,
60 digits, cross-checked against the two-sided entropy bracket) at the prize
rows, where the decision margins are 10^11 bits wide and precision is a
non-issue.
"""

from __future__ import annotations

import json
import os
import sys
from math import comb

sys.dont_write_bytecode = True

from mpmath import mp, mpf, log, loggamma  # noqa: E402

mp.dps = 60
LN2 = log(mpf(2))

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "THRESHOLDS.json")

# ---------------------------------------------------------------------------
# The six clean-rate rows.  (n, k, A) banked at
#   critical/nodes/dyadic_profile_evaluation/proof.md:79-86
#   critical/nodes/xr_smallcore_spread_count/notes/
#       audit_consumption_replay_20260710.py:98
# h = A - k.
# ---------------------------------------------------------------------------
ROWS = [
    ("RowC 1/4", 1 << 10, 1 << 8, 261),
    ("RowC 1/8", 1 << 10, 1 << 7, 133),
    ("RowC 1/16", 1 << 10, 1 << 6, 67),
    ("prize 1/4", 1 << 41, 1 << 39, 558345748481),
    ("prize 1/8", 1 << 41, 1 << 38, 283467841537),
    ("prize 1/16", 1 << 41, 1 << 37, 141733920769),
]

EPS_BITS = 128            # tools/prize_row_descriptor.py:17
FIELD_CAP_BITS = 256      # tools/prize_row_descriptor.py:18  (q < 2^256)
PIN_ROWC_BITS = 250       # e1_pair_feasible_prime_field_reduction/proof.md:20-22
PIN_PRIZE_BSTAR = 317494674775468773183020924238786383963


def lg_binom(n: int, r: int) -> mpf:
    """log2 C(n,r): exact for n <= 4096, 60-digit Stirling otherwise."""
    if r < 0 or r > n:
        return mpf("-inf")
    if n <= 4096:
        c = comb(n, r)
        # exact integer -> exact log2 to 60 digits
        return log(mpf(c)) / LN2
    return (loggamma(mpf(n + 1)) - loggamma(mpf(r + 1))
            - loggamma(mpf(n - r + 1))) / LN2


def entropy_bracket(n: int, a: int):
    """Rigorous two-sided bracket 2^{nH}/(n+1) <= C(n,a) <= 2^{nH}."""
    p = mpf(a) / mpf(n)
    hh = -(p * log(p) / LN2 + (1 - p) * log(1 - p) / LN2)
    hi = mpf(n) * hh
    return hi - log(mpf(n + 1)) / LN2, hi


def iroot(x: int, k: int) -> int:
    """floor(x**(1/k)) exactly."""
    if x < 0:
        raise ValueError
    if x == 0:
        return 0
    r = 1 << ((x.bit_length() + k - 1) // k)
    while True:
        nr = ((k - 1) * r + x // r ** (k - 1)) // k
        if nr >= r:
            return r
        r = nr


def row_record(name, n, k, A):
    h = A - k
    b8 = 3 + 3 * (n.bit_length() - 1)          # log2(8 n^3), exact integer
    b16 = b8 + 1
    assert 8 * n ** 3 == 1 << b8

    C1 = lg_binom(n, A)
    C1p = lg_binom(n, A + 1)
    C1m = lg_binom(n, A - 1)

    G_T2 = C1p / h
    G_GG = C1 / (2 * h)
    G_CASC = C1m / (2 * (h - 1))
    L1 = (C1 + EPS_BITS) / h
    L2 = C1 / h
    L3 = (C1 - b8) / (h - 1)
    F0_16 = mpf(EPS_BITS + b16)
    F0_8 = mpf(EPS_BITS + b8)

    gate_floor = max(G_T2, G_GG, G_CASC)
    prog_floor = max(gate_floor, F0_16)

    rec = dict(
        row=name, n=n, k=k, A=A, h=h,
        log2_8n3=b8, log2_16n3=b16,
        log2_C_nA=str(C1), log2_C_nA1=str(C1p), log2_C_nAm1=str(C1m),
        G_T2_tangent=str(G_T2),
        G_GG_globally_generic=str(G_GG),
        G_CASC_below_cascade=str(G_CASC),
        L1_mean_live_le_Bstar=str(L1),
        L2_no_competition=str(L2),
        L3_supply_8n3=str(L3),
        F0_Bstar_ge_16n3=str(F0_16),
        F0_Bstar_ge_8n3=str(F0_8),
        gate_floor=str(gate_floor),
        program_floor=str(prog_floor),
        bare_band_nonempty=bool(L3 > gate_floor),
        bare_band_width_bits=str(L3 - gate_floor),
        program_band_nonempty=bool(L3 > prog_floor),
        program_band_width_bits=str(L3 - prog_floor),
        sound_band_nonempty=bool(L3 > max(prog_floor, L1)),
        sound_band_width_bits=str(L3 - max(prog_floor, L1)),
    )

    # worst-case violation: mu at the floor of each band, in bits over 8n^3
    for tag, fl in (("bare", gate_floor), ("program", prog_floor),
                    ("sound", max(prog_floor, L1))):
        if L3 > fl:
            rec[f"{tag}_max_violation_bits"] = str((h - 1) * (L3 - fl))
            rec[f"{tag}_log2_mu_at_floor"] = str(C1 - (h - 1) * fl)
        else:
            rec[f"{tag}_max_violation_bits"] = None
            rec[f"{tag}_safety_margin_bits"] = str(fl - L3)

    # exact integer thresholds where the binomials are representable
    if n <= 4096:
        C = comb(n, A)
        Cp = comb(n, A + 1)
        # smallest q with q^h > C(n,A+1)  (E[T2 violations] < 1)
        r = iroot(Cp, h)
        rec["q_gate_T2_min_exact"] = r + 1
        # largest q with 8n^3 q^(h-1) < C   (mu > 8n^3)
        r3 = iroot((C - 1) // (1 << b8), h - 1)
        while (1 << b8) * (r3 + 1) ** (h - 1) < C:
            r3 += 1
        while (1 << b8) * r3 ** (h - 1) >= C:
            r3 -= 1
        rec["q_supply_max_exact"] = r3
        rec["q_F0_16n3_exact"] = (1 << b16) << EPS_BITS
        rec["C_nA_exact_bitlen"] = C.bit_length()
    else:
        lo, hi = entropy_bracket(n, A)
        rec["entropy_bracket_log2_C"] = [str(lo), str(hi)]
        rec["stirling_inside_bracket"] = bool(lo <= C1 <= hi)

    # banked envelope pin
    if name.startswith("RowC"):
        rec["envelope_pin_log2q"] = float(PIN_ROWC_BITS)
    else:
        rec["envelope_pin_log2q"] = float(
            log(mpf(PIN_PRIZE_BSTAR << EPS_BITS)) / LN2)
    rec["pin_above_L3_bits"] = str(mpf(rec["envelope_pin_log2q"]) - L3)
    rec["field_cap_ok"] = bool(L3 < FIELD_CAP_BITS)
    return rec


def main():
    recs = [row_record(*r) for r in ROWS]

    print("=" * 96)
    print("PART 1 -- ROW CONSTANTS AND THE FIVE THRESHOLDS (log2 q)")
    print("=" * 96)
    hdr = ("%-11s %5s %14s %10s %10s %10s %10s %10s %10s" %
           ("row", "h", "log2 C(n,A)", "G_T2", "G_GG", "G_CASC",
            "F0(16n^3)", "L1", "L3"))
    print(hdr)
    for r in recs:
        print("%-11s %5d %14.4f %10.4f %10.4f %10.4f %10.4f %10.4f %10.4f" %
              (r["row"], r["h"], float(mpf(r["log2_C_nA"])),
               float(mpf(r["G_T2_tangent"])), float(mpf(r["G_GG_globally_generic"])),
               float(mpf(r["G_CASC_below_cascade"])), float(mpf(r["F0_Bstar_ge_16n3"])),
               float(mpf(r["L1_mean_live_le_Bstar"])), float(mpf(r["L3_supply_8n3"]))))

    print()
    print("prize-row thresholds to full precision (the bands are ~1e-8 bits wide):")
    for r in recs[3:]:
        print("  %-11s G_T2 = %s" % (r["row"], mp.nstr(mpf(r["G_T2_tangent"]), 22)))
        print("  %-11s L3   = %s" % ("", mp.nstr(mpf(r["L3_supply_8n3"]), 22)))
        print("  %-11s L1   = %s" % ("", mp.nstr(mpf(r["L1_mean_live_le_Bstar"]), 22)))
        print("  %-11s F0   = %s" % ("", mp.nstr(mpf(r["F0_Bstar_ge_16n3"]), 22)))

    print()
    print("=" * 96)
    print("PART 2 -- THE EXPOSURE BANDS   (random pair admissible  AND  mu > 8n^3)")
    print("=" * 96)
    print("%-11s %-34s %-12s %-12s" %
          ("row", "band (log2 q)", "width bits", "max violation"))
    for tag, floorkey in (("BARE  (gates only)", "gate_floor"),
                          ("PROG  (+ B* >= 16n^3)", "program_floor")):
        print("--- %s" % tag)
        for r in recs:
            fl = mpf(r[floorkey])
            L3 = mpf(r["L3_supply_8n3"])
            if L3 > fl:
                print("%-11s (%s, %s) %12s %12s" %
                      (r["row"], mp.nstr(fl, 12), mp.nstr(L3, 12),
                       mp.nstr(L3 - fl, 6),
                       mp.nstr((mpf(r["h"]) - 1) * (L3 - fl), 6)))
            else:
                print("%-11s EMPTY -- safe by %s bits of q" %
                      (r["row"], mp.nstr(fl - L3, 6)))

    print()
    print("--- SOUND (additionally mean live slopes <= B*, i.e. q >= L1)")
    for r in recs:
        fl = max(mpf(r["program_floor"]), mpf(r["L1_mean_live_le_Bstar"]))
        L3 = mpf(r["L3_supply_8n3"])
        if L3 > fl:
            print("%-11s (%s, %s) %12s %12s" %
                  (r["row"], mp.nstr(fl, 12), mp.nstr(L3, 12),
                   mp.nstr(L3 - fl, 6),
                   mp.nstr((mpf(r["h"]) - 1) * (L3 - fl), 6)))
        else:
            print("%-11s EMPTY -- safe by %s bits of q" %
                  (r["row"], mp.nstr(fl - L3, 6)))

    print()
    print("=" * 96)
    print("PART 3 -- EXACT INTEGER THRESHOLDS AT THE RowC ROWS")
    print("=" * 96)
    for r in recs[:3]:
        print("  %s" % r["row"])
        print("    q_gate_T2_min (smallest q with q^h > C(n,A+1)) = %d"
              % r["q_gate_T2_min_exact"])
        print("    q_supply_max  (largest q with 8n^3 q^(h-1) < C) = %d"
              % r["q_supply_max_exact"])
        print("    q_F0          (16 n^3 * 2^128)                  = %d"
              % r["q_F0_16n3_exact"])
        live = (r["q_supply_max_exact"] > max(r["q_gate_T2_min_exact"],
                                              r["q_F0_16n3_exact"]))
        print("    program band non-empty: %s" % live)

    print()
    print("=" * 96)
    print("PART 4 -- THE FAMILY-UNIFORM P-B CONSTANT")
    print("     smallest c with |Gamma_lo| <= c valid at EVERY q in the")
    print("     admissible range, = sup mu over the band, in units of 8n^3")
    print("=" * 96)
    print("%-11s %16s %16s %16s" % ("row", "bare", "program", "sound(q>=L1)"))
    for r in recs:
        C1 = mpf(r["log2_C_nA"])
        b8 = r["log2_8n3"]
        out = []
        for key in ("gate_floor", "program_floor", None):
            if key is None:
                fl = max(mpf(r["program_floor"]), mpf(r["L1_mean_live_le_Bstar"]))
            else:
                fl = mpf(r[key])
            v = C1 - (mpf(r["h"]) - 1) * fl - b8
            out.append("2^%s" % mp.nstr(v, 6) if v > 0 else "fits")
        print("%-11s %16s %16s %16s" % (r["row"], out[0], out[1], out[2]))

    with open(OUT, "w") as fh:
        json.dump(recs, fh, indent=1, sort_keys=True)
    print("\nwrote %s" % OUT)


if __name__ == "__main__":
    main()

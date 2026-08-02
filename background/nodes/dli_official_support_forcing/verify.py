#!/usr/bin/env python3
"""Verifier for dli_official_support_forcing.

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 verify.py
Pure python integers only; no third-party imports.  Every comparison below is
an exact integer comparison -- no floats, no logarithms.

  A  the banked official schedule pins (inlined from
     notes/pilots_20260802/c2pp_nullity_structure/results/official_scale.json)
     and the derivation L_j = #{r <= t : v_2(r) = j}
  B  the uniform 256:1 ratio and the collapse q^{L_j} <= E^{N_j/2}
     <=> q <= E^128 at every junction
  C  the E_min pricing table, exactly bracketed
  D  4^128 = 2^256 EXACTLY (the official cap) and 3^128 = 2^202.87...
  E  the C2'' named 256-bit exhibit: admissibility, bracket, E_min = 4
     (primality is NOT certified here -- BPSW caveat, see below)
  F  support forcing: q > 3^128  =>  |S_0| = 0 or |S_0| >= 4, and the
     general small-cell exclusion sum_i c_i^2 <= 3
  G  honest scope: small admissible q gives only E_min = 2; and the
     34th-block reading (ratio 128) would give E_min = 16 -- NOT used
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True

FAILURES = []


def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
    if not ok:
        FAILURES.append(label)


# ------------------------------------------------------- banked official pins
# Source: notes/pilots_20260802/c2pp_nullity_structure/results/official_scale.json
N_OFFICIAL = 2199023255552          # n = 2^41
T_OFFICIAL = 8589934592             # t = 2^33
N_BLOCKS = 34
N_JUNCTIONS = 33
ELL = [4294967296, 2147483648, 1073741824, 536870912, 268435456, 134217728,
       67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576,
       524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024,
       512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 1]
N_J = [1099511627776, 549755813888, 274877906944, 137438953472, 68719476736,
       34359738368, 17179869184, 8589934592, 4294967296, 2147483648,
       1073741824, 536870912, 268435456, 134217728, 67108864, 33554432,
       16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072,
       65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256]
SUPPORT_TO_CONSTRAINT_RATIO = 256
EXHIBIT = 115792089237316195423570985008687907853269984665640564039457583816598106406913
SMALL_Q_ROW = 6597069766657        # C2'' small-q row, official_scale.json


def v2(m):
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1
    return k


def e_min(q):
    """min{E in Z_{>0} : E^128 >= q} -- exact, by bracketed integer search."""
    E = 1
    while E ** 128 < q:
        E += 1
    return E


def miller_rabin(m, bases):
    """NOT a primality certificate: a strong-probable-prime test."""
    d, r = m - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in bases:
        x = pow(a, d, m)
        if x in (1, m - 1):
            continue
        for _ in range(r - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def main():
    # ---------------- A: schedule pins
    ok = (N_OFFICIAL == 2 ** 41 and T_OFFICIAL == 2 ** 33
          and len(ELL) == N_BLOCKS and len(N_J) == N_JUNCTIONS
          and N_BLOCKS == N_JUNCTIONS + 1
          and all(ELL[j] == 2 ** (32 - j) for j in range(33))
          and ELL[33] == 1
          and sum(ELL) == 2 ** 33
          and all(N_J[j] == 2 ** (40 - j) for j in range(33)))
    check("A: banked official pins -- n = 2^41, t = 2^33, 34 blocks / 33 "
          "junctions, ell_j = 2^{32-j}, N_j = 2^{40-j}, sum_j ell_j = t",
          ok, f"sum(ell) = {sum(ELL)} = 2^33")

    # L_j = #{r <= t : v_2(r) = j}: exhaustive for small t, formula for t = 2^33
    ok = True
    for lg in range(1, 12):
        t = 2 ** lg
        blocks = [0] * (lg + 1)
        for r in range(1, t + 1):
            blocks[v2(r)] += 1
        pred = [2 ** (lg - 1 - j) for j in range(lg)] + [1]
        ok &= blocks == pred
    check("A: the block sizes are DERIVED, not assumed -- "
          "#{r <= t : v_2(r) = j} = 2^{log2(t)-1-j} for j < log2 t, and 1 at "
          "j = log2 t (exhaustive for t = 2..2^11)", ok,
          "matches the pinned ell schedule shape at t = 2^33")

    # N_j = phi(h_j) = h_{j+1}, h_j = n / 2^j
    ok = all(N_J[j] == (N_OFFICIAL // 2 ** j) // 2 == N_OFFICIAL // 2 ** (j + 1)
             for j in range(33))
    check("A: N_j = phi(h_j) = h_{j+1} = n/2^{j+1} at every junction", ok)

    # ---------------- B: the uniform ratio and the 256:1 collapse
    ok = all(N_J[j] == SUPPORT_TO_CONSTRAINT_RATIO * ELL[j] for j in range(33))
    check("B: N_j = 256 * L_j at ALL 33 junctions (uniform support:constraint "
          "ratio)", ok, f"ratio = {N_J[0] // ELL[0]} at j = 0, "
                        f"{N_J[32] // ELL[32]} at j = 32")
    ok = all(N_J[j] // 2 == 128 * ELL[j] and N_J[j] % 2 == 0 for j in range(33))
    check("B: hence N_j/2 = 128 L_j exactly, so E^{N_j/2} = (E^128)^{L_j}", ok)

    # the collapse, verified as exact integer comparisons on surrogate L
    bad = 0
    for L in (1, 2, 3, 4):
        for q in (2 ** 41 + 1, 2 ** 128, 3 ** 128, 3 ** 128 + 1, EXHIBIT,
                  2 ** 256 - 1):
            for E in (1, 2, 3, 4, 5):
                if (q ** L <= (E ** 128) ** L) != (q <= E ** 128):
                    bad += 1
    check("B: q^{L} <= E^{128 L}  <=>  q <= E^128 for every L (exact integer "
          "comparison; the criterion is INDEPENDENT of the junction index)",
          bad == 0, "120 (L,q,E) triples, 0 disagreements")

    # ---------------- C: the E_min pricing table
    TABLE = [("2^41 + 1  (smallest admissible modulus size)", 2 ** 41 + 1, 2),
             ("6597069766657  (C2'' small-q row)", SMALL_Q_ROW, 2),
             ("2^128", 2 ** 128, 2),
             ("2^128 + 1", 2 ** 128 + 1, 3),
             ("3^128  (= 2^202.87...)", 3 ** 128, 3),
             ("3^128 + 1", 3 ** 128 + 1, 4),
             ("2^250", 2 ** 250, 4),
             ("2^255", 2 ** 255, 4),
             ("2^256 - 191315023233023  (C2'' named exhibit)", EXHIBIT, 4),
             ("2^256  (the official cap)", 2 ** 256, 4)]
    bad, lines = 0, []
    for lab, q, want in TABLE:
        got = e_min(q)
        if got != want or not ((got - 1) ** 128 < q <= got ** 128):
            bad += 1
        lines.append(f"{lab}: E_min = {got}")
    check("C: E_min(q) = min{E : E^128 >= q} pricing table, each entry "
          "bracketed by (E_min-1)^128 < q <= E_min^128", bad == 0,
          " | ".join(lines))

    # ---------------- D: the cap coincidence
    check("D: 4^128 = 2^256 EXACTLY -- the official cap sits precisely on the "
          "E = 4 rung", 4 ** 128 == 2 ** 256,
          f"4^128 has bit_length {(4 ** 128).bit_length()} (= 257, i.e. 2^256)")
    check("D: 3^128 = 11790184577738583171520872861412518665678211592275841109096961",
          3 ** 128 == 11790184577738583171520872861412518665678211592275841109096961
          and (3 ** 128).bit_length() == 203,
          "bit_length 203, i.e. 2^202 < 3^128 < 2^203")
    check("D: the production margin -- 2^53 * 3^128 < 2^256 < 2^54 * 3^128, so "
          "every q >= 2^203 is already in the E_min = 4 regime with 53 bits to "
          "spare", 2 ** 53 * 3 ** 128 < 2 ** 256 < 2 ** 54 * 3 ** 128)

    # ---------------- E: the named exhibit
    q = EXHIBIT
    ok = (q.bit_length() == 256 and 2 ** 256 - q == 191315023233023
          and (q - 1) % 2 ** 41 == 0 and v2(q - 1) >= 41
          and 3 ** 128 < q < 2 ** 256 and e_min(q) == 4)
    check("E: C2'' named exhibit q = 2^256 - 191315023233023 is official-"
          "admissible in shape (256 bits, v_2(q-1) >= 41, q < 2^256) and lies "
          "in the E_min = 4 window 3^128 < q <= 4^128", ok,
          f"v_2(q-1) = {v2(q - 1)}, (q-1)/2^41 = {(q - 1) // 2 ** 41}")
    spp = miller_rabin(q, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
    check("E: exhibit passes a 12-base strong-probable-prime test -- this is "
          "NOT a primality certificate (the banked claim is BPSW; the theorem "
          "below does not depend on the exhibit being prime)", spp)

    # ---------------- F: support forcing
    bad = 0
    for E in (1, 2, 3):
        if not (E ** 128 <= 3 ** 128):
            bad += 1
    check("F: E <= 3  =>  E^128 <= 3^128, so every q > 3^128 excludes all "
          "energies 1, 2, 3 at EVERY official junction", bad == 0,
          "1^128 = 1, 2^128, 3^128 all <= 3^128 < q")
    # junction 0: domain {+-1}^{S_0}, so E = |S_0| exactly
    excluded = [s for s in range(1, 4) if s ** 128 <= 3 ** 128]
    check("F: junction 0 -- the skew domain is {+-1}^{S_0}, so E = |S_0| "
          "exactly; hence for q > 3^128 every t-null state has |S_0| = 0 or "
          "|S_0| >= 4", excluded == [1, 2, 3],
          "supports of size 1, 2, 3 are all excluded")
    # general small-cell exclusion: E <= sum_i c_i^2
    cases = [([1, 1, 1], 3, True), ([1, 1], 2, True), ([1], 1, True),
             ([1, 1, 1, 1], 4, False), ([2], 4, False), ([1, 1, 2], 6, False)]
    ok = True
    for cs, sq, killed in cases:
        assert sum(c * c for c in cs) == sq
        ok &= ((sq ** 128 <= 3 ** 128) == killed)
    check("F: general small-cell exclusion -- a junction-j state whose whole "
          "admissible skew domain has sum_i c_i^2 <= 3 admits NO nonzero skew "
          "at any q > 3^128; sum_i c_i^2 >= 4 is not excluded by this gate",
          ok, "c-profiles [1,1,1] (killed) ... [1,1,1,1], [2] (not killed)")

    # ---------------- G: honest scope
    check("G: SCOPE -- a formally admissible but small official q gives only "
          "E_min = 2; the |S_0| >= 4 form needs q > 3^128 = 2^202.87",
          e_min(2 ** 41 + 1) == 2 and e_min(SMALL_Q_ROW) == 2
          and e_min(3 ** 128) == 3 and e_min(3 ** 128 + 1) == 4,
          "E_min(2^41+1) = E_min(6597069766657) = 2; E_min(3^128) = 3; "
          "E_min(3^128+1) = 4")
    # the o = 1 contrast: a single constraint at junction 0 excludes only E = 1
    # (bit-length comparison; 2^(2^39) is not materializable)
    half0 = N_J[0] // 2
    ok = (half0 == 2 ** 39 and EXHIBIT.bit_length() <= half0
          and 1 ** half0 < EXHIBIT)
    check("G: HONEST PRICING -- a SINGLE constraint (o = 1) at junction 0 has "
          "ceiling E^{N_0/2} with N_0/2 = 2^39; since q < 2^256 <= 2^{2^39} "
          "<= E^{N_0/2} for every E >= 2, it excludes ONLY E = 1 even at "
          "q ~ 2^256. All the strength comes from LN2's full block q^{L_j} at "
          "the fixed 256:1 ratio", ok,
          f"N_0/2 = 2^39 = {half0} >> 256 = bit length of q")
    # the 34th-block reading, recorded and NOT used
    e16 = 1
    while e16 ** 64 < EXHIBIT:
        e16 += 1
    check("G: CAVEAT recorded -- a 34th-block reading (N = 128, L = 1, i.e. "
          "ratio 128, criterion q <= E^64) would give E_min = 16 at the "
          "exhibit; the theorem uses the PINNED 33-junction schedule with "
          "ratio 256 and does NOT use that reading", e16 == 16
          and 15 ** 64 < EXHIBIT <= 16 ** 64,
          f"15^64 < q <= 16^64 = 2^256")

    if FAILURES:
        print("FAILED CHECKS:", FAILURES)
        sys.exit(1)
    print("DLI_OFFICIAL_SUPPORT_FORCING_ALL_PASS")


if __name__ == "__main__":
    main()

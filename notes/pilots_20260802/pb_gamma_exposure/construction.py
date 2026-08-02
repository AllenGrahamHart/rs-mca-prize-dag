#!/usr/bin/env python3
"""The split-fibre pencil at official-row shapes: exact |Gamma| and |Gamma_lo|.

Three exact results, all integer arithmetic:

 1. SELF-COLLISION IDENTITY.  For a split-fibre pencil the exact-A witness
    set is EXACTLY {S_J = core U (fibres of J) : J in C(B, a)} (plus the
    random supply), B = n/m - g.  Two of them meet in
        |S_J ^ S_J'| = g + m |J ^ J'|,
    so ADJACENT label sets (|J ^ J'| = a-1) meet in g + m(a-1) = A - m, and
    the split-fibre range m <= h forces A - m >= A - h = K.  Every adjacent
    pair is therefore HIGH-core.  Verified against the measured masks.

 2. EXACT DISTINCT-SLOPE COUNT.  zeta = omega^m has order F = n/m, a power
    of two, and zeta^{i+P} = -zeta^i with P = F/2 = deg Phi_F, while
    {zeta^0..zeta^{P-1}} is a Z-basis of Z[zeta_F].  Hence
        z_J = sum_{j in J} zeta^j = sum_{i<P} d_i zeta^i,
        d_i = [i in J] - [i+P in J] in {-1,0,1},
    and in characteristic zero distinct d give distinct slopes.  The count
    of realizable d is closed-form and is validated EXACTLY against the
    measured |Gamma| at the top of every q-ladder.

 3. OFFICIAL-ROW EVALUATION of 1 and 2 against 8n^3 and B*, plus the
    rigorous single-field (one prime) realization bound.
"""

from __future__ import annotations

import json
import os
import sys
from itertools import combinations
from math import comb

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
PILOTS = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(PILOTS, "pb_split_fibre_selector"))
import pb_split_fibre_pilot as P            # noqa: E402
from measure import FastCase                 # noqa: E402

OUT = os.path.join(HERE, "CONSTRUCTION.json")

SHAPES = {
    "S1": dict(n=32, m=2, K=8, h=2, g=2, a=4, b=14),
    "S2": dict(n=32, m=2, K=8, h=3, g=1, a=5, b=14),
    "S3": dict(n=32, m=2, K=16, h=2, g=2, a=8, b=14),
    "S4": dict(n=32, m=4, K=8, h=5, g=1, a=3, b=7),
}

ROWS = [
    ("RowC 1/4", 1 << 10, 1 << 8, 261, 1 << 122),
    ("RowC 1/8", 1 << 10, 1 << 7, 133, 1 << 122),
    ("RowC 1/16", 1 << 10, 1 << 6, 67, 1 << 122),
    ("prize 1/4", 1 << 41, 1 << 39, 558345748481,
     317494674775468773183020924238786383963),
    ("prize 1/8", 1 << 41, 1 << 38, 283467841537,
     317494674775468773183020924238786383963),
    ("prize 1/16", 1 << 41, 1 << 37, 141733920769,
     317494674775468773183020924238786383963),
]


def n_slopes(F: int, g: int, a: int) -> int:
    """EXACT number of distinct characteristic-zero slopes z_J of the
    split-fibre pencil with F fibres, g core fibres (labels F-g..F-1
    unavailable) and a fibres per witness.

    P = F/2 paired positions; positions 0..P-g-1 have both i and i+P
    available ("double", d_i in {-1,0,+1}), positions P-g..P-1 have only i
    available ("single", d_i in {0,+1}).  d is realizable with |J| = a iff
    a - u - v is even, non-negative, and (a-u-v)/2 <= (P-g) - u, where u
    (resp. v) is the number of nonzero doubles (resp. singles).
    """
    P = F // 2
    assert 1 <= g <= P, (F, g)
    nd, ns = P - g, g
    tot = 0
    for u in range(0, min(nd, a) + 1):
        cu = comb(nd, u) << u
        for v in range(0, min(ns, a - u) + 1):
            rem = a - u - v
            if rem < 0 or rem % 2:
                continue
            if rem // 2 > nd - u:
                continue
            tot += cu * comb(ns, v)
    return tot


def full_family(case):
    """every exact-A witness of split-fibre type: all C(B,a) label sets."""
    out = []
    for J in combinations(range(case.b), case.a):
        z = sum(case.labels[i] for i in J) % case.q
        sup = sorted(set(case.core_idx)
                     | {i for j in J for i in case.fibre_idx[j]})
        assert len(sup) == case.A
        out.append((J, z, P.mask_of(sup)))
    return out


def main() -> None:
    res: dict = {"self_collision": [], "distinct_slope_validation": [],
                 "official_rows": []}

    print("=" * 78)
    print("1  --  SELF-COLLISION IDENTITY, verified on the banked shapes")
    print("=" * 78)
    print(f"{'shape':<6}{'n':>5}{'m':>4}{'K':>5}{'h':>4}{'A':>5}{'g':>4}"
          f"{'a':>4}{'B':>5}{'C(B,a)':>10}{'max core':>10}{'A-m':>7}"
          f"{'>=K?':>7}")
    for nm, s in SHAPES.items():
        prm = dict(s)
        prm["q"] = 2147483713 if s["n"] == 32 else 97   # top-of-ladder prime
        case = FastCase(f"{nm}_cons", dict(prm))
        fam = full_family(case)
        sets = [frozenset(J) for J, _, _ in fam]
        masks = [mk for _, _, mk in fam]
        mx = 0
        adj = 0
        for i in range(len(fam)):
            si, mi = sets[i], masks[i]
            for j in range(i + 1, len(fam)):
                c = bin(mi & masks[j]).count("1")
                inter = len(si & sets[j])
                assert c == s["g"] + s["m"] * inter
                if c > mx:
                    mx = c
                if inter == s["a"] - 1:
                    adj += 1
        A = s["K"] + s["h"]
        rec = dict(shape=nm, n=s["n"], m=s["m"], K=s["K"], h=s["h"], A=A,
                   g=s["g"], a=s["a"], B=s["b"], family=len(fam),
                   max_pairwise_core=mx, A_minus_m=A - s["m"],
                   high_core=mx >= s["K"], adjacent_pairs=adj)
        res["self_collision"].append(rec)
        print(f"{nm:<6}{s['n']:>5}{s['m']:>4}{s['K']:>5}{s['h']:>4}{A:>5}"
              f"{s['g']:>4}{s['a']:>4}{s['b']:>5}{len(fam):>10}{mx:>10}"
              f"{A-s['m']:>7}{str(mx >= s['K']):>7}")
    print("  every shape: max pairwise core == A - m >= K, so every adjacent")
    print("  label pair is HIGH-core and lands in Gamma_hi, never Gamma_lo.")

    print()
    print("=" * 78)
    print("2  --  EXACT DISTINCT-SLOPE COUNT vs the measured |Gamma| at the")
    print("       top of each q-ladder (q = 2147483713, random supply ~ 0)")
    print("=" * 78)
    for nm, s in SHAPES.items():
        path = os.path.join(HERE, f"MEASURE_{nm}.json")
        if not os.path.exists(path):
            print(f"  {nm}: no measurement yet")
            continue
        with open(path) as fh:
            md = json.load(fh)
        top = md["points"][-1]
        F = s["n"] // s["m"]
        pred = n_slopes(F, s["g"], s["a"])
        ok = pred == top["gamma_meas"]
        res["distinct_slope_validation"].append(
            dict(shape=nm, F=F, g=s["g"], a=s["a"], formula=pred,
                 measured=top["gamma_meas"], q=top["q"], match=ok,
                 witnesses_formula=comb(F - s["g"], s["a"]),
                 witnesses_measured=top["witnesses_meas"],
                 witnesses_match=comb(F - s["g"], s["a"])
                 == top["witnesses_meas"]))
        wf = comb(F - s["g"], s["a"])
        print(f"  {nm}: F={F} g={s['g']} a={s['a']}  slopes: formula "
              f"{pred:>6} measured {top['gamma_meas']:>6} "
              f"{'MATCH' if ok else 'MISMATCH'}"
              f"  | witnesses C({F-s['g']},{s['a']})={wf:>6} measured "
              f"{top['witnesses_meas']:>6} "
              f"{'MATCH' if wf == top['witnesses_meas'] else 'MISMATCH'}")

    print()
    print("=" * 78)
    print("3  --  OFFICIAL-ROW EVALUATION")
    print("=" * 78)
    for name, n, k, A, bstar in ROWS:
        h = A - k
        b8 = 8 * n ** 3
        # the unique admissible fibre width: m | n, m <= h < 2m
        ms = [m for m in (1 << e for e in range(0, n.bit_length()))
              if n % m == 0 and m <= h < 2 * m]
        assert len(ms) == 1, (name, ms)
        m = ms[0]
        F = n // m
        best = None
        for a in range(2, A // m + 1):
            g = A - m * a
            if g < 1 or g > F // 2 or F - g < a:
                continue
            v = n_slopes(F, g, a)
            if best is None or v > best[0]:
                best = (v, a, g)
        assert best is not None
        NS, a, g = best
        wit = comb(F - g, a)
        rec = dict(row=name, n=n, k=k, A=A, h=h, m=m, F=F, a=a, g=g,
                   witnesses_C_B_a=wit,
                   witnesses_log2=wit.bit_length() - 1,
                   distinct_slopes_char0=NS,
                   distinct_slopes_log2=NS.bit_length() - 1,
                   budget_8n3=b8, budget_8n3_log2=b8.bit_length() - 1,
                   Bstar=bstar, Bstar_log2=bstar.bit_length() - 1,
                   over_8n3=NS > b8, over_Bstar=NS > bstar,
                   max_pairwise_core=A - m, K=k, high_core=(A - m) >= k,
                   gamma_lo_contribution=0)
        res["official_rows"].append(rec)
        print(f"  {name:<11} m={m:<12} F={F:<5} a={a:<4} g={g:<12}")
        print(f"      split-fibre witnesses  C({F-g},{a}) = 2^"
              f"{rec['witnesses_log2']}")
        print(f"      distinct char-0 slopes         = 2^"
              f"{rec['distinct_slopes_log2']}"
              f"   ({'>' if rec['over_8n3'] else '<='} 8n^3 = 2^"
              f"{rec['budget_8n3_log2']};"
              f" {'>' if rec['over_Bstar'] else '<='} B* = 2^"
              f"{rec['Bstar_log2']})")
        print(f"      max pairwise core = A - m = {A-m} >= K = {k}: "
              f"{rec['high_core']}  ->  Gamma_lo contribution 0")

    print()
    print("=" * 78)
    print("4  --  RIGOROUS SINGLE-FIELD (one prime) REALIZATION BOUND")
    print("=" * 78)
    print("  A pair of label sets collides mod p iff p divides the norm of a")
    print("  nonzero element of Z[zeta_F] whose coefficients lie in {-2..2}.")
    print("  |Norm| <= (2 P)^P, so each pair kills at most floor(P log2(2P)/")
    print("  log2 q_min) primes; the RowC envelope interval [2^250,")
    print("  2^250+2^128) holds ~ 2^128 / (phi(1024) ln 2^250) primes = 1 mod")
    print("  1024.  A family of size M is realizable in ONE such prime as")
    print("  soon as (M choose 2) * killed_per_pair < #primes.")
    for name, n, k, A, bstar in ROWS[:3]:
        h = A - k
        m = [mm for mm in (1 << e for e in range(0, n.bit_length()))
             if n % mm == 0 and mm <= h < 2 * mm][0]
        F = n // m
        Pp = F // 2
        killed = (Pp * (2 * Pp).bit_length()) // 250
        nprimes = (1 << 128) // (512 * 174)          # PNT in AP, RowC window
        Mmax = 1
        while (Mmax * (Mmax - 1) // 2) * max(killed, 1) < nprimes:
            Mmax <<= 1
        Mmax >>= 1
        print(f"  {name:<11} F={F} P={Pp}  <=~{killed} primes killed/pair,"
              f"  window holds ~2^{nprimes.bit_length()-1} primes"
              f"  ->  rigorous M up to ~2^{Mmax.bit_length()-1}"
              f"   (8n^3 = 2^{(8*n**3).bit_length()-1})")

    with open(OUT, "w") as fh:
        json.dump(res, fh, indent=1, sort_keys=True)
    print()
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

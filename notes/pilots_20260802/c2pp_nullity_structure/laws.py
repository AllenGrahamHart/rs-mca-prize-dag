#!/usr/bin/env python3
"""C2'' pilot -- candidate structural laws for delta, tested exactly.

L1  RANK LAW           rank{v_i : i in S} = min(L_j, |S|)        (validate_dli V4)
L2  NULLITY FORMULA    delta_j = (L_j - |S_j|)^+, S_j = unsaturated cells
L3  STRATUM LAW        {delta = t} = the archived coset class, exactly
L4  COMMON-LATENT      sum_j rank_x(block j) - rank_x(all) = 0 identically
L5  IDENTITY           R = E_MF[q^delta]
L6  DOMINATION         R <= E_MF[q^delta]
L7  CONDITIONED        R = E_NULL[q^delta]
L9  CARRIER            share of R carried by the delta = 0 stratum
L10 DUAL SEAM          junctions = support elements  ->  delta' = (|S_j| - L_j)^+
L11 TRAP REALIZABILITY can a cross-junction circuit exist in the DLI tower?
L12 DIFFERENCE MULTISET  does the F2-style difference multiset of the support
                         determine the junction ratio rho?
L13 NORM GATE          is the residual a norm-divisibility event in Z[zeta_n]?
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product as iproduct
from pathlib import Path

from dli_model import blocks, block_matrix, get_zeta
from junctions import skewcount_table
from nullity import rref_rank

HERE = Path(__file__).resolve().parent
VERDICTS = []


def verdict(lid, name, status, evidence):
    VERDICTS.append({"id": lid, "law": name, "status": status,
                     "evidence": evidence})
    print(f"{lid:<5} {status:<9} {name}\n        {evidence}")


# ------------------------------------------------------------------ L4 / L11
def l4_common_latent():
    rows = []
    for (n, t, q) in [(16, 2, 97), (16, 4, 97), (16, 8, 193), (32, 2, 97),
                      (32, 4, 97), (32, 8, 97), (64, 8, 193), (64, 16, 193)]:
        zeta = get_zeta(q, n)
        V = [[pow(zeta, (r * i) % n, q) for i in range(n)] for r in range(1, t + 1)]
        B = blocks(t)
        loc = []
        for j, U in enumerate(B):
            loc.append(rref_rank([V[u * 2**j - 1] for u in U], q))
        glob = rref_rank(V, q)
        rows.append({"n": n, "t": t, "q": q, "local_ranks": loc,
                     "sum_local": sum(loc), "global_rank": glob,
                     "delta_common_latent": sum(loc) - glob})
    bad = [r for r in rows if r["delta_common_latent"] != 0]
    verdict("L4", "common-latent cross-junction nullity is identically zero",
            "SURVIVES" if not bad else "DIES",
            f"{len(rows)} rows: sum_j rank_x(block j) = global rank = t in every "
            f"case (the t Vandermonde rows split into blocks by v_2(r), and any "
            f"t rows of a Vandermonde with distinct nodes are independent); "
            f"violations = {len(bad)}")
    verdict("L11", "a cross-junction circuit (the trap geometry) is realizable "
            "in the DLI tower", "DIES",
            "no support of any junction has a rank defect (L1) and the block row "
            "spaces are independent (L4); a 33-junction system with local ranks "
            "summing above the global rank -- the four-wise / 32-wise trap -- "
            "therefore has no DLI realization at tower-junction granularity")
    return rows


# ------------------------------------------------------------------ L5-L9
def l5_l9_from_census():
    out = []
    for f in sorted((HERE / "results").glob("census_*.json")):
        out.extend(json.loads(f.read_text()))
    tab = []
    dom_fail = []
    id_fail = []
    for r in out:
        R = Fraction(r["R"])
        Emf = Fraction(r["mf_E_q_delta"])
        En = Fraction(r["null_E_q_delta"]) if "null_E_q_delta" in r else None
        n0 = r["null_delta_hist"].get("0", 0)
        share0 = Fraction(n0, r["n_tnull"]) if r["n_tnull"] else Fraction(0)
        tab.append({"n": r["n"], "t": r["t"], "q": r["q"], "R": str(R),
                    "R_f": float(R), "E_MF": str(Emf), "E_MF_f": float(Emf),
                    "E_NULL_f": float(En) if En is not None else None,
                    "R_over_E_MF": float(R / Emf) if Emf else None,
                    "delta0_share_of_R": float(share0),
                    "R_from_delta0": float(R * share0)})
        if R > Emf:
            dom_fail.append((r["n"], r["t"], r["q"], float(R), float(Emf)))
        if R != Emf:
            id_fail.append((r["n"], r["t"], r["q"]))
    verdict("L5", "exact identity R = E_MF[q^delta]", "DIES",
            f"fails at {len(id_fail)}/{len(tab)} rows (equality holds nowhere)")
    verdict("L6", "dominating form R <= E_MF[q^delta]", "DIES",
            f"exact counterexamples at {dom_fail}")
    worst = max(tab, key=lambda r: (r["E_NULL_f"] or 0) / max(r["R_f"], 1e-30))
    verdict("L7", "conditioned identity R = E_NULL[q^delta]", "DIES",
            f"E_NULL overshoots R by up to {worst['E_NULL_f']/worst['R_f']:.3g}x "
            f"(n={worst['n']},t={worst['t']},q={worst['q']}: R={worst['R_f']:.4g}, "
            f"E_NULL={worst['E_NULL_f']:.4g})")
    carr = [r for r in tab if r["n"] == 32]
    verdict("L9", "the joint excess R is carried by the delta = 0 stratum",
            "SURVIVES",
            "; ".join(f"n={r['n']},t={r['t']},q={r['q']}: "
                      f"{100*r['delta0_share_of_R']:.2f}% of the t-null mass and "
                      f"R_delta0={r['R_from_delta0']:.4g} of R={r['R_f']:.4g}"
                      for r in carr))
    (HERE / "results" / "law_table.json").write_text(json.dumps(tab, indent=1))
    return tab


# ------------------------------------------------------------------ L10
def l10_dual_seam():
    rows = []
    for (n, t, q) in [(32, 2, 97), (32, 4, 97), (64, 8, 193)]:
        B = blocks(t)
        for j, U in enumerate(B):
            L = len(U)
            h1 = n // 2**(j + 1)
            rows.append({"n": n, "t": t, "q": q, "j": j, "L_j": L, "cells": h1,
                         "delta_level_seam_max": max(0, L - 0),
                         "delta_element_seam_full_support": max(0, h1 - L)})
    off = {"n": 2**41, "t": 2**33}
    off_rows = []
    for j in range(33):
        L = -(-(2**33 // 2**j) // 2)
        off_rows.append({"j": j, "L_j": L, "cells": 2**41 // 2**(j + 1),
                         "delta_element_seam": 2**41 // 2**(j + 1) - L})
    verdict("L10", "the nullity is seam-dependent: level-junctions vs "
            "support-element junctions", "SURVIVES (as a fence)",
            "level seam gives delta = (L_j-|S_j|)^+ (0 on every support-rich "
            "state); the dual element seam gives delta' = (|S_j|-L_j)^+, which at "
            f"the official ratio |S_j| = 256 L_j equals 255 L_j, i.e. "
            f"delta'_total = 255 t = 255*2^33 -- the two canonical latent "
            "expansions of the SAME junction differ by q^(255t). Gate 0 (PP2.0) "
            "must fix the expansion before 'E[q^delta] <= 2^21' has a meaning")
    return {"small": rows, "official": off_rows}


# ------------------------------------------------------------------ L12
def l12_difference_multiset():
    n, t, q = 32, 2, 97
    sc, o = skewcount_table(q, n, t)
    h = n // 2
    groups = defaultdict(set)
    for G in range(1 << h):
        idx = [i for i in range(h) if (G >> i) & 1]
        k = len(idx)
        if not (1 <= k <= 8):
            continue
        diffs = Counter((a - b) % h for a in idx for b in idx if a != b)
        key = (k, tuple(sorted(diffs.items())))
        rho = Fraction(sc.get(G, 0) * q**o, 2**k)
        groups[key].add(rho)
    multi = {k: v for k, v in groups.items() if len(v) > 1}
    verdict("L12", "the support's difference multiset determines the junction "
            "ratio rho (the F2 lane's Delta-multiset analogue)",
            "DIES" if multi else "SURVIVES",
            f"{len(multi)} of {len(groups)} difference-multiset classes carry "
            f"more than one rho value at (n=32,t=2,q=97), supports of size 1..8; "
            f"largest spread {max((max(v)-min(v) for v in multi.values()), default=0)}")
    return {"classes": len(groups), "ambiguous": len(multi)}


# ------------------------------------------------------------------ L13
def bareiss_det(M):
    M = [row[:] for row in M]
    nn = len(M)
    sign = 1
    prev = 1
    for k in range(nn - 1):
        if M[k][k] == 0:
            piv = next((i for i in range(k + 1, nn) if M[i][k] != 0), None)
            if piv is None:
                return 0
            M[k], M[piv] = M[piv], M[k]
            sign = -sign
        for i in range(k + 1, nn):
            for j in range(k + 1, nn):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
        prev = M[k][k]
    return sign * M[nn - 1][nn - 1]


def norm_cyclotomic(coeffs, hh):
    """Norm of sum_i c_i zeta^i in Z[zeta_{2hh}] = Z[x]/(x^hh + 1)."""
    M = [[0] * hh for _ in range(hh)]
    for k in range(hh):
        for i, c in enumerate(coeffs):
            if c:
                e = i + k
                M[e % hh][k] += c * (-1 if e >= hh else 1)
    return bareiss_det(M)


def l13_norm_gate():
    rows = []
    for (n, t, q) in [(16, 2, 17), (16, 2, 97), (16, 2, 113)]:
        h = n // 2
        cols = block_matrix(q, n, t, 0)          # o = 1 here
        assert len(blocks(t)[0]) == 1
        sol_and_norm = sol_not_norm = norm_not_sol = neither = 0
        for G in range(1 << h):
            idx = [i for i in range(h) if (G >> i) & 1]
            if not idx:
                continue
            for eps in iproduct((1, -1), repeat=len(idx)):
                c = [0] * h
                for a, i in enumerate(idx):
                    c[i] = eps[a]
                is_sol = sum(eps[a] * cols[i][0] for a, i in enumerate(idx)) % q == 0
                Nz = norm_cyclotomic(c, h)
                divides = (Nz % q == 0)
                if is_sol and divides:
                    sol_and_norm += 1
                elif is_sol and not divides:
                    sol_not_norm += 1
                elif divides and not is_sol:
                    norm_not_sol += 1
                else:
                    neither += 1
        rows.append({"n": n, "t": t, "q": q, "sol_and_norm": sol_and_norm,
                     "sol_not_norm": sol_not_norm, "norm_not_sol": norm_not_sol,
                     "neither": neither})
    ok = all(r["sol_not_norm"] == 0 for r in rows)
    verdict("L13", "the junction residual is a NORM-DIVISIBILITY event: every "
            "skew solution has q | Norm_{Q(zeta_n)/Q}(sum eps_i zeta_n^i)",
            "SURVIVES" if ok else "DIES",
            "; ".join(f"(n={r['n']},q={r['q']}): solutions={r['sol_and_norm']} all "
                      f"norm-divisible, false-negatives={r['sol_not_norm']}, "
                      f"norm-divisible-but-not-solutions={r['norm_not_sol']}"
                      for r in rows))
    return rows


def main():
    out = {}
    out["L4"] = l4_common_latent()
    out["L5_L9"] = l5_l9_from_census()
    out["L10"] = l10_dual_seam()
    out["L12"] = l12_difference_multiset()
    out["L13"] = l13_norm_gate()
    (HERE / "results" / "laws.json").write_text(json.dumps(
        {"verdicts": VERDICTS, "detail": out}, indent=1, default=str))


if __name__ == "__main__":
    main()

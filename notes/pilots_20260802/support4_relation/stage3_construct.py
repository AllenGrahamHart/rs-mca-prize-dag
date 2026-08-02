#!/usr/bin/env python3
"""STAGE 3 -- CONSTRUCT: an ADMISSIBLE pairwise-intersecting ray system that
carries a support-4 relation.

Build the U-mechanism family (s4lib.build_mobius_family), solve the linear
system for a received pair (u,v), then run the FULL banked occlib gate scan:
below cascade, globally generic, tangent-free at every finite slope AND in
the (0:1) direction, v non-vanishing, k-packing.

Also measures, from the realised (u,v):  the live rays, the C(V,2) band data
at depth d, the family rank and the exact deficit.

Run: tools/ramguard local -- python3 stage3_construct.py
"""
from __future__ import annotations

import itertools
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import s4lib as S                                              # noqa: E402
import tslib as T                                              # noqa: E402

CHECKS, FAIL = [0], []


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    print(("PASS " if ok else "FAIL ") + label + (("  | " + detail)
                                                 if detail else ""))
    if not ok:
        FAIL.append(label)
    return ok


def try_fixture(cs, seeds=(1, 2, 3, 5, 7, 11, 13, 17, 19, 23)):
    k, h, d, V, q = cs["k"], cs["h"], cs["d"], cs["V"], cs["q"]
    priv = (h - 1) - (V - 1) * d
    n = (k + 2) + (V * (V - 1) // 2) * d + V * priv + cs.get("free", 2)
    row = T.Row2(n, k, h, q)
    out = []
    for fseed in seeds:
        fam = S.build_mobius_family(row, d, V, seed=fseed)
        if fam is None:
            continue
        sup, zs = fam["supports"], fam["slopes"]
        dim, rels, _ = S.relation_space(row, sup, zs)
        if dim != V - 3:
            continue
        for rseed in seeds:
            uv = S.realise_family(row, sup, zs, seed=rseed)
            if uv is None:
                continue
            u, v = uv
            rec, pairs, band = S.gate_report(row, u, v,
                                             name=f"s4_{k}_{h}_{d}_{V}")
            out.append((row, fam, u, v, rec, pairs, band, fseed, rseed, dim))
            if rec["FULL_GATE"]:
                return row, fam, u, v, rec, pairs, band, fseed, rseed, dim, out
    if out:
        return out[0] + (out,)
    return None


def main():
    res = []
    CASES = [dict(k=3, h=5, d=1, V=4, q=6421),
             dict(k=3, h=7, d=2, V=4, q=10007),
             dict(k=4, h=6, d=1, V=4, q=6421),
             dict(k=5, h=6, d=1, V=4, q=10007),
             dict(k=3, h=8, d=1, V=4, q=10007),
             dict(k=4, h=8, d=2, V=4, q=10007)]
    for cs in CASES:
        k, h, d, V, q = cs["k"], cs["h"], cs["d"], cs["V"], cs["q"]
        got = try_fixture(cs)
        tag = f"k={k} h={h} d={d} V={V}"
        if got is None:
            chk(f"D0 {tag}: fixture realises", False)
            continue
        row, fam, u, v, rec, pairs, band, fs, rs, dim, allout = got
        n = row.n
        tag = f"k={k} h={h} d={d} V={V} n={n}"
        sup, zs = fam["supports"], fam["slopes"]

        chk(f"D1 {tag}: FULL banked gate (below cascade, globally generic, "
            f"tangent-free finite + (0:1), v non-vanishing, k-packing)",
            rec["FULL_GATE"],
            f"cascade={rec['below_cascade']} generic={rec['globally_generic']} "
            f"tanfin={rec['tangent_free_finite_slopes']} "
            f"tanv={rec['tangent_free_v_direction']} "
            f"vnz={rec['v_nonvanishing']} kpack={rec['kpacking_ok']} "
            f"maxJ={rec['max_joint_agreement']} A={row.A} "
            f"maxray={rec['max_ray_agreement']} vmax={rec['max_v_side_agreement']} "
            f"kpmax={rec['kpacking_max_intersection']}")

        # the intended rays are live with exactly the intended supports
        live = {}
        for Zf, p, dd, sl in band:
            for z in sl:
                live[(z, frozenset(p["supports"][z]))] = dd
        want = [(zs[a], frozenset(sup[a])) for a in range(V)]
        chk(f"D2 {tag}: the {V} designed rays are live with exactly the "
            f"designed supports", all(w in live for w in want),
            f"found={sum(1 for w in want if w in live)}/{V}")

        # the C(V,2) data at depth d
        fam_meas = []
        for Zf, p, dd, sl in band:
            if dd == d and len(sl) >= 2:
                fam_meas.append((tuple(sorted(Zf)),
                                 [(z, tuple(sorted(p["supports"][z])))
                                  for z in sl]))
        M = V * (V - 1) // 2
        chk(f"D3 {tag}: M = C(V,2) = {M} band data at depth {d}",
            len(fam_meas) == M, f"M_measured={len(fam_meas)}")

        rank = S.family_rank(row, sup, zs)
        chk(f"D4 {tag}: rank = Vh - (V-3) = {V*h-(V-3)}, deficit = {V-3} "
            f"(the relation is REAL)",
            rank == V * h - (V - 3) and dim == V - 3,
            f"rank={rank} Vh={V*h} dim Rel={dim}")

        # realisability margin
        Tset = set()
        for s_ in sup:
            Tset |= set(s_)
        m = len(Tset) - k
        chk(f"D5 {tag}: non-collapse rank <= 2m-1 = {2*m-1}", rank <= 2 * m - 1,
            f"rank={rank} m={m} slack={2*m-1-rank}")

        res.append(dict(cs=cs, n=n, seeds=(fs, rs), FULL_GATE=rec["FULL_GATE"],
                        ADMISSIBLE=rec["ADMISSIBLE"],
                        below_cascade=rec["below_cascade"],
                        globally_generic=rec["globally_generic"],
                        tangent_free=rec["tangent_free_finite_slopes"],
                        tangent_free_v=rec["tangent_free_v_direction"],
                        kpacking_ok=rec["kpacking_ok"],
                        kpacking_max=rec["kpacking_max_intersection"],
                        max_joint=rec["max_joint_agreement"], A=row.A,
                        max_ray=rec["max_ray_agreement"],
                        vmax=rec["max_v_side_agreement"],
                        n_rays=rec["n_rays"], N_total=rec["N_total"],
                        M_measured=len(fam_meas), rank=rank, Vh=V * h,
                        deficit=V * h - rank,
                        charge_per_ray=rank / V,
                        charge_per_datum=rank / M,
                        slopes=zs, supports=[list(s_) for s_ in sup],
                        U=fam["U"], ys=fam["ys"],
                        ledger=rec["ledger_by_depth"]))

    with open(os.path.join(HERE, "stage3_construct.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    print(f"\n{CHECKS[0]} checks, {len(FAIL)} FAIL")
    for f in FAIL:
        print("  FAIL:", f)


if __name__ == "__main__":
    main()

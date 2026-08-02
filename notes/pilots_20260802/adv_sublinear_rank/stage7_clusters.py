#!/usr/bin/env python3
"""STAGE 7 -- do several K_V clusters sharing one (k-1)-set Y add up?

The toy-row arithmetic uses  clusters * C(V,2)  data for  clusters * V h
rank and  clusters * [C(V,2)(d+1) + V tau]  points on top of ONE shared Y.
This checks additivity and admissibility for 2 and 3 clusters.
"""
from __future__ import annotations
import json, os, random, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import advlib as A
import tslib as T
import occlib

FAIL, CH = [], [0]
def chk(l, ok, det=""):
    CH[0] += 1
    print(("PASS " if ok else "FAIL ") + l + (("  | " + det) if det else ""))
    if not ok: FAIL.append(l)

def build_multi(row, d, V, ncl, seed=0):
    """ncl K_V clusters sharing the same Y."""
    rnd = random.Random(seed)
    n, k, h, q = row.n, row.k, row.h, row.q
    tau = (h + 1) - (V - 1) * (d + 1)
    if tau < 0: return None
    M = V * (V - 1) // 2
    need = (k - 1) + ncl * (M * (d + 1) + V * tau)
    if need > n: return None
    pts = list(range(n)); Y = pts[:k-1]; cur = k-1
    f = tuple(rnd.randrange(q) for _ in range(k))
    g = tuple(rnd.randrange(q) for _ in range(k))
    VY = A.vanish_poly(row, Y)
    u = [None]*n; v = [None]*n
    for i in Y:
        u[i] = row.ev(f, row.xs[i]); v[i] = row.ev(g, row.xs[i])
    supports, zsall, cores = [], [], []
    for c in range(ncl):
        geo = A.lines_general_position(q, V, rnd)
        if geo is None: return None
        zs, cs, P = geo
        keys = [(a,b) for a in range(V) for b in range(a+1,V)]
        petal = {}
        for key in keys:
            petal[key] = pts[cur:cur+d+1]; cur += d+1
        block = {}
        for a in range(V):
            block[a] = pts[cur:cur+tau]; cur += tau
        for key in keys:
            al, be = P[key]
            fab = A.add_poly(f, A.scal_poly(VY, al, q), q)
            gab = A.add_poly(g, A.scal_poly(VY, be, q), q)
            for i in petal[key]:
                u[i] = row.ev(fab, row.xs[i]); v[i] = row.ev(gab, row.xs[i])
            cores.append(tuple(sorted(Y + petal[key])))
        for a in range(V):
            psi = A.add_poly(A.add_poly(f, A.scal_poly(g, zs[a], q), q),
                             A.scal_poly(VY, cs[a], q), q)
            for x in block[a]:
                vx = rnd.randrange(1, q)
                u[x] = (row.ev(psi, row.xs[x]) - zs[a]*vx) % q; v[x] = vx
            S = set(Y) | set(block[a])
            for key in keys:
                if a in key: S |= set(petal[key])
            supports.append(tuple(sorted(S))); zsall.append(zs[a])
    for i in range(n):
        if u[i] is None:
            u[i] = rnd.randrange(q); v[i] = rnd.randrange(1, q)
    return u, v, supports, zsall, cores, cur

def main():
    res = []
    for cs in [dict(k=3,h=5,d=1,V=4,q=6421,ncl=2),
               dict(k=3,h=5,d=1,V=4,q=6421,ncl=3),
               dict(k=3,h=7,d=1,V=5,q=6421,ncl=2),
               dict(k=4,h=5,d=1,V=4,q=6421,ncl=2)]:
        k,h,d,V,q,ncl = cs["k"],cs["h"],cs["d"],cs["V"],cs["q"],cs["ncl"]
        tau = (h+1)-(V-1)*(d+1); M = V*(V-1)//2
        n = max((k-1)+ncl*(M*(d+1)+V*tau), k+h+2)
        row = T.Row2(n,k,h,q)
        got = None
        for seed in range(6):
            b = build_multi(row,d,V,ncl,seed=seed)
            if b is None: continue
            u,v,S,zs,cores,used = b
            rec,_,band = occlib.measure(row,u,v,name="multi",want_checks=True)
            if rec["ADMISSIBLE"]: got=(u,v,S,zs,cores,used,rec,band); break
            got=(u,v,S,zs,cores,used,rec,band)
        if got is None:
            print(f"SKIP {cs}"); continue
        u,v,S,zs,cores,used,rec,band = got
        rows=[]
        for a,s in enumerate(S): rows += T.ray_rows(row,s,zs[a])
        rk = T.rank_mod(rows,q)
        fam = A.measured_family(row,band,d)
        frk = A.family_rank_two_rays(row,fam) if fam else 0
        Nd = rec["ledger_by_depth"].get(str(d),{}).get("N_d",0)
        tag=f"k={k} h={h} d={d} V={V} x{ncl} n={n} R={row.R}"
        chk(f"S7 {tag}: ADMISSIBLE", rec["ADMISSIBLE"],
            f"maxJ={rec['max_joint_agreement']}<=A-2={row.A-2} "
            f"maxray={rec['max_ray_agreement']}<=A={row.A}")
        chk(f"S7 {tag}: N_d = ncl*C(V,2) = {ncl*M}", Nd==ncl*M, f"N_d={Nd}")
        chk(f"S7 {tag}: rank ADDS across clusters = ncl*V*h = {ncl*V*h}",
            rk==ncl*V*h and frk==ncl*V*h, f"ray-rank={rk} family-rank={frk}")
        chk(f"S7 {tag}: cost/datum = {frk/max(Nd,1):.4f} = 2h/(V-1)",
            abs(frk/max(Nd,1) - 2*h/(V-1)) < 1e-9)
        chk(f"S7 {tag}: N_d beats SHARP-OCC law {(row.R+1)//(h-d)}",
            Nd > (row.R+1)//(h-d), f"N_d={Nd}")
        res.append(dict(cs=cs,n=n,R=row.R,N_d=Nd,rank=rk,family_rank=frk,
                        points_used=used,ADMISSIBLE=rec["ADMISSIBLE"],
                        law=(row.R+1)//(h-d)))
    json.dump(res, open(os.path.join(HERE,"stage7_clusters.json"),"w"),
              indent=1, default=str)
    print(f"\n{CH[0]} checks, {len(FAIL)} FAIL")
    for f in FAIL: print("  FAIL:", f)

if __name__ == "__main__":
    main()

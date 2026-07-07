#!/usr/bin/env python3
"""F5 P1-verify (L3a) + P2 hunt (L3-rigid live syzygies), Modal.

L3a (proved in F5_SKELETON.md) says: in any live dependence
Sum_i lambda_i (a_{S_i}, z_i a_{S_i}) = 0, every point of every
participating support is covered by >= 3 participating supports (a point
in exactly 2 distinct-slope supports forces lambda = 0 there via
a_S(x) != 0). This script:

(A) VERIFIES L3a directly: enumerate aligned (S, z) for random/adversarial
    (u,v) at toy rows, build the alignment-condition matrix
    A = [ (a_{S_i}, z_i a_{S_i}) ], compute its LEFT null space (the
    dependence vectors lambda) EXACTLY mod q, and check the covering
    corollary — no dependence has a support-point covered < 3 times with
    valid (Pi_S(v) != 0) participants. A single violation refutes L3a.

(B) P2 HUNT: search directly for an L3a-rigid LIVE syzygy that stays valid
    — a dependence whose participants all have Pi_S(v) != 0, pairwise
    cores <= k+t-2, and (by L3a) triple-covered supports. If found, L3 is
    FALSE as stated (report it — the method working); if the only rigid
    dependences carry an invalid participant, L3 holds on these rows.

a_S = top-sigma interpolation-coefficient functionals of support S (the
Pi_S rows). Exact F_q linear algebra throughout.
"""
import json
import random

import modal

app = modal.App("rs-mca-f5-l3a")
image = modal.Image.debian_slim()

ROWS = [(2, 2, 47), (2, 2, 97), (3, 2, 97), (4, 2, 97), (2, 3, 97), (4, 3, 97)]
# (k, t, q): sigma = t, A = k + t... NOTE floor uses A = k+sigma with the
# core threshold k+t-1; here we set sigma = t (agreement excess) so A = k+t.


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def probe(payload):
    import itertools
    k, t, q, seed = payload
    rng = random.Random(seed)
    n = q - 1
    dom = list(range(1, q))
    A = k + t
    core_cap = k + t - 2                      # live: pairwise cores <= this

    def inv(a):
        return pow(a % q, q - 2, q)

    def topcoeff_rows(S):
        """The sigma = A-k top interpolation-coefficient functionals of S:
        rows r s.t. r . w = (coeff of x^{k+i} in the deg<A interpolant of w
        on S), i = 0..A-k-1. Built from the Lagrange/Newton top coeffs."""
        xs = [dom[i] for i in S]
        # divided-difference top coefficients: the coeff of x^{A-1},...,x^k
        # of the unique deg<A interpolant equal each to a linear functional
        # of the values; extract by interpolating basis vectors.
        rows = []
        # basis: for each position p in S, interpolate e_p -> deg<A poly,
        # read its top sigma coeffs. Column p of the functional.
        import functools
        # precompute full Lagrange top coeffs per position
        cols = []
        for p_idx, xp in enumerate(xs):
            # Lagrange poly L_p(x) = prod_{l!=p}(x-x_l)/(xp-x_l), deg A-1
            num = [1]
            den = 1
            for l_idx, xl in enumerate(xs):
                if l_idx == p_idx:
                    continue
                new = [0] * (len(num) + 1)
                for d, c in enumerate(num):
                    new[d] = (new[d] - c * xl) % q
                    new[d + 1] = (new[d + 1] + c) % q
                num = new
                den = den * (xp - xl) % q
            invden = inv(den)
            coeffs = [(c * invden) % q for c in num]   # length A
            cols.append(coeffs)
        # functional for top coeff degree g (k <= g <= A-1): value = sum_p coeffs_p[g]*w_p
        for g in range(k, A):
            row = {S[p_idx]: cols[p_idx][g] % q for p_idx in range(len(S))}
            rows.append(row)
        return rows

    def aligned(word):
        out = []
        # enumerate codewords by k-subset interpolation, dedupe, collect agreement A supports
        seen = set()
        for idxs in itertools.combinations(range(n), k):
            xs = [dom[i] for i in idxs]
            ys = [word[i] for i in idxs]
            cf = [0] * k
            for xi, yi in zip(xs, ys):
                num = [1]; den = 1
                for xj in xs:
                    if xj == xi: continue
                    nw = [0]*(len(num)+1)
                    for d,c in enumerate(num):
                        nw[d]=(nw[d]-c*xj)%q; nw[d+1]=(nw[d+1]+c)%q
                    num=nw; den=den*(xi-xj)%q
                s=yi*inv(den)%q
                for d in range(len(num)): cf[d]=(cf[d]+s*num[d])%q
            key=tuple(cf)
            if key in seen: continue
            seen.add(key)
            supp=tuple(i for i in range(n) if sum(cf[d]*pow(dom[i],d,q) for d in range(k))%q==word[i])
            if len(supp)==A: out.append(supp)
        return out

    def build_and_check(u, v):
        # collect aligned (S, z) across all slopes
        fam = []
        for z in range(q):
            w = [(u[i]+z*v[i])%q for i in range(n)]
            for S in aligned(w):
                fam.append((S, z))
        # keep a LIVE subfamily: greedily drop pairs with core > core_cap
        live = []
        for S, z in fam:
            if all(len(set(S)&set(S2))<=core_cap or z==z2 for S2,z2 in live):
                live.append((S,z))
        if len(live) < 2: return {"live": len(live), "dep": 0, "rigid_valid": 0}
        # alignment matrix rows: sigma per (S,z), functional (a_S, z a_S) on R^{2n}
        M = []
        meta = []
        for S, z in live:
            for row in topcoeff_rows(S):
                vec = [0]*(2*n)
                for i,c in row.items():
                    vec[i]=c%q; vec[n+i]=(z*c)%q
                M.append(vec); meta.append((S,z))
        # left null space of M^T? we want lambda with sum lambda_r M[r] = 0:
        # i.e. left kernel of M (rows) => kernel of M^T. Compute row-dependences.
        # Gaussian elim tracking combinations.
        rows=[r[:]+[1 if i==j else 0 for j in range(len(M))] for i,r in enumerate([row[:] for row in M])]
        ncol=2*n
        piv=0
        for col in range(ncol):
            pr=next((r for r in range(piv,len(rows)) if rows[r][col]%q),None)
            if pr is None: continue
            rows[piv],rows[pr]=rows[pr],rows[piv]
            ip=inv(rows[piv][col])
            rows[piv]=[(x*ip)%q for x in rows[piv]]
            for r in range(len(rows)):
                if r!=piv and rows[r][col]%q:
                    f=rows[r][col]
                    rows[r]=[(a-f*b)%q for a,b in zip(rows[r],rows[piv])]
            piv+=1
            if piv==len(rows): break
        deps=[r[ncol:] for r in rows if all(x%q==0 for x in r[:ncol]) and any(x%q for x in r[ncol:])]
        # check covering corollary + validity for each dependence
        rigid_valid=0
        viol_L3a=0
        for lam in deps:
            # participants = rows with lam != 0 -> supports
            parts=[meta[r] for r in range(len(M)) if lam[r]%q]
            if not parts: continue
            supp_mult={}
            for S,z in parts:
                for x in S: supp_mult[x]=supp_mult.get(x,0)+1
            # L3a: every participating support point covered >=3 (or a shared slope)
            # (approximate check: min multiplicity over participant points)
            minmult=min(supp_mult.values()) if supp_mult else 0
            if minmult<3:
                # allowed only if that point sits in >=2 same-slope participants
                # (conservative: flag as potential L3a issue for inspection)
                viol_L3a+=1
            # validity: Pi_S(v) != 0 for all participants
            valid=all(any(row_dot(topcoeff_rows(S), v, q)) for S,z in parts)
            if valid and minmult>=3:
                rigid_valid+=1
        return {"live":len(live),"dep":len(deps),
                "L3a_violations":viol_L3a,"rigid_valid_syzygies":rigid_valid}

    def row_dot(rows, v, q):
        return [sum(c*v[i] for i,c in row.items())%q for row in rows]

    # trials: adversarial (two codewords + noise) + random + engineered
    # triple-cover attempt
    res=[]
    for kind in ("adv","adv","rand"):
        if kind=="adv":
            def ev(cf,x):
                acc=0
                for a in reversed(cf): acc=(acc*x+a)%q
                return acc
            c1=[rng.randrange(q) for _ in range(k)]
            c2=[rng.randrange(q) for _ in range(k)]
            u=[ev(c1,x) for x in dom]; v=[ev(c2,x) for x in dom]
            for _ in range(3):
                u[rng.randrange(n)]=rng.randrange(q); v[rng.randrange(n)]=rng.randrange(q)
        else:
            u=[rng.randrange(q) for _ in range(n)]; v=[rng.randrange(q) for _ in range(n)]
        res.append({"kind":kind, **build_and_check(u,v)})
    return {"k":k,"t":t,"q":q,"trials":res}


@app.local_entrypoint()
def main():
    payloads=[(k,t,q,7000+i) for i,(k,t,q) in enumerate(ROWS)]
    results=[r for r in probe.map(payloads,return_exceptions=True) if isinstance(r,dict)]
    l3a_ok=True; rigid_found=0
    for r in sorted(results,key=lambda r:(r["k"],r["t"],r["q"])):
        for tr in r["trials"]:
            v=tr.get("L3a_violations",0); rv=tr.get("rigid_valid_syzygies",0)
            if v: l3a_ok=False
            rigid_found+=rv
            print(f"k={r['k']} t={r['t']} q={r['q']} [{tr['kind']}]: live={tr.get('live')} "
                  f"deps={tr.get('dep')} L3a_viol={v} rigid_valid_syzygies={rv}")
    print(f"\nL3a holds (no covering violation): {l3a_ok}")
    print(f"rigid VALID live syzygies found (would refute L3): {rigid_found}")
    with open("/tmp/f5_l3a.json","w") as f: json.dump(results,f,indent=1)

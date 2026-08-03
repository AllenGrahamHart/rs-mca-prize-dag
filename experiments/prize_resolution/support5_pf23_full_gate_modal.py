#!/usr/bin/env python3
"""Decide the FULL band gate for PF2/PF3 (support-5 pilot, standing
COMPUTE REQUEST): does the unique nontrivial realiser class of each
charge-defeating all-escape-1 pencil fixture have max slope agreement
exactly A (live) or > A (over-agreement, gate fail)?

Class-invariance: dim Ann = 1, and adding a trivial (P, Q) in
RS_k x RS_k shifts codewords bijectively, so per-slope max agreement
depends only on the class — ONE scan per fixture decides it.

Local: rebuild PF2/PF3 via the pilot's own constructor, solve the
realiser system, pick a v-nonvanishing representative. Remote: for
every slope z in F_q u {inf}, decide whether any (A+1)-subset carries
w_z; chunked map. Exact integer arithmetic mod q throughout.
"""
import hashlib
import json
import sys
from itertools import combinations, islice
from pathlib import Path

import modal

DIRECTORY = Path(__file__).parent
RESULT = DIRECTORY / "support5_pf23_full_gate_result.json"

app = modal.App("rs-mca-support5-pf23-full-gate")
image = modal.Image.debian_slim(python_version="3.12").pip_install("numpy==2.2.5")

CHUNK = 200_000


@app.function(image=image, cpu=2.0, memory=4096, timeout=1800)
def scan_chunk(job):
    import numpy as np
    q, xs, u, v, slopes_all, subsets, k = (
        job["q"], job["xs"], job["u"], job["v"], job["slopes"],
        job["subsets"], job["k"])
    inv = [0] * q
    for a in range(1, q):
        inv[a] = pow(a, q - 2, q)
    S = np.array(subsets, dtype=np.int64)          # (c, A+1)
    T, R = S[:, :k], S[:, k:]                       # anchors / checks
    x = np.array(xs, dtype=np.int64)
    xT, xR = x[T], x[R]                             # point values
    c, rest = T.shape[0], R.shape[1]
    # Lagrange weights W[c, rest, k]: pred(y_r) = sum_j W[c,r,j] w(t_j)
    W = np.ones((c, rest, k), dtype=np.int64)
    for j in range(k):
        num = np.ones((c, rest), dtype=np.int64)
        den = np.ones(c, dtype=np.int64)
        for i in range(k):
            if i == j:
                continue
            num = num * ((xR - xT[:, i:i + 1]) % q) % q
            den = den * ((xT[:, j] - xT[:, i]) % q) % q
        deninv = np.array([inv[int(d)] for d in den], dtype=np.int64)
        W[:, :, j] = num * deninv[:, None] % q
    uu = np.array(u, dtype=np.int64)
    vv = np.array(v, dtype=np.int64)
    hits = {}
    for z in slopes_all:                            # z = int, or "inf"
        w = vv % q if z == "inf" else (uu + int(z) * vv) % q
        wT, wR = w[T], w[R]
        pred = np.einsum("crj,cj->cr", W, wT) % q
        ok = np.all(pred == wR, axis=1)
        nhit = int(ok.sum())
        if nhit:
            first = int(np.flatnonzero(ok)[0])
            hits[str(z)] = dict(count=nhit, example=[int(t) for t in S[first]])
    return hits


@app.local_entrypoint()
def main():
    sys.path.insert(0, str(DIRECTORY.parent.parent
                           / "notes/pilots_20260803/support5_deficit"))
    import verify as sv                                     # pilot's own code

    out = {}
    for name, args in (("PF2", (29, 2, 4, 10)), ("PF3", (31, 2, 4, 12))):
        fx = sv.build_pencil_E1(*args, name=name)
        q, k, n, xs = fx["q"], fx["k"], fx["n"], fx["row"].xs
        A = k + fx["h"]
        # realiser system: for each ray, dual-code checks on its support
        rows = []
        for a, sup in enumerate(fx["supports"]):
            z = fx["slopes"][a]
            pts = [xs[i] for i in sup]
            lam = []
            for x0 in pts:
                p = 1
                for y in pts:
                    if y != x0:
                        p = p * ((x0 - y) % q) % q
                lam.append(pow(p, q - 2, q))
            for j in range(A - k):
                row = [0] * (2 * n)
                for t, i in enumerate(sup):
                    cji = lam[t] * pow(xs[i], j, q) % q
                    row[i] = cji
                    row[n + i] = cji * z % q
                rows.append(row)
        # nullspace mod q by Gaussian elimination
        M = [r[:] for r in rows]
        piv, prow = [], 0
        for col in range(2 * n):
            sel = next((r for r in range(prow, len(M)) if M[r][col] % q), None)
            if sel is None:
                continue
            M[prow], M[sel] = M[sel], M[prow]
            ip = pow(M[prow][col], q - 2, q)
            M[prow] = [x * ip % q for x in M[prow]]
            for r in range(len(M)):
                if r != prow and M[r][col] % q:
                    f = M[r][col]
                    M[r] = [(a - f * b) % q for a, b in zip(M[r], M[prow])]
            piv.append(col)
            prow += 1
        free = [c0 for c0 in range(2 * n) if c0 not in piv]
        nullity = len(free)
        # trivial subspace = RS_k x RS_k has dim 2k; pick a basis vector of
        # the nullspace outside it (deficit class), by checking degree > k
        def null_vec(fc):
            vvec = [0] * (2 * n)
            vvec[fc] = 1
            for r, col in enumerate(piv):
                vvec[col] = (-M[r][fc]) % q
            return vvec
        import itertools as it
        # Vandermonde matrix for degree-<k fit test
        def is_trivial(vec):
            for half in (vec[:n], vec[n:]):
                pts = list(zip(xs, half))
                # interpolate first k, verify rest
                tx = [p[0] for p in pts[:k]]
                tv = [p[1] for p in pts[:k]]
                for (y, val) in pts[k:]:
                    acc = 0
                    for j in range(k):
                        numv, denv = 1, 1
                        for i2 in range(k):
                            if i2 != j:
                                numv = numv * ((y - tx[i2]) % q) % q
                                denv = denv * ((tx[j] - tx[i2]) % q) % q
                        acc = (acc + tv[j] * numv * pow(denv, q - 2, q)) % q
                    if acc != val % q:
                        return False
            return True
        cand = None
        for fc in free:
            vec = null_vec(fc)
            if not is_trivial(vec):
                cand = vec
                break
        assert cand is not None, "no nontrivial realiser found"
        u, v = cand[:n], cand[n:]
        # make v nowhere zero by adding a trivial Q in RS_k to v
        import random
        rnd = random.Random(7)
        for _ in range(500):
            if all(x % q for x in v):
                break
            coef = [rnd.randrange(q) for _ in range(k)]
            v = [(v[i] + sum(coef[j] * pow(xs[i], j, q) for j in range(k)))
                 % q for i in range(n)]
        assert all(x % q for x in v), "no v-nonvanishing representative"
        slopes_all = list(range(q)) + ["inf"]
        subs = combinations(range(n), A + 1)
        jobs = []
        while True:
            block = list(islice(subs, CHUNK))
            if not block:
                break
            jobs.append(dict(q=q, xs=xs, u=u, v=v, slopes=slopes_all,
                             subsets=block, k=k))
        agg = {}
        for hits in scan_chunk.map(jobs):
            for zt, d in hits.items():
                if zt not in agg:
                    agg[zt] = dict(count=0, example=d["example"])
                agg[zt]["count"] += d["count"]
        over = sorted(agg.keys())
        designed = [str(z) for z in fx["slopes"]]
        out[name] = dict(
            q=q, k=k, h=fx["h"], V=fx["V"], n=n, A=A,
            nullity=nullity, designed_slopes=fx["slopes"],
            over_agreeing_slopes=agg,
            full_gate_max_ray=("PASS: max agreement = A at every slope"
                               if not over else
                               f"FAIL: {len(over)} slopes exceed A"),
            designed_slope_over_agrees=[z for z in designed if z in agg],
            chunks=len(jobs),
        )
        print(name, "->", out[name]["full_gate_max_ray"],
              "| over-agreeing:", over)
    payload = json.dumps(out, indent=1, sort_keys=True)
    RESULT.write_text(payload + "\n")
    print("sha256", hashlib.sha256(payload.encode()).hexdigest())

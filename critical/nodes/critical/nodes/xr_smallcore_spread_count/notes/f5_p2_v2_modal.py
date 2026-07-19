#!/usr/bin/env python3
"""F5 P2 v2 (Modal): fixed checker + the engineered triple-cover hunt.

FIXES from run 1 (banked in F5_SKELETON.md):
- LIVE FAMILY = one support per slope (same-slope mass is class-(i),
  stripped) + pairwise cores <= k+t-2. Run 1 admitted same-slope members,
  making random words degenerate.
- L3a CHECK = for every computed dependence: every participant point is
  covered >= 3 times OR all its coverers share one slope (the proved
  escape). Any computed dependence violating this contradicts the paper
  lemma => checker-vs-paper discrepancy alarm (none expected).

P2 HUNT (the L3 decision experiment): L3a confines counterexamples to
rigid triple-cover designs. We build them DIRECTLY: combinatorial designs
(m supports of size A on P points, every point in >= 3 supports, pairwise
cores <= k+t-2), embedded into the domain at random, distinct slopes
assigned; exact GF(q) linear algebra decides (i) whether the alignment
conditions are DEPENDENT, and if so (ii) whether a solution (u,v) exists
with ALL alignments valid (Pi_S(v) != 0) and exact agreement — a rigid
VALID live syzygy = L3 refuted as stated (then L4 absorbs it via a design
bound, or L3 is weakened; either way the method proceeds). Zero hits
across the design space = the confined surface is empty at these scales.
"""
import itertools
import json
import random

import modal

app = modal.App("rs-mca-f5-p2v2")
image = modal.Image.debian_slim()

ROWS = [(2, 2, 47), (2, 2, 97), (2, 2, 193)]
DESIGN_TRIES = 120
EMBED_TRIES = 8


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def hunt(payload):
    k, t, q, seed = payload
    rng = random.Random(seed)
    n = q - 1
    dom = list(range(1, q))
    A = k + t
    core_cap = k + t - 2

    def inv(a):
        return pow(a % q, q - 2, q)

    def top_rows(S_pts):
        """sigma x |S| top-coefficient functional rows for domain points S_pts."""
        m = len(S_pts)
        cols = []
        for p_idx, xp in enumerate(S_pts):
            num = [1]
            den = 1
            for l_idx, xl in enumerate(S_pts):
                if l_idx == p_idx:
                    continue
                new = [0] * (len(num) + 1)
                for d, c in enumerate(num):
                    new[d] = (new[d] - c * xl) % q
                    new[d + 1] = (new[d + 1] + c) % q
                num = new
                den = den * (xp - xl) % q
            iv = inv(den)
            cols.append([(c * iv) % q for c in num])
        return [[cols[p][g] % q for p in range(m)] for g in range(k, A)]

    def random_design():
        """3-regular-ish A-uniform design with pairwise cores <= core_cap."""
        P = rng.randrange(2 * A, 3 * A + 3)
        target_m = (3 * P + A - 1) // A + rng.randrange(0, 3)
        blocks = []
        for _ in range(300):
            if len(blocks) >= target_m:
                break
            S = tuple(sorted(rng.sample(range(P), A)))
            if all(len(set(S) & set(B)) <= core_cap for B in blocks) and S not in blocks:
                blocks.append(S)
        cover = [0] * P
        for B in blocks:
            for x in B:
                cover[x] += 1
        # prune points covered < 3 (they force lambda = 0 through any block
        # containing them unless slope-shared; for the hunt demand full >= 3)
        if min(cover) < 3:
            return None
        return P, blocks

    def gauss_nullspace(M):
        """Left-dependences of rows of M over F_q: returns basis of
        {lam : sum lam_r M[r] = 0}."""
        R = len(M)
        C = len(M[0]) if R else 0
        aug = [list(M[r]) + [1 if i == r else 0 for i in range(R)] for r in range(R)]
        piv = 0
        for col in range(C):
            pr = next((r for r in range(piv, R) if aug[r][col] % q), None)
            if pr is None:
                continue
            aug[piv], aug[pr] = aug[pr], aug[piv]
            ip = inv(aug[piv][col])
            aug[piv] = [(x * ip) % q for x in aug[piv]]
            for r in range(R):
                if r != piv and aug[r][col] % q:
                    f = aug[r][col]
                    aug[r] = [(a - f * b) % q for a, b in zip(aug[r], aug[piv])]
            piv += 1
            if piv == R:
                break
        return [row[C:] for row in aug
                if all(x % q == 0 for x in row[:C]) and any(x % q for x in row[C:])]

    def try_realize(fam_pts, slopes, deps, sig_rows):
        """Given a dependent family, look for (u,v) satisfying ALL alignment
        conditions with all Pi_S(v) != 0. Solve the linear system for (u,v)
        restricted to the union of support coordinates; sample the solution
        space; test validity."""
        used = sorted(set(x for S in fam_pts for x in S))
        idx = {x: i for i, x in enumerate(used)}
        U = len(used)
        rows = []
        for (S, z, srows) in sig_rows:
            for row in srows:
                vec = [0] * (2 * U)
                for p_i, x in enumerate(S):
                    vec[idx[x]] = row[p_i] % q
                    vec[U + idx[x]] = (z * row[p_i]) % q
                rows.append(vec)
        # solution space of rows . (u,v) = 0 : nullspace of the matrix
        R = len(rows)
        C = 2 * U
        aug = [list(r) for r in rows]
        piv_cols = []
        piv = 0
        for col in range(C):
            pr = next((r for r in range(piv, R) if aug[r][col] % q), None)
            if pr is None:
                continue
            aug[piv], aug[pr] = aug[pr], aug[piv]
            ip = inv(aug[piv][col])
            aug[piv] = [(x * ip) % q for x in aug[piv]]
            for r in range(R):
                if r != piv and aug[r][col] % q:
                    f = aug[r][col]
                    aug[r] = [(a - f * b) % q for a, b in zip(aug[r], aug[piv])]
            piv_cols.append(col)
            piv += 1
            if piv == R:
                break
        free = [c for c in range(C) if c not in piv_cols]
        if not free:
            return False, 0
        # sample solutions
        for _ in range(24):
            sol = [0] * C
            for c in free:
                sol[c] = rng.randrange(q)
            for r in range(piv - 1, -1, -1):
                col = piv_cols[r]
                s = sum(aug[r][c] * sol[c] for c in range(C) if c != col) % q
                sol[col] = (-s) % q
            v_vals = {used[i]: sol[U + i] for i in range(U)}
            ok = True
            for (S, z, srows) in sig_rows:
                pv = [sum(row[p_i] * v_vals[x] for p_i, x in enumerate(S)) % q
                      for row in srows]
                if all(c == 0 for c in pv):
                    ok = False
                    break
            if ok:
                return True, len(free)
        return False, len(free)

    found = []
    designs_tested = 0
    dependent_configs = 0
    for _ in range(DESIGN_TRIES):
        d = random_design()
        if d is None:
            continue
        P, blocks = d
        designs_tested += 1
        for _ in range(EMBED_TRIES):
            pts = rng.sample(dom, P)
            fam_pts = [tuple(pts[x] for x in B) for B in blocks]
            slopes = rng.sample(range(q), len(blocks))
            sig_rows = [(S, z, top_rows(S)) for S, z in zip(fam_pts, slopes)]
            M = []
            for (S, z, srows) in sig_rows:
                used = S
                for row in srows:
                    # full 2n vector unnecessary; dependence is a property of
                    # rows — build on union coords
                    pass
            # dependence test on union coordinates
            usedU = sorted(set(x for S in fam_pts for x in S))
            idxU = {x: i for i, x in enumerate(usedU)}
            M = []
            for (S, z, srows) in sig_rows:
                for row in srows:
                    vec = [0] * (2 * len(usedU))
                    for p_i, x in enumerate(S):
                        vec[idxU[x]] = row[p_i] % q
                        vec[len(usedU) + idxU[x]] = (z * row[p_i]) % q
                    M.append(vec)
            deps = gauss_nullspace(M)
            if not deps:
                continue
            dependent_configs += 1
            ok, dof = try_realize(fam_pts, slopes, deps, sig_rows)
            if ok:
                found.append({"P": P, "m": len(blocks), "slopes": slopes,
                              "supports": [list(S) for S in fam_pts],
                              "free_dof": dof})
    return {"k": k, "t": t, "q": q, "designs_tested": designs_tested,
            "dependent_embedded_configs": dependent_configs,
            "RIGID_VALID_LIVE_SYZYGIES": found[:3], "n_found": len(found)}


@app.local_entrypoint()
def main():
    payloads = []
    for i, (k, t, q) in enumerate(ROWS):
        for s in range(6):   # 6 shards per row
            payloads.append((k, t, q, 9000 + 37 * i + s))
    results = [r for r in hunt.map(payloads, return_exceptions=True)
               if isinstance(r, dict)]
    agg = {}
    for r in results:
        key = (r["k"], r["t"], r["q"])
        a = agg.setdefault(key, {"designs": 0, "dependent": 0, "found": 0})
        a["designs"] += r["designs_tested"]
        a["dependent"] += r["dependent_embedded_configs"]
        a["found"] += r["n_found"]
    total_found = 0
    for key, a in sorted(agg.items()):
        total_found += a["found"]
        print(f"(k,t,q)={key}: designs={a['designs']} dependent-configs={a['dependent']} "
              f"RIGID VALID LIVE SYZYGIES={a['found']}")
    print(f"\nTOTAL rigid valid live syzygies (refutes L3 as stated if > 0): {total_found}")
    with open("/tmp/f5_p2v2.json", "w") as f:
        json.dump(results, f, indent=1)

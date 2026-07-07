#!/usr/bin/env python3
"""F5 P2 realization decision (Modal): can the q=47 syzygy hit be realized
with EXACT agreement sets, or is exactness forced to fail?

Deterministic structure: once the union values (u,v)|_used are fixed (a
point of the 5-dim solution space), the 6 codewords cf_i are determined;
- OUTSIDE points x: choosing (u_x, v_x) avoiding the 6 lines
  u_x + z_i v_x = cf_i(x) is always possible (q^2 - 6q > 0) — never an
  obstruction.
- UNION points y not in S_i: the coincidence cf_i(y) = u_y + z_i v_y is a
  linear condition ON THE SOLUTION SPACE; if some such condition is
  IDENTICALLY satisfied on the whole solution space, exactness is FORCED
  to fail (the hit is an artifact and L3 stands); otherwise a solution
  avoiding all ~24 coincidence hyperplanes exists (genuine counterexample
  to L3 as stated; L3 weakens to L3' = design-expensive syzygies, and the
  L4 composition still gives Theta(n)).

This script decides it exactly: parameterize the solution space, express
each union-coincidence as a linear functional in the 5 free parameters,
check which are identically zero; if none, construct an explicit avoiding
point and output the full certificate (u,v) with all checks.
"""
import json
import random

import modal

app = modal.App("rs-mca-f5-realize")
image = modal.Image.debian_slim()


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def decide(hit):
    q, k = hit["q"], hit["k"]
    A = 4
    n = q - 1
    dom = list(range(1, q))
    sup = [tuple(S) for S in hit["supports"]]
    slopes = hit["slopes"]

    def inv(a):
        return pow(a % q, q - 2, q)

    def top_rows(S):
        cols = []
        for pi, xp in enumerate(S):
            num = [1]
            den = 1
            for li, xl in enumerate(S):
                if li == pi:
                    continue
                nw = [0] * (len(num) + 1)
                for d, c in enumerate(num):
                    nw[d] = (nw[d] - c * xl) % q
                    nw[d + 1] = (nw[d + 1] + c) % q
                num = nw
                den = den * (xp - xl) % q
            iv = inv(den)
            cols.append([(c * iv) % q for c in num])
        return [[cols[p][g] % q for p in range(len(S))] for g in range(k, A)]

    used = sorted(set(x for S in sup for x in S))
    idx = {x: i for i, x in enumerate(used)}
    U = len(used)
    C = 2 * U
    rows = []
    for S, z in zip(sup, slopes):
        for row in top_rows(list(S)):
            vec = [0] * C
            for pi, x in enumerate(S):
                vec[idx[x]] = row[pi] % q
                vec[U + idx[x]] = (z * row[pi]) % q
            rows.append(vec)
    # solution space basis
    M = [r[:] for r in rows]
    piv = 0
    pivcols = []
    for col in range(C):
        pr = next((r for r in range(piv, len(M)) if M[r][col] % q), None)
        if pr is None:
            continue
        M[piv], M[pr] = M[pr], M[piv]
        ip = inv(M[piv][col])
        M[piv] = [(x * ip) % q for x in M[piv]]
        for r in range(len(M)):
            if r != piv and M[r][col] % q:
                f = M[r][col]
                M[r] = [(a - f * b) % q for a, b in zip(M[r], M[piv])]
        pivcols.append(col)
        piv += 1
    free = [c for c in range(C) if c not in pivcols]
    D = len(free)

    def basis_vec(j):
        sol = [0] * C
        sol[free[j]] = 1
        for r in range(piv - 1, -1, -1):
            col = pivcols[r]
            s = sum(M[r][c] * sol[c] for c in range(C) if c != col) % q
            sol[col] = (-s) % q
        return sol

    B = [basis_vec(j) for j in range(D)]

    # linear functional of a union coincidence: cf_i(y) - (u_y + z_i v_y)
    # cf_i is linear in the solution: cf_i = line through (u+z_i v)|first-two
    # points of S_i; express cf_i(y) as a linear functional of sol.
    def coincidence_functional(i, y):
        S = list(sup[i])
        z = slopes[i]
        x0, x1 = S[0], S[1]
        # w(x) = sol[idx[x]] + z*sol[U+idx[x]]
        # cf(y) = w(x0)*(y-x1)/(x0-x1) + w(x1)*(y-x0)/(x1-x0)
        c0 = (y - x1) * inv(x0 - x1) % q
        c1 = (y - x0) * inv(x1 - x0) % q
        f = [0] * C
        f[idx[x0]] = c0
        f[U + idx[x0]] = c0 * z % q
        f[idx[x1]] = c1
        f[U + idx[x1]] = c1 * z % q
        f[idx[y]] = (f[idx[y]] - 1) % q
        f[U + idx[y]] = (f[U + idx[y]] - z) % q
        return f

    coincidences = []
    for i, S in enumerate(sup):
        for y in used:
            if y in S:
                continue
            f = coincidence_functional(i, y)
            # restrict to solution space: g_j = f . B_j
            g = [sum(f[c] * B[j][c] for c in range(C)) % q for j in range(D)]
            coincidences.append({"i": i, "y": y, "g": g,
                                 "identically_zero": all(x == 0 for x in g)})
    forced = [c for c in coincidences if c["identically_zero"]]
    # validity functionals: Pi_S(v) = 0 is a codim-sigma condition on sol;
    # also check none identically zero (else valid realization impossible)
    forced_invalid = []
    for i, S in enumerate(sup):
        tr = top_rows(list(S))
        gs = []
        for row in tr:
            f = [0] * C
            for pi, x in enumerate(S):
                f[U + idx[x]] = row[pi] % q
            g = [sum(f[c] * B[j][c] for c in range(C)) % q for j in range(D)]
            gs.append(g)
        if all(all(x == 0 for x in g) for g in gs):
            forced_invalid.append(i)
    result = {"free_dim": D, "n_coincidence_conditions": len(coincidences),
              "forced_coincidences": [(c["i"], c["y"]) for c in forced],
              "forced_invalid_supports": forced_invalid}
    if forced or forced_invalid:
        result["verdict"] = "ARTIFACT: exactness/validity forced to fail — L3 stands on this hit"
        return result
    # search the free space for a point avoiding all coincidence hyperplanes
    # and all validity loci (each nonzero functional kills <= q^{D-1} points)
    rng = random.Random(3)
    for _ in range(5000):
        pt = [rng.randrange(q) for _ in range(D)]
        okc = all(sum(c["g"][j] * pt[j] for j in range(D)) % q != 0
                  for c in coincidences)
        if not okc:
            continue
        sol = [0] * C
        for j in range(D):
            for c in range(C):
                sol[c] = (sol[c] + pt[j] * B[j][c]) % q
        # validity check on this sol
        ok = True
        for i, S in enumerate(sup):
            vv = [sol[U + idx[x]] for x in S]
            pv = [sum(r_[pi] * vv[pi] for pi in range(A)) % q
                  for r_ in top_rows(list(S))]
            if all(x == 0 for x in pv):
                ok = False
                break
        if ok:
            result["verdict"] = "GENUINE: exact + valid realization exists on the union"
            result["solution_union"] = sol
            return result
    result["verdict"] = "UNDECIDED after sampling (raise samples)"
    return result


@app.local_entrypoint()
def main():
    hit = json.load(open('/tmp/f5_hit.json'))
    r = decide.remote(hit)
    print(json.dumps({k: v for k, v in r.items() if k != "solution_union"}, indent=1))
    with open("/tmp/f5_realize.json", "w") as f:
        json.dump(r, f, indent=1)

#!/usr/bin/env python3
"""F5 P3b (Modal): ON-LOCUS absorption certification at p = 2^31 - 1.

Part A showed generic embeddings of the minimal stratum are independent;
absorption is only needed ON the dependence locus. This run samples the
locus directly at a large prime: fix all but one embedding coordinate,
leave x_last = T free; the rank-drop condition is det D(T) = 0 for a
12x12 minor polynomial D. Find the F_p-roots of D by Cantor-Zassenhaus,
keep roots where the FULL matrix genuinely drops rank, and run the exact
absorption decision (P0-quotient form) at each on-locus embedding.

Per on-locus point: compute the fresh directions F (solution space mod
P0), and check whether some spillover chi_{i,y} or Pi_{S_i}(v)-block
vanishes identically on F (= absorption). Output per shape: locus points
found / absorbed / NOT absorbed (a NOT-absorbed point refutes absorption
outright — report the certificate).
"""
import itertools
import json
import random

import modal

app = modal.App("rs-mca-f5-p3b")
image = modal.Image.debian_slim()

P31 = (1 << 31) - 1
SHAPES_PER_JOB = 3
LINES_PER_SHAPE = 4
NJOBS = 14


def _tools(q):
    def inv(a):
        return pow(a % q, q - 2, q)

    def top_rows(S, k, A, normalized=True):
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
            if normalized:
                iv = inv(den)
                cols.append([(c * iv) % q for c in num])
            else:
                # unnormalized: polynomial in the support coordinates
                # (row scaling by the nonzero den does not move rank drops,
                # PROVIDED dens are nonzero; we exclude tau hitting other
                # points separately). NOTE: scaling differs per ROW-set but
                # is uniform within the support's sigma rows.
                cols.append([c % q for c in num])
        return [[cols[p][g] % q for p in range(len(S))] for g in range(k, A)]

    def build_rows(sup, slopes, used, k, A):
        idx = {x: i for i, x in enumerate(used)}
        U = len(used)
        rows = []
        for S, z in zip(sup, slopes):
            for row in top_rows(list(S), k, A):
                vec = [0] * (2 * U)
                for pi, x in enumerate(S):
                    vec[idx[x]] = row[pi] % q
                    vec[U + idx[x]] = (z * row[pi]) % q
                rows.append(vec)
        return rows, idx, U

    def eliminate(rows):
        Mx = [r[:] for r in rows]
        piv = 0
        pivcols = []
        C = len(Mx[0]) if Mx else 0
        for col in range(C):
            pr = next((r for r in range(piv, len(Mx)) if Mx[r][col] % q), None)
            if pr is None:
                continue
            Mx[piv], Mx[pr] = Mx[pr], Mx[piv]
            ip = inv(Mx[piv][col])
            Mx[piv] = [(x * ip) % q for x in Mx[piv]]
            for r in range(len(Mx)):
                if r != piv and Mx[r][col] % q:
                    f = Mx[r][col]
                    Mx[r] = [(a - f * b) % q for a, b in zip(Mx[r], Mx[piv])]
            pivcols.append(col)
            piv += 1
        return Mx[:piv], pivcols

    def nullspace(rows, C):
        basis, pivcols = eliminate(rows)
        free = [c for c in range(C) if c not in pivcols]
        out = []
        for fc in free:
            vec = [0] * C
            vec[fc] = 1
            for r, col in enumerate(pivcols):
                vec[col] = (-basis[r][fc]) % q
            out.append(vec)
        return out, len(basis)

    return inv, top_rows, build_rows, eliminate, nullspace


def _polytools(q):
    def pmul(a, b, mod):
        r = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    r[i + j] = (r[i + j] + x * y) % q
        return pmod(r, mod) if mod else r

    def pmod(a, m):
        a = a[:]
        dm = len(m) - 1
        iv = pow(m[-1], q - 2, q)
        while len(a) - 1 >= dm:
            c = a[-1] * iv % q
            if c:
                off = len(a) - 1 - dm
                for i, x in enumerate(m):
                    a[off + i] = (a[off + i] - c * x) % q
            a.pop()
            while a and a[-1] == 0 and len(a) - 1 >= dm:
                a.pop()
        while a and a[-1] == 0:
            a.pop()
        return a or [0]

    def pgcd(a, b):
        a, b = a[:], b[:]
        while b != [0] and b:
            a, b = b, pmod(a, b)
        if a != [0]:
            iv = pow(a[-1], q - 2, q)
            a = [x * iv % q for x in a]
        return a

    def ppow_x(e, mod):
        # x^e mod (mod)
        result = [1]
        base = pmod([0, 1], mod)
        while e:
            if e & 1:
                result = pmul(result, base, mod)
            base = pmul(base, base, mod)
            e >>= 1
        return result

    def roots(f, rng):
        # all roots in F_q of polynomial f (coeff list, low->high)
        f = f[:]
        while f and f[-1] == 0:
            f.pop()
        if not f or len(f) == 1:
            return []
        xq = ppow_x(q, f)
        xq_minus_x = [(a - b) % q for a, b in
                      zip(xq + [0] * (2 + len(f)), [0, 1] + [0] * (len(xq) + len(f)))]
        g = pgcd(f, xq_minus_x)
        out = []

        def split(h):
            h = h[:]
            while h and h[-1] == 0:
                h.pop()
            if len(h) <= 1:
                return
            if len(h) == 2:
                out.append((-h[0]) * pow(h[1], q - 2, q) % q)
                return
            for _ in range(40):
                a = rng.randrange(q)
                # gcd((x+a)^((q-1)/2) - 1, h)
                shift = [a, 1]
                e = (q - 1) // 2
                acc = [1]
                base = pmod(shift, h)
                ee = e
                while ee:
                    if ee & 1:
                        acc = pmul(acc, base, h)
                    base = pmul(base, base, h)
                    ee >>= 1
                acc = acc[:]
                acc[0] = (acc[0] - 1) % q
                d = pgcd(h, acc)
                if 1 < len(d) < len(h):
                    split(d)
                    # h / d
                    quo = pdiv(h, d)
                    split(quo)
                    return
            return

        def pdiv(a, b):
            a = a[:]
            out_q = [0] * (len(a) - len(b) + 1)
            iv = pow(b[-1], q - 2, q)
            while len(a) >= len(b) and any(a):
                c = a[-1] * iv % q
                off = len(a) - len(b)
                out_q[off] = c
                for i, x in enumerate(b):
                    a[off + i] = (a[off + i] - c * x) % q
                while a and a[-1] == 0:
                    a.pop()
            return out_q or [1]

        split(g)
        return sorted(set(out))

    return roots


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def onlocus(payload):
    shapes, seed = payload
    q = P31
    k, A = 2, 4
    rng = random.Random(seed)
    inv, top_rows, build_rows, eliminate, nullspace = _tools(q)
    roots_of = _polytools(q)
    report = []
    for cls in shapes:
        Pn = 8
        found = absorbed = notabs = 0
        details = []
        for _ in range(LINES_PER_SHAPE):
            base_pts = rng.sample(range(1, 10**9), Pn - 1)
            slopes = rng.sample(range(1, 10**9), 6)

            def matrix_at(tval, normalized=True):
                pts = base_pts + [tval]
                sup = [tuple(pts[x] for x in B) for B in cls]
                used = sorted(set(x for S in sup for x in S))
                if normalized:
                    rows, idx, U = build_rows(sup, slopes, used, k, A)
                else:
                    idx = {x: i for i, x in enumerate(used)}
                    U = len(used)
                    rows = []
                    for S, z in zip(sup, slopes):
                        for row in top_rows(list(S), k, A, normalized=False):
                            vec = [0] * (2 * U)
                            for pi, x in enumerate(S):
                                vec[idx[x]] = row[pi] % q
                                vec[U + idx[x]] = (z * row[pi]) % q
                            rows.append(vec)
                return rows, sup, used, idx, U

            # minor polynomial via interpolation: det of rows[:,cols12]
            # pick 12 columns = first 12 that give generic full rank
            deg_bound = 40
            ts = rng.sample(range(1, 10**9), deg_bound + 1)
            # choose a column set once at a generic t
            rows0, _, _, _, _ = matrix_at(ts[0], normalized=False)
            basis0, pivcols0 = eliminate(rows0)
            if len(basis0) < 12:
                continue  # line starts on-locus; rare, skip
            cols12 = pivcols0[:12]

            def det12(tval):
                rows, _, _, _, _ = matrix_at(tval, normalized=False)
                Mx = [[r[c] for c in cols12] for r in rows]
                det = 1
                n_ = 12
                for col in range(n_):
                    pr = next((r for r in range(col, n_) if Mx[r][col] % q), None)
                    if pr is None:
                        return 0
                    if pr != col:
                        Mx[col], Mx[pr] = Mx[pr], Mx[col]
                        det = (-det) % q
                    det = det * Mx[col][col] % q
                    ipv = inv(Mx[col][col])
                    for r in range(col + 1, n_):
                        if Mx[r][col] % q:
                            f = Mx[r][col] * ipv % q
                            Mx[r] = [(a - f * b) % q
                                     for a, b in zip(Mx[r], Mx[col])]
                return det % q

            evals = [(t, det12(t)) for t in ts]
            # Lagrange interpolation of the minor polynomial
            coeffs = [0] * (deg_bound + 1)
            for i, (ti, yi) in enumerate(evals):
                num = [1]
                den = 1
                for j, (tj, _) in enumerate(evals):
                    if j == i:
                        continue
                    nw = [0] * (len(num) + 1)
                    for d, c in enumerate(num):
                        nw[d] = (nw[d] - c * tj) % q
                        nw[d + 1] = (nw[d + 1] + c) % q
                    num = nw
                    den = den * (ti - tj) % q
                s = yi * inv(den) % q
                for d in range(len(num)):
                    coeffs[d] = (coeffs[d] + s * num[d]) % q
            for tau in roots_of(coeffs, rng):
                if tau in base_pts or tau == 0:
                    continue
                rows, sup, used, idx, U = matrix_at(tau)
                basis, pivcols = eliminate(rows)
                if len(basis) >= 12:
                    continue  # minor zero but full matrix still rank 12
                found += 1
                # absorption decision in P0-quotient form: nullspace V,
                # quotient by P0 (deg<k pencil pairs), test spillover +
                # Pi(v)-block vanishing on the fresh directions
                V, rank = nullspace(rows, 2 * U)
                # P0 basis on union coords
                P0 = []
                for du in range(k):
                    vec = [0] * (2 * U)
                    for x in used:
                        vec[idx[x]] = pow(x, du, q)
                    P0.append(vec)
                    vec2 = [0] * (2 * U)
                    for x in used:
                        vec2[U + idx[x]] = pow(x, du, q)
                    P0.append(vec2)
                # fresh = V mod span(P0): reduce V against P0 basis
                pb, ppiv = eliminate(P0)
                fresh = []
                for v_ in V:
                    w = v_[:]
                    for r, col in enumerate(ppiv):
                        if w[col] % q:
                            f = w[col]
                            w = [(a - f * b) % q for a, b in zip(w, pb[r])]
                    if any(x % q for x in w):
                        fresh.append(w)
                fb, fpiv = eliminate(fresh)
                if not fb:
                    found -= 1
                    continue  # V = P0: no fresh direction (degenerate)

                def vanishes_on_fresh(func):
                    return all(sum(func[c] * fv[c] for c in range(2 * U)) % q == 0
                               for fv in fb)

                absorbed_here = False
                for i, S in enumerate(sup):
                    S = list(S)
                    z = slopes[i]
                    base2 = S[:k]
                    for y in used:
                        if y in S:
                            continue
                        f = [0] * (2 * U)
                        for xb in base2:
                            lg = 1
                            for xo in base2:
                                if xo == xb:
                                    continue
                            # careful: k=2 -> single xo
                            xo = [t_ for t_ in base2 if t_ != xb][0]
                            lg = (y - xo) * inv(xb - xo) % q
                            f[idx[xb]] = (f[idx[xb]] + lg) % q
                            f[U + idx[xb]] = (f[U + idx[xb]] + lg * z) % q
                        f[idx[y]] = (f[idx[y]] - 1) % q
                        f[U + idx[y]] = (f[U + idx[y]] - z) % q
                        if vanishes_on_fresh(f):
                            absorbed_here = True
                            break
                    if absorbed_here:
                        break
                if not absorbed_here:
                    for i, S in enumerate(sup):
                        gs = []
                        for row in top_rows(list(S), k, A):
                            f = [0] * (2 * U)
                            for pi, x in enumerate(S):
                                f[U + idx[x]] = row[pi] % q
                            gs.append(vanishes_on_fresh(f))
                        if all(gs):
                            absorbed_here = True
                            break
                if absorbed_here:
                    absorbed += 1
                else:
                    notabs += 1
                    details.append({"tau": tau, "base_pts": base_pts,
                                    "slopes": slopes, "shape": cls})
        report.append({"found": found, "absorbed": absorbed,
                       "NOT_absorbed": notabs, "counterexamples": details[:1]})
    return {"shapes": len(shapes), "report": report}


@app.local_entrypoint()
def main():
    # sample shapes from the enumerated stratum (re-enumerate quickly here)
    P, m, A = 8, 6, 4
    blocks_all = [frozenset(c) for c in itertools.combinations(range(P), A)]
    sols = []

    def rec(chosen, start, cover):
        if len(chosen) == m:
            if all(c == 3 for c in cover):
                sols.append(tuple(sorted(tuple(sorted(b)) for b in chosen)))
            return
        for bi in range(start, len(blocks_all)):
            b = blocks_all[bi]
            if any(cover[x] >= 3 for x in b):
                continue
            if any(len(b & set(c)) > 2 for c in chosen):
                continue
            for x in b:
                cover[x] += 1
            rec(chosen + [b], bi + 1, cover)
            for x in b:
                cover[x] -= 1

    b0 = blocks_all[0]
    cov = [0] * P
    for x in b0:
        cov[x] += 1
    rec([b0], 1, cov)
    rng = random.Random(2026)
    picks = rng.sample(sols, min(NJOBS * SHAPES_PER_JOB, len(sols)))
    payloads = [( [[list(b) for b in s] for s in picks[i:i + SHAPES_PER_JOB]],
                 6200 + i) for i in range(0, len(picks), SHAPES_PER_JOB)]
    results = [r for r in onlocus.map(payloads, return_exceptions=True)
               if isinstance(r, dict)]
    tot = {"found": 0, "absorbed": 0, "NOT_absorbed": 0}
    cexs = []
    for r in results:
        for rep in r["report"]:
            tot["found"] += rep["found"]
            tot["absorbed"] += rep["absorbed"]
            tot["NOT_absorbed"] += rep["NOT_absorbed"]
            cexs.extend(rep.get("counterexamples", []))
    print(f"ON-LOCUS points at p = 2^31-1: {tot}")
    if cexs:
        print("COUNTEREXAMPLE CANDIDATE (verify!):", json.dumps(cexs[0])[:400])
    with open("/tmp/f5_p3b.json", "w") as f:
        json.dump({"totals": tot, "results": results}, f, indent=1)

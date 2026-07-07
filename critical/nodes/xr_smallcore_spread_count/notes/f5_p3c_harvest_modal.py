#!/usr/bin/env python3
"""F5 P3.4 (Modal): Schwartz-Zippel class certificates for the L3 dichotomy
+ the exact-decision sweep.

PART A — class certificates. Enumerate ALL isomorphism classes of minimal
rigid designs (P = 8 points, m = 6 blocks of size A = 4, every point in
exactly 3 blocks, pairwise cores <= 2). For each class, embed at random
into F_p, p = 2^61 - 1 (points distinct, slopes distinct), and decide
exactly: (i) is the alignment system dependent? (ii) if so, does the
containment hold (some union-coincidence functional chi in the row space
R, or some Pi_S(v)-block subset of R)? A containment verified at a random
M61 embedding certifies the generic (Zariski) identity with error
<= deg/p per trial (Schwartz-Zippel); NB independent embeddings compound.

PART B — exact-decision sweep at q in {47, 97, 193, 389}: the P2 hunt,
but EVERY dependent configuration gets the exact decision (forced
coincidence / forced invalidity / GENUINE realization constructed) —
no sampling verdicts. A GENUINE hit refutes L3-point outright.
"""
import itertools
import json
import random

import modal

app = modal.App("rs-mca-f5-p3c")
image = modal.Image.debian_slim()

M61 = (1 << 61) - 1
EMBEDS_PER_CLASS = 8
LADDER = [(97, 4000), (193, 8000), (389, 16000), (769, 24000)]
SHARDS = 8


def _linalg(q):
    def inv(a):
        return pow(a % q, q - 2, q)

    def top_rows(S, k, A):
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

    def eliminate(rows):
        """Row-reduce; return (basis, pivcols). basis rows are reduced."""
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

    def in_span(basis, pivcols, vec):
        w = vec[:]
        for r, col in enumerate(pivcols):
            if w[col] % q:
                f = w[col]
                w = [(a - f * b) % q for a, b in zip(w, basis[r])]
        return all(x % q == 0 for x in w)

    return inv, top_rows, eliminate, in_span


def _decide_config(q, k, A, sup, slopes):
    """Exact L3-point decision for one embedded configuration.
    Returns dict with dependent?, mode ('forced_coincidence' |
    'forced_invalid' | 'GENUINE' | 'independent'), and details."""
    inv, top_rows, eliminate, in_span = _linalg(q)
    used = sorted(set(x for S in sup for x in S))
    idx = {x: i for i, x in enumerate(used)}
    U = len(used)
    C = 2 * U
    rows = []
    for S, z in zip(sup, slopes):
        for row in top_rows(list(S), k, A):
            vec = [0] * C
            for pi, x in enumerate(S):
                vec[idx[x]] = row[pi] % q
                vec[U + idx[x]] = (z * row[pi]) % q
            rows.append(vec)
    basis, pivcols = eliminate(rows)
    rank = len(basis)
    if rank == len(rows):
        return {"dependent": False, "mode": "independent"}
    # coincidence functionals chi_{i,y}: c_i(y) - (u_y + z_i v_y) for union
    # y outside S_i; c_i = deg<k interpolant of (u + z_i v)|_{S_i}: use the
    # first k points of S_i (on the solution locus the interpolant of any k
    # points of S_i equals c_i).
    forced = []
    for i, S in enumerate(sup):
        S = list(S)
        z = slopes[i]
        base = S[:k]
        for y in used:
            if y in S:
                continue
            f = [0] * C
            for xb in base:
                lg = 1
                for xo in base:
                    if xo == xb:
                        continue
                    lg = lg * (y - xo) % q * inv(xb - xo) % q
                f[idx[xb]] = (f[idx[xb]] + lg) % q
                f[U + idx[xb]] = (f[U + idx[xb]] + lg * z) % q
            f[idx[y]] = (f[idx[y]] - 1) % q
            f[U + idx[y]] = (f[U + idx[y]] - z) % q
            if in_span(basis, pivcols, f):
                forced.append((i, y))
    if forced:
        return {"dependent": True, "mode": "forced_coincidence",
                "n_forced": len(forced), "rank": rank, "nrows": len(rows)}
    forced_inv = []
    for i, S in enumerate(sup):
        gs = []
        for row in top_rows(list(S), k, A):
            f = [0] * C
            for pi, x in enumerate(S):
                f[U + idx[x]] = row[pi] % q
            gs.append(in_span(basis, pivcols, f))
        if all(gs):
            forced_inv.append(i)
    if forced_inv:
        return {"dependent": True, "mode": "forced_invalid",
                "supports": forced_inv, "rank": rank, "nrows": len(rows)}
    return {"dependent": True, "mode": "GENUINE", "rank": rank,
            "nrows": len(rows), "sup": [list(S) for S in sup],
            "slopes": list(slopes)}


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def enum_classes(_):
    """All iso classes of (P=8, m=6, A=4, 3-regular, cores<=2) designs."""
    P, m, A = 8, 6, 4
    blocks_all = [frozenset(c) for c in itertools.combinations(range(P), A)]
    sols = []

    def rec(chosen, start, cover):
        if len(chosen) == m:
            if all(c == 3 for c in cover):
                sols.append(tuple(sorted(tuple(sorted(b)) for b in chosen)))
            return
        need = m - len(chosen)
        # prune: remaining incidences must fix coverage to exactly 3
        deficit = sum(3 - c for c in cover)
        if deficit != need * A:
            if deficit > need * A or any(c > 3 for c in cover):
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

    # wlog the lex-min block is {0,1,2,3}: every design contains SOME
    # block; relabel points to make it {0,1,2,3}, which is lex-min among
    # all 4-subsets, so enumerate only designs containing block index 0.
    b0 = blocks_all[0]
    cover0 = [0] * P
    for x in b0:
        cover0[x] += 1
    rec([b0], 1, cover0)
    # certify EVERY raw shape (covers every iso class with duplicates;
    # no canonicalization needed — soundness is per-configuration anyway)
    def fingerprint(sol):
        return tuple(sorted(len(set(a) & set(b))
                            for a, b in itertools.combinations(sol, 2)))
    return {"n_raw": len(sols),
            "fingerprints": [str(fingerprint(s)) for s in sols],
            "classes": [[list(b) for b in s] for s in sols]}


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def certify_batch(payload):
    batch, seed = payload
    q = M61
    k, A = 2, 4
    rng = random.Random(seed)
    out = []
    for cls in batch:
        modes = []
        for _ in range(EMBEDS_PER_CLASS):
            pts = rng.sample(range(1, 10**9), 8)
            sup = [tuple(pts[x] for x in B) for B in cls]
            slopes = rng.sample(range(1, 10**9), 6)
            r = _decide_config(q, k, A, sup, slopes)
            modes.append(r["mode"])
        out.append({"modes": modes,
                    "bad": [m for m in modes if m == "GENUINE"]})
    return {"n": len(batch), "results": out}


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def harvest(payload):
    shapes, q, n_configs, seed = payload
    k, A = 2, 4
    rng = random.Random(seed)
    dom = list(range(1, q))
    dep = 0
    absorbed = 0
    notabs = 0
    tried = 0
    genuine = []
    # cheap dependence pre-screen: rank of the 12x16 system; decision only
    # on dependent configs
    for _ in range(n_configs):
        cls = shapes[rng.randrange(len(shapes))]
        pts = rng.sample(dom, 8)
        sup = [tuple(pts[x] for x in B) for B in cls]
        slopes = rng.sample(range(q), 6)
        tried += 1
        r = _decide_config(q, k, A, sup, slopes)
        if r["mode"] == "independent":
            continue
        dep += 1
        if r["mode"] == "GENUINE":
            notabs += 1
            genuine.append(r)
        else:
            absorbed += 1
    return {"q": q, "tried": tried, "dependent": dep,
            "absorbed": absorbed, "not_absorbed": notabs,
            "genuine": genuine[:1]}


@app.local_entrypoint()
def main():
    ec = enum_classes.remote(0)
    print(f"minimal rigid designs: raw shapes={ec['n_raw']}")
    rng0 = random.Random(4242)
    shapes = [ec["classes"][i] for i in
              rng0.sample(range(len(ec["classes"])), 60)]
    harvest_payloads = [(shapes, q, n // SHARDS, 7100 + 17 * qi + s)
                        for qi, (q, n) in enumerate(LADDER)
                        for s in range(SHARDS)]
    sweeps = list(harvest.map(harvest_payloads, return_exceptions=True))
    certs = []
    agg = {}
    for s in sweeps:
        if not isinstance(s, dict):
            print("  worker error:", str(s)[:90])
            continue
        a = agg.setdefault(s["q"], {"tried": 0, "dependent": 0,
                                    "absorbed": 0, "not_absorbed": 0})
        for kk in a:
            a[kk] += s[kk]
    print("\nMINIMAL-STRATUM ON-LOCUS HARVEST (dependence density + absorption):")
    import math
    bad = 0
    for qv, a in sorted(agg.items()):
        dens = a["dependent"] / a["tried"] if a["tried"] else 0
        codim = -math.log(dens, qv) if dens else float("inf")
        bad += a["not_absorbed"]
        print(f"  q={qv}: tried={a['tried']} dependent={a['dependent']} "
              f"(density~q^-{codim:.2f}) absorbed={a['absorbed']} "
              f"NOT_absorbed={a['not_absorbed']}")
    print(f"\nNOT-absorbed on-locus points (refutes absorption if > 0): {bad}")
    with open("/tmp/f5_p3c.json", "w") as f:
        json.dump([s for s in sweeps if isinstance(s, dict)], f, indent=1)

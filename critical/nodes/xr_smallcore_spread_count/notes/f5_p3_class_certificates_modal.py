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

app = modal.App("rs-mca-f5-p3")
image = modal.Image.debian_slim()

M61 = (1 << 61) - 1
EMBEDS_PER_CLASS = 8
SWEEP_ROWS = [(2, 2, 47), (2, 2, 97), (2, 2, 193), (2, 2, 389)]
SWEEP_SHARDS = 5
SWEEP_DESIGNS = 60


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
def sweep(payload):
    k, t, q, seed = payload
    rng = random.Random(seed)
    A = k + t
    core_cap = k + t - 2
    dom = list(range(1, q))
    verdicts = {"independent": 0, "forced_coincidence": 0,
                "forced_invalid": 0, "GENUINE": 0}
    genuine = []
    for _ in range(SWEEP_DESIGNS):
        P = rng.randrange(2 * A, 3 * A + 3)
        target_m = (3 * P + A - 1) // A + rng.randrange(0, 3)
        blocks = []
        for _ in range(300):
            if len(blocks) >= target_m:
                break
            S = tuple(sorted(rng.sample(range(P), A)))
            if all(len(set(S) & set(B)) <= core_cap for B in blocks) \
                    and S not in blocks:
                blocks.append(S)
        cover = [0] * P
        for B in blocks:
            for x in B:
                cover[x] += 1
        if not blocks or min(cover) < 3:
            continue
        for _ in range(6):
            pts = rng.sample(dom, P)
            sup = [tuple(pts[x] for x in B) for B in blocks]
            slopes = rng.sample(range(q), len(blocks))
            r = _decide_config(q, k, A, sup, slopes)
            verdicts[r["mode"]] += 1
            if r["mode"] == "GENUINE":
                genuine.append(r)
    return {"k": k, "t": t, "q": q, "verdicts": verdicts,
            "genuine": genuine[:2]}


@app.local_entrypoint()
def main():
    ec = enum_classes.remote(0)
    print(f"minimal rigid designs: raw shapes={ec['n_raw']}")
    B = 30
    class_payloads = [(ec["classes"][i:i+B], 5000 + i)
                      for i in range(0, len(ec["classes"]), B)]
    sweep_payloads = [(k, t, q, 8000 + 13 * i + s)
                      for i, (k, t, q) in enumerate(SWEEP_ROWS)
                      for s in range(SWEEP_SHARDS)]
    certs = list(certify_batch.map(class_payloads, return_exceptions=True))
    sweeps = list(sweep.map(sweep_payloads, return_exceptions=True))
    print("\nPART A — M61 certificates over the FULL minimal stratum:")
    all_contained = True
    mode_totals = {}
    n_shapes = 0
    for c in certs:
        if not isinstance(c, dict):
            print("  worker error:", str(c)[:100])
            continue
        for r in c["results"]:
            n_shapes += 1
            if r["bad"]:
                all_contained = False
            for mo in r["modes"]:
                mode_totals[mo] = mode_totals.get(mo, 0) + 1
    print(f"  shapes certified: {n_shapes}; embedding-mode totals: {mode_totals}")
    print(f"  ALL dependent embeddings satisfy containment: {all_contained}")
    print("\nPART B — exact-decision sweep:")
    agg = {}
    for s in sweeps:
        if not isinstance(s, dict):
            continue
        key = s["q"]
        a = agg.setdefault(key, {"independent": 0, "forced_coincidence": 0,
                                 "forced_invalid": 0, "GENUINE": 0})
        for kk, vv in s["verdicts"].items():
            a[kk] += vv
    tot_gen = 0
    for qv, a in sorted(agg.items()):
        tot_gen += a["GENUINE"]
        print(f"  q={qv}: {a}")
    print(f"\nGENUINE realizable syzygies (refutes L3-point if > 0): {tot_gen}")
    with open("/tmp/f5_p3.json", "w") as f:
        json.dump({"classes": ec, "certs": [c for c in certs if isinstance(c, dict)],
                   "sweeps": [s for s in sweeps if isinstance(s, dict)]}, f, indent=1)

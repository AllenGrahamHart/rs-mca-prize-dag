#!/usr/bin/env python3
"""wz F-round 1 against WCL-ZONE-COVERAGE: exact primitive signed-shift
orbit ledger census on analogue rows (q, n'=2N, L), per wz_falsifiers.md.

Runs on a Modal worker via tools/modal_run_script.py; shard name in argv[1].
Shards: pc_l1 | pc_l2 | band_a17 | band_a19 | band_a21 | band_a23 |
        band_b10 | band_b1214 | band_c | xcheck64

Conventions pinned in wz_falsifiers.md section 0 (M2 code shapes reused:
primitive_root, level conditions, primitivity, signed-shift orbits from
m2_c1prime_level_scaled_modal.py; shadow solver from round 7; lift identity
from ORBIT_CENSUS_SUMMARY item 5). All verdict arithmetic exact.
"""
import itertools
import json
import sys
import time
from fractions import Fraction

import numpy as np

T0 = time.time()
AUX_PRIMES = [1000003, 1000033, 1000037, 1000039, 1000081]

# ---------------------------------------------------------------- utilities

MR_BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in MR_BASES:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in MR_BASES:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def first_primes_1mod(nprime: int, lo: int, count: int) -> list:
    out = []
    k = (lo - 1 + nprime - 1) // nprime
    while len(out) < count:
        q = k * nprime + 1
        if q >= lo and is_prime(q):
            out.append(q)
        k += 1
    return out


def primitive_root(q: int) -> int:
    # verbatim shape: m2_c1prime_level_scaled_modal.py lines 31-45
    remaining = q - 1
    factors = set()
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors.add(divisor)
            remaining //= divisor
        divisor += 1
    if remaining > 1:
        factors.add(remaining)
    candidate = 2
    while any(pow(candidate, (q - 1) // factor, q) == 1 for factor in factors):
        candidate += 1
    return candidate


def row_powers(q: int, N: int, L: int) -> list:
    nprime = 2 * N
    assert (q - 1) % nprime == 0, (q, nprime)
    omega = pow(primitive_root(q), (q - 1) // nprime, q)
    return [[pow(omega, (2 * l - 1) * y, q) for y in range(N)]
            for l in range(1, L + 1)], omega


# vectors are dicts pos->coef rendered as tuples ((pos, coef), ...) sorted.

def normalize(vec: tuple) -> tuple:
    # first (lowest-position) nonzero coefficient +1
    if vec and vec[0][1] < 0:
        return tuple((p, -c) for p, c in vec)
    return vec


def shift1(vec: tuple, N: int) -> tuple:
    out = []
    for p, c in vec:
        p2 = p + 1
        if p2 == N:
            out.append((0, -c))
        else:
            out.append((p2, c))
    return tuple(sorted(out))


def eval_levels(vec: tuple, powers: list, q: int) -> list:
    return [sum(c * pw[p] for p, c in vec) % q for pw in powers]


def is_primitive(vec: tuple, powers: list, q: int) -> bool:
    # M2 shape (lines 96-131): a proper signed sub-vector kills primitivity
    # iff EVERY level evaluates to zero on it.
    w = len(vec)
    for mask in range(1, (1 << w) - 1):
        sub = tuple(vec[i] for i in range(w) if (mask >> i) & 1)
        if all(v == 0 for v in eval_levels(sub, powers, q)):
            return False
    return True


def orbit_partition(hits: set, N: int, powers: list, q: int):
    """Partition normalized hit set into signed-shift orbits.

    Returns (orbits: list of representative vec (lex-min normalized member),
    per-orbit member counts, flags). Asserts closure: every normalized shift
    of a hit is itself a hit (completeness invariant)."""
    remaining = set(hits)
    orbits = []
    flags = []
    while remaining:
        v0 = remaining.pop()
        members = {v0}
        v = v0
        for _ in range(2 * N):
            v = normalize(shift1(v, N))
            members.add(v)
        missing = [m for m in members if m not in hits]
        if missing:
            flags.append("ORBIT_CLOSURE_MISS")
        remaining -= members
        rep = min(members)
        orbits.append((rep, len(members)))
        if len(members) != N and len(members) != 2 * N:
            flags.append("DEGENERATE_ORBIT_%d" % len(members))
    return orbits, flags


# ------------------------------------------------------------- enumerators

def _full_join(ka: np.ndarray, tb: np.ndarray):
    """all index pairs (i into ka, j into tb) with ka[i]==tb[j]."""
    order = np.argsort(tb, kind="stable")
    tbs = tb[order]
    lo = np.searchsorted(tbs, ka, "left")
    hi = np.searchsorted(tbs, ka, "right")
    cnt = hi - lo
    ia = np.repeat(np.arange(len(ka)), cnt)
    if len(ia) == 0:
        return ia, ia
    starts = np.repeat(lo, cnt)
    offs = np.arange(len(ia)) - np.repeat(np.cumsum(cnt) - cnt, cnt)
    jb = order[starts + offs]
    return ia, jb


def _side(N, k, powers_np, q, first_plus):
    combos = np.array(list(itertools.combinations(range(N), k)),
                      dtype=np.int64)
    if first_plus:
        signs = np.array(list(itertools.product((1, -1), repeat=k - 1)),
                         dtype=np.int64) if k > 1 else np.zeros((1, 0),
                                                                dtype=np.int64)
        signs = np.hstack([np.ones((len(signs), 1), dtype=np.int64), signs])
    else:
        signs = np.array(list(itertools.product((1, -1), repeat=k)),
                         dtype=np.int64)
    vals = [(pw[combos] @ signs.T) % q for pw in powers_np]  # (nc, ns) each
    return combos, signs, vals


def enumerate_mitm(q, N, L, weights, powers):
    """set of normalized weight-w level-L vanishers, all w in weights.
    Exact (per-hit re-verified with pure-python ints)."""
    powers_np = [np.array(pw, dtype=np.int64) for pw in powers]
    hits = {w: set() for w in weights}
    n_cand = 0
    for w in weights:
        a, b = w // 2, w - w // 2
        ca, sa, va = _side(N, a, powers_np, q, True)
        cb, sb, vb = _side(N, b, powers_np, q, False)
        nsa, nsb = sa.shape[0], sb.shape[0]
        if L == 1:
            ka = va[0].ravel()
            tb = (q - vb[0].ravel()) % q
        else:
            ka = va[0].ravel() * q + va[1].ravel()
            tb = ((q - vb[0].ravel()) % q) * q + ((q - vb[1].ravel()) % q)
        ia, jb = _full_join(ka, tb)
        n_cand += len(ia)
        if len(ia) == 0:
            continue
        ai, bi = ia // nsa, jb // nsb
        keep = ca[ai, -1] < cb[bi, 0]  # max(A) < min(B): disjoint + ordered
        ia, jb, ai, bi = ia[keep], jb[keep], ai[keep], bi[keep]
        asig, bsig = ia % nsa, jb % nsb
        for t in range(len(ia)):
            vec = tuple(
                [(int(p), int(c)) for p, c in zip(ca[ai[t]], sa[asig[t]])] +
                [(int(p), int(c)) for p, c in zip(cb[bi[t]], sb[bsig[t]])])
            if any(v != 0 for v in eval_levels(vec, powers, q)):
                raise AssertionError("MITM_FALSE_HIT %s q=%d" % (vec, q))
            hits[w].add(vec)
    assert n_cand > 0, "EMPTY_CANDIDATE_STREAM q=%d" % q  # catch 137
    return hits


def enumerate_direct(q, N, L, weights, powers, chunk=120_000):
    """M2-shape chunked enumerator (masks over all levels)."""
    powers_np = [np.array(pw, dtype=np.int64) for pw in powers]
    hits = {w: set() for w in weights}
    n_pairs = 0
    for w in weights:
        signs = np.array(list(itertools.product((1, -1), repeat=w - 1)),
                         dtype=np.int64)
        signs = np.hstack([np.ones((len(signs), 1), dtype=np.int64), signs])
        it = itertools.combinations(range(N), w)
        while True:
            block = list(itertools.islice(it, chunk))
            if not block:
                break
            sup = np.asarray(block, dtype=np.int64)
            n_pairs += len(sup) * len(signs)
            mask = (powers_np[0][sup] @ signs.T) % q == 0
            if L > 1 and mask.any():
                idx = np.argwhere(mask)
                for pw in powers_np[1:]:
                    vals = (pw[sup[idx[:, 0]]] * signs[idx[:, 1]]).sum(1) % q
                    idx = idx[vals == 0]
                mask = np.zeros_like(mask)
                mask[idx[:, 0], idx[:, 1]] = True
            for si, gi in np.argwhere(mask):
                vec = tuple((int(p), int(c))
                            for p, c in zip(sup[si], signs[gi]))
                if any(v != 0 for v in eval_levels(vec, powers, q)):
                    raise AssertionError("DIRECT_FALSE_HIT q=%d" % q)
                hits[w].add(vec)
    assert n_pairs > 0, "EMPTY_ENUMERATION q=%d" % q
    return hits


# ------------------------------------------------------- ledger and dedup

def ledger_census(q, N, L, powers, hits):
    """orbit partition + primitivity per orbit representative."""
    weights = sorted(hits)
    full, prim, reps, flags = {}, {}, {}, []
    for w in weights:
        orbs, fl = orbit_partition(hits[w], N, powers, q)
        flags += fl
        full[w] = len(orbs)
        pr = [rep for rep, _ in orbs if is_primitive(rep, powers, q)]
        prim[w] = len(pr)
        reps[w] = sorted(pr)
    wcl = sum((Fraction(prim[w] * 2 * N, 2 ** w) for w in weights),
              Fraction(0))
    return full, prim, reps, wcl, flags


def mult_matrix(vec, N):
    """NxN integer left-multiplication matrix of vec in Z[z]/(z^N+1)."""
    M = np.zeros((N, N), dtype=np.int64)
    for k in range(N):
        for p, c in vec:
            p2 = p + k
            if p2 >= N:
                M[p2 - N, k] = -c
            else:
                M[p2, k] = c
    return M


def inv_mod(M, p):
    n = len(M)
    A = np.concatenate([M % p, np.eye(n, dtype=np.int64)], axis=1)
    for col in range(n):
        piv = None
        for r in range(col, n):
            if A[r, col] % p:
                piv = r
                break
        if piv is None:
            return None
        A[[col, piv]] = A[[piv, col]]
        A[col] = A[col] * pow(int(A[col, col]), p - 2, p) % p
        for r in range(n):
            if r != col and A[r, col]:
                A[r] = (A[r] - A[r, col] * A[col]) % p
    return A[:, n:]


def vec_dense(vec, N):
    d = np.zeros(N, dtype=np.int64)
    for p, c in vec:
        d[p] = c
    return d


def shadow_pairs(orbit_list, N, sources=None):
    """round-7 ternary-multiplier detection. orbit_list: list of vec
    (sorted by (weight,key)). Returns list of (i,j) shadow links."""
    links = []
    n = len(orbit_list)
    dense = [vec_dense(v, N) for v in orbit_list]
    targets_of = []
    for j in range(n):
        cols = []
        M = mult_matrix(orbit_list[j], N)
        for s in range(N):
            col = M[:, s]  # z^s * P_j
            cols.append(col)
            cols.append(-col)
        targets_of.append(np.array(cols).T)  # N x 2N
    src = range(n) if sources is None else sources
    for i in src:
        Mi = mult_matrix(orbit_list[i], N)
        inv = None
        for p in AUX_PRIMES:
            inv = inv_mod(Mi, p)
            if inv is not None:
                break
        if inv is None:
            links.append(("SINGULAR", i))
            continue
        for j in range(n):
            if j == i:
                continue
            X = inv @ (targets_of[j] % p) % p
            tern = np.all((X == 0) | (X == 1) | (X == p - 1), axis=0)
            for s in np.nonzero(tern)[0]:
                m = np.where(X[:, s] == p - 1, -1, X[:, s]).astype(np.int64)
                if np.array_equal(Mi @ m, targets_of[j][:, s]):  # exact Z
                    links.append((i, j))
                    break
    return links


def shadow_dedup(reps_by_w, N):
    """first-owner dedup across the window. Returns (owners_by_w, n_links,
    skipped_flag)."""
    ordered = []
    for w in sorted(reps_by_w):
        for rep in reps_by_w[w]:
            ordered.append((w, rep))
    n = len(ordered)
    if n < 2:
        return {w: list(reps_by_w[w]) for w in reps_by_w}, 0, False
    if n > 24:
        return {w: list(reps_by_w[w]) for w in reps_by_w}, 0, True
    links = shadow_pairs([r for _, r in ordered], N)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    real = [l for l in links if l[0] != "SINGULAR"]
    for i, j in real:
        parent[find(j)] = find(i)
    owners = {}
    for idx in range(n):
        r = find(idx)
        owners.setdefault(r, idx)
        owners[r] = min(owners[r], idx)
    keep = set(owners.values())
    out = {w: [] for w in reps_by_w}
    for idx in keep:
        w, rep = ordered[idx]
        out[w].append(rep)
    return out, len(real), False


def wcl_of(counts_by_w, N):
    return sum((Fraction(len(v) * 2 * N, 2 ** w) if isinstance(v, list)
                else Fraction(v * 2 * N, 2 ** w)
                for w, v in counts_by_w.items()), Fraction(0))


def fr(x: Fraction):
    return [x.numerator, x.denominator]


def vec_str(vec):
    return ",".join("%d:%+d" % (p, c) for p, c in vec)


# ------------------------------------------------------------------ shards

BANKED_M2 = {  # from m2_c1prime_level_scaled_results.json (primitive orbits)
    (1, 193): {2: 0, 3: 3, 4: 46, 5: 529, 6: 4497},
    (1, 449): {2: 0, 3: 1, 4: 20, 5: 228, 6: 1981},
    (1, 769): {2: 0, 3: 0, 4: 10, 5: 144, 6: 1193},
    (1, 1409): {2: 0, 3: 0, 4: 4, 5: 79, 6: 660},
    (1, 3137): {2: 0, 3: 0, 4: 2, 5: 33, 6: 294},
    (1, 5569): {2: 0, 3: 0, 4: 1, 5: 17, 6: 153},
    (1, 7937): {2: 0, 3: 2, 4: 8, 5: 31, 6: 126},
    (1, 12289): {2: 0, 3: 0, 4: 0, 5: 9, 6: 71},
    (2, 193): {3: 0, 4: 0, 5: 4, 6: 24, 7: 176},
    (2, 257): {3: 0, 4: 0, 5: 3, 6: 15, 7: 92},
    (2, 449): {3: 0, 4: 0, 5: 0, 6: 1, 7: 33},
    (2, 577): {3: 0, 4: 0, 5: 1, 6: 3, 7: 19},
}
BANKED_WCL = {
    (1, 193): (5763, 1), (1, 449): (2525, 1), (1, 769): (1521, 1),
    (1, 1409): (834, 1), (1, 3137): (368, 1), (1, 5569): (191, 1),
    (1, 7937): (236, 1), (1, 12289): (89, 1),
    (2, 193): (120, 1), (2, 257): (67, 1), (2, 449): (35, 2),
    (2, 577): (29, 2),
}
BANKED_M1_FULL_W6 = {193: 4712, 7937: 224}  # m1_dli_m1_results.json V_orbits


def cell_report(q, N, L, band, engine, do_shadow=True):
    weights = list(range(L + 1, L + 6))
    powers, _ = row_powers(q, N, L)
    if engine == "mitm":
        hits = enumerate_mitm(q, N, L, weights, powers)
    else:
        hits = enumerate_direct(q, N, L, weights, powers)
    full, prim, reps, wcl, flags = ledger_census(q, N, L, powers, hits)
    rep = {"q": q, "N": N, "L": L, "band": band, "engine": engine,
           "full": {str(w): full[w] for w in weights},
           "prim": {str(w): prim[w] for w in weights},
           "Wcl": fr(wcl), "flags": flags}
    if do_shadow:
        owners, nlinks, skipped = shadow_dedup(reps, N)
        wcl_d = wcl_of(owners, N)
        rep["shadow"] = {"links": nlinks, "skipped": skipped,
                         "Wcl_dedup": fr(wcl_d),
                         "owners": {str(w): len(owners[w]) for w in weights}}
    tot = sum(prim.values())
    if 1 <= tot <= 24:
        rep["orbit_reps"] = [vec_str(r) for w in weights for r in reps[w]]
    return rep, reps, hits


def shard_pc_l1():
    out = {"shard": "pc_l1", "cells": [], "controls": {}}
    ok = True
    for q in (193, 449, 769, 1409, 3137, 5569, 7937, 12289):
        rep, reps, hits = cell_report(q, 32, 1, "PC", "direct")
        b = BANKED_M2[(1, q)]
        match = all(rep["prim"][str(w)] == b[w] for w in b)
        wb = BANKED_WCL[(1, q)]
        match &= tuple(rep["Wcl"]) == wb
        rep["banked_match"] = match
        ok &= match
        # mitm replay: hit-set equality
        powers, _ = row_powers(q, 32, 1)
        hits_m = enumerate_mitm(q, 32, 1, list(range(2, 7)), powers)
        rep["mitm_equal"] = all(hits_m[w] == hits[w] for w in hits)
        ok &= rep["mitm_equal"]
        if q in BANKED_M1_FULL_W6:  # M-1 mutation control
            rep["m1_full_w6"] = rep["full"]["6"]
            rep["m1_control"] = (rep["full"]["6"] == BANKED_M1_FULL_W6[q]
                                 and rep["full"]["6"] != rep["prim"]["6"])
            ok &= rep["m1_control"]
        if q == 7937:  # M-2 shadow trip control
            ordered = [(w, r) for w in sorted(reps) for r in reps[w]]
            vecs = [r for _, r in ordered]
            srcs = [i for i, (w, _) in enumerate(ordered) if w == 3]
            links = [l for l in shadow_pairs(vecs, 32, sources=srcs)
                     if l[0] != "SINGULAR"]
            trip = len(links) > 0
            if not trip:  # synthetic must trip
                base = vecs[0]
                prod = {}
                for p, c in base:  # (1+z)*base
                    prod[p] = prod.get(p, 0) + c
                    p2, c2 = (p + 1, c) if p + 1 < 32 else (0, -c)
                    prod[p2] = prod.get(p2, 0) + c2
                synth = normalize(tuple(sorted(
                    (p, c) for p, c in prod.items() if c)))
                sl = shadow_pairs([base, synth], 32, sources=[0])
                trip = ("synthetic", any(l[0] != "SINGULAR" for l in sl))
                ok &= trip[1]
            out["controls"]["M2_shadow_trip"] = str(trip)
        out["cells"].append(rep)
        print("PC L=1 q=%d prim=%s banked=%s mitm=%s t=%.0fs" %
              (q, rep["prim"], rep["banked_match"], rep["mitm_equal"],
               time.time() - T0))
    out["ok"] = ok
    return out


def shard_pc_l2():
    out = {"shard": "pc_l2", "cells": [], "controls": {}}
    ok = True
    for q in (193, 257, 449, 577):
        rep, reps, hits = cell_report(q, 32, 2, "PC", "direct")
        b = BANKED_M2[(2, q)]
        match = all(rep["prim"][str(w)] == b[w] for w in b)
        match &= tuple(rep["Wcl"]) == BANKED_WCL[(2, q)]
        rep["banked_match"] = match
        ok &= match
        powers, _ = row_powers(q, 32, 2)
        hits_m = enumerate_mitm(q, 32, 2, list(range(3, 8)), powers)
        rep["mitm_equal"] = all(hits_m[w] == hits[w] for w in hits)
        ok &= rep["mitm_equal"]
        out["cells"].append(rep)
        print("PC L=2 q=%d prim=%s banked=%s mitm=%s t=%.0fs" %
              (q, rep["prim"], rep["banked_match"], rep["mitm_equal"],
               time.time() - T0))
    out["ok"] = ok
    return out


def band_shard(name, N, L, bands, count, nprime):
    out = {"shard": name, "cells": []}
    for b in bands:
        qs = first_primes_1mod(nprime, 2 ** b, count)
        for q in qs:
            rep, _, _ = cell_report(q, N, L, "b%d" % b, "mitm")
            out["cells"].append(rep)
        nonempty = sum(1 for c in out["cells"]
                       if c["band"] == "b%d" % b
                       and sum(c["prim"].values()) > 0)
        print("band %s b=%d done: %d/%d nonempty t=%.0fs" %
              (name, b, nonempty, count, time.time() - T0))
    return out


def shard_band_c():
    """N=64 cells + N=32 companions + level-lift dedup + trip control."""
    out = {"shard": "band_c", "cells": []}
    for b in (21, 23, 25, 27):
        qs = first_primes_1mod(128, 2 ** b, 10)
        for q in qs:
            rep, reps64, hits64 = cell_report(q, 64, 1, "b%d" % b, "mitm")
            # companion N=32 row (admissible: q < 2^32, N=32 >= 16)
            powers32, _ = row_powers(q, 32, 1)
            hits32 = enumerate_mitm(q, 32, 1, list(range(2, 7)), powers32)
            f32, p32, reps32, wcl32, fl32 = ledger_census(
                q, 32, 1, powers32, hits32)
            rep["companion_prim"] = {str(w): p32[w] for w in p32}
            # lift: double every companion orbit rep; must appear in N=64
            powers64, _ = row_powers(q, 64, 1)
            owned = set()
            miss = 0
            all64 = {r for w in reps64 for r in reps64[w]}
            orbmap = {}
            for w in reps64:
                for r in reps64[w]:
                    members = {r}
                    v = r
                    for _ in range(128):
                        v = normalize(shift1(v, 64))
                        members.add(v)
                    for m in members:
                        orbmap[m] = r
            for w in reps32:
                for r32 in reps32[w]:
                    d = normalize(tuple(sorted((2 * p, c) for p, c in r32)))
                    if d in orbmap:
                        owned.add(orbmap[d])
                    else:
                        miss += 1
            rep["lift"] = {"companion_orbits": sum(p32.values()),
                           "owned64": len(owned), "miss": miss}
            deduped = {w: [r for r in reps64[w] if r not in owned]
                       for w in reps64}
            rep["Wcl_liftdedup"] = fr(wcl_of(deduped, 64))
            out["cells"].append(rep)
        print("band_c b=%d done t=%.0fs" % (b, time.time() - T0))
    return out


def shard_xcheck64(b=25):
    # w=6 direct at N=64 is out of the shard budget (C(64,6)=7.5e7 python
    # tuple stream); direct-vs-mitm equality is checked at w=2..5 here and
    # at ALL window weights on the 12 PC cells (N=32). w=6 N=64
    # completeness additionally guarded by orbit-closure + lift controls.
    # b=21 rerun (xcheck64b): the b=25 first prime has an empty w<=5
    # window (orbit-clustered Poisson), so equality there is vacuous.
    q = first_primes_1mod(128, 2 ** b, 1)[0]
    powers, _ = row_powers(q, 64, 1)
    weights = list(range(2, 6))
    hits_d = enumerate_direct(q, 64, 1, weights, powers, chunk=200_000)
    print("direct done q=%d t=%.0fs" % (q, time.time() - T0))
    hits_m = enumerate_mitm(q, 64, 1, weights, powers)
    eq = all(hits_d[w] == hits_m[w] for w in weights)
    full, prim, reps, wcl, flags = ledger_census(q, 64, 1, powers, hits_d)
    return {"shard": "xcheck64", "q": q, "equal": eq,
            "n_hits": {str(w): len(hits_d[w]) for w in weights},
            "prim": {str(w): prim[w] for w in prim}, "Wcl": fr(wcl),
            "flags": flags}


def main():
    shard = sys.argv[1]
    if shard == "pc_l1":
        res = shard_pc_l1()
    elif shard == "pc_l2":
        res = shard_pc_l2()
    elif shard == "band_a17":
        res = band_shard("band_a17", 32, 1, (17,), 48, 64)
    elif shard == "band_a19":
        res = band_shard("band_a19", 32, 1, (19,), 48, 64)
    elif shard == "band_a21":
        res = band_shard("band_a21", 32, 1, (21,), 48, 64)
    elif shard == "band_a23":
        res = band_shard("band_a23", 32, 1, (23,), 48, 64)
    elif shard == "band_b10":
        res = band_shard("band_b10", 32, 2, (10,), 24, 64)
    elif shard == "band_b1214":
        res = band_shard("band_b1214", 32, 2, (12, 14), 24, 64)
    elif shard == "band_c":
        res = shard_band_c()
    elif shard == "xcheck64":
        res = shard_xcheck64()
    elif shard == "xcheck64b":
        res = shard_xcheck64(21)
        res["shard"] = "xcheck64b"
    else:
        raise SystemExit("unknown shard " + shard)
    res["wall_s"] = round(time.time() - T0, 1)
    print("WZ_JSON " + json.dumps(res, separators=(",", ":")))


if __name__ == "__main__":
    main()

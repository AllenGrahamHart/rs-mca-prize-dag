#!/usr/bin/env python3
"""wz2 F-round 2 against WCL-ZONE-COVERAGE (dli_wcl_zone_coverage).

Shard name in argv[1]. Runs on Modal via tools/modal_run_script.py.
Pre-registration: wz2_falsifiers.md; dedup convention: wz2_dedup_spec.md.

Reused VERBATIM from round-1 wz_census_modal.py (itself pinned to the M2
code shapes; #137 anti-drift): is_prime, first_primes_1mod, primitive_root,
row_powers, normalize, shift1, eval_levels, is_primitive, orbit_partition
(flag strings now carry the orbit rep), _full_join, _side (plus a combo
cache), enumerate_direct, mult_matrix, inv_mod, vec_dense, fr, vec_str,
r1_shadow_pairs/r1_shadow_dedup (round-1 convention, kept for replay).
NEW (pre-declared in wz2_falsifiers.md section 0): L<=3 mitm key packing,
tag classifier, canonical dedup module (division + weight-<=3 singular
sweep + lift pass, lift-first composition), #137 guard redesign.
All verdict-path arithmetic exact (ints mod q, fractions.Fraction).
"""
import itertools
import json
import math
import sys
import time
from fractions import Fraction

import numpy as np

T0 = time.time()
AUX_PRIMES = [1000003, 1000033, 1000037, 1000039, 1000081]
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


def row_powers(q: int, N: int, L: int):
    nprime = 2 * N
    assert (q - 1) % nprime == 0, (q, nprime)
    omega = pow(primitive_root(q), (q - 1) // nprime, q)
    return [[pow(omega, (2 * l - 1) * y, q) for y in range(N)]
            for l in range(1, L + 1)], omega


def normalize(vec: tuple) -> tuple:
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
    w = len(vec)
    for mask in range(1, (1 << w) - 1):
        sub = tuple(vec[i] for i in range(w) if (mask >> i) & 1)
        if all(v == 0 for v in eval_levels(sub, powers, q)):
            return False
    return True


def orbit_members(vec: tuple, N: int) -> set:
    members = {vec}
    v = vec
    for _ in range(2 * N - 1):
        v = normalize(shift1(v, N))
        members.add(v)
    return members


def vec_str(vec):
    return ",".join("%d:%+d" % (p, c) for p, c in vec)


def parse_vec(s):
    out = []
    for part in s.split(","):
        p, c = part.split(":")
        out.append((int(p), int(c)))
    return tuple(out)


def orbit_partition(hits: set, N: int, powers: list, q: int):
    remaining = set(hits)
    orbits = []
    flags = []
    while remaining:
        v0 = remaining.pop()
        members = orbit_members(v0, N)
        rep = min(members)
        missing = [m for m in members if m not in hits]
        if missing:
            flags.append("ORBIT_CLOSURE_MISS|" + vec_str(rep))
        remaining -= members
        orbits.append((rep, len(members)))
        if len(members) != N and len(members) != 2 * N:
            flags.append("DEGENERATE_ORBIT_%d|%s" % (len(members),
                                                     vec_str(rep)))
    return orbits, flags


_COMBO_CACHE = {}


def _combos(N, k):
    key = (N, k)
    if key not in _COMBO_CACHE:
        _COMBO_CACHE[key] = np.array(
            list(itertools.combinations(range(N), k)), dtype=np.int64)
    return _COMBO_CACHE[key]


def _full_join(ka: np.ndarray, tb: np.ndarray):
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
    combos = _combos(N, k)
    if first_plus:
        signs = np.array(list(itertools.product((1, -1), repeat=k - 1)),
                         dtype=np.int64) if k > 1 else np.zeros(
                             (1, 0), dtype=np.int64)
        signs = np.hstack([np.ones((len(signs), 1), dtype=np.int64), signs])
    else:
        signs = np.array(list(itertools.product((1, -1), repeat=k)),
                         dtype=np.int64)
    vals = [(pw[combos] @ signs.T) % q for pw in powers_np]
    return combos, signs, vals


def enumerate_mitm(q, N, L, weights, powers):
    """Normalized weight-w level-L vanishers; L in {1,2,3}; key packing
    exact in int64 (guard q^L < 2^62). Returns (hits, n_cand). #137 guard
    redesign (wz2_falsifiers.md 0.3): sides asserted nonempty per cell;
    candidate totals enforced at band level by callers."""
    assert q ** L < 2 ** 62, (q, L)
    powers_np = [np.array(pw, dtype=np.int64) for pw in powers]
    hits = {w: set() for w in weights}
    n_cand = 0
    for w in weights:
        a, b = w // 2, w - w // 2
        ca, sa, va = _side(N, a, powers_np, q, True)
        cb, sb, vb = _side(N, b, powers_np, q, False)
        assert len(ca) > 0 and len(cb) > 0, ("EMPTY_SIDE", q, N, w)
        nsa, nsb = sa.shape[0], sb.shape[0]
        ka = va[0].ravel().copy()
        tb = ((q - vb[0].ravel()) % q).copy()
        for lv in range(1, L):
            ka = ka * q + va[lv].ravel()
            tb = tb * q + (q - vb[lv].ravel()) % q
        ia, jb = _full_join(ka, tb)
        n_cand += len(ia)
        if len(ia) == 0:
            continue
        ai, bi = ia // nsa, jb // nsb
        keep = ca[ai, -1] < cb[bi, 0]
        ia, jb, ai, bi = ia[keep], jb[keep], ai[keep], bi[keep]
        asig, bsig = ia % nsa, jb % nsb
        for t in range(len(ia)):
            vec = tuple(
                [(int(p), int(c)) for p, c in zip(ca[ai[t]], sa[asig[t]])] +
                [(int(p), int(c)) for p, c in zip(cb[bi[t]], sb[bsig[t]])])
            if any(v != 0 for v in eval_levels(vec, powers, q)):
                raise AssertionError("MITM_FALSE_HIT %s q=%d" % (vec, q))
            hits[w].add(vec)
    return hits, n_cand


def enumerate_direct(q, N, L, weights, powers, chunk=120_000):
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


def ledger_census(q, N, L, powers, hits):
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


def fr(x: Fraction):
    return [x.numerator, x.denominator]


def frs(x: Fraction):
    return "%d/%d" % (x.numerator, x.denominator)


def parse_fr(s):
    a, b = s.split("/")
    return Fraction(int(a), int(b))


def wcl_of(reps_by_w, N):
    return sum((Fraction(len(v) * 2 * N, 2 ** w)
                for w, v in reps_by_w.items()), Fraction(0))


# ------------------------------------------------- round-1 convention (kept)

def r1_shadow_pairs(orbit_list, N, sources=None):
    links = []
    n = len(orbit_list)
    targets_of = []
    for j in range(n):
        cols = []
        M = mult_matrix(orbit_list[j], N)
        for s in range(N):
            col = M[:, s]
            cols.append(col)
            cols.append(-col)
        targets_of.append(np.array(cols).T)
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
                if np.array_equal(Mi @ m, targets_of[j][:, s]):
                    links.append((i, j))
                    break
    return links


def r1_shadow_dedup(reps_by_w, N):
    ordered = []
    for w in sorted(reps_by_w):
        for rep in reps_by_w[w]:
            ordered.append((w, rep))
    n = len(ordered)
    if n < 2:
        return {w: list(reps_by_w[w]) for w in reps_by_w}, 0, False
    if n > 24:
        return {w: list(reps_by_w[w]) for w in reps_by_w}, 0, True
    links = r1_shadow_pairs([r for _, r in ordered], N)
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


# ------------------------------------------------------------- tags (NEW)

FACTORS = {
    48: [("Phi32", 16, {0: 1}), ("Phi96", 32, {0: 1, 16: -1})],
    96: [("Phi64", 32, {0: 1}), ("Phi192", 64, {0: 1, 32: -1})],
    24: [("Phi16", 8, {0: 1}), ("Phi48", 16, {0: 1, 8: -1})],
}
ORDER_TO_FACTOR = {48: {32: "Phi32", 96: "Phi96"},
                   96: {64: "Phi64", 192: "Phi192"},
                   24: {16: "Phi16", 48: "Phi48"}}


def poly_divisible(vec, N, deg, lower):
    rem = [0] * N
    for p, c in vec:
        rem[p] = c
    for i in range(N - 1, deg - 1, -1):
        c = rem[i]
        if c:
            rem[i] = 0
            for pos, coef in lower.items():
                rem[i - deg + pos] -= c * coef
    return all(x == 0 for x in rem[:deg])


def tag_of(vec, N):
    out = []
    for name, deg, lower in FACTORS.get(N, []):
        if poly_divisible(vec, N, deg, lower):
            out.append(name)
    return tuple(sorted(out))


def uncovered_count(tags, N, L):
    if N not in ORDER_TO_FACTOR:
        return L
    u = 0
    for l in range(1, L + 1):
        d = 2 * N // math.gcd(2 * l - 1, 2 * N)
        if ORDER_TO_FACTOR[N].get(d) not in tags:
            u += 1
    return u


def resultant_check(vec, N, L, q):
    """C-7: for each uncovered level with point of order d, q must divide
    the exact integer resultant Res(Phi_d, P) and Res must be nonzero
    (Res == 0 would mean a missed tag)."""
    import sympy
    y = sympy.symbols("y")
    res = {"rep": vec_str(vec), "ok": True, "levels": []}
    tags = tag_of(vec, N)
    Ppoly = sum(c * y ** p for p, c in vec)
    for l in range(1, L + 1):
        d = 2 * N // math.gcd(2 * l - 1, 2 * N)
        fname = ORDER_TO_FACTOR.get(N, {}).get(d)
        if fname in tags:
            continue
        phi = sympy.cyclotomic_poly(d, y)
        R = int(sympy.resultant(phi, Ppoly, y))
        okl = (R != 0 and R % q == 0)
        res["levels"].append({"l": l, "d": d, "R_zero": R == 0,
                              "q_divides": R % q == 0 if R else None,
                              "ok": okl})
        res["ok"] &= okl
    return res


# --------------------------------------- canonical dedup module (NEW, spec)

_TMULT_CACHE = {}


def ternary_mult_bank(N, wmax=3):
    if N in _TMULT_CACHE:
        return _TMULT_CACHE[N]
    rows = []
    for w in range(1, wmax + 1):
        for sup in itertools.combinations(range(N), w):
            for sg in itertools.product((1, -1), repeat=w - 1):
                row = np.zeros(N, dtype=np.int8)
                row[sup[0]] = 1
                for p, c in zip(sup[1:], sg):
                    row[p] = c
                rows.append(row)
    bank = np.array(rows, dtype=np.int8)
    _TMULT_CACHE[N] = bank
    return bank


def sweep_links_from(src_vec, N, member_to_idx, self_idx):
    """spec D4 singular-source path: weight-<=3 ternary multipliers,
    exact dense sweep over Z."""
    bank = ternary_mult_bank(N)
    out = np.zeros(bank.shape, dtype=np.int16)
    for p, c in src_vec:
        rolled = np.roll(bank, p, axis=1).astype(np.int16)
        if p:
            rolled[:, :p] *= -1
        out += c * rolled
    ok = (np.abs(out) <= 1).all(axis=1) & (out != 0).any(axis=1)
    linked = set()
    for ridx in np.nonzero(ok)[0]:
        row = out[ridx]
        vec = normalize(tuple((int(p), int(row[p]))
                              for p in np.nonzero(row)[0]))
        j = member_to_idx.get(vec)
        if j is not None and j != self_idx:
            linked.add(j)
    return linked


def division_links_from(i, vecs, N, targets_big, tern_ok=None):
    """spec D2(b) round-7 path: exact division via aux prime, unique
    modular solution ternarity, exact Z re-verify."""
    if tern_ok is None:
        def tern_ok(X, p):
            return np.all((X == 0) | (X == 1) | (X == p - 1), axis=0)
    Mi = mult_matrix(vecs[i], N)
    inv = None
    for p in AUX_PRIMES:
        inv = inv_mod(Mi, p)
        if inv is not None:
            break
    if inv is None:
        return None
    X = inv @ (targets_big % p) % p
    tern = tern_ok(X, p)
    linked = set()
    ncols = 2 * N
    for col in np.nonzero(tern)[0]:
        j = int(col) // ncols
        if j == i or j in linked:
            continue
        m = np.where(X[:, col] == p - 1, -1, X[:, col]).astype(np.int64)
        if not (m == 0).all() and np.array_equal(
                Mi @ m, targets_big[:, col]):
            linked.add(j)
    return linked


def shadow_pass(reps_by_w, N, order="fwd", skip_above=360, mutate_gate=None):
    """canonical shadow dedup (spec D1-D5)."""
    ordered = [(w, r) for w in sorted(reps_by_w)
               for r in sorted(reps_by_w[w])]
    if order == "rev":
        ordered = ordered[::-1]
    n = len(ordered)
    if n < 2:
        return ({w: list(reps_by_w[w]) for w in reps_by_w}, 0, False, {})
    if n > skip_above:
        return ({w: list(reps_by_w[w]) for w in reps_by_w}, 0, True, {})
    vecs = [r for _, r in ordered]
    tags = [tag_of(r, N) for r in vecs]
    member_to_idx = {}
    for idx, v in enumerate(vecs):
        for m_ in orbit_members(v, N):
            member_to_idx[m_] = idx
    blocks = []
    for j in range(n):
        M = mult_matrix(vecs[j], N)
        cols = []
        for s in range(N):
            cols.append(M[:, s])
            cols.append(-M[:, s])
        blocks.append(np.array(cols).T)
    targets_big = np.hstack(blocks)
    links = set()
    methods = {"division": 0, "sweep": 0, "aux_exhausted": 0}
    for i in range(n):
        if tags[i]:
            got = sweep_links_from(vecs[i], N, member_to_idx, i)
            methods["sweep"] += 1
        else:
            got = division_links_from(i, vecs, N, targets_big,
                                      tern_ok=mutate_gate)
            if got is None:
                got = sweep_links_from(vecs[i], N, member_to_idx, i)
                methods["aux_exhausted"] += 1
            else:
                methods["division"] += 1
        for j in got:
            links.add((min(i, j), max(i, j)))
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i, j in links:
        parent[find(j)] = find(i)
    owners = {}
    for idx in range(n):
        r = find(idx)
        owners[r] = min(owners.get(r, idx), idx)
    keep = set(owners.values())
    out = {w: [] for w in reps_by_w}
    for idx in keep:
        w, rep = ordered[idx]
        out[w].append(rep)
    for w in out:
        out[w].sort()
    return out, len(links), False, methods


def lift_sources(N, q, L):
    out = []
    for k in range(2, N + 1):
        if N % k or N // k < 2:
            continue
        Ns = N // k
        adm = (Ns >= 16 * L) and (2 ** Ns >= q ** L)
        out.append((Ns, k, adm))
    return out


def lift_pass(q, N, L, reps_by_w, mutate=False):
    """canonical lift dedup (spec D6-D8). Mutation (M-D): the minimal
    support position of each source vector is displaced by +1 AFTER the
    k-scaling — not a ring operation, so no z^s shift can absorb it."""
    orbmap = {}
    for w in reps_by_w:
        for r in reps_by_w[w]:
            for m_ in orbit_members(r, N):
                orbmap[m_] = r
    owned = {}
    miss = 0
    stats = []
    for Ns, k, adm in lift_sources(N, q, L):
        if not adm:
            stats.append([Ns, k, "inadm"])
            continue
        powersS, _ = row_powers(q, Ns, L)
        hitsS, _ = enumerate_mitm(q, Ns, L, list(range(L + 1, L + 6)),
                                  powersS)
        fS, pS, repsS, wclS, flS = ledger_census(q, Ns, L, powersS, hitsS)
        n_src = sum(pS.values())
        n_owned = 0
        for w in repsS:
            for r in repsS[w]:
                pts = [(k * p, c) for p, c in r]
                if mutate:
                    p0, c0 = pts[0]
                    pts = [((p0 + 1) % N, c0)] + pts[1:]
                img = normalize(tuple(sorted(pts)))
                tgt = orbmap.get(img)
                if tgt is not None:
                    prev = owned.get(tgt)
                    owned[tgt] = Ns if prev is None else min(prev, Ns)
                    n_owned += 1
                else:
                    miss += 1
        stats.append([Ns, k, n_src, n_owned])
    return owned, miss, stats


def dedup_canonical(q, N, L, reps_by_w, do_alt=False):
    owned, miss, lstats = lift_pass(q, N, L, reps_by_w)
    surv = {w: [r for r in reps_by_w[w] if r not in owned]
            for w in reps_by_w}
    kept, nlinks, skipped, methods = shadow_pass(surv, N)
    rep = {"W_lift": frs(wcl_of(surv, N)),
           "W_canon": frs(wcl_of(kept, N)),
           "lift_owned": len(owned), "lift_miss": miss,
           "lift_stats": lstats, "links": nlinks,
           "skipped": skipped, "methods": methods}
    if do_alt:
        keptS, nlS, skS, _ = shadow_pass(reps_by_w, N)
        altsurv = {w: [r for r in keptS[w] if r not in owned]
                   for w in keptS}
        rep["W_shadow_only"] = frs(wcl_of(keptS, N))
        rep["W_alt_order"] = frs(wcl_of(altsurv, N))
        rep["order_material"] = (rep["W_alt_order"] != rep["W_canon"])
    return rep, kept


# ------------------------------------------------------- banked constants

BANKED_M2 = {
    (1, 7937): {2: 0, 3: 2, 4: 8, 5: 31, 6: 126},
    (1, 3137): {2: 0, 3: 0, 4: 2, 5: 33, 6: 294},
    (1, 5569): {2: 0, 3: 0, 4: 1, 5: 17, 6: 153},
    (1, 12289): {2: 0, 3: 0, 4: 0, 5: 9, 6: 71},
    (2, 193): {3: 0, 4: 0, 5: 4, 6: 24, 7: 176},
    (2, 257): {3: 0, 4: 0, 5: 3, 6: 15, 7: 92},
    (2, 449): {3: 0, 4: 0, 5: 0, 6: 1, 7: 33},
    (2, 577): {3: 0, 4: 0, 5: 1, 6: 3, 7: 19},
}
BANKED_WCL = {
    (1, 7937): (236, 1), (1, 3137): (368, 1), (1, 5569): (191, 1),
    (1, 12289): (89, 1), (2, 193): (120, 1), (2, 257): (67, 1),
    (2, 449): (35, 2), (2, 577): (29, 2),
}
BANKED_M1_FULL_W6 = {193: 4712, 7937: 224}

R1_A21 = {"q": 2107073, "prim6": 4, "W": "4/1", "links": 5, "Wd": "1/1"}
R1_B14 = {"q": 21569, "rep": "0:+1,1:-1,12:-1,16:-1,19:+1,25:+1,27:-1",
          "W": "1/2"}
R1_C21 = {"q": 2100353, "prim": {5: 2, 6: 18}, "W": "44/1",
          "links": 10, "Wd": "34/1"}

F96 = ((0, 1), (16, -1), (32, 1))
F192 = ((0, 1), (32, -1), (64, 1))


# ------------------------------------------------------------- cell report

def cell_report(q, N, L, band, engine="mitm", dedup=True, do_alt=False,
                compact=False):
    weights = list(range(L + 1, L + 6))
    powers, _ = row_powers(q, N, L)
    if engine == "mitm":
        hits, n_cand = enumerate_mitm(q, N, L, weights, powers)
    else:
        hits = enumerate_direct(q, N, L, weights, powers)
        n_cand = -1
    full, prim, reps, wcl, flags = ledger_census(q, N, L, powers, hits)
    tot = sum(prim.values())
    rep = {"q": q, "band": band,
           "prim": {str(w): prim[w] for w in weights if prim[w]},
           "W": frs(wcl), "nc": n_cand, "tot": tot}
    if not compact:
        rep.update({"N": N, "L": L, "eng": engine,
                    "full": {str(w): full[w] for w in weights}})
    fl_detail = []
    for f in flags:
        kind, _, repstr = f.partition("|")
        fl_detail.append({"flag": kind, "rep": repstr,
                          "tag": list(tag_of(parse_vec(repstr), N))})
    # JSON-size discipline (40k stdout return cap): degenerate flags on
    # Phi_{n'}-tagged orbits are the PREDICTED whitelisted class
    # (wz2_falsifiers 0.4) — keep them as a count; full detail only for
    # anomalies (closure misses or degenerate WITHOUT the 2-power-component
    # tag).
    anom = [f for f in fl_detail
            if f["flag"].startswith("ORBIT_CLOSURE") or not f["tag"]]
    if anom:
        rep["flags"] = anom
    ndeg = len(fl_detail) - len(anom)
    if ndeg:
        rep["deg_tagged"] = ndeg
    orbs = []
    for w in weights:
        for r in reps[w]:
            t = tag_of(r, N)
            orbs.append({"w": w, "rep": vec_str(r), "tag": list(t),
                         "u": uncovered_count(t, N, L)})
    rep["pop"] = {"f": sum(1 for o in orbs if o["u"] == 0),
                  "s": sum(1 for o in orbs if 0 < o["u"] < L),
                  "g": sum(1 for o in orbs if o["u"] == L)}
    if 1 <= tot <= 64:
        rep["orbs"] = orbs
    if dedup and tot >= 1:
        drep, kept = dedup_canonical(q, N, L, reps, do_alt=do_alt)
        if compact:
            drep.pop("lift_stats", None)
            drep.pop("methods", None)
        rep["dedup"] = drep
    return rep, reps, hits, powers


def lam_orb(q, N, L):
    return sum(math.comb(N, w) * 2 ** (w - 1)
               for w in range(L + 1, L + 6)) / (2 * N * q ** L)


def agg_band(cells, N, L):
    n = len(cells)
    nonempty = sum(1 for c, _, _, _ in cells if c["tot"] > 0)
    gen_nonempty = sum(1 for c, _, _, _ in cells if c["pop"]["g"] > 0)
    semi_total = sum(c["pop"]["s"] for c, _, _, _ in cells)
    ppred = sum(1 - math.exp(-lam_orb(c["q"], N, L))
                for c, _, _, _ in cells) / n
    wsum = sum((parse_fr(c["W"]) for c, _, _, _ in cells), Fraction(0))
    epred = sum(sum(math.comb(N, w) for w in range(L + 1, L + 6))
                / (2 * c["q"] ** L) for c, _, _, _ in cells) / n
    return {"n": n, "nonempty": nonempty, "gen_nonempty": gen_nonempty,
            "semi_orbits": semi_total,
            "Phat": round(nonempty / n, 6),
            "Phat_gen": round(gen_nonempty / n, 6),
            "Ppred": round(ppred, 6), "Wbar": frs(wsum / n),
            "Epred": epred,
            "q_range": [cells[0][0]["q"], cells[-1][0]["q"]]}


def band_cells(nprime, N, L, b, K, compact=True):
    qs = first_primes_1mod(nprime, 2 ** b, K)
    cells = []
    band_cand = 0
    for q in qs:
        rep, reps, hits, powers = cell_report(q, N, L, "b%d" % b,
                                              compact=compact)
        band_cand += max(rep["nc"], 0)
        cells.append((rep, reps, hits, powers))
    return qs, cells, band_cand


# ------------------------------------------------------------------ shards

def shard_replay():
    out = {"shard": "replay", "checks": {}, "cells": []}
    ok = True

    rep, reps, hits, powers = cell_report(7937, 32, 1, "PC", "direct",
                                          do_alt=True)
    b = BANKED_M2[(1, 7937)]
    t1a = all(rep["prim"].get(str(w), 0) == b[w] for w in b) and \
        rep["W"] == "%d/%d" % BANKED_WCL[(1, 7937)]
    hm, _ = enumerate_mitm(7937, 32, 1, list(range(2, 7)), powers)
    t1a &= all(hm[w] == hits[w] for w in hits)
    ma = (rep["full"]["6"] == BANKED_M1_FULL_W6[7937]
          and rep["full"]["6"] != rep["prim"]["6"])
    out["checks"]["T1a_7937"] = t1a
    out["checks"]["MA_prim_off_trips"] = ma
    ok &= t1a and ma
    out["cells"].append(rep)
    print("T1a q=7937 banked=%s M-A=%s W_canon=%s t=%.0fs"
          % (t1a, ma, rep["dedup"]["W_canon"], time.time() - T0))

    # T8: sweep links subset of division links on the 7937 window
    ordered = [(w, r) for w in sorted(reps) for r in sorted(reps[w])]
    vecs = [r for _, r in ordered]
    m2i = {}
    for idx, v in enumerate(vecs):
        for m_ in orbit_members(v, 32):
            m2i[m_] = idx
    blocks = []
    for j in range(len(vecs)):
        M = mult_matrix(vecs[j], 32)
        cols = []
        for s in range(32):
            cols.append(M[:, s])
            cols.append(-M[:, s])
        blocks.append(np.array(cols).T)
    tbig = np.hstack(blocks)
    t8 = True
    for i in range(len(vecs)):
        sw = sweep_links_from(vecs[i], 32, m2i, i)
        dv = division_links_from(i, vecs, 32, tbig)
        if dv is None or not sw.issubset(dv):
            t8 = False
            break
    out["checks"]["T8_sweep_subset_division"] = t8
    ok &= t8
    print("T8=%s t=%.0fs" % (t8, time.time() - T0))

    rep2, reps2, hits2, powers2 = cell_report(193, 32, 2, "PC", "direct")
    b = BANKED_M2[(2, 193)]
    t1b = all(rep2["prim"].get(str(w), 0) == b[w] for w in b) and \
        rep2["W"] == "%d/%d" % BANKED_WCL[(2, 193)]
    hm2, _ = enumerate_mitm(193, 32, 2, list(range(3, 8)), powers2)
    t1b &= all(hm2[w] == hits2[w] for w in hits2)
    out["checks"]["T1b_193L2"] = t1b
    ok &= t1b
    out["cells"].append(rep2)
    print("T1b q=193 L2 banked=%s t=%.0fs" % (t1b, time.time() - T0))

    repA, repsA, hitsA, powersA = cell_report(R1_A21["q"], 32, 1, "r1A",
                                              do_alt=True)
    t2a = (repA["W"] == R1_A21["W"]
           and repA["prim"].get("6", 0) == R1_A21["prim6"])
    d1, nl1, sk1 = r1_shadow_dedup(repsA, 32)
    t2a &= (nl1 == R1_A21["links"]
            and frs(wcl_of(d1, 32)) == R1_A21["Wd"])
    out["checks"]["T2a_A21_r1conv"] = t2a
    ok &= t2a
    kf, _, _, _ = shadow_pass(repsA, 32, order="fwd")
    kr, _, _, _ = shadow_pass(repsA, 32, order="rev")
    setf = {vec_str(r) for w in kf for r in kf[w]}
    setr = {vec_str(r) for w in kr for r in kr[w]}
    mc = setf != setr
    out["checks"]["MC_order_reversal_trips"] = mc
    ok &= mc
    import random
    t5 = True
    for seed in (1, 2, 3):
        rng = random.Random(seed)
        shuf = {w: list(repsA[w]) for w in repsA}
        for w in shuf:
            rng.shuffle(shuf[w])
        ks, _, _, _ = shadow_pass(shuf, 32)
        t5 &= {vec_str(r) for w in ks for r in ks[w]} == setf
    out["checks"]["T5_order_invariance"] = t5
    ok &= t5
    k2p, nl2, _, _ = shadow_pass(kf, 32)
    t6 = ({vec_str(r) for w in k2p for r in k2p[w]} == setf and nl2 == 0)
    out["checks"]["T6_idempotent"] = t6
    ok &= t6
    out["cells"].append(repA)
    print("T2a=%s MC=%s T5=%s T6=%s t=%.0fs"
          % (t2a, mc, t5, t6, time.time() - T0))

    repB, repsB, _, _ = cell_report(R1_B14["q"], 32, 2, "r1B")
    t2b = (repB["W"] == R1_B14["W"] and repB["tot"] == 1
           and repB["orbs"][0]["rep"] == R1_B14["rep"])
    out["checks"]["T2b_B14"] = t2b
    ok &= t2b
    out["cells"].append(repB)

    repC, repsC, hitsC, powersC = cell_report(R1_C21["q"], 64, 1, "r1C",
                                              do_alt=True)
    t2c = (repC["W"] == R1_C21["W"]
           and all(repC["prim"].get(str(w), 0) == c
                   for w, c in R1_C21["prim"].items()))
    dC, nlC, skC = r1_shadow_dedup(repsC, 64)
    t2c &= (nlC == R1_C21["links"]
            and frs(wcl_of(dC, 64)) == R1_C21["Wd"])
    out["checks"]["T2c_C21_r1conv"] = t2c
    ok &= t2c
    out["cells"].append(repC)
    print("T2c=%s W_canon=%s alt=%s t=%.0fs"
          % (t2c, repC["dedup"]["W_canon"],
             repC["dedup"].get("W_alt_order"), time.time() - T0))

    # T3 synthetic shadow (base chosen with no adjacent support positions
    # so (1+z)*base is genuinely ternary) + M-B gate mutation
    base = None
    for r in repsA.get(6, []):
        ps = [p for p, _ in r]
        if all(ps[i + 1] - ps[i] > 1 for i in range(len(ps) - 1)) \
                and ps[-1] < 31:
            base = r
            break
    assert base is not None, "NO_T3_BASE"
    prod = {}
    for p, c in base:
        prod[p] = prod.get(p, 0) + c
        p2, c2 = (p + 1, c) if p + 1 < 32 else (0, -c)
        prod[p2] = prod.get(p2, 0) + c2
    synth = normalize(tuple(sorted((p, c) for p, c in prod.items() if c)))
    assert all(abs(c) == 1 for _, c in synth), "T3_SYNTH_NOT_TERNARY"
    pair = {len(base): [base], len(synth): [synth]}
    kp, nlp, _, _ = shadow_pass(pair, 32)
    t3 = (nlp >= 1 and sum(len(v) for v in kp.values()) == 1)
    out["checks"]["T3_synthetic_links"] = t3
    ok &= t3

    def empty_gate(X, p):
        return np.zeros(X.shape[1], dtype=bool)
    kpm, nlm, _, _ = shadow_pass(pair, 32, mutate_gate=empty_gate)
    mb = (nlm == 0 and sum(len(v) for v in kpm.values()) == 2)
    out["checks"]["MB_gate_mutation_trips"] = mb
    ok &= mb
    print("T3=%s MB=%s t=%.0fs" % (t3, mb, time.time() - T0))

    out["ok"] = ok
    return out


def shard_c1audit():
    rows = [(1, 3137), (1, 5569), (1, 7937), (1, 12289),
            (2, 193), (2, 257), (2, 449), (2, 577)]
    src = json.load(open("m1_dli_m1_results.json"))
    srows = {((r["t"] + 1) // 2, r["q"]): r for r in src["rows"]}
    out = {"shard": "c1audit", "rows": [], "violations": []}
    ok = True
    for L, q in rows:
        rep, reps, hits, powers = cell_report(q, 32, L, "audit", "mitm",
                                              do_alt=True)
        b = BANKED_M2[(L, q)]
        match = all(rep["prim"].get(str(w), 0) == b[w] for w in b) and \
            rep["W"] == "%d/%d" % BANKED_WCL[(L, q)]
        ok &= match
        srow = srows[(L, q)]
        assert srow["q"] == q and not srow["suborbit_flags"]
        weighted = Fraction(1, 1)
        for wt, cnt in srow["V_orbits"].items():
            weighted += Fraction(int(cnt) * 2 * 32, 2 ** int(wt))
        E = Fraction(q ** L, 2 ** 32) * weighted
        r_ = Fraction(q ** L, 2 ** 32)
        Wd = parse_fr(rep["dedup"]["W_canon"])
        Wraw = Fraction(*BANKED_WCL[(L, q)])
        kraw = (E - 1) / (r_ * (1 + Wraw))
        kded = (E - 1) / (r_ * (1 + Wd))
        viol = (E - 1) > 4 * r_ * (1 + Wd)
        out["rows"].append({"L": L, "q": q, "banked_match": match,
                            "W_raw": frs(Wraw), "dedup": rep["dedup"],
                            "K_raw": float(kraw), "K_dedup": float(kded),
                            "violation_exact": viol})
        if viol:
            out["violations"].append([L, q])
        print("audit L=%d q=%d match=%s W %s->%s K' %.4f->%.4f viol=%s "
              "t=%.0fs" % (L, q, match, frs(Wraw),
                           rep["dedup"]["W_canon"], kraw, kded, viol,
                           time.time() - T0))
    out["ok"] = ok
    return out


def shard_band_b(bands, name):
    out = {"shard": name, "bands": {}, "cells_nonempty": []}
    for b, K in bands:
        qs, cells, band_cand = band_cells(64, 32, 2, b, K)
        ag = agg_band(cells, 32, 2)
        ag["band_cand"] = band_cand
        out["bands"]["b%d" % b] = ag
        for c, reps, hits, powers in cells:
            if c["tot"] > 0:
                h1, _ = enumerate_mitm(c["q"], 32, 1, list(range(3, 8)),
                                       [powers[0]])
                c["l1_hits"] = {str(w): len(h1[w]) for w in h1}
                c["l2_hits"] = {str(w): len(hits[w]) for w in hits
                                if len(hits[w])}
                out["cells_nonempty"].append(c)
        assert band_cand > 0, "EMPTY_BAND_STREAM b%d" % b
        print("%s b=%d K=%d nonempty=%d cand=%d t=%.0fs"
              % (name, b, K, ag["nonempty"], band_cand, time.time() - T0))
    return out


def explain_missing_plant(plant, powers, q, N):
    lv = eval_levels(plant, powers[:1], q)
    assert all(v == 0 for v in lv), ("PLANT_NOT_VANISHING", q)
    return {"vanishes": True,
            "primitive": is_primitive(plant, powers, q)}


def shard_o_l1(nprime, N, bands, shardname, fvec, fname):
    out = {"shard": shardname, "bands": {}, "cells": [], "checks": {}}
    ok = True
    prepF = min(orbit_members(fvec, N))
    for b, K in bands:
        qs, cells, band_cand = band_cells(nprime, N, 1, b, K)
        ag = agg_band(cells, N, 1)
        ag["band_cand"] = band_cand
        forced_sets = []
        for c, reps, hits, powers in cells:
            found = any(prepF == r for r in reps.get(3, []))
            c["plant_F"] = found
            if not found:
                c["plant_missing_explained"] = explain_missing_plant(
                    prepF, powers, c["q"], N)
            forced_sets.append(frozenset(
                o["rep"] for o in c.get("orbs", [])
                if fname in o["tag"]))
            if not (c["pop"]["g"] or c["pop"]["s"] or "flags" in c
                    or not found):
                c.pop("orbs", None)  # forced-only cell, keep JSON lean
            out["cells"].append(c)
        ag["forced_set_identical"] = len(set(forced_sets)) == 1
        out["bands"]["b%d" % b] = ag
        assert band_cand > 0
        print("%s b=%d nonempty=%d gen=%d forced_id=%s t=%.0fs"
              % (shardname, b, ag["nonempty"], ag["gen_nonempty"],
                 ag["forced_set_identical"], time.time() - T0))
    plant_ok = all(
        c["plant_F"] or (c.get("plant_missing_explained", {})
                         .get("vanishes")
                         and not c["plant_missing_explained"]["primitive"])
        for c in out["cells"])
    out["checks"]["plant_ok"] = plant_ok
    out["checks"]["plant_missing_n"] = sum(
        1 for c in out["cells"] if not c["plant_F"])
    ok &= plant_ok
    tot_miss = sum(c.get("dedup", {}).get("lift_miss", 0)
                   for c in out["cells"])
    out["checks"]["lift_miss_total"] = tot_miss
    ok &= tot_miss == 0
    firstband = "b%d" % bands[0][0]
    out["checks"]["guard_gen_nonempty"] = \
        out["bands"][firstband]["gen_nonempty"] > 0
    ok &= out["checks"]["guard_gen_nonempty"]
    return out, ok


def shard_o96_l1():
    out, ok = shard_o_l1(96, 48, ((21, 24), (23, 24), (25, 24)),
                         "o96_l1", F96, "Phi96")
    # T7 singular-source sweep exercise
    prod = {}
    for p, c in F96:
        prod[p] = prod.get(p, 0) + c
        p2, c2 = (p + 1, c) if p + 1 < 48 else (0, -c)
        prod[p2] = prod.get(p2, 0) + c2
    synth = normalize(tuple(sorted((p, c) for p, c in prod.items() if c)))
    m2i = {}
    for idx, v in enumerate([F96, synth]):
        for m_ in orbit_members(v, 48):
            m2i[m_] = idx
    t7 = 1 in sweep_links_from(F96, 48, m2i, 0)
    out["checks"]["T7_singular_sweep"] = t7
    ok &= t7
    # M-D mutated lift map must miss at the first b21 prime
    q0 = first_primes_1mod(96, 2 ** 21, 1)[0]
    powers0, _ = row_powers(q0, 48, 1)
    hits0, _ = enumerate_mitm(q0, 48, 1, list(range(2, 7)), powers0)
    f0, p0, reps0, w0, fl0 = ledger_census(q0, 48, 1, powers0, hits0)
    _, miss_true, _ = lift_pass(q0, 48, 1, reps0, mutate=False)
    _, miss_mut, _ = lift_pass(q0, 48, 1, reps0, mutate=True)
    md = (miss_true == 0 and miss_mut >= 1)
    out["checks"]["MD_lift_mutation_trips"] = md
    out["checks"]["MD_misses"] = [miss_true, miss_mut]
    ok &= md
    # M-E wrong-factor tag must break the plant-tag control
    wrongtag = poly_divisible(F96, 48, 16, {0: 1})
    righttag = poly_divisible(F96, 48, 32, {0: 1, 16: -1})
    me = (not wrongtag) and righttag
    out["checks"]["ME_tag_mutation_trips"] = me
    ok &= me
    out["ok"] = ok
    return out


def shard_o192_l1():
    out, ok = shard_o_l1(192, 96, ((25, 12), (27, 12), (29, 12)),
                         "o192_l1", F192, "Phi192")
    out["ok"] = ok
    return out


def shard_o_l2(nprime, N, b, K, shardname):
    out = {"shard": shardname, "bands": {}, "cells_nonempty": [],
           "checks": {}}
    fvec = F96 if N == 48 else F192
    prepF = min(orbit_members(fvec, N))
    qs, cells, band_cand = band_cells(nprime, N, 2, b, K)
    ag = agg_band(cells, N, 2)
    ag["band_cand"] = band_cand
    neg_ok = True
    norm_ok = True
    for c, reps, hits, powers in cells:
        if any(prepF == r for w in reps for r in reps[w]):
            neg_ok = False
        if c["tot"] > 0:
            nchecks = []
            for o in c.get("orbs", []):
                if o["tag"] and o["u"] > 0:
                    nk = resultant_check(parse_vec(o["rep"]), N, 2,
                                         c["q"])
                    nchecks.append(nk)
                    norm_ok &= nk["ok"]
            if nchecks:
                c["norm_checks"] = nchecks
            out["cells_nonempty"].append(c)
    ag["neg_plant_ok"] = neg_ok
    out["bands"]["b%d" % b] = ag
    out["checks"]["neg_plant_ok"] = neg_ok
    out["checks"]["norm_ok"] = norm_ok
    assert band_cand > 0, "EMPTY_BAND_STREAM"
    out["ok"] = neg_ok and norm_ok
    print("%s b=%d nonempty=%d gen=%d semi=%d neg=%s norm=%s t=%.0fs"
          % (shardname, b, ag["nonempty"], ag["gen_nonempty"],
             ag["semi_orbits"], neg_ok, norm_ok, time.time() - T0))
    return out


def shard_o96_l3():
    out = {"shard": "o96_l3", "bands": {}, "cells_nonempty": [],
           "checks": {}}
    prepF = min(orbit_members(F96, 48))
    qs, cells, band_cand = band_cells(96, 48, 3, 13, 12)
    ag = agg_band(cells, 48, 3)
    ag["band_cand"] = band_cand
    neg_ok = True
    norm_ok = True
    for c, reps, hits, powers in cells:
        if any(prepF == r for w in reps for r in reps[w]):
            neg_ok = False
        if c["tot"] > 0:
            nchecks = []
            for o in c.get("orbs", []):
                if o["tag"] and o["u"] > 0:
                    nk = resultant_check(parse_vec(o["rep"]), 48, 3,
                                         c["q"])
                    nchecks.append(nk)
                    norm_ok &= nk["ok"]
            if nchecks:
                c["norm_checks"] = nchecks
            out["cells_nonempty"].append(c)
    out["bands"]["b13"] = ag
    out["checks"]["neg_plant_ok"] = neg_ok
    out["checks"]["norm_ok"] = norm_ok
    out["ok"] = neg_ok and norm_ok
    print("o96_l3 nonempty=%d cand=%d t=%.0fs"
          % (ag["nonempty"], band_cand, time.time() - T0))
    return out


def shard_xcheckl3():
    out = {"shard": "xcheckl3"}
    tried = []
    for q in first_primes_1mod(64, 193, 8):
        powers, _ = row_powers(q, 32, 3)
        hits_m, n_cand = enumerate_mitm(q, 32, 3, list(range(4, 9)),
                                        powers)
        tot = sum(len(v) for v in hits_m.values())
        tried.append([q, tot])
        if tot > 0:
            hits_d = enumerate_direct(q, 32, 3, list(range(4, 9)), powers)
            eq = all(hits_d[w] == hits_m[w] for w in hits_m)
            out.update({"q": q, "equal": eq, "nonempty": True,
                        "n_hits": {str(w): len(hits_m[w])
                                   for w in hits_m},
                        "tried": tried, "ok": eq})
            print("xcheckl3 q=%d equal=%s hits=%s t=%.0fs"
                  % (q, eq, out["n_hits"], time.time() - T0))
            return out
    out.update({"nonempty": False, "tried": tried, "ok": False})
    return out


def shard_xcheck96():
    out = {"shard": "xcheck96"}
    q = first_primes_1mod(192, 2 ** 25, 1)[0]
    powers, _ = row_powers(q, 96, 1)
    weights = [2, 3, 4]
    hits_d = enumerate_direct(q, 96, 1, weights, powers, chunk=200_000)
    hits_m, _ = enumerate_mitm(q, 96, 1, weights, powers)
    eq = all(hits_d[w] == hits_m[w] for w in weights)
    fin = F192 in hits_d[3]
    out.update({"q": q, "equal": eq, "F192_found": fin,
                "n_hits": {str(w): len(hits_d[w]) for w in weights}})
    # k=3 lift identity on data: (193, N=32) w=3 vanishers -> D_3 images
    # must vanish at (193, N=96) level 1 (exact evaluation)
    q2 = 193
    powers32, _ = row_powers(q2, 32, 1)
    h32, _ = enumerate_mitm(q2, 32, 1, [3], powers32)
    powers96, _ = row_powers(q2, 96, 1)
    k3ok = len(h32[3]) > 0
    for v in h32[3]:
        img = normalize(tuple(sorted((3 * p, c) for p, c in v)))
        if any(x != 0 for x in eval_levels(img, powers96, q2)):
            k3ok = False
    out["k3_identity_ok"] = k3ok
    out["k3_n_sources"] = len(h32[3])
    out["ok"] = eq and fin and k3ok
    print("xcheck96 q=%d equal=%s F192=%s k3=%s(%d) t=%.0fs"
          % (q, eq, fin, k3ok, len(h32[3]), time.time() - T0))
    return out


def main():
    shard = sys.argv[1]
    if shard == "replay":
        res = shard_replay()
    elif shard == "c1audit":
        res = shard_c1audit()
    elif shard == "band_b15":
        res = shard_band_b([(14, 96), (15, 384)], "band_b15")
    elif shard == "band_b16":
        res = shard_band_b([(16, 384)], "band_b16")
    elif shard == "o96_l1":
        res = shard_o96_l1()
    elif shard == "o96_l2a":
        res = shard_o_l2(96, 48, 13, 24, "o96_l2a")
    elif shard == "o96_l2b":
        res = shard_o_l2(96, 48, 14, 24, "o96_l2b")
    elif shard == "o96_l2c":
        res = shard_o_l2(96, 48, 15, 24, "o96_l2c")
    elif shard == "o96_l3":
        res = shard_o96_l3()
    elif shard == "o192_l1":
        res = shard_o192_l1()
    elif shard == "o192_l2a":
        res = shard_o_l2(192, 96, 16, 10, "o192_l2a")
    elif shard == "o192_l2b":
        res = shard_o_l2(192, 96, 17, 10, "o192_l2b")
    elif shard == "xcheckl3":
        res = shard_xcheckl3()
    elif shard == "xcheck96":
        res = shard_xcheck96()
    else:
        raise SystemExit("unknown shard " + shard)
    res["wall_s"] = round(time.time() - T0, 1)
    # aggregates-first line survives even if the full JSON hits the 40k
    # stdout return cap
    agg = {k: res.get(k) for k in ("shard", "bands", "checks", "ok",
                                   "violations", "wall_s")
           if k in res}
    print("WZ2_AGG " + json.dumps(agg, separators=(",", ":"),
                                  default=str))
    blob = json.dumps(res, separators=(",", ":"), default=str)
    print("WZ2_SIZE %d" % len(blob))
    print("WZ2_JSON " + blob)


if __name__ == "__main__":
    main()

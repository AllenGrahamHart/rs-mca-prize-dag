#!/usr/bin/env python3
r"""L-B: ESCAPE-1 OVER-AGREEMENT -- machine verification.

Pilot: Opus 5, 2026-08-03.  Anchor: L-B, the second fallback lemma of the
ratified band-heart consolidation
(notes/band_heart_consolidation_20260803/CONSOLIDATION.md, section 5.3).

CLAIM UNDER TEST.  In a full-gate admissible live-slope system realised by
a received pair (u,v), a (3,k+1)-core ray of escape exactly 1 is never the
SELECTED exact-A ray of its slope: agr(z_a) > A, hence V_1 = 0.

Falsifiers LB-F1..LB-F10 and predictions P1..P6 were fixed in PREREG.md
BEFORE this file existed.  Every falsifier is evaluated and reported.

REUSE (read-only imports, never copies): s4lib.py (support4_relation),
tslib.py (xr_occupancy_v2), occlib.py (xr_band_occupancy) and the sibling
pilots' verify.py (escape1_realizability: fibre_system / build_X1p /
build_E1; k_escape_unification: phi_kernel).

Run:  tools/ramguard local -- python3 \
      notes/pilots_20260803/lb_escape1_overagreement/verify.py
"""
from __future__ import annotations

import importlib.util
import itertools
import json
import os
import random
import sys

sys.dont_write_bytecode = True

_P2 = "/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802"
for _d in ("support4_relation",):
    _p = os.path.join(_P2, _d)
    if _p not in sys.path:
        sys.path.append(_p)

import s4lib as S                                              # noqa: E402
import tslib as T                                              # noqa: E402
import occlib                                                  # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_P3 = "/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260803"
E1V = _load("e1_verify", os.path.join(_P3, "escape1_realizability",
                                      "verify.py"))
UNI = _load("uni_verify", os.path.join(_P3, "k_escape_unification",
                                       "verify.py"))

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKS = [0]
FAILS = []
HITS = []
LOG = {"checks": [], "fixtures": [], "theoremF": [], "search": []}


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    LOG["checks"].append(dict(label=label, ok=bool(ok), detail=str(detail)))
    if not ok:
        FAILS.append(label)
        print("  FAIL", label, detail)
    return bool(ok)


def falsifier(tag, fired, detail=""):
    LOG["checks"].append(dict(label="FALSIFIER " + tag, ok=not fired,
                              detail=str(detail)))
    CHECKS[0] += 1
    if fired:
        HITS.append(tag)
        print("  *** FALSIFIER", tag, "FIRED:", detail)
    return fired


# ------------------------------------------------------- exact agreement
def parity(row):
    """Parity checks of RS_k on the full point set (n-k rows)."""
    return T.dual_basis(tuple(range(row.n)), row)


def syndrome(H, w, q):
    return [sum(h[i] * w[i] for i in range(len(w))) % q for h in H]


def _solve_supported(H, D, s, q):
    """Return an error vector supported on D with H e = s, or None."""
    nr = len(H)
    cols = len(D)
    M = [[H[t][i] for i in D] + [s[t]] for t in range(nr)]
    piv = []
    r = 0
    for c in range(cols):
        p = None
        for i in range(r, nr):
            if M[i][c]:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        iv = pow(M[r][c], q - 2, q)
        M[r] = [x * iv % q for x in M[r]]
        for i in range(nr):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(a - f * b) % q for a, b in zip(M[i], M[r])]
        piv.append(c)
        r += 1
    for i in range(nr):
        if M[i][cols] and not any(M[i][c] for c in range(cols)):
            return None
    e = [0] * cols
    for i, c in enumerate(piv):
        e[c] = M[i][cols]
    return e


def max_agreement(row, H, w, rmax):
    """EXACT max agreement of w with RS_k, provided it is >= n - rmax.

    Enumerates deletion sets of size 0,1,..,rmax and solves H e = syn(w)
    supported there; the first level that succeeds gives the exact
    minimum weight (hence the exact max agreement).  Returns
    (agreement, agreement_set) or (None, None) if agreement < n - rmax.
    """
    n, q = row.n, row.q
    s = syndrome(H, w, q)
    if not any(s):
        return n, frozenset(range(n))
    for r in range(1, rmax + 1):
        for D in itertools.combinations(range(n), r):
            e = _solve_supported(H, list(D), s, q)
            if e is None:
                continue
            supp = {D[j] for j in range(r) if e[j]}
            return n - len(supp), frozenset(i for i in range(n)
                                            if i not in supp)
    return None, None


def brute_max_agreement(row, w):
    """O(C(n,k)) reference oracle (soundness cross-check only)."""
    n, k, q = row.n, row.k, row.q
    best, bset = 0, None
    for W in itertools.combinations(range(n), k):
        f = row.interp(W, [w[i] for i in W])
        ag = frozenset(i for i in range(n) if row.ev(f, row.xs[i]) == w[i])
        if len(ag) > best:
            best, bset = len(ag), ag
    return best, bset


def ray_word(row, u, v, z):
    q = row.q
    return [(u[i] + z * v[i]) % q for i in range(row.n)]


# --------------------------------------------------------- ray machinery
def gates_of(row, supports):
    return S.combinatorial_gates(row, supports)


def core_of(row, supports):
    live, Ts, it, _ = UNI.phi_kernel(row, supports)
    esc = [len(Sa) - (len(Ts[a]) if a in live else 0)
           for a, Sa in enumerate(supports)]
    return live, Ts, esc


def ann_basis(row, supports, slopes):
    """Basis of {(u,v) in F^2n : (u + z_a v)|_{S_a} in RS_k|_{S_a} for all a}."""
    _, cols = S.ray_columns(row, supports, slopes)
    if not cols:
        return [[1 if i == j else 0 for i in range(2 * row.n)]
                for j in range(2 * row.n)]
    return T.nullspace_mod(cols, 2 * row.n, row.q)


def ann_dims(row, supports, slopes):
    """(dim of the full solution space, rank, m, nontrivial dim on U)."""
    ns = ann_basis(row, supports, slopes)
    rank = S.family_rank(row, supports, slopes)
    U = set().union(*[set(x) for x in supports])
    m = len(U) - row.k
    # free coordinates at points outside U contribute 2 each
    free = 2 * (row.n - len(U))
    return len(ns), rank, m, len(ns) - 2 * row.k - free


def interp_on(row, w, pts):
    base = tuple(sorted(pts)[:row.k])
    return row.interp(base, [w[i] for i in base])


def psi_forced(row, supports, slopes, a, drop):
    """Forced over-agreement points of ray a when its condition is imposed
    only on T_a = S_a \\ drop.

    Returns (dim of R = Ann(Sigma~), forced points y outside S_a with
    Psi_y = 0 identically on R, dim of Ann(Sigma)).
    """
    n, q, k = row.n, row.q, row.k
    sup2 = list(supports)
    Ta = tuple(sorted(set(supports[a]) - set(drop)))
    sup2[a] = Ta
    ns2 = ann_basis(row, sup2, slopes)
    ns1 = ann_basis(row, supports, slopes)
    outside = [y for y in range(n) if y not in set(supports[a])]
    forced = []
    for y in outside:
        bad = False
        for b in ns2:
            w = ray_word(row, b[:n], b[n:], slopes[a])
            f = interp_on(row, w, Ta)
            if (row.ev(f, row.xs[y]) - w[y]) % q:
                bad = True
                break
        if not bad:
            forced.append(y)
    return len(ns2), forced, len(ns1)


def proj_rank(row, ns, drop):
    """Rank of the realiser space after forgetting the coordinates (u,v) at
    the points of `drop` -- i.e. the dimension of what the realiser space
    determines away from those points."""
    n, q = row.n, row.q
    keep = [i for i in range(n) if i not in set(drop)]
    rows = [[b[i] for i in keep] + [b[n + i] for i in keep] for b in ns]
    return T.rank_mod(rows, q) if rows else 0


def draw_realisers(row, ns, count, seed=0, need_v_nonzero=True):
    """Nondegenerate draws from the realiser space."""
    rnd = random.Random(seed)
    n, q = row.n, row.q
    out = []
    if not ns:
        return out
    for _ in range(60 * count):
        if len(out) >= count:
            break
        w = [0] * (2 * n)
        for b in ns:
            c = rnd.randrange(q)
            if c:
                for i in range(2 * n):
                    w[i] = (w[i] + c * b[i]) % q
        u, v = w[:n], w[n:]
        if need_v_nonzero and any(t == 0 for t in v):
            continue
        if T.is_codeword(row, u) and T.is_codeword(row, v):
            continue
        if T.is_codeword(row, v):
            continue
        out.append((u, v))
    return out


def ray_report(row, H, u, v, supports, slopes, rays=None):
    """Exact max agreement of the selected ray slopes.

    The realiser condition guarantees agreement >= A on S_a (checked via
    own_missing), so it suffices to decide agreement >= A+1, i.e. distance
    <= n-A-1: cost C(n, n-A-1).  max_agr = A means EXACTLY A."""
    n, q = row.n, row.q
    A = row.k + row.h
    rmax = n - A - 1
    out = []
    for a, Sa in enumerate(supports):
        if rays is not None and a not in rays:
            continue
        w = ray_word(row, u, v, slopes[a])
        f = interp_on(row, w, Sa)
        own = frozenset(i for i in range(n) if row.ev(f, row.xs[i]) == w[i])
        ag, agset = max_agreement(row, H, w, rmax)
        if ag is None:
            ag, agset = A, frozenset(Sa)
        out.append(dict(a=a, own=len(own), own_extra=sorted(set(own) - set(Sa)),
                        own_missing=sorted(set(Sa) - own), max_agr=ag,
                        exact_A=(ag == A), over=(ag > A), agset=agset))
    return out


# =====================================================================
# PART 1 -- oracle soundness (LB-F9) and LEMMA R replay (LB-F8)
# =====================================================================
def part1_oracles():
    print("\nPART 1 -- exact-agreement oracle soundness + LEMMA R replay")
    rnd = random.Random(11)
    q, n, k, h = 13, 11, 4, 3
    row = T.Row2(n, k, h, q)
    H = parity(row)
    agree = 0
    for trial in range(12):
        w = [rnd.randrange(q) for _ in range(n)]
        bf, _ = brute_max_agreement(row, w)
        mine, _ = max_agreement(row, H, w, n - k)
        if mine is None:
            mine = 0
        if bf == mine:
            agree += 1
        else:
            falsifier("LB-F9", True, f"brute {bf} vs syndrome {mine}")
    chk("agreement oracle == brute force on 12 random words (n=11,k=4)",
        agree == 12, agree)
    # planted-codeword check
    for trial in range(6):
        f = tuple(rnd.randrange(q) for _ in range(k))
        w = [row.ev(f, row.xs[i]) for i in range(n)]
        D = rnd.sample(range(n), 3)
        for i in D:
            w[i] = (w[i] + 1 + rnd.randrange(q - 1)) % q
        ag, agset = max_agreement(row, H, w, 4)
        bf, _ = brute_max_agreement(row, w)
        chk(f"planted 3-error word decodes exactly (trial {trial})",
            ag == bf and ag >= n - 3, f"{ag} vs {bf}")
    falsifier("LB-F9", False, "oracle == brute force on all trials")

    # LEMMA R replay on the sibling's own fixtures
    for nm, b in (("Zfib11", E1V.fibre_system(31, 2, 11, 17, 3)),
                  ("E1P", E1V.fibre_system(31, 3, 10, 22, 5, True)),
                  ("X1p", E1V.build_X1p())):
        if b is None:
            chk(f"{nm}: built", False, "")
            continue
        row, sup, zs = b["row"], b["supports"], b["slopes"]
        dim, rank, m, nontriv = ann_dims(row, sup, zs)
        ok = (nontriv == 2 * m - rank)
        chk(f"{nm}: LEMMA R  dim(realisers)-2k-2(n-|U|) = 2m - rank",
            ok, f"{nontriv} vs {2*m-rank} (rank {rank}, m {m}, n {row.n})")
        if not ok:
            falsifier("LB-F8", True, f"{nm}: {nontriv} vs {2*m-rank}")
        print(f"    {nm}: n={row.n} k={row.k} h={row.h} V={len(sup)} m={m} "
              f"rank={rank} 2m={2*m} dim_Ann={nontriv}")
    falsifier("LB-F8", False, "LEMMA R identity holds on all three")


# =====================================================================
# PART 2 -- E1P dissection: WHERE the extra agreement sits (P1, LB-F3)
# =====================================================================
def part2_e1p():
    print("\nPART 2 -- E1P dissection: the escape-1 ray's extra agreement")
    b = E1V.fibre_system(31, 3, 10, 22, 5, True)
    row, sup, zs = b["row"], b["supports"], b["slopes"]
    n, k, h, q = row.n, row.k, row.h, row.q
    A = k + h
    H = parity(row)
    mult = S.multiplicity([set(x) for x in sup], n)
    live, Ts, esc = core_of(row, sup)
    priv = [i for i in sup[0] if mult[i] == 1]
    removed = sorted(set(b["blocks"][1]) - set(sup[0]))
    chk("E1P: escape vector (1,0,...,0)",
        esc[0] == 1 and set(esc[1:]) == {0}, esc)
    chk("E1P: the escaped point is the private (mult-1) point",
        len(priv) == 1 and priv[0] == sorted(set(sup[0]) - set(Ts[0]))[0],
        (priv, sorted(set(sup[0]) - set(Ts[0]))))
    chk("E1P: exactly one point was removed from the unperturbed support",
        len(removed) == 1, removed)
    x0, y = removed[0], priv[0]
    dim, rank, m, nontriv = ann_dims(row, sup, zs)
    ns = ann_basis(row, sup, zs)
    reps = draw_realisers(row, ns, 12, seed=3)
    chk("E1P: nondegenerate realisers drawn", len(reps) >= 8, len(reps))
    extras, exacts, overs = set(), 0, 0
    for u, v in reps:
        rr = ray_report(row, H, u, v, sup, zs, rays={0})
        r0 = rr[0]
        chk("E1P: realiser agrees on all of S_0 (construction guarantee)",
            not r0["own_missing"], r0["own_missing"])
        if r0["exact_A"]:
            exacts += 1
        if r0["over"]:
            overs += 1
        extras |= set(r0["own_extra"])
    print(f"    E1P: m={m} rank={rank} dim_Ann={nontriv} | draws={len(reps)}"
          f" exact-A={exacts} over-A={overs} | extra points={sorted(extras)}"
          f" (removed x0={x0}, private y={y})")
    chk("E1P: EVERY nondegenerate realiser over-agrees on the escape-1 ray",
        overs == len(reps) and exacts == 0, (overs, exacts, len(reps)))
    chk("P1: the extra agreement point is exactly the REMOVED point x0",
        extras == {x0}, (sorted(extras), x0))
    if exacts:
        falsifier("LB-F3", True, f"{exacts} realisers made ray 0 exact-A")
    else:
        falsifier("LB-F3", False, f"{len(reps)} draws, all A+1")
    # the dichotomy machinery: forced points
    dimR, forced, dimA = psi_forced(row, sup, zs, 0, {y})
    sup2 = list(sup)
    sup2[0] = tuple(sorted(set(sup[0]) - {y}))
    pr1 = proj_rank(row, ann_basis(row, sup, zs), {y})
    pr2 = proj_rank(row, ann_basis(row, sup2, zs), {y})
    print(f"    E1P: dim Ann(Sigma~) = {dimR} vs dim Ann(Sigma) = {dimA}; "
          f"forced over-agreement points = {forced}; projections away from "
          f"the private point: {pr1} vs {pr2}")
    chk("E1P: dropping the PRIVATE escaped point's condition adds exactly "
        "the one free direction at that point", dimR == dimA + 1,
        (dimR, dimA))
    chk("LEMMA P (private-point freedom): away from the private point the "
        "two realiser spaces coincide", pr1 == pr2, (pr1, pr2))
    chk("E1P: x0 is a FORCED over-agreement point (Psi_x0 = 0 on all of R)",
        x0 in forced, (forced, x0))
    LOG["fixtures"].append(dict(name="E1P", n=n, k=k, h=h, m=m, rank=rank,
                                dim_Ann=nontriv, escapes=esc, x0=x0, y=y,
                                forced=forced, draws=len(reps),
                                over=overs, exact_A=exacts))


# =====================================================================
# PART 3 -- THEOREM F: fibre rigidity (P2, P3, LB-F4)
# =====================================================================
def theoremF_predict(d, h):
    """dim of the pinned space {lam_j = 0, mu_{d+j} = 0, lam_{d+j} = mu_j}
    with m = d + h:  free mu_j for j in [max(0,h-d), d-1]."""
    return max(0, d - max(0, h - d))


def build_group_fibre(q, d, V, h, perturb=False, N=None, mode="private"):
    """U = the multiplicative subgroup H of order N (default q-1);
    blocks = V distinct fibres of x -> x^d on H; S_a = H \\ B_a;
    slopes = the fibre parameters.  perturb: swap one point of S_0 for a
    fresh point outside H (escape 1).  Point set = H (+ the fresh point)."""
    N = N or (q - 1)
    if (q - 1) % N or N % d:
        return None
    g = None
    for cand in range(2, q):
        if pow(cand, N, q) == 1 and all(pow(cand, N // p, q) != 1
                                        for p in (2, 3, 5, 7, 11, 13)
                                        if N % p == 0):
            g = cand
            break
    if g is None:
        return None
    Hset = sorted({pow(g, i, q) for i in range(N)})
    if len(Hset) != N:
        return None
    fib = {}
    for x in Hset:
        fib.setdefault(pow(x, d, q), []).append(x)
    cs = [c for c in sorted(fib) if len(fib[c]) == d][:V]
    if len(cs) < V:
        return None
    A = N - d
    k = A - h
    if k < 2:
        return None
    pts = list(Hset)
    fresh = None
    if perturb and mode == "private":
        cand = [x for x in range(q) if x not in set(Hset)]
        if not cand:
            return None
        fresh = cand[0]
        pts = sorted(Hset + [fresh])
    xs = pts
    n = len(xs)
    idx = {v: i for i, v in enumerate(xs)}
    row = T.Row2(n, k, h, q, xs=xs)
    blocks = [[idx[x] for x in fib[c]] for c in cs]
    Hi = set(idx[x] for x in Hset)
    sup = [tuple(sorted(Hi - set(bl))) for bl in blocks]
    x0 = None
    if perturb and mode == "private":
        x0 = blocks[1][0]                       # a point of B_1, in S_0
        sup[0] = tuple(sorted((set(sup[0]) - {x0}) | {idx[fresh]}))
    elif perturb and mode == "swap":
        # repair from inside B_0: no private point anywhere
        x0 = blocks[1][0]
        sup[0] = tuple(sorted((set(sup[0]) - {x0}) | {blocks[0][0]}))
    elif perturb and mode == "dswap":
        # delete ONE point from TWO supports: at V = 5 this is what it takes
        # to push a block point down to multiplicity 2 (LEMMA V4)
        if V < 5:
            return None
        x0 = blocks[V - 1][0]
        for a in (0, 1):
            sup[a] = tuple(sorted((set(sup[a]) - {x0}) | {blocks[a][0]}))
    zs = [c % q for c in cs]
    if len(set(zs)) != V:
        return None
    return dict(row=row, supports=sup, slopes=zs, blocks=blocks,
                x0=x0, y=(idx[fresh] if fresh is not None else None),
                meta=dict(q=q, N=N, d=d, V=V, h=h, k=k, A=A, n=n))


def part3_theoremF():
    print("\nPART 3 -- THEOREM F (fibre rigidity): 3 rays pin Ann; "
          "dim Ann = max(0, d - max(0, h-d))")
    grid = [(31, 3, 10, 5), (31, 3, 6, 5), (31, 3, 5, 4), (31, 2, 11, 3),
            (31, 2, 8, 3), (31, 5, 6, 6), (17, 4, 4, 6), (17, 2, 8, 3),
            (19, 3, 6, 4), (19, 2, 9, 3), (37, 4, 9, 5), (37, 3, 8, 4),
            (41, 4, 10, 6), (43, 6, 7, 8), (29, 4, 7, 5), (29, 7, 4, 8)]
    good = 0
    for (q, d, V, h) in grid:
        b = build_group_fibre(q, d, V, h)
        if b is None:
            continue
        row, sup, zs = b["row"], b["supports"], b["slopes"]
        pred = theoremF_predict(d, h)
        dim, rank, m, nontriv = ann_dims(row, sup, zs)
        okm = (m == d + h)
        okdim = (nontriv == pred)
        # 3-ray pinning: Ann of any 3 rays equals Ann of all V
        pins = []
        for sub in ([0, 1, 2], [0, 1, V - 1], [V - 3, V - 2, V - 1]):
            if max(sub) >= V:
                continue
            s3 = [sup[i] for i in sub]
            z3 = [zs[i] for i in sub]
            _, r3, _, nt3 = ann_dims(row, s3, z3)
            pins.append(nt3)
        okpin = all(p == nontriv for p in pins)
        g = gates_of(row, sup)
        rec = dict(q=q, d=d, V=V, h=h, k=row.k, m=m, rank=rank,
                   dim_Ann=nontriv, predicted=pred, pins=pins,
                   kpacking=g["kpacking_ok"], pairwise=g["pairwise_intersecting"],
                   max_triple=g["max_triple"], min_pair=min(g["pair"].values()))
        LOG["theoremF"].append(rec)
        good += 1
        print(f"    q={q} d={d} V={V} h={h} k={row.k}: m={m} (=d+h:{okm}) "
              f"rank={rank} dim_Ann={nontriv} predicted={pred} "
              f"3-ray pins={pins} | (T) {g['kpacking_ok']} (P) "
              f"{g['pairwise_intersecting']}")
        chk(f"THEOREM F [q={q},d={d},V={V},h={h}]: m = d + h", okm, m)
        chk(f"THEOREM F [q={q},d={d},V={V},h={h}]: dim Ann = prediction",
            okdim, f"{nontriv} vs {pred}")
        chk(f"THEOREM F [q={q},d={d},V={V},h={h}]: any 3 rays pin Ann",
            okpin, pins)
        if not (okdim and okpin):
            falsifier("LB-F4", True, rec)
    chk("THEOREM F tested on >= 10 group-fibre members", good >= 10, good)
    falsifier("LB-F4", any(t == "LB-F4" for t in HITS),
              f"{good} members, prediction and pinning")


def part3b_theoremF_corollary():
    print("\nPART 3b -- COROLLARY F1: perturbed group-fibre systems always "
          "over-agree on the escape-1 ray (E1P is one member)")
    grid = [(31, 3, 10, 5), (31, 3, 6, 5), (31, 5, 6, 6), (17, 4, 4, 6),
            (19, 3, 6, 4), (37, 4, 9, 5), (29, 4, 7, 5)]
    tested = 0
    for (q, d, V, h) in grid:
        b = build_group_fibre(q, d, V, h, perturb=True)
        if b is None:
            continue
        row, sup, zs = b["row"], b["supports"], b["slopes"]
        n, k = row.n, row.k
        A = k + h
        H = parity(row)
        live, Ts, esc = core_of(row, sup)
        if esc[0] != 1:
            continue
        x0, y = b["x0"], b["y"]
        dimR, forced, dimA = psi_forced(row, sup, zs, 0, {y})
        ns = ann_basis(row, sup, zs)
        import math
        cheap = math.comb(n, n - A - 1) <= 12000
        reps = draw_realisers(row, ns, 4 if cheap else 0, seed=5)
        overs = sum(1 for (u, v) in reps
                    if ray_report(row, H, u, v, sup, zs, rays={0})[0]["over"])
        rec = dict(q=q, d=d, V=V, h=h, k=k, n=n, escapes=esc, forced=forced,
                   x0=x0, y=y, dimR=dimR, dimA=dimA, draws=len(reps),
                   over=overs)
        LOG["fixtures"].append(dict(name=f"gfib({q},{d},{V},{h})+perturb",
                                    **rec))
        tested += 1
        print(f"    q={q} d={d} V={V} h={h}: esc={esc[:3]}... forced="
              f"{forced} (x0={x0}) dim Ann(Sigma~)={dimR} dim Ann={dimA} "
              f"| draws={len(reps)} over-agreeing={overs}")
        chk(f"COROLLARY F1 [q={q},d={d},V={V},h={h}]: x0 forced",
            x0 in forced, (forced, x0))
        if reps:
            chk(f"COROLLARY F1 [q={q},d={d},V={V},h={h}]: every draw "
                "over-agrees", overs == len(reps), (overs, len(reps)))
        sup2 = list(sup)
        sup2[0] = tuple(sorted(set(sup[0]) - {y}))
        pr1 = proj_rank(row, ann_basis(row, sup, zs), {y})
        pr2 = proj_rank(row, ann_basis(row, sup2, zs), {y})
        chk(f"COROLLARY F1 [q={q},d={d},V={V},h={h}]: LEMMA P -- away from "
            "the private point the realiser spaces coincide", pr1 == pr2,
            (pr1, pr2))
        chk(f"COROLLARY F1 [q={q},d={d},V={V},h={h}]: private point adds "
            "exactly one free direction", dimR == dimA + 1, (dimR, dimA))
    chk("COROLLARY F1 tested on >= 3 perturbed members", tested >= 3, tested)
    print("\n    COROLLARY F2 (as CORRECTED by measurement -- the in-run "
          "conjecture 'swap => not realisable' was FALSE): the SWAP "
          "perturbation is often realisable, but its perturbed ray is "
          "FORCED to over-agree, and LEMMA V4: escapes need V <= 4")
    import math
    tested2 = 0
    for (q, d, V, h) in grid + [(31, 2, 11, 3), (41, 4, 10, 6), (43, 6, 7, 8)]:
        b = build_group_fibre(q, d, V, h, perturb=True, mode="swap")
        if b is None:
            continue
        row, sup, zs = b["row"], b["supports"], b["slopes"]
        n, k = row.n, row.k
        A = k + h
        live, Ts, esc = core_of(row, sup)
        dim, rank, m, nontriv = ann_dims(row, sup, zs)
        dimR, forced, dimA = psi_forced(row, sup, zs, 0, set())
        tested2 += 1
        cheap = math.comb(n, n - A - 1) <= 30000
        overs, ndraw = 0, 0
        if nontriv > 0 and cheap:
            H = parity(row)
            reps = draw_realisers(row, ann_basis(row, sup, zs), 3, seed=9)
            ndraw = len(reps)
            overs = sum(1 for (u, v) in reps
                        if ray_report(row, H, u, v, sup, zs,
                                      rays={0})[0]["over"])
        print(f"      q={q} d={d} V={V} h={h}: esc={esc[:4]}"
              f"{'...' if V > 4 else ''} rank={rank} 2m={2*m} "
              f"dim_Ann={nontriv} | forced points for the perturbed ray="
              f"{forced} | draws={ndraw} over-agreeing={overs}")
        chk(f"COROLLARY F2 [q={q},d={d},V={V},h={h}]: the perturbed ray has "
            "a FORCED over-agreement point", len(forced) >= 1, forced)
        if ndraw:
            chk(f"COROLLARY F2 [q={q},d={d},V={V},h={h}]: every realiser "
                "over-agrees on the perturbed ray", overs == ndraw,
                (overs, ndraw))
        chk(f"LEMMA V4 [q={q},d={d},V={V},h={h}]: a one-point perturbation "
            "creates an escape only when V <= 4",
            (max(esc) == 0) == (V > 4), (V, esc))
        LOG["fixtures"].append(dict(name=f"gfib({q},{d},{V},{h})+swap",
                                    escapes=esc, rank=rank, twom=2 * m,
                                    dim_Ann=nontriv, forced=forced,
                                    draws=ndraw, over=overs))
    chk("COROLLARY F2 tested on >= 5 members", tested2 >= 5, tested2)


# =====================================================================
# PART 4 -- the DICHOTOMY and the refutation search (LB-F1/F2/F5/F6/F10)
# =====================================================================
def full_live_system(row, H, u, v, rmax):
    """All finite slopes with max agreement >= A, with their agreement sets,
    plus the (0:1) direction agreement.  EXACT (syndrome enumeration)."""
    n, k, h, q = row.n, row.k, row.h, row.q
    A = k + h
    out = {}
    for z in range(q):
        w = ray_word(row, u, v, z)
        ag, agset = max_agreement(row, H, w, rmax)
        if ag is not None and ag >= A:
            out[z] = (ag, agset)
    agv, _ = max_agreement(row, H, list(v), rmax)
    return out, agv


def live_core_test(row, H, u, v, name=""):
    """THE decisive measurement: from the received pair (u,v) alone,
    recompute the live-slope system EXACTLY (every z in F_q with max
    agreement = A, with its selected support), then its (3,k+1)-core and
    escapes.  V_1 > 0 with the tangent gate intact refutes L-B."""
    n, k, h, q = row.n, row.k, row.h, row.q
    A = k + h
    sysmap, agv = full_live_system(row, H, u, v, n - A)
    over = sorted(z for z in sysmap if sysmap[z][0] > A)
    live = sorted(z for z in sysmap if sysmap[z][0] == A)
    sups = [tuple(sorted(sysmap[z][1])) for z in live]
    rec = dict(name=name, live_slopes=live, over_agreeing_slopes=over,
               v_direction=agv, tangent_free=(not over and (agv is None
                                                            or agv <= A)),
               V=len(live))
    if sups:
        core, Ts, esc = core_of(row, sups)
        g = gates_of(row, sups)
        rec.update(core=sorted(core), escapes=esc,
                   V_1=[a for a in sorted(core) if esc[a] == 1],
                   kpacking_ok=g["kpacking_ok"], max_triple=g["max_triple"],
                   min_pair=(min(g["pair"].values()) if len(sups) > 1
                             else None))
    else:
        rec.update(core=[], escapes=[], V_1=[], kpacking_ok=True)
    print(f"      LIVE SYSTEM [{name}]: {len(live)} exact-A slopes, "
          f"{len(over)} over-agreeing {over}, v-dir={agv} | core="
          f"{rec['core']} esc={rec['escapes']} V_1={rec['V_1']} | "
          f"tangent_free={rec['tangent_free']} kpack={rec['kpacking_ok']}")
    return rec


def analyse_fixture(name, b, draws=12, seed=7, do_full=True, note=""):
    """The full L-B test on one fixture."""
    row, sup, zs = b["row"], b["supports"], b["slopes"]
    n, k, h, q = row.n, row.k, row.h, row.q
    A = k + h
    V = len(sup)
    H = parity(row)
    g = gates_of(row, sup)
    live, Ts, esc = core_of(row, sup)
    dim, rank, m, nontriv = ann_dims(row, sup, zs)
    gate_clean = bool(g["size_ok"] and g["pairwise_intersecting"]
                      and g["kpacking_ok"])
    print(f"  [{name}] n={n} k={k} h={h} V={V} q={q} A={A} m={m} | "
          f"gate_clean={gate_clean} (T)<={g['max_triple']} (P)>="
          f"{min(g['pair'].values())} | core={sorted(live)} esc={esc} | "
          f"rank={rank} 2m={2*m} dim_Ann={nontriv}")
    rec = dict(name=name, note=note, n=n, k=k, h=h, V=V, q=q, A=A, m=m,
               rank=rank, dim_Ann=nontriv, escapes=esc, core=sorted(live),
               gate_clean=gate_clean, max_triple=g["max_triple"],
               min_pair=min(g["pair"].values()))
    if nontriv <= 0:
        rec["verdict"] = "not band-admissible (rank = 2m, LEMMA R)"
        print("      -> no nontrivial realiser (LEMMA R): not admissible")
        LOG["search"].append(rec)
        return rec
    # escape-1 core rays
    e1rays = [a for a in sorted(live) if esc[a] == 1]
    rec["escape1_core_rays"] = e1rays
    forced_by_ray = {}
    for a in (sorted(live) if V <= 6 else e1rays):
        drop = set(sup[a]) - set(Ts[a])
        dimR, forced, dimA = psi_forced(row, sup, zs, a, drop)
        forced_by_ray[a] = dict(dropped=sorted(drop), forced=forced,
                                dimR=dimR, dimA=dimA)
        print(f"      ray {a}: escaped {sorted(drop)} | dim Ann(Sigma~)="
              f"{dimR} vs {dimA} | FORCED over-agreement points = {forced}")
    rec["psi"] = forced_by_ray
    # sample realisers, exact agreements
    ns = ann_basis(row, sup, zs)
    reps = draw_realisers(row, ns, draws, seed=seed)
    stats = []
    hit = None
    for u, v in reps:
        rr = ray_report(row, H, u, v, sup, zs)
        chk(f"{name}: realiser agrees on every S_a (construction guarantee)",
            not any(r["own_missing"] for r in rr),
            [r["own_missing"] for r in rr])
        prof = tuple(r["max_agr"] for r in rr)
        stats.append(prof)
        if all(r["max_agr"] == A for r in rr) and hit is None:
            hit = (u, v, rr)
    rec["agreement_profiles"] = [list(p) for p in stats[:6]]
    rec["draws"] = len(reps)
    e1_exact = 0
    for prof in stats:
        if all(p == A for p in prof):
            e1_exact += 1
    rec["draws_all_rays_exact_A"] = e1_exact
    print(f"      draws={len(reps)} profiles(first 3)={stats[:3]} | "
          f"all-rays-exact-A draws={e1_exact}")
    # LB-F2 exactly as pre-registered: a gate-clean escape-1 system with a
    # nondegenerate realiser making an escape-1 CORE ray exact-A.
    e1_exactA = sorted({a for prof in stats for a in e1rays
                        if prof[a] == A})
    rec["escape1_rays_that_are_exact_A"] = e1_exactA
    if gate_clean and e1_exactA:
        falsifier("LB-F2", True, f"{name}: gate-clean escape-1 core rays "
                  f"{e1_exactA} are exact-A under a nondegenerate realiser "
                  f"(profiles {stats[:2]})")
    rec["found_all_exact_A"] = hit is not None
    # THE decisive test: the live system of the actual received pair
    import math
    if do_full and reps:
        cost = sum(math.comb(n, r) for r in range(1, n - A + 1)) * q
        rec["live_scan_cost"] = cost
        if cost > 4_000_000:
            rec["live_system"] = "SKIPPED (scan cost -- COMPUTE REQUEST)"
            print(f"      live-system scan skipped (cost {cost})")
        else:
            picks = [hit[:2]] if hit else []
            picks += [rp for rp in reps[:2] if not picks or rp is not picks[0]]
            outs = []
            for (u, v) in picks[:2]:
                lr = live_core_test(row, H, u, v, name=name)
                outs.append(lr)
                if lr["V_1"]:
                    if lr["tangent_free"] and lr["kpacking_ok"]:
                        if math.comb(n, k) <= 60000:
                            grec, _, _ = S.gate_report(row, u, v, name=name)
                            lr["full_gate"] = {
                                kk: grec.get(kk) for kk in
                                ["below_cascade", "globally_generic",
                                 "tangent_free_finite_slopes",
                                 "tangent_free_v_direction", "v_nonvanishing",
                                 "kpacking_ok", "FULL_GATE", "live_slopes",
                                 "max_ray_agreement"]}
                            print("      occlib gate: " + "  ".join(
                                f"{kk}={vv}" for kk, vv in
                                lr["full_gate"].items()))
                            if grec.get("FULL_GATE"):
                                falsifier("LB-F1", True,
                                          f"{name}: FULL_GATE pair with "
                                          f"exact-A escape-1 core rays "
                                          f"{lr['V_1']}")
                            else:
                                falsifier("LB-F2", True,
                                          f"{name}: exact-A escape-1 core "
                                          f"rays {lr['V_1']}, occlib gate "
                                          f"{grec.get('FULL_GATE')}")
                        else:
                            falsifier("LB-F2", True,
                                      f"{name}: exact-A escape-1 core rays "
                                      f"{lr['V_1']} (occlib gate not "
                                      f"decidable at this scale)")
                    else:
                        print("      (escape-1 core rays present but the "
                              "pair fails tangent-freeness / k-packing)")
            rec["live_system"] = outs
    LOG["search"].append(rec)
    return rec


def build_swap(q=17, k=6, t=4, victim=3, which=0):
    """SWAP fixture -- escape 1 with NO private point.

    Four fibres of x^t over F_q^* with the cross-ratio-matched slopes of the
    collapse pilot's THEOREM 4(c) (as in the sibling's X1p), but ray 0's
    support is repaired from INSIDE its own block instead of by a fresh
    private point:  S_0 = (U \\ B_0 \\ {x}) u {b},  x in B_victim, b in B_0.
    Then x drops to multiplicity 2 (it escapes from the two other rays that
    still hold it) while b rises to V; no point has multiplicity 1, so no
    ray carries a private escape."""
    got = E1V.build_X1p(q, k, t)
    if got is None:
        return None
    row, base, zs = got["row"], got["base"], got["slopes"]
    blocks = None
    # recover the blocks from the base supports: B_a = U \ S_a
    U = set().union(*[set(x) for x in base])
    blocks = [sorted(U - set(base[a])) for a in range(4)]
    if victim == 0:
        return None
    x = blocks[victim][which % len(blocks[victim])]
    b = blocks[0][which % len(blocks[0])]
    sup = list(base)
    sup[0] = tuple(sorted((set(base[0]) - {x}) | {b}))
    return dict(row=row, supports=sup, slopes=zs, blocks=blocks,
                meta=dict(q=q, k=k, t=t, x=x, b=b, victim=victim))


def part4_search():
    print("\nPART 4 -- the refutation search: escape-1 core rays that ARE "
          "exact-A")
    out = {}
    # (a) X1p: the cross-ratio-matched 4-fibre perturbation (escapes 1,1,1,0)
    for (q, k, t) in ((17, 6, 4), (13, 4, 3), (19, 6, 4), (29, 8, 7),
                      (31, 8, 6), (37, 10, 9)):
        b = E1V.build_X1p(q, k, t)
        if b is None:
            continue
        row = b["row"]
        if row.n - (row.k + row.h) - 1 > 4:
            continue
        rec = analyse_fixture(f"X1p({q},{k},{t})", b, draws=10,
                              note="cross-ratio matched 4-fibre perturbation")
        out[f"X1p({q},{k},{t})"] = rec
    # (b) the unperturbed cross-ratio system, for contrast
    for (q, k, t) in ((17, 6, 4), (13, 4, 3)):
        b = E1V.build_X1p(q, k, t)
        if b is None:
            continue
        b2 = dict(row=b["row"], supports=b["base"], slopes=b["slopes"])
        analyse_fixture(f"X0({q},{k},{t}) unperturbed", b2, draws=6,
                        note="zero escape, contrast")
    # (c) SWAP: escape 1 with NO private point (the sharpest candidate)
    for (q, k, t) in ((17, 6, 4), (13, 4, 3), (19, 6, 4), (31, 8, 6)):
        for victim in (1, 2, 3):
            b = build_swap(q, k, t, victim=victim)
            if b is None:
                continue
            row = b["row"]
            if row.n - (row.k + row.h) - 1 > 4:
                continue
            rec = analyse_fixture(f"SWAP({q},{k},{t},victim={victim})", b,
                                  draws=10,
                                  note="escape 1 with no private point")
            out[f"SWAP({q},{k},{t},v{victim})"] = rec
    # (d) DSWAP at V = 5: the only other way (LEMMA V4) to reach a
    #     multiplicity-2 point -- delete it from TWO supports
    for (q, d, V, h) in ((31, 3, 5, 5), (19, 3, 5, 4), (37, 3, 5, 4),
                         (31, 2, 5, 3)):
        b = build_group_fibre(q, d, V, h, perturb=True, mode="dswap")
        if b is None:
            continue
        row = b["row"]
        if row.n - (row.k + row.h) - 1 > 3:
            continue
        rec = analyse_fixture(f"DSWAP({q},{d},V={V},{h})", b, draws=8,
                              note="V=5, point deleted from two supports")
        out[f"DSWAP({q},{d},{V},{h})"] = rec
    return out


# =====================================================================
# PART 5 -- sibling sharp question: all-escape-1 with dim Ann = 1 (LB-F7)
# =====================================================================
def part5_all_escape1():
    print("\nPART 5 -- sibling flag 6: an all-escape-1 gate-clean system "
          "with dim Ann = 1?")
    rnd = random.Random(21)
    found = []
    tested = 0
    for h in (4, 5, 6):
        for s in range(max(1, -(-h // 2)), h - 1):
            for p in (3, 4, 5, 6):
                for kk in (11, 15, 19, 23):
                    b = E1V.build_E1(h, s, p, kk)
                    if b is None:
                        continue
                    row, sup = b["row"], b["supports"]
                    g = gates_of(row, sup)
                    if not (g["size_ok"] and g["pairwise_intersecting"]
                            and g["kpacking_ok"]):
                        continue
                    live, Ts, esc = core_of(row, sup)
                    if set(esc) != {1} or len(live) != len(sup):
                        continue
                    V = len(sup)
                    U = set().union(*[set(x) for x in sup])
                    m = len(U) - row.k
                    best = None
                    for trial in range(14):
                        zs = rnd.sample(range(row.q), V)
                        rank = S.family_rank(row, sup, zs)
                        tested += 1
                        if best is None or rank < best:
                            best = rank
                        if rank < 2 * m:
                            found.append(dict(h=h, s=s, p=p, k=kk, V=V, m=m,
                                              rank=rank, slopes=zs))
                    # WHY no deficit: a support-4 relation needs a common
                    # pencil support of >= k+2 points inside the 4-wise
                    # intersection (S4-5/S4-6).  Measure the 4-wise cap.
                    Ss = [set(x) for x in sup]
                    q4 = max(len(Ss[a] & Ss[b] & Ss[c] & Ss[d])
                             for a in range(V) for b in range(a + 1, V)
                             for c in range(b + 1, V)
                             for d in range(c + 1, V))
                    chk(f"E1 shape (h={h},s={s},p={p},k={kk}): 4-wise "
                        "intersection < k+2, so NO support-4 relation exists",
                        q4 < row.k + 2, (q4, row.k + 2))
                    LOG.setdefault("all_escape1", []).append(
                        dict(h=h, s=s, p=p, k=kk, V=V, m=m, best_rank=best,
                             twom=2 * m, max_quad=q4, kplus2=row.k + 2))
    print(f"    all-escape-1 gate-clean shapes scanned: "
          f"{len(LOG.get('all_escape1', []))}, slope tuples: {tested}, "
          f"deficits found: {len(found)}")
    chk("all-escape-1 shape scan ran", tested >= 100, tested)
    if found:
        falsifier("LB-F7", True, found[:2])
    else:
        falsifier("LB-F7", False, f"{tested} tuples, no rank deficit")
    LOG["all_escape1_deficits"] = found[:5]


def main():
    print("L-B ESCAPE-1 OVER-AGREEMENT -- verification")
    part1_oracles()
    part2_e1p()
    part3_theoremF()
    part3b_theoremF_corollary()
    part4_search()
    part5_all_escape1()
    LOG["total_checks"] = CHECKS[0]
    LOG["fails"] = FAILS
    LOG["falsifiers_fired"] = sorted(set(HITS))
    with open(os.path.join(HERE, "verify.json"), "w") as fh:
        json.dump(LOG, fh, indent=1, sort_keys=True, default=str)
    print(f"\nCHECKS {CHECKS[0]}  FAILS {len(FAILS)}  "
          f"FALSIFIERS_FIRED {len(set(HITS))}")
    for f in FAILS:
        print("  - FAIL", f)
    for t in sorted(set(HITS)):
        print("  - FALSIFIER", t)
    if not FAILS:
        print("LB_ESCAPE1_OVERAGREEMENT_ALL_PASS")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())

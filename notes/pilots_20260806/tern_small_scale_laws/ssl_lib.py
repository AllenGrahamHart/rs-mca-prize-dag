#!/usr/bin/env python3
"""Round 19 -- TERNARY SMALL-SCALE LAWS: ONE exact census framework.

All three instance miniatures are the same shape:

    CT(N, p, T) = { v in {0,+-1}^N : sum_{i<N} v_i omega^{s i} = 0,  s in T }

with M = 2N and omega a primitive M-th root of unity in characteristic p.

    I3(n,p,w)     = CT(n/2, p, <p>-closure of {odd s in [1,w-1]})
    I2(L,p)       = CT(L,   p, <p>-closure of {1})
    I1(2N,p,R,a)  = CT(N,   p, {a,...,a+R-1})     [p = 1 mod 2N, so <p>={1}]

Everything is EXACT integer / F_p arithmetic.  Floats appear only in
printed diagnostics, never in a decision path.

Banked machinery reused (read-only, never edited):
  notes/pilots_20260806/efloor_sparsity/sp_lib.py   (phi_factors, census_by_weight)
  notes/pilots_20260806/es_coprimality/cop_lib.py   (F_p polynomial arithmetic)
"""

import os
import sys

sys.dont_write_bytecode = True

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, os.pardir, "efloor_sparsity"))

import sp_lib  # noqa: E402  (banked round-18 machinery, read-only source)


# --------------------------------------------------------------------------
# primitive M-th roots of unity in characteristic p
# --------------------------------------------------------------------------

def _is_two_power(x):
    return x >= 2 and (x & (x - 1)) == 0


def root_powers(M, p, factor_index=0):
    """(delta, pw) with pw[s] = F_p-coordinate vector of omega^s, s in [0,M).

    2-power M: omega = X mod g, g the (sorted) factor_index-th irreducible
    factor of X^{M/2}+1 over F_p -- the SAME convention as the banked
    efloor_sparsity/verify_sp.py:467.  Works for every odd p.

    composite M: requires p = 1 mod M (the z1/I1 protocol, where the
    half-system must live in F_p^*), delta = 1.
    """
    assert p % 2 == 1 and M % 2 == 0
    if _is_two_power(M):
        fs = sp_lib.phi_factors(M, p)
        g = fs[factor_index]
        delta = len(g) - 1
        pw = []
        cur = [1]
        for _ in range(M):
            pw.append(tuple((cur + [0] * delta)[:delta]))
            cur = sp_lib.prem([0] + cur, g, p)
        # omega has order exactly M: omega^{M/2} = -1
        half = pw[M // 2]
        assert half == tuple(((-1) % p,) + (0,) * (delta - 1)), \
            "omega^{M/2} != -1"
        return delta, pw, len(fs)
    if p % M != 1:
        raise ValueError("composite M=%d needs p = 1 mod M (got p=%d)" % (M, p))
    # primitive M-th root inside F_p
    om = None
    for cand in range(2, p):
        t = pow(cand, (p - 1) // M, p)
        ok = True
        for q in _prime_divisors(M):
            if pow(t, M // q, p) == 1:
                ok = False
                break
        if ok:
            om = t
            break
    assert om is not None, "no primitive M-th root in F_p"
    return 1, [(pow(om, s, p),) for s in range(M)], 1


def _prime_divisors(x):
    out, d = set(), 2
    while d * d <= x:
        while x % d == 0:
            out.add(d)
            x //= d
        d += 1
    if x > 1:
        out.add(x)
    return sorted(out)


def p_closure(T, M, p):
    """The smallest superset of T closed under multiplication by p mod M."""
    out = set()
    for s in T:
        c = s % M
        while c not in out:
            out.add(c)
            c = c * p % M
    return out


# --------------------------------------------------------------------------
# the condition system and its exact F_p rank
# --------------------------------------------------------------------------

def condition_matrix(N, p, T, delta, pw):
    """Rows of the F_p-linear system; column i <-> coordinate v_i."""
    M = 2 * N
    rows = []
    for s in sorted(T):
        for j in range(delta):
            rows.append([pw[(s * i) % M][j] for i in range(N)])
    return rows


def rref(rows, p):
    """Row-reduced echelon form over F_p; returns (rank, reduced rows)."""
    mat = [list(r) for r in rows]
    ncol = len(mat[0]) if mat else 0
    piv, r = [], 0
    for c in range(ncol):
        sel = None
        for i in range(r, len(mat)):
            if mat[i][c] % p:
                sel = i
                break
        if sel is None:
            continue
        mat[r], mat[sel] = mat[sel], mat[r]
        inv = pow(mat[r][c], p - 2, p)
        mat[r] = [(x * inv) % p for x in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][c] % p:
                f = mat[i][c]
                mat[i] = [(a - f * b) % p for a, b in zip(mat[i], mat[r])]
        piv.append(c)
        r += 1
        if r == len(mat):
            break
    return r, [mat[i] for i in range(r)], piv


def null_basis(rows, p, N):
    """A basis of the F_p null space of the condition system."""
    if not rows:
        return [[1 if i == j else 0 for i in range(N)] for j in range(N)]
    rank, red, piv = rref(rows, p)
    free = [c for c in range(N) if c not in piv]
    basis = []
    for fc in free:
        v = [0] * N
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-red[i][fc]) % p
        basis.append(v)
    return basis


def is_self_orthogonal(basis, p):
    """Direct test: C <= C^perp, i.e. every pairwise inner product is 0."""
    for a in range(len(basis)):
        for b in range(a, len(basis)):
            s = sum(x * y for x, y in zip(basis[a], basis[b])) % p
            if s:
                return False
    return True


# --------------------------------------------------------------------------
# EXACT ternary census -- meet in the middle over {0,+-1}^N
# --------------------------------------------------------------------------

def _cols(rows, p, N):
    rank, red, _ = rref(rows, p) if rows else (0, [], [])
    return rank, [tuple(red[r][i] for r in range(rank)) for i in range(N)]


def _half_table(cols, idxs, p, rank):
    """syn -> [count by weight]; exact over all 3^{len(idxs)} ternary halves."""
    zero = (0,) * rank
    tab = {zero: [1]}
    for i in idxs:
        c = cols[i]
        cm = tuple((-x) % p for x in c)
        nd = {}
        for syn, wd in tab.items():
            for d, extra in ((None, 0), (c, 1), (cm, 1)):
                if d is None:
                    s2 = syn
                else:
                    s2 = tuple((a + b) % p for a, b in zip(syn, d))
                cur = nd.get(s2)
                if cur is None:
                    cur = [0] * (len(wd) + 1)
                    nd[s2] = cur
                elif len(cur) < len(wd) + 1:
                    cur.extend([0] * (len(wd) + 1 - len(cur)))
                for w, cnt in enumerate(wd):
                    if cnt:
                        cur[w + extra] += cnt
        tab = nd
    return tab


def ternary_weight_distribution(N, p, rows):
    """EXACT weight distribution of { v in {0,+-1}^N : conditions }.

    W[w] = #{v : wt(v) = w}, including v = 0 at W[0].  Exhaustive over all
    3^N ternary vectors (meet in the middle; no sampling anywhere).
    """
    rank, cols = _cols(rows, p, N)
    lo = list(range(0, N // 2))
    hi = list(range(N // 2, N))
    A = _half_table(cols, lo, p, rank)
    B = _half_table(cols, hi, p, rank)
    W = [0] * (N + 1)
    for syn, wa in A.items():
        nsyn = tuple((-x) % p for x in syn)
        wb = B.get(nsyn)
        if not wb:
            continue
        for i, ca in enumerate(wa):
            if not ca:
                continue
            for j, cb in enumerate(wb):
                if cb:
                    W[i + j] += ca * cb
    return W, rank


def ternary_kernel_vectors(N, p, rows, cap=2000000):
    """The actual nonzero ternary kernel vectors (for orbit analysis).

    Exhaustive; raises if the kernel exceeds `cap` (fail-closed, never
    silently truncates).
    """
    rank, cols = _cols(rows, p, N)
    lo = list(range(0, N // 2))
    hi = list(range(N // 2, N))

    def halves(idxs):
        out = {}
        stack = [((0,) * rank, ())]
        for i in idxs:
            c = cols[i]
            cm = tuple((-x) % p for x in c)
            nxt = []
            for syn, vec in stack:
                nxt.append((syn, vec + (0,)))
                nxt.append((tuple((a + b) % p for a, b in zip(syn, c)),
                            vec + (1,)))
                nxt.append((tuple((a + b) % p for a, b in zip(syn, cm)),
                            vec + (-1,)))
            stack = nxt
        for syn, vec in stack:
            out.setdefault(syn, []).append(vec)
        return out

    A, B = halves(lo), halves(hi)
    out = []
    for syn, va in A.items():
        nsyn = tuple((-x) % p for x in syn)
        vb = B.get(nsyn)
        if not vb:
            continue
        if len(out) + len(va) * len(vb) > cap + 1:
            raise MemoryError("kernel exceeds cap=%d" % cap)
        for a in va:
            for b in vb:
                v = a + b
                if any(v):
                    out.append(v)
    return out


def brute_weight_distribution(N, p, rows):
    """Independent code path: plain enumeration over 3^N (small N only)."""
    assert N <= 11, "brute force only for N <= 11"
    rank, cols = _cols(rows, p, N)
    W = [0] * (N + 1)
    v = [0] * N
    def rec(i, syn, wt):
        if i == N:
            if not any(syn):
                W[wt] += 1
            return
        c = cols[i]
        cm = tuple((-x) % p for x in c)
        rec(i + 1, syn, wt)
        rec(i + 1, tuple((a + b) % p for a, b in zip(syn, c)), wt + 1)
        rec(i + 1, tuple((a + b) % p for a, b in zip(syn, cm)), wt + 1)
    rec(0, (0,) * rank, 0)
    return W


# --------------------------------------------------------------------------
# symmetry / orbit structure  (LEMMA ROT and its registered break)
# --------------------------------------------------------------------------

def rot_neg(v):
    """negacyclic twisted rotation: (Rv)_0 = -v_{N-1}, (Rv)_j = v_{j-1}."""
    return (-v[-1],) + v[:-1]


def rot_cyc(v):
    """plain cyclic rotation: (Cv)_0 = v_{N-1}, (Cv)_j = v_{j-1}."""
    return (v[-1],) + v[:-1]


def orbit_report(vecs):
    """Which symmetries the kernel is closed under, and the orbit sizes."""
    S = set(vecs)
    closed_neg = all(tuple(-x for x in v) in S for v in S)
    closed_rn = all(rot_neg(v) in S for v in S)
    closed_rc = all(rot_cyc(v) in S for v in S)
    gens = []
    if closed_neg:
        gens.append(lambda v: tuple(-x for x in v))
    if closed_rn:
        gens.append(rot_neg)
    if closed_rc:
        gens.append(rot_cyc)
    seen, sizes = set(), []
    for v in S:
        if v in seen:
            continue
        orb, stack = {v}, [v]
        while stack:
            u = stack.pop()
            for g in gens:
                x = g(u)
                if x not in orb:
                    orb.add(x)
                    stack.append(x)
        seen |= orb
        sizes.append(len(orb))
    return {"closed_neg": closed_neg, "closed_rot_neg": closed_rn,
            "closed_rot_cyc": closed_rc, "orbits": len(sizes),
            "orbit_sizes": sorted(set(sizes))}


# --------------------------------------------------------------------------
# instance constructors
# --------------------------------------------------------------------------

def T_I3(n, p, w):
    return p_closure([s for s in range(1, w) if s % 2 == 1], n, p)


def T_I2(L, p):
    return p_closure([1], 2 * L, p)


def T_I1(N, p, R, a):
    return p_closure(list(range(a, a + R)), 2 * N, p)


def self_orth_predicate(N, p, T):
    """SELF-ORTH as registered: T u (-T) contains every odd residue mod 2N."""
    M = 2 * N
    U = set(T) | set((-s) % M for s in T)
    return all(s in U for s in range(1, M, 2))


def mass_and_scount(W, N):
    """Z = sum 2^{-wt} over the WHOLE kernel; Sct = sum_{v!=0} 2^{z(v)}.

    Returned exactly: (num, den) for Z = num/2^N, and the integer Sct.
    Registered identity D3:  Sct = 2^N (Z - 1).
    """
    num = sum(W[w] * (1 << (N - w)) for w in range(N + 1))
    sct = num - (1 << N)
    return (num, 1 << N), sct

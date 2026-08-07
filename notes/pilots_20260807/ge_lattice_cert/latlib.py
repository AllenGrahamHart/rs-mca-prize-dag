#!/usr/bin/env python3
"""Round-23 dim-64 lattice certification library.  STDLIB ONLY, EXACT.

REUSE NOTICE: the exact 2-adic tower norm comes from round-22's
notes/pilots_20260807/ge_floor_falsifier/gelib.py (coordinator-replayed).
The lattice Lambda_p and its basis are round-22's d4_cone.py construction
verbatim; what is new here is (a) an exact INTEGER LLL (Cohen 2.6.7 /
de Weger integral Gram-Schmidt) that scales past dimension 8, (b) a
scaled-INTEGER Fincke-Pohst enumerator with an explicit fail-closed
rounding lemma, and (c) checkpoint/resume so both fit the 5-minute
ramguard wall.

THE ROUNDING LEMMA (fail-closed, runtime-asserted).
  Let S = 2^SBITS.  We store
      q[i]   = floor( ||b*_i||^2 * S )                    (UNDER-estimate)
      m[k][j]= round( mu[k][j] * S )                      (|err| <= 1/2)
  and enumerate with the integer test
      sum_{j>=i} (x_j*S + C_j)^2 * q[j]  <=  (R2+1) * S^3,
  where C_j = sum_{k>j} m[k][j] x_k.
  With runtime assertions
      A1: q[i] >= 2^48                (so ||b*_i||^2 >= 2^-48 > 0)
      A2: |x_j| <= XMAX = 2^40        (checked at every visited node)
      A3: max_i ||b*_i||^2 <= 2^80
  the total deviation of the integer test from the exact real test is
      <= n * ( 2*R*max||b*_i||*(n*XMAX/(2S)) + (n*XMAX/(2S))^2*max||b*_i||^2 )
      <= 64 * ( 2*2^4*2^40*2^-83 + 2^-166*2^80 ) < 2^-32  <  1,
  for SBITS = 128, R <= 16.  Hence every w with exact ||w||^2 <= R2 IS
  visited (no false negatives), while some w with R2 < ||w||^2 <= R2+1 may
  also be visited (a harmless superset).  EVERY leaf is then re-checked in
  EXACT integer arithmetic, so there are no false positives either.
"""
import json
import os
import sys
import time
from math import isqrt

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
_R22 = os.path.normpath(os.path.join(HERE, '..', 'ge_floor_falsifier'))
if _R22 not in sys.path:
    sys.path.insert(0, _R22)
from gelib import tower_norm            # noqa: E402  (round-22, replayed)

SBITS = 128
S = 1 << SBITS
XMAX = 1 << 40
QMIN = 1 << 48
BMAX = 1 << 80


# ------------------------------------------------------------------ basics
def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def zeta_of_order(N, p):
    """Smallest g >= 2 whose ((p-1)/N)-th power has exact order N.  This is
    d4_cone.py's routine verbatim."""
    for g in range(2, p):
        c = pow(g, (p - 1) // N, p)
        if pow(c, N // 2, p) == p - 1:
            return c
    return None


def coeff_basis(h, p, cvec):
    """Basis of { w in Z^h : sum_j w_j cvec[j] = 0 mod p }, assuming
    cvec[0] = 1 (so the lattice has determinant exactly p).
    Rows: (p,0,...,0) and (-cvec[j] mod p, 0,..,1 at j,..,0)."""
    assert cvec[0] % p == 1 % p
    B = [[0] * h for _ in range(h)]
    B[0][0] = p
    for j in range(1, h):
        B[j][0] = (-cvec[j]) % p
        B[j][j] = 1
    return B


def kernel_basis(h, p, z):
    """Lambda_p = { w : w(zeta) = 0 mod p }, zeta = z of order 2h in F_p.
    Identical to d4_cone.py's construction."""
    return coeff_basis(h, p, [pow(z, j, p) for j in range(h)])


def boxcount(h, L):
    """#{w in {-2..2}^h : ||w||_1 <= L}, exact DP (d3_kernel.py's routine)."""
    dp = [0] * (L + 1)
    dp[0] = 1
    for _ in range(h):
        nd = [0] * (L + 1)
        for s in range(L + 1):
            if not dp[s]:
                continue
            v = dp[s]
            nd[s] += v
            if s + 1 <= L:
                nd[s + 1] += 2 * v
            if s + 2 <= L:
                nd[s + 2] += 2 * v
        dp = nd
    return sum(dp)


# ------------------------------------------------- integral Gram-Schmidt
def integral_gso(B):
    """d[0..n], lam[i][j] (j<i) with  ||b*_i||^2 = d[i+1]/d[i],
    mu[i][j] = lam[i][j]/d[j+1].  All exact integers (Bareiss recursion).
    d[n] = det(Gram) = det(B)^2."""
    n = len(B)
    d = [1] * (n + 1)
    lam = [[0] * n for _ in range(n)]
    for k in range(n):
        Bk = B[k]
        for j in range(k + 1):
            u = dot(Bk, B[j])
            lk = lam[k]
            lj = lam[j]
            for i in range(j):
                u = (d[i + 1] * u - lk[i] * lj[i]) // d[i]
            if j < k:
                lam[k][j] = u
            else:
                if u <= 0:
                    raise ValueError("rows not independent at k=%d" % k)
                d[k + 1] = u
    return d, lam


def nint(a, b):
    """round(a/b) for b > 0, ties away from zero."""
    if a >= 0:
        return (2 * a + b) // (2 * b)
    return -((-2 * a + b) // (2 * b))


# --------------------------------------------------------- integer LLL
def lll_step_loop(B, d, lam, k, num, den, deadline, swaps):
    """Cohen 2.6.7 with a full up-front GSO (kmax = n-1).  Returns
    (status, k, swaps): status 'DONE' or 'RUNNING'."""
    n = len(B)
    ctr = 0
    while k < n:
        # REDI(k, k-1)
        if 2 * abs(lam[k][k - 1]) > d[k]:
            q = nint(lam[k][k - 1], d[k])
            Bl = B[k - 1]
            B[k] = [B[k][t] - q * Bl[t] for t in range(n)]
            lam[k][k - 1] -= q * d[k]
            lk = lam[k]
            lm = lam[k - 1]
            for i in range(k - 1):
                lk[i] -= q * lm[i]
        if den * d[k + 1] * d[k - 1] < num * d[k] * d[k] - den * lam[k][k - 1] ** 2:
            # SWAPI(k)
            B[k], B[k - 1] = B[k - 1], B[k]
            for j in range(k - 1):
                lam[k][j], lam[k - 1][j] = lam[k - 1][j], lam[k][j]
            lmb = lam[k][k - 1]
            bb = (d[k + 1] * d[k - 1] + lmb * lmb) // d[k]
            for i in range(k + 1, n):
                t = lam[i][k]
                lam[i][k] = (lam[i][k - 1] * d[k + 1] - lmb * t) // d[k]
                lam[i][k - 1] = (bb * t + lmb * lam[i][k]) // d[k + 1]
            d[k] = bb
            swaps += 1
            k = max(1, k - 1)
        else:
            for l in range(k - 2, -1, -1):
                if 2 * abs(lam[k][l]) > d[l + 1]:
                    q = nint(lam[k][l], d[l + 1])
                    Bl = B[l]
                    B[k] = [B[k][t] - q * Bl[t] for t in range(n)]
                    lam[k][l] -= q * d[l + 1]
                    lk = lam[k]
                    lm = lam[l]
                    for i in range(l):
                        lk[i] -= q * lm[i]
            k += 1
        ctr += 1
        if (ctr & 255) == 0 and time.time() > deadline:
            return 'RUNNING', k, swaps
    return 'DONE', k, swaps


def atomic_write(path, obj):
    # per-process tmp name: two shards starting the SAME fresh cell would
    # otherwise collide on one .tmp and one of them would die on os.replace.
    tmp = "%s.%d.tmp" % (path, os.getpid())
    with open(tmp, "w") as f:
        json.dump(obj, f)
    os.replace(tmp, path)


def lll_resumable(state_path, B0, phash, deltas, deadline, log=print):
    """Run integer LLL with an escalating delta ladder, checkpointing to
    state_path.  deltas = [(num,den), ...].  Returns (status, info)."""
    if os.path.exists(state_path):
        st = json.load(open(state_path))
        if st["phash"] != phash:
            raise SystemExit("CHECKPOINT PROBLEM MISMATCH -- refusing to resume")
        B = st["B"]
        k = st["k"]
        swaps = st["swaps"]
        stage = st["stage"]
        secs = st["secs"]
    else:
        B = [list(r) for r in B0]
        k, swaps, stage, secs = 1, 0, 0, 0.0
    t0 = time.time()
    while stage < len(deltas):
        num, den = deltas[stage]
        d, lam = integral_gso(B)
        status, k, swaps = lll_step_loop(B, d, lam, k, num, den, deadline, swaps)
        secs += time.time() - t0
        t0 = time.time()
        if status == 'RUNNING':
            atomic_write(state_path, {"phash": phash, "B": B, "k": k,
                                      "swaps": swaps, "stage": stage,
                                      "secs": secs})
            return 'RUNNING', {"stage": stage, "k": k, "swaps": swaps,
                               "secs": secs}
        log("   LLL stage %d (delta=%d/%d) DONE: swaps=%d cum_secs=%.1f"
            % (stage, num, den, swaps, secs))
        stage += 1
        k = 1
        atomic_write(state_path, {"phash": phash, "B": B, "k": k,
                                  "swaps": swaps, "stage": stage,
                                  "secs": secs})
    return 'DONE', {"B": B, "swaps": swaps, "secs": secs}


# ------------------------------------------------ scaled-integer Fincke-Pohst
def enum_setup(B, R2):
    """Returns (q, m, LIMIT, d, lam, diag) for the scaled integer FP."""
    n = len(B)
    d, lam = integral_gso(B)
    q = [(d[i + 1] * S) // d[i] for i in range(n)]
    for i in range(n):
        if q[i] < QMIN:
            raise SystemExit("ASSERT A1 FAILED at i=%d (q=%d)" % (i, q[i]))
        if d[i + 1] * BMAX < d[i]:
            pass
        if d[i + 1] > BMAX * d[i]:
            raise SystemExit("ASSERT A3 FAILED at i=%d" % i)
    m = [[0] * n for _ in range(n)]
    for k in range(n):
        for j in range(k):
            m[k][j] = nint(lam[k][j] * S, d[j + 1])
    LIMIT = (R2 + 1) * S * S * S
    return q, m, LIMIT, d, lam


def _mcols(m, n):
    """mcol[j][k] = mu[k][j] scaled -- column j as a flat list over k, so the
    centre  C_j = sum_{k>j} m[k][j] x_k  is one C-level map/sum."""
    return [[m[k][j] for k in range(n)] for j in range(n)]


def enum_resumable(state_path, B, R2, L, phash, deadline, boxinf=2, log=print,
                   report_every=4_000_000, shard=0, nshard=1, sdepth=4):
    """Complete Fincke-Pohst enumeration of { w != 0 in the lattice spanned by
    B : ||w||_inf <= boxinf, ||w||_1 <= L }, with checkpoint/resume.

    SHARDING (exact, not heuristic).  Let flev = n-1-sdepth.  The DFS is a
    tree; every node at level flev roots a subtree that is disjoint from
    every other such subtree, and the union of those subtrees together with
    the prefix (levels > flev) is the WHOLE tree.  Shard s of nshard owns
    the frontier nodes whose ordinal is = s mod nshard.  Node accounting:
    prefix nodes (levels > flev) are counted only in shard 0, frontier and
    below only in the owning shard, so sum_s FPNODES_s is exactly the
    single-process FPNODES.  Union_s FPFOUND_s is exactly FPFOUND.
    Returns (status, dict)."""
    n = len(B)
    # flev >= 1 is REQUIRED: level 0 is processed by a batched interval
    # intersection inside the level-1 step, so it cannot itself be a
    # frontier (that would double-count the batch in every shard).
    flev = max(1, n - 1 - sdepth) if nshard > 1 else -1
    q, m, LIMIT, d, lam = enum_setup(B, R2)
    mcol = _mcols(m, n)
    from operator import mul
    if os.path.exists(state_path):
        st = json.load(open(state_path))
        if st["phash"] != phash:
            raise SystemExit("CHECKPOINT PROBLEM MISMATCH -- refusing to resume")
        x = st["x"]
        lo = st["lo"]
        hi = st["hi"]
        lev = st["lev"]
        nodes = st["nodes"]
        found = [tuple(w) for w in st["found"]]
        secs = st["secs"]
        fcnt = st.get("fcnt", 0)
        if lev >= n:
            return 'DONE', {"nodes": nodes, "found": found, "secs": secs,
                            "fcnt": fcnt}
        # rebuild centres / partial sums from x for levels >= lev
        c = [0] * n
        psum = [0] * (n + 1)
        for i in range(n - 1, lev - 1, -1):
            cc = 0
            for kk in range(i + 1, n):
                if x[kk]:
                    cc += m[kk][i] * x[kk]
            c[i] = cc
            psum[i] = psum[i + 1] + (x[i] * S + cc) ** 2 * q[i]
        # psum[lev] currently uses the CURRENT x[lev]; the loop re-adds it
        # after incrementing, so recompute only levels > lev here.
        c_lev = 0
        for kk in range(lev + 1, n):
            if x[kk]:
                c_lev += m[kk][lev] * x[kk]
        c[lev] = c_lev
    else:
        x = [0] * n
        lo = [0] * n
        hi = [0] * n
        c = [0] * n
        psum = [0] * (n + 1)
        nodes = 0
        found = []
        secs = 0.0
        fcnt = 0
        lev = n - 1
        tt = isqrt(LIMIT // q[lev])
        lo[lev] = -(tt // S)
        hi[lev] = tt // S
        x[lev] = lo[lev] - 1
    t0 = time.time()
    ctr = 0
    nxt = report_every
    while True:
        x[lev] += 1
        if x[lev] > hi[lev]:
            lev += 1
            if lev >= n:
                secs += time.time() - t0
                atomic_write(state_path, {"phash": phash, "x": x, "lo": lo,
                                          "hi": hi, "lev": lev, "nodes": nodes,
                                          "found": [list(w) for w in found],
                                          "secs": secs, "fcnt": fcnt})
                return 'DONE', {"nodes": nodes, "found": found, "secs": secs,
                                "fcnt": fcnt}
            continue
        if x[lev] > XMAX or x[lev] < -XMAX:
            raise SystemExit("ASSERT A2 FAILED (|x| > 2^40) at lev=%d" % lev)
        ps = psum[lev + 1] + (x[lev] * S + c[lev]) ** 2 * q[lev]
        if lev == flev:
            fcnt += 1
            if (fcnt - 1) % nshard != shard:
                continue
            nodes += 1
        elif lev > flev:
            if shard == 0:
                nodes += 1
        else:
            nodes += 1
        psum[lev] = ps
        if lev > 1:
            nl = lev - 1
            cc = sum(map(mul, mcol[nl][lev:], x[lev:]))
            c[nl] = cc
            tt = isqrt((LIMIT - ps) // q[nl])
            lo[nl] = -((cc + tt) // S)
            hi[nl] = (tt - cc) // S
            x[nl] = lo[nl] - 1
            lev = nl
        else:
            # lev == 1: batch level 0 (box interval intersection, exact)
            cc = sum(map(mul, mcol[0][1:], x[1:]))
            tt = isqrt((LIMIT - ps) // q[0])
            l0 = -((cc + tt) // S)
            h0 = (tt - cc) // S
            if h0 >= l0:
                nodes += h0 - l0 + 1
                wr = [0] * n
                for kk in range(1, n):
                    xk = x[kk]
                    if xk:
                        Bk = B[kk]
                        for u in range(n):
                            wr[u] += xk * Bk[u]
                B0 = B[0]
                a, b = l0, h0
                for u in range(n):
                    g = B0[u]
                    r = wr[u]
                    if g == 0:
                        if r > boxinf or r < -boxinf:
                            a, b = 1, 0
                            break
                    elif g > 0:
                        a = max(a, -((boxinf + r) // g))
                        b = min(b, (boxinf - r) // g)
                    else:
                        a = max(a, -((boxinf - r) // (-g)))
                        b = min(b, (boxinf + r) // (-g))
                    if a > b:
                        break
                for x0 in range(a, b + 1):
                    w = [wr[u] + x0 * B0[u] for u in range(n)]
                    if not any(w):
                        continue
                    if max(abs(t) for t in w) <= boxinf and \
                            sum(abs(t) for t in w) <= L:
                        wt = tuple(w)
                        if wt not in found:
                            found.append(wt)
        ctr += 1
        if (ctr & 8191) == 0:
            if time.time() > deadline:
                secs += time.time() - t0
                atomic_write(state_path, {"phash": phash, "x": x, "lo": lo,
                                          "hi": hi, "lev": lev, "nodes": nodes,
                                          "found": [list(w) for w in found],
                                          "secs": secs, "fcnt": fcnt})
                return 'RUNNING', {"nodes": nodes, "found": found,
                                   "secs": secs, "lev": lev, "fcnt": fcnt}
            if nodes >= nxt:
                log("      ... nodes=%d lev=%d elapsed=%.1fs"
                    % (nodes, lev, time.time() - t0))
                nxt += report_every


# ------------------------------------------------------------- brute force
def brute_box(h, p, cvec, L, boxinf=2):
    """Exhaustive sweep of {-boxinf..boxinf}^h -- the ground truth at small h."""
    import itertools
    out = []
    rng = list(range(-boxinf, boxinf + 1))
    for w in itertools.product(rng, repeat=h):
        if not any(w):
            continue
        if sum(abs(t) for t in w) > L:
            continue
        s = 0
        for j in range(h):
            if w[j]:
                s += w[j] * cvec[j]
        if s % p == 0:
            out.append(tuple(w))
    return out

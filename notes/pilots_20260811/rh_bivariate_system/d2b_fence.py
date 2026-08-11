"""D2(b) -- the wave-57 incidence fence
(background/nodes/rate_half_type2_fr_incidence_only_route_fence), m = 64,
a = 7m-1 = 447, T = rho+2 = 257, N = 16m = 1024, AT FULL SCALE, plus the same
quartic-difference-family construction scaled to m = 3 (q_0 = 13) and
m = 4 (q_0 = 17).

The fence is a SET SYSTEM.  The bivariate realizability system needs, in
addition, an EMBEDDING  W -> mu_N < F_q  and  Z -> F_q.  That is a genuine
extra input: the incidence data alone does NOT determine the system.  So a
full-rank result here kills the tested embeddings, not the fence; see D4.

Streaming row generation (the full matrix is 16962 x 894 and must never be
materialised).
"""

import hashlib
import json
import random
import sys

sys.path.insert(0, "notes/pilots_20260811/rh_bivariate_system")
from biv_core import PackedRank, is_prime, mu_N, poly_from_roots, primes_one_mod

out = []
P = out.append
P("=" * 78)
P("D2(b) -- WAVE-57 INCIDENCE FENCE: BIVARIATE REALIZABILITY SYSTEM")
P("=" * 78)


# --------------------------------------------------- the fence at general m
def fence_blocks(q0):
    """S_gamma for gamma in F_q0, over D = {0,1,2,3} x F_q0^*, m = (q0-1)/4."""
    m = (q0 - 1) // 4
    # generator of F_q0^*
    def order(g):
        k, cur = 1, g
        while cur != 1:
            cur = cur * g % q0
            k += 1
        return k
    gen = next(g for g in range(2, q0) if order(g) == q0 - 1)
    H = {pow(gen, 4 * j, q0) for j in range(m)}
    cosets = [{pow(gen, i, q0) * v % q0 for v in H} for i in range(4)]
    blocks = {}
    for gamma in range(q0):
        b = {(i, (gamma + v) % q0)
             for i, cs in enumerate(cosets) for v in cs if (gamma + v) % q0}
        if gamma == 0:
            b.discard((0, 1))
        blocks[gamma] = b
    domain = {(i, x) for i in range(4) for x in range(1, q0)}
    return m, gen, domain, blocks


def stream_rank(m, q, Wvals, Amap, extra, cap_rows=None, seed=1):
    """rank of S2 with rows generated lazily (never materialise the matrix)."""
    extra = extra or {}
    cols, polys = [], {}
    for x in Wvals:
        pi = poly_from_roots(Amap[x], q)
        for t in range(extra.get(x, 0) + 2):
            polys[(x, t)] = [0] * t + pi
            cols.append((x, t))
    nc = len(cols)
    pw = {}
    for x in Wvals:
        row = [1] * (4 * m + 1)
        for i in range(1, 4 * m + 1):
            row[i] = row[i - 1] * x % q
        pw[x] = row
    idx = [(i, j) for i in range(4 * m + 1) for j in range(m + 2)]
    random.Random(seed).shuffle(idx)
    if cap_rows:
        idx = idx[:cap_rows]
    pr = PackedRank(nc, q)
    used = 0
    for (i, j) in idx:
        if pr.rank == nc:
            break
        vec = [0] * nc
        nz = False
        for ci, (x, t) in enumerate(cols):
            p = polys[(x, t)]
            if j < len(p):
                v = p[j]
                if v:
                    vec[ci] = pw[x][i] * v % q
                    nz = True
        if nz:
            used += 1
            pr.add_row(vec)
    return pr.rank, nc, used, len(idx)


# ----------------------------------------------------------- m = 64, the node
P("")
P("[A] m = 64 : rebuild the node's own system and W (my code; banked-number replay)")
payload = json.loads(
    open("experiments/prize_resolution/rh_type2_fr_incidence_m64_result.json").read())
q0 = payload["field_order"]
m, gen, domain, blocks = fence_blocks(q0)
raw = bytes.fromhex(payload["W_bitset_hex_little_endian"])
sha = hashlib.sha256(raw).hexdigest()
mask = int.from_bytes(raw, "little")
Wset = {(k // (q0 - 1), k % (q0 - 1) + 1) for k in range(16 * m) if (mask >> k) & 1}
a = len(Wset)
dx = {p: sum(1 for b in blocks.values() if p in b) for p in domain}
X = {g: len(b & Wset) for g, b in blocks.items()}
spend = {g: len(b - Wset) for g, b in blocks.items()}
P("    q_0 = %d, m = %d, generator = %d, |D| = %d = 16m : %s"
  % (q0, m, gen, len(domain), len(domain) == 16 * m))
P("    W sha256 matches node                : %s" % (sha == payload["W_sha256"]))
P("    T = %d = rho+2 = %d ; all |S| = rho = %d : %s"
  % (len(blocks), 4 * m + 1, 4 * m - 1, {len(b) for b in blocks.values()} == {4 * m - 1}))
P("    sum_x (m - d_x) = %d  (=1+O)          : %s"
  % (sum(m - dx[p] for p in domain), sum(m - dx[p] for p in domain) == 1))
P("    |W| = %d = 7m-1 = %d                 : %s" % (a, 7 * m - 1, a == 7 * m - 1))
P("    max_g |S_g ^ W| = %d = 3m-3 = %d      : %s"
  % (max(X.values()), 3 * m - 3, max(X.values()) == 3 * m - 3))
P("    min_g |S_g \\ W| = %d = m+2 = %d       : %s"
  % (min(spend.values()), m + 2, min(spend.values()) == m + 2))
unsatW = [p for p in Wset if dx[p] < m]
P("    unsaturated domain point (0,1) has d = %d ; is it inside W? %s"
  % (dx[(0, 1)], (0, 1) in Wset))
P("    T_1 (slopes with S_g inside W)       : %d   [max X = %d < rho = %d]"
  % (sum(1 for g in blocks if blocks[g] <= Wset), max(X.values()), 4 * m - 1))
P("    incidences inside W: sum_x d_x|_W = %d ;  sum_g X_g = %d"
  % (sum(dx[p] for p in Wset), sum(X.values())))

P("")
P("[B] m = 64 : rank of the bivariate system at RANDOM embeddings")
P("    unknowns 2a = %d (+1 per unsaturated W-point) ; equations (m+2)(4m+1) = %d"
  % (2 * a, (m + 2) * (4 * m + 1)))
Wl = sorted(Wset)
for q in [p for p in primes_one_mod(16 * m, count=2, limit=200000)][:2]:
    D = mu_N(q, 16 * m)
    for trial in range(2):
        rnd = random.Random(9000 + q + trial)
        Wv = rnd.sample(D, a)
        slopes = rnd.sample(range(1, q), 4 * m + 1)
        emb = dict(zip(Wl, Wv))
        sl = {g: slopes[k] for k, g in enumerate(sorted(blocks))}
        Amap = {emb[p]: [sl[g] for g in blocks if p in blocks[g]] for p in Wl}
        extra = {emb[p]: m - dx[p] for p in unsatW}
        rk, nc, used, tot = stream_rank(m, q, Wv, Amap, extra, seed=77 + trial)
        P("    q=%-6d trial %d : unknowns %d, rank %d, NULLITY %d   (rows consumed %d of %d)"
          % (q, trial, nc, rk, nc - rk, used, tot))

# ------------------------------------------------- scaled fences m = 3, 4
P("")
P("[C] the SAME construction scaled: q_0 = 4m+1 prime, m = 3 (q_0=13), m = 4 (q_0=17)")
for q0s in (13, 17):
    ms, gens, doms, blks = fence_blocks(q0s)
    a_s = 7 * ms - 1
    dxs = {p: sum(1 for b in blks.values() if p in b) for p in doms}
    ok_sizes = {len(b) for b in blks.values()} == {4 * ms - 1}
    defi = sum(ms - dxs[p] for p in doms)
    pu = min(len(blks[g] | blks[h]) for g in blks for h in blks if g < h)
    P("")
    P("    q_0=%d m=%d N=%d rho=%d T=%d a=%d : blocks size ok %s, deficit %d, min pair union %d (a=%d)"
      % (q0s, ms, 16 * ms, 4 * ms - 1, len(blks), a_s, ok_sizes, defi, pu, a_s))
    # search a W of size a with min spend >= m+2 maximising max X
    best = None
    rnd = random.Random(31337 + q0s)
    dl = sorted(doms)
    for _ in range(4000):
        Wc = set(rnd.sample(dl, a_s))
        sp = min(len(b - Wc) for b in blks.values())
        if sp < ms + 2:
            continue
        mx = max(len(b & Wc) for b in blks.values())
        if best is None or mx > best[0]:
            best = (mx, Wc, sp)
    mx, Wc, sp = best
    P("    searched W: |W|=%d, min spend %d (>= m+2 = %d), max X = %d (cap 3m-3 = %d)"
      % (len(Wc), sp, ms + 2, mx, 3 * ms - 3))
    Wls = sorted(Wc)
    unsat_s = [p for p in Wc if dxs[p] < ms]
    for q in primes_one_mod(16 * ms, count=2, limit=6000)[:2]:
        D = mu_N(q, 16 * ms)
        nulls = []
        for trial in range(20):
            rnd2 = random.Random(555 + q + 17 * trial)
            Wv = rnd2.sample(D, a_s)
            slopes = rnd2.sample(range(1, q), 4 * ms + 1)
            emb = dict(zip(Wls, Wv))
            sl = {g: slopes[k] for k, g in enumerate(sorted(blks))}
            Amap = {emb[p]: [sl[g] for g in blks if p in blks[g]] for p in Wls}
            extra = {emb[p]: ms - dxs[p] for p in unsat_s}
            rk, nc, used, tot = stream_rank(ms, q, Wv, Amap, extra, seed=3 + trial)
            nulls.append(nc - rk)
        hist = {}
        for n in nulls:
            hist[n] = hist.get(n, 0) + 1
        P("    q=%-5d unknowns %d, equations %d : nullity histogram over 20 embeddings %s"
          % (q, nc, (ms + 2) * (4 * ms + 1), dict(sorted(hist.items()))))

P("")
P("=" * 78)
print("\n".join(out))
with open("notes/pilots_20260811/rh_bivariate_system/d2b_fence_results.txt", "w") as f:
    f.write("\n".join(out) + "\n")

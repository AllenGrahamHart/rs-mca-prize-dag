#!/usr/bin/env python3
"""D1 - anatomy of the wave-57 (FR) incidence fence, and the canonical-W test.

Written from scratch for pilot rh_fr_algebraic (round 32).  Rebuilds the
quartic-difference-family block system of
background/nodes/rate_half_type2_fr_incidence_only_route_fence/proof.md
independently (bitmask representation, my own coset code), decodes the
banked W mask from the result artifact, replays the fence's six numbers,
and then runs the D1 question:

    the fence's W is an ARBITRARY a-set.  The (C2)/(AO1) machinery is
    entitled to choose W = S_g u S_h (apolar_origin/PREREG.md:163
    "W = a joint support (e.g. S_gamma u S_gamma')").  What is
    max_gamma |S_gamma ^ (S_g u S_h)| on the fence's OWN blocks?

Stdlib only.  Run under tools/ramguard local.
"""

import hashlib
import json
import sys
from itertools import combinations

RESULT = "experiments/prize_resolution/rh_type2_fr_incidence_m64_result.json"


def popcount(x):
    return x.bit_count()


def build_blocks(m, q, g):
    """Blocks S_gamma as 1024-bit masks; index of (i,x) is i*(q-1)+(x-1)."""
    sub = {pow(g, 4 * j, q) for j in range(m)}
    assert len(sub) == m
    cosets = [sorted({(pow(g, i, q) * u) % q for u in sub}) for i in range(4)]
    assert sum(len(c) for c in cosets) == q - 1
    assert set().union(*[set(c) for c in cosets]) == set(range(1, q))
    idx = lambda i, x: i * (q - 1) + (x - 1)
    blocks = {}
    for gamma in range(q):
        mask = 0
        for i, coset in enumerate(cosets):
            for u in coset:
                y = (gamma + u) % q
                if y:
                    mask |= 1 << idx(i, y)
        if gamma == 0:
            mask &= ~(1 << idx(0, 1))
        blocks[gamma] = mask
    return blocks


def main():
    payload = json.loads(open(RESULT).read())
    m, q, g = payload["m"], payload["field_order"], payload["generator"]
    N, rho, T, a = payload["N"], payload["rho"], payload["T"], payload["a"]
    R = 8 * m
    out = []
    P = out.append
    P("=== D1  fence anatomy (rh_fr_algebraic, round 32) ===")
    P(f"m={m} q={q} N={N} rho={rho} T={T} a={a} R={R} R+1={R+1}")
    P(f"7m-1={7*m-1}  2m={2*m}  3m-3={3*m-3}  2(m-1)={2*(m-1)}  (8m-8)/3={(8*m-8)/3:.4f}")

    blocks = build_blocks(m, q, g)
    P(f"[rebuild] block count {len(blocks)}; sizes set {sorted({popcount(b) for b in blocks.values()})}")

    raw = bytes.fromhex(payload["W_bitset_hex_little_endian"])
    assert hashlib.sha256(raw).hexdigest() == payload["W_sha256"], "mask digest"
    W = int.from_bytes(raw, "little")
    P(f"[mask] sha256 OK, |W|={popcount(W)} (claimed {a})")

    full = (1 << N) - 1
    deg = [0] * N
    for b in blocks.values():
        bb = b
        while bb:
            low = bb & -bb
            deg[low.bit_length() - 1] += 1
            bb ^= low
    P(f"[deg] sum_x (m-d_x) = {sum(m - d for d in deg)}  (claim 1); max d_x={max(deg)} min d_x={min(deg)}")

    inter = [[0] * T for _ in range(T)]
    maxpair_int = 0
    minunion = 10 ** 9
    minunion_pairs = []
    for i, j in combinations(range(T), 2):
        c = popcount(blocks[i] & blocks[j])
        inter[i][j] = inter[j][i] = c
        if c > maxpair_int:
            maxpair_int = c
        u = popcount(blocks[i]) + popcount(blocks[j]) - c
        if u < minunion:
            minunion, minunion_pairs = u, [(i, j)]
        elif u == minunion:
            minunion_pairs.append((i, j))
    P(f"[pairs] max |S ^ S'| = {maxpair_int} (m-1={m-1});  min |S u S'| = {minunion} (a={a});"
      f"  #minimising pairs = {len(minunion_pairs)}")

    xs = {gamma: popcount(b & W) for gamma, b in blocks.items()}
    ps = {gamma: popcount(b & ~W & full) for gamma, b in blocks.items()}
    P(f"[fenceW] max |S ^ W| = {max(xs.values())} at {sorted(k for k,v in xs.items() if v==max(xs.values()))};"
      f" min |S \\ W| = {min(ps.values())};  mean |S ^ W| = {sum(xs.values())/T:.4f}")
    P(f"[fenceW] blocks CONTAINED in W (type-1 count for the fence's W): "
      f"{sum(1 for b in blocks.values() if b & ~W & full == 0)}")
    P(f"[fenceW] is W equal to some pair union?  "
      f"{any(blocks[i] | blocks[j] == W for i, j in combinations(range(T), 2))}")
    P(f"[fenceW] sum_gamma |S ^ W| = {sum(xs.values())} ; m*a - def = {m*a} - def")

    # ---- D1 CORE: the canonical joint supports W* = S_g u S_h -------------
    worst_min = 0
    worst_min_at = None
    for (i, j) in minunion_pairs:
        u = blocks[i] | blocks[j]
        mx = max(popcount(blocks[k] & u) for k in range(T) if k not in (i, j))
        if mx > worst_min:
            worst_min, worst_min_at = mx, (i, j)
    P(f"[canonW-min] over the {len(minunion_pairs)} MINIMISING pairs (|W*|={minunion}): "
      f"max_gamma |S_gamma ^ W*| = {worst_min} at pair {worst_min_at}   "
      f"[2m={2*m}, 2(m-1)={2*(m-1)}, fence's 3m-3={3*m-3}]")

    # exhaustive over ALL pairs, using the exact union mask
    worst_all = 0
    worst_all_at = None
    worst_union = None
    for i, j in combinations(range(T), 2):
        u = blocks[i] | blocks[j]
        mx = 0
        for k in range(T):
            if k == i or k == j:
                continue
            c = popcount(blocks[k] & u)
            if c > mx:
                mx = c
        if mx > worst_all:
            worst_all, worst_all_at, worst_union = mx, (i, j), popcount(u)
    P(f"[canonW-all] over ALL {T*(T-1)//2} pair unions: max_gamma |S_gamma ^ (S_g u S_h)| = "
      f"{worst_all} at pair {worst_all_at} (|W*|={worst_union})   [2m={2*m}]")
    P(f"[canonW-all] VERDICT: fence's 3m-3={3*m-3} occurs at NO pair-union W; "
      f"the sup over canonical W is {worst_all} <= 2m={2*m}: {worst_all <= 2*m}")

    # ---- (C2) fibre-consistency of the fence's own W ----------------------
    slack = {gamma: ps[gamma] - (R + 1 - a) for gamma in blocks}
    P(f"[C2] n_gamma <= |S\\W| - (R+1-a): min slack {min(slack.values())}, "
      f"max slack {max(slack.values())}, sum slack {sum(slack.values())}")
    P(f"[C2] sum_gamma |S \\ W| = {sum(ps.values())} ; (N-a)m = {(N-a)*m}")
    open("notes/pilots_20260810/rh_fr_algebraic/d1_fence_results.txt", "w").write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()

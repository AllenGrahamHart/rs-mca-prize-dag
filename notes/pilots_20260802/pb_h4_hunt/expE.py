#!/usr/bin/env python3
"""EXPERIMENT E -- the ONE spread block geometry the dichotomy leaves open.

THEOREM (block dichotomy, proved in the report).  If the planted family is
S_J = G u (union of blocks B_j, j in J) over a-subsets J of a pool of b>=a+1
disjoint blocks and all S_J are witnesses of one pencil at >=2 slopes, then
  (i)  the block moment vectors beta_j = (p_1(B_j),...,p_h(B_j)) satisfy
       beta_j = beta_1 + c_j d for one direction d != 0;
  (ii) the family is SPREAD iff every block has size m >= h+1;
  (iii) for subgroup-coset blocks beta_j = m*lam_j*e_m when m<=h and
       beta_j = 0 when m>h, so (ii) and (i) cannot hold together.
The residue is: NON-coset blocks of size m >= h+1 with collinear moment
vectors.  There is no identity available, so this is a pure incidence
question; here it is measured exactly, and its q-dependence quantified (F3).

Run:  tools/ramguard local -- python3 expE.py
"""
from __future__ import annotations

import json
import math
import os
import sys
from itertools import combinations

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np

import core

HERE = os.path.dirname(os.path.abspath(__file__))

# n, q, h, m (block size, must be >= h+1 for spread), K, g, a
CASES = [
    dict(n=24, q=73, h=3, m=4, K=8, g=3, a=2),
    dict(n=24, q=241, h=3, m=4, K=8, g=3, a=2),
    dict(n=24, q=1201, h=3, m=4, K=8, g=3, a=2),
    dict(n=20, q=101, h=2, m=3, K=6, g=2, a=2),
    dict(n=20, q=1181, h=2, m=3, K=6, g=2, a=2),
]


def run(cfg):
    n, q, h, m, K = cfg["n"], cfg["q"], cfg["h"], cfg["m"], cfg["K"]
    D = core.domain(q, n)
    blocks = list(combinations(range(n), m))
    P = np.array([core.moment_vector([D[i] for i in B], h, q)
                  for B in blocks], dtype=np.int64)
    NB = len(blocks)
    INV = np.zeros(q, dtype=np.int64)
    for x in range(1, q):
        INV[x] = pow(x, q - 2, q)
    pw = np.array([q ** j for j in range(h)], dtype=np.int64)

    best = (0, None, None)          # (#blocks on line, i, code)
    for i in range(NB):
        d = (P - P[i]) % q
        nz = np.any(d != 0, axis=1)
        dd = d[nz]
        if dd.size == 0:
            continue
        first = np.argmax(dd != 0, axis=1)
        inv = INV[dd[np.arange(dd.shape[0]), first]]
        dn = (dd * inv[:, None]) % q
        code = dn @ pw
        cs = np.sort(code)
        starts = np.concatenate(([0], np.flatnonzero(np.diff(cs)) + 1))
        sizes = np.diff(np.concatenate((starts, [cs.size])))
        j = int(np.argmax(sizes))
        tot = int(sizes[j]) + 1
        if tot > best[0]:
            best = (tot, i, int(cs[starts[j]]))

    tot, bi, bcode = best
    dv = []
    c = bcode
    for _ in range(h):
        dv.append(c % q)
        c //= q
    on = [blocks[bi]]
    for j in range(NB):
        if j == bi:
            continue
        d = tuple((int(P[j][t]) - int(P[bi][t])) % q for t in range(h))
        if not any(d):
            on.append(blocks[j])
            continue
        f = next(t for t in range(h) if d[t])
        iv = pow(d[f], q - 2, q)
        if tuple(x * iv % q for x in d) == tuple(dv):
            on.append(blocks[j])
    assert len(on) == tot
    # maximum set of pairwise DISJOINT blocks on that line (greedy + exact
    # for small counts) and the number of DISTINCT c_j they realise
    masks = [core.mask_of(B) for B in on]
    chosen = []
    for i, mk in enumerate(masks):
        if all(mk & masks[j] == 0 for j in chosen):
            chosen.append(i)
    b_disj = len(chosen)
    f = next(t for t in range(h) if dv[t])
    cvals = {(int(P[blocks.index(on[i])][f]) - int(P[bi][f])) % q
             for i in chosen}
    a = cfg["a"]
    fam = math.comb(b_disj, a) if b_disj >= a else 0
    exp_on_line = len(blocks) / q ** (h - 1)
    res = dict(cfg=cfg, blocks=NB, max_blocks_on_a_line=tot,
               expected_blocks_per_line=exp_on_line,
               max_disjoint_on_that_line=b_disj,
               distinct_slope_shifts=len(cvals),
               spread_block_family_size=fam,
               need_b_at_least=a + 1,
               feasible=b_disj >= a + 1,
               budget_8n3=8 * n ** 3)
    print(f"  n={n} q={q} h={h} m={m} (>=h+1) | {NB} blocks, mean/line="
          f"{exp_on_line:.3g} | richest line carries {tot} blocks, "
          f"{b_disj} of them DISJOINT -> family C({b_disj},{a})={fam} "
          f"(need b>={a+1}: {b_disj >= a+1})")
    return res


if __name__ == "__main__":
    out = [run(c) for c in CASES]
    p = os.path.join(HERE, "EXPE.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print(f"-> {p}")

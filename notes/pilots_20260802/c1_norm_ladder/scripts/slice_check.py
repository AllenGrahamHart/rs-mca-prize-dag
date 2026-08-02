#!/usr/bin/env python3
"""Verify the d_0 = +1 slice reduction exhaustively at N = 4 and N = 8.

Checks, for every weight w:
  (a) max over the slice  ==  max over ALL ternary f of weight w
  (b) the SET of norms attained on the slice == the set attained globally
  (c) every U-orbit of a nonzero ternary vector has size exactly 2N (freeness)
"""

from __future__ import annotations

import json
from itertools import combinations, product

from norm_core import compose, group_U, norm_descent_py


def apply(g, d):
    perm, sign = g
    out = [0] * len(d)
    for i, c in enumerate(d):
        out[perm[i]] = sign[i] * c
    return out


def main() -> None:
    rep = []
    for N in (4, 8):
        U = group_U(N)
        for w in range(1, N + 1):
            glob = {}
            sl = {}
            for pos in combinations(range(N), w):
                for signs in product((1, -1), repeat=w):
                    d = [0] * N
                    for p, s in zip(pos, signs):
                        d[p] = s
                    v = norm_descent_py(d)
                    glob[v] = glob.get(v, 0) + 1
                    if d[0] == 1:
                        sl[v] = sl.get(v, 0) + 1
            rep.append({
                "N": N, "w": w,
                "max_global": str(max(glob)), "max_slice": str(max(sl)),
                "max_equal": max(glob) == max(sl),
                "value_sets_equal": set(glob) == set(sl),
                "n_global": sum(glob.values()), "n_slice": sum(sl.values()),
                "slice_size_formula": (1 if w == 1 else
                                       len(list(combinations(range(1, N), w - 1))) * (1 << (w - 1))),
            })
            assert max(glob) == max(sl) and set(glob) == set(sl)
        # freeness of U on nonzero ternary vectors
        bad = 0
        for d in product((-1, 0, 1), repeat=N):
            if not any(d):
                continue
            orb = {tuple(apply(g, list(d))) for g in U}
            if len(orb) != 2 * N:
                bad += 1
        rep.append({"N": N, "U_action_free_violations": bad, "|U|": len(U)})
        assert bad == 0
    print(json.dumps(rep, indent=1))


if __name__ == "__main__":
    main()

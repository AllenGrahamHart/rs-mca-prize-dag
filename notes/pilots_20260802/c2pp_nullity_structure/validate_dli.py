#!/usr/bin/env python3
"""C2'' pilot -- validation of the DLI tower reconstruction (Model B).

V1  block decomposition is EXACT: x is t-null  <=>  every block constraint
    holds (brute force, n = 16).
V2  the reconstruction reproduces the banked exhaustive mu_32 censuses
    (coset, noncoset) of `b2b_balance_concentration_scan` / the archived
    level-2 falfisier's SCAN table, at all 12 rows.
V3  the junction-0 count equals the archived skewcount(G).
V4  RANK LAW: rank{v_i : i in S} = min(L_j, |S|) -- exhaustive over supports.
"""

from __future__ import annotations

import json
import random
from pathlib import Path

from dli_model import (blocks, block_matrix, count_null, get_zeta,
                       junction_domain_and_count, levels_of, local_rank)
from nullity import rref_rank

HERE = Path(__file__).resolve().parent
ROWS = []

SCAN = {
    (2, 97): (255, 455488), (2, 193): (255, 116256), (2, 577): (255, 14240),
    (2, 8353): (255, 320), (2, 16417): (255, 288), (2, 32801): (255, 0),
    (2, 65537): (255, 0),
    (3, 97): (255, 6336), (3, 193): (255, 768), (3, 1153): (255, 0),
    (4, 97): (15, 160), (4, 193): (15, 0),
}


def record(vid, statement, certified, reproduced, ok):
    ROWS.append({"id": vid, "statement": statement, "certified": str(certified),
                 "reproduced": str(reproduced), "verdict": "PASS" if ok else "FAIL"})
    print(f"{vid:<8} {'PASS' if ok else 'FAIL'}  {statement}")
    print(f"{'':<8}       certified={certified}  reproduced={reproduced}")
    if not ok:
        raise AssertionError(vid)


# ------------------------------------------------------------------ V1
def v1_block_decomposition():
    for (n, t, q) in [(16, 2, 97), (16, 3, 97), (16, 4, 97), (16, 5, 17),
                      (16, 7, 97), (16, 8, 193)]:
        zeta = get_zeta(q, n)
        B = blocks(t)
        mats = [block_matrix(q, n, t, j) for j in range(len(B))]
        bad = 0
        n_null_direct = n_null_blocks = 0
        for x in range(1 << n):
            ps = [0] * t
            for i in range(n):
                if (x >> i) & 1:
                    for r in range(1, t + 1):
                        ps[r - 1] = (ps[r - 1] + pow(zeta, (r * i) % n, q)) % q
            direct = all(v == 0 for v in ps)
            lev = levels_of(x, n, len(B))
            viab = True
            for j in range(len(B)):
                h1 = n // 2**(j + 1)
                dv = [lev[j][i] - lev[j][i + h1] for i in range(h1)]
                for a in range(len(B[j])):
                    if sum(dv[i] * mats[j][i][a] for i in range(h1)) % q:
                        viab = False
                        break
                if not viab:
                    break
            n_null_direct += direct
            n_null_blocks += viab
            bad += (direct != viab)
        record(f"V1(n={n},t={t},q={q})",
               "x is t-null  <=>  every block-j skew constraint holds "
               "(exhaustive over 2^n)", (0, n_null_direct),
               (bad, n_null_blocks), bad == 0)


# ------------------------------------------------------------------ V2
def v2_scan_censuses():
    n = 32
    for (t, q), (c0, nc0) in sorted(SCAN.items()):
        total, sols = count_null(n, t, q, collect=True)
        M0 = 1
        while M0 <= t:
            M0 *= 2
        stride = n // M0
        full = (1 << n) - 1
        coset = noncoset = 0
        for m in sols:
            if m == 0:
                continue
            rot = ((m << stride) | (m >> (n - stride))) & full
            if rot == m:
                coset += 1
            else:
                noncoset += 1
        record(f"V2(t={t},q={q})",
               "independent MITM census reproduces the banked "
               "(coset, noncoset) mu_32 ground truth", (c0, nc0),
               (coset, noncoset), (coset, noncoset) == (c0, nc0))


# ------------------------------------------------------------------ V3
def v3_skewcount():
    """Junction-0 count over the {+-1}^G domain == archived skewcount(G)."""
    for (n, t, q) in [(16, 2, 97), (16, 3, 17), (32, 2, 97), (32, 4, 97)]:
        h1 = n // 2
        o = len(blocks(t)[0])
        cols = block_matrix(q, n, t, 0)
        rnd = random.Random(7)
        Gs = [tuple(sorted(rnd.sample(range(h1), k)))
              for k in range(1, min(h1, 8) + 1) for _ in range(6)]
        ok = True
        for G in Gs:
            Mvec = [1 if i in G else 0 for i in range(h1)]
            dom, cnt = junction_domain_and_count(q, n, t, 0, Mvec)
            brute = 0
            for e in range(1 << len(G)):
                acc = [0] * o
                for a, i in enumerate(G):
                    s = 1 if (e >> a) & 1 else -1
                    for b in range(o):
                        acc[b] += s * cols[i][b]
                brute += all(v % q == 0 for v in acc)
            ok &= (dom == 2**len(G) and cnt == brute)
        record(f"V3(n={n},t={t},q={q})",
               "junction-0 DP count over {+-1}^G equals brute-force skewcount",
               True, ok, ok)


# ------------------------------------------------------------------ V4
def v4_rank_law():
    summary = []
    for (n, t, q) in [(16, 2, 97), (16, 4, 97), (16, 7, 97), (16, 8, 193),
                      (32, 2, 97), (32, 4, 97), (32, 6, 193), (32, 8, 97),
                      (64, 8, 193), (64, 12, 193), (128, 16, 257)]:
        B = blocks(t)
        for j in range(len(B)):
            L = len(B[j])
            h1 = n // 2**(j + 1)
            cols = block_matrix(q, n, t, j)
            if h1 <= 14:                                   # exhaustive
                bad = 0
                tested = 0
                for msk in range(1 << h1):
                    S = [i for i in range(h1) if (msk >> i) & 1]
                    tested += 1
                    if rref_rank([cols[i] for i in S], q) != min(L, len(S)):
                        bad += 1
                mode = f"exhaustive 2^{h1}"
            else:                                          # systematic sample
                rnd = random.Random(1000 * n + 10 * t + j)
                bad = 0
                tested = 0
                for k in list(range(0, min(h1, L + 3) + 1)) + [h1 // 2, h1]:
                    for _ in range(40):
                        S = rnd.sample(range(h1), k)
                        tested += 1
                        if rref_rank([cols[i] for i in S], q) != min(L, len(S)):
                            bad += 1
                mode = f"sampled {tested}"
            summary.append({"n": n, "t": t, "q": q, "j": j, "L": L, "h": h1,
                            "mode": mode, "violations": bad, "tested": tested})
            if bad:
                record(f"V4(n={n},t={t},q={q},j={j})",
                       "rank{v_i : i in S} = min(L_j,|S|)", 0, bad, False)
    tot = sum(s["tested"] for s in summary)
    bad = sum(s["violations"] for s in summary)
    record("V4", f"RANK LAW rank{{v_i : i in S}} = min(L_j,|S|) over "
           f"{len(summary)} (row, junction) cells, {tot} supports tested "
           f"(exhaustive wherever h_{{j+1}} <= 14)", 0, bad, bad == 0)
    (HERE / "results" / "rank_law.json").write_text(json.dumps(summary, indent=1))


def main():
    v1_block_decomposition()
    v2_scan_censuses()
    v3_skewcount()
    v4_rank_law()
    (HERE / "results" / "dli_validation.json").write_text(json.dumps(ROWS, indent=1))
    print(f"\nC2PP_DLI_MODEL_VALIDATION: {len(ROWS)}/{len(ROWS)} PASS")


if __name__ == "__main__":
    main()

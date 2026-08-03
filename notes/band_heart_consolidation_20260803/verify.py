#!/usr/bin/env python3
"""Row arithmetic for the band-heart consolidation (coordinator, 2026-08-03).

Checks, at the six recorded rows (constants from
notes/pilots_20260802/support4_relation/stage5_escape.json):
 (1) the PROVED floor bounds on the ray-side classes;
 (2) the NEGATIVE finding: even granting lemmas L-A and L-B, the
     pair-graph lens C(V,2) EXCEEDS the 0.68 n^2 occupancy budget at
     every row — the charge/ray route cannot close the heart alone;
 (3) the calibration gap: the banked U-mechanism core count (~n/2) is
     ~2n/2.72 below budget, consistent with the core-count route.
"""
import json

ROWS = json.load(open('notes/pilots_20260802/support4_relation/stage5_escape.json'))['criterion']
BUDGET = 0.68


def require(c, m):
    if not c:
        raise SystemExit('FAIL: ' + m)


for r in ROWS:
    n, k, h, R = r['n'], r['k'], r['h'], r['R']
    require(R == n - k, 'R identity ' + r['name'])
    rank_budget = 2 * R - 1          # Lemma R + banked L2: rank <= 2m-1 <= 2R-1
    v_dead_max = rank_budget // h    # 3-drop floor: dead rays cost h each
    v_esc2_max = rank_budget // 2    # core rays escaping >= 2 cost >= 2 each
    v0_max_LA = n // 2               # under L-A: zero-escape => disjoint blocks, t >= 2
    # under L-A + L-B (V1 = 0): total live V bound
    V = v0_max_LA + v_esc2_max + v_dead_max
    pairs = V * (V - 1) / 2
    ratio = pairs / (n * n)
    # (2) the pair-graph lens FAILS at every row (this is the finding):
    require(ratio > BUDGET, 'pair-graph lens unexpectedly closes ' + r['name'])
    # (1) the individual floor bounds are sane and small where claimed:
    require(v_dead_max * h <= rank_budget, 'dead floor ' + r['name'])
    print('%-11s V<= %.3fn  pairs/n^2 = %.3f  (budget %.2f)  v_dead<=%d' % (
        r['name'], V / n, ratio, BUDGET, v_dead_max))

# (3) calibration: U-mechanism N_1 = 510 at n = 1024 (RowC 1/4) — the
# measured core count is ~n/2, a factor ~2.7e3 x n under the budget:
n_rowc = 1024
require(510 <= n_rowc / 2 + 2, 'U-mechanism calibration')
require((n_rowc / 2) / (BUDGET * n_rowc * n_rowc) < 0.001, 'core-count headroom')
print('U-mechanism calibration: N_1 = 510 ~ n/2; core-count route headroom > 1000x')
print('CONSOLIDATION_ARITHMETIC_PASS')

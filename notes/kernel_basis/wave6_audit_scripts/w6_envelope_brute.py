#!/usr/bin/env python3
"""w6 check: validate 9d058055's finite-extrema envelope reduction by brute force.

For many small parameter sets, compare highcore_local_envelope_rank (candidate
points {1, crossover+/-1, saturation, max}) against a full scan over every
basis count b in 1..C(k,a).  Also compare highcore_overlap_rank against a
direct all-b line-or-chart check.
"""
from math import comb
import sys

sys.path.insert(0, "/tmp/claude-1000/-home-u2470931-smooth-read-solomin/d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad")
from w6_xr_cogirth_verify import highcore_local_envelope_rank, highcore_overlap_rank


def brute_local_envelope_rank(n, k, reserve, budget):
    radius = n - k
    line_cap = radius // reserve
    paid_rank = 1
    for affine_dimension in range(2, k + 2):
        a = affine_dimension - 1
        maximum_bases = comb(k, a)
        denominator = comb(reserve + a, a)
        worst = 0
        for b in range(1, maximum_bases + 1):
            chart = min(n, radius + b + a - 1)
            subsets = comb(chart, a)
            acg = subsets * (chart - a) // denominator
            line = line_cap * (subsets // b)
            worst = max(worst, min(acg, line))
        if worst > budget:
            break
        paid_rank = affine_dimension
    return paid_rank


def brute_overlap_rank(n, k, reserve, budget):
    radius = n - k
    line_cap = radius // reserve
    paid_rank = 1
    for affine_dimension in range(2, k + 2):
        a = affine_dimension - 1
        maximum_bases = comb(k, a)
        ok = True
        for b in range(1, maximum_bases + 1):
            line_paid = line_cap * (comb(n, a) // b) <= budget
            chart = min(n, radius + b + a - 1)
            acg_paid = comb(chart, a) * (chart - a) <= budget * comb(reserve + a, a)
            if not (line_paid or acg_paid):
                ok = False
                break
        if not ok:
            break
        paid_rank = affine_dimension
    return paid_rank


def main():
    mismatches = 0
    tested = 0
    for n in range(6, 40):
        for k in range(2, min(n - 1, 12)):
            radius = n - k
            for reserve in (1, 2, 3, 5):
                if reserve > radius:
                    continue
                for budget_scale in (1, 8, 64, 8 * n, 8 * n * n, 8 * n ** 3):
                    budget = budget_scale
                    tested += 1
                    fast = highcore_local_envelope_rank(n, k, reserve, budget)
                    slow = brute_local_envelope_rank(n, k, reserve, budget)
                    if fast != slow:
                        mismatches += 1
                        print("LOCAL MISMATCH", (n, k, reserve, budget, fast, slow))
                    fast2 = highcore_overlap_rank(n, k, reserve, budget)
                    slow2 = brute_overlap_rank(n, k, reserve, budget)
                    if fast2 != slow2:
                        mismatches += 1
                        print("OVERLAP MISMATCH", (n, k, reserve, budget, fast2, slow2))
    print(f"W6_ENVELOPE_BRUTE tested={tested} mismatches={mismatches}")
    if mismatches:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

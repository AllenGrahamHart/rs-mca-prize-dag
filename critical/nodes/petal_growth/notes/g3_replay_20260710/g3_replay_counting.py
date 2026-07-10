#!/usr/bin/env python3
"""Fresh verifier, part 2: the counting/assembly nodes of the fifth E22 branch.

Ground truth = direct enumeration of all 2^n supports (n = 8, 16).
Weights: w == 1, a pseudorandom weight, and the payload's toy weight —
the branch is weight-parametric, so every check is run for all three.

Checks:
  [GF]    e22_residual_profile_generating_function: coefficient formula equals
          the (c, r, b) histogram exactly, for every eligible pair; and the
          admissible slice sum equals #{R : adm(M_i) and adm(M_j)}.
  [IE]    e22_lower_scale_filter_inclusion_exclusion (ELIGIBLE-scale reading):
          weighted inclusion-exclusion over smaller ELIGIBLE scales equals the
          direct weighted count of minimal-at-M_i members of the universe.
  [IE-lit] the LITERAL statement reading (all dyadic M' < M_i, incl. M' <= t):
          demonstrate it gives 0 (scale-1 event is universal), i.e. the
          statement's quantifier domain is wrong as written.
  [OVL]   e22_minimal_scale_overlap_counts: O_{i,j} from the GF+IE pipeline
          equals direct enumeration.
  [TRI]   e22_dyadic_chain_mobius_accounting: A_j = N_j + sum_{i<j} O_{i,j}.
  [COL]   e22_minimal_scale_column_evaluation: sum_j (A_j - sum_i O_{i,j})
          equals the weighted count of supports with >= 1 admissible scale,
          i.e. the disjoint-cell sum.
  [CNT]   e22_minimal_scale_count_formula: N_j equals the weighted count of
          supports satisfying the tail criterion at M_j.

--mutate: negative control (drops one inclusion-exclusion subset).
"""

from __future__ import annotations

import sys
from itertools import combinations

sys.path.insert(0, "/tmp/claude-1000/-home-u2470931-smooth-read-solomin/d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad")
from g3_lib import (
    WEIGHTS,
    admissible,
    dyadic_scales,
    eligible_scales,
    gf_counts,
    minimal_scale,
    residual_stats,
    tail_criterion,
    tail_size,
)

MUTATE = "--mutate" in sys.argv


def powerset(items):
    items = list(items)
    for r in range(len(items) + 1):
        yield from combinations(items, r)


def run(n: int, t: int) -> None:
    elig = eligible_scales(n, t)
    allscales = dyadic_scales(n)
    masks = list(range(1 << n))
    # precompute tail sizes for every dyadic scale
    ts = {M: [tail_size(n, M, mk) for mk in masks] for M in allscales}
    adm = {M: [ts[M][mk] < M for mk in masks] for M in allscales}
    msc = []
    for mk in masks:
        a = [M for M in elig if adm[M][mk]]
        msc.append(min(a) if a else None)

    # [GF]
    for i, Mi in enumerate(elig):
        for Mj in elig[i + 1:]:
            hist: dict[tuple[int, int, int], int] = {}
            for mk in masks:
                key = residual_stats(n, Mi, Mj, mk)
                hist[key] = hist.get(key, 0) + 1
            formula = gf_counts(n, Mi, Mj)
            assert formula == hist, ("GF", n, t, Mi, Mj)
            slice_sum = sum(
                v for (c, r, b), v in formula.items()
                if b < Mi and b + Mi * r < Mj
            )
            direct = sum(1 for mk in masks if adm[Mi][mk] and adm[Mj][mk])
            assert slice_sum == direct, ("GF-slice", n, t, Mi, Mj)
    print(f"  PASS [GF] n={n} t={t}")

    for wname, wf in WEIGHTS.items():
        w = [wf(mk, n) for mk in masks]

        # per-scale aggregates
        A = {M: sum(w[mk] for mk in masks if adm[M][mk]) for M in elig}
        N = {M: sum(w[mk] for mk in masks if msc[mk] == M) for M in elig}
        O: dict[tuple[int, int], int] = {}
        for i, Mi in enumerate(elig):
            for Mj in elig[i + 1:]:
                O[(Mi, Mj)] = sum(
                    w[mk] for mk in masks if msc[mk] == Mi and adm[Mj][mk]
                )

        # [IE] + [OVL]: pipeline overlap via inclusion-exclusion over smaller
        # ELIGIBLE scales inside the GF universe
        for i, Mi in enumerate(elig):
            smaller = [M for M in elig if M < Mi]
            for Mj in elig[i + 1:]:
                universe = [mk for mk in masks if adm[Mi][mk] and adm[Mj][mk]]
                total = 0
                for S in powerset(smaller):
                    if MUTATE and len(S) == len(smaller) and S:
                        continue  # negative control: drop the top subset
                    term = sum(
                        w[mk] for mk in universe
                        if all(adm[Mp][mk] for Mp in S)
                    )
                    total += (-1) ** len(S) * term
                assert total == O[(Mi, Mj)], ("IE/OVL", wname, n, t, Mi, Mj, total, O[(Mi, Mj)])

        # [IE-lit]: literal statement domain (ALL dyadic M' < M_i)
        for i, Mi in enumerate(elig):
            if i == 0 and t >= 1:
                smaller_lit = [M for M in allscales if M < Mi]
                if not smaller_lit:
                    continue
                Mj = elig[i + 1] if i + 1 < len(elig) else None
                if Mj is None:
                    continue
                universe = [mk for mk in masks if adm[Mi][mk] and adm[Mj][mk]]
                lit_minimal = sum(
                    w[mk] for mk in universe
                    if all(ts[Mp][mk] >= Mp for Mp in smaller_lit)
                )
                # scale-1 tail is always empty -> event universal -> minimal set empty
                assert lit_minimal == 0, ("IE-lit nonzero?", n, t, Mi)
                direct_minimal = O[(Mi, Mj)]
                if direct_minimal != 0:
                    print(
                        f"  [IE-lit] n={n} t={t} Mi={Mi} Mj={Mj} w={wname}: literal-domain "
                        f"minimal weight = 0, eligible-domain = {direct_minimal} (statement drift confirmed)"
                    )

        # [TRI]
        for j, Mj in enumerate(elig):
            lhs = A[Mj]
            rhs = N[Mj] + sum(O[(Mi, Mj)] for Mi in elig[:j])
            assert lhs == rhs, ("TRI", wname, n, t, Mj, lhs, rhs)

        # [COL]
        col = sum(A[Mj] - sum(O[(Mi, Mj)] for Mi in elig[:j]) for j, Mj in enumerate(elig))
        anyadm = sum(w[mk] for mk in masks if msc[mk] is not None)
        assert col == anyadm, ("COL", wname, n, t, col, anyadm)

        # [CNT]
        for Mj in elig:
            crit = sum(w[mk] for mk in masks if tail_criterion(n, t, mk, Mj))
            assert crit == N[Mj], ("CNT", wname, n, t, Mj, crit, N[Mj])

        print(f"  PASS [IE/OVL/TRI/COL/CNT] n={n} t={t} weight={wname}")


def main() -> None:
    for n, tvals in ((8, (1, 2, 3)), (16, (1, 3))):
        for t in tvals:
            run(n, t)
    print("ALL PASS: counting/assembly layer (weight-parametric)")


if __name__ == "__main__":
    main()

# TARGET 4 — THE h = 4 SHALLOW COLLISION CENSUS. Prove or falsify.

The next rung of a ladder with two proved predecessors. Self-
contained; either resolution moves a load-bearing kernel (the
census core of the rigidity-kernel program, notes/kernel_basis/).

## Setup

q an odd prime with q > 4 (so indices 1,2,3 are p-free), N a power
of two with N | q - 1, mu_N <= F_q^x. For h >= 2 define the
SHALLOW COLLISION CENSUS

  T_h(q, N) = #{ ordered pairs (A, B) : A, B disjoint h-subsets of
                 mu_N with p_i(A) = p_i(B) for i = 1, ..., h-1 }.

Known: T_2 <= C N^{5/2} (proved via Heath-Brown--Konyagin;
ladder data to N = 512 puts the truth at ~N^2). At h = 3, the
characteristic-zero pair families are classified (toral/unit-circle
families only), and all interior mass at finite q is norm-gate
accidents with per-shape activation at most phi(N) log 6 / (2 log N)
primes. Structured families at h <= 3 are exactly: quotient
pullbacks (coset-compatible pairs) and toral families.

## The conjecture

There is an absolute constant C such that for all (q, N) as above:

    T_4(q, N) <= C N^3,

with the pair families attaining the count classified as (i)
quotient pullbacks, (ii) toral/norm-kernel families, and (iii)
finitely many norm-gate accident shapes per (N), each active at
O(phi(N) / log N) primes.

## PROVE OR FALSIFY.

Notes: the exponent 3 is the first uncommitted point above the
proved T_2 <= C N^{5/2} and the h-ladder heuristic T_h ~ N^{h-1};
a proof of ANY exponent < 4 with the classification is valuable; a
falsification means a family (3+ growing scales, exact counts)
beating every polynomial the classification permits. The h = 2
proof imports Stepanov's method; whether it extends past the
resolvent degree at h = 4 is exactly the open question. In-repo
context: the shared_census_kernel node (dag.json), the f3_h2/h3
theorem nodes and their verifiers, and qx13_pair_rank_ledger
(the moment-level machinery, replayed 164/164).

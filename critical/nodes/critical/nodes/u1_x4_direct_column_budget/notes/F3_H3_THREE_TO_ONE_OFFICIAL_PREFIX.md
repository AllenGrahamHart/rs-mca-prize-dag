# F3 h=3 three-to-one official-prefix falsifier

> **REPAIR AT IMPORT (2026-07-10, catch #71 — fresh-context amber audit of the
> worktree proposal):** the trace-zero envelope `A_3^0 <= binom(R,2)` is FALSE
> for the pair-orbit count the compiler consumes — counterexample at
> (p,n) = (7937,64): A_3^0 = 2 pair-orbits ({P,-P} class, missed by the
> binomial) vs binom(R,2) = 1 (exact enumeration; cx_amber_audit_20260710.py,
> 32 PASS incl. the counterexample). CORRECTED ENVELOPE:
> A_3^0 <= 2*binom(R,2) + R = R^2 <= I^2/36 < (4/9) n^(4/3) (the R-term
> cancels exactly). All displayed `8n^(4/3)` / `(2/9)` constants below are
> SUPERSEDED by `16n^(4/3)` / `(4/9)`; the closing identity re-lands at
> exactly n^3 (4/9 = 16/36). The 'combined 6986 < 8191, no retune' corollary
> DIES (corrected 5780 + 4096 = 9876 > 8191) — only the C36' identity route
> survives, which is the route the master assembly uses.

Status: EXACT FINITE FALSIFICATION EVIDENCE; NOT `H3-3TO1-C36`.

## Target

For `n=8192`, the direct-floor conjecture is

```text
N_3to1((1-H)\{0}) < 36n^2-8n^(4/3)-n/2.       (P1)
```

The first official prime had already survived `(P1)`.  This sweep tests whether
that row concealed prime-to-prime spikes by scanning the first twelve primes
`p=1 (mod n)` with `p>=n^2`.  These are the rows where the random-scale main
term `n^4/(p-1)` is largest.

Failure criterion: one exact row with `N_3to1` at least the right side of
`(P1)`.  Such a row falsifies `H3-3TO1-C36`, though it need not falsify the
smaller complete-splitting count that the direct floor actually consumes.

## Result

Modal run

```text
ap-r3ml7etGBYJnPdtJqnGHUW
```

completed all twelve rows exactly.  No falsifier was found.  The worst row was
the first:

```text
n=8192
p=67239937
N_3to1=66933997
N_3to1/n^2=0.9973942786455154
threshold=2414593885.0251856
N_3to1/threshold=0.02772060238167208
```

Across the prime prefix, `N_3to1/n^2` decreased from `0.997394279` to
`0.986549750`.  The nonidentity product-over-quotient overlap maximum ranged
from `14` to `20`, below the separate sufficient cap `35` on every row.

This is strong resistance to the cheapest official-boundary falsifier, not a
uniform theorem.  It covers twelve of infinitely many official primes for one
of the twenty-nine official subgroup orders.

## Replay

```bash
~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_three_to_one_official_prefix_modal.py
```

Expected digest:

```text
H3_THREE_TO_ONE_OFFICIAL_PREFIX completed=12 falsified=0 \
worst_prime=67239937 worst_ratio_n2=0.997394279
```

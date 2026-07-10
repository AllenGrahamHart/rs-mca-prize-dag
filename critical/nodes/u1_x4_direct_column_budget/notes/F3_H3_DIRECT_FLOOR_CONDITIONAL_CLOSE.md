# F3 h=3 direct-floor conditional close

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

Status: PROVED CONDITIONAL COMPILER.

## Premise

Assume `F3-H3-3TO1-C36`:

```text
N_3to1((1-H)\{0})<36n^2-16n^(4/3)-n/2.   [C36-prime, catch #71 repair]
```

## Proved implication

The banked direct-floor inputs are

```text
T_3 <= n^2/72+n(A_3^0+A_3^nz),
A_3^0 < (4/9)n^(4/3),   [catch #71 repair]
A_3^nz <= N_3to1((1-H)\{0})/36.
```

Substitution gives

```text
T_3
 < n^2/72+(4/9)n^(7/3)
   +(n/36)(36n^2-16n^(4/3)-n/2)
 = n^3.
```

The `n^(7/3)` terms cancel because `4/9=16/36`; the `n^2` terms cancel because
`1/72=(1/2)/36`. The implication is strict because the premise and the
trace-zero bound are strict.

If `R_3` is the fully stripped primitive direct-column residue of width three,
then `R_3<=T_3`, so the same premise proves

```text
R_3<n^3.                                        (H3-PAY)
```

No rank, bridge, shifted-energy, or overlap-cap premise is needed by this
compiler. Those remain alternate proof routes for the red premise.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_u1_x4_amber_assembly.py
```


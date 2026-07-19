# F3 h=3 three-to-one C36 node

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

Status: PROPOSED TARGET / RED.

## Statement

For every official row

```text
n=2^s, 13<=s<=41,
p prime, p=1 (mod n), p>=n^2,
H<=F_p^* of order n,
A=(1-H)\{0},
```

define

```text
N_3to1(A)=#{(a1,a2,a3,a4) in A^4:a1*a2*a3=a4}.
```

Then

```text
N_3to1(A)<36n^2-16n^(4/3)-n/2.               (C36-prime, catch #71 repair)
```

This is the complete proposed red premise. It does not assert shifted-energy
control, a pointwise Mobius-fiber cap, or any particular proof mechanism.

## Falsifier

One official row on which the exact count is at least the right side of `(C36)`
falsifies this node. It would not necessarily falsify the h=3 floor, because
`N_3to1` is an envelope containing product tuples which fail the complete-split
filter.

The exact twelve-prime `n=8192` official-prefix sweep found no falsifier. Its
worst count used `0.027721` of the original threshold (`0.02774` of the
repaired C36-prime threshold). This is evidence only.

## Proved interface

`F3_H3_DIRECT_FLOOR_CONDITIONAL_CLOSE.md` proves that `(C36)` implies the
complete h=3 payment `T_3<n^3`.


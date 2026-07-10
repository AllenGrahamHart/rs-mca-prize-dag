# F3 h=3 trace-zero official payment

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

Status: PROVED OFFICIAL-ROW TRACE-ZERO PAYMENT.

## Target

Let `H=mu_n <= F_p^*`, where

```text
n=2^s,       13<=s<=41,       p=1 mod n,       p>=n^2.
```

Let `A_3^0(n,p)` count dilation-normalized unordered pairs of distinct
three-subset orbits with

```text
e1(P)=e1(Q)=0,       e2(P)=e2(Q),
```

after any paid/repaired exclusions.  Then

```text
A_3^0(n,p) < 2890*n.
```

Thus trace zero is paid directly.  It does not need private `q`, which is
undefined on this branch.

## Zero-sum orbit count

For a zero-sum triple, divide by one coordinate and write it as

```text
{1,x,y},       1+x+y=0,       x,y in H.
```

Since `-1 in H`, the number of ordered ratio solutions is

```text
I=|{x in H: x+1 in H}|.
```

Every dilation orbit of a three-element zero-sum subset gives six ordered
ratio solutions.  The action is free: a nontrivial dilation stabilizer of a
three-set would have order three, impossible in a power-of-two group.
Degenerate/repeated solutions only increase `I`.  Hence the number `R` of
distinct zero-sum three-subset dilation orbits satisfies

```text
R <= I/6.
```

The trace-zero classifier `c0=b^(n/2)` partitions these `R` orbits.  Therefore
all activated trace-zero pairs, even before paid exclusions, satisfy

```text
A_3^0 <= 2*binom(R,2)+R = R^2 <= I^2/36.   [catch #71 repair; see banner]
```

## Optimized one-shift Stepanov bound

Apply the proved auxiliary-polynomial theorem from
`F3_H2_RICH_COSET_STEPANOV.md` to the single shift `-1`.  For every official
`n`, choose

```text
A=D=floor((27*n^2/64)^(1/3)),
B=floor((125*n/64)^(1/3))+1.
```

Its size hypothesis holds because `p>n^2` implies `n^4<p^3`.

The exact replay verifies at all 29 rows:

```text
D(A+D) < A*B^2,
A*B <= n,
A+n*B < n^2+1 <= p,
(A+2nB)^3 < 64*A^3*n^2.
```

These are exactly the linear-system, nonvanishing, and degree inequalities of
the proved Stepanov lemma.  The last inequality gives

```text
I < (A+2nB)/D < 4*n^(2/3).
```

Consequently

```text
A_3^0 < (4/9)*n^(4/3) < 5780*n   [catch #71 repair]
```

through `n=2^41`; the final inequality is checked by exact cubing.

## Compiler consequence

If the remaining nonzero-trace family proves

```text
A_3^nz(n,p) <= 4096*n,
```

then the full activation count obeys

```text
A_3(n,p) < 6986*n.
```

The existing h=3 arithmetic compiler accepts every uniform integer constant
at most `8191`, so `6986` proves `T_3<n^3` on every official row.  The
nonzero-trace bridge may continue to use its existing `H3-ACT(4096)` boxes;
there is no need to retune them to the weaker `8191` rank-deficit profile.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_tracezero_official_payment.py
```

Expected digest:

```text
H3_TRACEZERO_OFFICIAL_PAYMENT_PASS rows=29 trace_c=2890 combined_c=6986
```

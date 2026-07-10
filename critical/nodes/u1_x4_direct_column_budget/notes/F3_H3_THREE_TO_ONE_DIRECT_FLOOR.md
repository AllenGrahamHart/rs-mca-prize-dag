# F3 h=3 three-to-one direct-floor compiler

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

Status: PROVED STRICT RETARGETING; EXPLICIT THREE-TO-ONE COUNT BOUND OPEN.

## The narrower envelope

Put

```text
A=(1-H)\{0}
```

and define

```text
N_3to1(A)=#{(a1,a2,a3,a4) in A^4: a1*a2*a3=a4}.
```

The shifted-product splitting reduction proves, before its final
Cauchy--Schwarz step,

```text
36 A_3^nz = S_nz <= N_3to1(A) <= E_x(A).       (TO1)
```

Thus shifted multiplicative energy is only a convenient positive envelope;
it is not the closest object consumed by the floor.

Writing `ai=1-xi`, the three-to-one count is equivalently the one-forced-
output count

```text
N_3to1(A)
 =#{(x,y,z) in (H\{1})^3:
       1-(1-x)(1-y)(1-z) in H}.                (TO2)
```

The forced output cannot equal `1`, since all three factors are nonzero.
Unlike energy, `(TO2)` retains the orientation of the product relation and
does not square a representation function.

## Exact direct-floor threshold

The proved h=3 inputs are

```text
T_3 <= n^2/72+n(A_3^0+A_3^nz),
A_3^0 < (2/9)n^(4/3),
A_3^nz <= N_3to1(A)/36.
```

Consequently the complete h=3 stratum closes whenever

```text
N_3to1(A) < 36n^2-8n^(4/3)-(1/2)n.            (TO3)
```

This is the same numerical threshold previously imposed on `E_x(A)`, but
it is a strictly weaker theorem because of `(TO1)`.  In particular, proving
`(TO3)` is sufficient for the official floor without proving either
`H3-ACT(4096)` or the cyclotomic third-factorial-moment target.

## Fourier distinction from energy

For a multiplicative character `chi` of `F_p^*`, put

```text
S_chi=sum_(a in A) chi(a).
```

Multiplicative character orthogonality gives exactly

```text
N_3to1(A)=1/(p-1) sum_chi S_chi^3 conjugate(S_chi),
E_x(A)   =1/(p-1) sum_chi |S_chi|^4.           (TO4)
```

The nontrivial-character terms in the first sum retain phases and may
cancel.  Replacing them by absolute values recovers `N_3to1(A)<=E_x(A)` and
discards precisely this possible saving.  A direct Jacobi-sum or auxiliary-
polynomial proof should therefore target `(TO2)` or the first expression in
`(TO4)`, not return immediately to energy.

## Small exact rows

The replay checks `(TO1)` and `(TO2)` directly:

```text
(p,n)=(97,32):    N_3to1=9692,  E_x=10315,
(p,n)=(4289,64):  N_3to1=3639,  E_x=10755,
(p,n)=(7937,64):  N_3to1=5765,  E_x=13191.
```

The first row lies outside `p>=n^2`.  On both official-regime small rows the
oriented count is below `1.5n^2`, while energy is between `2.6n^2` and
`3.3n^2`.  These are falsification data, not a uniform proof of `(TO3)`.

## Signed-collision split

Expand `(TO2)` as the vanishing sum of the eight signed subgroup roots

```text
xy, xz, yz, q, -x, -y, -z, -xyz.               (TO5)
```

`F3_H3_THREE_TO_ONE_CHARZERO_CLASSIFICATION.md` proves, over every finite
row and without a field-size hypothesis, that the `28` pair labels on which
two roots in `(TO5)` coincide collapse to `19` distinct loci and satisfy

```text
N_coll<=19(n-1)^2+2(n-1).                       (TO6)
```

Writing `N_cf` for the complementary collision-free count, `(TO3)` therefore
follows from the narrower all-field target

```text
N_cf<17n^2-8n^(4/3)+(71/2)n-17.                 (TO7)
```

This is an exact decomposition, not a claim that `(TO7)` is proved.  Its
advantage is semantic: every equality degeneration among the eight signed
roots is already paid, so the remaining count consists only of genuinely
nondegenerate finite-characteristic relations.  The exact small rows split
as

```text
(p,n)       N_3to1   N_coll   N_cf
(97,32)       9692     4742    4950
(4289,64)     3639      981    2658
(7937,64)     5765     1571    4194.
```

Thus the observed collision-free ratios are `4.833,0.649,1.024` times
`n^2`; the first row is outside the official field-size regime.

## Residual theorem

The live h=3 leaf can now be stated without an intermediate square moment:

```text
H3-3TO1-C36:
  for n=2^s, 13<=s<=41, p=1 (mod n), p>=n^2,
  N_3to1((1-H)\{0})
    < 36n^2-8n^(4/3)-n/2.
```

## First official boundary row

The pre-registered Modal run

```text
ap-xzZdLazA6MSY1K3HkD10vS
```

completed the first official boundary row exhaustively in `6.642` seconds:

```text
n=8192, p=67239937,
N_3to1(A)=66933997,
N_3to1(A)/n^2=0.997394...
```

The same row has `E_x(A)=201137059`, so retaining the orientation reduces
this envelope by a factor just over `3`.  The row survives `(TO3)` with a
wide margin.  This is evidence only; the proof obligation remains the
uniform inequality above.

## Proved large-field branch

`F3_H3_THREE_TO_ONE_CHARZERO_CLASSIFICATION.md` proves that every complex
relation is a binary telescoping relation

```text
(q,-q,-q^2) -> q^4,
```

and hence that the ordered characteristic-zero count is exactly `3(n-4)`.
The signed-collision Parseval norm bound transports this classification,
while `(TO6)` pays all collision pairs, whenever

```text
p>8^(n/4).
```

Thus `(TO3)` and the complete h=3 stratum are proved in that large-field
branch.  The remaining uniform debt is confined to

```text
n^2<=p<=8^(n/4).
```

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_three_to_one_direct_floor.py
```

Expected digest:

```text
H3_THREE_TO_ONE_DIRECT_FLOOR_PASS rows=3 collision_free=11802
```

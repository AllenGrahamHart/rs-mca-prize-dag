# F3 h=3 repeat-boundary LP4 Stepanov compiler

Status: CONDITIONAL ARITHMETIC COMPILER, NOT A LINE-PENCIL BOUND.

This packet records the exact Stepanov bookkeeping for the line-pencil target
from `F3_H3_REPEAT_BOUNDARY_LINE_COMPILER.md`.  It is deliberately conditional:
the h=2 rich-coset theorem does not prove this four-form statement, and the
current h=3 rich-curve compiler has only three subgroup variables.

## Pre-registration

Question:

```text
What is the exact auxiliary-polynomial compiler needed to bound B_line?
```

Success criterion:

- reuse the log-jet idea from the h=3 rich-curve compiler;
- exploit that all four boundary maps are affine linear;
- state the missing nonvanishing/rank gate explicitly;
- show how a future line-pencil theorem pays the repeat residue.

Failure criterion:

- claim the h=2 two-form rich-coset estimate proves the four-form line count;
- silently drop the fourth membership condition `lambda in H`;
- promote the compiler to an unconditional bound.

## Why This Is a New Gate

The line compiler reduces the repeat boundary to the count `B_line` of pairs
`(r,t)` for which

```text
L_1(t)=1+t,
L_2(t)=1+rt,
L_3(t)=1-(r/(r+1))t,
L_4(t)=1+((r^2+r+1)/(r+1))t
```

all lie in `H`, with `L_1,L_2,L_3` distinct.

The h=2 rich-coset theorem controls two affine membership conditions, summed
over shift cosets.  If applied only to `L_1,L_2`, it sees essentially every
ordered pair `(u,v) in H^2` and gives the trivial scale `n^2`.  The fourth
condition is essential.

The existing h=3 rich-curve compiler handles three degree-2 rational maps.
Here one can set the source variable to `t`; the boundary target is four
degree-1 maps.  The lower degree improves the arithmetic, but it still needs a
four-block nonvanishing theorem.

## LP4 Auxiliary

For a family `R` of repaired line parameters `r`, use

```text
Phi(X,Y_1,Y_2,Y_3,Y_4),
deg_X < A,
deg_{Y_i} < B.
```

For fixed `r`, substitute

```text
Psi_r(X)=Phi(X, L_1(X)^n, L_2(X)^n, L_3(X)^n, L_4(X)^n).
```

There are

```text
A B^4
```

coefficients.

Since the `L_i` are affine, no denominator clearing is needed after fixing a
nondegenerate `r`.  The substituted degree is at most

```text
L_4(A,B,n) = (A-1) + 4n(B-1).
```

Thus, under nonvanishing, multiplicity `D` at all counted points gives

```text
sum_{r in R} T_r < |R| L_4(A,B,n) / D.
```

## Log-Jet Reduction

For a monomial

```text
m(X)=X^a prod_i L_i(X)^{n b_i},
0 <= a < A, 0 <= b_i < B,
```

put

```text
S(X)=X prod_i L_i(X).
```

At admissible boundary points, `X != 0` and all `L_i(X) != 0`.  The logarithmic
derivative recurrence used in the h=3 rich-curve packet gives

```text
S(X)^j m^{(j)}(X) = m(X) W_j(X),
deg W_j <= 4j,
```

because `deg S <= 5`.  Since `L_i(X)^n=1` at admissible points, the `j`-th
multiplicity condition is over-imposed by a polynomial in `X` of degree
`< A+4D`.  Hence it is represented by at most

```text
5(A+D)
```

linear coefficient conditions per derivative order and per line parameter.
This proves the reduced-condition gate:

```text
LP4-RED(5):
  conditions <= 5 D (A+D) |R|.
```

## Conditional Compiler

The remaining theorem gate is:

```text
LP4-RANK / LP4-NV:
  after excluding the finite coefficient-collision parameters and separately
  paying or including the q(r)=r^2+r+1 triple-repeat cell, the direct-sum
  substitution image over R has rank greater than 5D(A+D)|R|.
```

If

```text
5 D (A+D) |R| < A B^4
```

and `LP4-RANK` holds, then

```text
B_line = sum_{r in R} T_r
       < |R| ((A-1)+4n(B-1)) / D.
```

Combined with the previous packet,

```text
repeat_residue <= 12 n B_line + 18 n^2.
```

Thus any line-pencil theorem with `B_line <= C n^alpha`, `alpha < 2`, makes the
repeat residue subcubic:

```text
repeat_residue <= 12 C n^{1+alpha} + 18 n^2.
```

The proof debt is now sharply separated: prove the LP4 rank/nonvanishing
theorem and optimize the constants, or pay the line-pencil boundary by another
method.

The LP4 exception ledger records the excluded cells for this generic gate:
`r in {0,-1,1,-1/2,-2}` is inadmissible for distinct triples, while
`r^2+r+1=0` is the q0 triple-repeat cell already paid by the q0 packet.

## Replay

Standalone arithmetic check:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_lp4_stepanov_compiler.py
```

Expected digest:

```text
H3_REPEAT_BOUNDARY_LP4_STEPANOV_COMPILER_PASS
```

# F3 official rich-coset Stepanov theorem with constant 6

Status: PROVED FOR THE OFFICIAL `n>=8192`, `p>=n^2` REGIME.

## Statement

Let `H=mu_n<=F_p^*`, where

```text
n>=8192,       p>=n^2.
```

For a nonzero shift `u`, put

```text
C(u)={x in H:x-u in H}.
```

If `U` is a set of `T>=1` nonzero shifts, no two in the same multiplicative
`H`-coset, then

```text
sum_(u in U) |C(u)| <= 6 (nT)^(2/3).            (K6)
```

This is an official-regime sharpening of the self-contained constant `129`
theorem in `F3_H2_RICH_COSET_STEPANOV.md`.  It uses the same auxiliary
polynomial and sparse nonvanishing lemma; only the parameter choice and the
field-size input are sharpened.

## Normalization and small scale

As in the existing proof, normalize

```text
D(u)=u^(-1)C(u),       E=union_(u in U)D(u).
```

The sets `D(u)` are disjoint and every `z in E` satisfies

```text
z^n=(z-1)^n.
```

Since `n<p`, the nonzero polynomial `z^n-(z-1)^n` has degree `n-1`.
Therefore

```text
|E|<n.                                               (K6a)
```

Set

```text
X=n^(2/3)T^(-1/3),       Y=n^(1/3)T^(1/3).
```

Then `XY=n`, `X^2T=XY^2`, and

```text
R=(nT)^(2/3)=nY/X=n^2/X^2.
```

If `X<=36`, inequality `(K6a)` and `T>=1` give

```text
|E|/R <= X^2/n <= sqrt(X) <= 6.                 (K6b)
```

## Auxiliary-polynomial parameters

Assume `X>36` and choose

```text
A=floor(X),       B=floor(Y),       D=floor(2X/5).
```

The relation `T>=1` gives `n>=X^(3/2)`, hence `Y=n/X>=sqrt(X)>6`.  The floor
bounds are

```text
A>(35/36)X,
B>(5/6)Y,
D<=(2/5)X,
A+D<=(7/5)X.
```

Consequently

```text
AB^2 > (875/1296)XY^2
     = (875/1296)X^2T,

D(A+D)T <= (14/25)X^2T.
```

Since `875/1296>14/25`, the auxiliary linear system has a nonzero solution.

## Nonvanishing and degree

The sparse nonvanishing conditions hold.  First,

```text
AB<=XY=n.
```

Second, distinct shift cosets give `T< p/n`, so

```text
X<=n^(2/3)<=p^(1/3),
Y=(nT)^(1/3)<p^(1/3),
nY<p^(5/6).
```

For the official range, `p^(1/3)+p^(5/6)<p`; hence

```text
A+nB<X+nY<p.
```

The sparse lemma from the original proof therefore shows that the specialized
auxiliary polynomial is nonzero.

Its root multiplicity and degree give

```text
|E|<(A+2nB)/D.
```

Since `X>36`,

```text
D>(67/180)X.
```

It follows that

```text
|E| < 180/67 + (360/67)R
     < (180/(67*36)+360/67)R
     < 6R.                                      (K6c)
```

Together, `(K6b)` and `(K6c)` prove `(K6)`.

## Consequences

The existing exact level-set compiler states that rich-coset constant `K`
implies

```text
E_+(H) <= (1+5(K^2+K)) n^(5/2).
```

With `K=6`, this becomes

```text
E_+(H) <= 211 n^(5/2),
T_2 <= (211/8)n^(5/2)<n^3
```

for `n>(211/8)^2=44521/64`.  Thus the in-house h=2 route now closes every
official row without the external sharp constant.

For h=3, `(K6)` supplies the optimized one-condition rich-cell leg needed by
the truncated product/quotient tail program.  It does not by itself prove the
joint weighted tail: the affine product-mass condition must still be retained.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_official_rich_coset_k6.py
```

Expected digest:

```text
F3_OFFICIAL_RICH_COSET_K6_PASS K=6 h2_energy=211
```


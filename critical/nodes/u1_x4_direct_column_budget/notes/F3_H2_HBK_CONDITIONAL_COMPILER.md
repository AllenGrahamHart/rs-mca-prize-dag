# F3 h=2 HBK conditional compiler (Terminal B)

Status: PROVED CONDITIONAL COMPILER.  This does not close Terminal B
unconditionally; it reduces the remaining in-house proof to one explicit
rich-coset Stepanov lemma and gives the constant propagation.

## Source Map

Primary source: Heath-Brown and Konyagin, *New bounds for Gauss sums derived
from k-th powers, and for Heilbronn's exponential sum*, Quart. J. Math. 51
(2000), 221--235.  Oxford ORA record:

```text
https://ora.ox.ac.uk/objects/uuid:f2d980d4-ef1d-4b72-89a9-3d9d8527a024
```

Relevant paper labels:

- their `mu_h` is our subgroup `H`;
- their `C(u)` is our shifted-intersection fiber `r_C`;
- their Lemma 3 is exactly the additive-energy theorem `#A(h) << h^(5/2)`;
- their Lemma 5 is the rich-coset estimate whose dyadic summation proves
  Lemma 3.

The current repo still needs an in-house proof with explicit constants, so the
paper is used here only as a map.  The imported source still has implicit
Vinogradov constants.

## Conditional Lemma B2-rich

Let `H <= F_p^*` have size `h <= p^(2/3)`.  For each nonzero multiplicative
coset `C=sH`, let

```text
r_C = |H cap (H+s)|.
```

For any set `U` of `T >= 1` distinct nonzero cosets, define

```text
R(U) = sum_{C in U} r_C.
```

The single remaining B2-rich input is:

```text
R(U) <= K * (h*T)^(2/3)        for every U,
```

with an explicit absolute constant `K`, in the range `h <= p^(2/3)`.

This is the exact constant-bearing version of the HBK rich-coset lemma needed
by Terminal B.

## Compiler

Order the nonzero cosets so that

```text
r_1 >= r_2 >= ...
```

The exact first moment from `F3_H2_LEVEL_SET_REDUCTION.md` is

```text
sum_i r_i = h - 1 <= h.
```

The B2-rich lemma applied to the first `T=i` cosets gives

```text
r_i <= K h^(2/3) i^(-1/3).
```

Split indices into dyadic blocks `N <= i < 2N`.  On such a block:

```text
sum_{N <= i < 2N} r_i^2 <= K^2 h^(4/3) N^(1/3)
```

from the pointwise bound and block length, and also

```text
sum_{N <= i < 2N} r_i^2 <= K h^(5/3) N^(-1/3)
```

from the pointwise bound times the first moment.

Only positive fibers need to be counted.  Since each positive `r_i` is an
integer and `sum_i r_i <= h`, there are at most `h` positive cosets; hence the
second dyadic sum stops at `N <= h`.  Summing the first estimate for
`N <= h^(1/2)` and the second for `h^(1/2) < N <= h`, and using

```text
sum_{dyadic N <= h^(1/2)} N^(1/3) <= 5 h^(1/6),
sum_{dyadic h^(1/2) < N <= h} N^(-1/3) <= 5 h^(-1/6),
```

gives

```text
sum_i r_i^2 <= 5 * (K^2 + K) * h^(3/2).
```

Combining with the exact identity

```text
E(H) = h^2 + h * sum_i r_i^2
```

gives the explicit conditional energy theorem

```text
E(H) <= (1 + 5*(K^2+K)) * h^(5/2)      for h >= 1.
```

Therefore

```text
T_2 <= E(H)/8 <= ((1 + 5*(K^2+K))/8) * h^(5/2).
```

Once B2-rich is proved with any explicit `K`, the h=2 floor follows for all

```text
h > ((1 + 5*(K^2+K))/8)^2,
```

with the finitely many smaller `h` handled by exact replay/certificates.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_hbk_conditional_compiler.py
```

Expected digest:

```text
H2_HBK_CONDITIONAL_COMPILER_PASS
```

## Remaining Open Work

Terminal B is now concentrated into:

```text
prove B2-rich in-house with explicit K.
```

That proof is the Stepanov/nonvanishing/rank content.  Everything after it is
the elementary dyadic compiler above.

# Proof - L1 joint core/background Johnson bound

Take two distinct exact saturated pairs `(F_1,W_1),(F_2,W_2)` and set

```text
Delta=W_1F_2-W_2F_1.                                   (1)
```

As in the fixed-support Johnson theorem, primitivity and monicity imply that
`Delta` is nonzero. The common labelled equations on `X` give
`L_X|Delta`. If `I=D_1 intersect D_2`, both terms in `(1)` are divisible by
`L_I`, so `L_I|Delta`.

Every background agreement is a background root of `W_j`. Hence, for
`R=R_1 intersect R_2`, both terms in `(1)` vanish on `R` and `L_R|Delta`.
The core, petal support, and background are pairwise disjoint. Therefore

```text
L_X L_I L_R | Delta.                                   (2)
```

Since `deg Delta<=2d`, equation `(2)` proves

```text
h+|I|+|R|<=2d,                                         (3)
```

which is `(CJ2)`. If `r=2d-h<0`, no distinct pair exists.

Suppose now that `r>=0` and write `m` for the cell size. For each core point
`x`, let `A_x` count defect sets containing `x`; for each background point
`y`, let `H_y` count chosen agreement sets containing `y`. Then

```text
sum_x A_x=md,       sum_y H_y=mu.                       (4)
```

Summing `(CJ2)` over unordered contributor pairs gives

```text
sum_x binom(A_x,2)+sum_y binom(H_y,2)<=binom(m,2)r.      (5)
```

When `(CJ3)` holds, necessarily `b>0`. Cauchy-Schwarz in the two disjoint
universes and `(4)--(5)` give

```text
m^2 d^2/N-md+m^2 u^2/b-mu<=m(m-1)r,
m(d^2/N+u^2/b-r)<=d+u-r.                               (6)
```

Now `r=d-s` and `u=ell-s`, so `d+u-r=ell`. Multiplying `(6)` by `Nb` proves
`(CJ4)`. Its denominator is a positive integer and its numerator is at most
`n^3`.

At `p<=P`, there are at most `2^M(P+1)n^P` exact petal-support patterns and
at most `n` defect degrees. Multiplying by the `n^3` cell bound and using
`2^M<=n^(1/c_0)` proves `(CJ5)`.

Finally, substitute `d=N-a`, `r=N-2a+c`, and
`u=ell-a+c` in `(CJ3)`. Cancellation gives `(CJ6)`, and failure of strict
positivity gives `(CJ7)`. If `b>0`, each nonnegative summand on the left of
`(CJ7)` is at most `Nbc`, yielding the two separate nonpositive-Johnson
inequalities. The two exact fixtures prove the sharpness assertions.

# Proof - PMA sigma-one low-defect payment

The sigma-one scope theorem gives `ell=2`, `b=1`, and `L=2M=n-k`. Exact
defect zero is empty: the maximal-sunflower tradeoff requires at least two
touched petals, while the non-planted per-petal cap is `|S_i|<=d=0`.

Fix `D` and the exact background agreement set `R_P`, and put `r=|R_P|`.
The source-to-paving bridge factors the background locator and sets

```text
kappa=d-r+1.
```

It bounds the auxiliary list by

```text
floor(binom(L,kappa)/binom(kappa+1,kappa)),
```

because `sigma=1`. There is exactly one background subset at each of
`r=0,1`. The four nonempty parameter cells are therefore

```text
(d,r)=(1,0): floor(binom(L,2)/3),
(d,r)=(1,1): floor(L/2)=M,
(d,r)=(2,0): floor(binom(L,3)/4),
(d,r)=(2,1): floor(binom(L,2)/3).
```

There are `binom(k-1,d)` choices of `D`, and the core-defect injection is
unique for fixed `D`. Summing the four cells proves `(L1)`. Since this upper
bound counts the complete source list, deleting exact-periodic members only
decreases it.

For `(L2)`, write `x=k/n` and `y=L/n=1-x`, so `0<x<=1/2`. Use the
elementary bounds

```text
binom(a,2)<a^2/2,    binom(a,3)<a^3/6.
```

Then, after division by `n^5`,

```text
B_low/n^5
 < xy/(2n^3) + xy^2/(6n^2) + x^2y^2/(12n) + x^2y^3/48.   (L3)
```

The derivative of `x^2(1-x)^3` vanishes in `(0,1/2]` only at `x=2/5`,
where its value is `108/3125`. Hence the last term in `(L3)` is at most

```text
9/12500 < 3/4096.
```

Also `xy<=1/4` and `x^2y^2<=1/16`. For every official `n>=2^13`, each of
the first three terms in `(L3)` is strictly below `1/12288`; together they
are below `1/4096`. Thus `(L3)` is strictly below

```text
3/4096 + 1/4096 = 1/1024,
```

proving `(L2)`.

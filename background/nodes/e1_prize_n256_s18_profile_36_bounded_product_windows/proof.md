# Proof

For the 64 conjugate squares `y_u` from the parent proof,

```text
0<y_u<=144,
sum_u y_u=64*18,
sum_u (y_u-18)^2=64V,
R=product_u y_u.                                    (1)
```

The upper bound is the square of the coefficient `l_1` norm, which is 12 in
profile `(3,6)`.

## Capped extremum classification

Maximize the product on the compact closure of (1). A zero coordinate gives
zero product, so a positive maximum has no lower-bound coordinate. Let `k`
coordinates attain the upper cap 144. Since their sum is at most `64*18`,
one has `0<=k<=7` at a positive maximum.

Every remaining interior coordinate satisfies the same quadratic multiplier
equation

```text
1/y=lambda+2 nu (y-18),
```

and hence takes at most two values. Put `N=64-k`. The residual mean and
variance are forced to be

```text
mu_k=(64*18-144k)/N,
W_(V,k)=(64V-k(144-18)^2-N(mu_k-18)^2)/N.            (2)
```

If the lower interior value occurs `j` times, `1<=j<N`, the two values are

```text
a=mu_k-sqrt(W_(V,k)(N-j)/j),
b=mu_k+sqrt(W_(V,k)j/(N-j)).                         (3)
```

Only chambers with `a>0` and `b<=144` are feasible. The case `W=0` is the
single residual level. Thus every positive maximum is among the finite list

```text
144^k a^j b^(N-j).                                  (4)
```

## Exact cofactor ledger

The committed certificate encloses each square root in (3) between adjacent
rationals of denominator `2^192`. It compares a rational upper endpoint of
(4) with `m B_P 2^128` for every even variance removed from the parent
window. The exact comparison counts are

```text
m=2: 2651       m=4: 2072       m=8: 1112
m=16: 516       m=32: 757       m=64: 946
m=256: 1111     m=512: 929      m=514: 929.
```

All 11023 comparisons are strict. The closest chamber occurs at the first
excluded variance: `(k,j)=(1,62)` for `m=2,4,8` and `(k,j)=(0,63)` for the
other six cofactors. For each row the certificate also finds a feasible
chamber whose rational lower endpoint exceeds the prize floor at the
preceding even variance. Combining these comparisons with the parent
windows and its exclusions of `V=0,2` proves the table.

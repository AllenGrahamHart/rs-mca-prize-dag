# Proof

Let `A` be the affine hull of the target parameter set and `C'` its
`s`-dimensional direction code on `H\D`.  Let `G` be the common-zero set of
`C'`, let `g` count the points of `G` where the common affine value agrees
with the punctured word, and put `b=|G|-g`.  As in the generalized-weight
affine compiler, the active coordinate count is `d_s=N-|G|` and every
listed parameter is incident with at least

```text
d_s-(N-K-w)+b
```

active core-agreement hyperplanes.  After `i` independent normals have been
chosen, at least `d_(s-i)-(N-K-w)+b` incident normals extend their span.
Thus every target parameter contains at least

```text
B_core=product_(j=2)^s(d_j-(N-K-w)+b)/(s-1)!          (1)
```

unordered independent `(s-1)`-subsets.  Such a subset cuts `A` to an affine
line.

## Two-point block incidence

For a projective value `[a:b]`, its `phi`-fiber is the zero set on `H` of
the nonzero polynomial `bP-aQ`.  Coprimality prevents this polynomial from
vanishing identically, so every fiber has size at most `ell`.  In an
`r`-point block the number of same-fiber pairs is at most
`r(ell-1)/2`.  Hence at least

```text
C(r,2)-r(ell-1)/2=r(r-ell)/2                         (2)
```

pairs have distinct `phi`-values.

Fix an independent core subset and parametrize its affine line by
`tau_c=tau_0+c delta`.  At `x in D`, write the error vector as

```text
V_x(c)=(E_0(x)-Q(x)delta(x)c,
        E'_0(x)+P(x)delta(x)c).                       (3)
```

It is nonzero because the invariant residual
`P E_0+Q E'_0` is nonzero on `D`.  Two points `x,y` lie in one selected
active block exactly when their unique annihilator slopes agree, equivalently

```text
det(V_x(c),V_y(c))=0.                                 (4)
```

This is a polynomial of degree at most two in `c`.  If it is nonzero, there
are at most two solutions.  If it vanishes identically, its quadratic
coefficient is

```text
delta(x)delta(y)(P(x)Q(y)-Q(x)P(y)).                  (5)
```

For a pair counted in `(2)`, the last factor is nonzero, so one of
`delta(x),delta(y)` is zero.  The corresponding error vector is fixed, and
`(4)` then forces the common annihilator slope to be fixed along the whole
line.  Two distinct target pairs at the same high depth cannot share that
globally selected ray: the first-match convention and the proved interaction
strip would give `2d<=h-1`, contrary to `d>=ceil(h/2)`.  The degenerate case
therefore contains at most one target member.  In all cases a fixed core
subset and fixed distinct-`phi` point pair own at most two occurrences.

Every target pair has at least two disjoint selected blocks.  Double counting
the core subsets from `(1)` and point pairs from `(2)` now gives

```text
2 |Tau| B_core r(r-ell)/2
 <= 2 C(d_s,s-1) C(e,2).                              (6)
```

Use `d_s<=N` and the Reed-Solomon generalized-weight inequalities

```text
d_j-(N-K-w)+b >= w+j.
```

After cancelling factorials in `(6)`, this is `(MCB1)`.

## Official arithmetic

Let `B_0=floor((17n^2-25(n-4))/25)`, the smallest possible local budget.
Put `x=d+ell`, `d_0=ceil((2h+2)/3)`, and `x_0=d_0+1`.  The affine compiler
is at most

```text
U_s(x)=product_(j=1)^s
 (R-2h+2x-1+j)/(x+j),                                 (7)
```

because `e>=2(h-d)` and `ell>=1`.  Every factor in `(7)` decreases with
`x`, since `j+1<=R-2h`.  Define `T` as the first integer with
`floor(U_s(T))<=B_0`.  The exact pins are

| rate | `s` | `x_0` | `T` | `floor U_s(T-1)` | `floor U_s(T)` |
|---|---:|---:|---:|---:|---:|
| `1/4` | 10 | 5726623064 | 5809347492 | 3288278233653601276869020 | 3288278228033288972798440 |
| `1/8` | 10 | 5726623064 | 6787763913 | 3288278231095806578696610 | 3288278226285629384991152 |
| `1/16` | 9 | 2863311533 | 3889759269 | 3288278235812617761960026 | 3288278228233027003914950 |

Thus the affine bound pays when `x>=T`.  If `x<T`, then `T<h`, so
`ell<r` and `(MCB1)` applies.  Since

```text
e<=d-ell-1<=x-3,
r-ell=h-x,
r>=h-x+1,
N<=n,
```

the mixed cap is at most

```text
F_s(x)=n^(s-1)(x-3)(x-4)
       / ((h-x)(h-x+1) product_(j=2)^s(x+j)).          (8)
```

Write `(8)=n^(s-1)A_s(x)B(x)`.  The factor `A_s` decreases for
`x>=x_0`, because

```text
A_s(x+1)/A_s(x)
 =(x-2)(x+2)/((x-4)(x+s+1))<=1
```

is equivalent to `(s-3)x>=4s`.  The factor `B` increases.  Split
`[x_0,T-1]` at `X=floor((x_0+T-1)/2)`.  Bounding the lower half by
`A_s(x_0)B(X)` and the upper half by `A_s(X)B(T-1)` gives:

| rate | `X` | lower cross-bound | upper cross-bound |
|---|---:|---:|---:|
| `1/4` | 5767985277 | 747618070831366029933789 | 732194370222112484701579 |
| `1/8` | 6257193488 | 1094070037805154915828409 | 985869572620074284318171 |
| `1/16` | 3376535400 | 1176340468015061167222396 | 2247266833636175323939571 |

All six values are below
`B_0=3288278229349592331945250`.  Hence either the affine or mixed bound
pays every allowed tuple at the displayed dimensions.  QED.

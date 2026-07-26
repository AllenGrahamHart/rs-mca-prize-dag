# Proof

Write `L_A(u,m)` for the listed codewords in the affine flat.

## Recursive compiler

Induct on `s`. The case `s=0` is immediate. Let

```text
G={x in D: c(x)=0 for every c in C'},       z=|G|.
```

All polynomials in the `s`-dimensional direction space are divisible by the
locator of `G`. After division they have degree below `K-z`, so dimension
gives

```text
z<=K-s.                                                   (1)
```

Let `g` be the number of coordinates in `G` where the common affine value
agrees with `u`. Every listed codeword has at least `m-g` agreements outside
`G`. For `x` outside `G`, evaluation on `C'` is a nonzero functional. Hence

```text
A_x={c in A:c(x)=u(x)}
```

is empty or an affine flat of direction dimension `s-1`. The induction
hypothesis bounds the number of listed words in every nonempty `A_x` by

```text
B_(s-1)=C(n-K+s-1,s-1)/C(w+s-1,s-1).
```

Double counting listed-word/agreement-coordinate pairs outside `G` gives

```text
|L_A(u,m)|(m-g)<=(n-z)B_(s-1).                         (2)
```

Put `b=z-g` and `q=K-s-z`. Both are nonnegative, and direct expansion gives

```text
(m-g)(n-K+s)-(n-z)(w+s)
  =b(n-K+s)+q(n-m)>=0.                                 (3)
```

Thus `(n-z)/(m-g)<=(n-K+s)/(w+s)`. Combining this with `(2)` and the exact
binomial ratio proves `(AS1)`.

## Generalized-weight compiler

Identify `A` with affine `s`-space using a basis of `C'`. At each coordinate
outside `G`, agreement with `u` is an affine hyperplane with nonzero normal
equal to the evaluation functional on `C'`. There are `d_s=n-z` such active
coordinates, and every listed point lies on at least

```text
h=m-g=d_s-t+b                                             (4)
```

active hyperplanes.

Suppose `r` independent incident normals span `W`. The active coordinates
whose normals lie in `W` are common zeros of the `(s-r)`-dimensional subcode
`W^perp`. By the definition of generalized weights, at most

```text
d_s-d_(s-r)
```

active normals lie in `W`. Therefore at the next step there are at least

```text
h-(d_s-d_(s-r))=d_(s-r)-t+b
```

choices for an independent incident normal. Every listed point is incident
with at least

```text
product_(j=1)^s(d_j-t+b)/s!
```

unordered independent bases. Any independent `s` hyperplanes have at most
one common point, while the active coordinates contain only `C(d_s,s)`
possible bases. Double counting proves `(AS3)`.

Finally, a `j`-dimensional polynomial subspace of degree below `K` has at
most `K-j` common zeros, by the same locator-division argument as `(1)`.
Consequently `d_j>=n-K+j`, and subtracting `t=n-m` gives `(AS4)`. QED.

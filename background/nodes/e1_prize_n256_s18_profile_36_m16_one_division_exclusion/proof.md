# Proof

Write the positive-half integer autocorrelation as `(A_d)_(1<=d<64)` and put

```text
E=sum_d A_d^2,          L=sum_d |A_d|,
q=#{d:A_d is odd}.
```

The imported cofactor-16 product certificate leaves 967 exact `(E,q,L)`
chambers, all with `E<=89`.

## Exhaustive support branch

Cofactor 16 forces exact multiplicity four at `X=1` in the six-singleton
binary support polynomial `P`. In the once-divided branch, all exponents have
one parity. After translation write `P(X)=T(X^2)`. In characteristic two,
`T(X^2)=T(X)^2`, so `T` has exact multiplicity two. By definition of this
branch, the exponents of `T` contain both parities; a second division is
therefore unavailable.

Translation and an odd unit normalize the quotient support in `Z/64` to
contain `{0,1}`. Enumeration of all `binom(62,4)=557845` six-term supports
containing this pair finds 139,360 of exact multiplicity two. Affine
canonicalization and multiplication by two leave 9,080 orbits. Their
odd-chord weights are

```text
q=1:8, 2:14, 3:57, 4:9, 5:164, 6:94, 7:704, 8:354,
q=9:1768, 10:623, 11:2209, 12:465, 13:1360, 14:471, 15:780.    (1)
```

## Product and square-norm contractions

The imported exact product ledger uses the raw chord weights `W=63`, `Q=135`
and the proved inequality

```text
4L <= E+117.
```

It partitions all 3,685 candidate chambers into 967 live and 2,718 excluded
records using 295,256 exact rational comparisons.

Every singleton position in this branch is even. If all three heavy positions
are also even, the full nine-term polynomial is `F(X)=G(X^2)`. Its
degree-128 cyclotomic norm is the square of the degree-64 norm of `G`, because
`G(zeta_128)` lies in the index-two subfield of `Q(zeta_256)`. It therefore
cannot equal `16p` for odd prime `p`. For each support orbit this removes
exactly

```text
binom(58,3)=30856
```

of the `binom(122,3)=295240` heavy triples before sign enumeration.

## Dual complete radius search

On a parity-even lag, an odd value of `A_d/2` costs at least four units of
energy. Thus a vector in a live chamber has syndrome radius at most
`floor((E-q)/4)`. The primary engine scans every remaining heavy-position
triple and all 32 normalized singleton-sign assignments, then replays all
eight heavy-sign choices exactly. A rigorous early cap multiplies outward
fixed-root upper intervals from smallest to largest; every unevaluated
squared factor is bounded by `144*2^96=9*2^100`. It can certify only the
below side. All other vectors receive the original complete 64-root interval.

The audit reverses both outer orders, constructs its chord columns separately,
directly rebuilds the full autocorrelation for every low-energy survivor, and
uses the original complete fixed-root interval without the early cap. It
matches every proof-relevant primary count on each of the 9,080 orbits:

```text
affine orbits:                         9080
singleton sign assignments:          290560
raw heavy-position triples:       2680779200
post-square sign-distance tests: 76819415040
unique radius triples:            73175732492
exact heavy-sign tests:          585405859936
low-energy vectors:                6762240640
product-live vectors:              1816625504.                         (2)
```

## Certified norm separation

The fixed table contains all 64 odd roots and 128 positions, scaled by
`2^48`. Its independent 256-bit Arb audit proves all 16,384 real and imaginary
component errors strictly below one. Every vector has coefficient `L1` norm
12, so integer lower and upper squared-modulus bounds use component error 12
and are multiplied over all 64 roots.

The exact scaled cofactor-16 endpoints are

```text
16 B_P 2^128
and
16 ((B_P+1)2^128-1).
```

Of the 1,816,625,504 product-live vectors, 1,816,625,308 have upper norm bound
below the first endpoint and 196 have lower norm bound above the second. None
is unresolved. Every retained high-side state is independently reconstructed
by the verifier, including its autocorrelation chamber and lower interval.
The reverse full-interval audit gives the same split on every support orbit.
Hence no vector in the once-divided branch has norm `16p` in the prize row.

```text
fixed below:       1816625308
fixed above:              196
fixed unresolved:           0
```

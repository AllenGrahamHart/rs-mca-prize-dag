# Proof

Every monomial of `I` is indexed by a collection of primitive relations with
pairwise disjoint supports. If the collection has size `m`, its union has at
least `m w_0` coordinates. Hence `m<=K=floor(N/w_0)`.

For fixed `m`, discard the disjointness condition. The sum of the activities
over all unordered sets of `m` distinct primitives is at most `P^m/m!`:
the expansion of `P^m` contains every such product in all `m!` orders and has
only additional nonnegative terms from repeated primitives. Summing over the
possible matching sizes gives

```text
I<=sum_(m=0)^K P^m/m!=Exp_K(P).
```

There is a sharper bound. Form the compatibility graph whose vertices are
primitive relations and whose edges join disjoint supports. Then `I` is its
weighted clique polynomial and its clique number is at most `K`.

If two positive-weight vertices `u,v` are nonadjacent, no clique contains
both. Holding all other weights fixed, write

```text
I=A+z(u)B_u+z(v)B_v.
```

If `B_u>=B_v`, transfer all of `z(v)` to `u`; otherwise transfer all of
`z(u)` to `v`. The total activity stays `P`, `I` does not decrease, and the
number of positive weights drops by one. Iteration leaves positive weight on
a clique of size `r<=K`. On that clique the polynomial is

```text
product_(i=1)^r (1+z_i).
```

Append `K-r` zero weights and apply AM-GM, using `sum_i z_i=P`, to obtain

```text
I<=(1+P/K)^K.
```

Finally, coefficientwise

```text
(1+P/K)^K
 =sum_(m=0)^K binom(K,m)P^m/K^m
 <=sum_(m=0)^K P^m/m!,
```

since `binom(K,m)m!<=K^m`. This proves all of `(MT1)`.

The inequality `Z<=I` is the primitive-decomposition theorem proved in
`dli_full_spectrum_polymer_majorant`, so `(MT1)` follows. Since `Exp_K` is
increasing on the nonnegative reals, so is `(1+x/K)^K`; hence `P<=W_full`
and the proved normalization `E_j=r_j Z_j` give `(MT2)`.

It remains to justify the production caps. The official field characteristic
is greater than `2ell` at every level. The Newton short-window theorem
therefore excludes all support weights at most `2ell`. At `ell=1`, the
separate complete ambient certificates also exclude weights `3` and `4`, so
the first possible support has weight `5`. At `ell=2`, the exact norm-gcd
certificate additionally excludes weight `5`, so the first possible support
there has weight `6`. This proves the four minimum weights in `(MT3)`.
Substitution into `N=256ell` gives `51`, `85`, and `113`;
for `ell>=8`,

```text
256ell/(2ell+1)<128,
```

so the integer cap is at most `127`.

Finally multiply `(MT2)` over the production levels. As in the full-spectrum
majorant,

```text
product_j r_j=(q/2^256)^t.
```

Taking logarithms shows that `(MT4)` makes the product at most `2^100`, which
proves the final implication.

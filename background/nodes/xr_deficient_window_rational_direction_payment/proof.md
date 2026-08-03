# Proof

## Pointwise rational direction

For `l>=k`, the coefficient `u_l` is the inverse Fourier coefficient
of `e=u-f`, because `f` has degree `<k`:

```text
u_l = n^(-1) sum_{x in H} e(x)x^(-l),
v_l = n^(-1) sum_{x in H} e'(x)x^(-l).
```

The Pade relation in column `i`, `0<=i<=r'`, is therefore

```text
0 = sum_x x^(i+1) (A(x)e(x)+B(x)e'(x)).                         (1)
```

The errors vanish on the full core. Their joint support has exactly
`r'` points, while `(1)` gives its moments of orders `0,...,r'`.
The corresponding `(r'+1) x r'` Vandermonde matrix has full column
rank. Hence every coefficient in `(1)` vanishes pointwise, proving
`(RD)`.

## Exact forced roots

Let `c=dim K_d`. For each `x notin G_d`, syzygies vanishing in both
components at `x` form a proper linear subspace of `K_d`, of size at
most `q^(c-1)`. There are at most `n` such subspaces. Since `q>n`,
their union has size strictly below `q^c`, so a syzygy lies in none of
them. Its common roots on `H` are exactly `G_d`.

Every component of every syzygy vanishes on the distinct points of
`G_d`, so it is divisible by their monic locator. After division both
components have degree `<d-g_d`; the ambient space has dimension
`2(d-g_d)`. This proves `(FR)`.

## Outside-`G_d` occupancy payment

Choose the syzygy whose common-root set is exactly `G_d`. Outside
`G_d`, `(RD)` says that the unique projective slope cancelling the
nonzero error pair is the fixed rational direction

```text
phi(x)=[B(x):A(x)].
```

Let `N_d^out` count the pairs having a selected ray with an off-core
agreement point outside `G_d`. For each such pair choose one such ray
and one such point. Its slope belongs to

```text
phi(H\G_d),
```

a set of at most `n-g_d` projective slopes. Assign one such slope to
each pair. Item 7 of
`notes/BAND_LANE_DEFINITIONS.md` selects one global first-match
exact-`A` ray at each slope, so two pairs assigned the same slope are
subordinate to the same selected ray. The high-depth interaction strip
in `xr_band_ledger_theorems` then gives `d+d<=h-1` for two distinct
generic-branch pairs on that ray, contrary to `d>=ceil(h/2)`. Thus the
assignment is injective, and

```text
N_d^out<=|phi(H\G_d)|<=n-g_d.                  (3)
```

The complementary pairs counted by `N_d^G` have every selected
off-core point in `G_d`. Each selected live ray has exactly `h-d`
off-core points. A counted pair has at least two selected slopes, and
the corresponding off-core blocks are disjoint: a common point would
annul the two distinct scalar combinations of the same error pair and
would therefore lie in the joint core. Hence `N_d^G>0` implies

```text
g_d>=2(h-d).                                  (4)
```

Finally, a nonzero nonproportional pair of polynomials of degree `<d`
has common-gcd degree at most `d-2`. If
`d<=floor((2h+1)/3)`, then `d-2<2(h-d)`, so the payment applies. QED.

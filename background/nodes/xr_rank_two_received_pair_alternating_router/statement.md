# XR rank-two received-pair alternating router

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_higher_rank_uniform_split_pencil_reduction`,
  `xr_rank_two_three_anchor_grs3_factorization`,
  `xr_rank_two_four_anchor_quadric_centroid_atlas`

For a polynomial `U` representing a normalized dual word on the active union
`X`, and a function `f:X->F`, define

```text
<U,f>_X=sum_(x in X) U(x)f(x)/Lambda'_X(x).          (RP1)
```

Let `b,q` be the two punctured received directions in the uniform
split-pencil normalization. If

```text
lambda_i=(c_iF+d_iG)/Lambda'_X
```

is any active row with slope `gamma_i`, then actual agreement of its selected
block forces

```text
c_i<F,b>_X+d_i<G,b>_X
 +gamma_i c_i<F,q>_X+gamma_i d_i<G,q>_X=0.          (RP2)
```

Equivalently, the interaction vector

```text
theta=(<F,b>_X,<G,b>_X,<F,q>_X,<G,q>_X)             (RP3)
```

annihilates every Segre coefficient column `v_i`.

This gives an exact branch router.

1. In the three-anchor branch, use the slope-linear basis from the
   dual-`GRS_3` factorization:

   ```text
   lambda_i=s_i(P+gamma_i Q)/Lambda'_X.
   ```

   Since there are at least four distinct active slopes, `(RP2)` is
   equivalent to

   ```text
   <P,b>_X=0,
   <Q,q>_X=0,
   <P,q>_X+<Q,b>_X=0.                                (RP4)
   ```

   Thus the interaction matrix is alternating:

   ```text
   ((<P,b>,<P,q>),(<Q,b>,<Q,q>))=((0,eta),(-eta,0)). (RP5)
   ```

   The branch splits further into `eta=0` and the perfect-pairing branch
   `eta!=0`.

2. In the four-anchor branch, the coefficient columns span `F^4`, so

   ```text
   <F,b>_X=<G,b>_X=<F,q>_X=<G,q>_X=0.                (RP6)
   ```

Conversely, `(RP4)` or `(RP6)` makes the parity pairing
`<lambda_i,b+gamma_i q>_X` vanish for every row in the corresponding
coefficient atlas. This converse is only for the selected trade-row parity
conditions. It does not reconstruct the full `h` parity checks of an actual
agreement block, count compatible support extensions, choose a first Maxwell
core, or pay the cross-core slope aggregate.

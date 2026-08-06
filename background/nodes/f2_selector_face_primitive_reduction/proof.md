# Proof

For `x in F_v`, let `E_x` be its antipodal selector. The selector transport
shows that all `E_x` have the same first `2R` power sums and hence, by
Newton identities, the same top `2R` locator coefficients.

For every fixed coordinate, all selectors contain the same one of its two
antipodal roots. Their product is the monic squarefree polynomial `G_v`.
Writing

```text
L_x = G_v Q_x
```

therefore maps the fiber injectively to monic squarefree degree-`m-c`
locators on `D_v=mu_(2m)\Z(G_v)`. Multiplication by a fixed monic degree-`c`
polynomial is triangular with diagonal one on the top coefficients. Hence
the common top `2R` coefficients of `L_x` determine, and are equivalent to,
the top `s=min(2R,m-c)` coefficients of `Q_x`. This is the affine space
`A_v`, of codimension `s`. If `m-c<2R`, all nonleading coefficients of
`Q_x` are fixed, so at most one monic polynomial occurs and `|F_v|=1`.

Assume now `m-c>=2R`. For each nonfixed coordinate, both selector choices
occur somewhere in `F_v`; neither root of that antipodal pair is therefore
common to all `Q_x`. The unchosen root opposite a fixed coordinate is absent
from every `Q_x`, while its chosen root was removed with `G_v`. Thus the
sets of roots of all `Q_x` have empty intersection. Since the full locator
intersection contains the `Q_x`, a root common to the full intersection
would be common to the selector subfamily, which is impossible. This proves
gcd-triviality.

Every `Q_x` is antipodal-free because it is a subset of `E_x`. Every
nontrivial subgroup of the cyclic `2`-group `mu_(2m)` contains `-1`, so a
nonempty support invariant under such a subgroup would equal its negative.
That contradicts antipodal-freeness. Hence all `Q_x` are aperiodic and lie
in the primitive part bounded by `(FACE-2)`.

Finally, with `j=m-c`, `|D_v|=2m-c`, and `s=2R`,

```text
binom(2m-c,m-c) / q^(2R)
  <= 2^(2m-c) / q^(2R)
  = 2^(2 Delta-c)
  <= 2^(2 max(Delta,0)).
```

Substitution in `(FACE-2)` proves `(FACE-3)`. The asymptotic conclusions are
immediate, and the weighted-mass conclusion is exactly the upper half of
`f2_weighted_mass_max_fiber_sandwich`. QED.

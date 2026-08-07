# Rate-half FPC5 `M=4,t=2` payment

- **status:** TARGET
- **consumer:** `l1_fpc5_m4_t2_payment`

Fix one admissible maximal rate-half source with `M=4`. Count all non-planted
FPC5 contributors touching exactly two full petals. For a cell

```text
d=ell+s,       0<=s<ell,
```

the proved petal-equation envelope has dimension `2s+2`; the exact cell also
imposes its background roots and exact nonagreements. The formal locator
codimension is at least two. At equality, official arithmetic forces

```text
5ell=k+4,       b=r=s=ell-3,       d=2ell-3,
```

and the full-background guard cuts the pair and locator dimensions to
`ell-1`.

The uniform guarded-codimension theorem now covers every fixed exact
background set `R`, not only that endpoint. If `r=|R|`, the threshold gives
`r>=s`, and the guarded locator codimension is at least `ell-1`; it is exactly
`ell-1` when `r=s` and at least `ell` when `r>=s+1`. Aggregated without
choosing `R`, the remaining locus is one joint split-pair problem:

```text
F split on C,       W_F has at least s roots on B.      (RH0)
```

The exact set `R=Z_B(W_F)` is unique, but an independent sum over all
`binom(b,r)` possible sets is not a polynomial payment.

The proved sharp projective-flat descriptor now identifies this endpoint
exactly. For each fixed touched pair, contributors inject into

```text
P(V_F) intersect D_(2ell-3)(C),
|C|=5ell-5,       dim P(V_F)=ell-2,
affine codimension=ell-1.                              (RH1)
```

The numerator is reconstructed uniquely, and primitive, untouched-petal,
and first-owner conditions remain explicit filters. A companion theorem
proves the entire locator flat has maximal common gcd `1`, so no flat-wide
common-divisor branch remains. This is distinct from the candidate-wise
primitive filter `gcd(F,W_F)=1`. Since `n=2^41` and `2ell-3` is odd, the
proper pure multiplicative quotient-pullback stratum is also empty. Partial
quotient tails and reciprocal/dihedral classes remain. Because the projective
dimension grows with `ell`, the upstream fixed-dimensional split-flat bound
does not close (RH1).

Prove one disjoint aggregate payment of the remaining root-rich split-pair
locus over the six touched pairs and all defect/background cells in this
fixed source. Internal tangent, quotient, background-root, and
contributor-dependent recharts must have explicit first owners. No sum over
maximal source layouts is needed:
`l1_general_first_layout_domination` makes the fixed-layout payment global
after adding at most four anchors.

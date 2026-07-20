# `A=1` core-one distance-three external split-design saturation

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_pair_lagrange_normal_form`

Retain the distance-three pair-Lagrange chart. Put

```text
S=R_A union T,       |S|=2e+3,
D_res has size 8e+7.                                  (EDS1)
```

Let `P_X` be the squarefree saturated-row polynomial in the corrected
exceptional-only system. It has degree `8e+6`, so it omits one residual
domain point. That point is a unique

```text
x_0 in D_res\S.                                       (EDS2)
```

Let `Z_ext` be the `3e` external slopes and let `G_z` be the monic
degree-`2e+1` external locator at `z`. Then

```text
#{z in Z_ext:x in roots(G_z)}=
  e,       x in D_res\(S union {x_0}),
  0,       x=x_0.                                     (EDS3)
```

Thus the external incidence graph is exactly biregular:

```text
3e slope vertices of degree 2e+1,
6e+3 domain vertices of degree e.                     (EDS4)
```

If

```text
C(X)=product_(x in D_res\(S union {x_0}))(X-x),
```

then the complete external locator product is the exact power

```text
product_(z in Z_ext) G_z(X)=C(X)^e.                   (EDS5)
```

Up to the fixed monic normalization,

```text
P_X(X)=A(X)B_T(X)C(X).                                (EDS6)
```

This removes the `e` units of aggregate incidence slack left by the previous
router: they are all concentrated at the single omitted row `x_0`. It does
not classify the individual blocks of the biregular design or prove that a
pair-Lagrange generator realizing the design satisfies the lower Hankel and
reciprocal equations.

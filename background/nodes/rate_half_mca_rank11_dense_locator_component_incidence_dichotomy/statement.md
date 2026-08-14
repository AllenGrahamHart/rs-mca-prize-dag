# Rank-eleven dense-locator component-incidence dichotomy

- **status:** PROVED
- **scope:** the complete full-rank residual family after removal of the
  eighteen fixed dense-pair slopes

Let `q(Z)` be the monic degree-18 locator of the dense anchor slopes. For
every remaining record put

```text
R_gamma=(h_gamma'-a_0'-gamma b_0')/q(gamma) in V'.
```

The division is defined because slopes are distinct, and the normalized
vectors still span the fixed ten-dimensional `V'`. At coordinate `x`, rich
agreement is

```text
(a_0'-r_0')(x)+Z(b_0'-r_1')(x)+q(Z)R(x)=0.          (1)
```

Thus each coordinate gives a hypersurface of bidegree at most `(18,1)` in
`P^1_Z x P^10_R`. For any eleven-coordinate tuple, multihomogeneous
isolated-point Bezout bounds the isolated solutions of (1), counted with
multiplicity, by

```text
18*11=198.                                           (2)
```

Uniformly for every shortening `10<=K'<=1048576`, put

```text
n'=1048576+K',        m'=67472+K'.
```

The complete isolated-incidence contribution, normalized by the number of
eleven-subsets in one rich support, is at most

```text
A_iso(K')=ceil(198*C(n',11)/C(m',11))
          <=A_iso(10)=2526815879272440.              (3)
```

An unsafe original line leaves at least

```text
N_min=274980728111260126
```

non-dense post-near residual records after the exact near charge and the
eighteen anchors. Hence at least `990810934` parts per billion of all pairs

```text
(record gamma, eleven-subset T of its support)
```

lie on a positive-dimensional component through that rich point.

These component incidences split exactly into two lanes. If evaluation of
`V'` on `T` has rank ten, the component is one affine-owner clone. If its
rank is at most nine, the point lies on a positive-dimensional kernel fiber,
vertical at one slope or slope-dominating and covered by kernel shortening.
At least one lane carries `495405467` parts per billion of all incidences.

This is an aggregate abundance theorem, not an aggregate payment: one
record may contribute many component incidences and components may overlap.

## Falsifier

A remaining slope at a root of `q`; loss of membership or span under
nonzero scalar normalization; slope degree above 18 in (1); more than 198
isolated solutions for one eleven-tuple; a larger shortened endpoint than
`K'=10`; an unsafe residual below `N_min`; or a positive-dimensional
component through a non-dense rich point that is neither full-rank affine
owner nor rank-deficient kernel fiber.

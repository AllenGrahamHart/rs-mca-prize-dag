# `A=1` distance-three generic Schur-square saturation route fence

- **status:** PROVED
- **closure:** explicit arbitrary-size construction
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quadratic_locator_rank_gate`

The generic pair-locator branch does not force the quadratic-product bound
in the dependency to be sharp. For every `e>=3` and every odd
characteristic, some finite extension contains squarefree split coprime
polynomials

```text
deg A=2e,       deg B=3,
A=product_(i=1)^e D_i,       deg D_i=2,              (GSSF1)
```

such that

```text
dim span{D_1,...,D_e}=3,                              (GSSF2)
```

but, for

```text
U_0=A,       U_i=B A/D_i,       V=span{U_0,...,U_e},
```

one has

```text
dim(VV)<=3e<3e+1.                                    (GSSF3)
```

The construction uses pair factors from distinct fibers of the cubic
rational map

```text
B/R,       B=X(X-1)(X+1),       R=X^2+1.             (GSSF4)
```

Thus even arbitrarily large rank-three pair packets may carry one hidden
Schur-square defect. Any exclusion of the official generic distance-three
branch must use the calibrated external split design, incidence, boundary,
or residue data beyond pair-locator rank and the abstract `3e+1` cap.

This is a route fence, not an external-design counterexample.

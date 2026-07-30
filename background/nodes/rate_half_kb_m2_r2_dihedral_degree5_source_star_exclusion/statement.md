# KoalaBear m2 r2 dihedral degree-five source-star exclusion

- **status:** PROVED
- **scope:** the `n=5` factor case inside the residual actual
  `(m,r,delta)=(2,2,4)` row
- **dependencies:** `rate_half_kb_m2_r2_dihedral_outer_factor_reduction`,
  `rate_half_kb_m2_v4_outer_recurrence_router`, and the complete-source
  pullback identity
- **consumer:** `rate_half_band_closure`

The `n=5` Dickson/Chebyshev pole profile has one generic order-five outer
pole and one simple outer pole at the totally ramified value. Let `z_0` and
`y_0` be the unique source-pole values in the two reflection quotient
coordinates above that common value. The degree-two outer component has

```text
Z=z_0  =>  Y=y_0
```

on both normalization sheets.

The original quadratic endpoint map `h` has two distinct unramified source
poles above each of `z_0,y_0`. The source reduction supplies a quadratic
map `psi(X)=W` and the divisor identity

```text
div(B)=psi^*(sum_i [alpha_i]).
```

For either endpoint source pole `w` above `z_0`, put
`D_w=psi^*[w]`. Every source-parameter point in this degree-two divisor
makes the source quadratic `H(T,X)` have exactly the same two distinct
roots: the pair `h^(-1)(y_0)`. Thus all of `D_w` contributes weight two to
one matching source-star vertex. The two endpoint poles above `z_0`
contribute total weight four to that vertex. No identification of `D_w`
with the coordinate form carrying the same label is used.

The complete-source defect theorem gives `w_v<=3` for every star vertex.
Therefore the `n=5` factor case is empty, and the full-V4 row is reduced to

```text
n in {2,3,6}.                                       (KBM5-1)
```

No one of these three degrees is deleted. This proves no carrier/data/slope
owner, payment, `u=2` close, adjacent certificate, or Prize row.

## Falsifier

An `n=5` totally ramified pole whose two reflection quotients do not each
have a singleton source value, a failure of the two unramified `h` fibers,
or a source-star accounting with weight below four at the matching vertex.

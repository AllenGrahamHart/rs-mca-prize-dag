# KoalaBear m2 r4 coordinate negative one-loop 442 outside binary-sextic invariance compiler

- **status:** PROVED
- **scope:** every complete packet in the live rank-six one-loop `(4,4,2)`
  common orbit and all three outside skeletons
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_explicit_involution_compiler`,
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_template_orbit_classifier`
- **consumer:** `rate_half_band_closure`

Choose the outside record whose product equals the forced singleton mate
`m`.  Let the six remaining distinct products be `u_1,...,u_6` and form

```text
H(X,Z)=product_(j=1)^6 (X-u_j Z).                 (KB41BI-1)
```

For the explicit involution matrix

```text
M=[[Alpha,Beta],[Gamma,-Alpha]],
```

at least one of the fifteen residual perfect matchings passes the
paired-product gate if and only if there is a nonzero scalar `lambda` such
that

```text
H(Alpha X+Beta Z, Gamma X-Alpha Z)=lambda H(X,Z). (KB41BI-2)
```

Thus one binary-sextic invariance test replaces fifteen matching tests for
each forced record.

Quotienting the signed forced-record cells by outside representative changes
and valid unsigned skeleton automorphisms gives exactly

```text
S0: 6 invariant cells from  8*7= 56 raw forced cells;
S1: 10 invariant cells from 16*7=112 raw forced cells;
S2: 4 invariant cells from  1*7=  7 raw forced cells. (KB41BI-3)
```

Hence the accepted product frontier has twenty invariant-form cells per
common sign row and eighty over the four sextic common rows.  The former
201/804 matching-template census remains a correct audit but is superseded
as a computation endpoint.

This theorem does not evaluate the eighty invariance cells, impose outside
sums or full interpolation, classify another common orbit, close the
coordinate orientation or a row, or prove either Prize result.

## Falsifier

A six-product residual set that has three involution pairs but fails
`(KB41BI-2)`, an invariant guarded residual set that does not split into
three pairs, or failure of the forced-cell orbit census `(KB41BI-3)`.

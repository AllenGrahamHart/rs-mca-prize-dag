# KoalaBear m2 r4 coordinate negative one-loop 442 outside sign-orbit classifier

- **status:** PROVED
- **scope:** the signed product cells of all three one-loop `(4,4,2)`
  outside skeletons `S0,S1,S2`, for each fixed common sign row
- **dependency:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_complete_edge_skeleton_classifier`
- **consumer:** `rate_half_band_closure`

Changing the signs of outside representatives `D,E,F` preserves the target
pairs and the unsigned skeleton.  Quotienting by these changes gives exactly
five signed outside cells:

```text
S0: two orbits, indexed by tau_0=alpha*beta*gamma in {+1,-1};
S1: two orbits, indexed by tau_1=alpha*beta*gamma*delta in {+1,-1};
S2: one orbit.                                        (KB41SG-1)
```

Here the singleton products are

```text
S0: alpha*CE, beta*CF, gamma*EF;
S1: alpha*CE, beta*CF, gamma*DE, delta*DF,
```

while every multiplicity-two edge already contributes its full signed pair.
Thus the raw `8+16+1=25` signed cells reduce to `2+2+1=5` per common sign
row.  With `7*15=105` forced-value/matching templates per signed cell, the
pre-automorphism template cap is `525` per common sign row and `2100` over
the four sextic common rows.

This theorem does not quotient by unsigned skeleton automorphisms, evaluate
any product template, impose outside sums or interpolation, classify another
common orbit, close the coordinate orientation or a row, or prove either
Prize result.

## Falsifier

Two sign assignments with the same displayed parity that are not connected
by outside representative changes, or assignments with opposite parity that
are connected.

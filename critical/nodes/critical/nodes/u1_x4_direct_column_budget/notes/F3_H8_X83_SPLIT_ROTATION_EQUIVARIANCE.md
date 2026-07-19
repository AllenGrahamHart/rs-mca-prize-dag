# F3 h=8 x83 split rotation equivariance

Status: PROVED STRUCTURAL EQUIVARIANCE + FINITE-FIELD REPLAY.

This packet tightens the h=8 support-orbit certifier interface.  The rotation
compiler already proves that the x83 full-zero condition is invariant under
root scaling.  Here we also record that the canonical x83 split into the two
h=8 trade sides commutes with that rotation, up to swapping the two sides.

## Statement

Let `R <= mu_64` be an x83 full-zero 16-support:

```text
L_R(X) = S_R(X)^2 - alpha^2,
```

where `S_R` is the forced monic degree-8 square root and `alpha != 0`.  For
`c in mu_64`, put `cR={cr:r in R}`.  Then

```text
L_{cR}(X) = (c^8 S_R(X/c))^2 - (c^8 alpha)^2.
```

Thus the forced square root for `cR` is

```text
S_{cR}(X) = c^8 S_R(X/c),
```

and the recovered fibers satisfy

```text
S_R(r)= alpha   <=>   S_{cR}(cr)= c^8 alpha,
S_R(r)=-alpha   <=>   S_{cR}(cr)=-c^8 alpha.
```

If the square-root routine chooses the opposite sign for `alpha`, the two sides
are swapped.  Therefore the canonical h=8 trade split is rotation-equivariant
up to side swap.

## Role in h=8

A future h=8 support-orbit certifier may safely:

1. canonicalize a support under exponent translation;
2. run the x83 obstruction/split classifier on the representative;
3. rotate the recovered split back to the original support.

This does not reduce the number of non-antipodal support orbits.  It only
proves that the already-banked rotation quotient is compatible with the
support-to-trade reduction, so orbit-level certificates will not lose the
canonical split data.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_x83_split_rotation_equivariance.py
```

Expected digest:

```text
H8_X83_SPLIT_ROTATION_EQUIVARIANCE_PASS
```

# XR rank-five extension-list reduction

- **status:** see `dag.json` (single source of truth)
- **consumers:** `xr_highcore_collision_count`, `xr_lowcore_spread_heart`
- **dependency:** `xr_rs_flat_nullity_basis_charge`

Use the rank-five RowC selector notation from the flat-nullity charge, so the
kernel slice has rank `a=4`.  Write

```text
g=|G|=k-4-u,       p=|P_0|=g-v,
E=D\P_0,           N=|E|=R+4+u+v.
```

There is a five-dimensional linear code `C_E` on `E`, containing the
four-dimensional punctured kernel code `K_E`, and a received word `U_E` with
the following properties.  Every selected slope supplies a codeword in
`C_E` that:

1. agrees with `U_E` in at least

   ```text
   m=4+h+u+v
   ```

   coordinates;
2. occupies a distinct coset of `K_E` in `C_E`; and
3. has an agreement set meeting that of any other selected codeword in at
   most

   ```text
   4+u+v       in the high-core application (P-A),
   3+u+v       in the low-core application (P-B).
   ```

The code `K_E` has exactly `v` zero coordinates.  After deleting them and
scaling coordinates, it is the evaluation of a four-dimensional subspace

```text
W subset F[X]_<4+u
```

with no common evaluation root.

In particular, when `u=v=0`, `W=F[X]_<4`.  The hardest base residual is
therefore a distinct-quotient-class received-word list in a one-dimensional
extension of a generalized Reed-Solomon code `GRS_4` of length `R+4`.  Its
agreement threshold is `4+h`, and its pairwise agreement cap is `4` for P-A
or `3` for P-B.

This is an exact reduction of the surviving selector family.  It is not a
list-size bound and does not change either XR critical status.

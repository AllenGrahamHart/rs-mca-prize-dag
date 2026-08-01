# KoalaBear m2 r4 coordinate negative zero-loop 433 complete-Vieta exclusion router

- **status:** PROVED
- **scope:** every product-complete negative zero-loop `(4,3,3)` packet over
  `F_(2130706433^6)` in the finite common atlas
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`,
  `rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_product_skeleton_router`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_bc_singleton_product_skeleton_router`
- **consumer:** `rate_half_band_closure`

Use the explicit field model

```text
E=F_p[X]/(X^6+X+6),       p=2130706433.             (KBZ433V-1)
```

The residue of `X` is primitive.  If `M=(p^6-1)/(p-1)` and
`g=X^1768759633`, then `g` is primitive and `g^M=3`.  Thus this model
realizes exactly the extension logarithms used by both product routers.

For a common packet, reconstruct

```text
p(kappa)=(n_0+n_1 kappa)/(d_0+d_1 kappa)=B_0/B_2
```

from three common product rows and reconstruct the quadratic `A_1` from
the five common sum rows.  An outside edge `{u,v}` with product `p=uv` has
the forced quotient label and squared sum condition

```text
kappa=(n_0-p d_0)/(p d_1-n_1),
(-A_1(kappa)/B_2(kappa))^2=kappa(u+v)^2.            (KBZ433V-2)
```

Exact evaluation of `(KBZ433V-2)` deletes:

```text
common cells [2,5,6,9]: Z0, Z1, Z4;
common cell 12:         Z4;
common cell 13:         Z1, Z3;
common cell 14:         Z1, Z3.                    (KBZ433V-3)
```

The first outside row already fails on all `6528` common-record/isolated-
product assignments in these lanes.  Their `384` positive-dimensional
Smith systems all force a target-square or product collision, so no free
guarded family is omitted.  Together with the two product routers, this
deletes all 32 common packets in the orbit `[2,5,6,9]`.

The exact residual product-complete frontier is

```text
cell 12: Z2,Z3;       cell 13: Z2;       cell 14: Z2. (KBZ433V-4)
```

Those four lanes contain unresolved multiplicative families.  This theorem
does not delete them, impose their colored quotient records, close the
coordinate orientation, close a Prize row, or prove either Prize result.

## Falsifier

A guarded complete-Vieta lift in a lane listed in `(KBZ433V-3)`, a free
collision-free product family in one of those lanes, or a complete packet
in `[2,5,6,9]`.

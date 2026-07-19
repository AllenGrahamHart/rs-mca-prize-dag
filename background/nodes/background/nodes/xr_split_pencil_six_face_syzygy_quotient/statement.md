# XR six-face Plucker-syzygy quotient

- **status:** see `dag.json` (single source of truth)
- **consumers:** `xr_highcore_collision_count`, `xr_lowcore_spread_heart`
- **dependencies:** `xr_grs_split_pencil_rank_certificate`,
  `xr_split_pencil_trade_rank_two_support_atlas`

Let `X` be a six-coordinate set in a coherent `GRS_4` split-pencil family.
Suppose `t>=4` of its five-faces

```text
S_i=X\{x_i}
```

occur in distinct selected agreement blocks with slopes `gamma_i`, and the
divided-difference denominators on those faces are nonzero. For `y in X`,
put

```text
mu_i(y)=(y-x_i)/Lambda'_X(y).                          (SQ1)
```

Thus `mu_i` is zero at `x_i`, is supported on `S_i`, and is the canonical
dual-cubic word on that face.

The coefficient vectors `c=(c_i)` for which

```text
sum_i c_i mu_i=0,
sum_i gamma_i c_i mu_i=0                               (SQ2)
```

form a vector space of dimension exactly

```text
t-3.                                                   (SQ3)
```

More explicitly, this space is the kernel of

```text
 B_X=(1; x_i; gamma_i; x_i gamma_i)_(i=1,...,t),       (SQ4)
```

and `rank B_X=3`. These are forced local Plucker syzygies: they follow from
the six-face fractional-linear color law and require no further global rank
defect.

Conversely, every rank-two dual trade from the support atlas with active
coordinate count `R=6` is one of these six-face syzygies. Let `L_face` be
the span in the parity stack's left kernel of all such local relations.
Modulo `L_face`, no rank-two class with `R=6` remains. Hence a nonzero
rank-two class in the quotient can only have one of the two nonlocal support
profiles

```text
(t,R;{z_i})=(4,7;{1,2,2,2}) or (4,8;{2,2,2,2}).       (SQ5)
```

This is an exact quotient of known local syzygies, not a proof that the two
remaining profiles are absent or paid. It does not promote either consumer.

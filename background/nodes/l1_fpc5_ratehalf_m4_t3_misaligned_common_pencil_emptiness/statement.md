# Rate-half FPC5 `M=4,t=3` misaligned common-pencil emptiness

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t3_split_slice_payment`

Suppose the three touched petal locators lie in one degree-`ell` pencil,

```text
L_i=P-z_i,       z_1,z_2,z_3 distinct,                (MP1)
```

but the normalized source labels `(0,1,lambda)` are not affine-aligned with
the fiber values:

```text
lambda!=(z_3-z_1)/(z_2-z_1).                         (MP2)
```

Then every guarded LS6 atom is empty.

More precisely, the complement multiplier has the unique form

```text
Etilde=A(P-z_0),       A!=0,                          (MP3)
```

with `z_0` distinct from `z_2,z_3`. For any unguarded LS6 solution, writing

```text
D Etilde=L_2L_3 Q+V,       deg Q,deg V<=s=ell-a,      (MP4)
```

one necessarily has

```text
V=-(z_0-z_2)(z_0-z_3)Q,
A D=Q(P+z_0-z_2-z_3),       deg Q=s>0.               (MP5)
```

Thus `Q` is a nonconstant common divisor of `D` and `V`, contradicting the
exact LS6 guard `gcd(D,V)=1`.

Combined with aligned common-pencil emptiness, every LS6 atom whose three
touched petal locators belong to one common pencil is empty, for arbitrary
distinct source labels.

## Scope

The theorem does not show that arbitrary petal locators lie in a common
pencil, exclude isolated periodic locators inside a non-pencil flat, or pay
the primitive and dihedral master-flat strata.

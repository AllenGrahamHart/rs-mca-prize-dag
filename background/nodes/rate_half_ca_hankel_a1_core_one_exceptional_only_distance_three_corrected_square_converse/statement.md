# `A=1` core-one distance-three corrected-square converse

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_mds_source_weight_reconstruction`

Retain the exact distance-three split design. Put

```text
P(z)=z P_cl(z),       deg P=4e+1,
P_X(X)=A(X)B(X)C(X),  deg P_X=8e+6,                  (CSC1)
```

where `P_cl` is the product of the `4e` ordinary supported slopes and `P_X`
is the product of all residual-domain points except the unique omitted row.

There are biforms `V,W,A_c,B_c` satisfying

```text
Q V+P_X W=P,
Q A_c+P_cl B_c=P_X,                                  (CSC2)
```

with the sharp interpolation bounds

```text
deg_z V<=3e+1,       deg_X V<=8e+5,
deg_X W<=r-1,
deg_X A_c<=6e+5,     deg_z A_c<=4e-1,
deg_z B_c<=e-1.                                      (CSC3)
```

They may be normalized uniquely by the first two degree bounds: `V` is the
coefficientwise interpolation of `P/Q(z;x)` over the roots of `P_X`, and
`A_c` is the coefficientwise interpolation of `P_X/Q(z;X)` over the roots
of `P_cl`.

Moreover there is a biform `K` such that the complete two-sided weld holds:

```text
W B_c-z=QK,
V B_c+z A_c=-P_XK.                                   (CSC4)
```

Thus the full active complement system is a consequence of the exact split
design. At the exceptional slope, `Q(0;X)=A(X)` divides `P_X`; applying the
already-proved exceptional factor descent to `(CSC2)--(CSC4)` reconstructs
the corrected complement square and all of its reciprocal, resultant,
Bezout, and triangular identities.

Consequently the distance-three branch has no independent complement,
weld, or corrected-reciprocal variables. The live content is construction
or exclusion of the exact pair-Lagrange external split design, together with
an original endpoint lift that is column-far and has no additional close
slopes. This theorem does not supply those two remaining properties.

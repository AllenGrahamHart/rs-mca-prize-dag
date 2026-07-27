# Mattarei affine coset-pair bound

- **status:** PROVED
- **closure:** peer-reviewed external theorem plus an in-repo transport proof
- **consumers:** `f3_h3_dsp8_nodal_cube_preimage_envelope`,
  `f3_h3_dsp8_antipodal_quotient_mass_payment`,
  `f3_h3_dsp8_global_overlap_cover_payment`

Let `p` be prime, let `K<=F_p^*` have order `m`, and put

```text
d=(p-1)/m.
```

Assume `d>=4` and `d^3>=4m`. For any two nonconstant,
nonproportional affine forms `L_1,L_2` over `F_p`,

```text
#{x in F_p:L_1(x) in K, L_2(x) in K}
 < C_M m^(2/3),       C_M=3*2^(-2/3).              (MAC1)
```

The slope relating `L_1` and `L_2` need not belong to `K`. Thus `(MAC1)`
applies both to the twisted quotient fiber

```text
#{z in H:1-t(1-z) in H}
```

for arbitrary `t notin {0,1}` and to the cube-preimage fiber

```text
#{theta in K:1+theta in K}.
```

At every official H3 row, the hypotheses hold for subgroup orders
`m in {n,3n}`. This is a pointwise prime-field theorem; it supplies no
multi-fiber, energy, extension-field, or smooth-trace estimate.


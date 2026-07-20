# Cubic-preimage affine coset-pair Stepanov bound

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_nodal_cube_preimage_envelope`
- **dependency:** `f3_h2_stepanov_inhouse`

Let

```text
n=2^s,       13<=s<=41,
p=1 (mod n), p>=n^2,
m in {n,3n}, m divides p-1,
K<=F_p^*,    |K|=m.
```

For any two nonconstant, nonproportional affine forms `L_1,L_2` over
`F_p`, one has

```text
#{x in F_p:L_1(x) in K, L_2(x) in K}
 <(51/16)m^(2/3).                                   (CPS1)
```

The statement includes the order-`3n` cube-preimage subgroup when
`p=1 (mod 3)`. It strengthens the earlier `<4n^(2/3)` one-fiber bound at
order `n`; it is still a pointwise affine-pair theorem and supplies no
multi-fiber or energy estimate.

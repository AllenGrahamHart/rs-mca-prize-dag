# Optimized one-fiber affine coset-pair Stepanov bound

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_nodal_trace_parameter_router`
- **dependency:** `f3_h2_stepanov_inhouse`

Let

```text
n=2^s,       13<=s<=41,
p=1 (mod n), p>=n^2,
H<=F_p^*,    |H|=n.
```

For any two nonconstant, nonproportional affine forms `L_1,L_2` over
`F_p`, one has

```text
#{x in F_p:L_1(x) in H, L_2(x) in H}<4n^(2/3).      (ACS1)
```

The same bound therefore holds for the intersection of any two additive
translates of multiplicative `H`-cosets. This is the optimized `T=1`
specialization of the proved in-house Stepanov construction. It improves the
older conservative `66n^(2/3)` affine-pair corollary at one fixed fiber; it
does not improve the multi-fiber rich-coset constant or any energy theorem.

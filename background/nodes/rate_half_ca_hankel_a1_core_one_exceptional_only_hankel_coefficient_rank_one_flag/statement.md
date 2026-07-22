# `A=1` exceptional-only Hankel coefficient rank-one flag

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_coefficient_biisotropic_plane`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_kernel_plane_transversality`

Retain `W_q=span{q_0,...,q_e}` and the shifted exceptional locator
`v=Xq_0`. Put

```text
H_q=W_q+span{v}.                                     (HRF1)
```

Then

```text
dim H_q=e+2,                                         (HRF2)
W_q^(perp M_0)=W_q^(perp M_1)=H_q.                  (HRF3)
```

The two Hankel forms restrict to the exact rank profile

```text
M_0|_(H_q x H_q)=0,
rank(M_1|_(H_q x H_q))=1,
rad(M_1|_(H_q x H_q))=W_q,                          (HRF4)
```

and the sole nonzero Gram entry is the already-pinned scalar
`v^TM_1v`. Thus the size-one regular Kronecker block is represented in the
original coefficient coordinates by the quotient line `H_q/W_q`; no basis
change or extra regular-block variable is needed. This does not yet classify
`W_q` or exclude an endpoint profile.

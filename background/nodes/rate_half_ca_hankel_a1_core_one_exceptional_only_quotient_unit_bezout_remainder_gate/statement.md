# `A=1` exceptional quotient unit Bezout-remainder gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_unit_triangular_affine_reconstruction`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_reciprocal_bezout_normalization`

Retain the triangular reconstruction notation. The exact Bezout identity is

```text
l_0P_cl+f_0a_minus=1,       f_0=E q_bar.             (QBR1)
```

At stage `0<=k<r`, perform the single Euclidean division

```text
C_k^0=f_0d_k+r_k,       deg r_k<deg f_0=e.           (QBR2)
```

Then the canonical correction residue and the next quotient coefficient are
exactly

```text
rho_k=-r_k,
s_k=d_k+a_minus r_k.                                 (QBR3)
```

Consequently the stage survives if and only if

```text
deg r_k<=1.                                          (QBR4)
```

When it survives, the coefficients of the two correction polynomials are
the unique scalars satisfying `-r_k=t a_k+b_k`. Thus the endpoint recurrence
requires no modular inversion and no second exact division. A complete
packet still has to pass all `r` remainder gates and the final unit,
degree-box, recovered-complement, and Hankel checks.

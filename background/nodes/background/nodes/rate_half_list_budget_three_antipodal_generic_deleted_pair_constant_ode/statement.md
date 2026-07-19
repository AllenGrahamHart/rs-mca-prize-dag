# Budget-three antipodal generic deleted-pair constant ODE

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_even_factorization`,
  `rate_half_list_budget_three_antipodal_reverse_residual_stratification`

Retain a complete canonical survivor on the maximal generic deleted-pair
stratum. Thus `d=16M`, `r=4M-1`, `v=2M-2`, and the deleted roots are two
distinct antipodal pairs. In the original coordinate put `x=Y^2`. There are
polynomials

```text
D(Y)=D_0(x),       U(Y)=Y U_0(x),       V(Y)=V_0(x),             (COD1)
deg D_0=2,         deg U_0=2M-1,        deg V_0=M-1,
```

where `D_0,U_0` are monic and `V_0` is nonzero. For distinct nonzero
`lambda,mu` in the base field, the norm equation becomes

```text
D_0(x)(xU_0(x)^2+lambda V_0(x)^2)
      (xU_0(x)^2+mu     V_0(x)^2)=x^(8M)-1.           (COD2)
```

There is a nonzero scalar `kappa` such that the exact constant-forcing ODE

```text
(16M-4)D_0U_0-2xD_0'U_0-8xD_0U_0'=kappa              (COD3)
```

holds. In particular, if

```text
D_0=d_0+d_1x+x^2,       U_0=sum_(j=0)^(2M-1)u_jx^j,  (COD4)
```

and coefficients outside the printed range are zero, then

```text
d_0(16M-4-8j)u_j
 +d_1(16M+2-8j)u_(j-1)
 +(16M+8-8j)u_(j-2)=kappa 1_(j=0).                   (COD5)
```

Thus `u_1,...,u_(2M-1)` are determined successively by `u_0`, and polynomial
termination is the single exact condition

```text
d_1u_(2M-1)+4u_(2M-2)=0.                             (COD6)
```

For a fixed `D_0`, there is at most one monic `U_0` that can satisfy
`(COD3)`. Moreover

```text
kappa=(16M-4)d_0u_0!=0.                              (COD7)
```

Consequently `U` has a simple root at zero, all its other roots are simple,
and no root of `U` is a root of `D`. The zero root is exactly the one
exceptional root allowed by the generic linear residual.

This theorem does not classify solutions of `(COD2)--(COD3)`, determine
`V_0`, or exclude the remaining split quadratic field branch.

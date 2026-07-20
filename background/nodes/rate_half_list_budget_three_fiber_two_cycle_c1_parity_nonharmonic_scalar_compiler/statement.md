# Budget-three fiber-two c=1 parity nonharmonic scalar compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c1_parity_mobius_router`,
  `rate_half_list_budget_three_fiber_two_cycle_c1_parity_harmonic_exclusion`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_even_factorization`,
  `rate_half_list_budget_three_maximal_field_degree_collapse`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_ode`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_coefficient_legendre_collapse`

Retain the normalized generic `c=1` chamber whose denominator has two
antipodal root pairs. Put

```text
M=2^36,       L=8M=2^39,       q_field=p^2,
p=1 mod 2L,       r^(4L)=1,       t=r^4!=1.          (CNS1)
```

The denominator, canonical square-pencil coefficients, and unordered outer
ratio all descend to `F_p`. The source lift `r` need not descend and is not
used as a field assumption. In the original half-degree coordinate,

```text
D_0=(x-1)(x-t),       deg U_0=2M-1,
(16M-4)D_0U_0-2xD_0'U_0-8xD_0U_0'=kappa!=0.         (CNS2)
```

For fixed `D_0`, at most one monic `U_0` passes `(CNS2)`. Define

```text
Q=(x^L-1)/D_0,       A=xU_0^2,       R=Q-A^2,
R=AS+T,       deg T<deg A.                            (CNS3)
```

Take the six cross ratios `z_Xj`, for `X in {R,P}` and `j in {0,1,2}`, from
the parity Mobius router, and put

```text
y_Xj=tau(z_Xj)=4((z_Xj+1)/(z_Xj-1))^2-2.             (CNS4)
```

The complete square pencil and completion-root matching exist if and only if
at least one of these six role-labelled branches passes all of

```text
y:=y_Xj in F_p\{2,-2},
y_0=y,       y_(m+1)=y_m^2-2,       y_39=2,           (CNS5)

deg S=2M-2,       S^2=(y+2)T,                         (CNS6)

q_out^2-yq_out+1=0,
T/q_out=W^4,       W!=0,       deg W=M-1.             (CNS7)
```

Both roots in `(CNS7)` lie in `mu_L\{1,-1}` and in `F_p`. The fourth-power
verdict is independent of the reciprocal-root choice. Thus neither an outer
ratio nor a source-lift descent assertion is a search variable.

There are two exact first-rejection gates. Define

```text
H_n(t)=[z^n]((1-z)(1-tz))^(-1/2),       H=H_(4M-1)(t).
```

Every accepted branch satisfies

```text
4tH^2+y+2=0.                                           (CNS8)
```

If

```text
P_aux=2L+kappa x^2U_0^3,                              (CNS9)
```

then it also satisfies

```text
W divides P_aux,       S divides P_aux^2,
deg gcd(S,P_aux)>=M-1=2^36-1.                         (CNS10)
```

This is a coverage-equivalent compiler through the six scalar,
twisted-fourth-power, constant, and gcd gates. It does not prove uniform
rejection, provide a compressed official-degree implementation, cover the
nonparity `c=1` chamber, or authorize a large computation.


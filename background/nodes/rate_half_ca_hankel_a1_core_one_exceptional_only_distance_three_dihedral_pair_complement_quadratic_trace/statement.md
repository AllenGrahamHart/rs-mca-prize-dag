# `A=1` distance-three dihedral pair-complement quadratic trace

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_dihedral_quotient_external_product_ledger`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_pair_lagrange_normal_form`

Let

```text
P_Z(z)=product_(gamma external)(z-gamma)
```

be the monic degree-`3e` external-slope locator. For every nonexceptional
two-active-row orbit `O={x,tau(x)}` with quotient coordinate `u`, the two row
polynomials `Q(z;x),Q(z;tau(x))` have disjoint degree-`e` root sets. Hence

```text
K_u(z)=P_Z(z)/[Q(z;x)Q(z;tau(x))]                   (PCT1)
```

is a split squarefree polynomial of degree `e`, up to its nonzero leading
scalar.

Let `u_1,...,u_e` be the exceptional-pair orbit coordinates, let
`I(z)=product_i(z-xi_i)`, and put

```text
mu_i=P_Z(xi_i)/lambda_i^2,
M_j(z)=sum_i mu_i u_i^j L_i(z),       j=0,1,2.      (PCT2)
```

The four polynomials `I,M_0,M_1,M_2` are linearly independent. If
`a_u=[z^e]K_u`, then

```text
K_u(z)=a_u I(z)
       +chi(u)[u^2M_0(z)-2uM_1(z)+M_2(z)],          (PCT3)
```

where

```text
chi_-(u)=-1/[E(u)^2 product_(t in T)(u-t^2)]        (antipodal),

chi_c(u)=1/[c^(e-1)E(u)^2
             product_(t in T)(c+t^2-tu)]            (constant product).
                                                               (PCT4)
```

Thus the projective classes `[K_u]` lie in one `P^3`. In coordinates

```text
[a_u : b_0 : b_1 : b_2]
 =[a_u : chi(u)u^2 : -2chi(u)u : chi(u)],
```

they lie on the quadric cone

```text
b_1^2=4b_0b_2.                                      (PCT5)
```

Distinct orbit coordinates give distinct projective complement divisors.
The boundary has five points and the involution has at most two fixed points,
so the number of nonexceptional two-active-row orbits, and hence distinct
divisors `[K_u]`, is at least

```text
3e-2       on the antipodal branch,
3e-3       on the constant-product branch.          (PCT6)
```

The remaining rank-two problem therefore contains at least `3e-3` distinct
split degree-`e` divisors of one squarefree degree-`3e` polynomial on the
printed quadric in `P^3`. This theorem does not bound how many such divisors
a quadric can contain.

# Budget-three fiber-two c=2 one-antipodal degree-defect global gate router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_barycentric_support_polynomial_compiler`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_collision_or_high_support_router`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_secondary_differential_certifier`,
  `rate_half_list_budget_three_maximal_field_degree_collapse`,
  `f3_h2_stepanov_inhouse`

Retain any complete canonical candidate in the official one-antipodal `c=2`
chamber. Put

```text
m=deg C,       e=H-3-m,
epsilon_e=1 if e is even, and 0 if e is odd,
d_e=5H-10-3e-epsilon_e.                              (DGR1)
```

Let `J` be the even support polynomial in `(BSP1)`, and let `r_J` count its
roots in `mu_N\{+1,-1}`. Then

```text
deg J<=d_e,       eta=d_e-r_J in 2 Z_(>=0),           (DGR2)
|supp u|=3H+3e+epsilon_e+eta.                         (DGR3)
```

In particular the first degree-defect floors are

```text
e=0: |supp u|>=3H+1,
e=1: |supp u|>=3H+3,
e=2: |supp u|>=3H+7.                                 (DGR4)
```

The maximal-degree branch `e=0` inherits the following gates at every
support, not only at minimum support. With the notation of the secondary
differential certifier, put

```text
T_0=(H-1)EB+Hc_0z^(2H)-(H-1)E_4b_0z^(2H+1),
P_0=z^(-2H)(T_0B^3-(H-1)),
C_sharp=C/lc(C).                                      (DGR5)
```

Then

```text
C divides P_0,       gcd(C,T_0B)=1,
Res(C_sharp,T_0)Res(C_sharp,B)^3=(H-1)^(H-3),
Res(C_sharp,T_0) is a nonzero base-field cube.         (DGR6)
```

Write `b=[z^(2H-3)]B`, `c=[z^(H-3)]C`, and let `P_src` be the product of
the two complementary deleted roots. The four leading cell coefficients

```text
ell_i=b+cw_i
```

are distinct members of `mu_N`, have product `P_src^(-1)`, and are the roots
of

```text
O_inf(X)=(X-b)^4+alpha c^2(X-b)^2
             +beta c^3(X-b)+gamma c^4,
O_inf divides X^N-1.                                  (DGR7)
```

Moreover `O_inf'(ell_i)=c^3 Phi'(w_i)`. Thus on the collision branch the
infinity quartet has exactly one derivative-weight collision. If the
selected denominator pair is the unique antipodal pair, choose

```text
q^2=-alpha/6,       a=s/(2q),       tau=ell_4,
y=ell_3/ell_4,       a^2=-2,
A_a(y)=(a+2)y-(a+1),       B_a(y)=(a-1)y+(2-a).       (DGR8)
```

Then

```text
tau,y,A_a(y),B_a(y) in mu_N,
tau^4 y A_a(y)B_a(y)=P_src^(-1),
(P_src y A_a(y)B_a(y))^(N/4)=1,                       (DGR9)
```

and in every official field chamber

```text
#{y in mu_N:A_a(y),B_a(y) in mu_N}<=355106851<2^29.  (DGR10)
```

This theorem globalizes these gates only on `deg C=H-3`. It does not assert
the split-divisor condition for `J`, the endpoint product `Xi`, emptiness of
the affine intersection, or exclusion of any larger-support branch.

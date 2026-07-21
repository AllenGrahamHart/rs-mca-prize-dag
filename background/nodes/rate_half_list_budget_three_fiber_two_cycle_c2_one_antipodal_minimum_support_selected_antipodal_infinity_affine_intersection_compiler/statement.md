# Budget-three fiber-two c=2 minimum-support selected-antipodal infinity affine-intersection compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_barycentric_collision_branch_compiler`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_infinity_cell_torsion_gate`

Retain the minimum-support shard in which the selected denominator pair is
the unique antipodal pair.  Choose

```text
q^2=-alpha/6,       a=s/(2q),       d=c_m q,
u=b_r/d.                                                (SAI1)
```

Then `q,d` are nonzero and `a^2=-2`.  After ordering the equal-weight outer
pair first, the four infinity roots are

```text
ell_1=d(u+a+3),       ell_2=d(u+a-3),
ell_3=d(u-a+1),       ell_4=d(u-a-1).                 (SAI2)
```

Put

```text
tau=ell_4,       y=ell_3/ell_4,
A_a(y)=(a+2)y-(a+1),
B_a(y)=(a-1)y+(2-a).                                  (SAI3)
```

The roots are nonzero and distinct, so `y!=1`, and

```text
ell_1/tau=A_a(y),       ell_2/tau=B_a(y),
ell_3/tau=y.                                             (SAI4)
```

Consequently the infinity-cell torsion condition is exactly

```text
tau,y,A_a(y),B_a(y) in mu_N,                            (SAI5)
```

and its source-product endpoint is

```text
tau^4 y A_a(y)B_a(y)=P_src^(-1).                       (SAI6)
```

Eliminating the scale gives the strict quarter-order gate

```text
Z_inf=P_src y A_a(y)B_a(y)=tau^(-4),
Z_inf in mu_(N/4),       Z_inf^(N/4)=1,
N/4=2^38.                                                 (SAI6')
```

Conversely, inside the fixed selected-antipodal outer normal form, `y!=1`
and `(SAI3)--(SAI4)` recover the top canonical ratios through

```text
u=a+(y+1)/(y-1),       d=tau(y-1)/2,
b_r=du,                 c_m=d/q.                       (SAI7)
```

Changing the chosen square root `q` to `-q` induces the exact relabelling

```text
(a,y,tau) -> (-a,y^(-1),tau y),                        (SAI8)
```

which swaps the two roots within each displayed pair.  Thus the fixed
selected-antipodal infinity problem is a one-variable intersection of three
affine images with `mu_N`, plus one subgroup scale and the product equation.
This compiler does not prove that intersection empty, enumerate `mu_N`, or
reconstruct a full canonical packet.

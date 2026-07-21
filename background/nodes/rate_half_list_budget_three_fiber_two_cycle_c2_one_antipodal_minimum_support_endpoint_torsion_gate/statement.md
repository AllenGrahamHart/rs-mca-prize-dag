# Budget-three fiber-two c=2 one-antipodal minimum-support endpoint torsion gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_barycentric_support_polynomial_compiler`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_euler_divisor_gate`

Retain a minimum-support one-antipodal packet.  Write

```text
r=2H-3,       m=H-3,
B=sum_(j=0)^r b_jz^j,       C=sum_(j=0)^m c_jz^j,
Delta_inf=b_(r-1)c_m-b_rc_(m-1).                    (ETG1)
```

Here absent top coefficients are interpreted as zero.  For the support
compiler polynomial `J_supp` from `(BSP1)`, minimum support forces

```text
Delta_inf!=0,
J_supp(0)=2H,
lc(J_supp)=2P c_m^2 Delta_inf,                       (ETG2)
```

where `Q_-=1-Sz+Pz^2` is the complementary deleted-pair factor.  Therefore

```text
Xi=H/(P c_m^2 Delta_inf)                             (ETG3)
```

is the product of all roots of `J_supp`.

The polynomial `J_supp` is even, has degree `5H-11`, and in the
minimum-support case has distinct roots in `mu_N` while avoiding `+/-1`.
Its roots form negation pairs, and the product of each pair is a square in
`mu_N`.  Consequently

```text
Xi in mu_(N/2),       Xi^(N/2)=1,       N/2=2^39.    (ETG4)
```

This is a constant-size endpoint torsion test on the source product and the
top two coefficients of `B,C`.  It precedes the one-pair collision and
`L/Q` branches.  It does not prove `(ETG4)` impossible, evaluate the
official canonical coefficients, or address larger support.

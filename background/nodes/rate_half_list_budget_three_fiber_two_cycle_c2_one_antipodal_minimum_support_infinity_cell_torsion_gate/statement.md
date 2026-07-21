# Budget-three fiber-two c=2 one-antipodal minimum-support infinity-cell torsion gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_canonical_cell_fourier_ladder`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_barycentric_collision_branch_compiler`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_euler_divisor_gate`

Retain a minimum-support one-antipodal packet.  Put `m=H-3`, `r=2H-3`,
write

```text
b=b_r=[z^r]B,       c=c_m=[z^m]C,
ell_i=b+cw_i,       1<=i<=4,                         (ICT1)
```

and let `P_src=cd` be the product of the two complementary deleted roots in
`E=(1-z^2)(1-Sz+P_src z^2)`.  Then `c!=0`, the four `ell_i` are distinct,
and

```text
ell_i in mu_N,       product_i ell_i=P_src^(-1).      (ICT2)
```

Equivalently, the monic infinity quartic

```text
O_inf(X)=product_i(X-ell_i)
        =(X-b)^4+alpha c^2(X-b)^2
          +beta c^3(X-b)+gamma c^4                  (ICT3)
```

is a squarefree divisor of `X^N-1` and has constant coefficient
`P_src^(-1)`.  It has a constant-degree torsion certificate: in
`F[X]/(O_inf)`, define

```text
R_0=X,       R_(j+1)=R_j^2,       0<=j<40.           (ICT4)
```

Then every retained packet satisfies `R_40=1`.

The exact one-pair derivative-weight collision is preserved at infinity:

```text
O_inf'(ell_i)=c^3 Phi'(w_i).                         (ICT5)
```

Thus the reciprocal derivative weights of `O_inf` have exactly one equal
pair.  On the shard where the selected denominator pair is the unique
antipodal pair, the centered infinity coefficients also satisfy

```text
J_inf=72(alpha c^2)(gamma c^4)
      -27(beta c^3)^2-2(alpha c^2)^3=c^6J=0.         (ICT6)
```

This is a forty-squaring quartic prefilter on already canonical outputs.  It
does not classify subgroup quartets with one derivative collision, prove the
selected-antipodal shard empty, evaluate `b,c` cheaply at official degree,
or address larger barycentric support.

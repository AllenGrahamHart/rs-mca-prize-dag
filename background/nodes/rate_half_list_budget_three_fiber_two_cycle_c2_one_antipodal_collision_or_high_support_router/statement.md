# Budget-three fiber-two c=2 one-antipodal collision-or-high-support router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_canonical_cell_fourier_ladder`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_barycentric_support_polynomial_compiler`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_normalized_gap_span_compiler`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_torsion_field_router`

Retain any complete canonical candidate in the one-antipodal `c=2` chamber,
not necessarily at minimum barycentric support.  Let

```text
Phi(W)=product_i(W-w_i),       lambda_i=1/Phi'(w_i),
u(x)=f_lambda(x)-f_lambda(-x),       x in mu_N.       (CHR1)
```

Exactly one of the following alternatives holds.

1. **Distinct-weight/high-support branch.**  The four `lambda_i` are
   distinct and

   ```text
   |supp u|>=4H-2.                                    (CHR2)
   ```

2. **One-collision branch.**  Exactly one pair of the `lambda_i` is equal.
   If `s` is the sum of the corresponding outer roots and
   `y=s^2/alpha`, then

   ```text
   alpha s!=0,
   beta=-s^3,
   gamma=alpha^2/4+alpha s^2/2,                       (CHR3)

   Phi(W)=(W^2-sW+s^2+alpha/2)(W^2+sW+alpha/2).       (CHR4)
   ```

   For the selected denominator-pair trace `z=z_t`, this branch lies in the
   disjoint union

   ```text
   L: y(z+12)=2z-8,
   Q: [y(z+12)-16]^2=64z,       with Q using L!=0,    (CHR5)
   ```

   where the two intersections `(y,z)=(0,4),(4/3,36)` are assigned to `L`.
   Moreover `z!=-12` and

   ```text
   kappa=-2alpha/(z+12)                               (CHR6)
   ```

   is a nonzero base-field square.  If the selected denominator pair is the
   unique antipodal pair, then

   ```text
   z=0,       y=4/3,       J=0,
   12gamma=11alpha^2,       27beta^2=64alpha^3,
   -alpha/6 and -2 are squares.                       (CHR7)
   ```

Since `u` is odd under negation, its support is even.  Consequently every
candidate with `|supp u|<=4H-4` is on the one-collision `L/Q` branch.  The
theorem leaves the high-support distinct-weight branch and the collision
branches unexcluded; minimum-support-only Euler, endpoint, and infinity
gates are not asserted above minimum support.

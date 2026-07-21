# Budget-three fiber-two c=2 selected-antipodal affine Stepanov cap

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_selected_antipodal_infinity_affine_intersection_compiler`,
  `f3_h2_stepanov_inhouse`,
  `rate_half_list_budget_three_maximal_field_degree_collapse`

Work in any official field chamber of the selected-antipodal affine compiler.
Put `N=2^40`, choose `a^2=-2`, and define

```text
A_a(Y)=(a+2)Y-(a+1),
B_a(Y)=(a-1)Y+(2-a),
mathcal Y_a={y in mu_N:A_a(y),B_a(y) in mu_N}.       (SAC1)
```

Then

```text
#mathcal Y_a<=355106851<2^29.                         (SAC2)
```

In particular the additional requirements `y!=1`, the quarter-order product
gate, the canonical scale, gaps, and source coupling can only reduce this
cap.

The exact Stepanov parameters are

```text
A_0=D_0=79896510,       B_0=12902,
A_0+NB_0=14185899101462462.                          (SAC3)
```

They satisfy

```text
D_0(A_0+D_0)<A_0B_0^2,       A_0B_0<=N,
(A_0+2NB_0)^3<64D_0^3N^2.                            (SAC4)
```

For `q=p^e` on the official maximal row, `e<=2` and

```text
p>=31950697969885030204>A_0+NB_0.                    (SAC5)
```

Thus the sparse-polynomial nonvanishing argument is valid over `F_q` in
both the prime and quadratic chambers.  This theorem supplies a rigorous
candidate cap, not an emptiness result, an official canonical evaluator, or
an authorized exhaustive scan.

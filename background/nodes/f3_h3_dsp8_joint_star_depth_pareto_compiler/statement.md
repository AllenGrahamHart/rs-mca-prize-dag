# DSP8 joint-star / quotient-depth Pareto compiler

- **status:** PROVED
- **closure:** proof
- **consumers:** `f3_h3_dsp8_correlation_bound`,
  `f3_h3_official_order_template_survivor`
- **dependencies:** `f3_h3_dsp8_accident_depth_compiler`,
  `f3_h3_dsp8_disjoint_six_multiplicity_gate`,
  `f3_h3_excess_multistar_degree_ladder`,
  `f3_h3_double_accident_coupling_batch_odd_saturation`

For

```text
E in {6,8,10,12,14,16},
L_E=17-E,       q_E=19+E,       r_E=18-E,
rho_E(t)=max(R(t)-L_E,0),
```

split the retained disjoint-distance-six moment by target class:

```text
Dbar_E^c=sum_(t in class c,P(t)>=q_E)
                  N_6^disj(t)rho_E(t).             (JDP1)
```

Every positive summand has `P(t)>=q_E` and `R(t)>=r_E`. Pointwise, if
`e(t)=P(t)-18`, then

```text
e(t)<=a_E^0 N_6^disj(t)       on the antipodal-free class,
e(t)<=a_E^A N_6^disj(t)       on the antipodal class,          (JDP2)
```

with the exact current-router constants

```text
E   L_E  (q_E,r_E)  m_E   a_E^0   a_E^A   w_E=a_E^A/a_E^0
6    11   (25,12)    11     8/11       4          11/2
8     9   (27,10)    12      5/9     5/4           9/4
10    7   (29, 8)    13      4/9     3/4         27/16
12    5   (31, 6)    14      7/18   7/12           3/2
14    3   (33, 4)    15     16/47   8/17         47/34
16    1   (35, 2)    16      9/29   9/22         29/22.       (JDP3)
```

Here `m_E=8+E/2` is the minimum number of small unordered product
representations on that corner. The accident-depth budget therefore gives
the exact sufficient condition

```text
17(a_E^0 Dbar_E^0+a_E^A Dbar_E^A)
 <=B_(L_E,E)(n),                                   (JDP4)
```

and the following simpler conditions are sufficient:

```text
E    Dbar_E^0+w_E Dbar_E^A <= C_E n^2
6                              C_E=121/136
8                              C_E= 99/85
10                             C_E= 99/68
12                             C_E=198/119
14                             C_E=517/272
16                             C_E=319/153.        (JDP5)
```

The same six corners have exact sparse candidate packets. The product-side
packet and the complete quotient packet can be chosen as follows:

```text
E   (q_E,r_E)   antipodal-free product   antipodal product   quotient spokes
6    (25,12)    pure star degree 2       two-edge packet            11
8    (27,10)    pure star degree 3       pure star degree 2          9
10   (29, 8)    pure star degree 5       pure star degree 3          7
12   (31, 6)    pure star degree 6       pure star degree 4          5
14   (33, 4)    pure star degree 7       pure star degree 5          3
16   (35, 2)    pure star degree 8       pure star degree 6          1. (JDP6)
```

In the first antipodal row, the two disjoint-six edges need not share a
center, so their product ideal includes the cross-center generator from the
proved multiplicity gate. Let `J_E` denote the resulting product packet
ideal. Choose `r_E` distinct quotient lifts `Q_0,...,Q_(r_E-1)` and relabel so
that `lambda_0` is nonzero. At least `r_E-1` couplings are nonzero, and

```text
I_E^batch=(J_E,lambda_0,...,lambda_(r_E-1)),
I_E^anchor=(J_E,lambda_0,theta_(0,1),...,theta_(0,r_E-1)),
I_E^batch O[1/2]=I_E^anchor O[1/2].                (JDP7)
```

Both forms retain the exact quotient depth and have the same valuations at
every official odd row prime. The official row prime divides their ideal
norms.

This theorem offers six alternatives. Coordinates from different rows of
the tables cannot be mixed. It proves none of the moment estimates `(JDP4)`
or `(JDP5)`, supplies no template generator, and gives no survivor count.

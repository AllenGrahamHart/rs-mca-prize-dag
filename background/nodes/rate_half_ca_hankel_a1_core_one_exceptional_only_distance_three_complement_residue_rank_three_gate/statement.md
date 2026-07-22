# `A=1` core-one distance-three complement-residue rank-three gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_pair_lagrange_normal_form`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_external_split_design_saturation`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_pair_locator_mobius_dichotomy`

Retain the official pair-Lagrange external design. Let

```text
I(z)=product_(i=1)^e(z-xi_i),
P_Z(z)=product_(gamma in Z_ext)(z-gamma),
G_x(z)=product_(gamma in S_x)(z-gamma)       (x in C),
H_x(z)=P_Z(z)/G_x(z).                                (CR3G1)
```

Thus `deg P_Z=3e`, every `G_x` is a monic degree-`e` divisor of `P_Z`, and
every complement locator `H_x` has degree `2e`. The internal slopes `xi_i`
are distinct and disjoint from `Z_ext`, so reduction modulo `I` is detected
by evaluation at the `xi_i`.

Then the complement residues obey

```text
dim span{H_x mod I:x in C}<=3.                       (CR3G2)
```

Equivalently, the `(6e+3) x e` matrix

```text
M_comp=(H_x(xi_i))_(x in C,1<=i<=e)                 (CR3G3)
```

has rank at most three. The equivalent inverse-locator matrix

```text
M_inv=(G_x(0)/G_x(xi_i))_(x,i)                      (CR3G4)
```

also has rank at most three.

In fact these ranks equal

```text
dim span{D_1,...,D_e},                               (CR3G4a)
```

so they are exactly two on the common-Mobius branch and exactly three on
the generic branch of the pair-locator dichotomy.

There is also an internal-slope-free coefficient-span consequence. If

```text
W_comp=span{H_x:x in C} subset F[z]_(<=2e),
```

then

```text
dim W_comp<=e+4.                                      (CR3G5)
```

Thus the full coefficient matrix of the `6e+3` complement locators has row
nullity at least `5e-1`. This bound can be tested before choosing or
evaluating the internal slopes.

This gate is nontrivial from `e=4` onward. It is not a consequence of the
biregular incidence parameters: there are `e=4` families of 27 distinct
four-subsets on 12 slopes, with every slope occurring nine times, whose
complement polynomials span all nine degree-eight coefficients and whose
complement-residue matrix has rank four.

The theorem reduces the open external chart to a rank-three classification
of split complement locators in `F[z]/(I)`. It does not classify that rank-
three family or exclude the official design.

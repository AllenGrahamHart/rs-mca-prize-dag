# KoalaBear m2 r4 coordinate negative two-loop 442 H6 complete-product exclusion

- **status:** PROVED
- **scope:** all twelve remaining invariant-product cells over
  `H6,tau=-1` and `H6,tau=+1`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_exceptional_product_classifier`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_outside_product_involution_compiler`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_product_invariance_router`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_signed_pair_matching_template_exclusion`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h8_positive_complete_product_exclusion`
- **consumer:** `rate_half_band_closure`

All twelve cells are empty over the deployed KoalaBear field.  Consequently
the entire `(4,4,2)` common skeleton is impossible at the necessary complete
paired-product gate.

For `tau in {-1,+1}`, write

```text
P_tau(b)=4b^2+r_tau b+4,
(r_-1,c_-1)=(1,2(1-b)/3),
(r_+1,c_+1)=(7,2(b+1)).                          (KB44F-1)
```

Reduction by `l^2-l+1` gives the forced product

```text
p_xi=-b.                                         (KB44F-2)
```

The two common product pairs give

```text
Guv-A(u+v)-B=0,
G=b^2-tau bc+c-1,
A=c(tau b^3-1),
B=-bc(tau b^2c-tau b^2+b-tau c).                (KB44F-3)
```

Forced type `DF` is impossible immediately: after forcing `DF=p_xi=-b`,
the residual product `-DF=b` repeats the common singleton product `b`,
contrary to product injectivity.

For forced `cD` and `sigma DE`, the residual sextics are

```text
cD: (a,-sigma ba/c^2,x,-x,-ax/b,ax/b),
DE: (a,-sigma bc^2/a,x,-x,-sigma bc^2x/a^2,
     sigma bc^2x/a^2).                           (KB44F-4)
```

The signed-pair parent deletes matching indices `0,1,2`.  For
`sigma=-tau`, exact primary and alternate resultants delete the six
`F -> -F` representatives `3,4,5,9,10,11`.  Their complete factor-norm
prime supports are

```text
row/sign             cD                    sigma DE
H6-, sigma=+1        {2,3,5,7}             {2,3,5,7,29,41,757}
H6+, sigma=-1        {2,3,5}               {2,3,5,7,11,13,17,149}. (KB44F-5)
```

The deployed characteristic divides none of these norms.

For `sigma=tau`, exact Groebner reduction over `Q` gives the following
complete alternative on every representative: the ideal is already unit,
or it contains

```text
a^2-b^2.                                           (KB44F-6)
```

All six `cD` representatives have the second outcome.  For `sigma DE`,
indices `5,10` are unit and `3,4,9,11` have the second outcome.  Since the
deployed characteristic is not two, `(KB44F-6)` forces `a=+/-b`.  Here `a`
is the other colored product, so it repeats either the common product `b`
or the forced product `-b`.  Product injectivity excludes both choices.
A direct deployed-field saturation by `a^2!=b^2` independently gives the
unit ideal in every aligned case.

Thus all six cells on each H6 row are empty.  The exact `442` frontier drops
from two rows, 12 cells, and matching cap 156 to the empty set.

This theorem does not close the `(4,3,3)` or any other coordinate skeleton,
the coordinate orientation, a Prize row, or either Prize result.

## Falsifier

A guarded deployed-field H6 complete-product packet; a vanishing norm in
`(KB44F-5)`; a nonunit aligned collision saturation; or a complete-source
`(4,4,2)` lift that bypasses the necessary paired-product gate.

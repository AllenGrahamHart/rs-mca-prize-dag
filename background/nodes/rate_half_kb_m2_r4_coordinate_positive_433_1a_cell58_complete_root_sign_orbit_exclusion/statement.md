# KoalaBear positive 433-1a cell-5/8 complete root-sign orbit exclusion

- **status:** PROVED
- **scope:** every deployed parameter, matching cells `5,8`, all four
  common root-sign rows
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_coefficient_normal_form`,
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`, and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell58_epsilon2_minus_transport_exclusion`
- **consumer:** `rate_half_band_closure`

In the positive coefficient normal form

```text
H(T,X)=A_2(W)T^2+A_0(W)+XT B_1(W),      W=X^2,
```

apply the source-reciprocal involution

```text
I(H)(T,X)=X^4 H(T,-1/X).                         (KBC58R-1)
```

It remains in the same coefficient space.  In coefficient order
`(d_0,d_1,d_2,e_0,e_1,e_2,beta_0,beta_1)`, it is

```text
(d_2,d_1,d_0,e_2,e_1,e_0,-beta_1,-beta_0).       (KBC58R-2)
```

For a source lift `z`, quotient label `lambda=z^2`, target product `p`,
target sum `s`, and `q=zs`, put

```text
z'=-1/z,       lambda'=1/lambda,       q'=-q/lambda.
```

Then the transformed positive Vieta equations are exact nonzero multiples
of the originals:

```text
A_0'(lambda')-p A_2'(lambda')
  =lambda'^2 (A_0(lambda)-p A_2(lambda)),

lambda' B_1'(lambda')+q' A_2'(lambda')
  =-lambda'^3 (lambda B_1(lambda)+q A_2(lambda)). (KBC58R-3)
```

The map `lambda -> 1/lambda` preserves distinctness, opposite source pairs,
all source-facet incidences, and every target record.  In cell `5`, whose
common roots are

```text
LC=1, AC=epsilon_1 i, AB+2=r,
AB-=epsilon_2 i r, AB+1=t,
```

it preserves `epsilon_1` and sends

```text
(epsilon_2,r,t) -> (-epsilon_2,-1/r,-1/t).        (KBC58R-4)
```

The lift `LC=1` maps to its deck mate `-1`; its target record is the
antipodal loop and has `q=0`, so this is the same canonical row.  Thus
`(KBC58R-1)` is an exact bijection between the two `epsilon_2` rows in cell
`5`.  The duplicate-`AB+` transport gives the same bijection in cell `8`.

The parent theorem excludes both `epsilon_1` values in cells `5,8` when
`epsilon_2=-1`.  The reciprocal bijection therefore proves all eight rows

```text
{5,8} x {-1,+1} x {-1,+1}                         (KBC58R-5)
```

empty.

This deletes matching cells `5` and `8` from the positive common atlas.  It
does not treat another role-cell orbit, delete the full positive
`433-1a -> O0b` route, close K3 or a Prize row, or prove LIST or MCA.

## Falsifier

An admissible packet in `(KBC58R-5)`, failure of `(KBC58R-1)` to preserve
the positive coefficient space, a source or target guard lost under
inversion, or failure of either identity in `(KBC58R-3)`.

# KoalaBear positive 433-1a cell-4 genus-one plane-kernel reduction

- **status:** PROVED
- **scope:** common matching cell `4`, signs `(-1,-1)`, over
  `F_2130706433`; source symmetry identifies the common geometry for orbit
  `[4,7]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_kernel_uniqueness`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient`,
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_remaining_common_curve_profile`
- **consumer:** `rate_half_band_closure`

The guarded cell-4 common ideal has a seven-element lex basis in order
`(c,r,b,t)`.  Its first polynomial is a 21-term palindromic eliminant
`P(b,t)` of bidegree `(4,4)`.  On `b!=0`, the quotient `x=b+b^{-1}` is a
conic whose quadratic discriminant is

```text
48 (t+510119941)(t+899209895)
   (t-16711679)^2(t+16711679)^4.                 (KBC4-1)
```

The square-free conic in `(KBC4-1)` contains `(t,Y)=(1,66846712)`.  After
parametrizing from this point and restoring `b` through `b^2-xb+1`, the
second discriminant has square denominator and numerator, up to a nonzero
field scalar,

```text
(s-66846716)(s+4)^2
(s^3-66846708s^2-1061158961s-1035993668).       (KBC4-2)
```

The linear and cubic factors in `(KBC4-2)` are distinct and irreducible.
Removing the square `(s+4)^2` leaves a square-free polynomial of degree four,
so the smooth projective normalization of the asserted open common curve has
genus one.

The unique common coefficient kernel also has an exact compact plane model.
Solving the lex equations for `r,c`, clearing their common denominator,
removing the first projective scale, pseudo-reducing by `P`, and removing the
second common scale gives all eight coefficients of `A_2,A_0,B_1` with
`b`-degree at most three and `t`-degree at most eighteen.  Exactly

```text
b11=-b10, so B_1(W)=b10(1-W).                   (KBC4-3)
```

The four necessary target-free `DE+/DE-/BE` equations are compiled in this
model.  Their guard-saturated global basis reached its 250-second cap and has
no unit or nonunit conclusion.  Exceptional scale zeros are outside this
node's chart and are closed by the separate proved exceptional-scale child.
Thus this node does not exclude cell 4 or 7, close `[4,7]`, the positive
route, K3, LIST, MCA, or either Prize problem.

## Falsifier

A failed lex replay or reciprocal reconstruction, a repeated factor in the
degree-four square-free cover, a genus different from one, failed exact
kernel divisions, `b10+b11!=0`, or treating the bounded target-free timeout
as a mathematical conclusion.

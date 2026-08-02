# KoalaBear positive 433-1a cell-3 genus-three plane-kernel reduction

- **status:** PROVED
- **scope:** common matching cell `3`, signs `(-1,-1)`, over
  `F_2130706433`; by the proved source symmetries this is the common curve
  underlying the orbit `[3,6]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_kernel_uniqueness`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient`,
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_remaining_common_curve_profile`
- **consumer:** `rate_half_band_closure`

The guard-localized cell-3 common ideal has an exact seven-element lex basis
in order `(c,r,b,t)`.  Its first polynomial `P(b,t)` is palindromic of
bidegree `(4,4)`.  On the guard chart `b!=0`, setting `x=b+b^{-1}` gives a
quadratic `Q(x,t)` whose discriminant is

```text
48 (t+510119941)(t+899209895)
   (t+16711679)^2(t-16711679)^4.                 (KBC3-1)
```

The square-free conic in `(KBC3-1)` has the deployed rational point
`(t,Y)=(1,66846712)`.  Parametrizing it by a line of slope `s`, and then
adjoining the root of `b^2-xb+1`, gives a hyperelliptic model

```text
y^2 = R_8(s),                                     (KBC3-2)
```

where, up to a nonzero field scalar,

```text
R_8(s)=(s+4)(s+930460291)(s+1042373100)
       (s-1064153723)(s-997808612)
       (s^3-66846708s^2+1061158993s+1044382147). (KBC3-3)
```

All six factors in `(KBC3-3)` are distinct and irreducible over the deployed
field, so `R_8` is square-free of degree eight.  The normalization of this
open common curve therefore has genus three.  The exact inverse denominators
are squares and are sealed in the evidence packet.

The unique common coefficient kernel also admits a compact exact plane model.
After solving the lex equations for `r,c`, clearing one common denominator,
removing a common projective factor, and pseudo-reducing by `P`, all eight
coefficients of `A_2,A_0,B_1` have `b`-degree at most three and `t`-degree at
most 22.  Moreover

```text
b11 = -b10, so B_1(W)=b10(1-W).                  (KBC3-4)
```

The denominator scale, both removed common scales, and the sixteenth power of
the plane leading coefficient are explicit.  Their zero loci are retained as
separate exceptional charts; this node does not delete them.

The four target-free `DE+/DE-/BE` equations have been compiled exactly in the
compact model.  Their guard-saturated standard-basis run reached its bounded
250-second cap and makes no unit or nonunit claim.  Hence this node does not
exclude cell `3` or `6`, close the positive route, K3, LIST, MCA, or either
Prize problem.

## Falsifier

A failed lex-basis replay, failure of palindromy or reconstruction, a repeated
factor in `R_8`, a different genus, a failed exact kernel division or
pseudo-reduction, `b10+b11!=0`, or treating the timed-out target-free basis as
a mathematical conclusion.

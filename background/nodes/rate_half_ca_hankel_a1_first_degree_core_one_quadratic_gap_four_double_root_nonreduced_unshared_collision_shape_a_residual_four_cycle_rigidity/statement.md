# `A=1` collision shape-A residual four-cycle rigidity

- **status:** PROVED
- **closure:** the exact residual four-cycle is `2B` and has one section
- **consumer:** `rate_half_band_crossing_location`

Retain shape A. Let `C` be the normalized source-locator curve and

```text
pi:C -> P^1_X,       d=3e-2.                         (RFR1)
```

The double-root normal form supplies an effective degree-two correction
divisor `B` and a nonempty divisor `R_*` of degree `e-6` such that

```text
div_C(X-x_*)=R_*+3B,
div_C(s_F)=R_*+2B,                                  (RFR2)

pi_*O_C(B)=O direct_sum O(1-d)^2
                 direct_sum O(-d)^(e-3).            (RFR3)
```

Let `Z_4` be the pullback to `C` of the residual projective intersection
cycle obtained from `Q=G=0` after subtracting one copy of every mandatory
actual-support and padding point. Then

```text
Z_4=2B.                                             (RFR4)
```

The doubled correction divisor is rigid:

```text
h^0(C,O_C(2B))=1.                                   (RFR5)
```

Equivalently, every section of `O_C(2B)` is proportional to the square of
the canonical section `(X-x_*)/s_F` of `O_C(B)`. In particular, the exact
four-core does not furnish a degree-four pencil.

## Scope

This is a route decision, not a shape-A exclusion. A closure through the
four-core must construct a genuinely second section in the same residual
line bundle, which would contradict `(RFR5)`, or use structure not encoded
by the residual divisor alone. No smoothness or gonality assertion about
the locator curve is used.

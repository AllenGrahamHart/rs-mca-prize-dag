# AQB c=2 Box-Charge Amortization Refutation

Status: COUNTEREXAMPLE / REFUTED ROUTE.

Source DAG node: `aqb_box_charge_amortization`.

## Statement Refuted

The proposed AQB route asserted that an averaged `c=2` quotient-box family at

```text
sigma* = 8,592,912,738
```

could share the box charge across the family and save at least
`429,645,547` bits relative to the single-word quotient-box floor.

This note records why that amortization mechanism does not work.  The
obstruction is structural, not a numerical miss.

## Convex-Combination Obstruction

Let

```text
Omega = {quotient-support configurations S subset mu_N with |S| = m}
Phi   : Omega -> B
```

be the box-datum map.  For `b in B`, write

```text
Omega_b = Phi^{-1}(b).
```

The single-word floor is the mean box fiber

```text
|Omega| / |B|.
```

An averaged family chooses box data through a distribution `p_b` on `B`.
The family-average list mass is therefore

```text
Avg(F) = sum_b p_b |Omega_b|.
```

This is a convex combination of the same single-box counts.  Consequently,

```text
Avg(F) <= max_b |Omega_b|.
```

For the uniform family,

```text
Avg(F) = |Omega| / |B|,
```

exactly the single-word floor.  The apparent saving from "paying the box
charge once" is cancelled by the averaging transfer, which divides by the
number of averaged box choices.  In other words, the saved `log2 |A|` box bits
reappear as the family denominator.

Thus c=2 box-charge sharing alone cannot create a net entropy gain over the
plain floor.  To beat the floor one would need a separate heavy-fiber theorem:
some box fiber `Omega_b` must itself be larger than the mean by the required
factor.  That is a different statement, not box-charge amortization.

## Campaign Constants

The rate-`1/2` razor-slice target used

```text
d = 4,296,456,369
sigma* = 2d
target gain = 429,645,547 bits.
```

The target is about `0.000390760348` bits per `2^40` quotient fiber coordinate
and about `0.1` bits per extra fiber.  These constants explain why the route
looked numerically plausible, but they do not overcome the convex-combination
identity.

## Consequence

The canonical c=2 AQB amortization route does not close the rate-`1/2` band.
The band must be handled by a sibling route, such as an adjacent safe-side
upper ledger, a heavy-fiber theorem with its own falsifier, or a different
paid residual mechanism.

This is compatible with the current v13 guide: identity-scale rows now
supersede the old c=2 terminal-scale proposal unless the identity map is
intentionally excluded.

## Replay

```bash
python3 experimental/scripts/verify_aqb_c2_amortization_refutation.py --emit
```

The verifier records the campaign constants and checks representative finite
convex-combination instances.  The proof above is the general argument.

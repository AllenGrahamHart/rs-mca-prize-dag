# conditional: aqb_averaged_quotient_box

## Predicate nodes

- `aqb_deficit_arithmetic`
- `aqb_c2_average_family`
- `aqb_box_charge_amortization`

## Claim

Conditional on the family construction and amortization predicates, AQB-I
supplies the averaged quotient-box gain needed by `rate_half_band_closure`.

## Proof

The proved predicate `aqb_deficit_arithmetic` supplies the exact finite target:
at worst `Q = 256`, the missing gain is strictly less than `429,645,547` bits.

The predicate `aqb_c2_average_family` supplies the averaged `c=2` family at
`sigma*`. The predicate `aqb_box_charge_amortization` proves that this family
saves at least `429,645,547` bits after all box charges and normalizations are
paid.

Therefore the averaged family clears the certified deficit in every admissible
field range covered by the AQB-I statement. This is precisely the content
needed by `rate_half_band_closure`.

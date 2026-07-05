# conditional: aqb_box_charge_amortization

## Predicate nodes

- `aqb_c2_average_family`
- `aqb_amortization_threshold_accounting`
- `aqb_shared_entropy_gain`

## Claim

Conditional on the concrete averaged family and its net entropy-gain
inequality, the AQB shared box-charge amortization predicate holds.

## Proof

The family predicate supplies the averaged `c=2` quotient-box family at
`sigma*`. The shared entropy-gain predicate proves the exact accounting for
that family: after all box charges, overlaps, multiplicities, and
quotient/fiber normalizations are paid, the net gain is at least
`429,645,547` bits.

The proved threshold-accounting predicate compares this number with the finite
AQB deficit certified by `aqb_deficit_arithmetic`. Since the certified
worst-case deficit is strictly below `429,645,547` bits, any family meeting
that gain threshold amortizes the shared box charge by the amount required in
this node.

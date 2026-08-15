# Rank-nine weighted target elimination

- **status:** PROVED after shortening-scope repair
- **closed interval:** `20618<=K'<=1048576`
- **open interval:** `10<=K'<=20617`

For the fixed rank-nine affine-owner chart, the weighted component demand
exceeds the rank-nine component cap on every row

```text
20618<=K'<=1048576.
```

At the exact first crossing,

```text
K'=20618:
demand =92397581841774591,
cap    =92395178310909600,
gap    =2403530864991.
```

On the preceding row the cap still exceeds the demand:

```text
K'=20617:
demand =92386821615379573,
cap    =92394042904582935,
gap    =7221289203362.
```

The unrounded demand/cap ratio is a positive constant times ten increasing
RS factors, so the strict boundary gap persists through the deployed
endpoint.

## Scope repair

The former proof claimed closure below `K'=67473` by lifting a residual
plane to the original row, obtaining a `134944`-coordinate common core, and
then comparing that core with the residual support size `m'=67472+K'`.
That comparison is invalid. The reverse shortening already inserts
`1048576-K'` deleted coordinates into every lifted owner core. The
original-row common-core theorem therefore does not imply a
`134944`-coordinate residual core. It gives no low-row contradiction.

## Nonclaim

The rank-nine target remains open on `10<=K'<=20617`. This node does not
pay the fixed-kernel or rank-eight lanes, move an active-v4 atom, or close
rank eleven.

## Falsifier

A row at or above `20618` where the exact weighted demand does not exceed
the cap; failure of monotonicity of one of the ten printed factors; or any
use of the original-row `134944` core as a residual-core lower bound.

# E1 profile-weight payoff ladder

## Status

Exact draft lemma, not a DAG node. The arithmetic was independently derived
from the proved weighted-kernel formula, but its committed Python replay has
not run because Modal is disabled. No critical status changes here.

The one-container replay was attempted on 2026-07-28 and rejected before
container creation with `Workspace ... has exceeded its spend limit`. It
incurred no campaign compute. Do not retry until the spend limit changes.

## Binding row

For prize rate `1/8`, the proved dictionary gives

```text
sum_(a,b) M_33(a,b) D_(a,b) <= 2 E_max,
E_max = 65127585921474870475467050631501738502567,
```

where `D_(a,b)` is the number of oriented folded kernel vectors in profile
`(a,b,4a+b)`. There are exactly 271 eligible profiles after the proved prize
norm floors. If `M_max` is the greatest weight among profiles not proved
empty, then

```text
sum_(a,b) D_(a,b) <= floor(2 E_max / M_max)
```

is a sufficient uniform fallback. The exact weighted inequality is stronger.

## Exact ladder

The rows are sorted by decreasing weight. Deleting every preceding profile
makes the displayed row the new coarse maximum.

| next maximum profile | `M_33(a,b)` | sufficient total-vector cap |
|---|---:|---:|
| `(4,2,18)` | 1873053318886373426584792000465260242 | 69541 |
| `(3,6,18)` | 1386246316188473270092082114587711840 | 93962 |
| `(2,10,18)` | 1227527050040565145269313275179180544 | 106111 |
| `(1,14,18)` | 1154418456451360735963226152798543872 | 112831 |
| `(0,18,18)` | 1117325838856821897682125205459304448 | 116577 |
| `(4,4,20)` | 522452937039935372855706187881128712 | 249314 |
| `(3,8,20)` | 432776013393430570914298670133713280 | 300975 |
| `(2,12,20)` | 394747100704470761700528481188071424 | 329971 |
| `(1,16,20)` | 374901575688629273473602791080820736 | 347438 |
| `(0,20,20)` | 363409091422312822402997461372633088 | 358425 |
| `(5,2,22)` | 213637532202373724400313526161611334 | 609701 |
| `(4,6,22)` | 155883854763951097618312682146951968 | 835591 |

Every cap is sharp for this coarse maximum-weight inference: replacing it by
the adjacent integer makes `M_max (cap+1) > 2 E_max`. This does not assert
that the adjacent integer is prize-unsafe; only that the uniform inference no
longer certifies it.

## Route decision

The proved `(4,2,18)` exclusion has already moved the cap from `69,541` to
`93,962`. A complete `(3,6,18)` exclusion would move it to `106,111`, an
increase of `12,149`. Clearing all five `S=18` profiles would move it to
`249,314`.

Primitive `m=16` is only one of four live cofactors `2,4,8,16` in
`(3,6,18)`. Completing that child is valuable and nearly bankable, but it does
not change the aggregate cap until the other three cofactors are paid or the
profile receives an aggregate vector bound. This rules out treating the
interrupted reverse replay as a target closure by itself.

The pure-dyadic orbit debit sharpens what "paid" can mean: every colliding
full affine coefficient orbit contributes exactly 256 oriented vectors, so
the profile-only coarse allowance is 367 collision orbits, not necessarily
zero. See `notes/E1_PROFILE_36_ORBIT_DEBIT.md`.

## Replay

When Modal is enabled, run this verifier-scale task before promoting the
arithmetic to a green evidence node:

```bash
./tools/ramguard modal -- modal run \
  experiments/prize_resolution/e1_profile_weight_payoff_ladder_modal.py
```

The launcher uploads only the verifier and `dag.json`, requests one 128 MB
container, and has a 60-second hard timeout. No local replay is authorized
while the workspace remains disabled.

# Wave-72 addendum: positive 433-1b role-cell orbit [4,7] closure (2026-08-08)

The last cell-4 matching-exchange orbit and the complete role-cell orbit are
now closed.

## Matching 11 direct exclusion

The direct PROVED node

```text
rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_pairing11_quadratic_resultant_signfree_exclusion
```

excludes missing `df` at canonical matching 11. After omission, the pairs are

```text
(de,bf), (de,sigma_c cf), (-de,sigma_o ef).
```

The first two are quadratic in `q=de`. Their exact quadratic resultant,
reduction modulo the missing-sum quartic, and `z -> -z` elimination leave a
linear common-root cut in the four-basis tower. Complete exceptional-root
replay gives

```text
source-sign/sigma_c rows              8
norm bidegrees             (3864,1560) or (3868,1560)
target / candidate r roots          44 / 60
guarded source points                   16
compatible z / q candidates            8 / 8
final Pair(-q,sigma_o ef) checks          16
source boundary / no-lift             56 / 16
target boundary / witness               0 / 0
free branch / unresolved                0 / 0
```

The independent verifier recomputes all degree-3864/3868 base-field root
unions and every original finite equation. It passes on Modal app
`ap-74kOL7uM1Y7OHlIhM5mI1A`.

## Final transport and assemblies

The exact parallel-`DE` exchange and universal xi3/xi4 transport pay
`(xi,pairing)=(3,14),(4,11),(4,14)`. The resulting four-label block closes
the last live cell-4 orbit.

Three new set-theoretic assembly nodes then verify, without cumulative prose
counters:

```text
parallel-DE roles xi={0,1,2}: 45 labels, 720 raw systems;
outside roles     xi={3,4}:    30 labels, 480 raw systems;
endpoint roles    xi={5,6}:    30 labels, 480 raw systems.
```

Their pairwise-disjoint union is all `7*15=105` labels and all 1,680
principal systems. Together with the previously proved global rank-drop
exclusion, this proves complete role-cell-4 emptiness.

## Duplicate-role orbit

An exact `B/C` exchange sends cell 4 to its duplicate-role partner cell 7,
fixing target lanes and guards, mapping source signs by
`(epsilon_1,epsilon_2) -> (epsilon_1,-epsilon_2)`, and swapping only the two
colored outside records. Independent sparse-polynomial and 105-case matching
enumerations prove a bijection of all 1,680 principal systems. The global
rank-drop theorem covers the complementary branch. Hence role orbit `[4,7]`
is PROVED empty.

The remaining positive `433-1b -> O0a` role orbits are `[5,8]`, `[9,10]`,
`[11]`, and `[12,13]`. No positive-route, K3, LIST, MCA, or Prize endpoint is
claimed.

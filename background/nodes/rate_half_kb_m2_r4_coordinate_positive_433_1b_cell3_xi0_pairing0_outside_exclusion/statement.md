# Statement

## Claim `(KBP1B3-XI0P0-1)`

Work over `F_2130706433`, with `iota=16711679`.  On the guarded
product-rank-five branch of deployed positive `433-1b -> O0a` role cell `3`,
fix the first missing outside record `xi=0` and the first canonical residual
matching `pairing=0`.  For every one of the four source-sign pairs and every
one of the four target-sign lanes, there is no guarded target realization.

Equivalently, all

```text
4 source signs * 4 target lanes = 16
```

raw outside cases in this subfamily are empty.  The exhaustive reduction has
the following exact shape for each source-sign pair:

1. the common function algebra has basis
   `{1,t,t^2,b,bt,bt^2}` over `F_2130706433(r)`;
2. the target-free paired cut for the residual `(de,-de)` pair has a norm
   whose numerator has degree `422` and whose denominator has degree `156`;
3. its direct `6 x 6` multiplication norm equals the independent
   quadratic-over-cubic tower norm;
4. the numerator has exactly eleven base-field roots, five on printed route
   boundaries and six live norm roots;
5. exact lifting through the cubic base equation, quadratic `b` equation,
   linear `c` recovery, all route guards, and all six product cofactors leaves
   twelve guarded common points, exactly four of which satisfy the
   target-free cut; and
6. across the four target lanes, the resulting sixteen point/lane fibers
   contain no target point: twelve have no field-valued root of the colored
   quartic, while the remaining four have four such roots each and every
   resulting pair of univariate `u` cuts has gcd degree zero.

The final census therefore checks `64` point/lane fibers and `64` surviving
colored-`f` candidates across all source signs, with zero witnesses, zero
target-boundary solutions, and zero unresolved rows.

The claim does not cover `xi=1,...,6`, `pairing=1,...,14`, any other role
cell, complete cell-3 closure, the full positive `433-1b` route, K3, LIST,
MCA, or either Prize result.

# F3 h=8 chart-7 official scaling action

Status: PROVED OFFICIAL-ROW ORBIT LEDGER, NOT AN h=8 CLOSURE.

This packet connects the h=8 weighted homogeneity to the actual official rows.
The weighted action is not an arbitrary affine normalization: it is the finite
root-scaling action by `mu_n`.

## Action

Scaling a support by `gamma in mu_n` sends locator coefficients by

```text
c_i -> gamma^(16-i) c_i.
```

On reciprocal variables this gives the weights

```text
c8,c9,c10,c11,c12,c13,c14,c15       ->  8,7,6,5,4,3,2,1
bar_c8,bar_c9,...                   -> -8,-7,-6,-5,-4,-3,-2,-1.
```

`F3_H8_WEIGHTED_HOMOGENEITY.md` proves the reciprocal equations are
semi-invariant under this action, so their zero loci are preserved by official
root scaling.

## Chart-7 Freeness

On chart `7`,

```text
bar_c9 != 0.
```

If `gamma in mu_n` fixes a chart-7 point, then in particular

```text
gamma^7 bar_c9 = bar_c9.
```

For official rows `n=2^s`, `13 <= s <= 41`,

```text
gcd(7,n)=1.
```

Therefore `gamma=1`.  The chart-7 target has trivial stabilizer under official
root scaling, and every chart-7 orbit has size exactly `n`.

## Replayed Ledger

The compiler verifies all official exponents `s=13..41`:

```text
rows=29
chart7_weight=7
max_gcd=1
max_stabilizer_size=1
```

## Consequence

A future chart-7 count/payment argument may quotient by the finite official
`mu_n`-scaling action without stabilizer losses on this chart.  It must not
replace this by arbitrary scaling in the ambient field: such scaling does not
generally preserve the official support condition and cannot be used to set
`c9=1` on official rows.

This does not prove chart 7 empty or paid.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_chart7_official_scaling_action.py
```

Expected digest:

```text
H8_CHART7_OFFICIAL_SCALING_ACTION_PASS
```

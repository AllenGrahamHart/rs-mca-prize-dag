# F3 h=5 official scaling action

Status: PROVED OFFICIAL-ROW ORBIT LEDGER, NOT AN h=5 CLOSURE.

This packet connects the h=5 weighted homogeneity to the actual official rows.
The weighted action is not an arbitrary affine normalization: it is the finite
root-scaling action by `mu_n`.

## Action

Scaling a support by `gamma in mu_n` sends locator coefficients by

```text
l_i -> gamma^(10-i) l_i.
```

On the reciprocal variables this gives the weights

```text
l5,l6,l7,l8,l9       ->  5, 4, 3, 2, 1
bar_l5,bar_l6,...    -> -5,-4,-3,-2,-1.
```

The weighted-homogeneity packet proves the h=5 reciprocal equations are
semi-invariant under this action, so their zero loci are preserved by official
root scaling.

## Central Chart Freeness

On the central chart,

```text
bar_l5 != 0.
```

If `gamma in mu_n` fixes a central-chart point, then in particular

```text
gamma^5 bar_l5 = bar_l5.
```

For official rows `n=2^s`, `13 <= s <= 41`,

```text
gcd(5,n)=1.
```

Therefore `gamma=1`.  The central chart has trivial stabilizer under official
root scaling, and every central-chart orbit has size exactly `n`.

## Consequence

The next h=5 central-chart attack may quotient by the finite official
`mu_n`-scaling action without stabilizer losses on the central chart.  But it
must not replace this by arbitrary scaling in the ambient field: such scaling
does not generally preserve the official support condition.

This does not prove the central chart is empty.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_official_scaling_action.py
```

Expected digest:

```text
H5_OFFICIAL_SCALING_ACTION_PASS
```

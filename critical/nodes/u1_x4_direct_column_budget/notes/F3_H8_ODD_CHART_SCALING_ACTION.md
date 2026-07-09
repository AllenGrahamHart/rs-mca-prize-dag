# F3 h=8 odd-chart official scaling action

Status: PROVED OFFICIAL-ROW ORBIT LEDGER, NOT AN h=8 CLOSURE.

`F3_H8_CHART7_OFFICIAL_SCALING_ACTION.md` proves root-scaling freeness on the
smallest odd chart.  This packet extends the same official-row argument to all
four routed odd charts from `F3_H8_ODD_CHART_PARTITION.md`.

## Statement

Root scaling by `gamma in mu_n` sends locator coefficients by

```text
c_i -> gamma^(16-i) c_i.
```

On the routed odd charts the live denominator variables are:

```text
chart 7: bar_c9  has weight -7
chart 5: bar_c11 has weight -5
chart 3: bar_c13 has weight -3
chart 1: bar_c15 has weight -1
```

For official rows `n=2^s`, `13 <= s <= 41`, every chart weight is odd, hence

```text
gcd(7,n)=gcd(5,n)=gcd(3,n)=gcd(1,n)=1.
```

Therefore the official `mu_n` scaling action is free on every routed odd
chart.  Every routed chart orbit has size exactly `n`.

## Proof

If a scaling element fixes a point in chart `k`, the nonzero denominator
coordinate on that chart is multiplied by `gamma^(-k)`.  Since that coordinate
is nonzero, fixing the point forces `gamma^k=1`.  The official support scaling
group has order `n=2^s`, and `k` is one of `7,5,3,1`, so `gcd(k,n)=1`.  Thus
`gamma=1`.

The weighted-homogeneity packet proves that the reciprocal equations are
preserved by this root-scaling action.  The odd-chart partition packet proves
that these are exactly the four routed cells for non-antipodal x83 full-zero
supports.

## Consequence

Future chart-wise h=8 count or payment arguments may quotient each routed odd
chart by official root scaling without stabilizer losses.  As before, this is
only the finite official `mu_n` action; it does not justify arbitrary ambient
normalization such as setting a chart coefficient to `1`.

This does not prove any odd chart empty or paid.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_odd_chart_scaling_action.py
```

Expected digest:

```text
H8_ODD_CHART_SCALING_ACTION_PASS
```

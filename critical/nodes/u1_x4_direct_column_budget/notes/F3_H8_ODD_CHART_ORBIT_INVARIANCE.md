# F3 h=8 odd-chart orbit invariance

Status: PROVED STRUCTURAL ORBIT LEDGER, NOT AN h=8 CERTIFICATE.

This packet combines the odd-chart partition with official root-scaling
freeness.

## Statement

The rooted support-scaling action sends

```text
c_i -> gamma^(16-i)c_i.
```

Since `gamma` is nonzero, this action preserves the zero/nonzero status of
every high odd locator coefficient:

```text
c15,c13,c11,c9.
```

Therefore the first-live priority route

```text
c9 -> chart 7, c11 -> chart 5, c13 -> chart 3, c15 -> chart 1
```

is invariant under official root scaling.

Combined with `F3_H8_ODD_CHART_SCALING_ACTION.md`, every routed odd-chart orbit
has trivial stabilizer on official rows and stays inside its routed chart.

## Consequence

Future h=8 certifiers may shard chart-wise by official scaling orbits without
cross-chart leakage and without stabilizer corrections:

```text
routed support -> unique chart -> full free official scaling orbit in that chart.
```

This still does not certify any support as non-full-zero; it only makes the
chart-wise orbit bookkeeping exact.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_odd_chart_orbit_invariance.py
```

Expected digest:

```text
H8_ODD_CHART_ORBIT_INVARIANCE_PASS
```

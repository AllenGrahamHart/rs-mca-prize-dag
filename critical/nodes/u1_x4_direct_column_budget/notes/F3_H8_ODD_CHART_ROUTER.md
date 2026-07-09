# F3 h=8 odd-chart router

Status: CERTIFIER INTERFACE / DRY-RUN ROUTER, NOT AN h=8 CERTIFICATE.

This packet turns the four-chart symbolic split into a deterministic routing
rule for future non-antipodal x83 certifiers.

## Priority Rule

`F3_H8_X83_PARITY_REDUCTION.md` proves that any non-antipodal x83 full-zero
support has at least one nonzero high odd locator coefficient among

```text
c15,c13,c11,c9.
```

The odd-chart recovery work shows that chart `7` is the smallest local system,
then chart `5`, then chart `3`, then chart `1`.  The router therefore assigns a
canonical support to the first live chart in the priority order:

```text
c9  != 0  -> chart 7
c11 != 0  -> chart 5
c13 != 0  -> chart 3
c15 != 0  -> chart 1
```

This creates a disjoint chart partition of the high-odd branch.  Supports with
all four high odd coefficients zero are not routed; by the parity reduction
they cannot be non-antipodal x83 full-zero survivors.

## Dry-Run Replay

The replay scans a bounded prefix of anchored supports using the same anchoring
and rotation-canonicalization primitives as
`F3_H8_X83_ORBIT_CERTIFIER_SKELETON.md`.  It does not claim any global
certificate.  It verifies that:

- the router priority is `7,5,3,1`;
- routed counts add up to routed canonical supports;
- canonical supports split into routed plus high-odd-zero unrouted supports;
- the local high-odd predicate agrees with the existing parity helper.

Default sample size:

```text
2048 anchored supports.
```

Environment controls:

```text
F3_H8_ROUTER_P
F3_H8_ROUTER_START_RANK
F3_H8_ROUTER_MAX_SUPPORTS
```

## Consequence

The h=8 non-antipodal residual can now be attacked chart-wise:

```text
canonical non-antipodal support
  -> high-odd-zero skip, or
  -> chart 7 / 5 / 3 / 1 route.
```

This is mainly useful for focusing future Modal certifiers and symbolic joins:
chart `7` can be handled first without double-counting supports that also lie
on larger odd charts.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_odd_chart_router.py
```

Expected digest:

```text
H8_ODD_CHART_ROUTER_PASS
```

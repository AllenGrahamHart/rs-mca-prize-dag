# F3 h=8 odd-chart structural partition

Status: PROVED STRUCTURAL COVER, NOT AN h=8 CERTIFICATE.

This packet separates the proof-level chart partition from the bounded dry-run
sample in `F3_H8_ODD_CHART_ROUTER.md`.

## Statement

For an h=8 x83 full-zero support, the parity reduction proves:

```text
non-antipodal => at least one of c15,c13,c11,c9 is nonzero.
```

Define the priority route

```text
c9  != 0  -> chart 7
c11 != 0  -> chart 5
c13 != 0  -> chart 3
c15 != 0  -> chart 1
```

using the first nonzero coefficient in that order.

Then every non-antipodal x83 full-zero support lies in exactly one of these
four routed chart cells.

## Proof

Existence is the contrapositive supplied by
`F3_H8_X83_PARITY_REDUCTION.md`: if all four high odd coefficients vanish, a
full-zero support has an even locator and is antipodal.

Uniqueness is by the priority rule.  Even if several high odd coefficients are
nonzero, the first nonzero one in the fixed order is unique, so the routed
cells are disjoint.

Thus the four chart systems in `F3_H8_ODD_CHART_RECOVERY_COMPILER.md` form a
disjoint cover of the remaining primitive non-antipodal x83 branch.

## Role

Future h=8 certifiers may route by this partition without relying on the
bounded sample in the router packet.  What remains open is still the hard
certificate:

```text
prove every routed non-antipodal support is not x83 full-zero, or route it to a
paid quotient/norm-gate event.
```

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_odd_chart_partition.py
```

Expected digest:

```text
H8_ODD_CHART_PARTITION_PASS
```

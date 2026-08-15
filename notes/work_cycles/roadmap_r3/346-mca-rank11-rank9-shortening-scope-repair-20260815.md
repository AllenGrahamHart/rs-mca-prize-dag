# Cycle 346: MCA rank-11 rank-nine shortening-scope repair (2026-08-15)

An attempted one-replacement rank-eight coupling exposed a row mismatch in
the green rank-nine target elimination node.

## Retracted low-row argument

The nine-cell pair-core theorem is an original-row theorem. Its
`134944=2m-n` intersection floor applies after a residual chart has been
lifted back to length `2097152` and support size `1116048`. That lift inserts

```text
1048576-K'
```

deleted locator coordinates into every owner core. Consequently an
original-row common core of size at least `134944` does not imply a residual
common core of that size. The former comparison

```text
134944 <= |J| < m'=67472+K'
```

mixed original and residual rows and is invalid. It has been removed from
the statement, proof, contract, and both verifiers.

## Surviving weighted theorem

The marked component lower bound and rank-nine weighted cap use the same
residual `(record,T)` unit and are sound. Their honest first crossing is

```text
K'=20617:
  demand=92386821615379573,
  cap   =92394042904582935;

K'=20618:
  demand=92397581841774591,
  cap   =92395178310909600.
```

Before rounding, the first row has negative cross-product and the second has
positive cross-product. After cancellation, the ratio is

```text
constant * C(m',9)/C(n',9) * (m'-9)/n',
```

a product of ten strictly increasing factors. Therefore the repaired node
is PROVED on `20618<=K'<=1048576` and explicitly open on
`10<=K'<=20617`.

The rank-eight high-row capacity cut was audited separately. Its proof uses
only the weighted concentrator and rank-eight owner-pair cap, so the
unnecessary rank-nine dependency was removed without changing its exact
`K'=37996` boundary.

```text
result:                PROVED rank-nine closure on K'>=20618
retraction:            low-row original/residual core comparison
DAG status delta:      rank-nine rows 10..20617 reopened
rank-eight delta:      none; independent K'>=37996 cut retained
delta-star movement:   none
compute:               constant-memory exact integers under RAMguard
next route action:     derive a residual-unit plane/chronology cap for
                       K'<=20617, preserving marked extension weight
```

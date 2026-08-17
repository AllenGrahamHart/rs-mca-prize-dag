# O0b split cell-0 component Klein-four quotient

- **status:** PROVED
- **scope:** the complete equal-sign cell-`0` A/B outside ledger

Simultaneous `B<->C,E<->F` maps

```text
A_s -> A_-s,    B_s -> B_-s,    x -> -x,
```

and preserves all source and target guards. It commutes with `d->-d` in
`S0` and with the duplicate-record swap in `SDE/SDF`. The exact orbit census
is

```text
S0:       36 size-2 + 192 size-4 = 228 representatives /   840 cases
SDE/SDF: 120 size-2 + 360 size-4 = 480 representatives / 1,680 cases
total:                              708 representatives / 2,520 cases.
```

The canonical representative list has SHA-256
`23d7e403e420307b5466ffaf6d2af59d0cf9a4a93766b4d0bcf68231aba1a741`.
A 24-representative pilot subcover meets all 56
`component/lane-orbit/outside-sign/missing-record` strata and has SHA-256
`47ef7c3a9a92ac2bcb08462377195c0576c2495b0ff1f7c0948103d10e02bc27`.

## Falsifier

Failure of component-relation covariance, loss of a case under either
action, noncommutation, a different orbit profile, or a different canonical
representative hash or pilot-cover hash.

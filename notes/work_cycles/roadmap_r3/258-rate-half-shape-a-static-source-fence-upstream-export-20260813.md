# Cycle 258: rate-half Shape-A static-source fence upstream export (2026-08-13)

Cycle 257's proved arbitrary-stagnation construction was exported to the
existing Lane-T packet in `przchojecki/rs-mca` draft PR `#1161`.

Upstream Section 42 records that, for `R=d+n+2` source points and every
`0<=q<=n`, the explicit barycentric weights

```text
omega_x=G(x)/(Q(x)L_U'(x)),       G=(X-a)^(n-q),
```

are all nonzero, give middle Hankel rank exactly `d`, and realize an exact
omitted-recurrence zero run of length `q`. The proof uses the nondegenerate
residue pairing on polynomials of degree below `d`.

The export is deliberately a route fence rather than a Shape-A
counterexample. It proves that static source data, nonzero weights, exact
corank one, replacement minors, and bordered source sums cannot force
regular non-stagnation. The live route must use coupling across parameter
values.

```text
local source:            7041f043656506656ef00d4260f46b6170c0a12e
upstream PR:             #1161 (draft)
upstream commit:         357ca82
upstream section:        42
exact checks:            38804
source pins:             124/124
source subset terms:     560/560
hostile field mutations: 106/106 normal and optimized
row/endpoint movement:   none claimed
next route action:       exploit the common parameter pencil, source
                         partition, split-fiber weld, or collision geometry
```

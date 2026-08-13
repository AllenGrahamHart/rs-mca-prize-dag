# Cycle 254: rate-half shape-A omitted-recurrence upstream export (2026-08-13)

Cycle 253's proved source/Hankel coupling was exported to the existing
Lane-T packet in `przchojecki/rs-mca` draft PR `#1161`.

The upstream Section 40 records

```text
q_delta = length of the initial zero run
          R_(d+1)(delta),R_(d+2)(delta),...,
deg T=e-sum_(r=0)^(n-1)
          deg gcd(H_off,R_(d+1),...,R_(d+1+r)).
```

The consolidated verifier pins the complete local proof packet, checks the
official index weld `R-d-2=n`, and independently replays a finite-field
interpolation fixture with degree drops `2,1,0`. The export explicitly says
that no bound on the nested gcd flag, shape-A exclusion, or row payment is
being claimed.

```text
local source:            5d46985dff2c42dbab5b78794c353ea14c47d447
upstream PR:             #1161 (draft)
upstream commit:         0fe803b364e417e21a33ada3d27410f1f33f62d8
upstream section:        40
exact checks:            37930
source pins:             104/104
hostile field mutations: 96/96
row/endpoint movement:   none claimed
next route action:       constrain the nested gcd flag with the scalar weld
                         and collision jets
```

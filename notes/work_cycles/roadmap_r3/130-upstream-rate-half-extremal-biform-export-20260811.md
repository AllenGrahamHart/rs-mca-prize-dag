# Cycle 130: upstream rate-half extremal-biform export (2026-08-11)

## Cycle pins

```text
our source:      1c967ff948037490f8e7903aa45d168e63ad843f
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
upstream PR:     #1161 amended through c7542daf5b4d0a25f2a0dc013bd03d10405bb2d5
compute:         exact integer replay only
critical open:   28
```

## Lane-T synchronization

Draft PR `przchojecki/rs-mca#1161` now carries the Cycle-128/129 aftermath of
the macroscopic pair floor. The upstream packet records:

```text
three-center source partition;
at least 2e zero-excess minimum circuits;
at least e+6+d_A clean reciprocal locator gates;
the exact dual-GRS biform of bidegree (e-2,p-3);
the two directional split counts at official integers.
```

The source pin moved to `1c967ff9` and the packet prints all twelve SHA-256
statement/proof hashes. Its verifier now checks the biform degrees and split
counts in addition to the pair-floor arithmetic.

The PR is deliberately framed as a Lane-T `ROUTE_CUT`. Upstream's proved
split-pencil ray collapse identifies the deduplicated target with `LineRay`
but supplies no upper bound. The export therefore claims neither a BC
payment nor a finite-row ledger change.

## Burn-down

```text
result:                  EXPORTED the exact extremal residue in upstream
                         base-field split-pencil terminology
DAG delta:               none
critical status delta:   none
upstream terminal delta: sharper named LineRay/split-biform residual
delta-star movement:     none
new assumptions:         none
compute requests:        none
CI:                      Vercel authorization failure only; unrelated
```

Next test whether the biform profile is impossible on its own. If a small
model survives, bank the route fence and retain the extra marked-Hankel or
contact-section coupling as the next necessary input.

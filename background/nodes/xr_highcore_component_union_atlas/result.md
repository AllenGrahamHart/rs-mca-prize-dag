# Replay certificate

The standalone verifier was shipped by content to Modal and replayed in app
`ap-8gMZz7Pi1wy0zShhQzs2Lx`. It returned

```text
XR_HIGHCORE_COMPONENT_UNION_ATLAS_PASS
systems=10648 components=2 grk_sum=14
```

Peak worker RSS was `55 MB`. The exhaustive part checks every three-slope,
one-ray system with error weight at most two on a six-point domain. The
multiray fixture checks two collision components plus an isolated slope and
the integer GRK sum. A mutation that pays each collision edge separately is
rejected because its slope cover overlaps.

The first fixture draft was deliberately not banked: its intended components
shared accidental size-`R` cross-unions and therefore formed one component
under the theorem's actual adjacency relation. The corrected disjoint-block
fixture above is the replayed certificate.

After manifest refresh, the repository-wide Modal replay passed `125/125`
verifiers with no failures, timeouts, hash mismatches, or remote errors in app
`ap-iyQ9RM3QaRw9ORZjATFc1X`. The five integration gates passed in
`ap-V4BKfrJcQpgFasV2sUOGo2`, independently retaining the nine-node critical
frontier. The critical orbit was rebuilt remotely in
`ap-ECKKfEZYnUhMJ7IybdjPtF`.

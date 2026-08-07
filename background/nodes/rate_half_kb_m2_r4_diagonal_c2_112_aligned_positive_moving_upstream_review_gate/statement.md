# KoalaBear aligned-positive moving upstream review gate

- **status:** PROVABLE
- **scope:** the twelve literal
  `{M00,M01,M02,M03} x {R02,R11,R20}` aligned-positive cells
- **candidate proof:** Przemek repository PR #1144, commit
  `05ff2348de8f2c0f99683875ff12a9a79dcf21ec`
- **consumer:** source-line literal-assignment coverage

The pinned upstream packet claims exact named-open emptiness of all twelve
moving-moving cells. It directly rebuilds eight cells, transports the three
`M01 -> M02` companions by literal `b -> b^-1`, and imports the independently
GREEN `M00-R11` theorem from PR #1138.

The exact Python certificate replay at the pinned commit passes with payload

```text
343b691abab47586545aca75393bea1e1fff1dfb63537f059e4faef341893145
```

and all 29 semantic mutations caught. However, the candidate theorem's own
status and final section retain a fresh independent review gate for the
load-bearing Sage/Singular calculation. This local node therefore remains
PROVABLE rather than PROVED.

Promotion requires a reviewer to replay the Sage compiler and Python
verifier at the exact commit, inspect the two balanced parity chains and
their nilpotence witnesses, and confirm the operational PR #1138 import.

## Falsifier

A missing direct cell, failed literal transport, bad operational import,
nonempty named-open parity stage, content-pin mismatch, or independent review
that rejects a load-bearing Sage branch.

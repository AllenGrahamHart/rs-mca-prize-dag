# KoalaBear aligned-positive moving upstream review gate

- **status:** PROVABLE
- **scope:** the two residual balanced cells `M01-R11` and `M02-R11`
- **candidate proof:** Przemek repository PR #1144, commit
  `05ff2348de8f2c0f99683875ff12a9a79dcf21ec`
- **consumer:** source-line literal-assignment coverage

The pinned upstream packet claims exact named-open emptiness of all twelve
moving-moving cells. Independent replay now proves ten of them in the
sibling ten-cell import node. The unresolved candidate is `M01-R11`; literal
`b -> b^-1` would then transport its conclusion to `M02-R11`.

The exact Python certificate replay at the pinned commit passes with payload

```text
343b691abab47586545aca75393bea1e1fff1dfb63537f059e4faef341893145
```

and all 29 semantic mutations caught. The standalone exact M01 parity
derivation also passes. The complete direct cell cannot yet be independently
replayed: three Sage installations fail with `RecursionError` while
converting the external Singular `slimgb` basis, and an equivalent
`libsingular:slimgb` replay timed out after 1740 seconds. Three direct
standalone Singular routes independently recover the exact pinned q-slice
basis (`168`, dimension `2`) and `J` augmentation (`174`, dimension `2`).
They also close the `w=0` boundary when included, but monolithic and staged
reduction of the 151178-term `I` polynomial exceed 1740 seconds. Splitting
`I` into 148 deterministic 1024-term blocks still completes fewer than eight
blocks in 3540 seconds. This node therefore remains PROVABLE rather than
PROVED.

Promotion requires a portable exact replay or an independent exact proof of
`M01-R11`, followed by the already checked complete-source inversion to
`M02-R11`. The next replay must change the reduction geometry, for example by
interreducing or parametrizing the `J` quotient; merely extending the direct
`I` timeout is fenced out. The result must bind the q-slice basis, both parity
stages, localizers, and nilpotence witness without relying on a failed text
bridge.

## Falsifier

A surviving named-open `M01-R11` point, a failed literal transport to
`M02-R11`, a content-pin mismatch, or an exact replay that contradicts a
pinned basis, localizer, or nilpotence terminal.

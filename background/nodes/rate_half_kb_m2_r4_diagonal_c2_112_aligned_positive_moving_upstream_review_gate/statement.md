# KoalaBear aligned-positive moving upstream review gate

- **status:** PROVED
- **scope:** the two residual balanced cells `M01-R11` and `M02-R11`
- **candidate proof:** Przemek repository PR #1144, commit
  `05ff2348de8f2c0f99683875ff12a9a79dcf21ec`
- **consumer:** source-line literal-assignment coverage

The pinned upstream packet claims exact named-open emptiness of all twelve
moving-moving cells. Independent replay proves ten of them in the sibling
ten-cell import node and also checks the complete literal `M01 -> M02`
inversion. This node proves the remaining `M01-R11` representative and hence
its `M02-R11` companion.

The exact Python certificate replay at the pinned commit passes with payload

```text
343b691abab47586545aca75393bea1e1fff1dfb63537f059e4faef341893145
```

and all 29 semantic mutations caught. The standalone exact M01 parity
derivation also passes. A direct Singular replay avoids Sage's failing basis
conversion. It obtains the pinned q-slice basis (`168`, dimension `2`) and
`J` augmentation (`174`, dimension `2`), interreduces the same-ideal `J`
generators, and reduces all 148 deterministic blocks of the exact
151178-term `I` polynomial. The resulting `I` remainder has degree `19` and
`4435` terms, exactly the upstream metrics. A fresh `slimgb` basis of the
augmented ideal has size `168`, dimension `2`; the 20-factor named localizer
has degree `29`, `10653` terms, and square zero. The separate exact staged
trace closes the `w=0` boundary.

`interred` is not used as a claimed standard basis. Each division step gives
an exact same-ideal remainder, and the final `slimgb` is computed from those
same-ideal generators plus that remainder. Thus the terminal localizer
nilpotence is an exact certificate for the original q-slice, `J`, and `I`
ideal. The proved complete-source inversion transports emptiness to
`M02-R11`.

## Falsifier

A surviving named-open `M01-R11` point, a failed literal transport to
`M02-R11`, a content-pin mismatch, a missing one of the 148 `I` blocks, or an
exact replay that contradicts the final localizer-square-zero terminal.

## MCA O0b `FFF` reduced-`q5` bottleneck (2026-08-17)

### Exact checkpoint

The normal-form-first square-subsystem run preserves the section-408
necessary-superset logic: `E=e^2`, `q4` is omitted, and every admissible
`FFF` point satisfies the retained `q5,q7,q6` equations. The run reduced
`q5` modulo the proved 21-element common basis before any outside equation
was adjoined.

```text
q5 normal-form degree: 90
q5 normal-form terms:  4,717
next operation:        adjoin reduced q5
outcome:               timeout during that operation
Modal app:             ap-MhIhFWNqjNHO5cnOhY7yX9
```

The timeout has no proof status. It does show that equation order and a
single whole-polynomial normal form do not control the expression growth.
Increasing the same run's duration or memory is not the next gate.

### Next decision gate

1. Use the known low degree of the unreduced `q5` expression in `s` to write
   it exactly as a short coefficient sum in `s`.
2. Reduce each coefficient polynomial modulo the common base basis in the
   smaller coefficient variables and rebuild the exact reduced equation.
3. Factor or stratify the rebuilt equation before adjoining it. A unit
   necessary subsystem closes `FFF`; a nonunit basis becomes the exact input
   for `q7,q6` and eventually the omitted `q4` equation.
4. Do not promote the representative or repeat a monolithic `q5` basis run.

### Resource discipline

Local work remains RAM-guarded. Any Singular reduction or basis construction
runs on Modal in one preregistered bounded worker with retained partial
output.

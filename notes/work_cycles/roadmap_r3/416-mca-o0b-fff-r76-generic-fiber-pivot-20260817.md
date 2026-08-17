## MCA O0b `FFF` R76 generic-fiber pivot (2026-08-17)

### Retired product route

The first 128-term block of `M0[0]` squares to only 1,232 terms, but its
degree-128 reduction modulo the five-variable graph basis exceeds sixty
seconds at 2 GiB. Term count is not the governing complexity; splitting
further would create hundreds of shards while retaining high-degree
reduction.

```text
input terms: 128
raw square:  degree 128, 1,232 terms
normal form: timeout
Modal app:   ap-At0hOIj97ZuTPfosolIzNn
```

This timeout has no proof status. Deterministic term-block multiplication is
retired as the primary route.

### Generic-fiber route

The admissible ratio graph is one-dimensional in `x,t,r,c,b`. Treating
`t` as transcendental changes the coefficient field to `F_p(t)` and
leaves a zero-dimensional ideal in `x,r,c,b`. This is the natural setting
for multiplication and for eliminating `s,E`.

### Next decision gate

1. Recompile the 48-element admissible graph basis in
   `F_p(t)[x,r,c,b]` and retain the generic-fiber basis.
2. Record every coefficient denominator introduced by the generic basis and
   its reductions. The generic theorem applies only where their product is
   nonzero.
3. Reduce the 14 bracket representatives, the q5 coefficients, and the
   eventual common-root norm in the finite generic algebra.
4. Create separate finite exceptional-fiber leaves for every base-field root
   of the denominator product, together with the existing route guards.
5. A generic unit plus complete exceptional-fiber exclusions closes the
   necessary subsystem; no generic result alone promotes `FFF`.

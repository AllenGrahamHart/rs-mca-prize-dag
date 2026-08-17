## MCA O0b `FFF` generic `q5` extension (2026-08-17)

### Exact result

The generic `q5` extension is finite and nonempty:

```text
q5 input terms:       24
basis dimension:      0
basis size:           16
quotient dimension:   16
coefficient entries:  192
distinct denominators: 100
Modal app:            ap-h3NTK3YvbAxOLtnLf7sLZ4
```

The basis SHA-256 is
`bd4b2bf32d58c5f344d8d244eb2632646f0a7ca807bbefc5cf1c9c3737d6ab3b`;
result SHA-256
`b5320657fc191da5adf2743ad020ab6a30934fd584f7f3f3a995caf9a712953c`.

### Next decision gate

Write

```text
q7 = D0 + D1*E + D2*E^2
```

and reduce `D0,D1,D2` first in the dimension-eight base algebra, since none
depends on `s`. Their representatives embed unchanged into the `q5`
extension. Adjoin the resulting quadratic in `E` to the 16-element basis,
then impose `q6` only on that finite extension.

### Proof boundary

The `q5` branch survives generically; this is not evidence against the full
necessary subsystem. The 100 output denominators and transformation pivots
remain specialization obligations.

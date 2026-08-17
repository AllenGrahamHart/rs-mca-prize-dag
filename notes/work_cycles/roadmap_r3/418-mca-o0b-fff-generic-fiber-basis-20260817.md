## MCA O0b `FFF` generic-fiber basis (2026-08-17)

### Exact result

The admissible ratio graph over `GF(2130706433)(t)` is a finite algebra:

```text
source polynomials:        48/48
Groebner-basis dimension:  0
Groebner-basis size:       10
quotient dimension:        8
rational coefficients:    90
distinct denominators:     44
Modal app:                 ap-dshGHUIh6cSEc6EJmDphMN
```

Groebner.jl's `isgroebner` check passed. The full basis and every coefficient
numerator and denominator are retained in the result artifact. The hostile
checker accepts the exact ledger and rejects all four mutations. The result
SHA-256 is
`c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e`.

### Proof boundary

This is a structural reduction, not an `FFF` closure. It applies only away
from roots of the 44 basis denominators and does not yet adjoin the necessary
equations `q5,q7,q6`. Those equations may now be reduced in an
eight-dimensional algebra rather than in the original one-dimensional
five-variable quotient.

### Next decision gate

1. Factor the square-free product of the 44 denominators over the deployed
   field and retain exactly its base-field roots as exceptional `t` fibers.
2. Reduce `q5,q7,q6` in the generic finite algebra and certify whether their
   extension is the unit ideal, collecting every new denominator.
3. If the generic extension is unit, specialize the original admissible
   graph and necessary subsystem at every collected exceptional root.
4. Promote `FFF` only after the generic branch and every exceptional fiber
   are both empty; otherwise retain the surviving specialized component.

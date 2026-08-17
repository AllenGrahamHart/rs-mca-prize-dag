## MCA O0b `FFF` generic denominator roots (2026-08-17)

### Exact result

The 44 denominators in the generic basis have raw degree sum 1,013 but LCM
degree only 49. Their complete deployed-field root set is

```text
0
1
16711679
666570304
676802667
1141382033
2113994754
2130706432 = -1
```

For each denominator, FLINT computed `gcd(D,t^p-t)`, factored the square-free
field part into linear factors, and reconstructed it from the roots. The
union agrees exactly with the independent computation on the LCM. Modal app
`ap-OWgH6QIeyDAsAMnej0nU6T` completed in 0.017 seconds; the result SHA-256 is
`7489a4c860059240395ed0e1b264f5643ba58fe257076781a0bb596e582738b0`.

### Proof boundary

These eight fibers are exactly the specialization exceptions for the
current 10-polynomial generic basis. They are not yet checked against the
FFF necessary subsystem, and reductions of `q5,q7,q6` may introduce more
denominators.

### Next decision gate

1. Adjoin `q5,q7,q6` over `GF(p)(t)` to the 48 source equations or their
   certified 10-polynomial generic basis.
2. Certify the extended Groebner basis and collect every additional
   coefficient denominator.
3. If the extension is unit, merge all additional base-field roots with the
   eight-root basis set and replay each specialized finite fiber.
4. If it is nonunit, retain its exact generic component and derive the next
   algebraic obstruction instead of expanding another resultant.

# Result

All four residual WCL divisor ideals now have an exact sparse arithmetic-
circuit presentation. After removing deterministic low-degree squarings and
substituting the terminal remainder, the four systems range from `52`
variables and `54` equations to `114` variables and `119` equations. Every
equation has degree at most three and no expanded coefficient of
`Y^1024 mod G` is formed. A checked integer Nullstellensatz identity in these
equations is a complete characteristic sieve endpoint.

This removes expanded SymPy remainder arithmetic from the requested route.
It does not compute a certificate, estimate elimination cost, or promote a
slot.

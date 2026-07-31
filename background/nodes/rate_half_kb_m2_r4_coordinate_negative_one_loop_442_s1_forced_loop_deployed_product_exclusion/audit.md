# Audit

1. Nonsquareness of `-m` is checked separately in both cubic components.
2. Tower inversion uses the exact quadratic norm, so no quotient-ring
   zero-divisor is treated as a field element.
3. Both parity signs and both cubic base components are replayed.
4. The conclusions are raw unit ideals, not guard saturations.
5. Each verifier handles one cubic base component and remains below 60
   seconds.
6. No transport to another common sign row is counted.

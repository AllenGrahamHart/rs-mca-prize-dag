# Audit

1. The packet is a fresh finite recomputation; it does not specialize the
   generic colored Bezout multipliers at their pole values.
2. Every parent factor preserves its full degree, and all returned finite
   factors are independently checked irreducible and monic.
3. Degree-one factors are treated as irreducible; the earlier checker bug on
   this base case was repaired before producing the packet.
4. The primitive-coordinate identity is checked on all 433 rows.
5. A non-linear primitive factor is excluded only because an actual packet
   makes the primitive coordinate `F_p`-valued.
6. Every scalar outside gcd is factored independently; target-collision rows
   have no root outside the printed nonzero/square-distinctness guards.
7. The result closes 23 fibers, not the remaining 46 or the sign row over all
   deployed `t`.
8. Hostile mutation of a closure reason or target coordinate is rejected.

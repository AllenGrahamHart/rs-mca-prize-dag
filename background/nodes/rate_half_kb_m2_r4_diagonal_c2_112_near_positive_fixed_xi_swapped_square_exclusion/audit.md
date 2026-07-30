# Audit

1. The swapped mode relies on the two stated parents for reconstruction
   invertibility and forced-square divisibility. It independently solves the
   source and recomputes every swapped endpoint and middle equation.
2. No endpoint line is divided out globally. Its full leading-zero locus is
   handled by a separate base resultant.
3. Primary elimination uses resultants in `c`; independent elimination uses
   Bezout identities over `QQ(d)[c]` and exceptional resultants in `d`.
4. The independent `c=-1/2,-2` fibers are checked explicitly rather than
   discarded as generic coefficient branches.
5. Both paths reduce their certificates modulo the deployed characteristic.
6. Every task is one endpoint pair under `timeout 60s` and `ramguard tiny`.
7. The exact-monomial coefficient mutation that invalidated the first chart
   attempt remains an active regression test in every shard.

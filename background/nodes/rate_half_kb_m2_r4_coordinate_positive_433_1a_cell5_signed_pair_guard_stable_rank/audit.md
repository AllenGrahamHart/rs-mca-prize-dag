# Audit

1. The base is `F_p(t)`, not every deployed `t` fiber.
2. The number 24 is vector-space length.  No reducedness or component count
   is inferred from it.
3. Squaring `z0,z1` loses source signs; the theorem does not claim a guarded
   source-root lift.
4. Only chart 2 and the `DE+/DE-` pair are present.
5. The colored `BE` cubic and unsquared sum row are not present.
6. The primary exact solve and independent NTT checker use different
   arithmetic implementations.  The latter also checks the exported basis
   file and canonical hashes, all 18 leading monomials, and the count of 64
   standard monomials.  The NTT degree bound is 380 and all 512 roots are
   used.
7. Hostile deletion of a shard, alteration of one exact coordinate, and a
   one-byte packet mutation are all rejected.
8. No route, K3 row, or Prize status changes from this theorem alone.

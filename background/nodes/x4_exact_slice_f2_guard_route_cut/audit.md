# Audit

1. The proof is uniform in the real field-size parameter `L`; the printed
   `L=255.9` table is replay evidence, not a hypothesis.
2. Rate `1/2` is the worst binomial case at the comparison depth. The three
   lower rates are farther from the central slice.
3. The `129`-bit gap uses one comparison step below `t0` and the lower field
   bound `L>=128`; `L<256` leaves over `641` bits of Hoeffding room.
4. The theorem is stronger than a non-generating-row scope cut: it also
   excludes all five generating signed types at exact-slice depth.
5. The conclusion is only that the guarded F2 route is unavailable. Combined
   with pigeonhole it also fences an unweighted full-cube max route, but does
   not refute the fixed-slice extras budget.

# Audit

1. The distance estimate is on the symmetric difference of error sets and
   uses `g=a-k+1`, including the `+1`.
2. Functionals are counted projectively. There are `N_r` classes in total
   and `H_r` classes through one nonzero vector.
3. One good functional must keep all `L` projected polynomials distinct;
   preserving agreement alone is insufficient.
4. `D subset F` is what lets an `F`-linear functional commute with polynomial
   evaluation.
5. The strict inequality makes the average collision deficit less than one.
   A non-strict average does not force a zero-deficit functional.
6. `(SD2)` is a threshold equivalence, not an upper estimate.
7. The upstream numeric row uses `2^-100`. The local grand-prize target is
   `2^-128`, so the specialization is not wired as a row closure.
8. For target-dependent use, set `L=B*+1` and check `(SD1)` with exact
   integers at the actual candidate agreement.

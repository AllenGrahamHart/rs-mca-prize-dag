# Audit

1. The proof selects exactly `a` agreement coordinates per codeword; agreement
   sets larger than `a` do not weaken the argument.
2. Pairwise intersection is bounded by `k-1`, not `k`, because a nonzero
   degree-`<k` difference polynomial has at most `k-1` roots.
3. The balanced integer degree expression is exact. Replacing it by the
   real-valued Cauchy lower bound loses the useful small-`B` improvement.
4. The strict inequality in `(IJ2)` is necessary. Equality between the lower
   and upper pair ledgers does not rule out a family.
5. `a_IJ` is a safe anchor only. Failure of the integer Johnson test at
   `a_IJ-1` is not an unsafe witness and does not close adjacency.
6. At the prize maximum, the anchor ranges from `3n/4` for `B*=1,2,3` down
   to the first strict Johnson coordinate once `B*>=332114441762`. Thus it is
   materially stronger than the trivial `a=n` safe endpoint but remains far
   above the cyclic unsafe floor.

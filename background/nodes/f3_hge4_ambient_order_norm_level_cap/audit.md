# Audit

1. `p==1 mod n` implies complete splitting at every level `m|n`.
2. The lower norm exponent is `floor(h/2)`, the number of positive odd
   integers below `h`; it is not `ceil(h/2)`.
3. Primitivity is needed to make the first cyclotomic integer nonzero.
4. The strict inequality uses primality: `p>=n^2` and `n>1` imply `p>n^2`.
5. The cap uses `ceil(ma/(8s))`; replacing `ceil` by `floor` is not justified
   by the strict real inequality.
6. At `m=n` the formula must reproduce `m/4-1`, not claim a new top-level
   deletion.
7. The cap deletes both free and antipodal-swap pairs because it is applied
   before that stabilizer split.
8. The rational contraction is `36/25`, justified by the strict elementary
   bound `log 2<25/36`; replacing it by `3/2` makes the local inequality false.
9. Since `m/4` is even, `h=m/4-d` has the same parity as `d`. The odd branch
   loses one full factor of `n`, producing the extra `100s` term.

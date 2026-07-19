# Claim contract: C36' cutoff-18 weighted excess

- **claim id:** `f3_h3_mobius_excess_half`
- **statement:** for every official row, `17X_18<=300n^2` with the exact
  `P`, `R`, and `X_18` definitions in `statement.md`
- **scope:** all `n=2^s`, `13<=s<=41`, and all official primes
  `p=1 mod n`, `p>=n^2`
- **consumer:** `f3_h3_three_to_one_c36`, nonidentity rich-fiber tail
- **status:** `TARGET`
- **proved dependencies:** quotient-block identity, paired PGL2 identity,
  cutoff-18 compiler, rich-fiber norm cutoff, same-fiber ideal batching,
  distance-two 2-primary exclusion, low-distance ideal-star router,
  distance-four cross-overlap router, weighted multistar router,
  rich-excess multistar degree ladder, prime-alignment criterion, and exact
  excess-budget/degree tradeoff, high-excess low-distance moment reduction,
  edge–quotient incidence router, distance-four fiber-degree cap,
  high-excess distance-six reduction, antipodal-tail distance-six split, and
  C36' arithmetic
- **new open content:** on the proved-reduced range
  `n^2<=p<=6^(n/4)`, a joint product/quotient correlation estimate; the
  selected target pays `P<=32` by quotient mass and retains the refined exact
  `P>=33` moment `136(42M_6,33^0+53M_6,33^A)<=1113B_n`, where `M^A` is
  the unique-antipodal-target lane; proved analytic Pareto alternatives use
  `P>=25` at `E=6` or `P>=29` at `E=10`; the broader alternative remains
  `S_ns^rich<=1200n^2` on `P(t)>=19`
- **falsifier:** one exact official row with `17X_18>300n^2`
- **current proof route:** prove the `E=6` disjoint-support moment
  `D_6,25^0+(17/10)D_6,25^A<=(223/20)n^2`; all overlapping-support and
  antipodal-edge exceptional families are already paid by quotient mass. The
  fixed-order alternative remains at `E=14` and needs algebraic principal-
  prime generation before the exact weighted-multistar sieve
- **replay:** `python3 critical/nodes/f3_h3_mobius_excess_half/verify.py`
- **upstream mapping:** primitive shift-pair control / exact residual ray
  compiler

Do not replace the joint target by a marginal shifted-energy bound, and do not
consume a pointwise constant-fiber conjecture as a theorem.

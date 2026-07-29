# Audit

- The block kernel itself need not be a direct product; the argument uses
  its derived subgroup, whose projections are exactly the simple socles.
- Nontriviality of each kernel projection is proved by the outer-stabilizer
  order bound, not assumed from generic linear disjointness.
- Scott's lemma permits twisted diagonals. The proof retains all automorphism
  twists and checks the exceptional `M12` pair explicitly.
- The independent-socle case is killed only after importing the proved
  same-inner-fiber exclusion for the actual quartic suborbit.
- A `D_alpha` orbit is contained in the actual `G_alpha` orbit because
  `D_alpha <= G_alpha`; no equality of stabilizers is assumed.
- The `r=2` deletion uses both size four and the block projection. It does
  not delete any `r=4` branch profile or move an owner charge.
- `verify.py` independently enumerates the invariant strip partitions and
  route arithmetic. `verify_audit.py` reconstructs the paired `M12`
  permutation group from the printed ATLAS generators.

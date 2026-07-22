# Audit

- **Truth status:** PROVED by the module-basis argument in `proof.md`.
- **Object check:** the coefficient ideal is invariant under every
  unimodular polynomial basis change, not only constant changes of basis.
- **Exactness check:** squarefreeness is used when dividing one locator root;
  it is supplied by `W|Omega` on a distinct evaluation domain.
- **Direction check:** content roots imply extra agreements by division in
  the module; extra agreements imply content roots by uniqueness of module
  coordinates.  Both directions are proved.
- **Counting check:** the theorem identifies the primitive residual but gives
  no estimate for it.  `l1_mixed_petal_amplification` remains TARGET.
- **Replay:** `verify.py` exhausts all degree-below-three codewords and every
  level-three support on a nontrivial `F_7` fixture, including nonprimitive
  one-shell descents and two polynomial-unimodular basis changes.
- **Negative controls:** `verify_audit.py` rejects nine scope or identity
  mutations.

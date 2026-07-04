# lattice_cone_certificate

- **status:** TARGET
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

For a knife-edge row's specific p: a printed lattice certificate (dual/transference bound restricted to the sparse ternary cone, or exhaustion over reduced bases) proving K_p contains no ternary vector of support <= 2l' beyond the cyclotomic relations — certifying FULL injectivity in one per-row computation. Replaces the generator-design existence question as certified_valueset_lower's primary route; fits the repo's certificate grammar (the knife-edge certificate becomes a lattice certificate).

## Attack surface

DECOMPOSED: multiplier lemma (elementary) -> weight-graded MITM (provable radius extension 7 -> ~12 swaps per row) -> k-multiplier reduction (GV-favorable at k ~ 10) -> integer_code_distance_cert (the residue: one small explicit matrix per row). E24's BKZ hunt is the search-side complement throughout.

## Falsifier

BKZ finding a sparse ternary kernel vector = an actual collision = the collided branch is REAL at that cell (a zone-(b) verdict, not a route failure)

## Ledger (migrated notes)

The proof-logging certifier now aligns with the prize's own formal-verification-encouraged criterion — not just convenient, textually favored. | C-4 (#217): the toy pipeline VALIDATED — direct mod-p MITM and the exact B&B totality anchor agree exactly (288 antipodal cyclotomic relations, zero non-cyclotomic at N'=16, p=12289, w<=6); corrected N'=128 MITM costs: w=12 at 2^38.3, w=14 at 2^43.5, w=16 at 2^48.4. The Reading-B anchor works end to end at toy scale.

# stratification_partition_thm

- **status:** see dag.json (single source of truth; dag status PROVED)
- **statement provenance:** written 2026-07-27 (empty-statement remediation / sketch-tagged re-grade);
  see notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md and SKETCH_TAGGED_REGRADE.md

## Statement

THE T0-T7 FIRST-MATCH STRATIFICATION IS A PARTITION (total and pairwise disjoint) of the pair space. Precisely: for fixed exact agreement A (t = A-k, j = n-A) let Pi_A be the ordered pairs (u,v) of syndrome vectors at exact agreement A, so that the whole pair space is the disjoint union Pi = disjoint-union over A of Pi_A. The tree defines a classification map cls : Pi_A -> {T0,...,T7, L} (the eight gates plus the terminal residual leaf L), and the theorem is that cls is WELL-DEFINED and EVERYWHERE-DEFINED — every pair lands in exactly one cell. Machine-checked by this node's verify.py (exhaustive toy-model check + fuzz spec). Consumers: strat_tree takes it as its single predicate ('every pair enters exactly one T0-T7 cell'), and safe_assembly_uniformity clause (ii) is exactly this partition ('the stratified sum with first-match dedup composes'). [statement written 2026-07-27 from this node's own proof.md, which transcribes wp_detail/wp2_3_stratification_case_tree.md section 2]

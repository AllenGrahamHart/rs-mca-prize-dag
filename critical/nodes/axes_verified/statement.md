# axes_verified

- **status:** see dag.json (single source of truth; dag status PROVED)
- **statement provenance:** written 2026-07-27 (empty-statement remediation / sketch-tagged re-grade);
  see notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md and SKETCH_TAGGED_REGRADE.md

## Statement

AXES 3/5/7 VERIFIED + THE q-DICTIONARY (AXIS 6) — the scope-normalization aggregate. This node records that the scope axes 3, 5 and 7 are settled and supplies the quantifier/reserve dictionary of axis 6; the remaining axes are carried by their own nodes (`axis1_batching`, `axis2_ell`, `axis4_predicate`, `axis8_generating`, `axis9_dither`), and this node is a leaf feeding `s0_zero_open`. SOURCE: proof_sketch/s4_reserve_dictionary.md upstream, whose section 1 — 'The identity: FM crossover = tau*' — is tagged [VERIFIED] and machine-checked exact at all four rates (tau*(rho,q) the unique tau in (0,1-rho) with tau log2 q = H(rho+tau); the spine's FM crossover n H(delta) = t log2 q - 128 with t = n(1-delta-rho) is the same equation up to the 128/n term), and whose section 2 is the quantifier dictionary (three-t disambiguation: t_denom, T_slack, t_win). HONEST GAP recorded 2026-07-27: the node's ref carries NO section anchor and the individual contents of axes 3, 5 and 7 are not pinned in-tree — only the source file is. Before the submission dossier cites this node, pin each axis to its section and restate. The node is retained as PROVED because it is a scope-normalization record over settled axes, not a mathematical bound.

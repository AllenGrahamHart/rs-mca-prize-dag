# q_recursion

- **status:** see dag.json (single source of truth; dag status PROVED)
- **closure:** proof
- **statement provenance:** written 2026-07-27 during the empty-statement remediation; see notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md

## Statement

[transcribed 2026-07-27 from the upstream source read via git -C ../rs-mca show origin/main:experimental/notes/roadmaps/proof_sketch/s3b_ii_strip_periodic.md#2; the recursion itself is the proved multi-scale reduction (x1 quotient reduction, on main)]. THE MULTI-SCALE QUOTIENT RECURSION Q_M(H_n) = Q_1(H_{n/M}), rate-preserved. For UNSTRUCTURED pairs periodic locators receive no alignment boost — FM1 gives the same q^{1-t} per locator and the periodic strata are exponentially thin (C(n/M, j/M) against C(n,j)) — so their first-moment mass is negligible. The paid quotient mass comes from STRUCTURED pairs, where the t syndrome conditions fold to ~t/M conditions on the quotient row, boosting the probability to q^{1-t/M}; that folding is exactly the recursion above. SCOPE FENCE: the surrounding section is tagged 'SKETCH on proved parts' — only the recursion and the FM/thinness facts are claimed here.

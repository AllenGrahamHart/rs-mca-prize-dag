# char0_collision_classification

- **status:** see dag.json (single source of truth; dag status PROVED)
- **statement provenance:** written 2026-07-27 (empty-statement remediation / sketch-tagged re-grade);
  see notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md and SKETCH_TAGGED_REGRADE.md

## Statement

CYCLOTOMIC RIGIDITY (thm:rigidcyclo, tex/slackMCA_v4.tex upstream). Let N = 2^s and A subset mu_N subset Z[zeta_N] with p_1(A) = 0 in Z[zeta_N]. Then A is a union of antipodal pairs {omega, -omega}. Proof: in the power basis 1, zeta, ..., zeta^{N/2-1}, sum_{a in A} a = sum_j c_j zeta^j with c_j = 1[zeta^j in A] - 1[-zeta^j in A] in {-1,0,1}; vanishing forces c = 0, i.e. each antipodal pair is contained in or disjoint from A. CONSEQUENCE (the classification this node names): every CHARACTERISTIC-ZERO witness for V_2 is of COSET type, and the characteristic-zero slack-2 value set is exactly the ladder rung 2 * m^(mu_{N/2}). SCOPE FENCE (load-bearing, from the same source's rem:wall): this classifies the characteristic-ZERO witnesses only. Asymmetric elements of V_t require cancellations of size comparable to p and are 'genuinely modular, i.e. subgroup equidistribution' — that residual is NOT claimed here. [transcribed 2026-07-27]

# wild_row_audit

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: TARGET]
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/e36_pgl2_stabilizer.md']

## Statement

For the admissible wild rows (n in {2^13, 2^17, 2^19, 2^31}, q = (2^m - 1)^{2s} < 2^256): (a) enumerate exactly which (n, q, coset) pairs are wild (cosets of mu_n inherit wildness by scaling conjugacy); (b) the quotient taxonomy there = the Dickson subgroup lattice of PGL_2(F_{n-1}) (Borel, cyclic, dihedral, A_4, S_4, A_5, subfield PSL/PGL) — each subgroup class a candidate quotient stratum; (c) the unsafe side GAINS: more symmetry = more window families at wild rows — recompute the census window arithmetic there (thresholds may differ from tame rows; the determination is per-row, so wild rows get their own richer analysis, not a program failure); (d) the weight-2 inverse and completeness statements gain wild-row cases with Dickson conclusion spaces.

## Attack surface

pure arithmetic for (a); Dickson's classical theorem for (b); the existing census machinery transported for (c); toy laboratory: F_49/mu_8 (fully computable wild row)

## Falsifier

an invariant structure at a wild toy row outside the Dickson-derived strata (F_49/mu_8 is exhaustively checkable)

## Ledger (migrated notes)

QA.23 (16/16): the wild-row arithmetic CLOSED (exact admissible list) + the F_49/mu_8 toy fully audited (Dickson strata + window arithmetic); the prize-scale Dickson budget theorem honestly left open — needed only if a wild row is ever submitted, and the family's tame rows suffice for the three-rate campaign. | QA.23 detail (#17): 26 admissible wild rows enumerated exactly; the F_49/mu_8 Dickson toy shows NO escape, but Dickson-derived window PARTITIONS need their own census column at wild rows (unsafe side bookkeeping, queued with the dossier).

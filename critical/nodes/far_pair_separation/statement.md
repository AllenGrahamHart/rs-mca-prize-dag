# far_pair_separation

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: TARGET]
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

Construct class families F with |F| > B*/poly whose pairwise e1-differences all factor as (unit of height < p^{1/phi}) x (one of g <= poly generators). Then g per-row valuation checks certify ALL pairs of F simultaneously — constant per-row computation replacing 2^244 pairwise checks. The open problem is the DESIGN: Sidon-flavored difference structure in Z[zeta_N'] compatible with the class-to-e1 map. DECOMPOSED: = cluster_certificates (free cliques + one-check pairing + integer freebies, PROVABLE) + generator_economy (multiplicative difference-designs — the sharpened open core, with the root-difference factorization as its proved germ).

## Attack surface

toy design search at small N' (measure achievable |F| vs g); telescoping-chain and hierarchical-core approaches provably fail by height_only_impossibility unless generator-factored; the difference-set literature in abelian groups is the import candidate

## Falsifier

n/a (construction target); partial designs have PROPORTIONAL value — census_window_arithmetic converts any achieved L into decided window fractions

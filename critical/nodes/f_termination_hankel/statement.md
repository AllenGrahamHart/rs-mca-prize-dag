# f_termination_hankel

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: CONJECTURE]
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s3b_iii_3_fibers_and_noanchor.md#1']

## Statement

RESTATED after the E17 COUNTEREXAMPLE (#210, pre-registered falsifier fired): Hankel-kernel sparse dual words are NOT always coset-patterned — an exact j=5,t=3 kernel plane has a support-{2,3} weight-2 word, not a coset pair. The termination bound for the Hankel family must come from the GENERAL support-lattice accounting (f_support_lattice) with Hankel-specific closed-set counting, or a refined displacement structure theory beyond coset patterns. The observed support was still SMALL and LOCAL (adjacent exponents) — the restated question: are Hankel sparse-word supports always low-diameter/structured, if not coset?

## Attack surface

first step is EVIDENCE: rerun the E9 census RESTRICTED to Hankel-kernel flats and record the support patterns (predicted: unions of cosets); then the lattice bound via the displacement identities

## Falsifier

a kernel-flat sparse word with non-coset support in the restricted census

## Ledger (migrated notes)

E17 verdict: coset prediction FALSE; adjacent-exponent counterexample recorded with certificate. Pre-registered response executed: fall back to the general lattice argument. Falsification count for my leaps now 2 (of 5) — the cycle is honest.

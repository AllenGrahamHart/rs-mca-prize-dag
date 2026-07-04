# f_gcd_reduction

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s3b_iii_3_fibers_and_noanchor.md#1']

## Statement

Let w = deg gcd(P cap D_j). Division by the gcd maps P cap D_j injectively into P' cap D'_{j-w} for an explicit linear P' of dim <= dim P over the co-domain (X^n-1)/gcd, with trivial image gcd. Hence F reduces to gcd-trivial planes; the deep-gcd branch IS the tangent shape.

## Ledger (migrated notes)

Codex red-node pass (2026-07-04): banked as PROVED. Elementary:
multiples-of-ell_W form a subspace; division is linear | IN FLIGHT: PR #182
(Codex) proves this (verifier replayed green locally, 13792 reduction checks;
tip adds a bonus common-root consumer bound). Flips to PROVED on integration.

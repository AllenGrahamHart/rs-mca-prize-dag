# Ideal/Galois multiplicity node verification - contract-check repair

- **date:** 2026-08-06
- **preceding app:** `ap-kaveXQab3dd0pe4ot3QnS1`
- **preceding mathematical verifier:** PASS
- **failure class:** equivalent-scope wording rejected by an over-literal
  static assertion

The contract already says `no uniform percentage`; change the independent
verifier to require that exact committed phrase instead of `not uniform`.
No theorem, proof, result, manifest, numerical checker, or DAG edge changes.
The wrapper writes a new immutable result filename and reruns both verifiers
against the same compiled DAG.

One Modal container, one CPU, 1 GiB RAM, 120 seconds, no retry.  Only a final
`2/2` PASS authorizes promotion.  Any failure ends this verification route
and leaves the node unpromoted.

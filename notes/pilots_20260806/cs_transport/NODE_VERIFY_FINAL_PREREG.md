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

## Result

Modal app `ap-MCOrXFtNvxPe9tbqfvGCl6` returned `2/2` PASS.  The primary
verifier reported 816 norm checks, 1,104 finite-field divisibility checks,
the exact first-excluded boundary, and both DAG evidence edges.  The
independent verifier reported the two boundary checks, all 65 tower checks,
preserved failed-run provenance, and the tamper contract.  Result JSON
SHA-256:
`ae71d6737c1b98809640d70bbdc58fb37560d45f43d9316b6cb7be2144cb687c`.

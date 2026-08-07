# F2 admissible Newton-distance transport - preregistration

- **date:** 2026-08-06
- **candidate node:** `f2_admissible_newton_signed_distance`
- **candidate status:** PROVED

Replay the exact DAG contract and exhaust every signed support of weight at
most `2R` on three small prime-field half-systems.  The rows are
`(p,S,R)=(17,8,3),(97,16,2),(193,32,2)`.  The verifier must also reproduce
the official witness floor `2R+1=S/32+89` and find both PROVED requirement
edges plus the evidence edge to the TARGET F2 close.

Run in one fresh Modal worker with one CPU, 1 GiB RAM, a 120-second function
cap, a 90-second subprocess cap, and no retry.  Only a zero return code and
the printed PASS marker authorize banking the node.  The finite sweep is an
implementation audit; the general result rests on the written Newton proof.

The first launch, Modal app `ap-Kose4zOz3KyYDwrvxaoIYk`, failed during
launcher import because its repository-root calculation did not account for
Modal's `/root` import path.  No verifier code or mathematical check ran.
The launcher was repaired to use `/repo` remotely and to request zero
retries; the registered rows and verdict rule are unchanged.

## Result

Modal app `ap-lOOp59znUr1hMtB85YraY7` returned PASS with 328,240 exhaustive
small-row checks, the exact official floor `8,589,934,681`, and the complete
`2 req + 1 ev` DAG contract.  The captured result has SHA-256
`a83976944a52d87b33b5a51735118202cfbf15dbd6f42086b5fdd1c1c78ff3d0`.

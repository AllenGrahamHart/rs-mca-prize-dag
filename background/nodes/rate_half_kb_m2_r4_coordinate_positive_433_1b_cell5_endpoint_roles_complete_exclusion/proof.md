# Proof

Fix one of the four signed source rows and one endpoint role. The common-kernel theorem writes the missing record and the endpoint record on the exact guarded cell-5 common curve. The complete-fiber Vieta identities imply the necessary source compatibility equation

`(x^2 A(lambda) + B(lambda))^2 = lambda beta(lambda)^2 x^2`,

where `x` is `b` for `xi=5` and `c` for `xi=6`, and `lambda=-t^2`. Thus any admissible endpoint witness lies in the common ideal augmented by this cut and the deployed nonzero/distinctness guard.

Exact Singular elimination of `z,t,c,b` leaves one monic polynomial in `r` for each sign/endpoint case. The four `b`-endpoint eliminants have degree 16 and the four `c`-endpoint eliminants degree 11. Therefore an admissible deployed witness would give a root of the corresponding eliminant in `F_p`.

The replay factors every eliminant over `F_p` and finds zero linear factors. Independently, the rootlessness audit computes

`gcd(E(r), r^p-r) = 1`

for each of the eight eliminants. This identity is equivalent to absence of roots in `F_p`. Hence no guarded endpoint source candidate exists. The conclusion precedes residual matching, so it excludes all 15 pairings for each of the two endpoints, totaling 30 labels.

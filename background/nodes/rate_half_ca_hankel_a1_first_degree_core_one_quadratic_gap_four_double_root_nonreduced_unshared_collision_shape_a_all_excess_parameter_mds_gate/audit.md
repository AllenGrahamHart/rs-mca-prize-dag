# Audit

1. `D_delta=A_delta R_delta` has degree `n-a_delta`; the padding degree
   cancels between the two known factors and must not be added again.
2. The unknown block is `C_delta=zeta_delta H_delta`, including its scalar.
3. The parity powers are `0<=l<=2e`, giving `2e+1` checks per `X`
   coefficient.
4. Matrix entries are convolution coefficients `d_(delta,i-h)`, not just
   evaluations of the known locator.
5. A valid shape-A kernel must have every polynomial block nonzero; no
   individual coefficient is required to be nonzero.
6. Fiber degree drops are retained through the block degree and are not
   assumed zero.
7. Full rank in the `e=7` probes is not promoted to a theorem.
8. The partition probe exhausts excess partitions, not incidence tables;
   its `630` full-rank outcomes remain numerical evidence.

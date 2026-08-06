## Prize-resolution cycle, 2026-08-06

### WCL `(1,5)` squared-root hypersurface router

The odd-boundary divisor endpoint has been eliminated to one exact symmetric
equation. For a product-one five-subset of `mu_256`, with elementary
coefficients `e_j`, define

```text
d=4e_2-e_1^2,
Psi=(d^2-64e_4)^2-16384e_3+2048e_1d.
```

The candidate lifts to a normalized reduced weight-five relation if and only
if `Psi=0`. On the product-one square-root torus, `Psi` is exactly the product
of all 16 product-one signed sums. A fresh exact Burnside count reduces the
presentation from `2,296,920` signed affine-Galois classes to `289,043`
squared-root odd-dilation classes.

The compression is algebraic, not a closure claim. Norming `Psi` aggregates
the 16 sign-lift norms and makes complete factorization harder, so the paused
direct norm fleet should not be replaced by a blind aggregate sweep. The
router instead exposes one equation on which to seek a split-characteristic
obstruction or structured compatible-prime resultant.

```text
starting pin: edd32a13; canonical f08d96b6; upstream main 93fba1be
open upstream frontier checked: #1145-#1149; no WCL split-gate supplier
node: dli_wcl_weight5_squared_root_hypersurface_router [PROVED]
target: dli_wcl_slot_1_5_emptiness remains TARGET
result: NARROWED and exact route fence
DAG status delta: one proved evidence node; no target promotion
upstream terminal delta: none
delta-star bracket movement: none
new assumptions: none
verifier: exact 530/495-term identity, 128-map Burnside count, small-field iff
compute: local exact arithmetic under RAMguard; no Modal
next: exploit Psi under q=1 mod 2^41; do not resume blind norm factorization
```

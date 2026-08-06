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

### XR broad fiber-rigidity route fence

The round-13 syzygy audit proposed `(FR)`: selected blocks at the
tuple-incidence boundary should be complete `phi=[P:Q]` fibers plus at most
one point.  An exact scaled smooth fixture shows that this does not follow
from primitive deficiency, maximality, tangent saturation, active-defect
locality, `sigma=0`, and the normative first-match selector alone.  Its two
selected blocks both have profile `(2,1,1,1)` across five two-point fibers.

The primary and independently implemented scans each exhausted all
`C(64,4)=635376` interpolation anchors and all 194 projective slopes; twelve
hostile certificate mutations were rejected.  The fixture has affine target
dimension zero and is not an official prize row, so the official first-unpaid
post-envelope `(FR)` remains open.  The result narrows the permissible proof
route: a repaired statement must explicitly consume official-subgroup,
high-affine, or post-envelope structure.

```text
starting pin: 1065918d; canonical 9c3a6d90; upstream main 93fba1be
node: xr_band_forced_commonroot_syzygy_count [TARGET]
result: broad field-independent (FR) FALSIFIED; official scoped (FR) OPEN
DAG status delta: none
upstream terminal delta: none
delta-star bracket movement: none
new assumptions: none
compute: two bounded exact Modal apps, both stopped; independent full replay
next: formulate and attack official first-unpaid post-envelope (FR), not generic local forcing
```

### WCL `(1,5)` complete easy census and one hard tail

The interrupted direct norm route is now complete at easy depth.  Three
missing-only waves plus independent all-volume inventories cover every one of
the `2,296,920` affine-Galois classes.  Of these, `2,296,726` norms are
completely factored; none contains an official-gate prime and the maximum
observed `v_2(p-1)` is 30.  The exact hard-tail manifest has 194 distinct
norms.  A bounded 100-worker campaign completely factors 193, again with no
gate factor and maximum valuation 17.

One 269-bit composite remains.  Two PARI attempts, FLINT, and eight seeded
GMP-ECM workers all reached 300-second caps without a divisor.  It is now a
compact external ECM/QS/NFS request.  Separately, the full easy+tail packet
still needs an independent exact replay; the target therefore remains open.

An independently implemented custody pass now validates all 35,890 easy
summary/shard pairs and reconstructs the exact sorted factor vocabulary:
6,177,403 shard records and 4,443,651 distinct easy factors, with vocabulary
SHA-256
`1abfdfddbb9a168522b9413292cff6064308f9d7a0706b1f5cf34329a0d8bc3a`.
It independently reproduces maximum `v_2(p-1)=30` and finds no official-gate
factor.  This pays compact aggregation/custody, not factor primality or
per-row factor products.  The unexpectedly large vocabulary rules out a
naive monolithic primality pass; the replay must be sharded and separately
priced.

A fixed independent replay pilot then checks 128 batches and 8,152 rows via
direct FLINT resultants, FLINT primality, and trial division against each
stored shard.  All 21,762 sampled primes, 23,091 factor records, four timeout
norms, and both per-batch digests agree.  The projected full audit is about
18,715 CPU-seconds and 187 seconds of idealized 100-container wall time.  This
misses the pilot's deliberately strict 7,200-CPU-second gate but remains a
plausible sub-`$1` grouped audit; it needs a fresh preregistration rather than
an automatic scale-up.

That grouped audit is now complete.  One hundred checkpointed workers replay
all 35,890 batches and 2,296,920 rows using direct FLINT resultants, 6,177,403
FLINT primality checks, and independent trial division.  All 6,528,119 factor
records and every primary digest reproduce; coverage has no duplicate or
missing batch.  The global custody digest is
`975220600606e8f9fac4de09d7d350121ea04ea3de23b9e492fb0651b331e033`.
The easy census is therefore proof-grade.  The exact residual is only the 194
retained hard norms: independently certify the 193 primary factorizations and
obtain one complete factorization for tail 191.

```text
starting pin: fd4f2d23; canonical cee6244c; upstream main 93fba1be
node: dli_wcl_slot_1_5_emptiness [TARGET]
result: full easy census and independent replay COMPLETE; hard tails 193/194
DAG status delta: none
upstream terminal delta: none
delta-star bracket movement: none
new assumptions: none
compute: full replay apps ap-0OBpQSj0V7998tTvkzixwx and ap-y5FDRVADCUfOqoflndTSDg; all apps stopped
next: independently certify 193 tail rows; await complete certified factorization of tail 191
```

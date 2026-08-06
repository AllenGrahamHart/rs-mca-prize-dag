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

The 193 completed hard tails are now also independently certified.  A
content-pinned FLINT checker reproduces the 194-row manifest digest, verifies
all 193 products through 400 primality checks and 399 distinct primes,
reproduces the factor-vocabulary digest, and confirms maximum
`v_2(p-1)=17` with no gate event.  Thus the entire exhaustive `(1,5)` route
has one residual only: complete factorization and independent primality
certification of the explicit 269-bit tail-191 norm.

That final residual is discharged. Official CADO-NFS image
`sha256:d89bc19...fc10` factored tail 191 in 80.457 seconds as a 112-bit
prime times a 158-bit prime. A separate content-pinned FLINT app proves both
factors prime, multiplies them back to the exact norm, and computes
`v_2(p-1)=9,12`. Combining the easy maximum 30, the 193-tail maximum 17,
and tail 191 gives global maximum 30, strictly below the official gate 41.
The finite extension router, norm obstruction, complete replay, and hard-tail
certificates are assembled in the node proof; `dli_wcl_slot_1_5_emptiness`
is now PROVED. The WCL zone residual drops from ten slots to nine.

```text
starting pin: fd4f2d23; canonical cee6244c; upstream main 93fba1be
node: dli_wcl_slot_1_5_emptiness [PROVED]
result: complete 2,296,920-class norm census and all 194 tails certified
DAG status delta: one TARGET promoted to PROVED; WCL-zone residual 10 -> 9
upstream terminal delta: none
delta-star bracket movement: none
new assumptions: none
compute: full replay apps ap-0OBpQSj0V7998tTvkzixwx/ap-y5FDRVADCUfOqoflndTSDg; tail cert ap-beZVadXTE7z94tsQiEsGZ7; CADO ap-gyFwY6AxmBrU0NioPlsJ5C; final cert ap-hMfVc7KQMaSvmDtSO5a9kS
next: export the closed slot and attack the nine remaining WCL cells
```

### Round-17 canonical terminal correction and next WCL endpoint

Canonical Round 17 refutes the proposed four-lane `(ES-G)` weld.  The `u2c`
pin is the surviving global-balance statement, but the other consumers do not
share its regime: the crossing lane fails the deepest stratum at `w=2^34`
on every admissible pair; the rate-`1/16` band is never sub-balance; the low
fifth of the rate-`1/4` and rate-`1/8` band flips; and DLI RES is strictly
above balance by its own `(H2)`.  The roadmap must therefore carry separate
terminals for crossing, band, `u2c`, and DLI rather than treating `(ES-G)` as
a shared discharge.

After the `(1,5)` closure, the next WCL cell is `(1,6)`.  Its direct affine
census has `185,569,028` classes and is not an economical next run.  The
proved even-norm divisor descent instead reduces the cell to six remainder
equations in five variables; their rational ideal is the unit ideal.  The
next exact action is to price extraction of an integer Nullstellensatz
certificate `Delta_6`, not to launch the census.  A complete `Delta_6`
identity plus factor/gate certification would close the slot.

```text
starting pin: e7ec67fa; canonical 4ff7fe51; upstream main 93fba1be
canonical correction: shared ES-G terminal refuted; four lane-specific obligations
node selected: dli_wcl_slot_1_6_emptiness [TARGET]
preferred supplier: dli_wcl_ell1_weight6_even_norm_divisor_descent [PROVED]
DAG status delta: none in this subsection
upstream terminal delta: none; WCL register PR #1050 is closed unmerged
compute: none yet; bounded Singular certificate-pricing pilot next
next: construct the six exact remainders and test rational unit-certificate extraction
```

### WCL `(1,6)` expanded-certificate route fence

The bounded rational pilot removes the expanded six-remainder representation
from the active route.  A minimal Singular image now works, but exact
repeated squaring timed out after 60.010725 seconds before coefficient
extraction; no standard basis or lift was attempted.  This is already the
wrong cost shape, and a longer run would still produce a certificate blind to
the official `v_2(q-1)>=41` gate until its prime support was extracted.

The exact cubic straight-line ideal remains a valid theorem and possible
external endpoint, but there is no current evidence for a tractable
certificate.  The direct alternative has 185,569,028 classes and a projected
cost around `$6.6k`.  Do not spend the current Modal allowance on either
continuation.  The slot remains open and the roadmap pivots to a terminal
with a proved structural advance.

```text
starting pin: edc40e0f; canonical c987f5d1; upstream main 93fba1be
node: dli_wcl_slot_1_6_emptiness [TARGET]
result: expanded rational endpoint TIMEOUT_REMAINDER; representation retired
DAG status delta: none
upstream terminal delta: none
delta-star bracket movement: none
new assumptions: none
compute: app ap-WuMWiEvupHO6w3aghjgG1f, one bounded container
next: no WCL (1,6) compute without a materially smaller gate-aware theorem
```

### Round-17 F2 regression and crossing advance

Canonical Round 17 makes two route-deciding changes. First, `(O1)` is false
on explicit prize-admissible rows when the smooth domain does not generate
the ambient field. On the plus branch `p=1 mod 4`, the exact admissible
decomposition replaces the old 16-rung picture by at most four prime-field
MDS summands and leaves one honest mass terminal, `SL-1b'`; the moving-rung
discharge band is empty. The minus branch was omitted from this Round-17
statement and is corrected below. Any F2 route must therefore cover both
the minus branch and non-generating rows, not silently add either a residue
class or generation hypothesis.

Second, the ideal-level Galois-multiplicity theorem `(CS)` proves the crossing
instance unconditionally whenever

```text
ceil((w-1)/2) log_2 p > (n/4) log_2 r'.
```

At the formal benchmark `log2 p=256`, this covers every
`w>=170,752,922,588`, or 71.16% of the bracket `[2^34,2^39]`. This is not
uniform official-row coverage: `(CS)` depends on the base characteristic
`p`, not the ambient extension-field size `q=p^e`, and smaller `p` leaves a
larger residual (the bound is vacuous throughout the bracket at
`log2 p<=64`). The exact unresolved set is therefore the rowwise set of
`(p,w)` failing the printed inequality, together with the structural
strata. The theorem has now been independently audited and transported as
the PROVED supplier
`rate_half_crossing_ideal_galois_multiplicity_exclusion`, with evidence edges
to the crossing and F2 consumers and no target-status flip. The next useful
attack is the rowwise exceptional-floor sparsity or a stronger norm floor in
the printed low-characteristic/low-window residual.

```text
starting pin: edc40e0f; canonical c987f5d1; upstream main 93fba1be
lane: crossing / F2 quotient-prefix flatness
result: O1 FALSIFIED; CS independently PROVED rowwise, with a 71.16% near-256-bit benchmark
DAG status delta: one PROVED supplier added; two evidence edges; no target flip
upstream terminal delta: potentially shared with (Q), not yet exported
delta-star bracket movement: rowwise partial exclusion; no uniform movement
new assumptions: none for CS; E_floor sparsity remains open below threshold
compute: apps ap-JNBoN1s1INvr1ovkHvbf8h and ap-MCOrXFtNvxPe9tbqfvGCl6, bounded PASS
next: attack rowwise E_floor sparsity or strengthen the norm floor below CS
```

### Round-17 F2 critical-route repair

The critical graph formerly retained the July route
`f2_growing_order_myerson -> f2_conditional_close` even after canonical
Round 17 invalidated its all-row premise. This is now repaired. The
plus-branch admissible-row structure is banked as the PROVED supplier
`f2_admissible_direct_sum_grs_reduction`: for `p=1 mod 4`, every deployed
kernel is a direct sum of at most four explicit prime-field GRS/MDS kernels,
with exact dimension and `Z(L)=Z_1^C`. The false all-row `(O1)` statement is
recorded separately as `f2_all_admissible_o1_mass_bound [REFUTED]`; the
official row `p=3*2^41+1`, `q=p^6` has `ord_n(p)=1<6` and an exponential
`2^(5n/12)` shortfall, with primality certified by Pocklington base 5.

The prize-facing `f2_conditional_close` conclusion is not refuted. It is
now an honest critical TARGET leaf with no logical prerequisites. Its
proved July inputs, the plus-branch direct-sum theorem, the counterexample
alarm, and growing-order Myerson are evidence. The printed attack splits
into: plus-branch generating-row GRS ternary mass, a minus-branch coupled
kernel, a direct non-generating-row payment, the PP5.0 average-to-sum seam,
and any coset-sensitive descent. Myerson remains a useful upstream `(Q)`
target but no longer sits on every prize route.

```text
starting pin: 99a55c51; canonical c987f5d1; upstream main 93fba1be
lane: F2 / quotient-prefix flatness
result: plus-branch direct-sum GRS reduction PROVED; all-row O1 REFUTED
DAG status delta: f2_conditional_close CONDITIONAL -> TARGET; Myerson req -> ev/background
upstream terminal delta: Q remains relevant evidence, not a sufficient all-row close
delta-star bracket movement: none
new assumptions: none; generation explicitly not assumed
compute: apps ap-gc4EOdiUFEghRR4qkIjUfX and ap-bMpQIqA5drSKk82JQgIgGa, bounded PASS
next: attack the plus-branch GRS mass, derive the minus-branch kernel, and formulate a direct non-generating count
```

### Plus-branch admissible F2 Newton-distance transport

The first reusable theorem on the explicit `Z_1` terminal is now banked.
Each plus-branch admissible prime-field class is a half-system generated by
an element of order `2S`, so `p>=2S+1`. Under the deployed initial odd run,
a ternary class word of weight `w<=2R` is exactly a reduced signed polynomial
in the scope of the PROVED DLI Newton short-window theorem. It cannot exist.
Thus the class minimum signed weight is `2R+1`; at the maximal generating
witness this is `S/32+89`, nearly twice the generic GRS/MDS floor.

This does not control the number of words above the floor. The honest
remaining theorem is still the weighted enumerator `Z_1<=2^{o(S)}`.
Canonical Round 18 independently launched adversarial and generative pilots
on this same terminal at `prize@ec542009`; their eventual reports should be
subtracted against this transport before any further node is minted.

```text
starting pin: d64df9ab; canonical ec542009; upstream main 93fba1be
lane: F2 / admissible prime-field ternary mass
result: plus-branch DLI Newton signed-distance law transported, PROVED
DAG status delta: one PROVED supplier; one evidence edge; no target flip
upstream terminal delta: none; Q remains open
delta-star bracket movement: none
new assumptions: initial odd run 1,3,...,2R-1, already the deployed reading
compute: app ap-lOOp59znUr1hMtB85YraY7, 328,240 checks, bounded PASS
next: subtract canonical Round-18 reports, then attack weighted counts above 2R
```

### Plus-branch admissible F2 weighted-prefix L2 identity

The explicit plus-branch ternary mass is now identified exactly with a
second moment. For the odd-moment subset map `Phi` on one half-system, let
`N(v)` be its fiber sizes. Removing the common intersection of an ordered
pair of subsets gives a ternary kernel word, and adding an arbitrary common
intersection reverses the map. Therefore

```text
Z_1 = 2^-S sum_v N(v)^2.
```

Finite Fourier inversion gives the equivalent cosine-product partition
function over the `R`-dimensional family of odd polynomials. The zero mode
is `2^S/p^R`, so the same identity explains why non-generating rows fail at
the entropy-average level. On generating rows, the remaining theorem is
near-diagonal L2 collision mass `sum_v N(v)^2<=2^{S+o(S)}`. This is weaker
than a full max-fiber `(Q)` theorem. Upstream terminology should call it a
restricted weighted odd-prefix L2 instance, not silently identify it with
the standard unweighted quotient fiber.

Each fiber is also a full-agreement list-recovery instance for the explicit
`[S,S-R]` GRS code with two allowed symbols per coordinate. The current
near-capacity RS literature does not supply this endpoint: Guo--Li--
Shangguan--Tamo--Wootters prove existence for selected exponentially-large-
field evaluation sets, and Doron--Venkitesh treat random evaluation points.
Neither theorem covers this fixed dyadic half-system at essentially zero
entropy gap. Import those methods only after an explicit structured-point
specialization; generic-RS language alone is not a proof.

```text
starting pin: ac9d2373; canonical ec542009; upstream main 93fba1be
lane: F2 / restricted quotient-prefix L2 flatness
result: exact ternary-mass/collision/Fourier identity, PROVED
DAG status delta: one PROVED supplier; one evidence edge; no target flip
upstream terminal delta: Q max-fiber implies this instance, converse not claimed
delta-star bracket movement: none
new assumptions: none beyond the proved plus-branch admissible class model
compute: apps ap-Lik7i7u6TSwxHdBhbDIxzK and ap-aKhhNL94Wn8oytoS1Fu1dB, bounded PASS
next: bound the nonzero Fourier mass or L2 excess on generating rows
```

### Round-18 F2 minus-branch correction

The order calculation behind the purported all-admissible direct-sum
reduction omitted `p=3 mod 4`. The official generating row

```text
p=2^61-1, q=p^2
```

is decisive: `p=-1 mod 2^41`, so `ord_(2^41)(p)=2=e`, while
`gcd(2^41,p-1)=2`. After the antipodal quotient its `2^40` positions are
singleton `F_p`-proportionality classes, not at most four classes. The
all-admissible bounded-class reduction is therefore REFUTED. The
`p=1 mod 4` theorem survives and the Newton-distance and weighted-L2 nodes
are now explicitly scoped to it.

This does not refute the F2 prize target. It creates an honest minus-branch
terminal: derive the coupled extension-field odd-moment kernel and pay its
mass or extras directly. Treating the singleton classes as independent
would discard the Frobenius coupling and is forbidden.

```text
starting pin: 8769beba; canonical ec542009; upstream main 93fba1be
lane: F2 / admissible branch classification
result: all-admissible bounded-class reduction REFUTED; plus branch preserved
DAG status delta: one REFUTED route alarm; three PROVED nodes scope-corrected; no target flip
upstream terminal delta: Q remains open; a new coupled minus-branch instance is exposed
delta-star bracket movement: none
new assumptions: none
compute: apps ap-gD4VmoDpSyQJ2F6a5xsRnQ and ap-nC5KaETV5g1U6tiXAhfyDg, bounded PASS
next: derive the exact p=3 mod 4 coupled kernel before further mass experiments
```

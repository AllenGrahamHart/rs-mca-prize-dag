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

### Round-18 F2 coupled minus-kernel close and canonical harvest

Canonical `prize@feadaa03` completed four Round-18 pilots. The valid new
field-generic contribution is THEOREM Z-FLOOR: for every rank-`d` linear
syndrome map,

```text
2^m Z=sum_v N(v)^2,  Z>=max(1,2^m/p^d).
```

This is now the self-contained PROVED node
`f2_weighted_kernel_collision_floor`. Canonical's generating census is not
imported: its proof explicitly says admissibility forces
`v_2(p-1)>=39`, again omitting `p=3 mod 4` and the official M61 row.
Its route-(b) display also uses the unweighted factor `1+2cos`. The exact
weighted Fourier factor is `1+cos=2cos^2`, now included in the generic
supplier; any upper-mass attack must start from that normalization.

The minus branch itself is now structurally closed by the PROVED node
`f2_minus_branch_coupled_negacyclic_reduction`. For each exact/nested top
window, write a ternary vector as the coefficient polynomial `P`. The
kernel condition is vanishing at the first `R` odd roots. Frobenius closes
those roots into `hR` distinct roots and their product is one polynomial
`G_W in F_p[X]`; the kernel is exactly `G_W|P`. Thus

```text
window                         h        rank
exact order 2^40 or 2^41       2        2R
nested order 2^40              2        2R
nested order 2^41              k        kR, k in {2,4}
```

The mass has an exact global L2 collision identity and pointwise floor, and
the DLI transport gives ternary distance `2R+1`. It does not factor over
the `2^40` singleton proportionality classes. The remaining minus terminal
is now only the coupled-code mass upper bound. A scan of all 29 current
open `przchojecki/rs-mca` PRs (`#1121`--`#1149`) found K3/L1/list-special
packets and no overlapping F2 or `(Q)` packet to subtract. The corrected
branch census, M61 counterexample, coupled minus-kernel theorem, and Fourier
normalization have now been exported for independent upstream review as
draft PR `przchojecki/rs-mca#1150`; this custody event does not change a DAG
status or assert upstream acceptance.

```text
starting pin: 8418fe26; canonical feadaa03; upstream main 93fba1be
lane: F2 / ternary-in-cyclotomic-code
result: generic Z-FLOOR PROVED; minus top-window kernel/rank/L2/distance PROVED
DAG status delta: two PROVED suppliers and two evidence edges; no target flip
upstream terminal delta: canonical ternary-in-code primitive corrected to include the minus branch
upstream custody: draft PR https://github.com/przchojecki/rs-mca/pull/1150
delta-star bracket movement: none
new assumptions: none; initial odd run and official 2R<2^36 are deployed facts
compute: app ap-3u4NDxYLTav3KGsvw6nnhN, bounded PASS
next: seek one upper-mass theorem covering plus GRS and minus Frobenius-closed root codes
```

### F2 heaviest-fiber interface and Mint-4 subtraction

Canonical `prize@5a8f0dba` minted the Round-18 F2 reports into three
background nodes. Their generic collision floor is already imported, but
their all-admissible census is not: `f2_admissible_object` and
`f2_o1_status_split` again derive the generating classes only from
`v_2(p-1)` and therefore omit the official M61 minus row. The local critical
route remains the scope-corrected statement of record until canonical makes
the same branch split.

The PROVED `f2_admissible_generating_branch_classification` now completes
that split. Generating rows have exactly three plus types
`(v_2(p-1),e)=(>=41,1),(40,2),(39,4)` and two minus types
`(v_2(p+1),e)=(>=40,2),(39,4)`. All five are nonempty. The new
minus/order-four witness is `p=25*2^39-1`, `q=p^4`; a complete-factor
Pocklington certificate proves primality and exact arithmetic verifies the
order and field cap. Thus M61 is not an isolated omitted case.

The follow-on PROVED `f2_admissible_degree_order_classification` removes the
remaining extension-degree ambiguity. There are exactly 12 signed
`(valuation,k,e)` types and seven are non-generating: plus/order-one with
`e=2,3,4,5,6`, plus/order-two with `e=4`, and minus/order-two with `e=4`.
The apparent `e=6,k=2` type is empty: the field cap leaves nine elementary
characteristic candidates across the two branches and every one has a
printed proper divisor. The direct non-generating payment can now be posed
against these seven exact families.

The collision identity now has the exact PROVED upper interface
`f2_weighted_mass_max_fiber_sandwich`. If `M=max_v N(v)`, then

```text
M^2/2^m <= Z <= M.
```

Thus a row-sharp bound for this explicit syndrome map,
`M <= Lambda_Q*(2^m/p^d)+E_Q` pays the weighted F2 mass with the identical
constant pair and no Fourier loss. This applies to the plus-branch GRS maps
and the coupled minus-branch root-code maps. Upstream `def:q-row-atom` is not
automatically such a bound: it concerns the first-match residual family
`P_Q(z)` on different deployed adjacent rows. An explicit map-and-owner
transport is still required. The sandwich does not prove that transport or
the max-fiber bound.

A primary-literature refresh found capacity list recovery for random
evaluation sets (Doron--Venkitesh, arXiv:2404.00206) and zero-error
list-recovery discrepancy for random linear codes (Doron et al.,
arXiv:2606.24471). Neither theorem covers the fixed dyadic subgroup or its
Frobenius-coupled minus branch. The residual is therefore exactly the
explicit row-sharp `(Q)`/binary full-agreement fiber bound, not a generic RS
list-recovery corollary.

```text
starting pin: 5d9afd69; canonical 5a8f0dba; upstream main 93fba1be
lane: F2 / row-sharp quotient-prefix flatness
result: 12 degree/order types and seven non-generating families classified; mass sandwich PROVED
DAG status delta: three PROVED suppliers and seven edges; no target flip
upstream terminal delta: a proved Q-to-F2 map/owner transport would make Q a sufficient supplier
upstream custody: draft PR https://github.com/przchojecki/rs-mca/pull/1150 at bb045450
delta-star bracket movement: none
new assumptions: none
compute: local tiny verifiers only, 110 exact checks; no Modal spend
next: attack max_v N(v) on the five generating types and seek direct extras payments on the seven non-generating types
```

### F2 generated-field ambient descent

Canonical `prize@d6cfa1d7` added the Round-18 admissible-object packet and
preregistered four Round-19 ternary-mass pilots. The composite
`f2_admissible_object` cannot remain PROVED as written: it applies the
plus-branch `v_2(p-1)` order/class model to every row, while the exact M61
minus-branch witness has `ord_{2^41}(p)=2=e` and `2^40` singleton
prime-field proportionality classes after antipodal quotienting. The node
is therefore REFUTED, with its valid field-cap, trace-rank, and
coset-invariance components retained at their corrected scopes.

The new PROVED `f2_generated_field_ambient_invariance` removes the seven
non-generating families as separate final block/kernel obligations. Write
`F=F_{p^e}`, `B=F_p(mu_n)=F_{p^k}`, and `D=g mu_n`. For `S=gT`,

```text
sum_{x in S} x^j = g^j sum_{y in T} y^j,
e_j(S) = g^j e_j(T).
```

Hence scalar descent preserves the exact t-null blocks, equal-moment
pairs, complements, subgroup-coset and trade families, and every relevant
syndrome kernel. At matrix level `A_D=diag(g^ell) A_B`, so the
`F_p`-kernel, rank, weighted ternary mass, subset-syndrome fibers, maximum
fiber, and collision sum are identical. The seven non-generating types
therefore descend exactly as follows:

```text
plus k=1, e=2,3,4,5,6 -> plus k=e=1
plus k=2, e=4         -> plus k=e=2
minus k=2, e=4        -> minus k=e=2
```

All 12 official degree/order types now reduce to the five signed generating
types. This theorem does not restore the false ambient-normalized `(O1)`,
prove a weighted-mass upper bound, discharge PP5.0, or pay the final `n^3`
extras budget. Draft upstream PR `#1150` now carries the theorem and exact
replay at commit `bbd61489`; this is a review handoff, not upstream
acceptance.

```text
starting pin: a5e3b98d; canonical d6cfa1d7; upstream main 93fba1be
lane: F2 / generated-field normalization
result: ambient-extension axis CLOSED by proof; 12 official types reduce to five generating signed types
DAG status delta: +1 PROVED, canonical false composite PROVED -> REFUTED; F2 target remains TARGET
upstream terminal delta: draft #1150 extended with generated-field descent at bbd61489
delta-star bracket movement: none
new assumptions: none
compute: local exact F25/F5 replay only; no Modal spend
next: prove a common upper-mass theorem for the five generating signed types and settle PP5.0
```

### F2 fixed-weight flatness bridge

Canonical Round 19 (`prize@fed71a06`) proved that the shared ternary-code
framework does not itself discharge F2: the F2 object sits at the critical
mass threshold, while the crossing/ES instances sit in an emptiness regime.
It also killed the proposed pointwise Weil route after restoring its omitted
degree factor; the bound is vacuous by 26 bits at the official witness. The
remaining character formulation is a tail-count problem, not a
nontrivial-character cancellation problem.

The new PROVED `f2_fixed_weight_flatness_mass_bridge` replaces the need for
a full-cube max-fiber theorem by a fixed-weight one. For a linear map on
`{0,1}^S`, write `B_b=binom(S,b)`, `M_b` for the largest syndrome fiber on
weight `b`, and let `T_G` be the total binomial mass outside a good weight
set `G`. If

```text
M_b <= L(1+B_b/Q)  for b in G,
```

then, with every cross-weight collision retained,

```text
Z <= 3 T_G^2/2^S + 3L(S+1+2^S/Q).
```

When all weights are covered the factor is `2` and the tail term vanishes.
Complementation identifies weights `b` and `S-b`. Consequently
`log L=o(S)`, `2^S/Q=2^o(S)`, and omitted tails
`T_G=2^(S/2+o(S))` suffice for the required full-cube mass. Equivalently,
one needs mean-plus-one flatness only on a central binomial band whose
complement has entropy at most `1/2+o(1)`.

This is exactly the normalization shape of upstream
`prob:capfr1-master-flatness` and `prob:capfp-Q`, but not yet an object
identification: the F2 map has weighted odd-power columns and uses the full
fixed-weight slice, while upstream Q is unweighted or pruned by a
first-match owner. The theorem is exported in draft PR `#1150` at
`f15c8b07` with 4,601 replay checks.

```text
starting pin: 117e84c09; canonical fed71a06; upstream main 93fba1be
lane: F2 / fixed-weight split-locator flatness
result: fixed-weight mean-plus-one flatness on a central band implies full-cube mass
DAG status delta: +1 PROVED supplier; F2 target remains TARGET
upstream terminal delta: draft #1150 extended with the exact bridge at f15c8b07
delta-star bracket movement: none
new assumptions: none in the bridge; the fixed-weight flatness estimate remains open
compute: four tiny exhaustive maps, 130 local checks; no Modal spend
next: prove weighted odd-prefix mean-plus-one flatness on the central band for the five signed generating types
```

### F2 antipodal-selector transport to split-locator flatness

The PROVED `f2_antipodal_selector_prefix_transport` removes the weighted-map
seam left by the fixed-weight bridge. For a binary word `x` on a cyclic
half-system `H={theta^s:0<=s<m}`, choose `theta^s` when `x_s=1` and
`-theta^s` when `x_s=0`. This bijects the cube with the antipodal
transversal `m`-subsets of `mu_(2m)`. Their moments satisfy

```text
p_l(E_x)=2 A(x)_((l+1)/2)-c_l  for l odd,
p_l(E_x)=c_l                   for l even.
```

Thus every full-cube F2 syndrome fiber is exactly the transversal part of
one ordinary central fixed-size, depth-`2R` power-sum fiber and injects into
the full fiber. Since `p>2R` on every official row, Newton identities turn
this into the standard top-`2R` split-locator prefix fiber. The theorem
applies to both the plus GRS class matrices and the minus coupled root-code
matrix, up to invertible row scalings, and generated-field invariance covers
all ambient extensions.

This makes upstream `prob:capfr1-master-flatness` a literal common theorem
target rather than an analogy. Moreover, every official selector is
aperiodic in the upstream sense: every nontrivial subgroup of the cyclic
`mu_(2m)` contains `-1`, whereas a selector and its negative are disjoint.
The quotient-periodic support bucket is therefore absent on the transported
F2 images. It does not yet instantiate the upstream normalized band or pay
the common-divisor/first-match owner seam. Nor does it identify the deployed
pruned `def:q-row-atom` family. The transport and aperiodicity corollary are
exported in draft PR `#1150` at `8d89959b`; its replay now has 33,627 checks
and a warning-free seven-page TeX build.

```text
starting pin: 75b97465c; canonical fed71a06; upstream main 93fba1be
lane: F2 / master split-locator flatness
result: every F2 cube fiber injects into an ordinary central depth-2R split-locator prefix fiber; every official selector is aperiodic
DAG status delta: +1 PROVED supplier; F2 target remains TARGET
upstream terminal delta: draft #1150 extended with selector transport and aperiodicity at 8d89959b
delta-star bracket movement: none
new assumptions: none in the transport; master flatness and owner deployment remain open
compute: three tiny exhaustive cyclic fields, 29,026 local checks; no Modal spend
next: instantiate prob:capfr1-master-flatness at the transported parameters and pay the common-divisor/first-match owner seam
```

### F2 selector-face primitive reduction

The PROVED `f2_selector_face_primitive_reduction` pays the
common-divisor and normalization seams left by the selector transport. For
one nonempty syndrome fiber, factor the selector roots belonging to
coordinates fixed throughout that fiber. If all coordinates are fixed, the
fiber is a singleton. Otherwise division embeds the fiber into a punctured
degree-`m-c` locator-prefix instance of codimension `2R`. The residual
selector family has no common root, and it remains antipodal-free, hence
aperiodic. Thus it lies in the primitive gcd-trivial part of the upstream
master-flatness target.

Writing `Delta=m-R log_2|K|`, a primitive flatness bound uniform under these
punctures gives exactly

```text
M_F2 <= max(1, P_*(2m) (1+2^(2 max(Delta,0)))).
```

The locator average is therefore harmless at the saturated official
windows: only the one-condition rounding imbalance remains. Polynomial
primitive flatness would imply `2^o(m)` max-fiber and weighted-mass control.
It would not by itself prove the exact `n^3` consumer ledger.

Canonical Rounds 19-20, now merged through `f4143ab2f`, also rule that
`(O1)` is false and are actively re-posing F2 from the consumer downward.
The historical `2^o(m)` mass target may be stronger than the actual finite
signed-alignment requirement. The face theorem is therefore banked as a
sound optional supplier, while export beyond draft PR `#1150` head
`8d89959b` waits for the Round-20/Wave-47 reconciliation.

```text
starting pin: 0c972e31f; canonical f4143ab2f; upstream main 93fba1be
lane: F2 / primitive split-locator flatness
result: fixed selector roots reduce every non-singleton fiber to a punctured gcd-trivial aperiodic prefix instance, with exact rounding-factor normalization
DAG status delta: +1 PROVED supplier; no critical status change
upstream terminal delta: none; export queued behind the active F2 consumer re-pose
delta-star bracket movement: none
new assumptions: none in the reduction; primitive flatness uniform under punctures remains open
compute: five tiny exhaustive cyclic fields, 6,294 local checks; no Modal spend
next: reconcile the finite signed-alignment consumer; if mass remains required, attack primitive master flatness on the printed punctures
```

### Node-local proof-payload refactor

The large E1 evidence umbrellas had accumulated downstream census and norm
packets after their claims had already been decomposed into narrower DAG
nodes. The physical ownership now matches the theorem graph: 138 production,
launcher, result, and independent-audit files (47,588,230 bytes) were moved
from the E26, E28, E30, and square-mass-18 reduction directories into the 16
existing exclusion nodes whose claims they certify. Shared E30 light atlases
remain with the common profile reducer.

No theorem statement, status, dependency edge, or certificate content
changed. All 27 affected primary and audit verifiers pass, including the full
E26/E28/E30 census summaries and every square-mass-18 cofactor branch. The
compiled graph remains at 1,840 nodes and 5,121 edges. The ownership rule is
recorded in `background/NODE_PAYLOAD_OWNERSHIP.md`: generated packets belong
to the narrowest claiming node, and cross-node storage is reserved for real
shared suppliers.

```text
starting pin: 29d0c3941; canonical 18be2c0c3; upstream main 93fba1be
lane: repository integrity / DAG-local evidence ownership
result: 138 files and 47.6 MB moved to 16 existing theorem owners
DAG status delta: none; 1,840 nodes and 5,121 edges preserved
upstream terminal delta: none
delta-star bracket movement: none
new assumptions: none
compute: verifier-scale local replay only; no Modal spend
next: resume the highest-value live prize dependency after canonical Round-20/Wave-47 reconciliation
```

### F2 consumer guard and depth reconciliation

Canonical Round 20 (`prize@dc3549d00`) re-posed the F2 consumer and exposed
an apparent two-way terminal: under the full-subset balance `(C)`, the exact
first-moment identity yields the finite target `Z(L)<=1+N^3`; after
substituting the exact-slice `(T*)` depth, the same algebra gives an
exact-value obligation with essentially no headroom.

The PROVED `f2_consumer_guard_depth_reconciliation` shows that these are not
two in-scope F2 terminals. Write `q=p^e` and
`B0=F_p(mu_N)=F_(p^k)`. The banked consumer guard is

```text
|B0|^t >= 2^N  <=>  t k log2(p) >= N.
```

At the ambient full-subset depth
`t_C=ceil(N/(e log2(p)))`, this holds exactly when `k=e` on the 12 official
signed degree/order types. If `t e log2(p)<N`, as under `(T*)`, it fails even
when `k=e`, and hence on every official type. Fixed-depth ambient invariance
does not alter this conclusion: it preserves the object at the same `t`, not
a rule that recalibrates `t` from the ambient field.

The critical F2 target is therefore repaired to the guarded statement. Under
`(C)`, attack `Z(L)<=1+N^3` on the five generating signed types. Under
`(T*)`, the exact-value calculation is a route-cut certificate and the proof
must supply a different fixed-slice route or explicitly replace the guard.
No critical status changes: both the finite mass bound and the alternate
slice route remain open.

Upstream remains unchanged at `main@93fba1be`; draft PR `#1150` remains the
only directly relevant open F2 packet, with no review and only its unrelated
Vercel authorization failure. Do not extend it until this scope repair and
the Wave-47 selector packet are reconciled into one reviewable statement.

```text
starting pin: ff97f8ac9; canonical dc3549d00; upstream main 93fba1be
lane: F2 / consumer interface
result: proved guard/depth route split; (C) selects five generating types, (T*) selects none
DAG status delta: +1 PROVED background scope node; F2 target remains TARGET
upstream terminal delta: none; draft #1150 held for reconciliation
delta-star bracket movement: none
new assumptions: none
compute: exact inequality replay only; no Modal spend
next: prove the finite (C) mass bound or construct the alternate exact-slice route
```

### Round-20 completion and exact-slice u2c route cut

Canonical Round 20 is now merged through `prize@23df01a65`. The tail-count
pilot retires the proposed doubling/log-sine lead: it telescopes to the
elementary cost identity. The normalized F2 tail criterion binds at
`c*=1/ln(2)-1`, with zero flat-model margin. The available `R`-local moment
and interpolation supplies miss the required exponent by the quantified
factor `8.60`; no nonlocal supplier is currently named. The crossing pilot
kills the even-condition cover, proves the constant-weight floor on its valid
tower-row scope, and corrects the PT-2 watch line to a field-dependent one.
Neither packet closes a prize node, but both prevent further work on dead
routes.

The PROVED `x4_exact_slice_f2_guard_route_cut` resolves the reopened ensemble
dispatch. Let `N=2^41`, `K=rho N`, `128<=L=log2(q)<256`, and

```text
t_XR=min{t:tL>=log2 binom(N,N-K-t)+128}.
```

For `t0=floor((N-1)/L)`, a one-sided Hoeffding bound at the rate-half
central deviation gives

```text
log2 binom(N,N-K-t0)+128 < t0 L < N
```

uniformly at all four rates. Hence `t_XR L<N`; since
`B0=F_p(mu_N)<=F_q`, also `t_XR log2|B0|<N`. Every official exact-list
depth therefore fails the generated-field F2 guard, including generating
rows. This is not an ambiguity between two admissible F2 calibrations: the
full-subset `(C)` mass problem and the official exact-slice consumer are
different routes.

The critical DAG now owns the missing statement explicitly as
`u2c_exact_slice_extras_budget`. At this round it was posed as the post-strip
exact-slice null residual at most `N^3`; the later consumer-scope audit below
corrects this to a maximum full locator-prefix fiber. This TARGET replaces
`f2_conditional_close` as the requirement of
`u2c_giant_tnull_dichotomy`. The guarded `(C)` F2 target moves to the
background and remains an evidence edge. The `f1/ext` chain is not an
alternate proof: it prices the MCA extension stratum and does not route
guard-rejected generating `x4` rows.

Upstream `main` remains at `93fba1be`. Draft PR `#1150` remains the only
directly relevant open F2/Q packet, with no review, and upstream's row-sharp
Q/Myerson material still identifies an object rather than proving the needed
finite fixed-slice bound. Hold the PR until its scope is reconciled with the
new exact-slice leaf.

```text
starting pin: 9e9b9808c; canonical 23df01a65; upstream main 93fba1be
lane: LIST / u2c exact-slice consumer interface
result: proved every official exact-slice depth lies outside the generated-field F2 guard
DAG status delta: +1 PROVED route cut, +1 TARGET exact-slice leaf; guarded F2 leaves the strict critical orbit
critical census: math 241 (176/40/25), submission 256 (188/42/26); 15-node packaging spine unchanged
upstream terminal delta: none; draft #1150 remains held
delta-star bracket movement: none
new assumptions: none
compute: exact integer inequalities and bounded verifier replay only; no Modal spend
next: attack the post-strip exact-slice zero fiber directly or prove a weight-aware replacement payment
```

### Exact-slice near-tail payment at all four rates

The previous `b2b_near_tail_bound` paid 15 layers only at the rate-half
depth. Its own scope caveat recorded that carrying those same 15 layers to
rates `1/4`, `1/8`, and `1/16` exceeded the reserved `2^122` half-budget.
That gap is now closed without a generated-field balance hypothesis.

For the official exact-list depth `t=t_XR`, the route cut gives `t<N/128`.
Type-class lower bounds on the corridor binomial then give

```text
rho       1/2   1/4   1/8   1/16
C_rho     257   316   472    760
t        >N/C  >N/C  >N/C   >N/C
w_rho      15    14    13     12
```

The banked interpolation inequality

```text
A_(t+j) <= binom(N,j)/binom(t+j,j) < C_rho^j
```

and complementation therefore give

```text
2 sum_(j=1)^(w_rho) A_(t+j) < 2^122
```

at every official row. All entropy comparisons and final budget inequalities
are replayed as exact integer inequalities. The unpaid lower half-band in
the historical null-route middle bands now start at offsets `16,15,14,13`,
respectively. This is a real all-rates null-fiber payment, but it does not
bound any middle layer or arbitrary locator prefix.

```text
starting pin: caf91b93e; canonical 23df01a65; upstream main 93fba1be
lane: LIST / u2c exact-slice near tail
result: proved rate-dependent two-sided near-tail payment at all four prize rates
DAG status delta: no status flip; one proved route repaired and strengthened
upstream terminal delta: none; possible later export as finite list-completion support
delta-star bracket movement: none
new assumptions: none
compute: exact integer inequalities under local RAM guard; no Modal spend
next: audit whether the null-fiber object is the exact-list consumer before
attacking the primitive middle bands
```

### Exact-list consumer-scope correction: maximum prefix, not t-null mass

The audit forced a second, more important correction. For `A=K+t`, an
`A`-subset `S` has monic locator

```text
Q_S=X^A+c_1(S)X^(A-1)+...,
Phi_(A,t)(S)=(c_1(S),...,c_t(S)).
```

For every `z`, the polynomial boundary word

```text
U_z=X^A+z_1X^(A-1)+...+z_tX^(A-t)
```

has an exact bijection between its agreement-`A` codewords of degree `<K`
and `Phi_(A,t)^-1(z)`. Thus a universal worst-word upper ledger must control
the heaviest relevant full prefix fiber after paid first-match strips.

The historical F2 object cannot supply that quantifier without another
theorem. In characteristic `p`, vanishing of the first `t` power sums is
equivalent only to vanishing of the `p`-free locator coefficients; the
`p`-multiple coordinates remain free. Even when `t<p`, raw mode-at-null is
false: over `D=F_17^*`, at `(A,t)=(9,1)`, the null fiber has size `672` and
every nonzero fiber has size `673`. The exact count and the prefix-list
bijection are now banked in the PROVED node
`x4_locator_prefix_consumer_scope`.

Accordingly, `u2c_exact_slice_extras_budget` is re-posed as

```text
max_z |R_z| <= N^3,
```

where `R_z` is the full elementary-prefix fiber remaining after the explicit
`x4` first-match payments. `x4_exactlist_staircase_split` now requires this
target directly. `u2c_giant_tnull_dichotomy` is returned to TARGET and removed
from the strict chain; its extensive F2, complement, edge, and near-tail work
is retained as evidence for a future strip-aware heavy-fiber descent or
exchange-compression theorem. No proof result was lost, but the strict DAG no
longer treats a null/p-free census as a maximum-prefix certificate.

Upstream independently uses this exact distinction: `(Q)` is a maximum-prefix
fiber statement, while its mode-at-null/exchange-compression route remains
open. This correction therefore aligns the critical DAG with the current
`rs-mca` frontier and identifies a clean joint target.

```text
starting pin: fbcc57536; canonical 23df01a65; upstream main 93fba1be
lane: LIST / exact locator-prefix boundary
result: proved the consumer quantifier and removed the insufficient t-null premise from the strict chain
DAG status delta: +1 PROVED scope theorem; historical t-null conditional returned to off-orbit TARGET
upstream terminal delta: none; exact alignment with upstream (Q)
delta-star bracket movement: none
new assumptions: none
compute: 11,692 exact finite checks under tiny RAM guard; no Modal spend
next: prove strip-aware heavy-fiber descent/exchange compression, or attack max-prefix directly by high moments
```

### First heavy-fiber rung: twist-orbit moment amplification

The first upstream `(Q)` rung is now imported and independently proved as
`x4_prefix_twist_orbit_moment`. Multiplication of the domain by `zeta` sends a
prefix `z=(z_1,...,z_t)` to

```text
(zeta z_1,zeta^2 z_2,...,zeta^t z_t)
```

without changing its fiber size. If `I(z)={i:z_i!=0}` and
`s(z)=gcd(N,I(z))`, the orbit has exactly `N/s(z)` equal fibers. Hence one
heavy fiber forces the exact collision-moment contribution

```text
Gamma_r >= (N/s(z)) R(z)^r / |B|^t.
```

At `N=2^ell`, any prefix with a nonzero odd coordinate has a full `N`-element
orbit; larger stabilizers are confined to increasingly even active-index
faces. This is a rigorous first symmetry descent and aligns exactly with
upstream's archived `prop:twist-orbit` / `prop:q-orbit-moment`. It does not
identify even-index faces with quotient-periodic supports and supplies no
moment upper bound, so the maximum-prefix target remains open. Exact replay:
12,870 subsets, 4,881 fibers, 77,953 orbit checks, and moments `2,3,4`.

```text
starting pin: 89dae2543; canonical 23df01a65; upstream main 93fba1be
lane: LIST / Q heavy-fiber symmetry descent
result: proved twist-orbit constancy, exact stabilizers, and moment amplification
DAG status delta: +1 off-orbit PROVED node; no strict status change
upstream terminal delta: harvested one proved Q rung already present in upstream archive
delta-star bracket movement: none
new assumptions: none
compute: bounded exact enumeration under tiny RAM guard; no Modal spend
next: prove that heavy even-index faces descend to paid quotient rungs, or bound primitive high moments
```

### Fixed-weight fence: the full Boolean syndrome route is too large

The characteristic-`p` dictionary gives a valid but potentially lossy
linearization. A full elementary prefix determines all first power sums and,
in particular, its `p`-free power-sum syndrome. Hence each full prefix fiber
is contained in a fixed-weight fiber of an explicit `F_p`-linear map.

The weight cannot be discarded. Strengthening
`x4_exact_slice_f2_guard_route_cut` by one comparison step proves uniformly

```text
t_XR log2|B0| <= N-129.
```

The same syndrome map on all `2^N` incidence vectors has at most
`|B0|^t_XR` outputs, so pigeonhole forces

```text
max full-cube fiber >= 2^129 > N^3=2^123.
```

This is banked as `x4_fixed_slice_pfree_fullcube_route_cut`. It does not
threaten the prize target: the large fiber can collect many weights. It proves
that a direct F2/full-agreement-list-recovery maximum is the wrong supplier;
the proof must retain the exact weight `A`, use weight-resolved high moments,
or preserve an equally strong first-match owner decomposition. The verifier
checks 12,870 fixed-weight subsets and all 65,536 subsets at the finite
conformance row, plus the official integer inequalities.

```text
starting pin: 817c41971; canonical 23df01a65; upstream main 93fba1be
lane: LIST / fixed-slice linearization
result: strengthened the guard cut to 129 bits and proved the full-cube route cannot meet N^3
DAG status delta: +1 off-orbit PROVED route-cut node; no strict status change
upstream terminal delta: none; sharpens the shared Q/F2 route discipline
delta-star bracket movement: none
new assumptions: none
compute: bounded exact enumeration under tiny RAM guard; no Modal spend
next: stay on the constant-weight collision hierarchy or prove strip-aware exchange compression
```

### Exact local reformulation: maximum fiber is primitive shift-pair degree

The corrected target now has an exact local form. After the declared
support-wise first-match strips, join two residual `A`-subsets when they have
the same full depth-`t` locator prefix. The graph is a disjoint union of
prefix-fiber cliques, so

```text
max_z |R_z| = 1 + max_(S in R) deg_R(S).
```

Locator subtraction also proves, in every characteristic, that two distinct
same-prefix supports have Johnson side-distance `e>=t+1`. After their common
core is removed they are a shift pair; at `e=t+1` the two residual locators
differ by a nonzero constant. Thus `u2c_exact_slice_extras_budget` is
equivalent to the uniform local bound

```text
deg_R(S) <= N^3-1.
```

This is banked as `x4_maxfiber_local_shiftpair_equivalence` and aligns the
critical leaf exactly with upstream's primitive shift-pair input. It also
explains why the exact global second-moment identity is insufficient: it
controls the average of these degrees, while one exceptional support decides
the maximum. Exact replay at `F_17^*`: 12,870 supports, 4,881 fibers,
12,743 colliding pairs, and 8,820 top-stratum constant-shift pairs.

```text
starting pin: ffd826c67; canonical 23df01a65; upstream main 93fba1be
lane: LIST / local primitive shift-pair control
result: proved max-prefix/local-degree equivalence and the e>=t+1 rigidity threshold
DAG status delta: +1 off-orbit PROVED adapter; no strict status change
upstream terminal delta: exact adapter from our x4 leaf to upstream SP terminology
delta-star bracket movement: none
new assumptions: none
compute: bounded exact enumeration under tiny RAM guard; no Modal spend
next: bound local primitive shift-pair degree after quotient and moment-trade strips
```

### Exact-list ownership repair: structured Q/MT, primitive SP, and final budget

The repository and upstream scan found no new theorem-bearing PR that closes
the current exact-list frontier. Draft PR `#1150` remains the only directly
relevant open Q/F2 packet and still has no mathematical review. Upstream v13
now states the useful discipline explicitly: a finite upper certificate needs
one priority map, disjoint Q/BC/SP buckets, a coverage theorem, and one summed
numerator. Its primitive shift-pair input also says that the global second
moment does not replace the required local maximum.

Applying that discipline exposed an ownership error in our August 6 re-pose.
The corrected full-prefix quantifier was right, but assigning the entire
post-strip primitive fiber to `u2c_exact_slice_extras_budget` was not. The
historical `x4` graph required both `u2c` and `u1` because they own different
objects:

```text
u2c : structured moment/null and U2-boundary pullback list column;
u1  : primitive star-PTE record population;
x4  : one first-match list assembly and final sum.
```

The PROVED `x4_exactlist_bucket_currency_ownership` theorem now records the
exact algebra. Choosing a base support in one residual prefix fiber injects
every other member into its canonical general order-`t` star-PTE record. Thus
a universal record ledger of size `R` gives a local primitive fiber bound
`1+R`. Moment-null blocks instead generate structured staircases, so counting
blocks or maps does not count their expanded list members. QA.22 remains MCA
per-pair bad-slope arithmetic and cannot by itself certify a per-word list
sum.

Two previously hidden assumptions are now explicit critical leaves:

1. `x4_primitive_star_u1_coverage`: inject every general order-`t` residual
   star record into the exact `u1` ledger with multiplicity one. This must
   justify the current F-4 passage to order-`(h-1)` minimal records or broaden
   `u1` and re-prove its bound. If it lands, the strict `R_min<16n^3` premise
   gives `U_prim<=16n^3` including the base member.
2. `x4_exactlist_summed_budget`: print every consumed official and quotient
   row, actual list-member columns, one priority map, and the exact comparison
   `U_paid+U_QD+U_MT+U_prim<=floor(|F|/2^128)`.

`u2c_exact_slice_extras_budget` is re-posed accordingly as
`max_z |M_z|<=n^3`, where `M_z` is the actual structured moment/U2 bucket
after staircase expansion and coalescing. The guarded F2, near-tail, and
null-fiber results remain relevant evidence for this column. The maximum-fiber
and local shift-pair theorems now feed the primitive coverage leaf.

This repair adds two honest mathematical TARGETs without changing any theorem
status:

```text
math orbit       242 = 176 PROVED / 39 CONDITIONAL / 27 TARGET
submission orbit 257 = 188 PROVED / 41 CONDITIONAL / 28 TARGET
packaging spine   15 nodes, unchanged
```

The immediate proof priority is the coverage leaf. It is algebraic and may
either validate the current minimal-trade `u1` program or show exactly where
that program must be broadened. Only after its multiplicities are known is the
final list-side budget table meaningful.

```text
starting pin: 85826850e; canonical 23df01a65; upstream main 93fba1be
lane: LIST / x4 ownership and finite upper ledger
result: separated structured Q/MT, primitive SP, and MCA currencies; exposed two missing list-side leaves
DAG status delta: +1 PROVED background ownership theorem, +2 TARGET critical leaves
upstream terminal delta: none; exact alignment with v13 coverage and one-budget requirements
delta-star bracket movement: none
new assumptions: none; two old implicit assumptions made explicit
compute: manifest and exact finite verifier replay only; no Modal spend
next: prove or falsify the general-star-to-F-4-minimal u1 coverage map
```

### Route cut: general star records are not universally minimal-coverable

The first coverage attack found that the implicit F-4 passage cannot be an
algebraic convention.  On `F_17^*`,

```text
P={1,2,3}, Q={4,5,14}
```

share `e_1=6`, so they are a general order-1, width-3 star-PTE record.  They
do not share `e_2`, and their two-element sum sets are disjoint, so the record
is neither minimal nor peelable to a contained width-2 minimal trade.

The complete row census gives a cardinality obstruction stronger than this
witness:

```text
general order-1 width-3 records                         4576
minimal records, widths 1..8       120+364+352+126+0+0+0+1 = 963
minimal records, widths 2..8                                   843
```

Thus no multiplicity-one injection from *all* general records into even the
generously padded minimal ledger exists.  The PROVED node
`x4_general_star_minimal_trade_route_cut` has independent prefix-bucket and
union-partition exact replays.

This is not an official-row counterexample: `17<16^2`, and the raw census
precedes the quotient/dihedral/moment/U2/DLI first-owner strips.  It does,
however, decide the next proof architecture.  Coverage must now either prove
that those official strips remove enough nonminimal records to admit an
injective minimal first owner, or re-pose `u1` to count general order-`t`
records and establish a new tail budget.  The existing `14n^3` minimal tail
cannot be transferred by an unproved dictionary.

```text
starting pin: 97ee6fcb0; canonical 23df01a65; upstream main 93fba1be
lane: LIST / primitive SP coverage
result: refuted universal and subset-peeling general-to-minimal bridges
DAG status delta: +1 off-orbit PROVED route-cut node; no critical status change
upstream terminal delta: narrows the finite SP coverage obligation
delta-star bracket movement: none
new assumptions: none
compute: two complete F_17^* censuses under tiny RAM guard; no Modal spend
next: audit the exact u1 counted object, then attack strip-aware official coverage
```

### Currency correction: u1 proves a minimal-record budget

The dependency audit confirms that all four terms in the U16 assembly use
the F-4 minimal currency:

```text
h=1 : zero bookkeeping term;
h=2 : equal e_1;
h=3 : equal (e_1,e_2);
h>=4: explicitly order-(h-1) minimal records.
```

Thus the conditional arithmetic proves

```text
R_min < 16n^3,
```

not a bound on every general order-`t` primitive list record.  The node
`u1_x4_direct_column_budget` is re-posed to exactly that weaker proposition,
without changing its CONDITIONAL status or its open leaves.  Its former
headline silently bundled the separate general-to-minimal coverage theorem
that is now exposed as `x4_primitive_star_u1_coverage`.

The exact-list consumer consequently has two typed inputs: `u1` bounds the
minimal ledger, while the coverage leaf must inject each non-base primitive
list member into that ledger at multiplicity one and preserve every strip.
No theorem was demoted; one over-broad amber contract was corrected.

```text
starting pin: bc7254a0d; canonical 23df01a65; upstream main 93fba1be
lane: LIST / primitive SP currency audit
result: re-posed u1 to the exact F-4 minimal-record theorem its inputs prove
DAG status delta: none; proposition narrowed and coverage ownership made explicit
upstream terminal delta: aligns local u1 with v13 minimal-SP versus coverage split
delta-star bracket movement: none
new assumptions: none
compute: proof-object audit and existing exact assembly replay; no Modal spend
next: classify post-strip general records or broaden the u1 ledger
```

### Critical re-pose: consume the local general-star budget directly

The exact row audit shows that forcing every general prefix record through
the F-4 minimal ledger is stronger than the exact-list consumer needs.  The
primitive bucket is already characterized by the proved star map and local
degree identity.  Its direct obligation is simply

```text
max_z |F_z^prim| <= 16n^3,
```

or, after choosing a base support, local general order-`t` shift-pair degree
at most `16n^3-1`.  This is also the form of upstream v13's primitive SP
input.

The legacy-ID target `x4_primitive_star_u1_coverage` is therefore re-posed to
this weaker, exact consumer statement.  It has two proof routes:

```text
minimal route: strip-aware general-to-minimal injection + R_min<16n^3;
direct route:  bound all surviving general order-t records locally.
```

The route cut kills only a universal version of the first route.  It does not
touch the direct route.  `u1_x4_direct_column_budget` is now evidence for the
minimal route rather than a mandatory requirement of the `x4` assembly.
This removes an unnecessary theorem from the critical ancestry without
claiming any new bound or changing the primitive target's red status.

The strict orbit is correspondingly smaller and better typed:

```text
math orbit       230 = 171 PROVED / 34 CONDITIONAL / 25 TARGET
submission orbit 245 = 183 PROVED / 36 CONDITIONAL / 26 TARGET
packaging spine    15 nodes, unchanged
```

```text
starting pin: 24dec1cc3; canonical 23df01a65; upstream main 93fba1be
lane: LIST / primitive SP local control
result: replaced mandatory minimalization by the exact direct local budget
DAG status delta: target unchanged; u1/F3 minimal branch becomes optional evidence
upstream terminal delta: exact finite alignment with v13 local primitive SP input
delta-star bracket movement: none
new assumptions: none
compute: none
next: attack maximum local general shift-pair degree after the fixed strips
```

### Exact local partition: minimal versus nonconstant difference

The first direct attack now has an exact algebraic coordinate.  For a base
support `S0` and a same-prefix neighbour `S`, remove the common core and put

```text
P=S\S0,  Q=S0\S,  e=|P|=|Q|,
d=deg(L_P-L_Q).
```

The PROVED node
`x4_general_shiftpair_difference_degree_partition` gives

```text
0<=d<=e-t-1,                    e>=t+d+1,
d=0 iff e_j(P)=e_j(Q) for 1<=j<=e-1.
```

Thus the local primitive degree partitions disjointly into `D_0` and
`sum_(d>=1)D_d`.  The `D_0` term is exactly the F-4 minimal/constant-shift
currency developed in `u1`; every genuinely nonminimal record lies in the
nonconstant low-degree-difference incidence branch, starts at side width
`e=t+2`, and remains unpaid.  In particular, small-h minimal results cannot
be presented as coverage of the official general order-`t` fiber.

The row scope is now pinned.  Local official X4 base rows use `N=2^41`,
`K=rho N`, and the exact corridor depth

```text
t_XR=min{0<=j<=N-K : q^j>=2^128 binom(N,N-K-j)}.
```

Upstream v13.2's active deployed LIST rows use `n=2^21`.  The identification
with `prob:capg-active-shiftpairs` is exact at the structural
`(n,m,w)<->(N,A,t)` level, but no finite constant transports between the row
sets.  Quotient rows must likewise be printed and replayed individually.

```text
starting pin: daf87575d; canonical 23df01a65; upstream main 93fba1be
lane: LIST / local primitive SP
result: NARROWED by exact d=0 versus d>=1 partition; official row scope pinned
DAG status delta: +1 background PROVED structural node; critical target unchanged
upstream terminal delta: shared SP low-degree-difference sublemma isolated
delta-star bracket movement: none
new assumptions: none
compute: small exact convention replay only; no Modal spend
next: attack the local nonconstant split-difference incidence sum at d>=1
```

### Upstream SP harvest: exact coefficient-scale quotient sieve

Upstream main already contains a fully proved SP subcase in
`experimental/grande_finale_work/sp_next_section.tex`.  An independent local
proof and exact replay now bank it as
`upstream_sp_coefficient_scale_quotient_sieve`.

For a cyclic multiplicative coset, coefficient gaps characterize subgroup
periodicity exactly.  A shift pair with maximal common coefficient scale
`c>1` descends uniquely by

```text
(n,e,t,d) -> (n/c,e/c,ceil((t+1)/c)-1,d/c).
```

The maximal quotient pair is coefficient-primitive.  In particular
`c|gcd(n,e,d)`, so at local dyadic length `2^41` every quotient-borne
nonconstant pair lies in the even-`e`, even-`d` branch.  All common-scale
mass can therefore be assigned to the quotient owner before the local SP
incidence count.

This is a sieve, not a bound.  The X4 residue is now precisely the
coefficient-primitive part of `D_0+sum_(d>=1)D_d`.  The open upstream PR
`#1150` is a draft correction to the separate F2/max-fiber bridge and does
not supply an SP estimate; no unreviewed PR premise is consumed here.

```text
starting pin: 9c478e255; canonical 23df01a65; upstream main 93fba1be
open upstream PRs relevant to this cycle: #1150 draft (F2/u2c-adjacent, no SP supplier)
lane: LIST / primitive SP quotient sieve
result: HARVESTED exact maximal coefficient-scale quotient extraction
DAG status delta: +1 background PROVED import; critical target unchanged
upstream terminal delta: one upstream SP structural subcase independently banked locally
delta-star bracket movement: none
new assumptions: cyclic multiplicative-coset domain and char not dividing n
compute: 256-subset and 553-pair exact local replay; no Modal spend
next: bound coefficient-primitive nonconstant split-difference incidence locally
```

### First nonconstant SP stratum: translated complementary divisors

For one fixed base support `S0`, the `d=1` part of the local primitive SP
problem now has a certificate-level form.  If

```text
L0=L_(S0),       U=L_(D\S0),       H=aX+b,
```

then neighbours of side width `e` are in exact bijection with

```text
B|L0,            B+H|U,            deg B=e,
deg H=1<=e-t-1.
```

This is `x4_linear_difference_translated_divisor_interface`.  Every such
record is coefficient-primitive because a common quotient scale would divide
`d=1`.  The reduction is exact, but it is not a count.

The most tempting count is false: fixed base and fixed `H` do not determine
the record.  Over `F_17^*`, one fixed five-point base has three distinct
same-prefix neighbours whose reduced locator difference is the identical
`6X+10`.  The explicit locators replay directly.  Therefore neither the
number of possible linear polynomials nor a `q^2` parameter count is a local
degree bound.  The next X4 theorem must bound the translated-divisor
intersection itself while retaining the final first-owner predicates.

```text
starting pin: 7c0ec652d; canonical 23df01a65; upstream main 93fba1be
lane: LIST / primitive SP low-degree difference
result: NARROWED to an exact translated complementary-divisor incidence
DAG status delta: +1 background PROVED interface; critical target unchanged
upstream terminal delta: SP2 now has an exact local divisor formulation and an injectivity route cut
delta-star bracket movement: none
new assumptions: none
compute: tiny F_17 exact replay only; no Modal spend
next: retain first-owner strips and seek a uniform translated-divisor incidence bound; do not count H alone
```

### WCL `(1,6)` first-64 exact falsification panel

The next bounded attack tested the target itself rather than extending the
expensive certificate route. Any reduced signed six-term relation can be
rotated to contain `1`. Removing that term and its antipode leaves 510 roots,
so an exact meet-in-the-middle search needs only

```text
129,540 legal pairs and 21,849,080 legal triples per characteristic.
```

The search exhausted the first 64 certified prime values of
`q=k*2^41+1`, `3<=k<=996`. All 64 rows returned no relation: in total
`8,290,560` pairs and `1,398,341,120` triples were checked. A second
sorted-pair implementation independently replayed the first, middle, and
last rows. The finite theorem is banked as
`dli_wcl_ell1_weight6_first64_mitm_exclusion [PROVED]`.

This is exact falsification survival, not a universal proof. The target
`dli_wcl_slot_1_6_emptiness` remains `TARGET`, and a larger prime panel would
not materially reduce its quantifier. Return now to the structural
even-norm divisor route: seek a smaller gate-aware characteristic-divisor
certificate rather than buying a larger census.

```text
starting pin: 08d5f36fb; canonical 23df01a65; upstream main 93fba1be
open upstream PR relevant to selected lane: #1150 draft, F2 only; no WCL supplier
lane: WCL / (ell,h)=(1,6)
result: NARROWED; exact first-64 falsification panel survived
DAG status delta: +1 background PROVED evidence node; target unchanged
upstream terminal delta: none; classified OURS_ONLY
delta-star bracket movement: none
new assumptions: none
compute: Modal ap-3shnVd7pQ1dxDBBYN2Z7Ar; 64 bounded workers, zero errors
next: derive a universal gate-aware divisor certificate; do not extend the prime census by default
```

### WCL `(1,6)` unsigned sign-product router

The structural return produced a second exact coordinate for the slot. For a
six-subset of squared roots `y_i in mu_256`, the product of all 32 global-sign
square-root sums is a symmetric integer polynomial `Psi_6` of degree 16. It
vanishes exactly when one signed lift vanishes, and

```text
product_[sign lifts] Norm_(Q(zeta_512)/Q)(signed sum)
  = Norm_(Q(zeta_256)/Q)(Psi_6)^2.
```

Hence the aggregate norm has exactly the union of the signed prime supports.
Affine Galois descends to `x -> ax+b` on `Z/256`. Exact Burnside enumeration,
independently replayed with a second generating-function implementation,
gives two invariant product-parity sectors:

```text
even product   6,025,357 orbits
odd product    5,624,703 orbits
total         11,650,060 orbits
```

This is a factor-`15.928589...` quotient of the `185,569,028` signed census.
It is not yet a compute reduction: an aggregate norm combines 32 sign lifts
and can be harder to factor. A bounded attempt to expand `Psi_6` into
elementary symmetric coordinates reached `2,079` terms after four
eliminations and timed out under its stopping rule, so that representation
is retired. The next attack should seek a pairing/resultant factorization of
the abstract sign product that preserves prime support without forming one
large aggregate integer.

```text
starting pin: 3db840bd7; canonical 23df01a65; upstream main 93fba1be
lane: WCL / (ell,h)=(1,6)
result: NARROWED by exact 32-sign aggregation and 15.93x orbit quotient
DAG status delta: +1 background PROVED evidence node; target unchanged
upstream terminal delta: none; classified OURS_ONLY
delta-star bracket movement: none
new assumptions: none
compute: Burnside app ap-lVlwqd9Jq78L9k2fCosqa3; formula fence ap-WDu6iFzptBZRCVSDtGD5Wu
next: factor Psi_6 structurally by pairings or resultants; do not launch aggregate norm census
```

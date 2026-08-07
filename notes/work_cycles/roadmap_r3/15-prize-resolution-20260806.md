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

### WCL `(1,6)` pair-Heron factorization

The sign product admits the requested prime-support-preserving structural
factorization. Pair the six roots into three pairs and let `U,V,W` be the
squares of their internally signed pair sums. The four external pair-sign
classes multiply to

```text
H(U,V,W)=U^2+V^2+W^2-2UV-2UW-2VW.
```

There are eight internal pair-sign choices, so the 32-factor `Psi_6` is the
product of eight Heron factors. Equivalently it is the norm of this six-term
polynomial through the three quadratic extensions generated by the pair
products. The identity holds for all 15 pairings and was replayed symbolically
and by 900 independent finite-field checks.

This is a genuine improvement over the timed-out expanded formula: it keeps
`Psi_6` factored into eight explicit objects, each owning exactly four sign
classes, and preserves the union of rational prime supports. It does not yet
bound those primes. The next proposition should choose a deterministic
pairing and derive a cyclotomic resultant or congruence bound for its Heron
factor; no aggregate census is justified yet.

```text
starting pin: c43b94709; canonical 23df01a65; upstream main 93fba1be
lane: WCL / (ell,h)=(1,6)
result: NARROWED by exact eight-factor pair-Heron norm identity
DAG status delta: +1 background PROVED child; target unchanged
upstream terminal delta: none; classified OURS_ONLY
delta-star bracket movement: none
new assumptions: none
compute: no Modal; exact symbolic proof and bounded finite-field audit under RAMguard
next: deterministic pairing ownership plus a Heron-factor prime-support bound
```

### WCL `(1,6)` parity-adapted base-field descent

The two unsigned product sectors pay most of the formal quadratic extension.
If the product exponent is even, the odd and even exponent classes both have
even cardinality; pairing within parity puts all three pair products in
`Q(zeta_256)`. If it is odd, both classes have odd cardinality and a pairing
with exactly one mixed pair exists. Thus:

```text
even sector: 8 Heron factors directly in Q(zeta_256),
odd sector:  4 factors C^2-dD^2 in Q(zeta_256),

C=s^2+4d-2s(V+W)+(V-W)^2,   D=4(s-V-W).
```

The latter formula is the exact norm of the two conjugate Heron factors from
the unique mixed pair. All 64 exponent-parity patterns and 1,000 independent
modular instances replay. The prior formal degree-eight norm has therefore
collapsed to degree one in the even sector and degree two before explicit
descent in the odd sector.

The remaining proposition is now arithmetic and concrete: bound official
prime divisors of individual order-256 Heron or `C^2-dD^2` norms. A small
deterministic norm/factor-cost pilot is justified; a full census is not.

```text
starting pin: cfa9e1c3d; canonical 23df01a65; upstream main 93fba1be
lane: WCL / (ell,h)=(1,6)
result: NARROWED to base-field Heron/quadratic-norm factors in both sectors
DAG status delta: +1 background PROVED child; target unchanged
upstream terminal delta: none; classified OURS_ONLY
delta-star bracket movement: none
new assumptions: none
compute: no Modal; 64 exact parity patterns and 1,000 modular audit rows
next: bounded norm-size/factorability pilot on deterministic parity-adapted samples
```

### WCL `(1,6)` conductor and block-norm gcd fence

The proposed multi-pairing continuation does not create the independent
arithmetic obstruction that made the `ell=2` norm-gcd route effective. For a
six-support, first descend by the largest `2^d` dividing every exponent
difference. The all-one-parity stratum then has the exact lower-conductor
form

```text
S=zeta_512^c T,       |Norm(S)|=|Norm(T)|^(2^d),       d<=5,
```

and the descended support is mixed in parity. At that conductor the
`K/K_0` involution is free on sign classes. Exact block ownership gives

```text
even Heron block norm:       N_epsilon N_theta,
odd descended block norm:   N_epsilon1 ... N_epsilon4.
```

Therefore every parity-adapted block norm containing one sign class is
divisible by that class's complete rational norm. Two pairings can isolate
one conjugacy orbit as a set, but the integer gcd still contains its full
norm and offers no compression. The theorem is banked as
`dli_wcl_ell1_weight6_conductor_block_norm_gcd_fence [PROVED]`.

This changes the route decision, not the target status. Do not fund a larger
Heron aggregate norm/factor pilot. Either find direct arithmetic control of
individual minimal-conductor `(1,6)` norms, or move WCL effort to `(2,7)`,
where two moment equations can supply a genuinely independent gcd.

```text
starting pin: a1120ba75; canonical 23df01a65; upstream main 93fba1be
open upstream PRs: 8; #1150 is the only shared-program packet and is F2-only
lane: WCL / (ell,h)=(1,6)
result: NARROWED by exact conductor owner; cross-pairing block-gcd route retired
DAG status delta: +1 background PROVED route-fence node; target unchanged
upstream terminal delta: none; classified OURS_ONLY
delta-star bracket movement: none
new assumptions: none
compute: no Modal; exact 62-pattern/15-pairing audits and 12,104 conductor checks
next: inspect the (2,7) simultaneous-moment frontier before authorizing compute
```

### WCL `(2,7)` corrected quadruple-cubic prime filter

Inspection of the simultaneous-moment frontier confirmed two separate
facts. First, the existing complete route is far too large:

```text
selected quadruple + complement product
  -> complementary cubic
  -> two order-1024 doubling recurrences
  -> 94,652,815 affine candidate orbits.
```

The exact count independently reproduces the closed `(2,6)` control
`404,740` and is a `233.9x` blow-up. The old multi-thousand-dollar census
remains a no-go.

Second, the router's recorded saturation gap has an exact repair. If
`g_0=gcd(Norm(F),Norm(G))`, a rational prime shared with `Norm(u)` cannot be
deleted: the three norms may vanish at different split embeddings. For
every `p|g_0`, compute

```text
H_p=gcd(Phi_1024,F,G),       H_p^*=H_p/gcd(H_p,u).
```

The routed equations have a common embedding with `u!=0` exactly when
`deg H_p^*>0`; only those primes proceed to cubic/support reconstruction.
The paid weight-three exclusion separately proves `u!=0` on every actual
official relation. This is banked as
`dli_wcl_ell2_weight7_quadruple_cubic_prime_filter_router [PROVED]`.

The theorem repairs a load-bearing premise but does not shrink the orbit
fleet. Future `(2,7)` work must batch the free complement product, reduce the
401,712 selected-quadruple shapes, or find a smaller joint obstruction. No
sampling extension or complete fleet is authorized.

```text
starting pin: 17833b451; canonical 23df01a65; upstream main 93fba1be
open upstream PRs: 8; none supplies WCL arithmetic
lane: WCL / (ell,h)=(2,7)
result: CORRECTED exact prime filter; complete 94.7m-orbit route remains retired
DAG status delta: +1 background PROVED router; target unchanged
upstream terminal delta: none; classified OURS_ONLY
delta-star bracket movement: none
new assumptions: none
compute: no Modal; exact Burnside, recurrence, direct order-16 orbit, and polynomial-gcd audits
next: seek complement-product batching; pivot lanes if no exact compression appears
```

### X4/SP `d=1` projection codegree reduction

The translated complementary-divisor interface left two multiplicities
entangled: the number of possible linear differences and the number of
divisor incidences.  Fixed `H=aX+b` is not injective, but fixing either
locator projection gives a uniform packing theorem.

For a fixed added locator `L_P`, two distinct removed locators satisfy

```text
L_(Q_i)-L_(Q_j)=H_j-H_i,
```

so their root sets meet in at most one point.  The dual statement holds with
`P,Q` exchanged.  The exact incidence/Johnson count is

```text
deg(P)<=floor(A(e-1)/(e^2-A)),
deg(Q)<=floor((N-A)(e-1)/(e^2-(N-A))).
```

The official corridor itself forces `t_XR>=2^31`: below that depth the
symmetric binomial index stays between `N/16` and `N/2`, so
`binom(N,N-K-t)>=16^(N/16)=2^(N/4)` while `t log2(q)<2^(31)*256=N/4`.
Since `d=1` gives `e>=t+2`, both official projection codegrees are therefore
at most exactly `1024`.

This is a genuine multiplicity reduction, not X4 closure.  The first
nonconstant branch is now a first-owner-compatible distinct-locator
projection census with a certified ten-bit loss.  No quotient row inherits
the number without replaying its own tuple, and `d>=2` remains separate.

```text
starting pin: bf4ee100e; canonical 23df01a65; upstream main 93fba1be
open upstream PRs: 8; none closes SP2
lane: X4 / upstream SP2 low-degree difference incidence
result: NARROWED d=1 to a distinct-locator projection census with codegree <=1024
DAG status delta: +1 background PROVED child; target unchanged
upstream terminal delta: portable OVERLAP theorem for SP2; upstream SP remains open
delta-star bracket movement: none
new assumptions: none
compute: no Modal; exact integer verifier plus independent Fano-plane extremal audit
next: bound one first-owner-filtered d=1 locator projection; keep d>=2 separate
```

### X4/SP low-difference high-width payment

The fixed-projection `1024` bound can be strengthened on large side widths
without fixing a locator.  If two neighbours of one base have side width `e`
and reduced difference degree at most `d`, their changed `2e`-sets intersect
in at most `e+d`.  The local Johnson count is therefore

```text
M_(e,<=d)<=N(e-d)/(4e^2-N(e+d))
```

whenever the denominator is positive.

At `d=1`, positivity starts exactly at `e=N/4+1`.  The first width has
denominator four and bound `N^2/16`; every later bound is smaller.  There are
exactly `N/4` widths through `N/2`, so

```text
sum_(e=N/4+1)^(N/2) D_(e,1)<=N^3/64.
```

This pays the complete high-width linear-difference band.  The next SP2
attack is now restricted to `t_XR+2<=e<=N/4`, where the Johnson denominator
is nonpositive; the fixed-projection codegree remains available there.

```text
starting pin: b9ec8c6be; canonical 23df01a65; upstream main 93fba1be
open upstream PRs: 8; none closes SP2
lane: X4 / upstream SP2 low-degree difference incidence
result: PAID the complete d=1 high-width band by N^3/64
DAG status delta: +1 background PROVED child; target unchanged
upstream terminal delta: portable OVERLAP theorem for SP2; upstream SP remains open
delta-star bracket movement: none
new assumptions: none
compute: no Modal; exact integer verifier plus independent attained N=8 extremal audit
next: attack t_XR+2<=e<=N/4 using the 1024 projection codegree
```

### X4/SP complete Johnson-positive wedge payment

The low-difference Johnson formula can be summed across all exact `(e,d)`
cells, not only `d=1`.  Put

```text
Delta_(e,d)=4e^2-N(e+d).
```

For `Delta>=N`, each cell costs at most `e-d<=N/2`, and there are fewer than
`N^2/8` cells.  For `0<Delta<N`, increasing `d` by one subtracts exactly `N`,
so there is at most one boundary cell per `e`; each costs at most `N^2/2`.
Therefore

```text
sum_(Delta_(e,d)>0) D_(e,d)<=N^3/16+N^3/4=5N^3/16.
```

Every remaining nonconstant record is now confined to

```text
4e^2<=N(e+d),       e>=t_XR+d+1.
```

Together with the minimal `D_0` stratum, this residual has a sufficient
allowance `(251/16)N^3-1`.  This is a geometric narrowing only; no bound on
the reverse-inequality wedge is claimed.

```text
starting pin: 1662cf277; canonical 23df01a65; upstream main 93fba1be
open upstream PRs: 8; none closes SP2
lane: X4 / upstream SP2 low-degree difference incidence
result: PAID every Johnson-positive nonconstant cell by 5N^3/16
DAG status delta: +1 background PROVED child; target unchanged
upstream terminal delta: portable OVERLAP theorem for SP2; upstream SP remains open
delta-star bracket movement: none
new assumptions: none
compute: no Modal; exact finite controls through N=128 and independent even-N denominator audit
next: attack 4e^2<=N(e+d), e>=t_XR+d+1; retain D_0 separately
```

### X4/SP nonpositive-wedge packing route cut

The changed-set intersection consequence is not strong enough in the
remaining wedge.  At rate one half, take

```text
e=N/8,       d=e-t_XR-1,       L=2e=N/4.
```

Choose `e` disjoint pairs on each side of the base support.  A binary word of
length `L` chooses one point from each pair, producing `|P|=|Q|=e`, and two
changed sets intersect in `L` minus the words' Hamming distance.  The greedy
binary-code bound at distance `t_XR+1`, together with `t_XR<=N/128-2`, gives

```text
|C|>=2^L / sum_(i=0)^t_XR binom(L,i)
    >2^(25L/32-35)
    >2^127=16N^3.
```

These abstract blocks satisfy `|W_i intersect W_j|<=e+d`, the exact
side-width pin, and `4e^2<=N(e+d)`.  They are not locator incidences.  The
result therefore retires only the intersection/constant-weight continuation:
the live proof must use split-locator algebra, coefficient primitivity, or
operational first-owner predicates.

```text
starting pin: 9cb7fa1e0; canonical 23df01a65; upstream main 93fba1be
open upstream PRs: 8; none closes SP2
lane: X4 / upstream SP2 low-degree difference incidence
result: ROUTE CUT for abstract packing in the Johnson-nonpositive wedge
DAG status delta: +1 background PROVED child; target unchanged
upstream terminal delta: portable OVERLAP fence for SP2; upstream SP remains open
delta-star bracket movement: none
new assumptions: none
compute: no Modal; exact official arithmetic and a finite bipartite code audit
next: use locator equations or exact first-owner predicates inside the residual wedge
```

### X4/SP primitive dyadic norm router

For a signed primitive shift-pair vector `c=1_P-1_Q`, the locator-prefix
power sums now feed an exact dyadic DLI interface.  Every nonzero fold
`beta_j` satisfies

```text
p^(f_j o_j) <= |Norm(beta_j)|
             <= E_j^(n_j/4)
             <= (2^(j+2)e)^(N/2^(j+2)),
```

with the lower exponent counted by Frobenius orbits, not raw frequencies.
It is at least the number of available odd frequencies.  In an exact
`(e,d)` cell the usable depth is `T=e-d-1`, not merely `t_XR`.  The root fold
vanishes exactly on the common antipodal coefficient-scale branch, already
removed by the quotient sieve.  Thus every live primitive record is norm-
gated, including over generated extension fields.

No census follows from the gate alone.  The closure-bearing continuation is
to compile first ownership and count the norm-gated locator records in each
surviving `(e,d)` cell.

```text
starting pin: 3f33dbbff; canonical 23df01a65; upstream main 93fba1be
open upstream PRs: 30; none closes SP2
lane: X4 / upstream SP2 low-degree difference incidence
result: ROUTED every coefficient-primitive shift pair into an exact DLI norm gate
DAG status delta: +1 background PROVED child; target unchanged
upstream terminal delta: portable OVERLAP arithmetic adapter for SP2; upstream SP remains open
delta-star bracket movement: none
new assumptions: none
compute: no Modal; exact split-prime and generated-extension finite audits
next: count norm-gated primitive locator records under the operational first-owner map
```

### X4/SP shared Haar norm-product gate

All dyadic fold energies obey

```text
sum_j E_j/2^(j+1)=2e.
```

Consequently every nonempty active-scale set satisfies the exact integer
gate

```text
p^R_S A_S^A_S <= (eN)^A_S,
A_S=sum_(j in S)N/2^(j+2),
R_S=sum_(j in S)ord_(N/2^j)(p)o_j.
```

Coefficient primitivity forces scale zero active.  Higher zero folds remain
separate branches.  The gate deletes impossible patterns but supplies no
population estimate for survivors.

The companion ownership audit found no operational four-bucket membership
compiler in the current X4 assembly.  Row-pattern replay and that compiler
are the next closure-bearing tasks.

```text
starting pin: 51da18d95; canonical 23df01a65; upstream main 93fba1be
open upstream PRs: 30; none closes SP2 or prints the local X4 owner compiler
lane: X4 / upstream SP2 low-degree difference incidence
result: STRENGTHENED per-fold gates to one exact shared-energy norm product
DAG status delta: +1 background PROVED child; target unchanged
upstream terminal delta: portable OVERLAP multiscale filter for SP2; upstream SP remains open
delta-star bracket movement: none
new assumptions: none
compute: no Modal; exhaustive exact audits over 12,266 signed pairs and 74,152 active subsets
next: replay active patterns per consumed row; compile the four owner predicates; count survivors
```

### X4/SP structural zero-fold divisibility

Every zero fold is equivalent to an integral cyclotomic factor of the signed
support polynomial.  Together with the balance factor `X-1`, these factors
strengthen the active norm product to

```text
2^(|S|+T_2(S,Z)) p^R_S A_S^A_S <= (eN)^A_S,
T_2(S,Z)=sum_(j in S,a in Z)min(n_j,n_a)/2.
```

The comparison deletes impossible zero/active patterns but does not assign a
first owner or count survivors.

```text
starting pin: e79cb3180; canonical 23df01a65; upstream main 93fba1be
open upstream PRs: 30; none closes SP2
lane: X4 / upstream SP2 low-degree difference incidence
result: CHARGED every structural zero fold by exact dyadic norm divisibility
DAG status delta: +1 background PROVED child; target unchanged
upstream terminal delta: portable OVERLAP zero-pattern refinement for SP2; upstream SP remains open
delta-star bracket movement: none
new assumptions: none
compute: no Modal; exhaustive exact audit at N=8,16 over 12,266 signed pairs
next: evaluate the strengthened pattern gate row-wise and classify surviving integral factor patterns
```

### X4/SP hard-boundary norm-size route cut

At

```text
N=2^41, e=N/8, T=t_XR, d=e-T-1,
```

every active/zero pattern passes the complete generic norm-size gate.  The
lower factor is below `2^(3N+5160)` uniformly over `q<2^256`, while the Haar
ceiling is at least `2^(10N)`.  This is not a shift-pair construction; it
retires only the generic size-comparison route.

```text
starting pin: 3671fd167; canonical 23df01a65; upstream main 93fba1be
open upstream PRs: 30; none closes SP2
lane: X4 / upstream SP2 low-degree difference incidence
result: ROUTE CUT for generic multiscale norm size at the hard boundary
DAG status delta: +1 background PROVED child; target unchanged
upstream terminal delta: portable quantified endpoint warning for SP2; upstream SP remains open
delta-star bracket movement: none
new assumptions: none
compute: no Modal; exact symbolic official-row inequalities
next: attack hard-boundary locator incidence or operational ownership; use norms only with new exact shape data
```

### Conjecture-F false-green repair

The L1/upstream reconciliation found that `conj_f` was green only because two
routers had been consumed as payments. `f_sparse_rank_split` sends the
weight-at-least-three branch to Face 4 but does not pay its actual section
points. `f_spread_moment_count` gives exact leaf bounds, but neither it nor
polynomial state count produces one absolute exponent when the flat dimension
grows.

The DAG now names those obligations as
`f_higher_weight_sparse_payment` and `f_global_packing_step`. A third leaf,
`f_prize_consumer_flat_scope`, repairs the unproved assumption that every
actual caller lies in the useful dimension regime and includes the mixed-
petal/Pade family omitted by the refuted two-family compiler. The four parent
nodes through `conj_f` are honest conditional assemblies. This aligns our
critical frontier with upstream `prob:capfr1-master-flatness` and the L1 Pade
section rather than falsely claiming a theorem upstream still poses as open.

```text
starting pin: 84d04d06f; canonical 23df01a65; upstream main 93fba1be
open upstream PRs: 30; none closes the exposed flatness/payment leaves
lane: LIST / Conjecture F / split-pencil master flatness
result: FALSE-GREEN REMOVED; three exact critical leaves exposed
DAG status delta: -4 PROVED, +4 CONDITIONAL, +3 TARGET before orbit relabeling
upstream terminal delta: shared theorem boundary is now exact
delta-star bracket movement: none
new assumptions: none
compute: no Modal
next: prove an owner-aware absolute-exponent packing theorem, not another router
```

### Conjecture-F consumer-scope decomposition

The strict graph has only two `req` callers of `conj_f`: `imgfib` and
`spi_point_counting`. The SPI call is now closed as an exact interface: for
each slope `z`, its incidence fiber is

```text
P(ker M(z)) cap D_j(H),
```

and one descriptor occurrence per slope incidence preserves the multiplicity
used by the sieve. The existing component/payment order supplies the first
owner before the generic residual.

The LIST call remains under-specified. Its proof packet says only "plane
sections of D_j" and does not enumerate branches, parameters, punctures, or
the codeword-to-section multiplicity. The full-locator Pade section cannot
fill that gap because it is polynomial rather than linear. The proved
root-free rational-Q theorem does supply one exact punctured projective cell,
but not branch exhaustion. Accordingly the former scope TARGET is now a
CONDITIONAL compiler over the proved SPI interface and the narrower
`f_imgfib_consumer_descriptor` TARGET. Red leaves remain 28.

```text
starting pin: 7da3c1ed4; canonical 23df01a65; upstream main 93fba1be
open upstream PRs: 30; none prints the missing LIST branch-to-flat compiler
lane: LIST / Conjecture F consumer interfaces
result: PROVED the SPI descriptor; isolated the exact LIST interface gap
DAG status delta: +1 PROVED, +1 CONDITIONAL, TARGET count unchanged
upstream terminal delta: portable exact Hankel slope-fiber interface; no terminal closed
delta-star bracket movement: none
new assumptions: none
compute: no Modal; graph, proof-object, and linear-algebra audit only
next: compile the actual imgfib branch inventory and preserve puncture/owner multiplicity
```


### LIST Conjecture-F route retirement and FPC5 exposure

The branch audit found that the historical `conj_f -> imgfib` edge did not
name a linear section or preserve a codeword/section multiplicity. The actual
gap is direct. The green `petal_growth` packet is top-band only, and the
proved band/root composition leaves exactly

```text
M>=4,  d<ell(M-2),  t<2M-4,
max(0,2d+1-t ell)->infinity.                         (FPC5)
```

The new `l1_full_petal_fpc5_payment` TARGET owns this full-petal residue.
The disjoint `l1_mixed_petal_amplification` TARGET continues to own
mixed/diffuse partial petals. These direct leaves replace the unsupported
LIST flatness call.

The general Conjecture-F chain remains a genuine SPI research route, but its
only strict caller is now `spi_point_counting`, which is not required by
either grand-challenge root. Its 26-node ancestry therefore moves to the
background tree. This is dependency pruning, not a proof of Conjecture F.

```text
starting pin: bd9f96c91; canonical 23df01a65; upstream main 93fba1be
open upstream PRs: 30; none pays FPC5 or the mixed/partial target
lane: LIST / direct image-fiber residual partition
result: RETIRED the untyped LIST Conjecture-F route; exposed exact FPC5 leaf
DAG status delta: math 235(168/39/28) -> 210(150/34/26)
submission delta: 250(180/41/29) -> 225(162/36/27); spine unchanged
upstream terminal delta: direct portable FPC5 statement; no terminal closed
delta-star bracket movement: none
new assumptions: none
compute: no Modal; exact proof-interface and dependency audit only
next: attack FPC5 directly, coordinated with the mixed/partial L1 target
```


### FPC5 official-cell decomposition

The direct full-petal leaf is now a proved conditional partition over three
disjoint payment targets:

```text
rate-half M=4,t=3:  guarded Johnson-negative LS6 split slices;
M=4,t=2:            rate 1/2 and 1/4 coprime-pair slices;
large source:       M>=5,5,7,15 at rates 1/2,1/4,1/8,1/16.
```

The second branch gained a new exact petal-equation theorem. For
`d=ell+s<2ell`, every two-full-petal contributor injects into the unique
cofactor representation

```text
F=(L_1 A_1-L_2 A_2)/(c_2-c_1),
W=c_1F+L_1A_1,               deg A_i<=s.
```

The petal-equation locator envelope has dimension `2s+2`, codimension
`ell-s-1`, and exact core defect is equivalent to `gcd(A_1,A_2)=1` when the
locator is disjoint from the petals. A full PMA cell additionally imposes its
background roots, exact nonagreements, and first owner.

Official source arithmetic makes the formal codimension-zero endpoint empty.
At the apparent sharp rate-half codimension-two boundary it forces

```text
5ell=k+4,       b=r=s=ell-3,       d=2ell-3.
```

Thus every background point is an agreement. Imposing `L_0|W` changes the
cofactor condition to

```text
c_2L_1A_1 == c_1L_2A_2 (mod L_0)
```

and cuts the guarded pair and locator dimensions to `ell-1`, hence true
locator codimension `ell-1`. The residual is now a guarded split-core-locator
and ownership count, not a codimension-two ambient-slice problem.

Fifteen proved PMA reduction nodes are now strict critical suppliers. This
raises the visible leaf count from 26 to 28 while replacing broad general
flatness assumptions by exact official-cell obligations.

```text
starting pin: 6e8e1bc32; canonical 23df01a65; upstream main 93fba1be
open upstream PRs: 30; none pays the three FPC5 aggregates
lane: LIST / direct full-petal FPC5
result: DECOMPOSED FPC5 into three exact red leaves; proved petal and sharp background-guarded two-petal normal forms
DAG status delta: math 210(150/34/26) -> 228(165/35/28)
submission delta: 225(162/36/27) -> 243(177/37/29); spine unchanged
upstream terminal delta: portable two-petal slices and exact official partition
delta-star bracket movement: none
new assumptions: none
compute: no Modal; tiny finite-field rank replays only
next: count split core locators in the rate-half dimension-(ell-1) guarded congruence kernel, or attack the guarded LS6 max-to-mean gap
```

### FPC5 `M=4,t=2` rate split

The existing proved `l1_general_first_layout_domination` theorem applies to
FPC5 at every petal size. It reduces all maximal source layouts to the complete
non-planted contribution in one fixed first layout plus at most `M` anchors.
The earlier warning about uncontrolled source-layout multiplicity is therefore
retired; only contributor-dependent internal recharts still need first owners.

At rate quarter, `M=4` gives

```text
4ell+b=3k+1,       b<ell,       hence 2ell>k-1.
```

Two full petals therefore determine a degree-`<k` codeword uniquely. The fixed
layout has six unordered touched pairs, so at most six non-planted contributors;
adding four first-layout anchors gives the global absolute bound ten. This
closes the complete rate-quarter `M=4,t=2` branch.

The former two-rate target is now a CONDITIONAL router over the single exact
`l1_fpc5_ratehalf_m4_t2_payment` leaf. The sharp rate-half boundary remains the
dimension-`ell-1` background-guarded split-locator congruence kernel.

```text
starting pin: c99f4912c; canonical 23df01a65; upstream main 93fba1be
open upstream PRs: 30; none supplies the rate-half guarded split-locator payment
lane: LIST / direct full-petal FPC5 / M=4,t=2
result: PROVED rate quarter with absolute bound 10; isolated rate half as the only red child
DAG status delta: math 228(165/35/28) -> 231(167/36/28)
submission delta: 243(177/37/29) -> 246(179/38/29); spine unchanged
upstream terminal delta: portable first-layout and rate-quarter pair-uniqueness payment
delta-star bracket movement: none
new assumptions: none
compute: no Modal; exact arithmetic and tiny source replays only
next: classify/count primitive split locators in one fixed rate-half guarded slice
```

### Rate-half sharp-cell nonemptiness route cut

An exact adversarial finite census tested whether the corrected sharp guarded
slice might be algebraically empty. On `H_32 subset F_97^*` at

```text
(n,k,ell,M,b,s,d)=(32,16,4,4,1,1,5),
```

the solver derives the touched-label ratio from the complete second-petal
system rather than sampling it. Across 50 deterministic maximal layouts, 41
are nonempty and contain 71 primitive exact contributors in total, with
maximum five in one layout. Seed 3 is replayed end to end with exactly 19
agreements.

This is bounded root excess (`e=3`), so it neither creates an asymptotic FPC5
family nor threatens polynomiality. It does decisively retire universal
algebraic emptiness of the guarded equations. The live route is classification
and count after tangent/quotient ownership.

```text
starting pin: 6e9f3029d; canonical 23df01a65; upstream main 93fba1be
lane: LIST / rate-half FPC5 M=4,t=2
result: ROUTE CUT for sharp-cell algebraic emptiness; exact finite witness banked
DAG status delta: +1 background PROVED evidence node; critical frontier unchanged
upstream terminal delta: portable sharp-cell nonemptiness warning and certificate
delta-star bracket movement: none
new assumptions: none
compute: no Modal; two exact 50-layout local censuses under 256 MB RAM guard
next: emit the exact projective split-flat descriptor and separate its common-gcd owner
```

### Rate-half sharp projective-flat interface

The sharp guarded endpoint is now compiled as an exact split-locator flat.
For one fixed source and touched pair, projection from the guarded `(F,W)`
slice to its locator image `V_F` is an isomorphism, and

```text
|C|=5ell-5,       j=2ell-3,
dim P(V_F)=ell-2,       affine codimension=ell-1.
```

Every exact contributor is the unique monic representative of a point in
`P(V_F) intersect D_j(C)`, with a uniquely reconstructed numerator. Core
primitivity, untouched-petal nonagreements, and first ownership remain
explicit filters. Dividing the maximal common gcd gives an exact gcd-trivial
flat over the punctured core, but no tangent payment is inferred from that
division.

This is precisely a growing-dimensional instance of upstream's
split-locator master-flatness target. The fixed-dimensional theorem is not
enough because `r=ell-2`. A tiny replay on the seed-3 `F_97,H_32` source
finds one split point in the relevant projective plane, exactly the already
certified contributor, and verifies the projective and gcd-division
identities.

```text
starting pin: 6934b6c87; canonical 23df01a65; upstream main 93fba1be
lane: LIST / rate-half FPC5 M=4,t=2 / sharp cell
result: PROVED exact projective-flat descriptor and common-GCD normalization
DAG status delta: +1 background PROVED evidence node; critical frontier unchanged
upstream terminal delta: portable concrete instance of split-locator master flatness
delta-star bracket movement: none
new assumptions: none
compute: no Modal; one 3003-locator F_97 replay under 256 MB RAM guard
next: exploit the guarded congruence/exact filters or prove the needed growing-dimensional flatness count
```

### Sharp FPC5 common-GCD branch eliminated

The guarded cofactor kernel has no flat-wide common locator divisor. Indeed,
the two allowed cofactor pairs `(L_0,0)` and `(0,L_0)` show that every common
factor divides `L_0`. For each background root `y`, set `A_1=1` and interpolate
`A_2` on the background so that the guarded congruence holds. The resulting
locator satisfies `F(y)=-L_1(y)/c_1!=0`. Hence no factor of `L_0` is common and

```text
gcd(V_F)=1.
```

This puts the sharp endpoint directly in the primitive growing-dimensional
master-flatness regime. It does not remove the candidate-wise exact-core
condition `gcd(F,W_F)=1`.

```text
starting pin: a907068e9; canonical 23df01a65; upstream main 93fba1be
lane: LIST / rate-half FPC5 M=4,t=2 / sharp primitive flat
result: PROVED flat-wide gcd triviality; common-divisor branch eliminated
DAG status delta: +1 background PROVED evidence node; critical frontier unchanged
upstream terminal delta: portable primitive-instance sharpening of the master-flatness interface
delta-star bracket movement: none
new assumptions: none
compute: no Modal; eight finite-field rank/gcd replays under 256 MB RAM guard
next: count primitive split points using guarded congruence and exact PMA filters
```

### Sharp FPC5 pure dyadic quotient stratum empty

At the official sharp endpoint the locator degree `j=2ell-3` is odd, while
every proper quotient scale `M>1` dividing `n=2^41` is even. A pure
multiplicative pullback `g(X^M)` has degree divisible by `M`; equivalently, a
union of complete `mu_M`-orbits has cardinality divisible by `M`. Therefore

```text
gcd(n,j)=1
```

and the complete multiplicative-periodic stratum is empty. This does not
remove incomplete-orbit tails, general rational pullbacks, or
reciprocal/dihedral classes.

```text
starting pin: eca33cec7; canonical 23df01a65; upstream main 93fba1be
lane: LIST / rate-half FPC5 M=4,t=2 / sharp primitive flat
result: PROVED pure dyadic quotient-pullback absence
DAG status delta: +1 background PROVED evidence node; critical frontier unchanged
upstream terminal delta: portable official parity specialization of quotient recursion
delta-star bracket movement: none
new assumptions: none
compute: no Modal; 230 exact divisor checks under 256 MB RAM guard
next: isolate tail/rational/dihedral strata or attack the primitive aperiodic count directly
```

### Uniform guarded codimension and aggregate root-rich interface

For every fixed exact background agreement set `R`, not only the sharp cell,
the cofactor congruence has rank at least `min(|R|,s+1)`. Since the list
threshold gives `|R|>=s`, projection to the locator flat yields

```text
fixed-cell locator codimension >= ell-1;
|R|=s:       codimension = ell-1 exactly;
|R|>=s+1:    codimension >= ell.
```

The theorem also identifies the honest aggregate object. In the unguarded
two-petal flat, `F` determines `W_F` uniquely, and all contributors at fixed
`s` lie in

```text
F split on the source core,
W_F root-rich on the background: |Z_B(W_F)|>=s.
```

The exact background set is unique, so the cells are disjoint; however, a
sum over all `binom(b,r)` possible sets would be exponentially loose. The
next theorem must count this joint split-pair locus directly or compress the
realized background owners.

```text
starting pin: 1f6709ebd; canonical 23df01a65; upstream main 93fba1be
lane: LIST / rate-half FPC5 M=4,t=2 / all background cells
result: PROVED uniform codimension >=ell-1 and exact aggregate root-rich interface
DAG status delta: +1 background PROVED evidence node; critical frontier unchanged
upstream terminal delta: portable master-flatness/shift-pair consumer family
delta-star bracket movement: none
new assumptions: none
compute: no Modal; 161 finite-field rank cells under 256 MB RAM guard
next: aggregate root-rich numerator ownership; no per-background-set union bound
```

### Aggregate primitive cofactor distance

For two distinct exact contributors at one fixed source, touched pair, and
defect parameter `s`, the primitive cofactor determinant

```text
Delta=A_1A'_2-A'_1A_2
```

is nonzero of degree at most `2s`. It vanishes on every shared missed-core
root and every shared background-agreement root. Therefore

```text
|D intersect D'|+|R intersect R'|<=2s.
```

The combined supports have size at least `ell+2s`, so direct
constant-weight packing gives

```text
L_(s,pair)
 <= floor(binom(k-1+b,2s+1)/binom(ell+2s,2s+1)).
```

This is the first aggregate theorem that avoids selecting `R`. Its exponent
still grows with `s`, so it diagnoses rather than closes the remaining
primitive shift-pair problem.

```text
starting pin: be51e167f; canonical 23df01a65; upstream main 93fba1be
lane: LIST / rate-half FPC5 M=4,t=2 / aggregate shift pair
result: PROVED joint core/background distance and aggregate packing
DAG status delta: +1 background PROVED evidence node; critical frontier unchanged
upstream terminal delta: portable primitive shift-pair distance layer
delta-star bracket movement: none
new assumptions: none
compute: no Modal; 7140 determinant-pair replays under 256 MB RAM guard
next: improve the dimension-dependent packing using exchange or master-flatness structure
```

### Sharp distance-only no-go fence

The determinant distance cannot be upgraded to polynomiality using only
support weights and overlaps. Write `L=ell-2` at the sharp cell. A greedy
constant-weight construction gives `(2L+1)`-subsets of the `(5L+5)`-point
core with intersections at most `L-1` and cardinality at least

```text
binom(5L+5,2L+1)
 / sum_(i=0)^(L+1) binom(2L+1,i)binom(3L+4,i)
 =2^((0.099865...+o(1))L).
```

Adjoining the actual fixed `(L-1)`-point background block gives exactly the
combined weight and overlap cap of the proved FPC5 distance theorem. These
are abstract set systems, not guarded-flat locators or received-word
contributors. The conclusion is a route fence: closure must use the
cofactor equations, smooth-domain incidence, or ownership beyond distance.

```text
starting pin: fe11f0e38; canonical 23df01a65; upstream main 93fba1be
lane: LIST / rate-half FPC5 M=4,t=2 / sharp aggregate
result: PROVED quantified no-go fence for distance-only packing
DAG status delta: +1 background PROVED evidence node; critical frontier unchanged
upstream terminal delta: portable primitive shift-pair no-go fence
delta-star bracket movement: none
new assumptions: none
compute: no Modal; exact binomial arithmetic through L=1024 under 256 MB RAM guard
next: algebraic guarded-flat/exchange attack; do not iterate support-distance bounds
```

### Rate-half `M=4,t=3` outer composition collapsed

General first-layout domination and the exact cross-ratio/split-slice
reductions remove the apparent source and field-label sums from the
three-touched-petal tail. Fix the first admissible maximal `M=4` layout. Its
four anchors are paid separately; every non-planted contributor has one of
the four touched triples, and the triple's source labels determine one
normalized cross-ratio. Since the surviving defect range has fewer than `n`
values, a uniform bound `B(n)` for one exact guarded LS6 atom gives

```text
#FPC5_(M=4,t=3) <= 4n B(n)+4.
```

The remaining red content is now one uniform fixed-atom split-divisor
payment. No source-layout or field-many cross-ratio aggregation remains.

```text
starting pin: 596672ad7; canonical 23df01a65; upstream main 93fba1be
lane: LIST / rate-half FPC5 M=4,t=3 / guarded LS6 atom
result: PROVED first-layout and cross-ratio outer-cell collapse
DAG status delta: +1 background PROVED evidence node; target statement narrowed
upstream terminal delta: portable reduction of the split-slice frontier to one uniform LS6 atom
delta-star bracket movement: none
new assumptions: none
compute: no Modal; integer and finite-field normalization replay under 256 MB RAM guard
next: prove or falsify a uniform guarded split-divisor bound for one LS6 atom
```

### Three-petal LS6 master-flat descriptor

Every nonempty fixed LS6 atom embeds injectively into a full-domain,
unpunctured projective split flat. The exact parameters are

```text
j=2ell-a,       r=ell-2a+1,       j-r=ell+a-1,
j-2r=3a-2>=1.
```

The flat-wide common gcd is one: a common root would be a core root of an
actual split candidate, while the reduced mu-basis determinant is a nonzero
multiple of the three disjoint petal locators there. Moreover

```text
binom(n,j)/Q^(j-r) <=2^(-3ell-4)<1,
```

where `Q` is the field generated by the domain and flat coefficients. Thus
this is a strict sub-balance BC/master-flatness instance, not merely an
arbitrary large linear slice. Pure multiplicative pullbacks occur only at
dyadic scales dividing `j` and are absent whenever `a` is odd. The remaining
work is primitive max-to-mean flatness plus owner-safe even-defect quotient
and dihedral treatment. Current Conjecture-F ownership is not silently
transported into FPC5.

```text
starting pin: 9fab78c39; canonical 23df01a65; upstream main 93fba1be
lane: LIST / rate-half FPC5 M=4,t=3 / guarded LS6 atom
result: PROVED exact gcd-trivial sub-balance master-flat descriptor
DAG status delta: +1 background PROVED evidence node; critical frontier unchanged
upstream terminal delta: portable LIST-side prob:capfr1-master-flatness / BC consumer
delta-star bracket movement: none
new assumptions: none
compute: no Modal; official integer arithmetic replay under 256 MB RAM guard
next: primitive max-to-mean theorem, then owner-safe periodic/dihedral transport
```

### Aligned common-pencil LS6 stratum empty

A nonempty LS6 atom must satisfy

```text
deg Etilde>=a.
```

If `deg Etilde<a`, then `deg(D Etilde)<2ell`, so no reduction modulo
`L_2L_3` occurs; the product still has degree at least `2ell-a`, strictly
above the allowed remainder cutoff `ell-a`.

For an aligned common pencil

```text
L_i=P-z_i,       c_i=alpha z_i+beta,
```

source-label normalization and CRT uniqueness give
`Etilde=(z_2-z_1)^(-1)`. It is constant, so every tail atom with `a>=1` is
empty. This removes the most rigid quotient-aligned source without making
the invalid inference that a periodic locator has a periodic agreement set.
Misaligned common pencils and arbitrary petal locators remain.

```text
starting pin: 99c0b1dea; canonical 23df01a65; upstream main 93fba1be
lane: LIST / rate-half FPC5 M=4,t=3 / structured LS6 strata
result: PROVED multiplier-degree gate and aligned common-pencil emptiness
DAG status delta: +1 background PROVED evidence node; critical frontier unchanged
upstream terminal delta: portable split-pencil aligned-stratum exclusion
delta-star bracket movement: none
new assumptions: none
compute: no Modal; finite-field CRT arithmetic replay under 256 MB RAM guard
next: misaligned primitive max-to-mean and owner-safe periodic/dihedral transport
```

### Misaligned common-pencil LS6 stratum also empty

For common petal locators `L_i=P-z_i`, source-label misalignment makes the
CRT multiplier a fourth pencil member:

```text
Etilde=A(P-z_0),       A!=0.
```

Writing `D Etilde=L_2L_3Q+V` with `deg Q,deg V<=ell-a`, reduction modulo
`P-z_0` and the fact that both low polynomials have degree below `ell` force

```text
V=-(z_0-z_2)(z_0-z_3)Q.
```

The difference-of-fibers factorization then gives

```text
A D=Q(P+z_0-z_2-z_3),       deg Q=ell-a>0.
```

Thus `Q` divides both `D` and `V`, violating the exact LS6 gcd guard.
Together with the aligned theorem, every common-pencil three-petal LS6 atom
is empty. The master-flat frontier now starts only with genuinely non-pencil
petal data.

```text
starting pin: cf4254504; canonical 23df01a65; upstream main 93fba1be
lane: LIST / rate-half FPC5 M=4,t=3 / structured LS6 strata
result: PROVED misaligned common-pencil exactness obstruction; all common pencils empty
DAG status delta: +1 background PROVED evidence node; critical frontier unchanged
upstream terminal delta: portable complete common-pencil stratum exclusion
delta-star bracket movement: none
new assumptions: none
compute: no Modal; exact polynomial factorization replay under 256 MB RAM guard
next: primitive max-to-mean and owner-safe non-pencil periodic/dihedral transport
```

### Low-multiplier LS6 prefix ladder

Let `e=deg Etilde` and `s=ell-a`. In the range `a<=e<=s`, exact Euclidean
division gives a disjoint parametrization by quotient polynomials of degree
`e-a` with fixed leading coefficient and low tails of degree at most `s-e`.
For each fixed quotient, the locators form one ordinary prefix cell of depth

```text
h_e=ell+e-1.
```

There are exactly `Q_0^(e-a)` such cells over a generated field of order
`Q_0`, and the target/depth costs cancel:

```text
Q_0^(e-a) binom(n,j)/Q_0^(ell+e-1)
 =binom(n,j)/Q_0^(ell+a-1).
```

At `e=a` there is one prefix cell. This turns the whole low-multiplier branch
into an exact `(Q)` ladder rather than a general BC flat. The missing input
is depth-uniform prefix max-to-mean control that preserves the cancellation;
the high-multiplier branch `e>ell-a` remains BC-class.

```text
starting pin: a1e75a85c; canonical 23df01a65; upstream main 93fba1be
lane: LIST / rate-half FPC5 M=4,t=3 / low-multiplier LS6
result: PROVED exact prefix-ladder parametrization and average-scale cancellation
DAG status delta: +1 background PROVED evidence node; critical frontier unchanged
upstream terminal delta: portable (Q) ladder/tower-transfer consumer
delta-star bracket movement: none
new assumptions: none
compute: no Modal; exact polynomial division replay under 256 MB RAM guard
next: depth-uniform prefix flatness for the ladder; BC attack only above e=ell-a
```
### High-multiplier LS6 Pade coordinates

Let `e=deg Etilde>ell-a`. For every high-multiplier LS6 candidate, exact
Euclidean division gives

```text
D=quo_E((L_2L_3)Q),       V=-rem_E((L_2L_3)Q),
deg Q=e-a,                lc(Q)=lc(E).
```

Core/petal disjointness transports the exact guard without loss:

```text
gcd(D,V)=1  <=>  gcd(D,Q)=1.
```

If `F` is the canonical inverse of `E` modulo `L_2L_3`, then
`D=rem_(L_2L_3)(FV)`. On the official branch, nonemptiness forces the dual
degree gate

```text
deg F>=ell+a.
```

Indeed, below that gate no modular reduction occurs and `D=FV`, so the
nonconstant remainder `V` violates exactness. Thus the former generic
high-multiplier BC branch is an exact two-sided primitive Pade cell. Its
split maximum, quotient classification, and owner-safe dihedral transport
remain open.

```text
starting pin: 5a68fecfd; canonical 23df01a65; upstream main 93fba1be
lane: LIST / rate-half FPC5 M=4,t=3 / high-multiplier LS6
result: PROVED exact Pade quotient coordinates, guard transport, and inverse-degree gate
DAG status delta: +1 background PROVED evidence node; critical frontier unchanged
upstream terminal delta: portable primitive rational-approximation adapter
delta-star bracket movement: none
new assumptions: none
compute: no Modal; deterministic exact GF(257) replay under 256 MB RAM guard
next: count split primitive Pade quotients and classify owner-safe quotient/dihedral strata
```

### Universal LS6 inverse source-ratio gate

The inverse-multiplier obstruction is independent of the high/low split.
For every guarded LS6 candidate,

```text
F=Etilde^(-1) mod L_2L_3,
D=rem_(L_2L_3)(FV),       deg F>=ell+a.
```

The source CRT gives the exact form

```text
F=L_1+L_2A,
A=(lambda^(-1)-1) rem_(L_3)(L_1L_2^(-1)).
```

Hence nonemptiness forces the label-independent source gate

```text
deg rem_(L_3)(L_1L_2^(-1))>=a.
```

Failure is exactly a short syzygy
`L_1=U L_2+R L_3` with `deg U,deg R<a`. Common pencils are its degree-zero
case. The target now excludes the complete short-syzygy source stratum before
either multiplier branch; classifying the surviving degree-`>=a` ratios
remains open.

```text
starting pin: fbe7a594b; canonical 23df01a65; upstream main 93fba1be
lane: LIST / rate-half FPC5 M=4,t=3 / source syzygy gate
result: PROVED universal inverse-degree and modular source-ratio gate
DAG status delta: +1 background PROVED evidence node; critical frontier unchanged
upstream terminal delta: portable split-pencil/short-syzygy census rung
delta-star bracket movement: none
new assumptions: none
compute: no Modal; deterministic exact GF(257) CRT replay under 256 MB RAM guard
next: classify surviving source-ratio degrees and test cyclic relabeling as simultaneous gates
```

### Guarded LS6 primitive pair determinant

For every candidate, the quotient in `DE=MQ+V` is primitive:

```text
deg Q=e-a,       gcd(D,Q)=1.
```

For two distinct candidates in one fixed atom,

```text
H_12=D_1Q_2-D_2Q_1=(D_2V_1-D_1V_2)/M,
0!=H_12,       deg H_12<=ell-2a.
```

Thus `gcd(D_1,D_2)|H_12`, candidate root sets meet in at most `ell-2a`
points, and the determinant separates candidates relative to a fixed base.
The induced constant-weight Johnson denominator is exactly

```text
(2ell-a)^2-(4ell+b-2)(ell-2a)=J.
```

Since the live tail has `J<=0`, this proves a route fence as well as a
router: pairwise distance cannot close the cell. The next theorem must use
compatibility among several low-degree determinants, their split factors,
or owner-safe quotient structure.

```text
starting pin: 1577be145; canonical 23df01a65; upstream main 93fba1be
lane: LIST / rate-half FPC5 M=4,t=3 / primitive shift pairs
result: PROVED low pair determinant, root-intersection cap, injection, and exact Johnson fence
DAG status delta: +1 background PROVED evidence node; critical frontier unchanged
upstream terminal delta: portable primitive shift-pair/split-pencil router
delta-star bracket movement: none
new assumptions: none
compute: no Modal; deterministic exact GF(257) pair replay under 256 MB RAM guard
next: exploit three-or-more determinant compatibility; do not repeat distance-only packing
```

### Guarded LS6 determinant coordinate chart

Fix one primitive base candidate `(D_0,Q_0,V_0)` and put
`h=ell-2a`. The fixed-base determinant map is not merely injective: it is an
exact affine bijection from the complete monic unguarded LS6 slice to every
polynomial `H` of degree at most `h`. Its inverse is

```text
R_H=rem_(D_0)(-H Q_0^(-1)),       D_H=D_0+R_H,
Q_H=(H+D_HQ_0)/D_0,              V_H=(D_HV_0-MH)/D_0.
```

For coordinates `H,G`, the pair determinant is

```text
D_HQ_G-D_GQ_H=(D_HG-D_GH)/D_0,       deg<=h.
```

Thus every formal multi-determinant and Plucker identity already holds on
the whole ambient slice. Abstract collective compatibility cannot close the
cell. The exact remaining object is the subset for which `D_H` splits on the
core and the root-local primitive inequalities hold: off the base roots one
needs `H(x)!=0`, while at a shared root one needs
`H'(x)+D_H'(x)Q_0(x)!=0`.

```text
starting pin: 133af3dba; canonical 9c5727a89; upstream main 93fba1be
lane: LIST / rate-half FPC5 M=4,t=3 / determinant chart
result: PROVED exact affine determinant coordinates, inverse formulas, root-local guard, and formal-compatibility route fence
DAG status delta: +1 background PROVED evidence node; critical frontier unchanged
upstream terminal delta: portable primitive shift-pair/split-pencil chart extending PR #1151
delta-star bracket movement: none
new assumptions: none
compute: no Modal; 81 exact GF(257) chart coordinates and 144 pair checks under RAMguard
next: count split-root coordinates with the local guard; formal Plucker packing is retired
```

### Exact-five packets are strictly sub-Johnson

The stale comparison check against upstream PRs #1145/#1146 is resolved.
Their background-free coset sunflower has

```text
k-1=m*ell,       s=(m+1)ell,       n>=(m+tau)ell,       tau>=5.
```

Consequently

```text
s^2-n(k-1) <= ell^2(1-m(tau-2)) < 0.
```

Thus Theorem J does not subsume their sharp `ell=11` exact-five constants:
the packets lie strictly below the ordinary Johnson frontier already on the
smallest support domain. They remain genuine finite special-case evidence,
but their fixed-`ell`, fixed-shape scope does not pay an official asymptotic
L1 node.

```text
starting pin: f7e850788; canonical d3a5edba8; upstream main 93fba1be
lane: LIST / upstream harvest / exact-five scope
result: PROVED strict sub-Johnson placement of PRs #1145/#1146
DAG status delta: none; stale open domination check removed
upstream terminal delta: none; exact citation scope now fixed
delta-star bracket movement: none
new assumptions: none
compute: none
next: retain #1145/#1146 as finite fixtures; do not claim Theorem-J domination
```

### LS6 canonical owners and fixed-owner packing

For every non-base guarded point in the determinant chart,

```text
G=gcd(D_0,H)=gcd(D_0,D_H),
D_0=GA,       D_H=GB,       H=GK.
```

The factors `G,A,B` are pairwise coprime,
`K=AQ_H-BQ_0`, and the primitive guard is exactly
`gcd(K,B)=gcd(G,Q_H)=1`. Thus `G` is a canonical owner rather than a selected
common divisor.

At fixed `g=deg G`, the candidate-only root sets have size `j-g` in the
`|C|-j` points outside the base and meet pairwise in at most `h-g` roots.
The exact packing is

```text
|F_G| <= floor(
  binom(|C|-j,h-g+1) / binom(j-g,h-g+1)).
```

For `g=h-c` and `b<ell`, this is less than `3^(c+1)` per owner. Hence every
fixed bounded-co-deficiency top-owner chamber is paid. The remaining theorem
is aggregate: coalesce the realized `G` strata or transport them to
chronology-valid quotient/dihedral owners without summing all divisors of
`D_0`.

```text
starting pin: f7e850788; canonical d3a5edba8; upstream main 93fba1be
lane: LIST / rate-half FPC5 M=4,t=3 / split-pencil ownership
result: PROVED exact canonical owner, normalized primitive guard, and fixed-owner packing
DAG status delta: +1 background PROVED evidence node; critical frontier unchanged
upstream terminal delta: portable fixed-owner SPI/split-pencil ledger extending PR #1151
delta-star bracket movement: none
new assumptions: none
compute: no Modal; exact 561-point GF(257) chart replay under RAMguard
next: aggregate or chronology-route different owners; do not repeat fixed-owner packing
```

# Full-resolution campaign ledger

Worktree: `prize-codex-resolution-20260712`

Branch: `codex/full-prize-resolution`

Baseline: `ab87166` (`prize` roadmap revision; upstream snapshot `36de5bfc`).

## 2026-07-12: WP0 large-arity list scope repair

### Claim contract

```text
claim id: list_large_m_scope_closure
mathematical statement: adjacent interleaved-list determination for every
  fixed constant m omitted by the currently certified m-sweep
quantifiers and row scope: every admissible row; arbitrary fixed m outside
  the certified sweep; every official rate
consumer and exact slot: list_grand, omitted arity class
current status: TARGET
dependencies already proved: official family-per-constant-m reading; integer
  staircase monotonicity; ordinary-list lower embeddings; codegree theorem as
  a conditional compiler interface
new open content: finite constants and adjacent upper/lower meeting for every
  omitted fixed m
falsifier: exact interleaved list exceeding a proposed recursion/regularization,
  or a proposed upper ledger that cannot support its claimed adjacent crossing
proof routes: exact codegree compiler; a-regular/irregular pricing; new floor
upstream mapping: finite interleaved-list certificate interface; complete
  profile-envelope comparison
```

### Finding

`rules_m_reading` correctly says the official problem is a family indexed by
every constant `m`. The root nevertheless consumed `m_handling` as green after
shipping only the bounded affordable range; its own notes admit that larger
constants require a-regularity or an equivalent theorem. The edge
`a_regular_collapse -> m_handling` had been demoted to evidence.

The existing a-regular route has no complete proof artifact and the current
upstream theorem supplies only a conditional codegree compiler, not adjacent
finite certificates. The repair therefore introduces one direct red leaf
rather than a speculative conditional chain.

### Changes

- added `list_large_m_scope_closure` as a required child of `list_grand`;
- updated the list-grand conditional packet to split certified and omitted
  arity scopes;
- added statement, attack, frontier, and candidate dependency-sub-DAG files;
- retained a-regular and codegree routes as evidence-grade attacks.
- fixed `experiments/assembly_orphan_checks.py` after replay exposed a stale
  repository-root and output-path calculation left by its move out of
  `amber_stress/`.

### Replay

```text
python3 critical/nodes/list_large_m_scope_closure/verify.py
python3 experiments/assembly_orphan_checks.py
python3 tools/verify_prize_dag.py
python3 tools/build_critical_orbit.py
```

## 2026-07-12: C36' cutoff optimization

### Claim contract

```text
claim id: f3_h3_mobius_excess_half (legacy id, repaired statement)
mathematical statement: 17 X_18<=300n^2, where
  X_18=sum_(t!=1)(P(t)-18)_+R(t)
quantifiers and row scope: every official order and every official prime
consumer and exact slot: f3_h3_three_to_one_c36, nonidentity rich-fiber tail
current status: TARGET
dependencies already proved: product/quotient convolution, quotient total,
  identity Stepanov payment, cutoff-18 integer compiler
new open content: the cutoff-18 weighted correlation
falsifier: one official row with 17X_18>300n^2
proof route: S_ns<=1200n^2 or a direct simultaneous rich-fiber tail
replay: python3 critical/nodes/f3_h3_mobius_excess_half/verify.py
upstream mapping: primitive shift-pair control / exact second-moment ledger
```

The former target `X_35<=n^2/2` implies this one. Optimizing the baseline
payment at cutoff `18` proves that the exact non-swap incidence only needs

```text
S_ns<=1200n^2,
```

instead of `68n^2`. The observed fleet maximum remains below `3.825n^2`, but
that numerical separation is not used as proof.

## 2026-07-12: arbitrary-arity codegree closure

```text
claim id: list_codegree_closed_form
mathematical statement: if a_j=k+2^j sigma and B_j is the worst base-list
  size at agreement a_j, then the proved codegree recursion implies
  L_m(a_0) <= sum_{r=0}^{min(m-1,d)} binom(m-1,r) product_{j=0}^r B_j,
  where d=max{j:a_j<=n}
quantifiers and row scope: every code, row, integer m>=1, and a_0=k+sigma>k
consumer and exact slot: list_large_m_scope_closure; arbitrary-m upper compiler
current status: proposed proved reduction, not an adjacent threshold theorem
dependencies already proved: codegree Theorem C
new open content: exact base envelopes B_j and the adjacent lower match
falsifier: a recurrence instance violating the Pascal closed form
proof route being attempted: induction on m and finite-depth truncation at a_j>n
replay command: proof is the Pascal recurrence in the node packet
upstream hard-input mapping: complete profile-envelope comparison / L2 codegree
```

## 2026-07-12: G1 atlas-interface repair

```text
claim id: petal_g1_layer_maps
mathematical statement: every arbitrary-word top-band contributor is covered
  by a sunflower atlas A_U with |A_U|<=n^b1, exact layer maps and quotient
  scales, and b1+b4<=B
quantifiers and row scope: every official row and every received word U
consumer and exact slot: petal_growth primitive per-chart K4 sum; G3 first-match
current status: TARGET, re-posed after a logical sufficiency failure
dependencies already proved: concrete layer injection; distinct-label
  residual-free union recovery; G2/G3 compilers
new open content: arbitrary-word coverage, total atlas census, exponent fit
falsifier: uncovered contributor, super-polynomial necessary chart census,
  failed layer dictionary, or failed exponent fit
proof route being attempted: canonical chart recovery from U and bounded
  decomposition data, jointly over missed cores
replay command: python3 tools/verify_prize_dag.py
upstream hard-input mapping: witness-exhaustive first-match atlas
```

## 2026-07-12: arbitrary-arity support census

```text
claim id: list_interleaved_support_census
mathematical statement: L_m(a)<=C(n,a) for all a>=k; L_m(a) is at least
  the exact received-word average; if |F|^m>C(n,k+1), then
  L_m(k)=C(n,k)
quantifiers and row scope: every Reed-Solomon row and every m>=1
consumer and exact slot: list_large_m_scope_closure safe/unsafe anchors
current status: PROVED
dependencies already proved: RS interpolation uniqueness
new open content: none in the anchors; adjacency remains open
falsifier: two tuples assigned to one a-support, or a union-bound count that
  fails the strict received-word inequality
proof route being attempted: canonical-support injection, incidence averaging,
  and probabilistic existence by an exact union bound
replay command: proof is self-contained in the node packet
upstream hard-input mapping: complete profile-envelope comparison
```

## 2026-07-12: extension/interleaving identity

```text
claim id: list_extension_interleaving_identity
mathematical statement: coordinate expansion along a B-basis of E identifies
  RS[E,D,k] isometrically with RS[B,D,k]^{==m}, hence their lists agree exactly
quantifiers and row scope: every finite extension E/B of degree m and D subset B
consumer and exact slot: list_large_m_scope_closure arbitrary-m reduction
current status: PROVED
dependencies already proved: coefficientwise basis expansion
new open content: extension-uniform image-fiber upper bound against |B|
falsifier: a codeword or agreement set not preserved by coordinate expansion
proof route being attempted: direct basis decomposition and Hamming isometry
replay command: proof is self-contained in the node packet
upstream hard-input mapping: extension-code list identity / L2
```

## 2026-07-12: WP8 verifier harness closure

### Claim contract

```text
claim id: harness
mathematical statement: every discovered verifier is manifest-hashed and passes
quantifiers and row scope: entire critical/background verifier surface
consumer and exact slot: packaging replay and refusal discipline
current status: PROVED
dependencies already proved: none; artifact closure
new open content: none
falsifier: omitted/stale/tampered proof, failure, timeout, or hash mismatch
proof route: fail-closed discovery plus complete remote replay
replay: python3 background/nodes/harness/audit.py
upstream mapping: certificate grammar / machine replay layer
```

### Resolution

The stale `tools/replay_all.py` searched a nonexistent `nodes/` directory and
was replaced by exact discovery over both node partitions. The manifest pins
96 executable verifiers, one Modal launcher, and 172 adjacent proof assets.
Six independent negative controls are rejected. Modal app
`ap-LSUBiGJOwxv1kbJyD6YDVQ` replayed all 96 executable entries with no
failure, timeout, hash mismatch, or remote error.

## 2026-07-12: WP8 compiler refusal semantics

### Claim contract

```text
claim id: compiler
mathematical statement: exact packets compile to sound cell verdicts and radius
quantifiers and row scope: every schema-valid MCA/list certificate input
consumer and exact slot: packaging compiler and refusal rule
current status: PROVED
dependencies already proved: v13_finite_adjacent_compiler
new open content: none
falsifier: a prize-facing output from open, conditional, or inconsistent data
proof route: exact integer comparisons plus fail-closed schema validation
replay: python3 background/nodes/compiler/audit.py
upstream mapping: finite adjacent compiler / certificate grammar
```

### Resolution

The compiler emits `SAFE` only from a proved upper count at most `B*`, and
`UNSAFE` only from a proved lower count above `B*`. It emits the closed radius
only for one consecutive unsafe/safe pair after all four required convention
axes are proved. Open axes, conditional ledgers, missing adjacency, ambiguous
crossings, nonmonotone verdicts, and contradictions suppress or reject output.
The `F_17^32` calibration and seven refusal mutations pass.

## 2026-07-12: WP8 Tier-1, partial dossier, and packaging closure

### Claim contract

```text
claim ids: lean_tier1, dossier_partial, packaging
mathematical statement: the partial row package is formalized and gate-checked
quantifiers and row scope: F_(17^32), n=512, k=256 partial row only
consumer and exact slot: Paper-D-attached partial dossier / packaging
current status: PROVED
dependencies already proved: pinned_row, s0_zero_open, compiler, harness, bridge_ledger
new open content: none in packaging; 13 mathematical leaves remain explicit
falsifier: failed Lean build, stale non-claims, or an unproved positive claim
proof route: vendor Tier-1 Lean, build, assemble dossier, exact manifest audit
replay: python3 background/nodes/dossier_partial/audit.py
upstream mapping: certificate grammar v2 / finite adjacent partial
```

### Resolution

The stdlib-only Lean package was vendored unchanged from `rs-mca` commit
`53bb5df4d4d8d9be77c47c6f2e1f92e093824909` and builds under Lean 4.31.
Its source-tree hash is pinned and typed analytic targets remain non-claims.
The partial dossier packages the exact 506/507 row, envelope range, convention
freeze, compiler/harness commands, and a JSON non-claims set equal to all 13
critical red leaves. With all four packaging predicates proved, the packaging
conjunction is discharged.

### Next attack: rich-fiber structure

```text
claim id: f3_h3_mobius_rich_fiber_structure
mathematical question: does the largest known official M35 fiber decompose
  into finitely many exponent patterns forced by its quotient witness?
consumer: f3_h3_mobius_overlap_cap35
status: bounded route-selection experiment; no theorem claimed
input: n=8192, p=67657729 (observed overlap maximum 20)
falsifier/decision: unstructured exponent pairs favor replacing M35 by a
  weighted theorem; a small affine/cyclotomic pattern favors classification
resource: one 1 GiB Modal task, hard timeout 60 seconds
replay: modal run background/nodes/f3_h3_mobius_overlap_cap35/rich_fiber_modal.py
```

### 2026-07-12 paired-PGL2 bounded route test

```text
claim id: f3_h3_pgl2_pair_smallrow_falsification
mathematical statement under test: P(t)+2R(t)<=37 whenever t!=1 and R(t)>0,
  equivalently I_inv(t)+2I_aff(t)<=39
quantifiers and row scope: exhaustive over each enumerated prime-field row
  n=2^s, p=1 mod n, p>=n^2 in the printed shard ranges; this is route
  evidence only and is not an official-row proof
consumer and exact slot: f3_h3_mobius_excess_half, stronger M35 route
current status: bounded falsification experiment
dependencies already proved: f3_h3_pgl2_pair_identity
new open content: none; the pointwise constant remains unproved if it survives
falsifier: one enumerated parameter with P(t)+2R(t)>37
proof route being attempted: identify an extremal algebraic family from any
  counterexample; otherwise compare scaling before investing in a proof
replay command: modal run experiments/prize_resolution/f3_h3_paired_sweep_modal.py
upstream hard-input mapping: primitive shift-pair control / exact second moment
```

The exact run `ap-ttBP0c2JCopfqrGmGtvnI2` found `P(t)=20` but `R(t)=1`
at the maximum fiber. The unique quotient witness has exponent pair
`(4914,2457)=(2r,r)`, giving the telescoping parameter `t=1+q`. The pointwise
fiber is a finite-characteristic accident, but its contribution to the
oriented convolution is minimal.

### Route correction: weighted rich-fiber excess

```text
claim id: f3_h3_mobius_excess_half
mathematical statement: X_35=sum_{t!=1}(P(t)-35)_+ R(t) <= n^2/2
quantifiers and row scope: every official order and every official prime
consumer and exact slot: f3_h3_three_to_one_c36, nonidentity rich-fiber excess
current status: TARGET
dependencies already proved: identity Stepanov payment; product/quotient
  convolution; first-35 mass payment
new open content: the truncated weighted correlation bound
falsifier: one official row with X_35>n^2/2
proof route: simultaneous rich-product/rich-quotient incidence tail or
  oriented character estimate
replay: python3 critical/nodes/f3_h3_mobius_excess_half/verify.py
upstream mapping: exact primitive shift-pair/rich-fiber ledger
```

The weighted statement is strictly weaker than M35 and is the weakest clean
level-set form found so far that the C36' consumer accepts with ample exact
room. M35 was moved to the background as a sufficient route. This keeps one
red leaf on the critical path while allowing large product fibers whenever
their quotient weight is small.

### Proved quotient blocks and calibrated factorial route

The coefficient map `t -> (1/(1-t),-t/(1-t))` gives an exact partition of
nonidentity parameters into `H x H` coset blocks. If `B` is a block, then
`R(t)=|B|-1` for every `t in B`, and

```text
sum_B |B|(|B|-1)=(n-1)(n-2).
```

This identity is proved and independently enumerated on three rows. It is the
quotient collision ledger underlying the weighted leaf.

The integer inequality `(m-35)_+ <=m(m-1)/138` gives a standard sufficient
route:

```text
sum_(t!=1)P(t)(P(t)-1)R(t) <=69n^2 => X_35<=n^2/2.
```

The worst inspected boundary row has factorial moment `1.971577525n^2`
(Modal `ap-sTFOJvu8xxKqcxPrUt9l7r`), leaving a factor above `34` to the posed
constant. `FM69` is retained as a background attack route rather than made a
second critical conditional.

## 2026-07-12: WP0/WP4 G2 disposition

### Claim contract

```text
claim id: petal_g2_support_forcing
mathematical statement: every nonempty support is either aperiodic or an
  empty-tail staircase at its intrinsic dyadic stabilizer scale
quantifiers and row scope: every official power-of-two petal chart
consumer and exact slot: petal_growth structural periodic/primitive split
current status: PROVED
dependencies already proved: cyclic stabilizer partition
new open content: none in G2; pricing remains in G3/K4/P3
falsifier: a periodic support not equal to a union of its stabilizer orbits
proof route: direct cyclic group action
replay: python3 critical/nodes/petal_g2_support_forcing/verify.py
upstream mapping: quotient-periodic versus stabilizer-primitive partition
```

### Consumer-backward audit

The closure-form G2 claim is classification only and follows directly from
`thm:stabilizer-partition(i)`. The previously identified small-scale class
`2<=c(S)<=t` is real, but its numerator/multiplicity debt belongs to G3 and
the P3 quotient-profile emission, not to the dichotomy. G3 is now explicitly
quantified over every `M=c(S)>=2`, including those small scales; K4 remains
exactly the `c(S)=1` branch.

The fixed-M statement remains false. The verifier includes the banked `n=32`
witness as a mutation control: it is staircase at intrinsic scale `2` but not
at prescribed scales `4` or `8`.

## 2026-07-12: WP0/WP7 W2 endpoint and taxonomy closure

### Claim contract

```text
claim id: ww_lower_witnesses
mathematical statement: every clean-rate challenger spend has an explicit
  qcore family above floor(|F|/2^128) at the exact spent agreement
quantifiers and row scope: official clean rates 1/4,1/8,1/16; rate 1/2 excluded
consumer and exact slot: worst_word_challenger_pricing unsafe lower witness
current status: PROVED
dependencies already proved: quotient-core construction; spend map
new open content: none
falsifier: a spending row where qcore count is not above the threshold or
  misses the closed-radius endpoint
proof route: direct locator construction plus exact integer conversion
replay: python3 critical/nodes/ww_lower_witnesses/verify.py
upstream mapping: quotient-core lower staircase / unsafe-side comparison
```

### Resolution

The E15/X-4 taxonomy label is not consumed: the lower statement is a `sup_U`,
so the explicit qcore receiver is sufficient on its own. The endpoint seam is
also exact, not conjectural: `a` agreements give distance `n-a` and therefore
membership in the closed radius `1-a/n`; an integer family exceeds
`|F|/2^128` exactly when it has at least `floor(|F|/2^128)+1` members.

The qcore degree inequality is strict only for `sigma<M`; the verifier uses
`sigma=M` as a mutation control. Rate `1/2` remains outside W2 and continues
to be represented by `rate_half_band_closure`.

## 2026-07-12: WP4 G3 profile-conversion clause

### Claim contract

```text
claim id: petal_g3_profile_conversion_identity
mathematical statement: raw_M(A)=Q_M(A)*N/(N-h)*[x^b]H_M(x)^(N-h)
quantifiers and row scope: every partition n=MN and A=hM+b with h<N
consumer and exact slot: petal_g3_pricing_multiplicity clause (b)
current status: PROVED
dependencies already proved: canonical full-fiber/tail recovery; Q_M convention
new open content: none
falsifier: an admissible support omitted or multiply represented by the formula
proof route: exact double count of full fibers and proper-subset tails
replay: python3 background/nodes/petal_g3_profile_conversion_identity/verify.py
upstream mapping: profile-envelope conversion / periodic pricing column
```

### Resolution

Every admissible size-`A` support has exactly `h=floor(A/M)` full fibers and
a residual tail of size `b`. Choosing the full fibers and then the proper
subsets in the remaining fibers proves the identity. This closes G3's former
declared-weight placeholder. G3 remains red only for the per-received-word
sub-`k` codeword multiplicity.

### Verdict

`FIXED` scope/wiring defect. This intentionally increases the honest critical
frontier by one mathematical leaf. It is progress because full termination can
no longer occur while an official arity class is omitted.

## 2026-07-12: WP3 C36' Mobius-overlap decomposition

### Claim contract

```text
claim id: f3_h3_mobius_overlap_cap35
mathematical statement: every nonidentity product fiber on the quotient
  support of A=(1-H)\{0} has multiplicity at most 35
quantifiers and row scope: every official n=2^s, 13<=s<=41, and every prime
  p=1 mod n with p>=n^2
consumer and exact slot: f3_h3_three_to_one_c36, nonidentity terms of
  N_3to1=sum_t P(t)R(t)
current status: TARGET
dependencies already proved: the product/quotient convolution identity;
  one-shift Stepanov bound P(1)<4n^(2/3)
new open content: max{P(t):t!=1,R(t)>0}<=35
falsifier: one official (n,p,t) with R(t)>0 and P(t)>=36
proof route: simultaneous product/quotient Stepanov polynomial or power-two
  cross-ratio rigidity retaining t in A/A
replay command: python3 background/nodes/f3_h3_mobius_overlap_cap35/verify.py
upstream mapping: primitive shift-pair control; exact second-moment/rich-fiber
  ledger
```

### Finding

The oriented three-to-one count admits a sharper level-set compiler than the
shifted-energy envelope. The identity quotient fiber is already paid by the
proved one-shift Stepanov estimate. A uniform cap of `35` is needed only on
nonidentity product fibers whose parameter lies in the quotient support.
Under that single premise,

```text
N_3to1 < 4n^(2/3)(n-1)+35(n-1)(n-2),
```

which is strictly below the repaired C36' threshold at all 29 official
orders. The implication is exact and independently replayed.

The existing twelve-prime `n=8192` Modal instrument already measured the
relevant overlap maximum. A fresh replay (`ap-SSyWX6F4I6C3DMzaKwx3rk`)
completed all rows in under four seconds per task and found maxima `14..20`.
This is falsification resistance, not proof.

An independent consumer-backward arithmetic implementation, including a
`cap=36` mutation control, lives at
`experiments/prize_resolution/audit_c36_mobius_compiler.py`.

### Repairs

- replaced stale `8n^(4/3)` thresholds in the direct-floor and Modal packets
  by the canonical catch-#71 value `16n^(4/3)`;
- repaired a broken replay import in `f3_h3_three_to_one_direct_floor.py`;
- rewired C36' as amber conditional on the new red Mobius-overlap leaf.

### Replay

```text
python3 background/nodes/f3_h3_mobius_overlap_cap35/verify.py
python3 experiments/prize_resolution/audit_c36_mobius_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_three_to_one_direct_floor.py
python3 tools/verify_prize_dag.py
python3 tools/build_critical_orbit.py
```

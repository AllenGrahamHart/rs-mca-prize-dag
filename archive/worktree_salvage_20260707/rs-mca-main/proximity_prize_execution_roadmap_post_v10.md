# RS-MCA to Proximity Prize: Execution Roadmap Post-v10

Status: AUDIT / proposed working roadmap.

Source: imported from a Claude/Fable discussion and normalized for the repo by
Codex acting autonomously for AllenGrahamHart.

Baseline: `main @ 495ee48` ("Sync guides and site to Paper D v10",
2026-07-01), plus open PR #170 and PR #171.

This note does not supersede `towards-prize.md`.  Until reviewed and merged
into the maintainer roadmap, `towards-prize.md` remains the source of truth.
This note is intended as an execution scaffold: it folds in the two open PRs,
decomposes the remaining distance to the prize into concrete work packages, and
makes the critical path and major risks explicit.

## 0. Ground Truth

The Proximity Prize asks for thresholds for smooth-domain Reed-Solomon codes

```text
C = RS[F, D, k],
rho in {1/2, 1/4, 1/8, 1/16},
k <= 2^40,
epsilon* = 2^-128.
```

The repo-internal threshold formulation is:

```text
B_C(a0)     > B*(q_line) = floor(q_line / 2^128)    unsafe
B_C(a0 + 1) <= B*(q_line)                            safe
```

A full resolution should eventually be a theorem, or theorem plus certified
computation, that outputs the safe/unsafe adjacent agreement levels for every
admissible row in the official regime, with the object, sampler, denominator,
and endpoint convention printed.

Two structural facts frame the work.

1. The unsafe half is largely done.  Papers A/B and Paper D v10 give floors and
   caps.  The missing half is safe-side machinery below the caps, especially
   the aperiodic term after tangent, quotient, and extension ledgers have been
   removed.

2. The repo object and the official ABF object are not yet certified to
   coincide.  The M0 freeze in PR #171 deliberately leaves external sampler
   reconciliation open.  Object reconciliation is therefore a gate, not a
   later packaging nicety.

Pinned row constants:

```text
C = RS[F_17^32, H, 256], |H| = 512
n = 512, k = 256, rho = 1/2
floor(17^32 / 2^128) = 6
floor((17^32 + 1) / 2^128) = 6
LD_sw(C,506) = 7 unsafe
LD_sw(C,507) = 6 safe
M3 window: 385 <= A <= 426
regular overdetermined starts at A = 385
tangent exactness starts at A = 427
minor size m = j + 1 runs 128 down to 87
degree-only sum over the window = 4515 >> 6
```

Important consequence: by monotonicity, the 506/507 transition already pins
the pinned `F_17^32` row.  Work in the M3 window for this row is methodology
development, not a new threshold result for that row.  Its value is that it is
a fully controlled proving ground for aperiodic safe-side machinery that should
transfer to rows with much larger `q_line`.

## 1. State Snapshot

### Main at Baseline

Paper D v10 supplies:

```text
universal and first-grid caps
quotient support/image/dual-cosupport ledgers
extension-pole floor
canonical regular-Hankel gcd/lcm ledgers
aperiodic chart atlas
```

`towards-prize.md` says:

```text
M0 definition freeze: supplied by PR #171, object reconciliation still open
M1 schema checker: done
M2 high-agreement smoke row: done
M3 regular non-tangent window: in progress
M4 quotient/tangent subtraction table: not complete
M5 singular bucket program: narrowed but not complete
M6 M1 theorem candidate: not started
```

### Open PR #170

PR #170 is the synthetic low-rank / spectral-reduction lane.

Core outputs:

```text
low-rank synthetic ladder ranks 2..12 closed:
  finite affine canonical gcd has 0 roots for the checked family
  projective endpoint [0:1] is quotient-image paid by c=2 witnesses
  paid residual ledger closes the family

spectral reduction:
  det(H_X^(h) + Z H_Y^(h))
    = det(V_X)^2 prod(X)^h det(I + Z K_h)
  K_h is an explicit low-rank Lagrange/Cauchy kernel
  coefficients are replacement-subset / Cauchy-Binet sums
  Toeplitz-Cauchy factor T[a,i] = 1/(1-alpha^(m+a-i))
  rank-one displacement T - U T V = 1_r 1_m^T
  shift-two transfer gives a 2x2 comparison between same-parity shifts

explicit open target:
  gcd(Phi_{m,r,0}, Phi_{m,r,1}) = 1
  for 87 <= m <= 128 and 2 <= r <= ceil((m-1)/2)

weaker all-contiguous target:
  gcd(Phi_{m,r,h}: 0 <= h < 258 - 2m) = 1

rectangular null-polynomial formulation:
  true rank-drop slope is one degree-<m polynomial with a whole run of
  vanishing weighted moments, not merely per-block singularity.
```

The PR includes a counterexample-first search utility and a replayed frontier
probe at `A=426`, ranks `13..20`, with common gcd degree `0`.

### Open PR #171

PR #171 is the M3/M4 chart-atlas and lemma-kit lane.

Logical groups:

```text
M0 definition-freeze audit note
subgroup syndrome-section theorem
canonical gcd formula theorems for structured zero-u families
support/weight-uniform one-spike family theorem
M4 projective direction-rank budget split
direction-rank degree cap
rank-6 ambient sharpness counterexample
affine-pivot compression theorem
affine-pivot gcd-equivalence theorem
M5 finite/projective kernel charts
regular-root rank-drop bridge
rank-node regular/singular dichotomy
null-polynomial split-locator gate
regular-bucket synthesis table
local zero-u, zero-v, proportional, tangent-overlap, and infinity lemmas
checker upgrade
```

Two especially load-bearing PR #171 facts:

1. Rank-6 ambient sharpness: in the ambient regular-pencil class, six finite
   roots and one projective endpoint can coexist.  Direction rank plus generic
   regularity plus one endpoint is not enough to close the boundary.

2. Null-polynomial split-locator gate: ambient regular root tables are safe
   upper bounds, but actual support-wise split-locator witnesses must pass the
   divisor gate `L | X^512 - 1` and the noncontainment gate `H(v)ell != 0`.

### Live Fronts

Front alpha:

```text
prove or refute spectral disjointness:
gcd(Phi_{m,r,0}, Phi_{m,r,1}) = 1
or the weaker all-contiguous gcd target.
```

Front beta:

```text
close the direction-rank-6 endpoint-sensitive boundary using Hankel-specific
structure, exact compressed root tables, or endpoint payment/emptiness.
```

Every near-term mathematical PR should advance alpha, beta, or the
stratification reducing the general pencil to alpha/beta-shaped pieces.

## 2. Critical Path

```text
P0 gates:
  object reconciliation
  rules audit
  integrate PR #170 and #171
  verification harness

P1 finite-row package:
  pinned F_17^32 row, already threshold-pinned

P2 M3 window campaign:
  alpha spectral disjointness
  beta rank-6 boundary
  syndrome stratification
  M4 deduped table
  M5 residual charts

P3 prize-scale rows:
  Prime192 / near-2^256 rows
  localize transition windows
  apply P2 machinery symbolically

P4 M6 uniform theorem:
  aperiodic local-limit theorem after paid ledgers
  Graver/projection wall
  BETA_2 global conductor/monodromy wall

P5 list lane:
  L1 image-fiber theorem
  L2 interleaved constants

P6 bridges:
  F1 safe-side classification
  M2 line-decoding bridge
  X1 bridge ledger

P7 assembly:
  certificate compiler
  paper promotion
  formal gates
  submission dossier
```

Sequencing rule: P0 gates all prize-facing packaging.  P1 can run in parallel
because it consumes settled high-agreement material.  P2 is the main bottleneck
for P3 and P4.

## 3. Work Packages

### WP-0.1 Object Reconciliation

Goal: prove, or explicitly bridge with printed losses, the relation between
the frozen repo support-wise `B_C(a)` object and the official ABF
`epsilon_mca` object.

Axes to audit:

```text
batching shape: powers-of-alpha vs affine/projective lines
ell > 2 batching
quantifier order
same-support noncontainment
finite vs projective sampler
q_gen, q_line, q_chal
closed-grid vs supremum threshold
```

Deliverable:

```text
experimental/notes/audits/object_reconciliation_abf.md
```

Exit test: every axis is `EQUAL`, `BRIDGED(loss printed)`, or `OPEN`; zero
`OPEN` axes before any "prize-facing" claim is packaged.

Failure branch: any inequivalent axis becomes a new ledger column, not a prose
handwave.

### WP-0.2 Official Rules Freeze

Goal: freeze the operative prize constraints from proximityprize.org and ABF.

Deliverable:

```text
experimental/notes/audits/prize_rules_freeze.md
```

This should record field-range wording, domain assumptions, fixed/dithered
`k`, whether per-row answers count, partial-prize mechanics, and submission
format.

### WP-0.3 Integrate PR #170 and PR #171

Checklist:

```text
replay every verifier and certificate in both PRs
run upgraded checker against pre-existing packets
hand-merge agents-log.md entries by timestamp
spot-audit affine pivot compression, gcd equivalence, subgroup syndrome section
independently verify rank-6 ambient sharpness
log integration
```

Future recommendation: one theorem-cluster per PR; avoid mega-PRs.

### WP-0.4 Verification Harness

Goal:

```text
make verify
```

or equivalent script that discovers deterministic verifiers, checks certificate
hashes, runs the aperiodic packet checker, and emits one PASS/FAIL table.

Checker hardening:

```text
removed ledger refs resolve
declared numerators are recomputed
residual labels are from the allowed set
object/sampler/denominator blocks are present
cross-packet paid-root dedup is enforced
```

### WP-1.1 Pinned Finite-Row Submission Note

Goal: package the already pinned `F_17^32` threshold in repo and official
language after WP-0.1.

Deliverable:

```text
experimental/notes/submission/f17_32_partial_note.md
```

Exit test: two independent replays of the 506/507 numerator values agree.

### WP-1.2 Formalize Counting Core

Goal: Lean finite-certificate statements for the pinned row and the 506/507
numerators.  Scope tightly to finite certificate statements, not the entire
tangent theory.

### WP-2.1 Front Alpha: Spectral Disjointness

Targets:

```text
alpha-strong:
  gcd(Phi_{m,r,0}, Phi_{m,r,1}) = 1
  for 87 <= m <= 128, 2 <= r <= ceil((m-1)/2)

alpha-weak:
  gcd(Phi_{m,r,h}: 0 <= h < 258 - 2m) = 1
```

Attack ladder:

```text
1. Full-grid counterexample-first scan.
2. Spectral reformulation via generalized spectra of -D_h S_h.
3. Resultant route using structured determinant/product identities.
4. Rectangular null-polynomial / moment-run rigidity route.
5. Characteristic hygiene for char 17 and all future char p.
```

Deliverable on success:

```text
experimental/notes/m3/spectral_disjointness_theorem.md
experimental/data/certificates/hankel-f17-32-m3-spectral-disjointness/
```

Deliverable on failure:

```text
experimental/data/certificates/hankel-f17-32-m3-spectral-collision/
```

Failure branch: if a collision is paid, refine the target to a paid-root gcd
statement.  If it is unpaid, promote it to `candidate_new_obstruction`.

### WP-2.2 Front Beta: Rank-6 Endpoint-Sensitive Boundary

Goal: for nonsingular regular buckets with direction rank exactly 6, prove one
of:

```text
beta1: compressed 6x6 canonical root table is empty or within budget
beta2: every finite root / projective endpoint is paid
beta3: construct a Hankel-realizable sharpness example and count it
```

Attack ladder:

```text
1. Realizability search: can the ambient sharpness example be Hankel-realized?
2. If not, isolate and prove the Hankel obstruction.
3. Compute compressed 6x6 gcds on contiguous charts at window endpoints.
4. For surviving roots, run paid-ledger witnesses.
```

Deliverable:

```text
experimental/notes/m1/rank6_boundary_closure.md
experimental/data/certificates/hankel-f17-32-m3-rank6-{closure|sharpness}/
```

### WP-2.3 Syndrome-Space Stratification

Goal: partition all syndrome pairs `(u, v)` at each agreement into strata that
end in allowed labels:

```text
tangent-paid
quotient-paid
regular-closed(root table)
pivot-chart(M5)
residual(named)
```

Axes:

```text
direction rank
zero-u / zero-v / proportional special cases
tangent overlap
quotient periodicity
lower-rank containment
kernel-containment behavior
split-locator gate behavior
```

Deliverable:

```text
experimental/notes/m1/m3_window_stratification.md
```

Exit test: fuzz and adversarial syndrome-pair tests route to leaves whose
predicted contribution is confirmed by direct computation on selected small
instances.

### WP-2.4 M4 Deduped Assembly Table

Goal: emit the M4 table requested by `towards-prize.md`:

```text
A
B_tan
B_quot_support
B_quot_image
B_ext
B_ap_regular
B_ap_pivot
deduped_total
deduped_total <= 6?
lower bound
gap
```

The table must be generated by script and the dedup arithmetic must be checked,
not trusted.

### WP-2.5 M5 Residual Chart Closure

Goal: close every residual leaf by affine pivots, projective infinity charts,
curve coefficient pivots, dimension-degree diagnostics, or a named residual
classification.

Exit test: zero `unknown` leaves in the pinned M3 window.

### Phase P2 Exit Criterion

P2 is done when:

```text
alpha resolved, positively or negatively
beta resolved, positively or negatively
stratification note merged
M4 table complete
every residual named
experimental/notes/m1/f17_32_window_theorem.md exists
```

### WP-3.1 Prize-Scale Row Selection

Pick target rows:

```text
one from leaderboard_sweep_192
one near the top of the field range
one quotient-hostile stress row
```

For each, localize the transition window with floor/cap/tangent information.

### WP-3.2 Symbolic Scaling

Upgrade P2 lemmas from the pinned row to symbolic row descriptors:

```text
abstract order-2^s subgroup hypotheses
characteristic exclusions
symbolic stratum descriptors
non-enumerative root-counting theorems
complexity bounds
```

### WP-3.3 Pin a Second Row or Name the Wall

Goal: obtain a second prize-scale pinned row, or produce a wall note with a
minimal toy reproduction and an explicit consumer theorem.

### WP-4.1 Uniformize Displacement Structure

Goal: state and prove the #170 displacement/spectral identities over an
arbitrary field containing an order-`2^s` root of unity, with characteristic
exclusions.

### WP-4.2 Projection-to-Graver Wall

Goal: freeze the exact missing projection inequality and either prove it,
reduce it to moment-run rigidity, or adopt a dithered retreat theorem with
printed costs.

### WP-4.3 BETA_2 Wall

Goal: freeze the needed global monodromy/conductor statement as a standalone
conjecture with a consumer theorem, then pursue proof, density theorem, or
counterexample scans.

### WP-4.4 Hypothesis Management and Dithering

Goal: print a hypothesis-coverage table for every official rate and relevant
`n`, including any dither costs and official-rules status.

### WP-5.1 L1 Image-Fiber Local Limit

Use `ImgFib_U`, not raw `Fib_U`.  Prove a locator image-fiber bound consumable
by L2, with `q_gen` printed in every denominator.

### WP-5.2 L2 Interleaved Constants

Consume L1 through the codegree reduction.  Do not let the reduction claim its
own base-list input.

### WP-6.1 F1 Safe-Side Classification

Prove every genuinely `F`-valued bad line above the corrected reserve is
covered by extension or aperiodic ledgers, or produce bucket tables where it is
not.

### WP-6.2 M2 Line-Decoding Statements

Convert pinned MCA thresholds into line-decoding language without denominator
drift.

### WP-6.3 X1 Bridge Ledger

One table per bridge used in the submission chain:

```text
list <-> CA <-> MCA <-> LD <-> curve
radius loss
field loss
sqrt loss
support convention
sampler
```

### WP-7.1 Assembly Compiler

Implement a certificate compiler:

```text
input:
  field tower, D, n, k, rho
  q_gen, q_line, q_chal
  sampler, epsilon*
  quotient profile
  packet refs

output:
  a_safe, a_unsafe
  per-ledger status
  comparison against floor(q_line / 2^128)
```

The compiler refuses a verdict if any needed ledger is conjectural, unless run
in explicitly labeled conditional mode.

### WP-7.2 Paper Revision and Promotion

Promote stable theorem packets from `experimental/` to Papers B/D/C only after
maintainer review.

### WP-7.3 Formal Gates

Priority:

```text
definitions and finite certificate statements
M4 dedup arithmetic
highest-risk algebraic counting lemmas
```

### WP-7.4 Submission Dossier

Versioned dossier:

```text
partial: pinned finite row
interim: pinned row + window theorem + second row or named wall
full: uniform theorem + list lane + bridge lanes
```

## 4. Standing Orders

1. Every safe-side claim is a v10 packet.
2. Run counterexample-first scans before long proof attempts when feasible.
3. Paid-root dedup must be checker logic.
4. State new lemmas over abstract order-`2^s` subgroups when possible.
5. Do not optimize the pinned row threshold; it is already pinned.
6. Prefer one theorem-cluster per PR.
7. Every note prints object, sampler, denominators, and endpoint convention
   when those matter.
8. Walls need frozen statements, consumer theorems, toy instances, and scans.
9. Never let a reduction claim its own input.
10. Log agent work in `experimental/agents-log.md`.

## 5. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---:|---:|---|
| Repo object differs from official `epsilon_mca` | medium | fatal if late | WP-0.1 gates prize-facing packaging |
| Front alpha false | medium | medium | counterexample-first scan, paid-collision fallback |
| Front beta realizable sharpness | medium | medium | count it; a named polynomial-size stratum may still be fine |
| Uniform theorem false as stated | open | high | keep negative-resolution path first-class |
| Prize rules diverge from working regime | low-medium | high | WP-0.2 rules freeze and periodic recheck |
| Weak checker lets bad packets pass | medium | high | WP-0.4 hardening and corrupted-packet tests |
| Queue thrash from mega-PRs | high | medium | one theorem-cluster per PR and timestamped logs |
| Characteristic arithmetic bugs | medium | high | characteristic-hygiene audit in alpha/WP-4.1 reviews |

## 6. Immediate Queue

1. Integrate PR #170 and PR #171 with the WP-0.3 checklist.
2. Write object-reconciliation note plus acid test.
3. Write official-rules freeze note.
4. Add `run_all_verifiers` / checker hardening / CI.
5. Run full-grid spectral scan for front alpha.
6. Run rank-6 Hankel-realizability search for front beta.
7. Attempt the moment-run rigidity lemma in abstract-subgroup form.
8. Build stratification case-tree v1 from the PR #171 lemma kit.
9. Build M4 table generator with conditional cells where alpha/beta remain open.
10. Write finite-row submission note for the pinned row.

## 7. Success Criteria

Delta over `towards-prize.md`:

```text
object-reconciliation note with zero OPEN axes
checker recomputes every numerator
window theorem with abstract-subgroup lemma index
one prize-scale row pinned or one wall frozen as conjecture + consumer
dossier versioning with nonclaims intact
```

Shortest current path:

```text
object reconciliation
  + integrate PR #170/#171
  + resolve alpha and beta
  + stratify the M3 window
  + build window theorem
  + transfer to a Prime192-class row
  + uniformize displacement identities and wall packages
  + complete L1/L2 and bridge lanes
  + assembly compiler, formal gates, dossier
```

This route deliberately keeps negative-resolution outcomes first-class:
determining that the true threshold is lower than hoped is still a resolution
if the floors, caps, and safe side meet with certified adjacent agreement
levels.

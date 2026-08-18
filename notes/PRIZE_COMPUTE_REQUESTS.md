# Proximity Prize deferred compute requests

> **OPERATING PROTOCOL:** Authorization, RAM discipline, and upstream handoff
> rules are summarized in `notes/JOINT_PRIZE_RESOLUTION_PROTOCOL.md` section
> 10. This file remains the authoritative request ledger and run log.

> **PLAN-OF-RECORD POINTER (2026-07-22).** The resolution roadmap was
> rewritten as the date-free r3 gates-not-dates form and installed at
> `notes/PRIZE_RESOLUTION_ROADMAP.md` (maintainer-directed; supersedes every
> prior copy including branch-local ones — KB #120). Before posing a new
> campaign or large compute request, re-read it: sequencing is by the gates
> D0/D1/U3/D3, the dli lane carries a standing one-third effort cap (D2),
> and new poses should name their track (N/A/B/C/H) and pre-registered
> falsifier.

This ledger records computations whose outputs could close or decisively
reshape a named proof branch but whose conservative cost exceeds the current
sub-`$1` Modal policy. It is suitable for contributor requests and upstream
PR notes. Entries are not theorem claims, and partial runs are evidence only.

Every request must specify the mathematical decision, completeness boundary,
certificate format, deterministic checker, resource estimate, and effect of
both outcomes on the critical DAG. Shallow sweeps without a named decision do
not belong here.

> **MAINTAINER GOVERNANCE NOTE (2026-07-20, wave-17 integration — UNRATIFIED;
> carried forward 2026-07-21 across the w18-C1 ledger adoption).**
> The sub-`$1` Modal self-authorization clause remains maintainer-unratified
> (standing item w16-C5). Wave-17 was the **first wave to actually exercise
> it**: three in-tree Modal launches, each a no-hit exclusion screen whose
> `result.json` is **load-bearing for a PROVED node's `verify.py`** (via a
> local coverage/hash certificate checker; no local re-execution):
>
> | app_id | screen | ceiling | candidates/shards | hits | consuming PROVED node |
> |---|---|---|---|---|---|
> | `ap-6KQ2mJjoE3Qkq7VaKqnxlZ` | c1-parity-antiinvariant | `$0.25` | 2,247,721 / 16 | 0 | `…c1_parity_frobenius_router` |
> | `ap-Js6Im9DeoBlc0di05YG2WE` | c1-parity-harmonic-characteristic | `$0.50` | 4,495,441 / 32 | 0 | `…c1_parity_harmonic_exclusion` |
> | `ap-PVTrzkKlh4j1B6qDmGU1Wf` | harmonic-top (order 2^41) | (none stated) | 2,247,720 / 16 | 0 | `…matched_post_field_compiler` |
>
> The three nodes are wired **ev-only** into `rate_half_list_adjacent_crossing`
> (still TARGET); no red flipped on their account. Wave-18 launched zero jobs
> and TIGHTENED the policy (the >= `$1` / unknown / could-exceed-balance
> do-not-launch rule below).
>
> **RESOLVED 2026-07-21 (maintainer ruling, w17-C1).** (a) Remote no-hit
> screens carrying a local coverage/hash certificate ARE accepted as PROVED
> evidence; the three screens' launchers and checkers are now registered in
> the verifier manifest via per-node `verify_screen_certificate.py` (hash
> pins) and `verify_screen_remote.py` (remote launcher). (b) The sub-`$1`
> self-authorization clause is SUPERSEDED by the **time-based rule** in the
> maintainer-ruling section below: self-authorized launches must keep total
> wall-time under 5 minutes. This also settles standing item #260 in
> principle (queued jobs re-screen under the time rule).

## Current spend freeze

As of 2026-07-21, the local Modal account has about `$3` of credit remaining.
No large run in this ledger is authorized against that balance. Preserve it
for an explicitly approved, route-deciding pilot with a conservative total
cost below `$1`; otherwise treat every entry as an outbound contributor
request for an upstream PR.

Record newly identified valuable computations here even when they are not yet
executable. Use a **pre-request** while a finite completeness router, measured
pilot, checker, or cost ceiling is missing. Promote it to a numbered request
only when another contributor can run a bounded campaign and know exactly what
PASS, FAIL, and incomplete output mean. This distinction prevents an
open-ended search from being presented as useful donated compute.

The default disposition for any newly identified run whose conservative cost
is at least `$1`, is unknown, or could exceed the local balance is: do not
launch it; record it here with its proof purpose and readiness gaps. When the
related mathematics is vendored to Przemek's repository, include the record
as an upstream compute request so a contributor with suitable resources can
accept a declared budget and run it independently.

## Maintainer ruling (2026-07-21): time-based self-authorization

The self-authorization criterion above ("explicitly approved ... conservative
total cost below `$1`") is **superseded**. A Modal launch is self-authorized
if and only if ALL of:

1. it is **route-deciding** for a named node or pre-registered falsifier;
2. its conservative estimate of **total wall-time is under 5 minutes**
   (per-shard timings must be banked in the certificate so the bound is
   auditable after the fact);
3. a **result certificate + deterministic local checker** are banked with the
   launch (coverage accounting, per-shard hashes, hit list), and the checker
   is registered in the verifier manifest when the result becomes
   load-bearing for a node's verifier;
4. the launch is **logged in this ledger** (app id, purpose, wall-time).

Anything failing any clause is an outbound contributor request. The dollar
phrasing elsewhere in this file is retained for historical continuity; the
time rule governs. (Ruling recorded in notes/MAINTAINER_DECISIONS_20260713.md;
standing item #260's queued jobs re-screen under this rule.)

### Current operational cap (2026-07-22)

The monthly Modal allowance has refreshed to about `$30`. A self-authorized
launch must still satisfy every rule above **and** have a conservative total
cost below `$1` unless the maintainer explicitly approves more. Thus the
operative test remains the intersection of the five-minute and sub-`$1`
ceilings, not either ceiling alone. Runs costing tens or hundreds of dollars
are out of scope.
Valuable runs exceeding either ceiling, or lacking a reliable cost estimate,
must be recorded here and copied into the corresponding upstream PR as
requests for contributors with available compute.

## Request queue

| priority | request | readiness | contributor action | current authorization |
|---|---|---|---|---|
| P1 | CR-002 quotient-pencil rank-two classification | matched `c=0` and generic `c=1` norm contracts are complete; c2 parity shares them conditionally on C2-PAR; minimum support in the one-antipodal route is reduced to one explicit pair-collision curve; compressed implementations and pilots are missing | screen the `M=2^35` top norm and 36-level tower first; use `CR-002-C2CELL-COLL` for the separate one-pair design request | algorithm request only; cost unknown |
| P2 | CR-001 H3 high-excess certificate | blocks are formula-generated; a complete dense `n=8` Taylor conformance oracle is banked; sparse/distributed implementations and comparative cost pilots are missing; the maximum-degree class carries `75.009%` of degree at `n=8192` | first match the `n=8` hashes and support sets, compare Smith, Taylor cutoffs `2<=c<=35`, and three-resultant screening on complete small orders, then exercise a maximum-degree block before pricing production; evaluate `(36,1)` only on retained official primes | external pre-request only; no large run; cost unknown |
| P3 | CR-003 rate-half Hankel sharp-cap classification | the official distance-three chart is theorem-closed; live proof surfaces are the strict/half-distance `A=3` profiles, the high quotient-distance `A=1` tail, and other `A=1` component faces; `CR-003-CLIFT` is optional analogue auditing only | build coverage-complete symbolic compilers and measured pilots for one live face before pricing a run; do not launch distance-three support, pairing, tail, circuit, static-gcd, residual-pencil, or quartic-map fleets | pre-request only; raw census unauthorized |
| P4 | CR-004/CR-004-X6 WCL ten-slot classification | all ten cells are machine-enumerated; all have fixed unit-ideal endpoints; 934 powered samples across four cells found zero events but prove no subtraction | compute replayable modular unit bases and integer certificates, starting with the smallest `(1,5)` endpoint; do not scale the sample screens into blind fleets | external request only; do not duplicate expansion or support fleets |

Priority records expected proof value, not an instruction to spend. A request
remains unauthorized until a contributor accepts its resource cap. If a PR
cannot vendor the proved router, the checker, and the PASS/FAIL DAG contract,
it should link this ledger as future work rather than solicit the computation.
Cost estimates are conservative ceilings and must include failed shards and
retries; raw artifact storage is separate.

### Resolved CR-KB-C2-112-POS-QS-SAT: aligned positive q-slice saturation

- **Decision:** delete or exhibit an admissible survivor in the aligned
  positive saturated source-line `(1,1,2)` branch of `rate_half_band_closure`.
- **Complete algebraic input:** twelve fraction-free five-equation ideals:
  fixed-moving or moving-moving internal edges, three UFD allocations of the
  two residual quadratics, and unramified or repaired `w=0`. The endpoint
  roots occur only through `p=cd,t=-(c+d)`. Four equations impose the chosen
  allocation and `D*lambda_scale-L=0` restores the exact relative U/V scale.
- **Banked generator:**
  `critical/nodes/rate_half_band_closure/notes/kb_c2_112_positive_qslice_symmetric.py`.
- **Required output:** a comprehensive Gröbner/Bezout/subresultant certificate
  for the six remaining unramified ideals after saturation by `L*D`, exactly
  the printed denominators, and collision factors, plus a dependency-free
  exact checker. Generic-field gcds, pairwise resultants, and numerical slices
  are incomplete.
- **Banked close:** PROVED node
  `rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_ramified_q_slice_exclusion`
  closes all six repaired `w=0` cells. It retains the exact scale, audits the
  raw norm independently, descends moving reciprocity to `s=b+1/b`, and gives
  six unit full-forbidden saturations over `F_2130706433`. The earlier
  unscaled minor/FLINT pilot and its hashes remain retracted.
- **Bounded local pilot (2026-07-30):** the fixed-moving unramified `same`
  cell generates four scale-substituted equations of shapes
  `(degree,terms)=(16,870),(16,900),(13,396),(13,405)` after exact removal of
  `w^2(p-1)^2`. Both the direct deployed-field full saturation and the first
  quadratic-in-`b` scale-free resultant reached the hard `60 s`
  `ramguard tiny` limit without a certificate. Do not rerun this SymPy
  representation unchanged; use modular interpolation, a dedicated
  quadratic-resultant emitter, or contributed compute with streaming partial
  factors.
- **Dedicated-FLINT update (2026-07-30):** the corrected quadratic compiler
  now emits three star resultants, four factored coefficient minors, and the
  first projection cascade in about `21 s` under the same `256 MB / 60 s`
  envelope.  The common linear projection component is exactly excluded by
  forbidden support.  The common reciprocal quartic is generically rank two
  but fails the kernel-conic condition; its exceptions are reduced to a
  printed degree-`496` norm in `t` plus four denominator factors.  See
  `kb_c2_112_aligned_positive_unramified_fixed_same_frontier_20260730.md`.
  The same router now narrows all three fixed-moving allocations.  Their
  nontrivial divisorial components reduce to degree-`496`, degree-`225`, and
  degree-`48` kernel-conic norms; the mixed linear rank curve adds a
  degree-`116` norm.  Exact reciprocal trace descent now also narrows the
  moving-moving cells.  Their linear components are entirely forbidden;
  their remaining common components leave degree-`160`, degree-`26`, and
  degree-`1224` conic norms for `same`, `swap`, and `mixed`, respectively.
  The degree-12 mixed component is screened without a function-field gcd.
  The moving `swap` and `same` finite and off-common ledgers are fully
  replayed and mint PROVED q-slice exclusions. Moving `mixed` has four exact
  q-slice points over degrees `3,3,7,7`; only the two degree-3 traces embed in
  the deployed field, and all four reciprocal orientations fail both full
  colored quotient norms. Its twelve off-common combinations are boundary,
  so a separate PROVED full-quotient node closes that cell. Fixed `same`
  subsequently leaves four base-field q-slice points on its direct quartic;
  all four fail both full quotient norms, while both off-common branches are
  boundary. A separate PROVED node closes fixed `same`. Fixed `swap` leaves
  one quadratic-field point on its degree-333 direct norm; it also fails
  both full quotient norms, while all nine off-common endpoints are boundary.
  A separate PROVED node closes fixed `swap`. Fixed `mixed` leaves four
  quadratic-field q-slice points on its degree-338 direct norm; all fail both
  full quotient norms. Its complete degree-116 raw linear-rank norm is empty,
  and its 20 off-common combinations give five boundary endpoints. A third
  PROVED node closes fixed `mixed`; all six unramified allocations are done.
- **PASS:** mint PROVED aligned-positive unramified full-quotient exclusion
  nodes;
  together with the ramified and aligned-negative theorems, delete the
  complete aligned source-line branch.
- **SURVIVOR:** replay it independently, then route it to both full quotient
  identities; do not repair the deletion claim by genericity.
- **INCOMPLETE:** evidence only; no DAG status change.
- **Authorization:** resolved locally; no external or Modal request remains.
- **Branch close:** the PROVED complete source-line exclusion composes all 32
  census/compiler/cell prerequisites. The residual `c2(1,1,2)` frontier is
  coordinate and source-cover assembly, not another saturation computation.

### Resolved CR-KB-C2-112-NEAR-QS-ELIM: near-aligned q-slice elimination

- **Decision:** delete or exhibit an admissible reconstructed source form in
  the near-aligned saturated source-line `(1,1,2)` branch.
- **Exact specialization:** orient `J_1={eta,ell}` as `(c,d)`. The forced
  square is `w=1/c`, while the residual target roots are `tau(xi)` and `1/d`.
  Retain the exact `lambda_scale` normalization from the corrected positive
  generator. There are three relative `xi` orbits after fixing the common
  endpoint, two internal templates, and three residual allocations, hence 18
  affine positive charts. Treat repaired `w=0` in a separate homogeneous
  chart. Negative forms must first lie on the proved fixed-moving `B=0` or
  moving-moving `B*C=0` reconstruction loci.
- **Banked direct-square chart:** PROVED node
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_fixed_xi_direct_square_exclusion`
  treats fixed-moving, common endpoint `xi=2`, and the square allocation
  `(c -> 1/2, d -> 1/d)` over the deployed KoalaBear field. Four correct
  generic line-pair eliminations and both full leading-zero branches are
  covered by independent resultant and Bezout replays, including exact
  reduction modulo `p=2130706433`. The former middle eliminants remain
  retracted because they extracted only the exact monomial coefficient of
  `b`; both current checkers carry a regression fence for that error.
- **Banked swapped-square chart:** PROVED node
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_fixed_xi_swapped_square_exclusion`
  treats the same normalized fixed-moving template with target roots
  interchanged. Four generic pair certificates and two exceptional-line
  classifications have only forbidden support; independent opposite-variable
  elimination and exact reduction modulo `p=2130706433` confirm them.
- **Banked mixed chart:** PROVED node
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_fixed_xi_mixed_exclusion`
  treats the same template with both distinct target roots on both residuals.
  Degree-96 and degree-186 projection certificates have collision-only common
  support, independently in both projection directions and modulo the
  deployed characteristic.
- **Banked reciprocal-xi mixed chart:** PROVED node
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_tau_xi_mixed_exclusion`
  applies the same dual-projection certificate to target roots `2,1/d`.
- **Banked reciprocal-xi square charts:** PROVED node
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_tau_xi_square_exclusions`
  covers both square allocations with all eight generic endpoint-line pairs,
  every leading-zero branch, an independent opposite-variable audit, and
  exact replay modulo `p=2130706433`. Its exceptional support is either a
  collision, inversion-fixed, or on the excluded `z=1` locus.
- **Banked other-xi direct square chart:** PROVED node
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_other_xi_square_xi_exclusion`
  treats `xi=b` and `c->1/b,d->1/d`. Four product-branch pairs,
  every linear leading-zero fiber, a direct/resultant path, and an independent
  fraction-free/subresultant path have only forbidden support in
  characteristic zero and modulo the deployed prime.
- **Banked other-xi swapped square chart:** PROVED node
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_other_xi_square_ell_exclusion`
  treats `c->1/d,d->1/b`. Four linear-by-quadratic branch pairs,
  every line-degeneration fiber, and independent resultant/subresultant
  paths have only collision or inversion-fixed support over characteristic
  zero and the deployed characteristic.
- **Banked other-xi mixed chart:** PROVED node
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_other_xi_mixed_exclusion`
  has a complete four-component-pair classification with only forbidden
  `F_(p^6)` points, fail-closed primary shards, and an independent
  fraction-free/subresultant residue-field audit.
- **Banked moving-moving a-xi square chart:** PROVED node
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_moving_moving_a_xi_square_exclusion`
  reduces the four reciprocal conditions through `s=b+1/b`, exhausts all
  nine parent-component pairs, and gives unit forbidden saturations for all
  15 nonstandard modular factors whose degrees divide six. Independent
  direct/resultant and fraction-free/subresultant certificates agree.
- **Banked moving-moving a-xi square-ell chart:** PROVED node
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_moving_moving_a_xi_square_ell_exclusion`
  exhausts its six parent-component pairs. Irreducible degrees five and nine
  cannot enter `F_(p^6)`; all four retained linear fibers have unit forbidden
  saturations in independent direct/resultant and fraction-free/subresultant
  paths.
- **Banked moving-moving a-xi mixed chart:** PROVED node
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_moving_moving_a_xi_mixed_exclusion`
  reduces to one nonstandard parent-component pair. Its complete modular
  router retains four linear, five quadratic, and one cubic factor, all with
  unit forbidden saturation; irreducible degrees 5, 7, and 29 cannot enter
  `F_(p^6)`. This completes the moving-moving `xi=a` orbit.
- **Resolution:** all 18 affine-positive charts are PROVED empty. The PROVED
  `rate_half_kb_m2_r4_diagonal_c2_112_near_negative_q_slice_exclusion`
  removes both negative templates, including forced ramification. The PROVED
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_projective_boundary_exclusion`
  treats `q_hom=Y(T-dY)` directly and closes all seven positive homogeneous
  cells by full deployed-field saturation.
- **DAG effect:** the complete near-aligned source-line branch is empty by
  the necessary q-slice gate. Its evidence is banked under
  `rate_half_band_closure`; no target status changes without the remaining
  packet/source-row assembly.
- **Retirement:** do not request or fund further near-q-slice chart
  elimination. Preserve the checkers and move compute requests to the six
  aligned positive unramified cells or to a proved assembly interface.

## Upstream handoff convention

When one of these requests is included in a PR to Przemek's repository, copy
the request as a **compute request**, not as evidence for a theorem. The PR
body should put it in a distinct **Compute requests** section and should also
include:

1. the proved router that makes the computation complete for its stated
   scope;
2. the smallest reproducible pilot and its measured cost;
3. a resumable remote launcher with an explicit cost or resource ceiling;
4. a streaming, independently runnable certificate checker;
5. the exact DAG change authorized by PASS, FAIL, and incomplete outcomes.
6. the local source commit and the upstream target commit used to prepare the
   packet, so later contributors can distinguish mathematical drift from
   implementation drift.

Large raw artifacts should remain in contributor-controlled remote storage.
The PR should vendor compact manifests, hashes, certificates, and checkers.
An incomplete run may sharpen the request or expose a counterexample, but it
must not change a mathematical node to `PROVED`.

Use the following copy-ready block in an upstream PR. Delete a field only
when the request itself proves that the field is inapplicable.

```text
### Compute requests

#### <request id>: <mathematical decision>
- Upstream interface:
- Proved completeness router:
- Exact input rows/parameters:
- Command and source commit:
- Small pilot and measured cost:
- Hard CPU/RAM/time/dollar ceiling:
- Checkpoint and partial-output contract:
- Certificate artifact and independent checker:
- PASS effect on the DAG:
- FAIL effect on the DAG:
- Incomplete effect on the DAG: evidence only; no status change
- Raw-artifact location and compact manifest hashes:
```

The request is not PR-ready if `Proved completeness router`, `Hard
CPU/RAM/time/dollar ceiling`, or `Certificate artifact and independent
checker` is blank. In that case vendor the algebraic preprocessing and link
the item as a pre-request for later contributors; do not ask them to fund an
unbounded search.

Every related upstream PR should carry its still-live pre-requests as clearly
labelled implementation/donated-compute requests, even when they are not yet
runnable. This makes the missing compiler, pilot, or coverage theorem visible
to contributors with suitable machines without presenting an unknown-cost
campaign as authorized. Retired requests must not be copied forward.

Requests are added only after algebraic preprocessing has made the search
space auditable. At present CR-001 through CR-004 are the only large runs
meeting that bar; the other open critical lanes still need theorem-level
compression before a large computation would be responsible. CR-004 is a
handoff record, not permission to duplicate work that may already be running
in the canonical worktree.

### Grande Finale v4 workboard handoff index

The current upstream target is `przchojecki/rs-mca@32a41660`. Its
`agents.md` snapshot line still names `18cfc199`, so packets must print both
the actual target commit and the workboard contract they audited. Grande
Finale v4 replaces the former six-input priority list with exact-row items
`K0`--`K5`, `M0`--`M2`, and `T`. Every contributor request should name one
of those items and the exact row impact:

| upstream v4 item | local request | handoff status |
|---|---|---|
| K2: exact pruned row-sharp Q atom | QF pre-request below; F2 no-go dossier | needs a frozen first-match residual and complete profile compiler before large compute |
| K3: MCA slope projection and residual geometry | XR pre-requests; the geometric part of CR-001 | a chart payment needs proved one-pencil coverage or an exhaustive ray/slope compiler with exact multiplicities; support counts alone do not pay slopes |
| K4: algebraic routing and add-back | CR-002 and CR-004 | bounded symbolic endpoints exist; every quotient, extension, periodic, rank, and field ledger must bind to the active first-match chronology |
| K5: exact KoalaBear row certificate | eventual final compiler; CR-003 only where its theorem transfers | exact integer atoms and independent replay are required; exponent-only evidence is inapplicable |
| M1: primitive-fiber/list-interior maximum | L1 and QF pre-requests | no proof-grade large run exists until the chronology-valid received-word residual, variable-remainder orientation, and realized image are frozen exhaustively; open PRs #1023--#1039 rule out the raw `T46`, flat-baseline, bounded-packet, and absolute-MI+MA shortcuts |
| M2/T: transferable exact theorem or route cut | F2, F3/HGE4, and completed analytic reductions | hand off only when the result specializes to a live K/M integer atom, direct benchmark, counterexample, or compiler route cut |

`K0`, `K1`, `M0`, and direct K/M decisions are architecture or theorem work,
not generic compute requests. A local campaign may support a v4 item without
being equivalent to it. In particular, CR-001's H3 collision target is
stronger and more specialized than generic max-fiber Q, while a Q or
shift-pair certificate cannot be reported as an MCA slope payment unless
the packet also includes exhaustive ownership, projection, and exact RS
incidence multiplicities. The v4 moving-root theorem likewise pays only
charts already proved to be genuine projective pencils and does not supply
the missing cover or pencil count.

The open M31 source/Pade stack through PR #1041 is a theorem and route-cut
wave, not a compute invitation. In particular, contributors should not spend
large compute on any of the following already-refuted targets:

1. proving the raw cap `T46<=259880`;
2. deriving payment from packing number at most four or a four-point root
   transversal for the forced-collision unions;
3. choosing one flat raw baseline that both survives the realized C1 source
   and obtains the current two-row aggregate-Forney control;
4. replacing the Sidon payment by absolute MI+MA merely after exact-image
   normalization; or
5. extending bounded 16-, 30-, or 46-column packet calculations without a
   global chronology-valid owner/refund; or
6. enumerating the `261,192` `c=2048` occupancy profiles again: #1040 already
   exhausts them; or
7. trying to prove a universal cap of 29 members or identify all explanations
   with one actual locator-prefix target. #1041 constructs `1,693,898`
   members in one `(1,1)` profile and a same-remainder pair with distinct
   actual locator prefixes in both orientations. The live diagnostic is now
   `M31_C2048_FIXED_SYNDROME_MULTIPREFIX_FACE_CARRIER_OWNER`.

A future donated M1 run becomes responsible only after a finite compiler
enumerates the variable-remainder orientation residual, assigns every member
to C1/Q/list-interior/extension/new in first-match order, and prints the
signed nonnegative payment tested by the run. Until then the useful
contributor task is theorem/algorithm design, not a fleet.

For provenance, the superseded v3 six inputs were row-sharp Q, exhaustive
first-match charts, Sidon/Fourier payment, a residual ray compiler, exact
extension/quotient payments, and a summed adjacent-row certificate. Use
those phrases only as a crosswalk to the current K/M/T item, not as the PR's
primary impact claim.

### Pre-request QF: row-sharp finite Q / Sidon certificate

This pre-request separates two problems that must not be conflated:

1. `f2_growing_order_myerson` is a universal growing-order max-to-mean
   theorem on Frobenius moving sectors. Its extensive finite watch has not
   found a falsifier, but no finite campaign can prove its asymptotic
   quantifier.
2. Grande Finale v4's deployed-row Q obligation is a finite, row-sharp
   prefix-fiber certificate after a witness-exhaustive first-match split.
   Its normalization is by the attained prefix image, not automatically by
   the ambient codomain.

A future contributor campaign is useful only after a finite compiler prints,
for each declared residual profile, the domain slice, attained image size
`L`, full-slice mean `Qbar=|Omega^0|/L`, residual mass `m`, exact remaining
Q-bit margin `Delta`, and the complete major/minor or algebraic first-match
ownership. It must then certify either

```text
max_s Q(s)/Qbar <= 2^Delta
```

directly, or for an explicitly declared moment order `r`,

```text
log2(Gamma_r)+log2(L) <= r Delta.
```

The active upstream real-average theorem identifies necessary full-mass
moment orders `94196`, `94991`, `641593`, and `680397` for the four adjacent
routes. The Mersenne-31 MCA ceiling-average comparison is `641594`; the
one-order difference is convention-sensitive and pinned by
`upstream_finite_q_shortcut_route_cuts`. These are route diagnostics, not an
instruction to enumerate all `r`-tuples, and after first-match pruning the
mass-aware condition must include `tau`. A responsible algorithm must use
symbolic recurrences,
certified transforms, or another compressed exact representation and publish
a measured smaller pilot before requesting official-row resources.

PASS must emit a complete per-profile max-fiber or moment certificate, an
attained-image certificate, the major-arc aggregate payment, and a deterministic
checker. FAIL must emit either an actual oversized prefix fiber or a replayable
profile showing the proposed moment/normalization route misses its finite
margin. Incomplete output is evidence only. Until the first-match compiler,
compressed algorithm, pilot, memory ceiling, storage ceiling, and dollar
ceiling exist, this remains a pre-request and no large run should be launched
or solicited as proof-grade compute.

The XR high-core lane now has an arbitrary-rank uniform-cell Maxwell/trade
reduction. The low-core rank-five lane also has a complete local ratio router
for every `u=0` loop-defect cell, including a rich-core peeling formula and
the exact line cap. In the high-core uniform cell, the minimum-union rank-two
classification is now sharper: the collapsed branch contradicts the
post-strip common-zero cap, and the regular Plucker face syzygies are already
quotiented. The first residual rank-two shell at union `a+3` is also
classified as one quadratic-pullback chart: its two-point zero fibers are
cycles of a single base-field Mobius involution. A useful compiler should
therefore target ownership and embedding counts for those involution charts.
The shell/Maxwell router further gives every higher shell an exact
zero-fiber/arity profile and primitive-deficit test. It excludes primitive
full-core rank two through exact prize shell depths
`22,428,333;19,217,048;4,478,600`. The remaining first-shell rank-three form
has a simple edge-zero graph ledger and is also primitive-impossible at every
prize row. What survives in the first shell is therefore proper local-circuit
ownership, not an unspecified full-core anomaly. A compiler must also handle
nonpositive-deficit higher shells, trade rank at least three beyond the first
shell, and the RowC residual. There is still no finite template generator for
those objects at support-embedding level, no corresponding `u>=1` nonuniform-
cell coverage theorem, and no cross-core aggregate that turns the local ratio
fibers into the required distinct-slope payment. The block-arity part of rank
two is now complete: every relation decomposes into four-block Mobius/Plucker
or five-block full Segre circuits. A future registry must enumerate only those
two coefficient classes. Within each fixed rank-two trade, the
lexicographically first three/four-column basis now gives every non-anchor a
unique fundamental-circuit owner and reconstructs the complete scaling
kernel. A future registry must still prove first Maxwell-core/trade selection,
exhaustive support embedding, and cross-core ownership.

The three-anchor coefficient branch is narrower still: every row has the
form `s_i(P+gamma_i Q)` and the complete scalar vector is
`s_i=H(gamma_i)/L'_Gamma(gamma_i)` with `deg H<t-3` and no selected-slope
root. A future compiler should enumerate realized `(X,P,Q,H)` tuples for
this branch, not raw Mobius or Segre coefficients. The four-anchor branch
retains the canonical fundamental four/five-block star and is now constrained
further by one explicit smooth anchor quadric and the exact centroid
`(-1,-1,-1,-1)`. A compiler must enforce both conditions before any support
search.

The dual-codeword support extension is now exact too. Each row is specified
by an active zero fiber `Z_i`, a forced-size inactive extension
`|T_i|=h-d-1+|Z_i|`, and one cofactor `R_i` shared by the active-union and
block numerators. A future compiler should enumerate this data and then test
the genuinely missing received-pair agreement and first-core conditions; it
must not enumerate arbitrary completed blocks independently.

One received-pair parity condition is now exact before enumeration. In the
three-anchor branch the polynomial plane pairs alternately with `(b,q)`, with
one scalar `eta`; in the four-anchor branch it is orthogonal to both received
directions. A future compiler must apply this router first and then certify
the other `h-1` block parity checks. Searching coefficient planes outside
these interaction loci is provably irrelevant.

Those other checks are now compressed exactly as well. For each fixed
support and slope, unique degree-`<a` interpolation gives an external residual
zero set `E_i`; actual inactive extensions are precisely its `tau_i`-subsets
and have count `C(|E_i|,tau_i)`. A future compiler should carry that count
and the zero-set certificate, not enumerate all parity rows or arbitrary
completed blocks. The missing step is compatibility across the rows of one
canonical star and first-core/cross-core ownership.

Compatibility across one rank-two star is now exact too. Split each extension
into active-zero reuse and outside points; the pair cap becomes
`|I_i|+|I_j|+|O_i intersect O_j|<=z_i+z_j-d-1`, with a summed multiplicity
budget. A future checker should stream only packings satisfying this ledger.
The missing algorithmic step is enumeration and counting of coefficient-
compatible support/packing records and their first-core/cross-core owners.
Accordingly there is no XR large-run request yet. A raw Maxwell-core,
block-family, minimum-face, quadratic-chart, or fixed-loop-cell search would
not certify either aggregate XR target and should not be sent to contributors
as a compute task. Promote an XR request only after an ownership theorem turns
the involution and shell parameters into a finite exhaustive chart registry
with a streaming checker and measured pilot. Any such registry must tag
proper local circuits separately from full-core records and reject the
positive-deficit full-core ranges before enumeration. At prize scale it must
not enumerate primitive rank-two records inside the printed shell band or any
primitive first-shell record: both classes are provably empty.

This progress does not yet promote XR to a numbered compute request. Although
the circuit block arity and intratrade owner are now exact, the repository has
no finite exhaustive compiler for first-core selection, evaluation-coordinate
support-family/packing enumeration, or cross-core ownership. A raw sweep over
four/five block choices would therefore still omit the proof of coverage and
should remain an upstream algorithm pre-request.

### Pre-request M31-MULTIPREFIX: `c=2048` fixed-syndrome carrier ownership

**Upstream interface:** Grande Finale v4 item `M1`, exact terminal
`M31_C2048_FIXED_SYNDROME_MULTIPREFIX_FACE_CARRIER_OWNER`. This request is
based on open PR #1041 at feature commit
`752872ce98754a05f37540cd7780a89b86818222`, mechanically stacked on #1040
head `02b1b8195a9f219a110ce255b205a3e8aed26956`; it must be re-audited against
the integrated upstream head before execution.

PR #1040 already exhausts all `261,192` feasible occupancy profiles at the
deployed Mersenne-31 `c=2048` boundary. Of these, `260,576` are bi-deep. Its
proved dichotomy is exact: either their layer has at most `7,556,704`
codewords, or one profile contains 30 codewords whose coupled Pade--Forney
kernel has two independent rows of combined degree at most
`65,262 < 67,447`. PR #1041 then proves that the 30-column branch is genuinely
populated: one `(1,1)` fixed-template source contains `1,693,898` codewords,
and its common error core sharpens the source-specific two-row degree to
`65,106`. Across its exact sufficient criterion, 124 source profiles activate
at width 29 and 18 at width 30. These are separate source words, not one
simultaneous list. Re-enumerating profiles, sampling received words, searching
arbitrary 30-subsets, or seeking a universal profile cap 29 cannot improve
this result.

The useful contributor task is to classify actual same-profile frames in the
simultaneous data `(L_(S_i),H_i)` from `Y-P_i=L_(S_i)H_i` and compile them
into a fixed, non-oracular, codeword-disjoint first-match owner. PR #1041
proves that a common codeword translation cannot identify even one deployed
same-remainder pair with a single actual locator-prefix target. The compiler
must therefore route every component to a chronology-valid paid owner, an
attained-image bound fitting the remaining budget, or an explicit primitive
route cut, while bounding the complete sum over attained prefix targets.
The conditional exact face-plus-carrier allowance remains `9,216,781`; it is
not a maximum-fiber allowance.

This is a **pre-request, not an executable run**. Before promotion, it needs:

1. a finite normal form and proved completeness router for fixed-syndrome
   multiprefix partial-fiber incidence components in `(L_S,H)` coordinates;
2. a canonical owner key enforcing first-match chronology and disjoint
   codeword accounting across profiles and carrier occurrences;
3. a streaming checker that verifies incidence, Pade--Forney row degrees,
   owner predicates, duplicate rejection, attained-target aggregation, and
   the total `9,216,781` allowance;
4. a complete small analogue with measured throughput, peak RAM, artifact
   size, and conservative CPU/time/dollar ceilings; and
5. atomic checkpoints by complete incidence-component intervals, with every
   timeout reporting unresolved intervals and never reporting `PASS`.

**PASS** emits the complete multiprefix owner/payment certificate and advances
the exact boundary component of upstream `M1`; it does not by itself pay high
interior weights, `U_Q`, `U_list-int`, `U_ext`, or high `U_new`. **FAIL**
emits a replayable incidence component that has neither a valid owner nor the
claimed attained-image bound, thereby killing or refining the route.
**Incomplete** output is evidence only. Until items 1--4 exist, this belongs
in a PR as a theorem/algorithm request and must not solicit a fleet.

### Pre-request RH-NP: arbitrary received-line rate-half kill probe

**Upstream interface:** `K3`/`T`, or a direct route cut against a proposed
rate-half adjacent row. This is not a row-sharp Q or ordinary-list request.

The proved `rate_half_arbitrary_line_syndrome_router` gives the exact finite
criterion. For a parity-check matrix `H`, let `V_E` be the span of columns in
`E`. A received syndrome pair `(s_0,s_1)` has an MCA-bad slope `gamma` at
radius `r` exactly when

```text
s_0+gamma s_1 in V_E,
not (s_0 in V_E and s_1 in V_E)
```

for some `|E|<=r`. This quantifies over all received lines modulo `C^2` and
therefore tests the flank that the historical polynomial locator-fiber
launcher misses. A complete toy census at `(q,n,k,a)=(7,6,3,4)` finds the
pair `s_0=(0,1,0), s_1=(0,0,1)` with all seven finite slopes bad, compared
with the universal tangent baseline `r+1=3`. The witness has an explicit
moving-secant form: at slope `gamma`, two distinct nonzero evaluation points
`x_gamma,y_gamma` with sum `gamma` span `(0,1,gamma)`. The official lifting
question is therefore a rational-normal-curve secant problem, not a request
to sample arbitrary words.

This pre-request is **not runnable at official scale**. The official syndrome
space has dimension `2^40`, and raw pair enumeration is meaningless. Before
soliciting compute, prove either:

1. an explicit algebraic lift of a bounded-parameter syndrome-pencil family
   to the order-`2^41` domain, with an exact formula for its bad slopes; or
2. a completeness-preserving compression that enumerates a declared
   first-match family, prints every `V_E` ownership/projection multiplicity,
   and has a measured tiny pilot plus a conservative resource ceiling.

After that theorem-level compression, a contributor run should search only
the finite parameter family and emit `(s_0,s_1)`, every claimed slope, one
support `E_gamma` per slope, and a deterministic checker of both membership
and non-mutuality. PASS is an official admissible witness exceeding the
candidate integer budget; it moves the unsafe bracket and invokes the
delta-star relocation path. FAIL excludes only the declared complete family.
Incomplete output is evidence only. The old `rh_band_witness_census_modal.py`
must not be funded as an RH-NP test: by its own contract it counts zero-sum
quotient constructions and words `X^k L_T0`, not arbitrary syndrome pairs.

### Retired request W3: unneeded safe-side non-planted envelope

**Status: CANCELED; NO LIVE CONSUMER; DO NOT RUN.**

The former request asked contributors to certify
`N_nonplant(U)<=B*-p(U)` for safe-side planted-sunflower receivers. The packet
`ww_spending_cell_fiber_layout_counterexample` shows why extending that task to
the unsafe spending cell is invalid, without a large run:

```text
q=1705*2^120+1 prime, n=8192, k=2048, B*=6,
six printed plants + one factored non-plant = at least seven list words.
```

The witness uses distinct fibers of `x -> x^256`, six distinct nonzero petal
labels, and background size one. Its Proth primality certificate, subgroup
order, layout partition, degree, agreement lower bound, and strict budget
failure are independently replayed with mutation controls.

Do not spend contributor or Modal compute extending the old W3/QA.22 sweep.
QA.22 still has different MCA currency. Literal safe-side W3 remains open,
but the clean-rate prize consumer has been repaired to use `list_unsafe` and
`list_safe` directly. A future request may be added only for a newly posed,
actually consumed theorem; any unsafe-cell extension must explicitly own this
fiber-layout family.

### Pre-request XR: nondeep tangent/support-mismatch atlas

**Scope contraction (current).** The standalone mismatch bridge is now
`PROVED` as an ownership adapter. Its original combined `16n^3` numerical
obligation is merged verbatim as P-A2; P-A1/P-B retain their generic `8+8`
allocation. The branch-width work below is therefore a P-A2 attack, not a
third campaign and not two stronger per-stratum `8n^3` demands.

The support-wise audit originally added
`xr_tangent_support_mismatch_bridge`; its count now lives in P-A2. A smooth
exact rate-`1/4` fixture shows why the clause is necessary: outside the deep
range, one globally tangent pair can have more support-wise bad slopes than
the `n-A+1` tangent slot. The fixture is a regression test, not evidence about
an official candidate.

Two algebraic preprocessing steps are now complete. Genuine recovered-line
slopes inject into at most `n-A` discrepancy coordinates. Every remaining
nonzero mismatch, after factoring the witness zeros outside the discrepancy
set, enters a punctured GRS chart with dimension `K-d`, agreement `A-d`, and
the same excess `h=A-K`. Thus a future run must operate on canonical
fixed-excess charts; it must not enumerate arbitrary received pairs.

Canonicalization and the nongeneric router are also now proved. Taking all
external zeros of the selected difference codeword gives one chart per
selected slope/codeword pair. Genericity failure on that chart is equivalent
to another joint `A`-support extending the zero core, and supports for
distinct joint explanations intersect in at most `K-1` coordinates.

The low-rank cross-chart aggregate is now analytic. Support-wise
nontriviality on each selected ray is exactly the pointwise transversality
hypothesis of the all-LineRay affine-core theorem, even when the pair has a
joint explanation on another support. Applying that theorem before charting
pays minimum selector rank at most three on every row, and rank four at RowC
rate `1/4` against the full mismatch reserve. Any future atlas/compiler must
therefore preserve minimum selector rank at least `5,4,4,4,4,4`; a donated
run over lower-rank chart unions would only recompute a proved inequality.

Recursive nongeneric descent is finite: it preserves `h=A-K`, drops ambient
length by at least `h+1`, and has official depth caps
`169,169,255,254,254,510`. This is not a compute authorization. Without a
branch-width theorem, a depth-bounded tree can still be exponentially large.

The pathwise dimension profile is also now exact. Along every chain,

```text
sum_j(K_j+h)<=N_0-(h+1),       sum_j d_j<=K_0-1,
#{j:K_j>=kappa}<=floor((N_0-h-1)/(kappa+h)).
```

A future branch-width compiler or donated implementation must consume this
area law. Charging the initial dimension independently at all `256/512`
levels is an avoidable overcount and is not an acceptable campaign design.

The terminal branch width is now analytic. Canonical explanation supports
form a constant-weight code of distance `2(h+1)`. Once a descent state has
`N<=4(h+1)`, its full live nongeneric subtree has at most
`1+104(h+1)` instances and at most `420(h+1)^2` genuine-tangent charges.
Every fixed logarithmic window above that boundary also has polynomially many
explanations. A future run must not enumerate terminal explanation supports;
it must target pre-terminal slope fibers or the generic canonical-chart union.

The whole near-terminal tree is polynomial, not only one support level. If
`N-4(h+1)<=C log_2 n` and `h+1>=2C log_2 n`, the live subtree has at most
`1+200n^(C+1)` instances and its genuine-tangent charges cost at most
`201n^(C+2)`. A contributor run must therefore place any proposed
super-polynomial nongeneric breadth outside every fixed logarithmic terminal
window. Generic-chart slopes remain separate and are not paid by this bound.

The pre-terminal pairwise support cap is not a finite compiler. A proved
Gilbert construction gives abstract support families satisfying the exact
`K-1` intersection condition and containing more than `16n^3` members at all
six roots. Do not request a larger constant-weight support census or a sharper
support-only packing table. A useful donated implementation must preserve RS
polynomial realization, actual slope fibers, or first-match ownership and
explain how that extra structure makes its input space complete.

There is no responsible large XR run yet. A raw search over pairs, supports,
or Maxwell cores would have no finite completeness boundary and could not
prove P-A2's official universal clause. A future contributor-scale P-A2
computation is valuable only after a theorem
supplies all of:

1. a finite aggregate compiler for the higher-rank union of generic
   full-external-zero charts, avoiding a sum over all zero sets and enforcing
   the minimum-selector-rank floor `5,4,4,4,4,4`;
2. a complete slope-to-joint-explanation fiber bound on nongeneric charts;
3. a per-level or amortized aggregate theorem for the pre-terminal
   pairwise-`(K-1)`-low-core family, with quotient pullbacks and duplicate
   slopes first-matched, the dimension-area law consumed, and no
   multiplicative depth charge; this theorem must use algebraic realization
   or slope ownership rather than support packing alone; and
4. a streaming checker that combines those two currencies and enforces the
   exact `16n^3` residual slot. The `n-A` tangent slot, chart
   canonicalization, nongeneric coverage, recursion depth, pathwise dimension
   area, and terminal explanation breadth are already theorems.

After those items exist, promote P-A2 to a numbered request. PASS must emit a
complete cell manifest proving its combined `16n^3` slot at every routed
official row. FAIL must emit one replayable
official pair and its witness supports. Incomplete runs may improve the atlas
but cannot change a node status. Until then this is an upstream
theorem/algorithm request, with no cost estimate and no authorized Modal or
external run.

### Pre-request XR-PB-ENERGY: narrow oriented-difference compiler

**Upstream terminology guard:** this is a Boolean additive-energy fiber, not
CAP25 v13.2's local primitive locator shift-pair degree. It may support an
inverse/energy route to P-B, but it does not pay Przemek's SPI input.

The proved `xr_lowcore_shift_pair_terminal_fiber_bound` removes every
oriented support-difference fiber of width `t>=K`: its multiplicity is at
most one because two records would share the fixed `t`-side against the
low-core cap `K-1`. This includes the entire terminal Plotkin interval on all
six rows. The only unpaid repeated-difference concentration is therefore

```text
H<=t<=K-1,       H=h+1.
```

The fixed-difference RS realization step is now exact. Full-side locator
division produces two smaller globally generic line instances with
`(N',K',A')=(N-2t,K-t,A-t)` and unchanged excess. The affine-rank bound pays
`t=K-1,K-2` per fixed difference. This is a recursive compiler, not yet a
finite aggregate compiler.

Apply `xr_lowcore_near_k_difference_packing` before generating any width.
At `t=K-c`, residuals own disjoint `c`-subsets, giving the exact aggregate
energy coefficient

```text
R_c=floor(C(N-2K+2c,c)/C(H+c-1,c)).
```

The registered `8n` threshold deletes the consecutive codimension prefixes
`2,1,1,6,5,4` on the six clean-rate rows. A future compiler must begin at
reduced dimensions `K'=3,2,2,7,6,5`, respectively, and must not shard or
solicit compute for the deleted near-`K` widths.

This is a potentially valuable contributor-scale classification, but it is
**not ready to run**. Enumerating constant-weight supports in this range is
both exponential and mathematically irrelevant: abstract support families
need not be realizable by one RS received line.

Before promotion to a numbered compute request, theorem work must still
supply:

1. a finite normal form for the reduced generic instances with `K-t>=3`,
   rather than an unbounded recursive call;
2. a canonical quotient by coordinate, slope, and first-match symmetries;
3. an aggregate first-match ledger turning per-fiber outputs into the exact P-B
   `8n^3` slope currency, rather than additive energy alone; and
4. an independent streaming checker whose partial output remains useful by
   closing named width/chamber cells.

Once these exist, the external run should shard by normalized width and
algebraic chamber, checkpoint every completed cell, and print exact
certificates rather than counts alone. PASS closes the declared complete
narrow-difference cells and updates the remaining aggregate ledger. FAIL emits a
replayable realized line, slopes, codewords, and first-match supports. Until
then there is no responsible cost estimate and no Modal authorization. This
pre-request is suitable for inclusion in a PR so contributors can help build
the compiler before offering compute.

### Pre-request HGE4: x83 norm-divisor aggregate

The `f3_hge4_norm_gate_count` frontier has strong finite evidence but is not
yet a responsible large computation. The target ranges over every official
`n=2^s`, every prime `p=1 mod n` with `p>=n^2`, and every width through
`H_max`. The banked 68-cell census covers selected small rows and widths; a
larger collection of the same kind would remain evidence and could not close
that universal quantifier.

There is now a precise theorem target for any future contributor effort. Put

```text
B_h=binom(n,h)(binom(n,h)-1)/p^(h-1).
```

The proved `f3_hge4_primitive_shift_pair_aggregate_adapter` shows that the
finite-track primitive shift-pair estimate

```text
SP_h^prim<=7000n max(1,B_h)       for every 4<=h<=H_max
```

closes NG-COUNT after summing all widths. A useful large run must therefore
test or certify this normalized quantity after the exact quotient/full-fiber
deletion; an unclassified raw support sweep is not responsive to the theorem
target.

The proved scaling-orbit router supplies the preferred exact finite currency.
Every ordered primitive shift-pair orbit has size exactly `n`, so if
`O_h^prim` is the number of canonical scaling orbits, the complete target is

```text
sum_(h=4)^H_max O_h^prim<=14n^2.                  (OAR2)
```

The per-width `7000` estimate is equivalently
`O_h^prim<=7000 max(1,B_h)`. A future generator must enumerate or certify one
canonical representative per primitive scaling orbit; paying for all `n`
translates is unnecessary and should be treated as a failed design.
If the implementation instead fixes `1` in the left support, it produces
exactly `h` representatives per primitive ordered orbit and must divide by
`h` or apply a further canonical rotation key.

The proved near-square union router removes the partition search completely.
For each anchored `2h`-subset `U`, compute its monic locator `D_U`, recover
the unique monic degree-`h` polynomial `S_U` whose square agrees with `D_U`
in all nonconstant coefficients, and retain the candidate exactly when

```text
S_U^2-D_U=d_U^2 in F_p^*
```

and `S_U+/-d_U` reconstructs a primitive pair. If `A_h^union` is the number
of retained unions containing `1`, then

```text
A_h^union/h=O_h^prim
```

exactly, including the case where `-1` swaps the two fibers. The raw anchored
space is `binom(n-1,2h-1)`, smaller than an anchored ordered-pair scan by the
factor `binom(2h-1,h-1)`. Future contributed code must use this union test or
an at-least-as-strong proved compression; it must not enumerate every
left/right partition of one union. At widths `h=4,5,6,7,8`, the removed
factors are respectively `35,126,462,1716,6435`.

The proved swap routers further split the generator. A donated implementation
must apply these rules before allocating shards:

1. create no antipodal-swap shards at even `h`, because that class is empty;
2. at odd `h`, enumerate `h`-subsets `Y` of `mu_(n/2)` (including `1` in the
   anchored convention), put `c_Y=prod(Y)`, and retain exactly those with

   ```text
   (L_Y+c_Y)/Z=T_Y^2
   ```

   and trivial scaling stabilizer in `mu_(n/2)`;
3. reconstruct the two sides as `XT_Y(X^2)+/-sqrt(c_Y)` and count each
   surviving half-order support orbit once;
4. enumerate the free-stabilizer class separately by the original near-square
   union test. The swap descent supplies no bound or candidate discount there.

For an anchored odd-width swap scan there are at most
`binom(n/2-1,h-1)` half-order support candidates. The square test is
deterministic and removes all `2^(h-1)` sign choices. This is a hard
conformance ceiling, not an estimate for the number retained. A signed
odd-moment implementation may be retained as an independent small-order
checker, but must not be used as the production sharding plan.

The equivalent divisor form is `ZT^2-c | Z^(n/2)-1`. This is a theorem-facing
classification target, not a production enumeration plan: scanning all
`p^((h-1)/2)` coefficient tuples is prohibited unless another proved router
reduces that space and a pilot supplies a dollar ceiling.

The proved straight-line lift supplies the permitted fixed-cell certificate
representation. Repeated squaring modulo `ZT^2-c` gives a cubic system with

```text
b+k(2h-1)-h variables,       k(2h-1) equations,
b=(h+1)/2,  k=log_2(n/2)-floor(log_2(h-1)).
```

At the smallest official order `n=8192`, widths `5,7,9` have respectively
`88/90`, `127/130`, and `149/153` variables/equations. Each fixed system is a
unit ideal over characteristic zero, so a checked integer Nullstellensatz
identity gives a complete finite list of possible survivor characteristics.
This does not provide a uniform bound or make elimination cheap.

#### Deferred HGE4-SL certificate pilot

This is a valuable large contributor request, not a local Modal task.

- **Purpose:** determine whether arithmetic-circuit elimination can produce a
  checked bad-characteristic certificate for the smallest official swap cell
  `(n,h)=(8192,5)`, and whether the output exposes a recurrence in
  `m=log_2(n/2)` that could support an all-row theorem.
- **Exact input:** the pruned `88`-variable, `90`-equation cubic system from
  `f3_hge4_primitive_swap_straight_line_certificate_lift`; no expanded
  remainder polynomial and no support enumeration.
- **Pilot gate:** first run modular elimination on several declared primes and
  publish elimination order, peak RAM, term counts, wall time, artifact size,
  and a conservative dollar ceiling. Unknown-cost continuation is forbidden.
- **Required output:** either a checked identity
  `Delta=sum_a H_a E_a` with `Delta!=0`, followed by certified factorization
  sufficient to classify every prime `p==1 mod 8192, p>=8192^2`, or a
  replayable obstruction showing why the representation/order is unsuitable.
- **Independent checker:** parse a sparse arithmetic-circuit identity, reduce
  it modulo multiple fresh primes, verify it exactly over the integers or by
  a certified reconstruction bound, verify every reported prime factor, and
  replay direct divisibility for every surviving characteristic.
- **Partial-output contract:** checkpoint completed elimination blocks and
  modular images atomically, report unresolved blocks, and never label a
  modular or truncated identity `PASS`.
- **DAG effect:** a factored certificate excluding all compatible primes proves
  only the `n=8192,h=5` primitive-swap cell. A parameterized identity or
  proved transfer is required before it supports the uniform HGE4 target.

Do not proceed to `h=7`, `h=9`, or larger orders merely because the generator
exists. The smallest pilot must first demonstrate a viable method and cost
envelope, and priority should go to a symbolic transfer in `m` over a list of
unrelated fixed-cell certificates.

#### Deferred HGE4-NFS non-full certificate pilot

The proved non-full near-square lift now gives a broader request that covers
both free and swap unions. It takes priority over HGE4-SL if a contributor can
fund only one elimination pilot.

- **Purpose:** test the complete non-full near-square characteristic sieve at
  the smallest official cell `(n,h)=(8192,4)` and seek a transfer in
  `s=log_2(n)` or `h`, rather than only classifying the swap subfamily.
- **Exact input:** three inverse charts, one for each nonconstant intermediate
  coefficient of the monic quartic `S`. Every chart presents
  `S^2-a^2 | X^8192-1` by `163` variables and `166` cubic-or-lower equations.
  The equivalent global selector has `165` variables and `166` equations.
- **Coverage:** the union of the three charts is exactly the non-full-fiber
  locus. Selector or inverse variables are existential witnesses and are not
  counted as trades. Paid full fibers are deliberately absent.
- **Pilot gate:** benchmark one chart over several declared modular images;
  publish elimination order, term growth, peak RAM, wall time, artifacts, and
  a conservative dollar ceiling before integer reconstruction.
- **Required output:** for every chart, a checked nonzero integer identity and
  sufficient certified factorization to classify all
  `p==1 mod 8192, p>=8192^2`, or a replayable method/cost failure. A single
  chart certificate is incomplete coverage.
- **Independent checker:** verify the straight-line identities, chart inverse
  equation, integer or certified modular reconstruction, factorization, and
  direct divisibility at every surviving characteristic. Cross-check that a
  full-fiber fixture is rejected only by the chart equation.
- **Partial-output contract:** checkpoint by chart and modular block, preserve
  incomplete identities without a `PASS` label, and enumerate every missing
  chart/image in the summary.
- **DAG effect:** complete exclusion of compatible primes closes only the
  non-full `(n,h)=(8192,4)` near-square cell. HGE4 requires a proved transfer
  or aggregate over all rows and widths; a growing list of isolated cell
  certificates is evidence, not closure.

Do not launch this locally. Its cost is unknown, and the remaining Modal
credit is reserved for sub-dollar tasks with measured value.

#### Deferred HGE4-ERT exact-ratio level campaign

The proved exact-ratio tower compiler gives a more uniform contributor target
than a list of ambient `(n,h)` scans. This is a valuable large-run request,
not authorization to spend the remaining local Modal credit.

- **Purpose:** count or bound primitive shift-pair orbits once at their exact
  dyadic ratio level and test the sufficient level budget
  `sum_h E_h^prim(m,p)<=(21/2)m^2`. The primary research output is a transfer
  in `m` or `p`; isolated fixed-field counts are falsification evidence only.
- **Exact input:** a declared official ambient order `n=2^s`, exact dyadic
  level `m=2^r|n`, and characteristic `p=1 mod n`, `p>=n^2`. Before any
  generation put

  ```text
  c_(n,m)=2 ceil(mr/(8s)).
  ```

  Reject `m<=64` before width generation. The earlier norm/complement gates
  pay the lower levels, and the proved multiscale Haar norm product pays the
  last two endpoint widths at `m=64`, even on the smallest ambient row. A
  production manifest containing an `m=64` survivor or debit is invalid.

  Generate only widths `4<=h<c_(n,m)`. The proved ambient-prime contraction,
  complement-third, dual-gap, and cyclotomic-norm gates make every larger
  width empty; generating those shards is a checker failure, not conservative
  coverage. At `m=n` the cutoff is `m/4`; every proper level is smaller.
  Across the official ambient rows this precharge deletes
  `55,050,457,488` additional level-width cells.

  Before generating any width below that closed-form cutoff, put
  `v_h=floor((h-1)/2)+2` and test the exact integer/logarithmic predicate

  ```text
  n^(2 floor(h/2))>=(4h-v_h)^(m/4).
  ```

  A passing width is empty by the coupled ambient norm, Vandermonde-defect,
  and swap-norm theorem. Apply this test separately at each parity; an even
  pass does not authorize deleting the following odd width without its own
  check. A production manifest that allocates a passing cell is invalid.

  The stronger multiscale Haar gate may delete additional widths by
  multiplying all nonzero dyadic moment norms under their single shared
  energy budget and pricing zero folds by their exact cyclotomic powers of
  two. A contributor may use that gate only with the exact cross-multiplied
  subset certificate `(MHN8)` from
  `f3_hge4_multiscale_haar_m64_level_close`; do not enumerate `2^ell` masks
  at a large level without a proved subset optimizer and a measured bounded
  implementation.
  Generate left-anchored near-square
  bases `(S,a)` satisfying `S(1)=a`, the non-full condition,
  `S^2-a^2 | X^m-1`, and `S^2-a^2` not dividing `X^(m/2)-1`. Apply the exact
  primitive stabilizer test and canonicalize scaling orbits.

  After the ambient cutoff, before allocating any remaining near-quarter
  shard, write `h=m/4-d`, put
  `R=log m`, `x=4(d+1)R/m`, and define

  ```text
  Y_3=4((d+1)R-d)-8(d+1)^2R^2/m
       +(32/3)(d+1)^3R^3/m^2.
  ```

  If

  ```text
  x<=1,       Y_3<=floor((h-1)/2)+2,
  ```

  the Vandermonde-defect and swap-norm theorems make the complete width empty.
  Allocate no shard at either parity. At `m=2^41` this deletes
  `1<=d<=2,677,220,820`. The linear Vandermonde and cyclotomic-Haar bands are
  proved sub-bands and should not be scheduled separately.

  Outside that overlap, set `s=log_2(m)`. If

  ```text
  s(d+1)<=m/2,
  ```

  allocate only the free-class generator; the complete swap class is empty.
  At `m=2^41` this free-only rule continues through
  `d=26,817,356,774`. Allocate both free and swap shards only below that
  cutoff.

  Every live width now has `e=m-3h>=h+4`. The separator, Belyi, Kummer, and
  trace packets below are historical conformance fixtures for excluded
  near-third cells only; they are not production shards. On such a fixture,
  enforce the proved separator-defect identity

  ```text
  m(P+Q-PQG)=d^2 XP'R,       deg G=e.
  ```

  The `e=1,2` boundary systems carry no free defect coefficients. If
  `P=X^h+aX^(h-1)+bX^(h-2)+...`, substitute

  ```text
  e=1: G=d^2(a-(h/m)X),
  e=2: G=d^2((b-2a^2)+((m-1)/m)aX-(h/m)X^2).
  ```

  For `e=1`, canonicalize scaling further by `P(0)=1`, set
  `x=Q(0)`, and enforce `d=x-1` and
  `a=(1+x)/(x(x-1)^2)`. Satisfying these necessary identities is not a
  split-root certificate.

  The earlier `e=1` payment is retained only as a conformance interface. Its
  normalized locator is uniquely forced by

  ```text
  U(y)=(1-3ay)^(-1/3) mod y^h,
  ```

  and the central-star necklace theorem bounds its ordered orbit count by
  `2`. The dual-gap theorem now proves that the cell is empty, so its current
  debit is zero. The one-variable endpoint equation `(LBO3)` may be replayed
  as an independent conformance screen.

  The earlier `e=2` payment is similarly a checker interface. With
  `P(0)=epsilon in {1,omega}`, `x=Q(0)/P(0)`, and

  ```text
  c_2=(1+x)/(epsilon^3x(x-1)^2),
  F_(a,c_2)(y)=(1-3ay-3c_2y^2)^(-1/3),
  ```

  its endpoint equations are `f_h=epsilon(1+x)/2` and `f_(h+1)=0`.
  The latter has degree `h+1` in `a`. More sharply, the central-star necklace
  theorem gives the uniform payment

  ```text
  E_h^prim(m,p)<=h+2=(m+4)/3.
  ```

  The dual-gap theorem supersedes this payment by proving the cell empty, so
  its current debit is also zero.

  More generally, for every `0<e<h`, apply the proved necklace prefilter

  ```text
  E_h^prim(m,p)<=2N(h+e,e),
  N(c,e)=(1/c) sum_(r|gcd(c,e)) phi(r) binom(c/r,e/r).
  ```

  Before applying a positive necklace debit, enforce the stronger dual-gap
  exclusion

  ```text
  E_h^prim(m,p)=0       when h>=2e+1,
  E_h^prim(m,p)=0       when 7h>=2m+1.
  ```

  This is a zero-cost exclusion. It removes both boundaries, the cells at
  `m=64,128,256,1024`, and the former `(4096,1364,4)` unpaid guard. Before the
  later cyclotomic-norm theorem, one printed necklace cell remained a
  positive debit:

  ```text
  (m,h,e)       orbit debit
  (32,9,5)            286.
  ```

  The cyclotomic-norm theorem also proves `(32,9,5)` empty. No contributor
  computation is needed at or above the `m/4` line. Retain the old cells only
  as checker fixtures or falsification interfaces, reject a production
  manifest that allocates support, elimination, or orbit-count shards to
  them, and charge no positive necklace debit. Level-locally this leaves the
  lower-quarter region `e>=h+4`; in an official ambient row the earlier
  ambient cutoff and exact defect/swap predicate delete a further subset of
  that region before generation.

  For historical replay on an excluded near-third fixture, enforce the
  proved Kummer midpoint-pencil router. Reconstruct the complement and the
  unique endpoint scalar

  ```text
  W=ZS+lambda y^(h+e),       kappa=1-a^2lambda,
  S | 1-kappa y^m.
  ```

  Primitivity forces the uniform Kummer factor degree to be one at every
  width: a nontrivial Frobenius multiplier would stabilize `S` and, because
  its order divides `h`, both outside members. Require a genuine
  base-field-split three-member divisor pencil. Enumerating extension-field
  midpoint branches, all binary necklaces, or all midpoint support subsets
  before this filter is prohibited: those supersets no longer describe the
  historical checker interface.

  On the same excluded fixtures, apply the endpoint trace-power gate before
  reconstructing a midpoint. For

  ```text
  u=[y^h]U,       v=[y^h]V,       x=v/u,
  tau=x+x^(-1),   kappa=-(tau+2)/8,
  ```

  require

  ```text
  x in mu_m\{+/-1},       C_m(tau)=2,
  kappa^((p-1)/m)=1.
  ```

  Deduplicate the `m-2` outside ratios under `x <-> x^(-1)`, leaving exactly
  `(m-2)/2` trace IDs before the power test. Reject a failed power test without
  constructing `S`, `W`, or a necklace. On a standalone conformance fixture,
  a passing trace is only a candidate: reconstruct every complete pencil
  above it, and do not charge one orbit per trace.
  Every passing `x` must also be a square. When `(p-1)/m` is odd, restrict
  first to `x in mu_(m/2)`, leaving `m/4-1` trace IDs; at proper dyadic levels
  `(p-1)/m` is even and this preliminary square filter is automatic.

  The scalar trace stage has an exact polynomial compiler. Define

  ```text
  C_m(X)-2=(X^2-4)Q_m(X)^2,       q=(p-1)/m,
  M=m if q is even, else M=m/2,
  G_(m,p)=gcd(Q_M(X), (-(X+2)/8)^q-1).
  ```

  Compute the power by repeated squaring modulo `Q_M`; never materialize its
  degree-`q` representative. The trace count is exactly `deg G_(m,p)`, and
  complete factorization of the split squarefree gcd gives the stable scalar
  trace IDs. Emit `Q_M`, the reduced power residue, the monic gcd, its linear
  factors, and an independent substitution check. This stage has degree at
  most `m/2-1` and is not a large-run request. Nonconstant controls at
  `(m,p)=(8,137),(16,593),(32,1249)` forbid treating gcd one as a theorem.
  A passing trace remains a useful nonconverse control, but no
  trace-to-pencil continuation is required by HGE4 because the entire width
  is deleted by the cyclotomic-norm theorem.
- **Counted currency:** report `C_h^prim`, verify divisibility by `h`, set
  `E_h^prim=C_h^prim/h`, and report both each ratio `E_h^prim/m^2` and the
  complete retained-width sum. The final level ledger charges no near-third
  necklace debit and compares only the ambient- and exact-gate-retained total
  with `(21/2)m^2`.
  Selector or inverse witnesses are existential and must not be counted.
- **Pilot gate:** complete one modest level end to end, publish candidate and
  survivor counts, throughput, peak RAM, artifact bytes, wall time, and a
  conservative dollar ceiling. Do not launch a larger level while cost is
  unknown or projected above the contributor's declared budget.
- **Required output:** canonical representatives for every retained orbit,
  per-width exact counts, the complete level sum, and either a checked
  inequality certificate or a replayable over-budget witness set. A symbolic
  or certificate-based route must also publish its exact identities and all
  exceptional characteristics.
- **Independent checker:** reconstruct both locator factors; check disjoint
  roots in `mu_m`, all top-shift coefficients, left anchoring, non-fullness,
  exactness via failure at `m/2`, trivial common stabilizer, and canonical
  orbit uniqueness. Reconstruct `A,B,G`, verify its exact degree, leading
  coefficient, boundary trace coefficients, zero-value scalar gate, and
  differential identity. Reject every production width with `h>=c_(n,m)`,
  every lower width passing the exact ambient defect/swap predicate, and
  every record in the completely empty cyclotomic-Haar band. In the remainder
  of the swap-norm band, reject every swap-class record and require a
  free-stabilizer certificate. Recount `h` anchored presentations on small
  fixtures. On excluded
  near-third checker fixtures, also reconstruct `W`, verify that `W-ZS` has
  only its degree-`h+e` endpoint, check `kappa!=0` and
  `S | 1-kappa y^m`, independently recompute
  `kappa=-(u+v)^2/(8uv)`, reconstruct `Q_M`, verify the modular-power
  remainder and monic gcd certificate, replay every linear trace factor, then
  factor the twisted binomial and verify that every
  midpoint factor has degree one. If a nontrivial common degree is reported,
  reconstruct its Frobenius multiplier and reject the record as nonprimitive.
- **Analytic-payment checker:** replay the dual-gap coefficient identity and
  recurrence before `(LBO3)`, the quadratic endpoint equations, or the
  Burnside necklace formula. Reject any production manifest containing a
  width removed by the ambient cutoff, exact defect/swap predicate, or local
  quarter theorem. Replay the historical necklace value `286` for `(32,9,5)` as a
  checker fixture, then verify that the quarter-width theorem supersedes it
  by zero-cost emptiness; no positive near-third debit may be charged. Replay
  the midpoint-pencil congruence as a candidate filter only.
- **Partial-output contract:** checkpoint completed `(m,h)` orbit shards
  atomically; preserve canonical representatives and running sums; list every
  unresolved width/rank interval; never label a partial level `PASS`.
- **DAG effect:** a proof of the `21m^2/2` estimate for every dyadic level and
  compatible characteristic closes the orbit route to
  `f3_hge4_norm_gate_count`. One violating level falsifies this sufficient
  route but not HGE4 itself. Finite surviving levels provide calibrated
  evidence and reusable checker artifacts, not node closure.

The level campaign now takes priority over unrelated larger ambient-row
sweeps because exact-ratio routing prevents inherited lower-level orbits from
being recounted. The HGE4-NFS pilot remains useful for developing symbolic
bad-characteristic certificates at the smallest official cell.

The per-width `7000` route is now the integer check

```text
A_h^union<=7000h max(1,B_h).
```

A future contributor-scale run would be valuable only after a proved
compression supplies one of these complete finite input spaces:

1. a width-uniform orbit/component classification of the non-full-fiber x83
   support variety, including the exact F-4-minimal record multiplicity; or
2. a norm-divisor aggregate that reduces all relevant supports to a finite
   list of nonzero cleared norms whose prime divisors exhaust the official
   norm-gate events; or
3. a proved width cap together with complete per-width certificate generators
   whose summed output is exactly `RAW-NG` or `NG-COUNT`; or
4. a complete primitive near-square union generator that covers every retained
   width, applies the exact quotient deletion and free/swap stabilizer
   convention, and computes either the anchored `(NSU4)` aggregate or the
   equivalent `(OAR2)` orbit aggregate.

Once such a router exists, promote this item to a numbered request and vendor
the generator, shard manifest, independent norm/certificate checker, and a
small measured pilot. For route 4, PASS must certify `(NSU4)`/`(OAR2)` on the
complete routed scope and report every per-width anchored-union count,
free/swap orbit count, and normalized ratio. FAIL must emit a complete
replayable aggregate or cell certificate above its claimed allowance,
together with canonical near-square union representatives. For the
other aggregate routes, PASS must certify `<=14n^3` and FAIL must emit a
replayable over-budget slice with its F-4-minimal record certificates. Partial
runs must preserve completed union-orbit shards and report the unresolved
canonical rank intervals. Until then, official-row support sweeps, random prime scans,
and additional fixed-`h` shells should not be solicited from contributors as
large runs.

#### Deferred contributor campaign contract

This is the handoff record for a future run that is valuable but too large or
insufficiently priced for the local Modal balance.

- **Purpose:** decide `(NSU4)`/`(OAR2)` on a theorem-certified complete scope,
  while measuring the free and swap classes separately.
- **Inputs:** the exact row `(n,p)`, a proved complete retained-width set, the
  quotient/full-fiber deletion predicate, canonical union-rank shard
  intervals, and the commit hashes of generator and checker.
- **Execution gate:** first publish a small pilot with candidate throughput,
  peak RAM, artifact bytes, wall time, and a conservative dollar ceiling.
  Unknown-cost or fixed-width evidence sweeps do not pass this gate.
- **Independent checker:** reconstruct `D_U`, `S_U`, and `d_U`; verify the
  split supports, top-shift identity, primitivity, union stabilizer, canonical
  scaling key, and free/swap multiplicity. For swap records it must also
  verify both the half-order square identity and the odd power sums directly.
- **Partial-output contract:** checkpoint completed canonical rank intervals
  atomically; emit per-width free/swap counts, running normalized sums, and
  every retained representative. A timeout must label unresolved intervals
  explicitly and must never print `PASS`.
- **DAG effect:** a complete theorem-parametric certificate proving the bound
  can support `f3_hge4_norm_gate_count`; a complete counterexample above the
  allowance falsifies the relevant route. Any finite collection of rows is
  evidence only and does not change the target status.

Until the complete-scope router and priced pilot exist, this remains a
request for contributor implementation and costing, not authorization to
spend local Modal credit.

### Pre-request L1: bounded-mark split-pencil stability

The current L1 frontier is also not yet a responsible large computation.
Node `l1_bounded_polarity_marked_full_pencil_reduction` canonically reduces
every bounded-polarity, growing-cofactor word to

```text
L_(T_i)C_i-L_(T_j)C_j=(c_j-c_i)FJ,
deg J<=P,       deg C_i,deg C_j<=c+P,
```

with fixed-degree mark factor `J` but unbounded cofactor degree `c=d-ell`.
Enumerating small `c`, random fields, or bounded mark placements would not
cover the required uniform stability theorem. Such experiments may falsify a
proposed lemma, but their survival has no direct critical-DAG consequence.

The arbitrary-locator subbranch now has a sharper proved compiler. For one
source chart and defect degree, deleting `v<=P` dense-petal equations creates
at most `q^v` affine syndromes; each is a translate of the full-petal kernel
and homogenizes by exactly one projective direction. Every actual cell also
has the bounded-basepoint split-pencil form

```text
L_(T_i)C_i=J(W-c_iF),       gcd(JF,JW)=J.
```

Thus a raw arbitrary-locator sweep is no longer a useful contributor task.
A future run must classify exact split/saturated monic points in the complete
finite family of one-direction affine extensions and must retain a canonical
internal rechart key inside the fixed first source. The support-pattern and
syndrome enumeration is already polynomial for fixed `P`; recomputing it
cannot change the DAG.

Cross-determinant uniqueness removes the wide part of those affine cells as
well. Every support/syndrome cell with `t ell>2d+p` is a singleton, so a
future classifier may only enumerate cells in

```text
ceil((d-p+1)/ell)<=t<=floor((2d+p)/ell).
```

In strip `d=m ell+eta`, do not request the already-paid region
`t>=2m+1, 2eta+p<ell`. Any proposed generator must enforce this width window
before its pilot is costed.

The fixed-support fiber theorem removes every bounded-cross-slack layer from
that window. With

```text
r_cross=2d+v-t ell,
```

all exact saturated pairs for one support pattern, across all
missing-equation syndromes, inject into at most
`q^max(0,r_cross+1)` quotient polynomials. Thus every fixed
`(p,r_cross)` box is polynomial per source chart. A future contributor run
must not sweep `r_cross<=E` for any fixed `E`; it must start from a proved
finite compression or stabilization theorem for unbounded cross slack, or
from a finite aggregate owner for the internal contributor-dependent
recharts.

The whole-support Johnson payment removes most growing-slack cells as well.
For `N=k-1` and `e=max(0,2d+1-h)`, every exact support cell with

```text
N(e-1)<d^2
```

has a field-independent `O(n^2)` bound. A future contributor run must enforce
the complementary sub-Johnson condition `N(e-1)>=d^2` before generating any
cell. With background gap `g=ell-b`, every survivor also obeys
`d^2<=N(d-g)`. Positive-denominator support sweeps now reproduce a theorem
and are not a compute request.

Bounded retained-core size is redundant too. For `a=N-d`, every fixed
`(p,a)` box is polynomial per source chart, so a future generator must cover
`a` escaping every fixed bound and enforce

```text
a(N-a)>=Ng.
```

It must also replay the exact `F_23` nonsplit-quotient fixture in
`l1_cross_quotient_split_descent_obstruction`. A generator that recursively
treats every cross quotient as a split smaller defect locator is unsound: the
fixture's quotient has only its forced background root and an irreducible
quadratic cofactor. A split-descent proposal needs a proved coverage router
for the nonsplit complement before it can become a numbered request.

The nonsplit complement still has a direct codeword-difference payment. For
one fixed support `X`, the map `(P-P_0)/L_X` has degree at most `(k-1)-h` and
is injective. Therefore every fixed support-codimension layer is polynomial
per source chart. A future generator must enforce

```text
(k-1)-h=a-(h-d)
```

escaping every fixed cap. Enumerating bounded codimension, even with
nonsplit cross quotients, is not a contributor task.

Background overlap removes a further open-ended region. In the variables

```text
N=k-1,       a=N-d,       s=h-d,       c=N-h=a-s,
```

every fixed support/defect cell with `a+s<ell+(ell-b)` is a singleton. A
future generator must enforce the complementary balanced strip

```text
a^2/N<=c<=2a-ell-(ell-b).
```

The exact `F_17` equality fixture in
`l1_background_overlap_singleton_payment` is a mandatory strictness test.
Searching below this strip only reproduces the background-overlap theorem.

The derived-background Johnson payment removes another part of the balanced
strip. After subtracting the interpolant on the fixed petal support and
dividing by its locator, compatible words become degree-at-most-`c`
polynomials on the `b=ell-g` background with at least
`u=ell-a+c` agreements. Every cell with `u^2>bc` is already polynomial.
A future generator must therefore enforce both nonpositive conditions

```text
a^2/N<=c<=2a-ell-(ell-b),
(ell-a+c)^2<=(ell-(ell-b))c.
```

The sharp `F_7` positive fixture `(b,u,c)=(3,2,1)` and the exact `F_17`
zero-denominator fixture `(1,1,1)` in
`l1_background_quotient_johnson_bound` are mandatory regression tests.
Sweeping positive background-Johnson cells only reproduces a proved bound.

The core and background tests must finally be coupled. Common defect roots
and common background agreements divide the same cross determinant, so the
joint Johnson payment removes every cell with

```text
b a^2+N(ell-a+c)^2>Nbc,       b>0.
```

A future L1 generator must enforce the reverse inequality as well as
`c<=2a-ell-(ell-b)`. The exact `F_17` cell is paid sharply by the joint
bound and is no longer a live search target. The exact `F_23` nonsplit cell
is the mandatory zero-joint-denominator fixture. Any donated run that treats
the core and background Johnson tails as independent will generate a large
proved region and should not be launched.

The joint tail also imposes an official source-scale gate. For bounded petal
polarity, a future generator must enforce

```text
N+b>=4ell,       N>=3ell+1,       M>=3(r-1).
```

Consequently no bounded-polarity L1 task should generate source charts below
`M=3,9,21,45` at rates `1/2,1/4,1/8,1/16`. Growing-polarity work is outside
this exclusion. The arithmetic threshold family
`ell=2r,b=2r-1,k=6r+2,M=3(r-1)` should be replayed to check source-equation
bookkeeping, but it is not an existence target and does not justify a large
run.

The Plotkin-boundary payment strengthens the source gate to a strict one.
Every bounded-polarity compute proposal must enforce

```text
N+b>4ell,
r b>(4(r-1)-M)ell+r,
(M-3(r-1)+1)ell>r(g+1).
```

At the first scale `M=3(r-1)`, this means `ell>r(g+1)`. Equality layouts,
including `ell=2r,b=2r-1,k=6r+2`, are analytically paid by a `2(N+b)`
constant-weight-code bound. Generating them is redundant. The six
two-subsets of a four-point universe are the mandatory combinatorial
boundary control for any independent implementation.

Bounded positive Plotkin excess is redundant as well. Put

```text
E_P=N+b-4ell.
```

For `0<=E_P<=E_0`, same-pattern puncturing gives at most
`2^(E_0+1)n` contributors per exact support cell. A donated bounded-polarity
run must therefore target `E_P` escaping every fixed cap, or equivalently

```text
(M-3(r-1)+1)ell-r(g+1) -> infinity.
```

The `F_23` nonsplit chart is an excess-one regression fixture and split-route
fence, not a multiplicity target. A five-coordinate, weight-two code with
ten members and puncture classes `(6,4)` is the independent combinatorial
control. Do not spend compute enumerating fixed excess layers.

Exact background surplus must be applied before any remaining run. If the
actual background count is `u+z`, define

```text
E_z=N+b-4(ell+z)=E_P-4z.
```

Every fixed logarithmic window `E_z<=C log_2 n` is polynomial after
exact-count stratification. A donated bounded-polarity computation must
therefore enforce `E_z/log_2 n` escaping every fixed cap. It must derive the
background set from the numerator and must not enumerate it independently.
The synthetic `z=1,E_z=0` four-pair code and exact `F_23` `z=0,E_z=1` chart
are mandatory controls. Runs with large background surplus but only
logarithmic effective excess are redundant.

The proved `l1_marked_constant_shift_subtwoell_exclusion` already removes
the three-dense common-pencil subbranch when `d+v<2ell`. A future computation
must therefore target one of the genuinely live cells: two dense petals,
arbitrary locator triples, or `d+v>=2ell`. Recomputing the excluded strict
strip is not a contributor request.

The multistrip extension further removes every strip-`m` common-pencil cell
with at least `2m+1` selected dense petals and `d+v<(m+1)ell`. A future L1
compute proposal must name a surviving low-petal, arbitrary-locator, or
boundary cell; a generic marked-pencil sweep is now even less informative.
Away from the boundary, the low-petal cell is pinned further to
`ceil((d-p+1)/ell)<=T_dense<=2m` and should be indexed by that exact window.

The extremal cell `T_dense=2m` is now compressed to a two-generator
degree-`m` polynomial matrix with determinant the complete label locator.
This is still not a numbered compute request: a contributor must first prove
a finite classification of those determinant matrices or an explicit map to
an already budgeted profile owner. Raw enumeration of matrix coefficients or
the sharp family parameter `lambda` would not count the endpoint aggregate.

The all-window Forney theorem now gives the finite symbolic index
`(t,mu,nu)` and exact generator count `2m-t+2` for every common-pencil
survivor. This is still preprocessing, not an executable large run: before
promotion, a contributor must prove either a finite component classification
of the evaluated multiplier gcd/splitting constraints or an injective charge
to an existing natural-scale owner. Sweeping generic coefficient generators
would sample a populated ambient family without deciding its first-match
multiplicity.

CRT now removes coefficient-generator multiplicity over a fixed defect
locator: the numerator is unique off the lower endpoint and has at most
`q^(2p)` choices at it. A future compute proposal must therefore classify
squarefree core locators in the Forney strata and their first-match chart
multiplicity. Enumerating numerator coefficients is explicitly out of scope.

On a genuine quotient/coset chart, the quotient-boundary router removes a
second unsuitable search dimension. Every defect locator is uniquely a
partial-fiber boundary times a full-fiber quotient locator; bounded boundary
costs only a polynomial factor. A future computation must not enumerate raw
defect subsets. It must instead classify either the source-coupled
full-fiber quotient-core census after first match, or a finite normal form for
the unbounded partial-fiber-boundary branch. A sweep with a fixed small
boundary can only reproduce the proved router and is not a contributor
request.

The L1 cutoff closes even the ambient full-fiber quotient-core count in every
fixed boundary box: one source chart has only `O(log n)` complete fibers, so
all quotient-core subsets cost `2^O(log n)=poly(n)`. A future compute request
must therefore target a theorem-compressed unbounded partial-fiber boundary
or aggregate first-match overlap across contributor-dependent quotient
recharts inside the fixed first source. The thin next-strip region now has its
own `q^p` CRT theorem, so it is also excluded from future raw sweeps.
Fixed-boundary quotient-core enumeration is mathematically redundant.

The symmetric core-polarity closure removes another misleading experiment:
large one-sided boundary caused by almost-full fibers is already polynomial
when the number of holes is bounded. Any future L1 computation must target
growing symmetric core polarity, not merely growing `beta`. It still needs a
finite normal form or stabilization theorem and an internal-rechart ownership
contract before becoming a numbered request.

The finite normal form is now known algebraically but not yet finite in the
growing parameter: `F_D L_H=L_S product(P-a)` with
`deg L_H+deg L_S=p_core`. A future contributor request must operate on this
signed quotient-mark system and certify a degree-independent component
classification, stabilization threshold, or explicit natural-scale owner.
Enumerating defect subsets, full-fiber choices, or bounded signed marks is
out of scope; none can decide the remaining uniform theorem.

All maximal source-chart enumeration is now redundant. The general
first-layout theorem fixes one admissible source and absorbs every later
source-layout contribution into at most `M` anchors; the older intrinsic
`3^(n/ell)` census remains a valid special-case check but is no longer the
composition mechanism. A future compute request may address only internal
contributor-dependent rechart multiplicity after a finite model is proved.
The quotient-polynomial axis is also retired in the whole-petal anchored
scope: `l1_fixed_source_quotient_partition_anchor_census` gives at most `M`
partitions and `M 3^(n/ell)` complete-fiber role keys in the fixed source.
Raw generation of source layouts, quotient-polynomial additive shifts, or
anchored fiber-role assignments cannot affect the DAG.

This retirement is conditional on the whole-petal anchor being part of the
generated cell. Dense intersection with a source petal does not supply it.
A future finite generator must therefore either certify the anchor or emit
the smaller-fiber/refinement branch explicitly; silently treating dense
supports as complete fibers would make the census unsound.

Within the certified anchored branch, fixed-cap Forney enumeration is now
also redundant. `l1_fixed_source_anchored_triple_polarity_closure` pays every
partial-core source chart, support, defect locator, and numerator in a fixed
layout/core-defect/petal-polarity box. No donated run should scan Forney
coefficients, partial cores, or bounded exception sets in that box. A useful
future generator must instead expose one of three unresolved outputs:

1. an unanchored or smaller-fiber quotient representation together with its
   canonical refinement owner;
2. a growing signed layout/core-defect/petal-polarity profile; or
3. an arbitrary-petal-locator cell outside every common constant-shift pencil.

Until a finite complete generator for one of these outputs is proved, a large
run is a contributor request only and cannot alter the critical DAG.

Bounded partial-core charts are now redundant compute targets as well. The
triple-polarity closure counts them globally using layout polarity,
core-defect polarity, and petal polarity. A future intrinsic-chart request
must target a theorem-compressed growing-polarity regime and emit a signed or
natural-scale classification; sampling cores with fixed exception counts
cannot advance the frontier. Anchored non-intrinsic partial-core scans are now
redundant for the same reason. Only an unanchored/refinement, growing-polarity,
or arbitrary-locator finite generator can be promoted to this ledger.

Promote this to a numbered compute request only after either item 1 or item 2
is proved:

1. a degree-independent component/normal-form theorem reducing the
   sub-Johnson, unbounded-cross-slack affine one-direction cells and all `c`
   to a finite symbolic classification for each fixed `P`; or
2. an explicit stabilization bound `c_0(P)` together with a complete theorem
   covering `c>c_0(P)`, plus a finite generator for the residual cells.

First-match coverage itself is now closed by the proved
`l1_first_match_totality_scope_pin`: least carrying-chart ownership partitions
the distinct image contributors exactly. Maximal source-layout composition is
separately closed by `l1_general_first_layout_domination`. Any global request
still needs a finite canonical generator for the residual anchor/refinement,
growing-polarity, or arbitrary-locator owner cells in scope, because that
generator must make their complete payment sum executable and auditable.
Totality does not bound the number of those keys or their budgets.

The resulting request must classify the complete finite residual, retain the
fixed first source, internal anchor/refinement or growing-polarity key,
missing-equation syndrome, homogenizing direction, and the
coprimality conditions `gcd(F,J)=gcd(F,A_i)=gcd(F,A_j)=1`, and emit a
counterexample witness or a checkable component certificate. Until that gate
is met, an upstream PR should present the affine split-pencil compiler as a
theorem frontier and invite the missing uniform argument, not request a large
sweep.

#### Parked contributor campaign L1-NIC: internal non-intrinsic owner-cell payment

- **status:** PARKED; NOT EXECUTABLE AND NOT AUTHORIZED. This records a
  potentially valuable large run for contributors with compute, as requested;
  it is not a request to spend the current Modal balance.
- **raw-ledger route fence:**
  `l1_raw_support_ledger_exponential_route_fence` proves that merely summing
  the root-pinning or maximal background-anchor allowances is exponentially
  loose on a balanced formal profile. Unlimited compute does not repair that
  proof route. The campaign must reject any generator that only evaluates
  those numerical expressions.
- **decision target:** after one of the two theorem gates above is proved,
  fix the first maximal source layout using
  `l1_general_first_layout_domination`, classify the complete finite residual
  of its anchor/refinement, growing-polarity, or arbitrary-locator owner
  cells, and decide whether their total valid payment is polynomial at the L1
  cutoff.
- **required generator:** emit each canonical owner key exactly once and retain
  its source chart, defect degree, strip, signed petal/core marks, missing-
  equation syndrome, homogenizing direction, quotient boundary, and exact
  coprimality/squarefreeness/saturation guards. It must prove completeness
  against the theorem-certified residual range.
- **mandatory analytic precharge:** apply
  `l1_maximal_background_anchor_injection` to every exact support cell. Record
  `r`, `a_*`, and `q^max(0,d-max(r,a_*)+1)` and remove every complete
  `(t,u,r,E)` stratum paid by its printed ledger. Do not enumerate `(F,W)`
  coefficient pairs merely to rediscover this bound.
- **mandatory refinement normalization:** apply
  `l1_tame_fixed_petal_refinement_census`. For every `s|ell` with
  `char(F)` not dividing `ell/s`, retain one normalized map per fixed petal
  and shard only its unpaid role/support cells. Emit wild divisors under a
  separate flag. Enumerating tame quotient coefficients or additive shifts is
  forbidden because the proved census already removes that axis.
- **identity-endpoint exclusion:** apply
  `l1_identity_pullback_role_payment_fence`. At `s=1`, the pullback quotient
  list is exactly the original L1 list, with singleton fibers and
  `kappa=z=0`. A contributor campaign must either (a) restrict its executable
  residual to `s>=2` and state that it cannot close L1, or (b) name a separately
  proved global exact-shell/Toeplitz theorem that pays `s=1`. No large run may
  enumerate identity-map role vectors or present their classification as a
  reduction; that is a computational restatement of the target.
- **owner guard:** do not label a tame refinement exact-periodic merely because
  one source petal is a union of complete polynomial fibers. The exact
  `F_17^*` obstruction has trivial stabilizer on the complete agreement
  support. Each emitted small-scale cell must either certify nontrivial support
  stabilizer, carry a separate general-pullback owner, or remain in the
  aperiodic collective-payment residual.
- **general-pullback precharge:** for each retained monic degree-`s` map,
  apply `l1_general_pullback_interleaving_descent`. Emit the complete label
  set `B`, all `k_j`, and `kappa=sum_j max(0,k_j-|B|)`. Replace fully
  fiberwise role enumeration by the quotient ordinary-list target after the
  proved interleaving collapse. Shards with `kappa=0` must not enumerate role
  vectors; shards with `kappa>0` must charge `q^kappa` explicitly. Partial
  fibers remain separate residual data.
- **Johnson deletion:** on full domain partitions, delete every tame shard in
  `l1_full_pullback_divisibility_johnson_closure`: all `s>k`, and every
  `s<=k` satisfying `(k+ell)^2>(k-s)n`. The exact source shell is empty in
  those fully fiberwise classes and the total paid mass is at most `n^3`.
  Emit only the nonpositive gate, partial fibers, sparse coverage, wild maps,
  or unanchored owners.
- **full-partition retirement:**
  `l1_full_domain_pullback_intrinsic_rigidity` supersedes even the nonpositive
  full-partition gate. If all domain fibers are complete, certify
  `P=X^s+c` and route every fully fiberwise support to the exact-periodic
  owner. No donated computation may enumerate a non-intrinsic full-partition
  class. Retain only incomplete domain coverage, partial agreement fibers, or
  missing whole-petal anchors.
- **partial-pullback deletion:** compute `z`, `b`, the component dimensions,
  and `kappa` exactly, then apply `l1_partial_pullback_johnson_router`. Delete
  every fixed-`kappa` tame anchored cell with
  `ceil((k+ell-1-Z)/s)^2>b(ceil(k/s)-1)`; its cost is already bounded by
  `q^kappa b^2` per map. A retained shard must print the nonpositive gate,
  unbounded kernel, wild divisor, or failed whole-petal anchor.
- **kernel/loss merge:** replace the raw kernel calculation by the exact
  identity `kappa=max(0,k-sb)` and verify
  `kappa<=max(0,z-ell+1)`. A cap `Z<=ell-1+K` automatically gives
  `kappa<=K`; do not emit a separate sparse-kernel shard. Any unbounded kernel
  belongs to the growing partial-loss-excess output.
- **required added predicate:** every emitted cell must carry either a proved
  algebraic feasibility test stronger than the elementary list arithmetic or
  a certificate placing it in a collective cross-pattern injection. Formal
  support patterns with no such certificate are not valid compute shards.
- **sharding:** shard only by canonical owner-key rank intervals after all
  analytic deletions in this pre-request. Fixed-parameter boxes and raw support
  subsets are forbidden shards because they reproduce proved regions. Source
  layouts are also forbidden shards: the general first-layout theorem reduces
  them to one fixed source plus at most `M` anchors.
- **independent checker:** reconstruct every split-pencil identity and owner
  key; verify least-owner assignment, no duplicate image codeword across
  shards, every strict boundary convention, the B3/B4 anchor exponent and
  stratum deletion, and the exact aggregate sum of owner-cell budgets.
- **partial output:** atomically checkpoint completed key intervals, exact
  per-stratum totals, maximum cell size, and all over-budget witnesses. A
  timeout must list unresolved intervals and may not print `PASS`.
- **pilot/cost gate:** publish throughput, peak RAM, artifact size, wall time,
  and a conservative dollar ceiling on a complete theorem-certified pilot.
  No fleet may launch while total cost is unknown.
- **DAG effect:** a complete polynomial aggregate certificate supports
  `l1_mixed_petal_amplification`; a replayable super-polynomial family or
  route-kill lower bound refutes it. Any incomplete finite-row sample is
  evidence only.

#### Parked contributor request L1-WRR: wild refinement realizability

- **status:** PARKED; NOT EXECUTABLE AND NOT AUTHORIZED. This is a large-
  compute handoff for contributors after a finite decomposition generator and
  a costed pilot exist. It must not consume the current Modal balance.
- **decision target:** on admissible descriptors and L1 source sizes, decide
  whether a multiplicative-domain source petal can have two inequivalent
  monic degree-`s` right components when `s|ell` and
  `char(F)|ell/s`. The proved `F_9` decomposition of `X^9-X` shows that raw
  polynomial uniqueness is false, but does not realize a source petal inside
  the smooth multiplicative domain.
- **analytic prefilter:** enumerate only wild divisor triples `(p,ell,s)`
  compatible with the exact row descriptor, `ell=sigma+1`, and the source
  inequalities. Reject tame triples with
  `l1_tame_fixed_petal_refinement_census`; reject maps whose fibers are not
  complete, whose outer labels repeat, or whose petal is not contained in the
  row domain. Do not enumerate arbitrary subsets of `H`.
- **required positive certificate:** print the exact row and source contract,
  one petal locator `L_T`, two normalized monic maps `P!=P'`, split squarefree
  outer factors `F,F'`, and verify `L_T=F(P)=F'(P')`; list every fiber and
  label, prove `T subset H`, and prove the maps are not additive shifts.
- **required negative certificate:** provide a complete decomposition theorem
  or exhaustive component transcript for every surviving wild descriptor,
  with independent checks of factorization, subgroup containment, source
  admissibility, and affine-equivalence classes. A solver's bare `UNSAT` or a
  random search is insufficient.
- **execution shape:** shard by exact `(p,e,s_row,rho,ell,s)` after analytic
  pruning; checkpoint completed decomposition classes and compact hashes;
  publish peak RAM, wall time, artifact size, and a conservative total dollar
  ceiling from the smallest nontrivial pilot before launching a fleet.
- **DAG effect:** a complete negative classification retires the wild
  fixed-petal map-supply axis. A positive certificate blocks that retirement
  and identifies the wild owner class that the local payment must price. It
  does not by itself refute `l1_mixed_petal_amplification`.

#### Parked contributor request L1-N10-128: next balanced-chart growth point [DROPPED
2026-08-07, round-21/22: the census's enumeration domain has an exact
degree-6 closed form and the falsifier was structurally unfireable at
`ell=2`; superseded by `L1-N10-ELL` below.]

- **status:** PARKED; EXECUTABLE BUT NOT AUTHORIZED ON THE CURRENT CREDIT.
  The bounded N10 campaign is complete through `n=64`; its exact transcript
  is `experiments/prize_resolution/l1_balanced_mixed_growth_census_result.md`.
- **decision target:** run the same complete-agreement-set census at
  `(n,k,p)=(128,64,257)` for the consecutive and powers-of-five scalar
  schedules. Report whether the second-step factor near `38` persists or a
  faster escape begins. This is evidence about these chart families only and
  cannot promote L1.
- **exact input size:** `1,821,304,128` floor-pruned mixed candidates per
  schedule. Candidate ownership is the deterministic global rank modulo the
  shard count. Every shard must report its processed interval/rank class,
  exact-support count, agreement histogram, core-count histogram, and wall
  time.
- **required regression:** reproduce the saved `n=16,32,64` totals, including
  `109391` and `108600`, with an independently compiled binary or a second
  exact implementation before accepting the `n=128` aggregate.
- **partial-output rule:** a timeout is `INCOMPLETE`; preserve completed
  shard totals and rerun only named missing ranks. The first `n=64` run and
  its three-shard retry are the conformance example.
- **measured cost:** the two `n=64` modes used about `998` aggregate worker
  seconds. Scaling the current quadratic-interpolation implementation gives
  about `37` CPU-hours per `n=128` schedule, `74` CPU-hours total, and about
  `$4.1` at Modal function rates published 2026-07-21, before overhead. A
  contributor should first replace repeated interpolation by the separated
  base-petal barycentric update or publish a hard budget accepting this cost.
- **DAG effect:** a sharp upward escape strengthens the registered L1
  falsifier and redirects effort from flatness to repair; another falling
  ratio supports the polynomial-growth heuristic. Neither outcome changes
  node status without a uniform algebraic theorem.

#### Parked contributor campaign L1-ESQ: exact-shell row-sharp prefix flatness

- **status:** PARKED; NOT EXECUTABLE AND NOT AUTHORIZED. This is a donated-
  compute request for contributors with an independently approved budget. It
  must not consume the remaining Modal credit.
- **roadmap track:** Track C, L1 standing lane. Any separate small growth-law
  pilot belongs to Track N10 and must satisfy the current sub-dollar policy.
- **decision target:** for selected official-row analogues, enumerate the
  exact first-match shells `E_a(U)` from
  `l1_exact_shell_prefix_hankel_bridge`, remove every theorem-paid quotient or
  structured shell, and measure the primitive residual's maximum fiber
  against both its ambient and attained-image means. The output should test
  the row-sharp Q constant, print the effective-image collapse, count occupied
  cofactor targets and their Pade-graph divisor intersection, and identify
  extremal received words or a stable exchange-compression law.
- **object discipline:** enumerate complete agreement sets only. A codeword
  with agreement set `B` belongs once to `E_|B|(U)` and must not be counted
  through all sub-supports of `B`. Retain the interpolation-prefix vector,
  exactness guards, primitive/quotient classifier, and first-owner key.
- **support-moment cross-check:** consume
  `l1_pade_split_section_support_moment_inversion`.  If the implementation
  also enumerates upstream's lattice/split-pencil support census, verify
  exactly that it equals the unguarded full-Pade split count and
  `sum_a binom(a,m)Z_a`.  Print the guarded deletion and, on complete toy
  profiles, replay the finite inverse.  Never report `cen(U;m)` as a number
  of codewords: one codeword with `a` agreements carries `binom(a,m)` support
  witnesses.  A mismatch is a checker failure, not evidence about flatness.
- **balanced-lattice prefilter:** in every band instance
  `2m<=n+k-1`, compute one shifted weak-Popov basis of `M_U` and record
  `(d_1,d_2)`.  By
  `l1_exact_shell_balanced_shifted_lattice_reduction`, a `d_1<=w` instance
  has zero complete level-`m` shell and must be removed before the fleet; its
  binomial support census is not residual mass.  Enumerate only
  `w+1<=d_1<=d_2<=omega` through the degree-capped `(A,B)` pencil, retaining
  monicity, `W|Omega`, and `gcd(Q,W)=1`.  Report the base-field normalized
  raw support count and the exact-guarded count separately by profile and
  first owner.  Any near-rational exact-shell hit is a theorem falsifier and
  must emit the full basis and codeword profile.
- **complement-dimension prefilter:** before sharding balanced profiles, put
  `s=omega-w` and consume `l1_band_complement_dimension_packing`.  Compute the
  exact integer cap `floor(binom(n,s)/binom(omega,s))`; remove the shell when
  it fits the allocated numerator, and remove reserve-sublinear `s`
  asymptotically under the printed absorption condition.  Donated compute has
  no value in that transition strip.  Retain only linear-`s` rows for Q/BC
  concentration experiments, and report the packing cap as a coarse control,
  not as the base-field-normalized prediction.
- **boundary/interior shard split:** consume
  `l1_boundary_shifted_lattice_affine_q_cell` before scheduling balanced
  profiles.  At `d_1=w+1,d_2=omega`, report the `B=0` infinity ray separately
  and require its complete-agreement guard to retain at most one codeword;
  shard the `B!=0` points by the unique affine parameter `A`.  Mark whether
  `W_1=1` (the prescribed-top-coefficient locator-Q atom) or `W_1` is
  nonconstant (the quotient/residue Q cell).  Assign only `d_1>=w+2` to the
  interior BC census.  A valuable donated run measures Q-cell concentration,
  quotient-owner coalescing, and guard-pruned exact BC by these disjoint
  profiles; recombining the boundary into BC or charging it twice is a
  checker failure.
- **interior support-floor cross-level routing:** consume
  `l1_interior_bc_floor_higher_shell_q_routing` before treating Paper D's
  `M_B^disc/M_B^soft` term as an L1 baseline.  At profile `d_1`, identify the
  floor codewords with complete agreement `m'=k-1+d_1`, verify that every
  proper level-`m` sub-support fails `gcd(Q,W)=1`, and route each codeword once
  to boundary Q at level `m'`.  Report three columns: raw support census,
  deleted higher-shell-ray multiplicity, and residual `BC_exact_guarded`.
  Donated compute should target concentration in the last column.  Re-running
  the base-field floor without this separation has no list-side decision
  value; a retained proper floor sub-support is a theorem falsifier.
- **coefficient-content first owner:** consume
  `l1_split_pencil_content_exact_shell_descent` on every remaining balanced
  pencil.  For `(W,N)=A g_1+B g_2`, compute the monic
  `G=gcd(A,B)` and assert `agr(U,N/W)=m+deg G`.  Discard the raw level-`m`
  copy when `G!=1`, divide all four polynomials by `G`, and emit the one
  primitive owner at level `m+deg G`.  Basis changes may be used for speed,
  because the coefficient ideal is invariant, but each shard must replay
  that invariant on a sample.  A useful donated run enumerates only coprime
  coefficient pairs after this prefilter and reports primitive concentration
  by profile.  Support-ray enumeration or cross-level deduplication after
  content division is redundant compute; any disagreement between content
  degree and agreement excess is a theorem falsifier and must preserve the
  complete basis, word, and codeword.
- **polynomial-led deeper-Q curve:** for every residual polynomial-led profile
  with `1<=e<=k`, consume
  `l1_polynomial_led_interior_to_deeper_q_curve`.  Construct the `B^e`
  injective target curve `theta_z`, retain the per-slice cofactor gcd guard,
  and report occupied slices and their guarded populations.  Do not launch
  `|B|^e` independent jobs or charge one additive ceiling per formal slice.
  A useful donated run must evaluate a compressed curve/image intersection
  and decide whether the number or total excess of occupied slices is small
  enough for the finite numerator.  Record partial output by curve-parameter
  shard and preserve extremal `s,R_s,L_T`; raw enumeration of all formal
  slices is not an executable request.  Nonconstant-basis and `e>k` cells
  remain separate shards.
- **boundary planted-root precharge:** for every nonconstant `W_1`, compute
  `D=gcd(W_1,Omega)` once and consume
  `l1_boundary_q_planted_root_descent`.  Verify `D|N_1`, require every exact
  locator to contain `D`, and remove the rigid `deg D>=k` case analytically.
  For `deg D<k`, emit only the root-free residual in the unique coordinates
  `P=P_S+D R`, preserving depth `w`.  Do not shard over subsets of the
  planted roots and do not pool punctured domains under a smooth-domain Q
  constant.  A useful donated run groups the remaining rational-Q cells by
  residual multiplier and first quotient owner, and reports whether a
  numerator-preserving coalescing law is visible.
- **projective packing prefilter:** construct
  `V=span(G,W_1 F[X]_<d)` after planted descent and consume
  `l1_rootfree_rational_q_projective_packing`.  Reject any split point in the
  infinity hyperplane as a theorem falsifier, and remove every profile whose
  exact packing ceiling `floor(binom(n-r,d)/binom(m-r,d))` already fits its
  allocated numerator.  At linear locator density, also remove asymptotic
  profiles with `d=o(n)` whenever the printed reserve absorbs the resulting
  `exp(O(d))` cost.  Donated compute has value only on the remaining
  linear-`d` cells: report projective dimension, attained image scale,
  quotient-pullback owner, and concentration relative to both the packing
  ceiling and the base-field average.  A fixed-dimensional Conjecture-F sweep
  merely replays a proved payment and should not be launched.
- **deep-tail exclusion:** do not schedule shells with `2m>n+k-1`.
  `l1_deep_exact_shell_johnson_closure` pays all of them together by `n^2`.
  A checker may replay the one integer Johnson inequality at `m_J`, but a
  shell-by-shell deep census has no decision value and is not a contributor
  compute request.
- **preferred representation:** use
  `l1_exact_shell_complement_toeplitz_normal_form`. Enumerate monic complement
  divisors `M|Z^n-beta`, impose the exact coefficient window
  `[Z^(n-w)]UM=...=[Z^(n-1)]UM=0`, and retain the cofactor gcd guard. Quotient
  received words by degree-below-`k` shifts before sharding, since the
  Toeplitz window is proved invariant under those shifts. Do not repeatedly
  interpolate supports or materialize barycentric denominators.
- **cofactor-prefix representation:** for `0<=e<k`, first consume
  `l1_official_newton_cofactor_window_router`. Normalize the received
  polynomial, record `h`, and put `a_0=k+ell_0-1`. If
  `h-a_0<=p-ell_0`, use the first `d=min(a,h-k)` power sums or locator
  coefficients interchangeably; the target change is proved bijective
  because `d<p`. This covers at least the 3,175 layers
  `0<=h-a_0<=3174`, and every word when `p>=n-k`. Do not schedule separate
  Newton-cycle or locator-versus-power-sum jobs in this scope. The run must
  still test max-fiber concentration or collective graph intersection.
  Outside the ordinary Newton window, consume
  `l1_official_frobenius_checkpoint_q_router`: retain p-free power sums and
  the elementary coordinates at indices divisible by `p`. There are at most
  23 such checkpoints over the complete official degree range. Then consume
  `l1_official_coarse_pfree_entropy_reserve`: at every checkpoint depth the
  coarse ambient average is below `2^-28276`, and the finite sufficient
  target is coarse max-to-average inflation `K_d<=q 2^28148`. Report this
  ambient ratio directly. An image-normalized ratio is not interchangeable
  and must print the effective-image factor. The sharper generated-field
  calculation accepts an exactly owner-pruned F2-shaped bound
  `max Exc_d<=2^(15(d-r))mu_free(d)` and then forces every extras count below
  `2^-3393`, hence to zero; it does not apply to the full nonempty fiber.
  Sixteen bits per condition are not certified by the same coarse
  inequalities. A contributor may test this 15-bit statistic only after
  implementing a uniform arbitrary-target received-word/Pade owner and exact
  structured subtraction; the F2 zero-target sector is not a conformance
  substitute.
  Also consume `l1_coarse_pfree_wronskian_distance_packing` before launching
  any residual census. For each `(n,a,d)` cell, print the exact theorem cap
  `floor(binom(n,s)/binom(a,s))`, where
  `s=a-ceil((d+2)/2)+1` (and `s=floor((a+k)/2)` in the scalar L1
  specialization), together with the allocated row numerator. Discard cells
  already paid by this cap. The surviving computation must study whether
  far-separated families approach or exceed the required payment after the
  declared Pade/first-owner subtraction. Do not enumerate close pairs or
  spend a fleet verifying the proved distance inequality.
  Interpret this prefilter correctly. If `a+k>=n` and `n-a>=128`, its cap is
  provably above the official numerator, so no computation should present it
  as a row payment. If checkpoints are retained and the run is on exact
  mixed/Pade fibers, use the stronger existing `d+1` codeword-distance bound
  and the decorated shift-pair compiler instead. Contributor compute has
  value only after choosing one of these two typed lanes and measuring its
  genuinely unpaid concentration.
  For the coarse lane, implement the exact output schema supplied by
  `l1_coarse_pfree_wronskian_neighbor_compiler`: first compute
  `tau_p=max(ceil((d+2)/2),min(d+1,p))` and reject every proposed record with
  `t<tau_p`. For each surviving record `(t,j,X,W)`, where
  `j=t-ceil((d+2)/2)`, verify `deg W<=2j+(d mod 2)`, verify that `W` is nonzero on
  both tails, and canonicalize the first owner. Aggregate by
  `(row,owner,j,W)` and report the maximum number of distinct exchanged
  subsets `X`; the opposing tail has proved multiplicity one and must not be
  an independent shard axis. Compare this observed exchange multiplicity to
  both the allocated numerator and the exact `R_q(t,D)` certificate census.
  Large contributor runs should prioritize the smallest **admissible** `j`
  strata (at checkpoint depth, `t>=p>n/24`), retain
  partial per-owner maxima and witnesses, and stop before materializing all
  `binom(a,t)` subsets. Their decision target is a compression law in `X`,
  not another coarse-fiber census.
  Special-case the first-checkpoint minimum width before that generic schema.
  For `p<=d<=2p-2` and `t=p`, consume
  `l1_official_first_checkpoint_split_pencil_reduction` and represent every
  record by `(Q,b,c)` in
  `F_X=Z^p+Q+b`, `F_Y=Z^p+Q+b+c`, with
  `deg Q<=r_d=2p-d-1`. Compute
  `r_*(p,n)=floor((p(p-1)-1)/(n-1))` from the exact row and reject every depth
  with `r_d<=r_*` outright: its `t=p` stratum is proved empty. Use
  `floor(11(p-1)/256)` only as a family-wide fallback. At `p=3583` the
  fallback removes caps through `153`; for the control size `n=8192`, the
  exact row cutoff is `1566`. Then consume
  `l1_official_split_pencil_value_capacity`: each fixed normalized `Q` has at
  most `floor(n/p)<=23` fully split values and at most 253 unordered fiber
  pairs. For lower depths, shard a contributor run only by canonical
  affine/scaling orbit of `Q` and first owner, recover the bounded split-value
  list within that record as
  `G_Q(T)=gcd_Zcoeff((Z^n-alpha) mod (Z^p+Q-T))`, and checkpoint completed
  degree and orbit blocks. Emit the at-most-24-column coefficient-matrix rank,
  `G_Q`, its roots, and direct divisibility checks. Rank at least
  `floor(n/p)` rejects a pair; low rank without `deg G_Q>=2` is not a hit.
  Do not launch a `t=p` shard at all when `2p>n`. When `2p<=n<3p`, the proved
  complement-gap theorem additionally rejects `deg Q<3p-n`, equivalently
  every depth `d>=n-p`; at `(8192,3583)` the first retained depth is below
  `4609`, not below the weaker ratio-only boundary `5599`.
  In this `m=2` band, consume the exact polynomial-abc classification. If
  `n-2p>2`, the stratum is empty. If `n-2p=2`, it consists of exactly `n/2`
  antipodal pairs with `C=Z^2-b` and
  `R=ZC^((p-1)/2)`. No `m=2` complement or `Q` compute request remains.
  Before requesting any checkpoint compute, consume
  `l1_official_checkpoint_characteristic_atlas/checkpoint_atlas.tsv`. Of its
  59 exact pairs, 33 `m=1` rows are theorem-empty and must not be launched;
  six broad `m=2` rows are theorem-empty, four `m=2` rows are explicit, and
  only 16 rows initially have `m>=3`. A PR compute request must print the
  exact atlas tuple `(s,n,p,ord,m,remainder)`.
  Do not request minimum-width compute for any `m<=2` tuple.
  Also consume `l1_official_max_split_value_complement_census`. Do not request
  `h=m=deg G_Q` compute on any of the 16 rows; polynomial abc proves those
  strata empty at every depth. Also consume
  `l1_official_broad_checkpoint_frobenius_periodicity_exclusion`: all seven
  rows with `remainder>16` have no pair at all, so no `t=p` request remains
  there. Only the nine rows `n=m(p+1)`, `m in {4,8,16}`, are eligible for a
  lower-`h` pre-request. Such a proposal must print
  `2<=h<=m-1`, its depth interval, and
  `ell_h=n-hp-d+p`, together with the depressed-pencil valuation bounded by
  `n-(h+1)p`. The proved complement compiler replaces the normalized
  `Q` axis by at most
  `floor(binom(n,ell_h)/binom(n-hp,ell_h))` complements, but that is not an
  authorization to enumerate them when `ell_h` grows. A request still needs
  a further completeness-preserving compression, a measured cost ceiling,
  and the theorem decision changed by each output. Until those fields exist,
  the lower-`h` search is a research pre-request rather than an authorized
  local or Modal run.
  At the endpoint degrees `(m,h)=(8,7),(16,15)`, first consume
  `l1_mersenne_next_to_maximal_exceptional_reduction`. Every generic tangent
  branch and both binomial outer forms are empty. Do not request compute on
  them. The only live endpoint object is the zero-valuation constant-Euler
  passport `(NMR3)--(NMR5d)`. It is already an exactly saturated,
  domain-supported polynomial Belyi map. Then consume
  `l1_mersenne_next_to_maximal_belyi_shifted_value_gate`: the shifted
  degree-`h` polynomial must divide `W^n-1`, and a nonzero passport is empty
  if both printed projective invariants lie in `F_p`. The `z=0` chamber is
  empty as well. Only genuinely non-prime-field normalization reaches the
  staged proof-producing classification `CR-L1-MCP-NMCE` below.
  The decision target is a row-sharp split-pencil census or a further
  structural owner; do not shard over `(b,c)` or expand the same records into
  arbitrary exchanged subsets or Wronskian coefficients.
  Shard by attained checkpoint
  vectors only if a declared first-owner/Pade aggregation recombines them;
  otherwise test the coarse fiber as one object. Do not launch independent
  jobs over either the ambient `q^r` checkpoint space or an unaggregated list
  of attained vectors.
  Then consume `l1_cofactor_prefix_pade_graph_normal_form`. Reverse the high
  coefficients and represent all possible targets at once by
  `Lhat=Uhat/Qhat mod T^(a-k+e+1)`. The first `e` locator coefficients are
  free, the final `a-k` are determined, and `Qhat` is recovered uniquely by
  truncated division. Enumerate or bound the intersection of this graph with
  the split-divisor prefix image. Do not loop over independent cofactors and
  prefix targets; they are the same graph parameter.
- **all-cofactor representation:** consume
  `l1_full_locator_pade_section_all_cofactors` at every `e`, especially
  `e>=k`. Retain the full reversed locator and compute `Uhat/Lhat` through
  degree `e+w`; membership is the vanishing of its `w` coefficients
  `e+1,...,e+w`. Below the cap the ambient section is exactly the Pade graph
  cylinder of size `q^k`. At and above the cap, record the actual section
  count and rank profile; never assume `q^k`, but do not revert to `q^e`
  independent fixed-cofactor jobs.
- **Jacobian/tangent precharge:** consume
  `l1_pade_remainder_jacobian_tangent_dichotomy`. For every section point,
  compute `D=gcd(L,Q)`. Route `D!=1` by its tangent roots, degree, complement
  gcd, and first owner. For `D=1`, the theorem already certifies Jacobian rank
  `w`; a fleet that recomputes generic primitive ranks has no decision value.
  Any reported primitive rank failure is a theorem falsifier and must include
  `U,L,Q,P`, the exact multiplication matrix modulo `L`, and a checker. The
  useful large computation is global split-point/component concentration on
  the smooth primitive section plus a separate tangent census.
- **Tangent root-set compression:** consume
  `l1_tangent_hasse_root_pinning_census` before launching the tangent census.
  Shard tangent members by the exact monic owner `D=gcd(L,Q)`, not by every
  subset of their common roots.  The fixed-`D` fiber is already proved to
  contain at most `q^max(k-2 deg(D),0)` codewords via `D^2|U-P`, and its Pade
  corank is at most `deg(D)`; recomputing either fact has no decision value.
  Next consume `l1_tangent_confluent_packet_packing`: compute the exact
  integer packet ceiling for every degree cutoff and minimize both the
  `k`-condition and mixed complement-Hasse families over legal `j`. Remove
  every cutoff already fitting the allocated numerator; the `j=1`
  `k`-condition ceiling precharges the full tangent population without owner
  enumeration. For the mixed family, use `j=0` through `r_0<=w+1` and the
  clipped closed-form optimizer `ceil((r_0-w-1)/2)` above that threshold;
  do not scan all `j`. A
  valuable large run must instead report the number and
  distribution of **feasible exact owners beyond the packet ceiling** by
  degree, their quotient/first-match classification, and whether this
  residual mass fits the row reserve after complement packing.
  Preserve `U,D,P,L,Q`, the double-divisibility remainder, exact agreement
  support, and canonical owner for every extremizer.  PASS requires complete
  owner-orbit coverage; a timeout is `INCOMPLETE` with covered owner-key
  intervals.  This is an outbound contributor request until a measured
  complete-orbit pilot and hard cost ceiling exist.
- **Reduced primitive-shell output:** for each nonrigid exact owner `D`, also
  emit the canonical descent from
  `l1_tangent_double_root_descent_to_primitive_shell`: `P_D=U mod D^2`,
  `W_D=(U-P_D)/D^2`, and reduced parameters
  `(n-r,k-2r,a-r,e-r,w+r)`.  Verify that the reduced cofactor is coprime to
  `Omega/D` and count the reduced primitive shell directly.  For `2r>k`,
  record only the zero/one rigid-owner occupancy.  The decision question is
  whether reduced primitive counts are uniformly controlled despite
  puncturing, or whether the feasible punctures concentrate in a paid
  quotient/first-match family.  A fleet that treats the punctured set as a
  smooth subgroup without a transport certificate is invalid.
- **mandatory degree precharge:** normalize `U` modulo degree-below-`k`
  codewords, put `h=deg U`, and route each shell through
  `e=h-a`. Delete `a>h`. Route `e=0` exactly to its locator-Q prefix fiber and
  apply `l1_cofactor_depth_budget_cancellation` for every `0<e<k`. At depth
  `d=a-k+e`, report the maximum full and residual fiber, formal codomain
  `q^d`, attained full and residual image sizes, number of possible cofactors
  `q^e`, and number actually occupied by the shell. The ambient `q^e` union
  cancels algebraically; the image-normalized bound retains
  `q^d/L_(a,d)`, while integer rounding costs `<q^e`. Do not label `q^e`
  itself as a route kill. The deployed full-slice diagnostics predict first
  subunit depth at `e=2` for KoalaBear and `e=1` for Mersenne-31; replay these
  inequalities before extrapolating from toy fields. Route `e>=k` directly
  to the full-locator section and report the continued-reciprocal equation
  ranks, split intersection, gcd deletions, and first owners.
- **depth/owner scope:** upstream `prob:row-sharp-q` is posed at the active
  degree and depth `w`. Below the cap, a campaign at depth `w+e` is a new
  profile unless a checker-replayable degree/depth/first-owner transport is
  supplied. Above the cap, use the full-locator section rather than a formal
  depth beyond locator degree. The F2 ladder/tower identity is not either
  transport. For each profile report the normalized ratios

  ```text
  R_amb = q^d max_fiber/full_slice_mass,
  R_img = L_(a,d) max_fiber/full_slice_mass,
  R_occ = occupied_cofactor_targets/q^e.
  R_graph = q^w graph_divisor_intersection/full_slice_mass.
  R_full = q^w full_locator_section_split_count/full_slice_mass.
  R_tan = tangent_exact_members/full_locator_section_split_count.
  ```

  The primary research question after image collapse is whether `R_graph`,
  after first-match payments and the gcd guard, stays within the row constant.
  `R_occ` is a diagnostic for which part of that intersection creates excess.
- **second-moment compression:** after effective-image collapse, generate the
  ordered records of `l1_growing_cofactor_decorated_shift_pair_compiler`, not
  independent cofactor pairs. In the primitive `e<=w` region, shard by
  canonical ordered split support-pair keys because decoration multiplicity
  is proved at most one. Route `gcd(Q_1,Q_2)>1` by its canonical gcd, domain-
  core factor, and off-domain factor; retain `e>w` as a separate shard family.
  A job that loops over `q^(2e)` primitive decorations is analytically
  obsolete and invalid.
- **gcd descent and sharp endpoint:** divide every record by its canonical
  cofactor gcd before sharding. Store `c`, the domain-root multiplicities in
  the common core, off-domain factors, and reduced `(e-c,w+c)`. Route
  `e-c<=w+c` to the support-pair shard. Retain the received-word/Toeplitz key
  for `e-c>w+c`; the ten exact `F_13` witnesses in
  `l1_decorated_shift_pair_gcd_descent_sharpness` prove that forgetting it is
  unsound. Do not launch a support-only high-cofactor census.
- **map scope:** the toy power-sum map is not a substitute for the
  received-word interpolation-prefix map. A shard using another map is
  admissible only with a proved, checker-replayable transport of both fibers
  and owner conventions. In particular,
  `l1_received_word_barycentric_q_scope_fence` proves that the direct dual
  columns have moving weights `U(x)/L_A'(x)` and supplies a depth-one
  fixed-column obstruction; a contributor must retain these weights rather
  than silently run the locator-prefix Q census. The complement Toeplitz
  representation is the approved exact normalization of those weights, but
  it is still not a top-prefix locator projection. The Pade graph is the
  approved locator-prefix normalization for fixed shell degree and must retain
  its received-word series.
- **sharding and partial output:** shard by row, exact shell size, canonical
  received-word orbit, and deterministic owner-key intervals. Atomically
  checkpoint covered intervals, exact maxima and means, quotient removals,
  extremizers, and unresolved ranges. A timeout reports `INCOMPLETE` with its
  coverage manifest and never reports `PASS`.
- **independent checker:** reconstruct interpolation on every emitted support,
  verify prefix depth `a-k`, exact agreement, no duplicate codeword, shell
  partition totals, primitive/quotient classification, and the claimed
  max/mean ratio. It must replay `Qhat Lhat=Uhat mod T^(a-k+e+1)`, cofactor
  recovery, graph cardinality/coverage, and the complement gcd guard. It must
  also verify `d Rem_U(D)=-(QD mod L)`, full primitive rank `w`, and every
  tangent owner. For charted output it must replay the unitriangular
  saturated-Hankel equivalence and both extra-agreement guards.
- **pilot/cost gate:** before any fleet, publish one small complete orbit
  pilot with throughput, peak RAM, storage, wall time, projected total work,
  and a hard dollar ceiling. Stream artifacts remotely and vendor only compact
  certificates, manifests, hashes, and the checker.
- **DAG effect:** finite samples and stable ratios are evidence only. A DAG
  promotion requires either a theorem-certified complete family proving the
  needed uniform row-sharp bound together with an image-size/occupied-target
  payment, a theorem-certified Pade-graph intersection bound, or a replayable
  counterexample to the proposed bound. An ambient
  theorem before the sparse threshold consumes
  `l1_cofactor_depth_budget_cancellation` directly. Beyond that threshold, a
  max/mean result over the attained image alone is insufficient. A complete
  counterexample may force refinement of the primitive/quotient split or kill
  U2-G; it does not by itself kill U2-L.

#### Round-22 contributor requests L1-N10-ELL-*: the ell-sweep at the next rows

Replaces `L1-N10-128` (dropped). The decisive parameter is petal size
`ell`, not `n`; the falsifier of record is `retained > 10*N_{k+1}(ell)/q`
(the shell-resolved normaliser — see the round-22 addendum on
`critical/nodes/l1_mixed_petal_amplification`). Pricing measured at
1.98e7 candidates/s (round-22 local engine, `notes/pilots_20260807/
l1_ell_sweep/sweep_engine.py`; three-path validated).

- **L1-N10-ELL-48-4** (BEST VALUE): `n=48, q=97`, LAYOUT-A, `ell=4`
  (`t=6, b=1, Lambda=7`), BOX = 205,253,983,244, ~2.87 CPU-h/word,
  8 words ~ 23 CPU-h, 1 GiB. PARKED pending credit authorization.
- **L1-N10-ELL-64-4**: `n=64, q=193`, LAYOUT-A, `ell=4` (`t=8, b=1,
  Lambda=7`), BOX = 15,968,151,894,992, ~224 CPU-h/word, 4 words ~
  895 CPU-h, 1 GiB. PARKED.
- **L1-N10-ELL-64-5**: OUT OF SCOPE — DO NOT LAUNCH (~5.2e5
  CPU-h/word).
- Already done locally at zero cost: `n=32` through `ell=5` (the
  proper-band frontier, exhaustive per word), `n=24` through `ell=6`,
  `n=64` at `ell=2,3` — transcripts in
  `notes/pilots_20260807/l1_ell_sweep/results.jsonl`.

## CR-001: H3 fixed-order high-excess / double-accident certificate

- **status:** BLOCKED ON AN EFFICIENT OFFICIAL-SCALE CUTOFF-35 SCALAR
  ELIMINATION ALGORITHM. The candidate support is exact; no measured
  implementation exists. The complete toy-order benchmark is done; do not
  launch a raw orbit fleet.
- **U1 scope gate:** the extraction in
  `notes/U1_OFFICIAL_ROW_NORM_GATE_TABLE.md` shows that the existing C36
  multistar packet gives one row-prime ideal with norm ceiling
  `6^(n/4)/4`; its larger star degree at `P>=25` does not create the
  Galois-separated prime factors needed for a size contradiction against
  `p>=n^2`. Do not request or launch a campaign justified by a supposed
  `2^f | Norm` transfer. The valid large-compute endpoint is the exact
  blockwise candidate support and survivor census specified below.
- **consumer:** `f3_h3_mobius_excess_half` (C36').

### External contributor work packages

These packages record valuable work that exceeds or lacks a reliable estimate
under the local five-minute and sub-`$1` policy. They are copy-ready as
**Compute requests** in a future H3/shift-pair PR, but none is currently an
authorized local run.

| package | mathematical decision | readiness and promotion gate | DAG effect |
|---|---|---|---|
| `CR-001-ALG-PILOT` | Which of orbitwise Smith/subresultant, Taylor-content cutoff `2<=c<=35`, or the three-resultant superset has a credible official-scale implementation? | reproduce every `n=8` hash/support set; compare at least two methods on one complete larger toy order; include one maximum-degree block; print peak RAM, CPU time, wall time, artifact bytes, factor burden, retries, and a conservative dollar ceiling | route selection only; no status change |
| `CR-001-N8192` | At the first official order, what is the complete cutoff-35 support and does the exact `(36,1)` survivor moment pass? | promote only after `CR-001-ALG-PILOT` supplies a bounded launcher and independent checker; cover all `24,534` block IDs and all retained official-range primes | PASS proves only the fixed `n=8192` shard; endpoint failure kills only `(36,1)` unless an actual DSP8 violation is emitted |
| `CR-001-ALL` | Does one proved uniform generator certify the selected endpoint over all `13<=s<=41`? | promote only after a complete fixed-order campaign validates scaling, resumability, support deduplication, and certificate size; price each order before launch | complete PASS discharges the selected C36' alternative; incomplete output is evidence only |
| `CR-001-P24` | Is `max_(t!=1)P(t)<=24` on every official row? | compare the unordered cutoff-12, exact P25 subresultant, divisor tower, and ordered-root tower only through measured pilots; no full system before one route has a certificate and cost ceiling | PASS closes DSP8 by vacuity; one `P>=25` witness retires only this satellite |

The orbit workload is not uniform. For the top `r` degree classes,

```text
C_r=3(n(1-2^(-r))-r),
D_r=n^2(1-4^(-r))-3n(1-2^(-r)).
```

At `n=8192`, the degree-`4096` class contains `12,285` blocks and degree
mass `50,319,360`: `50.073%` of blocks but `75.009%` of total degree. The
top two classes contain `75.104%` of blocks and `93.757%` of degree. Thus a
low-degree-only pilot is invalid, equal-block-count sharding is misleading,
and production shards must be balanced by measured work or at least algebraic
degree. Degree is still not an operation-count estimate.

### CR-001-P24 satellite: vacuous DSP8 certificate

This is the highest-value alternative output of CR-001, not a separate raw
search.  A complete certificate that, at every official row in
`n^2<=p<=6^(n/4)`,

```text
max_(t!=1) P(t)<=24
```

makes the `P(t)>=25` locus empty, proves DSP8 with zero retained records, and
therefore closes the analytic C36' route.  A single official row and target
with `P(t)>=25` refutes this satellite only; it does not refute DSP8 or C36'.
The cheaper `P(t)>=21` watch proposed in the roadmap is falsification
telemetry, not the falsifier for the displayed theorem.

The algebraic candidate support is now proof-complete but not executable at
official scale. The unordered-product cutoff-12 compiler constructs one
degree-`n(n-1)/2` polynomial whose scalar derivative ideal, saturated by
`(T-1)Y=1`, retains exactly the nonidentity unordered-multiplicity-13
characteristics. At `n=8192` its degree is `33,550,336`, with thirteen
generators rather than the ordered compiler's degree `67,092,481` and
twenty-five generators. The saturation is load-bearing because `P(1)` can be
large. Exact row replay rejects the sole selected cutoff-boundary profile
`U=13,D=2,P=24`. The rich-fiber norm cutoff restricts the field range,
and the low-distance/direct-DSP8 routers supply independent candidate and
class-sensitive certificate checks. But no efficient scalar-elimination
algorithm, measured implementation, or cost ceiling exists. Raw low-distance
orbit enumeration still has at least `530,590,075` Galois/exchange classes at
`n=8192`, while the normalized trace family is generically elliptic and
cannot be replaced by the upstream Chebyshev complete-fiber or
same-`(e1,e2)` conic theorems.

Promote this satellite to a contributor run only after banking all of:

1. a sparse/subresultant implementation of the proved unordered cutoff-12
   scalar compiler, or of the exact sparse-input P25 subresultant scalar. The
   pilot must compare both: the first halves the global product degree but
   retains `U=13,D=2`; the second has exact nonidentity support but its
   zeroth subresultant has degree `(n-1)^2`;
2. a complete small-order comparison against direct hash enumeration,
   including candidate inflation and peak memory;
3. a resumable certificate that accounts for every candidate prime and
   checks the proved `G_12^neq|H_D` criterion using monic gcd,
   divisor-plus-Bezout witnesses and the full removed identity valuation,
   without materializing `H^2`;
4. an independent checker and conservative CPU/RAM/time/dollar ceilings.

PASS authorizes promotion of `f3_h3_dsp8_correlation_bound` to `PROVED` by
vacuity, followed by the existing C36' conditional chain.  FAIL emits the
first exact `(n,p,t,P(t))` witness with `P(t)>=25` and retires only this
satellite.  Incomplete output is evidence only.  Until the four readiness
items are present, this remains an upstream theorem/algorithm request and no
Modal launch is authorized.

The preferred PASS artifact is now the `G_12^neq|H_D` certificate, not a
target table. Its local valuation proof is exact: `G_12` charges
`(U-12)_+`, while `H_D` charges `(D-1)_+`. A contributor implementation may
still emit targetwise `(P,U,D)` values as an independent audit, but a list of
observed maxima without complete gcd/prime coverage is not a proof.

There are now two proof-complete candidate generators to benchmark. The
unordered route uses degree `n(n-1)/2` and cutoff 12, followed by the exact
boundary divisibility. The sparse-input route starts from
`F_n(X),X^(n-1)F_n(T/X)` and takes the coefficient ideal of subresultants
`0,...,24`; after the same nonidentity selector, its scalar prime support is
exactly the `P>=25` support. A donated pilot should compare coefficient
growth, elimination time, peak RAM, certificate size, and factorization
burden. Sparse input alone is not a cost estimate: subresultant zero is the
degree-`(n-1)^2` global product resultant.

A third implementation route is a pre-request until it has a small measured
pilot. The proved quadratic divisor tower selects a monic degree-25 divisor,
inverts `X,T,T-1`, and represents both dyadic torsion tests by repeated
squaring modulo that divisor. At order exponent `s` it has exactly
`98s+30` variables and `98s+54` quadratic equations, reaching `4,048` by
`4,072` at `s=41`. A checked integer unit-ideal certificate gives a complete
bad-characteristic outer set; a modular solution is a P24 falsifier. Do not
launch a full official system. A contributor should first implement `q=3,4`
conformance systems, compare their scalar support with direct fibers, then
benchmark one complete low exponent while recording peak RAM, wall time,
certificate size, and coefficient growth. Four thousand quadratic variables
may be worse than the dense univariate routes despite the bounded degree.

The ordered-root tower is a fourth implementation candidate and the smallest
proved quadratic presentation. It uses 25 explicit first coordinates, one
inverse and two scalar towers per coordinate, and an inverted prefix product
of all 300 pairwise differences. Its official maximum is `2,378` variables
and `2,402` equations. The same pilot must compare it with the divisor tower:
the ordered route saves about 1,670 variables but introduces at least `25!`
generic presentation symmetry. No full run should be requested until a toy
benchmark demonstrates that symmetry breaking makes the smaller system
materially faster and still emits a replayable unit-ideal certificate.

- **proved router:** `f3_h3_low_distance_ideal_star_router`, strengthening
  `f3_h3_low_distance_exceptional_prime_router`; the proved
  `f3_h3_ideal_star_prime_alignment_criterion` supplies the exact fixed-root
  sieve once candidate primes are available. The stronger proved
  `f3_h3_weighted_multistar_router` supplies the baseline sieve: a candidate
  fiber must contain a center of distance-deficit weight at least four. The
  proved `f3_h3_excess_multistar_degree_ladder` raises this threshold with
  `e=P-18`; degree four is confined to the boundary profiles
  `(P,D)=(19,1),(20,2)`. The proved
  `f3_h3_excess_budget_degree_tradeoff` pays `P<=32` analytically and forces
  center weight at least twelve on the selected residual. The proved
  `f3_h3_high_excess_low_distance_moment_reduction` and
  `f3_h3_low_distance_quotient_incidence_router` identify the exact
  certificate currency as a low-distance edge–quotient moment. The proved
  `f3_h3_distance_four_fiber_degree_cap` and
  `f3_h3_high_excess_distance_six_moment_reduction` then remove the
  distance-four term completely. The cap now canonically orients the generic
  graph with indegree at most one, so the generic distance-four graph is a
  pseudoforest rather than merely maximum-degree three. The proved
  `f3_h3_distance_six_support_overlap_payment` also removes every
  support-overlapping distance-six stratum from the direct analytic route.
  The proved `f3_h3_disjoint_distance_six_split_pencil_router` then rewrites
  the residue as a quadratic split-pencil / affine subgroup-line
  correlation with an exact integral certificate target.
  For the direct DSP8 interface, `P>=25` means `e>=7`, so the same proved
  ladder forces two distinct centers of incident weights at least eight and
  six. Minimal stars use respectively four to eight and three to six leaves,
  and their normalized differences form one common-prime bi-star ideal. A
  direct cutoff-25 candidate generator must therefore use the `(8,6)` bi-star
  union, not a generic weight-four or one-center weight-eight envelope. The
  separate post-payment `P>=33` route similarly uses a `(12,10)` bi-star.
  The proved disjoint-six multiplicity gate is sharper for the live DSP8
  stratum: the antipodal-free class forces a two-leaf disjoint-distance-six
  star, while the antipodal class forces two distinct disjoint-distance-six
  edges at one target. The latter ideal must include the cross-center product
  difference; two unrelated collision ideals are not enough. At `P>=33`, the
  two classes force pure disjoint-distance-six stars of degrees seven and
  five. These pure families are the selected product-side generator; the
  mixed bi-star is a completeness fallback.
  The accident-depth compiler's original fixed-order selection pays three
  quotient layers and covers
  `P>=33,R>=4`. Retain four distinct quotient lifts and batch the
  degree-seven/degree-five star with all four product-to-quotient couplings at
  the same row-prime ideal; at least three are nonzero. After choosing a
  nonzero anchor, odd saturation rewrites the batch as that anchor plus the
  three-spoke quotient-collision star. Product-only and one-coupling ideals
  are valid outer envelopes but must not be charged to the selected joint
  survivor count.
  There are now twelve exact disjoint-star/depth alternatives:

  ```text
  (P,R)>=(25,12),(26,11),(27,10),(28,9),(29,8),(30,7),
          (31,6),(32,5),(33,4),(34,3),(35,2),(36,1).
  ```

  Their antipodal-free/antipodal pure-star degrees and anchored quotient-star
  spoke counts are respectively

  ```text
  (2,two-edge;11), (2,two-edge;10),
  (3,2;9), (3,2;8), (5,3;7), (5,3;6),
  (6,4;5), (6,4;4), (7,5;3), (7,5;2), (8,6;1), (8,6;0).
  ```

  The exact normalized class weights repeat on the first five even/odd
  product-profile pairs. Swap parity and the diagonal-target affine payment
  give larger allowances on every odd cutoff:

  ```text
  E=6:      w=11/2,   C=121/136
  E=7:      w=11/2,   C=89023/43520
  E=8:      w=9/4,    C=99/85
  E=9:      w=9/4,    C=72837/27200
  E=10:     w=27/16,  C=99/68
  E=11:     w=27/16,  C=72837/21760
  E=12:     w=3/2,    C=198/119
  E=13:     w=3/2,    C=72837/19040
  E=14:     w=47/34,  C=517/272
  E=15:     w=47/34,  C=380371/87040
  E=16:     w=29/22,  C=319/153
  E=17:     w=29/22,  C=234697/48960.
  ```

  On `E=7,9,11,13,15`, a row evaluator should print

  ```text
  S_(D,E)=sum_(t!=1,D(t)>0)(R(t)-(17-E))_+
  ```

  and use the sharper exact budget

  ```text
  B_par,E=300n^2-17(17-E)(n-1)^2
                   -17(E-1)(n-2)^2-17S_(D,E).
  ```

  The printed constant is the uniform fallback. Omitting `S_(D,E)` is
  permitted only when that fallback is used.

  The first two antipodal product packets keep two edges and their cross-center
  generator. The other entries are pure-star degrees. A complete campaign on
  any one row suffices, but its `P` cutoff, `rho_L`, class weight, and allowance
  are inseparable. For symbolic preprocessing, try `(36,1)` first: it needs
  one quotient lift, no quotient-collision spoke, and has exact sufficient
  moment

  ```text
  Dbar_17^0+(29/22)Dbar_17^A <=(29/153)B_par(n),
  B_par(n)=300n^2-272(n-1)(n-2)-17S_D,
  S_D=sum_(t!=1,D(t)>0)R(t),
  Dbar_17^c=sum_(t in class c,P(t)>=36)N_6^disj(t)R(t).
  ```

  The uniform fallback is `(234697/48960)n^2`. A row evaluator that already
  streams `P(t),R(t)` should print `S_D` and use the sharper row-sensitive
  budget; omitting `S_D` is permitted only when the uniform fallback is used.

  For fixed quotient lift, at most two product centers lie on the complete
  zero-coupling locus, whereas the class-sensitive stars have at least nine
  and seven vertices. A nonzero anchor therefore always exists. The proved
  candidate compressor is stronger for implementation: the full-star /
  canonical-center coupling ideal is center-independent and stays nonzero
  when that coupling vanishes, so neither anchor designation nor the
  zero-locus test is required for completeness. The
  preceding `(35,2)` row needs two quotient lifts and has moment

  ```text
  Dbar_16^0+(29/22)Dbar_16^A <=(319/153)n^2.
  ```

  The larger `(36,1)` allowance comes from swap parity and the affine payment
  for diagonal targets; it does not compare the survivor sets. This is a
  route choice, not evidence that the `(36,1)` survivor set is smaller than
  the incomparable `(35,2)` or `(33,4)` sets.
  More generally, every integer corner on the diagonal `L+E=17` gives a
  sufficient rectangle exclusion. The original weighted-degree breakpoints
  are

  ```text
  (P,R)>=(19,18),(21,16),(25,12),(29,8),(33,4).
  ```

  while the disjoint-star/depth compiler prices every intermediate integer
  corner through `(36,1)`, including the low-depth `(34,3)` and `(35,2)`
  packets. A
  contributor may attack another corner if its template family is smaller,
  but must preserve that corner's exact product cutoff, quotient depth, and
  coupling multiplicity. Mixing coordinates from different corners is not a
  certificate.
- **proved double-accident alternative:** the joint-ideal router targets
  `Y_18` rather than all rich product fibers. Its nonzero-coupling refinement
  removes the second quotient lift from coarse template generation. Each
  positive summand supplies one quotient anchor with nonzero `lambda` and the
  normalized ideal

  ```text
  K^NZ=( (beta_F-beta_E)/pi^2,
         (beta_G-beta_E)/pi^2,
         (beta_EC-D)/pi ).
  ```

  For fixed product center, at most one quotient lift has zero coupling;
  `R(t)>=2` therefore supplies at least `R(t)-1` nonzero generators. The zero
  locus is exactly `{x,y,z}={q,-q,-q^2}`, `w=q^4`, so it is removed by an
  exponent-pattern test. The official row prime divides `N(K^NZ)`. Every
  prime outside the finite nonzero-coupling candidate set has `Y_18=0`, hence
  satisfies C36'. On survivors, reconstruct the complete quotient fiber and
  enlarge the ideal by all nonzero couplings. The proved odd-saturation
  syzygy shows this symmetric batch is exact at every odd row-prime ideal;
  equivalently, one nonzero anchor plus its quotient-collision star is an
  exact separated normal form. The product-direction
  identity similarly removes the product-collision generator type: after
  inverting two, one coupling row and column generate the complete
  product-by-quotient rectangle. Intersecting
  unrelated product-prime and quotient-prime unions does not certify common
  target or common prime-ideal alignment.
- **proved global resultant compiler:** with
  `F_n(X)=((1-X)^n-1)/X`, the complete ordered shifted-product polynomial is
  `Res_X(F_n(X),X^(n-1)F_n(T/X))`, and the nonidentity quotient polynomial is
  `Res_X(F_n(X),F_n(TX))/(n(T-1)^(n-1))`. Each cleared first-nineteen
  derivative packet is one bivariate resultant modulo `U^19`. Future
  preprocessing must use this representation or a stronger compression; it
  must not enumerate `(n-1)^2` product roots or construct the dense product
  polynomial. CR-001 remains blocked because a degree-`n-1` resultant at the
  first official order is still not an efficient template generator. A
  valuable contributor result is now a coverage-proved recurrence,
  modular/subresultant algorithm, or norm-template factorization for these
  truncated resultants, with a measured pilot and explicit cost ceiling.
- **proved layered-gcd row compiler:** after reduction modulo a candidate row
  prime, the quotient-lift index need not be enumerated. Successive
  derivative-gcd layers of the cutoff-18 product gcd, saturated to exponent
  `n-1`, recover `X_18` by intersection degrees with the global quotient
  polynomial and recover `Y_18` by replacing it with `gcd(Q,Q')`. A donated
  algorithm should therefore compute or bound these degree sums directly
  from the truncated resultants. A dense degree-`(n-1)^2` replay is not the
  requested computation, and reproducing a row already covered by the hash
  evaluator is not proof progress. The official product-fiber theorem leaves
  only `B_n=min(n-19,ceil(33n^(2/3))-19)` live layers. Each output layer must
  include sequential divisor-plus-Bezout certificates for the defining
  derivative gcds, followed by the terminal monic gcd, exact quotients, and a
  Bezout identity certifying the quotients are coprime; a divisor without
  that identity proves only a lower bound. Promote this route only after a
  pilot demonstrates a genuinely succinct representation, streaming memory
  use, and a conservative external cost ceiling.
- **proved quotient-algebra support prefilter:** over `Z[1/2]`, quotient the
  monic global quotient algebra by the first nineteen product Hasse
  derivatives; append the quotient derivative for the double-accident
  version. The two finite Fitting orders have exactly the official-prime
  support of `X_18>0` and `Y_18>0`, respectively. Their smaller scalar
  annihilators, equivalently their largest Smith invariants or scalar
  elimination generators, have the same support and are the preferred
  outputs. The mod-prime dimensions record only `min(R,(P-18)_+)` and
  `min((R-1)_+,(P-18)_+)`, so this is a candidate-prime compiler, not a proof
  of the weighted target and not a substitute for the stronger `e_n/f_n`
  valuations. For the preferred `(36,1)` endpoint, specialize instead to the
  first thirty-six product Hasse derivatives. The positive odd scalar
  annihilator

  ```text
  (s_(n,35)^X)=(Qhat_n,Pcal_n^[0],...,Pcal_n^[35]) intersect Z[1/2]
  ```

  has exactly the official-prime support of `P>=36,R>=1`, equivalently
  `Dbar_17>0`, and satisfies `s_(n,35)^X|s_(n,18)^X`. It is now the preferred
  candidate-support output for CR-001. A valuable donated computation would
  implement a structured modular Smith/subresultant algorithm for its
  orbit-annihilator family at `n=8192`, beginning with measured pilots across
  representative degree classes and a maximum-degree block at a smaller
  complete order. It must stream or shard, avoid dense maximal minors and the
  degree-`(n-1)^2` coefficient matrix, and
  emit: the odd candidate-prime support with exponents; modular rank witnesses
  at every retained prime; full-rank witnesses at excluded probe primes; and
  hashes/checkpoints sufficient for an independent checker. PASS means a
  complete certified support union for every orbit block at one declared
  order; FAIL means a replayable mismatch with the theorem's small-order
  verifier or a proved algorithmic obstruction; incomplete output changes no
  DAG status. This is
  a **pre-request**, not an authorized run: no official-scale algorithm,
  measured pilot, memory ceiling, or dollar ceiling exists yet.
- **proved Galois-orbit decomposition:** the cutoff-35 support computation is
  no longer one indivisible quotient algebra. Odd dilation partitions the
  ordered quotient lifts into

  ```text
  3(n-s-1) orbits,
  3(2^j-1) orbits of degree 2^j       (1<=j<=s-1).
  ```

  If `s_O,35` is the scalar annihilator formed with the orbit polynomial
  `q_O`, then

  ```text
  rad(s_(n,35)^X)=rad(product_O s_O,35).
  ```

  At `n=8192` there are exactly `24,534` blocks, each of degree at most
  `4,096`, and their degrees sum to `67,084,290`. A contributor may process
  and checkpoint blocks independently and union their certified odd prime
  supports. Duplicate primes across blocks must be deduplicated; the radical
  theorem does not permit adding their valuations. Total algebraic degree is
  unchanged, so this is a memory/resume contract, not a runtime or dollar
  estimate. The exact top-class formulas above show that the degree-`4,096`
  class carries `75.009%` of total degree, while the top two classes carry
  `93.757%`. Every resource pilot must therefore include a maximum-degree
  block, and every production schedule must avoid balancing by block count
  alone.
- **proved formula-generated block manifest:** no quotient-orbit enumeration
  is needed. For each `1<=j<=s-1`, put `L=2^(j+1)` and
  `S_w(Z)=1+Z+...+Z^(w-1)`. The complete canonical IDs are

  ```text
  (j,+,w),       2<=w<L,
  (j,-,w),       2<=w<L and w even.
  ```

  The plus polynomial is
  `Res_Z(Z^(2^j)+1,T-S_w(Z))`. If `a=v_2(w)`, the minus polynomial is
  `2^(-(2^a-1)) Res_Z(Z^(2^j)+1,S_w(Z)T-1)`, equivalently the monic
  normalized reciprocal of the corresponding plus polynomial. This grammar
  generates exactly the proved `3(2^j-1)` blocks and gives stable shard IDs.
  It does not identify scalar support between reciprocal blocks; both IDs
  must be processed.
- **proved three-resultant superset screen:** for each block, define

  ```text
  rho_(O,i)=Res_T(q_O,Pcal_n^[i]),       i=0,1,2,
  (g_O)=(rho_(O,0),rho_(O,1),rho_(O,2)) in Z[1/2].
  ```

  The three resultants are not all zero and `s_O,35|g_O`. Therefore complete
  factorization of every positive odd `g_O`, followed by exact evaluation at
  every retained official prime, is a proof-complete candidate-superset
  route. At `n=8192` it consists of `73,602` independent ordinary
  resultants. It may overgenerate: the three derivatives can meet different
  roots of `q_O` modulo one prime. A pilot must measure this false-positive
  inflation as well as time, RAM, artifact size, and factorization cost.
  Two resultants are not a valid substitute: the first two can both vanish
  in characteristic zero when a block occurs with multiplicity two in the
  product polynomial.
- **proved exact Taylor-content support:** define

  ```text
  F_35(T,X)=sum_(i=0)^35 Pcal_n^[i](T)X^i,
  C_O,35(X)=Res_T(q_O,F_35),
  c_O,35=positive odd coefficient content of C_O,35.
  ```

  Then `rad(c_O,35)=rad(s_O,35)` for every block. This gives exact candidate
  prime support with one polynomial resultant per block and no Smith form or
  three-resultant false positives. At `n=8192` there are `24,534` blocks,
  with `deg_T(q_O)<=4,096` and `deg_X(C_O,35)<=143,360`; the possible
  auxiliary degrees sum to `2,347,950,150`. These degree counts are not a
  resource estimate. A pilot must stream coefficients or modular content
  witnesses and compare coefficient growth, RAM, wall time, artifact volume,
  factorization burden, and dollars against both alternative methods.
- **proved Taylor cutoff ladder:** the preceding exact content identity holds
  for every `2<=c<n-1`, and

  ```text
  rad(c_O,b) divides rad(c_O,a)       whenever 2<=a<=b.
  ```

  Thus any `c<=35` is a complete cutoff-35 candidate superset. At `c=2`,
  the content keeps exactly quotient-supported triple product collisions,
  excludes different-root false positives from the three scalar resultants,
  and has maximum auxiliary degree `8,192` and total possible auxiliary
  degree `134,168,580` at `n=8192`. It still retains genuine product
  multiplicities `3<=P<=35`, which exact row filtering must reject. A
  complete pilot should measure at least cutoffs `2`, an intermediate cutoff,
  and `35`; selecting a cutoff from incomplete shards would bias the
  cost/inflation comparison.
- **banked small-order conformance oracle:**
  `tools/c36_taylor_cutoff_reference.py` is a dense exact implementation with
  a hard refusal above `n=16`, atomic per-block checkpoints, explicit timeout
  packets, and no official-scale entry point. The proved regression packet at
  `n=8`, cutoffs two and three, generates all 12 blocks and completes in about
  `0.82` seconds on the guarded local machine. Independent finite-field
  enumeration at eight primes gives cutoff-two support `{17,41}` and
  cutoff-three support `{17}`. A donated sparse or distributed implementation
  must first reproduce this packet's product hash, block IDs, block hashes,
  contents, and 16 direct support comparisons. This is a correctness oracle,
  not a cost model; `n=16` has not been validated and must be reported as a
  new measured pilot rather than an inherited claim.
- **first official order:** `n=8192`; later orders only after an orbitwise
  candidate-support implementation makes this first order credible.
- **decision:** select one complete row of the joint-star/depth table before
  generating candidates. The preferred first symbolic attempt is the
  coordinate-minimal `P(t)>=36,R(t)>=1` row. Generate its candidate-prime
  candidate set with every exact orbit annihilator `s_O,35`, every Taylor
  content `c_O,c` for one declared `2<=c<=35`, or every three-resultant
  superset integer `g_O`; union and deduplicate prime divisors. Every route
  with `c<35`, and the scalar-resultant route, must evaluate and reject
  lower-multiplicity or different-root false positives exactly. After
  official-range filtering, reconstruct the class-sensitive
  one-lift joint star (pure star
  degree eight off the antipodal class and degree six on it). Its
  canonical-center coupling may be zero without invalidating the nonzero star
  ideal. There is no
  quotient-collision spoke. At the same star centers retain at least five
  and three smooth-trace leaves respectively. If `r,s_i` are their
  distinguished products and `beta_E` is the lifted center target, saturate
  the product ideal by

  ```text
  product_i ((1+r+s_i-beta_E)^3-27r s_i).
  ```

  Every factor is nonzero at an actual row prime, so this saturation is
  completeness-preserving and removes all-singular template components.
  Then prove the row-sensitive inequality when `S_D` is available, or its
  uniform fallback

  ```text
  Dbar_17^0+(29/22)Dbar_17^A <=(29/153)B_par(n),
  or
  Dbar_17^0+(29/22)Dbar_17^A <=(234697/48960)n^2.
  ```

  The established four-lift `(33,4)` fallback instead proves

  ```text
  Mbar_(3),6,33^0+(53/42)Mbar_(3),6,33^A
    <=(583/272)n^2,
  Mbar_(3),6,33^c
    =sum_(t in class c,P(t)>=33)N_6(t)(R(t)-3)_+.
  ```

  The proved base and exact nonidentity quotient-mass payment then give C36'
  for the complete fixed-`n` scope. A violation refutes this sufficient route,
  not necessarily
  C36'; positive but safe rows identify the actual high-excess geometry.
- **legacy full-depth moment interface:** the earlier sufficient certificate
  was

  ```text
  M_6,33=sum_(P(t)>=33)N_6(t)R(t),
  136M_6,33<=21(300n^2-238(n-1)(n-2)).
  ```

  This is conservatively `M_6,33<(651/68)n^2<9.574n^2`. A certificate may
  prove this moment without enumerating every candidate prime if it uses the
  exact canonical incidence router. It remains valid, but the original
  `(33,4)` interface is the depth-three barred moment above because it
  discards all `R<=3` targets. The preferred first symbolic campaign is now
  the one-lift `(36,1)` row; the two-lift `(35,2)` row and wider depth-one
  analytic endpoint at constant `2385/272` remain available.
- **raw single-norm route fence:** a proved restricted-family count gives
  `2,173,296,943,108` unordered low-distance pair-pairs and at least
  `530,590,075` Galois/exchange orbits at `n=8192`. Distance six is generic for
  disjoint norm-three supports. The principal-prime union remains a complete
  outer envelope, but enumerating and factoring those raw orbits is not the
  requested implementation.
- **proved algebraic filter:** distance-two collision norms are powers of two
  and cannot contribute an odd candidate prime. Candidate generation is
  restricted to squared distances four and six; the rich seven-vector graph
  has at least six such low edges.
- **distance-class pilot:** Modal app `ap-nFVftE3yG19HwOwPvjIehP` completed
  both toy orders below `$0.001` in requested-resource function time.
  Distance-four relevant factors number `4` and `67`, while distance-six
  factors number `103` and `2,127`. A larger raw census is not requested;
  distance four should be classified as a four-term sublane and distance six
  remains the generic algebraic generator problem.
- **proved distance-four router:** the generic lane is already reduced to
  `uv=-y` and `x=(u^2-y)/(u(1-y))`; the antipodal lane is
  `x^2=u+v-uv`. Any contributor implementation must use these two-variable
  forms rather than enumerate four exponents. Their proved global ledger is
  `N_4<=(3n^2+n)/2`. Fiberwise, choose one valid cross-overlap orientation
  per generic edge: the head determines the tail uniquely, giving at most
  `g` generic edges and `N_4(t)<=g+ag<=2(m-1)` including the unique possible
  antipodal representation. On antipodal-free fibers `N_4(t)<=m`.
- **required preprocessing:** derive the complete class-sensitive prime union
  for one declared compiler row without enumerating raw collision orbits. For
  the preferred `(36,1)` row, compile all `3(n-s-1)` cutoff-35 orbit
  annihilators and factor only their official-range radical support. The
  orbit manifest must contain every degree class and total degree in the
  proved histogram. If a structural star-template
  implementation is used instead, use pure disjoint-distance-six stars of
  degrees eight and six coupled to one quotient lift at the same row-prime
  ideal. Root at the canonical star center: center-independence and the
  nonzero product ideal make a zero coupling harmless. No quotient-collision
  spoke or zero-locus filter is required. The `(35,2)` row retains its proved
  two-lift one-anchor/one-spoke packet. The
  `(33,4)` fallback uses degrees seven and five with three quotient spokes.
  For the direct `P>=25` interface, the
  corresponding minimal families are a two-leaf star off the antipodal class
  and a same-target two-edge packet on it; the latter must retain its
  cross-center product generator. Complete mixed bi-star and principal
  collision-prime lists are valid but deliberately overbroad fallbacks.
  Distance six needs a sparse cyclotomic norm-template, resultant, or
  equivalent algebraic generator with a proved coverage map under odd Galois
  dilation and pair exchanges. The selected final sieve is class-sensitive
  star/coupling common-prime alignment, not rational gcd, a product-only prime
  union, or ideal normal form.
  For the double-accident alternative, derive orbit-complete templates for
  the three-generator `K^NZ` coarse ideals under odd Galois dilation, internal
  product-pair exchange, and leaf exchange. Retain one distinguished quotient
  anchor and exclude zero coupling by the proved telescoping exponent test.
  The template manifest must retain `(beta_EC-D)/pi`; deleting it admits
  unrelated product and quotient targets and invalidates coverage of `Y_18`.
  The exact survivor checker must then reconstruct `R(t)` and the complete
  `R(t)-1`-or-larger nonzero coupling batch. No second quotient coordinate is
  needed in the coarse symbolic template. For the `(33,4)` fallback campaign,
  retain four distinct quotient lifts and use the anchored
  quotient-collision star as the exact structured batch. Replay
  `c_(u_0)lambda_1-c_(u_1)lambda_0=-theta_01` and
  `lambda_(i,j)-lambda_(0,j)=pi^2c_(u_j)alpha_i` as cross-checks. On an exact
  survivor, store and factor one coupling cross; reconstruct but do not factor
  the full rectangle.
- **analytic alternative:** the canonical edge–quotient router writes the
  remaining distance-six records as four free subgroup variables with two
  rational subgroup-membership tests. A constants-explicit point-count proof
  of the exact moment interface is a complete substitute for the prime-union
  generator; no distance-four incidence bound is required. The legacy
  full-depth split target is

  ```text
  136(42M_6,33^0+53M_6,33^A)
    <=1113(300n^2-238(n-1)(n-2)),
  ```

  or conservatively
  `M_6,33^0+(53/42)M_6,33^A<(1643/136)n^2<12.081n^2`.
  The original `(33,4)` fixed-order version replaces every `R` by `(R-3)_+`
  and has allowance `583/272<2.144`; the wider analytic version uses
  `(R-1)_+` with allowance `2385/272<8.769`. Here the antipodal-free lane has
  two membership tests and the relatively weighted antipodal lane has three.
  A contributor proving a direct incidence theorem may instead target either

  ```text
  4(10M_6,25^0+17M_6,25^A)<=5B_(n,6),
  17(8M_6,29^0+11M_6,29^A)<=22B_(n,10).
  ```

  Their conservative allowances are `24.75n^2` and `(715/34)n^2`, but their
  filters are only `P>=25` and `P>=29`. These are analytic alternatives, not
  authorization to weaken the original `(33,4)` fixed-order request: that
  row's `P>=33` threshold forces the class-sensitive pure distance-six
  degree-seven/degree-five screen. The preferred `(36,1)` row instead uses
  its inseparable degree-eight/degree-six, one-lift packet; `(35,2)` keeps the
  two-lift packet.

  The preferred direct-incidence request is sharper still. On the `E=6`
  interface, retain the selected antipodal quotient mass

  ```text
  S_A=sum_(t antipodal,P(t)>=25)R(t),
  Q_n=(n-1)(n-2).
  ```

  The proved pointwise quotient cap gives
  `S_A<(51/32)(n-2)n^(2/3)`. The two exact overlap covers contain at most
  `2n` generic--generic edges globally, while at most two additional edges
  meet the antipodal vertex on each antipodal target. It is therefore enough
  to prove

  ```text
  D_6,25^0+(17/10)D_6,25^A
    +(867/80)n^(5/3)+(17/5)S_A
    <=(300n^2-102Q_n)/8.                            (CR1-D)
  ```

  Every retained edge has six disjoint signed atoms. A contributor
  point-count argument should impose this disjointness from the outset and
  print `S_A` rather than paying the expensive class against all quotient
  mass. The exact normalized implementation is as follows. For each target
  `t`, split

  ```text
  Q_(t,r)(X)=X^2-(1+r-t)X+r
  ```

  over `H` as `r` varies in `H`; pairs of generic split members with disjoint
  signed supports are precisely the retained distance-six edges. The quotient
  weight is the affine line fiber
  `#{z in H\{1}:1-t(1-z) in H\{1}}`. If `J_25^0,J_25^A` are the raw ordered
  record totals before canonical orientation, the requested inequality is

  ```text
  10J_25^0+17J_25^A+272S_A+867n^(5/3)
    <=3000n^2-1020Q_n.
  ```

  The factor eight is exact. As an algebraic cross-check, every split-member
  pair `r!=s` must satisfy
  `(X-r)Q_(t,s)-(X-s)Q_(t,r)=t(s-r)X`. This is a `cX` shift, not a
  constant-shift top-stratum test.

  The proved primitive-SP adapter sharpens the handoff. Decorate the two
  cubics by `r,s` and forget only the two internal root orders at each
  endpoint. If `K_25^0,K_25^A` count the resulting ordered SP/quotient
  records, then

  ```text
  J_25^c=4K_25^c=8D_6,25^c,
  10K_25^0+17K_25^A+68S_A+(867/4)n^(5/3)
    <=750n^2-255Q_n.                                (CR1-SP)
  ```

  A target-independent proof may instead establish

  ```text
  160(10K_25^0+17K_25^A)<=76599n^2.                (CR1-SP-U)
  ```

  This replaces the former sufficient constants `223` and
  `29031/80=362.8875` by `76599/160=478.74375`. A donated exact row
  certificate should use the weaker target-sensitive `(CR1-SP)`, retaining
  the measured value of `S_A` and the exact order-dependent `n^(5/3)` term.

  The proved rich factorial-moment compiler supplies a second, cheaper output
  interface for the same campaign. While streaming `P(t)` and `R(t)`, print

  ```text
  F_25^c=sum_(t in class c,P(t)>=25)P(t)(P(t)-2)R(t),
  M_21=sum_(t!=1)P(t)(P(t)-1)R(t).
  ```

  These totals require no edge table. Either

  ```text
  40(10F_25^0+17F_25^A)<=76599n^2,
  680M_21<=76599n^2
  ```

  is a complete certificate for the uniform DSP8 route. The first is the
  preferred class-sensitive check; the second is stronger but simpler. The
  older `M_21<=69n^2` target is unnecessary for this consumer, which permits
  `M_21<=(76599/680)n^2`. A violation of either sufficient bound is only a
  route failure, not a DSP8 falsifier. Hash and checkpoint these scalar totals
  with the targetwise output so partial contributor runs remain auditable.

  Candidate coverage for this direct interface is also sharper than the
  generic rich-fiber router. Every retained `P>=25` target has a proved
  `(8,6)` mixed bi-star certificate, with a cross-center generator enforcing
  one target. More usefully, the antipodal-free class contains a two-leaf
  pure disjoint-distance-six star, and the antipodal class contains a
  same-target pair of distinct disjoint-distance-six edges. Generate these
  class-sensitive ideal unions before reconstructing `P,R,F_25`, or the full
  disjoint edge ledger. The `(33,4)` paid tail uses pure stars of degrees
  seven and five, while the `(35,2)` and `(36,1)` rows use degrees eight and
  six. Generic
  weight-four, one-center weight-eight, and mixed bi-star fleets remain
  complete fallbacks but fail the declared row's preprocessing contract
  because they retain avoidable candidates.

  These are degree-three/depth-one shift pairs with equal constant
  coefficient. Every pair is coefficient-primitive because
  `gcd(2^s,3)=1`; quotient-pullback deletion is therefore unavailable. A
  contributor implementing Przemek's SP machinery must preserve the
  target-local affine-line weight and antipodal class. An unweighted SP
  census is not a certificate for `(CR1-SP)`.

  The proved unit-product trace normal form removes another false degree of
  freedom. For distinguished cubic roots `R,S`, let `q^3=RS` and divide all
  six roots by `q`. The decoration forces

  ```text
  q=rs,       ruv=sxy=1,
  sigma=r+u+v=s+x+y,
  t=1+rs(r+s-sigma).
  ```

  Hence a contributor implementation should generate decorated `(r,s,sigma)`
  records for which both

  ```text
  T^2-(sigma-r)T+r^(-1),
  T^2-(sigma-s)T+s^(-1)
  ```

  split over `H`, then apply signed-disjointness, richness, class, and
  quotient-line tests. It must not enumerate generic pairs of cubic triples:
  that ambient search is of order `n^6`, discards the forced scale and target
  weight, and cannot certify `(CR1-SP)`. This normalization refines CR-001;
  it does not create or authorize a separate large run. An official-scale
  campaign still needs a complete compressed generator and measured pilot
  before contributor compute is responsibly requested.

  The antipodal class has a separate proved product-bucketing interface. For
  one canonical sign `a` of `t=1-a^2`, form

  ```text
  C(h)=(1+h)/(1-h),       B=C(H\{1,-1}),
  M_a=#{(alpha,beta) in B^2:alpha beta=C(a)}.
  ```

  Then `P(t)=2+M_a`. The antipodal parity theorem proves `P(t)` and `M_a`
  are even, so a target enters DSP8 exactly when `P(t)>=26`, equivalently
  `M_a>=24`. Its contribution is `E_a L_a`, where `E_a` is the ordered
  signed-disjoint edge count inside that factor fiber and
  `L_a=R(1-a^2)`. For an already selected row, an implementation should hash
  `B` once and, for each special center `C(a)`, scan `alpha in B` and test
  whether `C(a)/alpha` is in that hash set. This evaluates all `M_a` in
  `O(n^2)` field operations and `O(n)` memory. Only centers with `M_a>=24`
  need their small-generic support graph and quotient weight reconstructed.
  It must not materialize either `B*B` or a generic cubic-pair table.

  The proved anharmonic/twin symmetry gives a sound additional
  canonicalization. `R(t)` is constant on the six-value anharmonic orbit,
  and for antipodal `t=1-a^2`, the twin `tau(t)=t/(t-1)=1-a^(-2)` has the
  same `P` and `R`. A row evaluator may therefore compute one quotient weight
  per anharmonic orbit and one product richness per antipodal `tau`-orbit,
  retaining orbit multiplicities. It must still reconstruct the
  signed-disjoint support graph separately at every target: the exact
  `F_97`, order-32 control has equal `(P,R)=(6,9)` at the twin targets
  `23,76` but disjoint edge counts `0,1`.

  This gives an efficient row evaluator and a certificate schema, but it
  does not generate the finite list of official primes on which a rich fiber
  can occur. It therefore does not clear CR-001's preprocessing gate and is
  not a request for another broad row sweep. A useful donated campaign must
  still use the collision-norm/coupled-ideal machinery to prove candidate
  coverage before applying this evaluator.

  The generic normalized trace fiber is not the rational conic appearing in
  the upstream same-`(e1,e2)` h=3 guardrail. DSP8 fixes `(e1,e3)` and lies on

  ```text
  C_sigma: X^2Y+XY^2-sigma XYZ+Z^3=0.
  ```

  This curve is genus one for `sigma^3!=27` and nodal genus zero on the
  exceptional locus. A contributor must therefore not apply the upstream
  degree-two conic parameterization to CR-001. A useful trace-curve program
  would need a theorem for subgroup points on this elliptic family and would
  still have to retain the pair target
  `t=1+rs(r+s-sigma)`, signed-disjointness, richness, and `R(t)`. Counting
  points on each curve, or applying a full-field Weil bound, is not a
  certificate for the weighted pair correlation.

  This geometry is a route fence, not a separate compute request. Do not ask
  contributors to enumerate all `H^2` trace points at official scale unless
  a proved compression specifies which trace/target packets are complete and
  how their output changes DSP8. Any accepted packet must stream or shard its
  points and must not materialize the full `H^2` table in WSL.

  The singular trace locus has now been reduced further and does not justify
  a marginal point-count run. The optimized one-fiber Stepanov specialization
  proves

  ```text
  #{x:L_1(x),L_2(x) in H}<4n^(2/3)
  ```

  for every fixed nonproportional affine pair at official aspect. The former
  branchwise use gave class-weighted coefficient `29376`, but it has been
  superseded. If `g=gcd(3,p-1)`, all singular branches together are one
  shifted intersection in `K={x:x^3 in H}`, of order `gn`. The sharpened
  `(51/16)|K|^(2/3)` theorem gives exact nodal envelopes `552n^2` for
  `p=2 (mod 3)` and `2387n^2` for `p=1 (mod 3)`. More enumeration of marginal
  branch sizes cannot improve the proof route.

  Nor can a search over Stepanov parameters improve it enough. The exact
  ansatz constraints imply the constant floor `2^(5/3)` for every choice of
  `A,B,D`; using two such marginal bounds in the three-cubic-root lane forces
  coefficient greater than `2176>76599/40`. Do not request an optimizer or a
  larger marginal affine-intersection campaign. A signed-disjoint nodal
  antipodal control at `(n,p)=(64,7937)` has `(P,R)=(10,7)`, so replacing the
  class weight by `10` is invalid unless the implementation explicitly uses
  the `P>=25` cutoff.

  A stronger decoration-only class discount is also unavailable. Over
  `F_769` with the order-256 subgroup, one exact signed-disjoint singular pair
  has all nine decorated targets in the live `P>=25,R>0` locus and seven of
  those targets are antipodal. This kills universal `4/9`, `5/9`, and `2/3`
  class-A fraction caps even after richness and quotient support are imposed.
  The fixture has `p<n^2`, so it does not kill an official-size theorem. Any
  donated class-discount argument must nevertheless expose where it uses
  `p>=n^2` or a cross-target arithmetic correlation; a packet that merely
  measures the nine decorations is not a proof route and should not be sent
  as a large-compute request.

  A valuable donated nodal computation must instead attack the joint rational
  target

  ```text
  ((theta phi-1)(theta phi+theta+1)
   (theta phi+theta+phi)(theta phi+phi+1))
  /(theta^2 phi^2(1+theta)^2(1+phi)^2)
  ```

  together with `P(t)>=25`, signed-disjointness, and `R(t)`. Before becoming
  a numbered request it needs a complete finite packet generator and a
  decision threshold capable of improving the weighted constant below the
  residual allocation. Random nodal sampling or independent affine-fiber
  censuses should not be solicited.

  The proved target-divisor router now specifies the front end of such a
  packet. Put `q(a)=a(a+1)`. Before any expensive count, a generator must:

  ```text
  canonicalize {a,-a-1,a^-1,-(a+1)/a,-a/(a+1),-1/(a+1)},
  retain exact decoration and repeated-root multiplicities,
  reject all nine tests T_i(a)+T_j(b)=0,
  reject q(a)+q(b)+3q(a)q(b)=0.
  ```

  The first line removes every positive root collision; in particular the
  complete `t=0` divisor is already gone. The last line is exactly `t=1`.
  Applying only the four visible target-zero factors is incomplete because
  the other two same-triple permutations also violate signed disjointness.

  The proved trace-orbit energy router adds mandatory diagnostics to any
  future candidate-row packet. Let `N_c` count internally signed-distinct
  ordered nodal presentations on trace `3c`. The generator must verify
  `6|N_c` and print

  ```text
  N=sum_c N_c,
  E_tr=sum_c N_c(N_c-6).
  ```

  When `p=1 (mod 3)`, it must also print the exact cubic-character sum

  ```text
  S=sum_(eligible theta) chi(theta(1+theta))
  ```

  and independently check

  ```text
  E_tr=(N^2+2|S|^2)/3-6N.
  ```

  The route-facing thresholds are

  ```text
  N<=(59/10)n^(2/3),
  E_tr<=(51066/1445)n^(4/3),       or       |S|<=4N/5.
  ```

  The first is a proved distribution-free payment. Since the point theorem
  gives `N<(106131/16000)n^(2/3)`, a candidate row below `5.9n^(2/3)` needs
  no cubic-bias analysis; only the narrow interval up to `6.6331875n^(2/3)`
  reaches the trace-balance branch.

  The second places the nodal payment below `1812n^2`, leaving more than
  `103n^2` for smooth traces. Passing either threshold does not close DSP8,
  because no compatible smooth payment is proved. Failing both does not
  falsify DSP8; it shows that this marginal trace-balance payment is
  insufficient and forces the target-sensitive ledger below. These values
  cost only one streaming counter per trace class once a candidate nodal row
  is already being processed. Do not fund a separate large run merely to
  estimate them, and do not infer a bias theorem from sparse samples.

  A donated candidate-row implementation should build the single
  cube-preimage subgroup `K`, scan `theta in K` with `1+theta in K`, recover
  the unique trace class, enumerate the surviving decorated parameter pairs,
  and shard their target set. For each
  shard, stream the `(1-H)` product table to recover `P(t)` and the
  `(1-H)/(1-H)` ratio table to recover `R(t)`; retain only targets in the
  shard. This has `O(n^2+#nodal pairs)` field operations and
  `O(n+#shard targets)` memory, rather than an `H^2` resident table. It must
  print `N_c,E_tr,S`, `G_sing^0,G_sing^A`, `S_A`, per-target contributions,
  orbit multiplicities, and hashes of all shards. The exact route-changing
  check is

  ```text
  10G_sing^0+17G_sing^A+272S_A+867n^(5/3)
    >3000n^2-1020Q_n,
  ```

  which would refute DSP8 on that row. Such a nodal-only falsifier is now
  proved impossible when `p=2 (mod 3)`, so donated nodal runs should be
  restricted to candidate rows with `p=1 (mod 3)`. A safe value is calibration
  only, not a proof. Do not rerun the already measured boundary rows merely
  to obtain a nodal zero: the first `n=8192` control has `max P=20`, and the
  first twelve have `P+R<=22`, so none can meet `P>=25`. Launch this packet
  only after the collision-prime or coupled-ideal generator supplies a
  candidate row where the cutoff can occur. Start with one shard, a hard cost
  ceiling below `$1`, and checkpointed partial totals; larger campaigns are
  contributor requests, not local or current-account jobs.
- **bounded pilot:** Modal app `ap-J4kT8st6P45yWvWZtc2Xgi` completed the full
  `n=32` orbit/norm census and an `n=64` scaling sample for below `$0.001` of
  requested-resource function time. Exact-norm equality compressed `5,216`
  orbits to `227` norms at `n=32`, but the first `5,000` `n=64` orbits already
  yielded `2,567` norms. Therefore simple norm deduplication does not satisfy
  the preprocessing gate. It predates the ideal-star selector and should not
  be extended.
- **bounded ideal-star pilots:** Modal app `ap-yiFl4ymMCORN2txyqtXONi`
  completed the normalized principal-gcd screen. It removed no relevant
  primes (`103 -> 103` at `n=32`, `2,127 -> 2,127` at `n=64`) and counted
  `24,407,583` and `2,569,691,591` raw rooted stars. Modal app
  `ap-InR5xZAak4rOrjhrEUWIIZ` then tested exact common-prime-ideal alignment
  without star enumeration. It compressed `103 -> 18` and `2,127 -> 162`.
  Both complete campaigns cost below `$0.001` in requested-resource function
  time. This selects prime-ideal alignment and rejects rational gcd screening.
- **bounded weighted-multistar pilot:** Modal app
  `ap-jU9q1eWAaOiRkg3sqZForL` applied the stronger exact sieve to those
  aligned lists. It compressed `18 -> 4` at `n=32` and `162 -> 67` at
  `n=64`, or `103 -> 4` and `2,127 -> 67` from the principal-prime lists.
  The two functions used `0.289` and `5.825` seconds and cost below `$0.001`
  in requested-resource time. Future contributor implementations should test
  the joint pure-star/nonzero-coupling condition, not merely weighted degree
  or two incident low-distance edges. Both toy orders have empty `P>=19`
  loci, so they also have empty `P>=33`, `P>=35`, and `P>=36` tails; the pilot
  measures historical mixed-edge compression rather than any live joint
  scale. It should not be extended before the new template family has a
  structural generator.
- **known rich-fiber check:** on both exact rich fibers at
  `(n,p)=(8192,67657729)`, one center has nine distance-six leaves and the
  first two normalized collisions generate the prime ideal itself. This
  demonstrates the intended ideal compression on known positives. These
  fibers have `P=20`, so the `E=14` theorem pays them before the requested
  high-excess computation. Their quotient multiplicity is one, so the
  accident-depth compiler also removes them from the selected joint campaign.
- **screen after preprocessing:** for each candidate prime, fix one primitive
  `n`th root and enumerate each squared-norm-at-most-three unordered shifted
  pair once. Group products by value and enforce the selected compiler row.
  On the preferred row, retain the prime only if some fiber has `P>=36`,
  `R>=1`, a disjoint distance-six degree at least eight off the antipodal
  class or at least six on it, and the canonical-center coupling for the one
  retained quotient lift lies in the same row-prime ideal as the star. That
  coupling may vanish in characteristic zero; the product star keeps the
  ideal nonzero. No quotient-collision spoke exists on this row. The
  `(35,2)` fallback uses the same star degrees, two lifts, one nonzero anchor,
  and one spoke. The `(33,4)` fallback uses degrees seven/five, four lifts, at
  least three nonzero couplings, and three spokes.
  Also replay
  the excess-dependent mixed-degree threshold as an independent check. Galois
  invariance makes one root complete; no rooted-star enumeration is required.
  Reconstruct every quotient lift on that target
  and verify that at least `R-1` couplings are nonzero and lie in the same
  degree-one prime ideal as the star. Across all `U(t)` unordered products,
  verify the coupling rectangle has at least
  `U(t)R(t)-min(U(t),R(t))` nonzero entries and is reconstructed from its
  stored row/column cross.
- **arithmetic:** certify every odd generated factor with `p=1 mod n` and
  `p>=n^2`, run the joint screen, and compute exact
  `P(t),R(t),N_6(t)` and barred high-tail moment totals for each survivor. For an
  analytic-route census, stream the split parameters and line fibers per
  target and return `J_25^0,J_25^A` separately; do not retain all raw tuples.
- **required certificate:** algebraic template manifest and coverage count;
  for the preferred scalar route, the formula-generated `(j,sign,w)` block
  manifest, the exact `3(2^j-1)` degree histogram, and every `q_O` hash. An
  exact-elimination shard must include one scalar Bezout or invariant-factor
  witness per block. A three-resultant shard must instead include all three
  resultant certificates, the odd-gcd witness, complete factorization and
  primality certificates, and the exact disposition of every retained
  official-range prime. A Taylor-content shard must include the truncated
  Hasse packet hash and declared cutoff, the polynomial-resultant certificate,
  a complete coefficient-content witness, and complete factorization of that
  content.
  The remaining packet contains normalized
  principal-norm hashes; complete relevant-factor and primality
  certificates; fixed-root subgroup certificates; compact weighted-screen
  summaries; per-prime histogram summaries; and a product/remainder witness
  proving that no relevant factor was omitted. A double-accident certificate
  must also include the zero-coupling exponent-pattern exclusions, nonzero
  coupling-norm hashes, target-local `R-1` batch counts, and odd-saturation
  syzygy hashes. Exact selected survivors must include every quotient-lift key
  required by the declared corner, the canonical coupling (plus a nonzero
  anchor only when that corner requires one), all anchored
  quotient-collision hashes required by that corner (none for `(36,1)`),
  coupling-cross hashes where the corner has multiple lifts, matrix
  dimensions, partial-matching zero locations, and a reconstruction hash for
  the full rectangle.
- **checker:** a small streaming verifier must validate template coverage,
  normalized principal norms, factor certificates, subgroup order, the
  excess-dependent weighted-degree screen, histogram totals, the exact
  edge–quotient moment and high-tail inequalities above, the factor-eight
  orientation identity, the `cX` cubic cross-check, and their composition with
  the proved low-tail payment without retaining the full data set in RAM. On
  the `(36,1)` route it must replay center-independence, accept a zero
  canonical coupling when a nonzero star generator remains, and verify the
  selected cutoff-35 candidate certificate: exact scalar elimination, exact
  Taylor-resultant content at the declared cutoff plus exact cutoff-35
  filtering when `c<35`, or all three scalar resultants plus their odd gcd and
  complete false-positive filtering. It must also verify orbit
  canonicalization from the `(j,sign,w)` grammar, each cyclotomic-resultant
  or normalized-reciprocal polynomial hash, the degree histogram,
  total-degree coverage, each block certificate, and radical-support
  deduplication without summing duplicate valuations. On the double-accident
  route it must independently replay the
  telescoping zero
  test, nonzero anchor congruence, complete quotient batch, normalized-factor
  2-power norms, both coupling syzygies, partial-matching zero bound, and
  cross-to-rectangle reconstruction before applying the `Y_18` reduction.
- **execution shape:** benchmark a tiny order first; shard the proved Galois
  orbit classes using the formula-generated IDs; checkpoint completed classes
  and factors; store large artifacts remotely; return only manifests and
  compact certificates. Before scaling, reproduce the complete `n=8`
  conformance packet from
  `f3_h3_taylor_cutoff_small_order_reference`; disagreement is an algorithm
  failure, not candidate evidence. Do not enumerate quotient orbits, materialize all raw
  pair-pairs, or return them to WSL. Do not factor every
  coupling-rectangle entry: `(CM5)` proves that the stored cross has the same
  odd-local ideal.
- **stop conditions:** do not enumerate rooted stars. Stop if the algebraic
  candidate generator, unfactored cofactors, or measured cost makes a complete
  fixed-order certificate implausible. Bank the partial template/factor
  manifest, but do not describe it as fixed-order coverage.
- **estimated resources:** deliberately unpriced pending a contributor
  benchmark beyond the dense `n=8` oracle. The official campaign is expected
  to exceed the local `<$1` allowance and must not be launched here without a
  new explicit budget. The first external benchmark must print peak RAM,
  CPU/GPU type, wall time, artifact bytes, retry count, and a conservative
  dollar ceiling before any larger order is authorized.
- **outbound `(36,1)` run contract:** the mathematical decision is whether an
  official-order cutoff-35 support compilation followed by an exact one-lift
  survivor census satisfies
  `Dbar_17^0+(29/22)Dbar_17^A<=(29/153)B_par(n)`, or its uniform
  `234697/48960` fallback. Inputs are one declared dyadic
  order, its complete official characteristic interval, the orbit-polynomial
  specification, one declared complete candidate method (every `s_O,35`,
  every `c_O,c` at one fixed `2<=c<=35`, or every `g_O`), and the one-lift
  degree-eight/six packet.
  A pilot must first measure wall time, peak remote RAM, artifact volume, and
  dollars on a strictly smaller complete order and on a maximum-degree block;
  success on low-degree blocks alone is not a scaling datum. Until then total
  cost is unknown and no local Modal launch is authorized. Completed shards must
  stream completed `(j,sign,w)` blocks, invariant-factor or Bezout witnesses,
  candidate factors, targetwise `P,R,N_6^disj`, class, `S_D`, canonical coupling,
  hashes, and unresolved block identifiers, so interruption
  yields checkable partial evidence rather than lost work. The independent
  checker described above recomputes the exact moment and coverage ledger.
  PASS at one order proves only that fixed-order shard. PASS for every order
  covered by a proved uniform generator promotes
  `f3_h3_official_order_template_survivor` and discharges the C36' alternative.
  Exceeding the sufficient moment kills only the `(36,1)` route unless the
  output separately exhibits a violation of C36' itself. Incomplete output
  changes no DAG status.

This request is stronger than extending the existing first-prime or raw-norm
sweeps and narrower than certifying every `P>=19` candidate. Its eventual
completeness follows from the proved disjoint-six multiplicity,
support-overlap, and excess-budget routers, but it is not yet an executable
official-order job.

## CR-002: Quotient-pencil rank-two component classification

- **status:** READY FOR EXACT SYMBOLIC CONTRIBUTOR COMPUTE; do not replace it
  with an official-field point sweep.
- **consumer:** `rate_half_list_adjacent_crossing`.
- **proved router:** `rate_half_list_budget_three_fiber_four_rank_gate`.
  The known antipodal component is already descended and welded by
  `rate_half_list_budget_three_fiber_four_antipodal_descent` and
  `rate_half_list_budget_three_antipodal_mobius_weld`. The follow-on
  `rate_half_list_budget_three_antipodal_primitive_quotient_gate` proves that
  its official residual is neither a dyadic cyclic/dihedral pullback nor the
  direct four-coset deletion partition. The reverse-contact theorem
  `rate_half_list_budget_three_antipodal_pencil_degree_floor` further proves
  that the monic pencil's degree-drop direction has degree at least
  `2^36-2`. On the centered pure-quartic stratum `e_2=e_3=0`, the Wronskian
  refinement `rate_half_list_budget_three_antipodal_pure_quartic_degree_rigidity`
  proves the exact degree `v=2^37-2`. The differential refinement
  `rate_half_list_budget_three_antipodal_reverse_residual_stratification`
  proves that `T=dDU-Y(D'U+4DU')` has exact degree
  `r+4-q(r-v)`, where `q` is the first nonzero centered coefficient.

  The proved
  `rate_half_list_budget_three_fiber_two_cycle_quotient_embedding` adds a
  second direct chamber to a parameter-uniform quartic-pencil input:

  ```text
  source branch             quotient order   member degree   dyadic M
  fiber-four antipodal          2^39            2^37-1         2^35
  fiber-two cycle, matched c=0  2^40            2^38-1         2^36.
  ```

  The cycle router is exhaustive in the number `c=0,1,2` of antipodal
  deleted-root pairs; completion-root coincidence is analytically impossible.
  Every stratum inherits the Mobius weld, primitive map
  degree, and degree floor `deg V>=2^37-2`. Only `c=0` has the matched
  denominator `product_i(Y-rho_i^2)` in the table. The `c=1,2` denominators
  replace one or two repeated coefficient-square roots by exceptional-pair
  squares and require separate symbolic routing. The proved
  `rate_half_list_budget_three_fiber_two_cycle_boundary_transfer` now replays
  the reverse-residual, pure, fourth-root, secondary, two-window, parity, and
  canonical-span stages at `d=2^40,s=2^38`. It finds linear generic and
  intermediate floor residuals and pins the completion-root PGL matching.
  The remaining finite symbolic audit begins after canonical span: the
  matched `c=0` two-antipodal-denominator subbranch now passes through
  `rate_half_list_budget_three_fiber_two_cycle_matched_lift_field_router`.
  At `M=2^36`, the order-`2^39` Fourier resultant removes the prime-field and
  negative quadratic branches. In the remaining `p=1 mod 2^40` branch, all
  quotient coefficients and outer roots descend to `F_p`; conjugating the
  three Mobius-ratio equations also eliminates the apparently quadratic
  anti-invariant source lifts. The proved
  `rate_half_list_budget_three_fiber_two_cycle_matched_post_field_compiler`
  then closes the harmonic branch and transfers the ODE, scalar, constant,
  Legendre, and gcd stages. Its exact final gate is `T/q_out=W^4`, invariant
  under reciprocal choice. This repairs the old unscaled `T=W^4` condition,
  which is false as a coverage gate for exact-order-`2^39` outer ratios in the
  nonsplit field class. The proved
  `rate_half_list_budget_three_fiber_two_cycle_matched_trace_jacobi_norm_transfer`
  now supplies the remaining exclusion interface: two torsion-sign packets,
  each with six degree-`2^36` Jacobi gcds, one top norm at order `2^39`, and a
  37-level plus tower through order `2^38`. The mathematical contract is
  complete for this parity subbranch,
  but no compressed implementation or measured pilot exists. Other matched
  denominator geometries are not covered. For `c=1,2`, the proved mismatch
  invariant router replaces the old denominator-lift Mobius search by 24 and
  six explicit binary-quartic scalar tests. The follow-on trace-resolvent
  theorem eliminates their radicals and discrete lift signs: `c=1` is twelve
  quadratic norms, while `c=2` is one degree-`6`/degree-`3` resultant in the
  coefficients of `D_*` and the canonical outer quartic. The proved
  `rate_half_list_budget_three_fiber_two_cycle_c2_outer_torsion_trace_gate`
  adds an outer official-order prefilter for `c=2`: forty squarings and cubic
  reductions test whether the outer invariant cubic has a trace coming from
  `mu_(2^40)`. The proved joint selector then intersects that terminal trace
  equation with the degree-six actual-pair resolvent. Its degree-at-most-three
  gcd is nonconstant exactly when the same trace belongs to an actual pair
  with invariant coupling and quotient torsion; outer-only false positives
  are discarded before reconstruction. Finally, common subgroup scaling
  replaces the six labelled pairs by one role-labelled `(t,S,P)` chamber
  modulo `(t,S,P)->(t^-1,S/t,P/t^2)`, with forty scalar squarings compiling
  all three nontrivial quotient roots. These are constant-memory theorem-side
  reductions, not contributor computations. The remaining next step is
  symbolic substitution of the twelve `c=1` norms and the normalized `c=2`
  chamber into the coefficient-gap and canonical-span equations, not a raw
  official-order sweep. The `c=1` packet
  also has a coefficient-only compiler: one bidegree-at-most-`(18,18)`
  divided-quartic iterated resultant equals `e_4^36` times the twelve-norm
  product. Future implementations must use that resultant rather than factor
  `D_*` merely to enumerate the root choices. Canonical covariance further
  turns theorem search into one role-labelled `(S,P,c)` chamber with
  repeated square one. Its three quotient-root torsion conditions use forty
  coupled scalar squarings. This normalization is cheap preprocessing, not a
  compute request; split, square-class, gap, and canonical-span checks remain.

  **Pre-request CR-002-C (next-order cycle shard).** The boundary transfer
  proves that a two-antipodal-pair denominator uses `M=2^36`, and the matched
  lift field router proves that every surviving normalized lift lies in
  `F_p`. This conclusion requires only `p=1 mod 2^40`; a contributor must not
  impose the stronger `p=1 mod 2^41` or allocate a separate quadratic-lift
  shard. A preregistered `$0.25`-capped harmonic extension has already checked
  the only new source-trace level over all `2,247,720` split congruence classes
  and found no hit; contributors must not repeat that campaign. The proved
  trace-Jacobi/cyclotomic-norm transfer gives the exact torsion-only screen at
  `M=2^36`: one top
  cyclotomic norm at order `2^39` and a `37`-level plus tower at orders
  `2^2,...,2^38`. Record this as a second contributor shard after
  CR-002-J0, not as permission to run it. PASS, FAIL, and incomplete outputs
  have the same certificate meanings as J0 but must carry the cycle source
  key, `c=0`, and the doubled parameter ledger. The `c=1,2` mismatch strata
  now have a coverage-equivalent thirteen-gate radical-free elimination, and
  `c=2` also has the cheap forty-step joint actual-pair selector and normalized
  `(t,S,P)` chamber above.
  The `c=1` side is likewise one constant-degree coefficient resultant.
  Any future `c=1` implementation must use its normalized `(S,P,c)`
  chamber and may not multiply work by twelve labelled root choices.
  They remain theorem requests rather than norm-compute requests until
  canonical span has been eliminated or a separately piloted algorithm has a
  finite completeness and cost boundary. A future contributor proposal must
  report how many candidates survive the joint selector and must not spend
  official-order resources on candidates that fail it. The exact
  decision contract is now:

  - **PASS:** neither torsion resultant has an official-compatible odd-prime
    divisor; this closes both six-branch trace-Jacobi packets in the matched
    parity subbranch and all fourteen primary/torsion/constant tests in the
    generic two-antipodal `c=1` parity packet.
  - **FAIL:** print each `(p,epsilon)`, a compact factor certificate, and
    `gcd(J,K_epsilon) mod p`; then evaluate the relevant signed `F_(j,s)` gcds
    and all relevant `c=1` polynomials: `F_R0,epsilon`, plus
    `F_R(s),F_P0(s),F_P(s)` for both roots `s^2=-epsilon`. Then replay the
    corrected scalar, next-coefficient, gcd-degree, and `T/q_out=W^4`
    filters.
  - **INCOMPLETE:** retain proved norm levels, cofactors, hashes, and exact
    characteristic coverage, with no DAG status change.

  This complete mathematical contract does not promote the task to a runnable
  request. It still lacks a compressed implementation, small-order measured
  pilot for that implementation, streaming checker, memory/storage estimate,
  and conservative dollar ceiling. Any larger or alternative official-order
  run must remain recorded here and be proposed in an upstream PR only after
  those artifacts exist. In particular, no contributor should run the old
  unscaled fourth-power schema at `M=2^36`; all survivors use the corrected
  downstream gate.

  **Completed CR-002-C1H (c=1 parity harmonic residues).** The proved
  `c=1` parity Mobius router leaves only two harmonic classes up to sign
  and conjugation:

  ```text
  H_R: r^2+3(1+iota)r+iota=0,
  H_P: 5r-4+3iota=0.
  ```

  They have fixed reciprocal-trace forms. For `H_P`,
  `r+r^(-1)=8/5`. For `H_R`, choose `zeta^2=iota`,
  put `s=r/zeta`, and set `theta=(1+iota)/zeta`; then
  `theta^2=2` and `s+s^(-1)=-3theta`. Source torsion requires the
  corresponding repeated-square trace recurrence to reach `2` by level
  `41`.

  The field router now proves the complete positive-quadratic interval and
  descent of both source lifts. Modal app
  `ap-Js6Im9DeoBlc0di05YG2WE` then completed the bounded two-trace
  campaign over all `4,495,441` integer moduli with no hit. All 32 shards
  finished in at most 3.121 seconds under the `$0.50` ceiling. The result,
  digests, launcher hash, and independent checker are pinned in the
  harmonic-exclusion node. This closes only harmonic `c=1` parity.
  Contributors must not duplicate the campaign; the remaining valuable work
  is theorem-level control of the six nonharmonic tests.

  **Pre-request CR-002-C1N (c=1 parity nonharmonic scalar packets).** The
  proved nonharmonic scalar compiler now supplies the exact mathematical
  interface that a future contributor implementation must preserve. There
  are six role-labelled source traces `y`, not a free outer-ratio search.
  Each branch has the complete decision sequence

  ```text
  y_39=2,       y notin {2,-2},
  S^2=(y+2)T,
  T/q_out=W^4,       q_out^2-yq_out+1=0,
  4tH_(4M-1)(t)^2+y+2=0,
  deg gcd(S,2L+kappa x^2U_0^3)>=M-1.
  ```

  Here `M=2^36`, `L=2^39`, and the reciprocal choice of `q_out` does not
  change the fourth-power verdict. All square-pencil and unordered-trace
  data descend to `F_p` on the exact field line `q_field=p^2`,
  `p=1 mod 2^40`; the source lift itself must not be assumed to descend.

  This is still an algorithm pre-request, not permission for an
  official-degree run. A contributor-scale campaign becomes useful only
  after an implementation represents `U_0,S,T,H` without materializing
  degree-`2^37` dense polynomials, proves that all six branches and all
  official characteristics are covered, and publishes a measured
  small-order pilot. Its request packet must include a conservative CPU,
  RAM, storage, and dollar ceiling; resumable characteristic/branch shards;
  and a streaming checker for every displayed identity.

  **PASS** means all six packets reject on every official characteristic and
  would close the two-antipodal `c=1` parity subbranch. **FAIL** must emit a
  replayable characteristic, role, source trace, reciprocal quadratic,
  compact polynomial certificates, and the first failed/passed gate; it may
  expose a genuine survivor or a false upstream premise. **INCOMPLETE** must
  retain exact interval/branch coverage, hashes, and partial certificates
  and causes no DAG status change. Cost is currently unknown, so this item
  remains outbound contributor work and is not authorized against the local
  Modal balance.

  **Pre-request CR-002-C2N (normalized c=2 mismatch chamber; not runnable).**
  This is the recorded handoff for a potentially valuable large computation;
  it must not be replaced by a sweep over six labelled denominator pairs.
  The theorem-side input is one chamber

  ```text
  D_A(Y)=(Y-1)(Y-t)(Y^2-SY+P),
  z=(1+t)^2/t,
  K_A(z)=0,
  t_40=1,       T_40=2,       P_40=1,
  tP(t-1)(1-S+P)(t^2-St+P)(S^2-4P)!=0,
  ```

  modulo the orientation involution
  `(t,S,P)->(t^-1,S/t,P/t^2)`. The forty-step recurrences and the
  degree-at-most-three joint actual-pair selector are exact. Any campaign
  must then use the proved normalized gap-span compiler. It generates
  `E^(-1/4)` by the signed four-term recurrence, enforces
  `a_(2H-2)=a_(2H-1)=0`, uses the equivalent secondary differential
  divisibility without constructing the high window, reconstructs
  `alpha=4c,beta,gamma`, and applies the final scalar invariant equation at
  `z_t=(1+t)^2/t` before cycle reconstruction. The torsion terminal already
  forces splitting and square class; distinctness remains explicit.

  The mathematical decision interface is now finite and coverage-exact, but
  a naive implementation has official length and is not a responsible run.
  Missing prerequisites are a compressed evaluator for the recurrence and
  polynomial span identity, an exhaustive official characteristic ledger
  organized into the fixed and reciprocal-Frobenius chambers, a canonical
  representative or orbit-safe deduplication under the involution, and a
  measured small-order pilot. Until
  those exist there is no responsible CPU, RAM, storage, or dollar estimate;
  cost is explicitly **unknown and potentially large**, so the local Modal
  balance must not be used.

  A bounded falsification sweep now constrains the theorem strategy. Across
  `680,500` normalized quartets in twenty smooth rows (`H=3,...,12`, two
  admissible characteristics per height), the nondegenerate primary gap had
  22 survivors, including twelve non-pure quartets. Thus primary-only
  fourth-root rigidity is false and must not be used in a contributor
  compiler. None of the twelve non-pure survivors passed the secondary square
  gate; all six primary-plus-secondary survivors were pure fourth-root
  quartets. A separate proof excludes that pure geometry at the official odd
  value `H=2^37+1`.

  The minimal repaired implication "primary plus secondary, together with
  official root torsion and distinctness, implies a
  two-antipodal denominator" is therefore a high-value theorem/falsification
  target, not a compute assumption. The official qualifiers cannot be
  dropped: the split squarefree quartic
  `1+z+11z^2+34z^3+43z^4` over `F_53` passes both gap packets at `H=8` but
  is nonparity. Its roots have orders `52,13,13,52` and mixed square classes,
  so it is an exact gap-only counterexample rather than an official packet.
  The stronger pure
  fourth-root conclusion also survived the sweep, but is unnecessary: the
  proved parity router collapses all six `c=2` selected pairs to three traces
  and imports the existing CR-002 Jacobi norm pair. The pure value itself is
  already excluded at the official row. More bounded rows cannot certify
  either official quantifier. A donated large run should not be requested
  merely to extend this census; contributors should instead seek an algebraic
  proof using the subgroup constraints, a compact official-torsion
  counterexample, or a coverage theorem reducing parity forcing to finitely
  many arithmetic cases. A gap-only differential or Groebner campaign cannot
  prove the required result and should not receive donated compute. The
  scripts, representative
  counterexamples, exact downstream census, and ledger check are in
  `experiments/prize_resolution/` under the
  `rate_half_list_*rigidity*` and
  `rate_half_list_fiber_two_cycle_c2_normalized_small_order_census*` names.

  **Pre-request CR-002-C2PAR (official-torsion parity certificate; not
  runnable).** A potentially valuable donated-compute task is to construct a
  sparse cyclotomic/elimination certificate for the following exact
  alternative at `H=2^37+1`, `N=2^40`: every distinct normalized quartet in
  `mu_N` that passes both coefficient gaps is two-antipodal, or there is a
  compact official-compatible witness. The
  purpose is to close the structural gate before canonical span and route all
  survivors through the shared CR-002 norms.

  Inputs must be the four-term fourth-root recurrence, the proved equivalent
  secondary differential divisibility (which removes the high coefficient
  window), forty-step scalar torsion recurrences, and distinctness. The proved
  torsion-field router makes splitting and square class automatic and divides
  the algebra into fixed and reciprocal-Frobenius chambers. A valid algorithm
  must exploit dyadic/cyclotomic structure or produce a parameter-uniform
  certificate. Naive enumeration of
  `mu_N` quartets, dense degree-`2^36` polynomials, and gap-only Groebner
  elimination are out of scope. No coverage algorithm, pilot, or credible
  resource estimate exists yet; the cost is **unknown and potentially very
  large**, so this is a contributor design request, not authorization to use
  the local Modal credit.

  Every shard or certificate component must emit its normalized parameter
  region, exact integer/modular hashes, first unresolved gate, and a compact
  replay object. An independent checker must reconstruct the quartet or
  certificate, replay torsion and both gaps, and verify the parity/nonparity
  conclusion without trusting search logs. **PASS** is a coverage-complete
  certificate for official parity forcing and would make the parity router
  applicable to all `c=2` candidates. **FAIL** is one distinct order-`2^40`
  nonparity quartet passing both gaps; splitting and square class are checked
  consequences of torsion. It refutes `C2-PAR` and
  redirects work to canonical span and coupling. **INCOMPLETE** preserves
  exact covered regions and certificates but changes no DAG status.

  The exactly-one-antipodal stratum now has a stricter pre-request interface.
  Normalize its known pair to `{1,-1}`, put

  ```text
  P=cd,       t=c/d,       Z=t+t^(-1),       X=P(Z+2),
  a_(2H-2)=F_H(X,P),       a_(2H-1)=(c+d)G_H(X,P).
  ```

  Since `X!=0` on this stratum, both primary equations are `F_H=G_H=0`.
  Complementary-root torsion must be imposed on that same `(P,Z)` by

  ```text
  P_(j+1)=P_j^2,       Z_(j+1)=Z_j^2-2,       0<=j<39,
  P_39^2=1,            Z_39=2P_39.
  ```

  A donated symbolic campaign may target a sparse joint cyclotomic
  certificate for this circuit before the antipodal-free stratum. It must
  not stop at `Res_X(F_H,G_H)` intersected with independent product and ratio
  torsion: incompatible half-order signs leave false positives. The exact
  distinctness gate is `(Z^2-4)(1+P^2-PZ)!=0`; reconstruction makes a
  separate square test unnecessary. In both official field chambers
  `Z in F_p`. Use `P in F_p` in the fixed chamber and `P^p=P^-1` in the
  reciprocal chamber.

  **PASS** for this subcampaign is a coverage-complete certificate that the
  displayed exactly-one-pair circuit has no official-field solution; it
  removes that stratum but leaves antipodal-free C2-PAR open. **FAIL** emits
  one official characteristic and compact `(P,Z)` certificate from which an
  independent checker reconstructs `t,c,d`, replays both primary
  coefficients, all 39 coupled torsion updates, distinctness, and `X!=0`.
  **INCOMPLETE** emits the covered cyclotomic factors or parameter regions
  and changes no DAG status. No compressed representation of `F_H,G_H`,
  official-coverage implementation, measured official-scale pilot, or
  credible cost ceiling exists, so this remains an algorithm and
  donated-compute request with unknown potentially large cost.

  A guarded small-order pilot on 2026-07-21 tested the complete split-field
  one-antipodal circuit at `N=8,16,32,64`. It enumerated respectively
  `6,672`, `53,424`, `251,580`, and `1,039,740` admissible unordered
  complementary pairs over every prime `p=1 mod N` below
  `20,000`, `50,000`, `100,000`, and `200,000`, with no simultaneous primary
  double-gap hit. Total coverage was `1,351,416` pairs. Separate symbolic
  resultants at `N=16,32` showed why the coupled gate must remain: product
  torsion has exceptional-characteristic common roots, but every checked
  split exceptional root failed the half-order trace sign.

  This is heuristic support for the exact circuit, not evidence about the
  official quantifier. It does not supply the missing compressed
  representation, and scaling the pair enumeration to `N=2^40` would be
  worthless. A valuable large contribution is still an algorithmic theorem:
  a sparse dyadic/cyclotomic representation of the joint primary and coupled
  sign ideal, with a measured bounded-order replay and a proved official
  coverage map. Until that exists, its cost remains unknown and no paid run
  is requested.

  **Pre-request CR-002-C2CELL (one-antipodal canonical-cell classifier; not
  runnable).** There is now a downstream alternative to eliminating the
  primary `(P,Z)` circuit. After secondary gap, canonical span, and split
  outer gates, every complete one-antipodal candidate gives

  ```text
  Q=(1-z^N)/E=product_(i=1)^4(B+w_i z^H C),
  mu_N\{1,-1,c,d}=A_1 disjoint_union ... disjoint_union A_4,
  |A_i|=2H-3.
  ```

  The proved Fourier ladder makes the four cell power sums equal through
  degree `H-1`. More generally, a weight vector orthogonal to
  `1,w,...,w^s` annihilates all cell moments below `(s+1)H` for
  `s=0,1,2`. Under source negation, each such weighted coloring is either
  exactly invariant or has support at least `(s+1)H+1`; the official sharp
  forms are `2H+2` for `s=1` and `3H+1` for `s=2`.

  The unique barycentric direction is no longer a dichotomy. With
  `Phi(W)=product_i(W-w_i)` and `lambda_i=1/Phi'(w_i)`, its negation
  difference has zero moments below `3H` and first syndrome exactly `-2H`.
  Hence its support is always at least `3H+1`. At equality, if `Psi` is the
  support polynomial, every value is forced to be `-2H/Psi'(a)` and `Psi`
  is even. A contributor classifier must enforce this syndrome and equality
  packet before considering larger-support cases; a run that merely checks
  the older invariant alternative is obsolete.

  The barycentric direction also has a cell-free endpoint. The proved
  compiler forms one even polynomial

  ```text
  J=(1-Sz+Pz^2)C(z)^2Theta(z)
    +(1+Sz+Pz^2)C(-z)^2Theta(-z),
  Theta=HBC+z(BC'-B'C),       deg J<=5H-11.
  ```

  Minimum support is equivalent to `J` having degree `5H-11`, dividing
  `(z^N-1)/(z^2-1)`, and avoiding `+/-1`. Consequently a contributor must
  not enumerate canonical cells even in the equality case. The useful
  algorithm request is a compressed subgroup-divisor rejection for `J`,
  followed by a root-count/classification argument for the larger-support
  cases. Dense construction of `B,C,J` is still forbidden, and no compressed
  evaluator or cost model exists.

  The collision geometry now controls the full low-support band, not only
  equality. If the four barycentric weights are distinct, the odd Wronskian
  root count gives `|supp(u)| >= 4H-2`. Otherwise exactly one pair collides,
  and the normal form and `L/Q` alternatives in `(COLL1)` apply at every
  support. Thus every one-antipodal packet with `|supp(u)| <= 4H-4` is already
  on the `L/Q` locus. A contributor implementation should route the
  distinct-weight case to the high-support ledger and should not scan it in
  the low band.

  Canonical degree now refines this routing. Put `e=H-3-deg C`. If `r_J`
  counts the ordinary subgroup roots of the support polynomial, then

  ```text
  |supp u|=3H+3e+1_(e even)+eta,       eta in 2 Z_(>=0).   (COLL0)
  ```

  On `e=0`, the Euler/cube gate `(COLL2)`, infinity gate `(COLL4)`, and the
  selected-antipodal affine and Stepanov gates `(COLL5)--(COLL8)` are valid
  at every support. Route those packets through the filters before any
  support-level enumeration. The split-divisor condition for `J`, endpoint
  `Xi` gate `(COLL3)`, and conclusions that explicitly use `eta=0` remain
  minimum-support-only. Degree-deficient packets must retain `(COLL0)` and
  must not be tested with maximal-degree top-coefficient formulas.

  **Deferred large run CR-002-C2CELL-COLL (minimum-support one-pair collision
  locus; contributor compute only).** The proved collision router removes
  every minimum-support packet except an exact one-pair derivative-weight
  collision. For a nonzero pair-sum parameter `s`, put `y=s^2/alpha`. A
  retained packet has

  ```text
  beta=-s^3,
  gamma=alpha^2/4+alpha s^2/2,
  Phi(T)=(T^2-sT+s^2+alpha/2)(T^2+sT+alpha/2),
  L: y(z_t+12)=2z_t-8,
  Q: [y(z_t+12)-16]^2=64z_t,
  -2alpha/(z_t+12) is a nonzero square.               (COLL1)
  ```

  Triple, two-pair, and fourfold collisions are proved impossible and must
  not be searched. The old cubic invariant equation has also been replaced
  by the two displayed branches; the two square-root signs on `Q` are one
  orbit and must not be duplicated. The two branch intersections
  `(y,z_t)=(0,4),(4/3,36)` belong to `L`; define the second shard by
  `Q=0,L!=0`. The requested run is a compressed
  classifier on `(COLL1)` together with `(C2G3)--(C2G8)`, the selected-ratio
  torsion recurrence, the exactly-one-antipodal source equations,
  squarefree/field-chamber conditions, and the split-divisor gate for `J`.
  It must retain `s` and the displayed factors, not merely solve the
  eliminated equation
  `(4gamma-alpha^2)^3=8alpha^3 beta^2`, which is only necessary over the
  official base field. Raw scans of `(alpha,beta,gamma)`, dense
  official-degree `B,C,J`, subgroup enumeration, and any trace-`-12` campaign
  are obsolete.

  The selected-antipodal shard is fixed at `z_t=0`, `y=4/3`, with
  `12gamma=11alpha^2`, `27beta^2=64alpha^3`, `J=0`, and `-alpha/6` square.
  It should be screened first because it has no residual `y` search. The
  non-antipodal shards use the `L/Q` label and the unordered square-root
  trace orbit `x~=-x`, where `z_t=x^2`.

  Every shard has a mandatory outer-free prefilter. Form

  ```text
  T_0=(H-1)EB+Hc_0z^(2H)-(H-1)E_4b_0z^(2H+1),
  P_0=z^(-2H)(T_0B^3-(H-1)),
  c_0=a_(2H),       b_0=a_(2H-3).
  ```

  Minimum support forces `deg C=H-3`; more generally every retained
  maximal-degree packet, at any support, must satisfy

  ```text
  C divides P_0,
  C_sharp=C/lc(C),
  Res(C_sharp,T_0)Res(C_sharp,B)^3=(H-1)^(H-3),
  Res(C_sharp,T_0) is a nonzero cube.                  (COLL2)
  ```

  The secondary-differential theorem makes this gate derivative-free; no
  high coefficient window is an input. This Euler remainder precedes all
  outer coefficients, selected-pair traces, and `L/Q` branches. A contributor
  implementation should evaluate `(COLL2)` first and stop a shard immediately
  on a nonzero remainder. A run that constructs or scans
  `alpha,beta,gamma,y,z_t` before applying this gate is obsolete.

  A shard surviving `(COLL2)` has a second mandatory constant-size endpoint
  prefilter.  Write `r=2H-3`, `m=H-3`, let `b_i=[z^i]B` and
  `c_j=[z^j]C`, and compute

  ```text
  Delta_inf=b_(r-1)c_m-b_rc_(m-1),
  Xi=H/(P c_m^2 Delta_inf).
  ```

  Minimum support forces `Delta_inf!=0`, and every retained packet must pass

  ```text
  Xi^(N/2)=1,                    N/2=2^39.            (COLL3)
  ```

  This test reads only the four top canonical coefficients and the
  complementary-source product `P`.  The checker must reject zero
  `Delta_inf`, reconstruct `Xi`, and evaluate `(COLL3)` by bounded repeated
  squaring before any full `J` split-divisor or `L/Q` work.  It must not build
  `J`, list its roots, or enumerate `mu_N` merely to check `(COLL3)`.  Failure
  is a proved rejection of that minimum-support shard; passage is only a
  necessary condition and does not certify the packet.

  After the canonical outer coefficients are available, apply the
  infinity-cell quartic gate before either `L/Q` branch is expanded.  Put

  ```text
  b=[z^(2H-3)]B,       c=[z^(H-3)]C,
  O_inf(X)=(X-b)^4+alpha c^2(X-b)^2
             +beta c^3(X-b)+gamma c^4.              (COLL4)
  ```

  A retained packet must have `c!=0`, `O_inf(0)=P^(-1)`, and
  `O_inf | X^N-1`.  Check the last condition without factoring: start with
  `R_0=X mod O_inf`, perform forty reductions
  `R_(j+1)=R_j^2 mod O_inf`, and require `R_40=1`.  The checker must also
  verify that the four reciprocal derivative weights of `O_inf` have exactly
  one equal pair.  On the fixed selected-antipodal shard it must additionally
  require the centered binary-quartic invariant `J_inf=0`.

  This is four-coefficient arithmetic and does not authorize construction of
  a subgroup list.  It is not an emptiness theorem: an exact order-32 control
  over `F_97` is a non-antipodal `J_inf=0` subgroup quartet with exactly one
  derivative collision.  Any classification or campaign which treats
  `(COLL4)` alone as contradictory is invalid; it must retain the canonical
  recurrence, gap, source, and completion coupling.

  The fixed selected-antipodal shard has a smaller replacement interface.
  Choose `q^2=-alpha/6`, put `a=s/(2q)`, and derive from the canonical top
  coefficients

  ```text
  tau=ell_4,       y=ell_3/ell_4,       a^2=-2,
  A_a(y)=(a+2)y-(a+1),
  B_a(y)=(a-1)y+(2-a).                               (COLL5)
  ```

  Require

  ```text
  y!=1,
  tau,y,A_a(y),B_a(y) in mu_N,
  tau^4 y A_a(y)B_a(y)=P^(-1).                       (COLL6)
  ```

  Before reconstructing `tau`, apply the scale-free two-bit gate

  ```text
  Z_inf=P y A_a(y)B_a(y),
  Z_inf^(N/4)=1,                    N/4=2^38.         (COLL7)
  ```

  Reject a shard immediately when `(COLL7)` fails.  Passing `(COLL7)` says
  only that a fourth-root scale exists in `mu_N`; the canonical `tau` must
  still be reconstructed and checked against `(COLL6)`.

  Four scalar forty-squaring traces check the memberships.  The two choices
  of `q` are one orbit under
  `(a,y,tau)->(-a,y^(-1),tau y)` and must not be duplicated.  A checker can
  reconstruct

  ```text
  u=a+(y+1)/(y-1),       d=tau(y-1)/2,
  b_(2H-3)=du,            c_(H-3)=d/q
  ```

  and compare them with the canonical outputs before retaining the shard.
  Any future classification should attack this three-affine-image subgroup
  intersection by a coverage-proved algebraic or character-sum method.  Raw
  enumeration of `y in mu_N` is forbidden, and an exact order-32 passing
  control shows that `(COLL5)--(COLL6)` alone are not contradictory.

  The proved all-field Stepanov specialization gives the exact a priori cap

  ```text
  #{y in mu_N:A_a(y),B_a(y) in mu_N}
    <=355106851<2^29.                                 (COLL8)
  ```

  It uses `A_0=D_0=79896510`, `B_0=12902`, and the official characteristic
  lower bound `p>=31950697969885030204`; it is valid in the prime, split
  quadratic, and unitary quadratic chambers.  This cap is not itself an
  enumeration algorithm.  A sweep over all `355106851` possible retained
  values, or over all `2^40` subgroup elements to find them, is outside the
  local and current Modal budget.  Such a campaign remains a donated-compute
  request unless a pilot supplies a nonenumerative candidate generator,
  measured throughput and memory, checkpoint format, independent checker,
  and a conservative dollar ceiling below the contributor's approved spend.

  **Completed finite sieve CR-002-C2CELL-COLL-RF (reciprocal selected-
  antipodal affine shard; do not rerun).** The reciprocal field
  chamber no longer has an affine search variable. For

  ```text
  N=2^40,       p=kN-1,
  29058991<=k<=33554432,
  r=(2a-1)/3,       a^2=-2,
  ```

  the three memberships in `(COLL6)` force

  ```text
  y=-r^2=(7+4a)/9,
  A_a(y)=r,       B_a(y)=-r.
  ```

  They hold exactly when the base-field trace recurrence

  ```text
  R_0=-2/3,       R_(j+1)=R_j^2-2,       R_40=2 mod p
  ```

  passes. There are exactly `4,495,442` progression values before primality.
  Modal app `ap-Ifv7cgmA0WCon3SfgP1aSo` partitioned the inclusive interval
  into sixteen disjoint shards. It processed all `4,495,442` values, including
  composites, with exact coverage and **zero hits**. The longest shard took
  `3.13` seconds under `512 MiB`, below the registered `$0.25` ceiling. The
  positive control `N=32,p=31` passed. The launcher, banked result, sixteen
  coverage digests, and deterministic checker are registered and hash-pinned.

  This is a stronger PASS than a prime-only sieve and excludes the reciprocal
  maximal-degree selected-antipodal collision shard. No extension-field
  arithmetic, subgroup enumeration, affine scan, or canonical coefficients
  were used. Do not rerun this campaign; redirect contributor compute to the
  fixed-field, degree-deficient, or non-selected-antipodal branches.

  Shard by official field chamber, first-match branch, normalized `(s,alpha,z_t)` orbit,
  and the compressed recurrence state. Each shard must checkpoint its exact orbit
  interval, retained-count ledger, rolling hash, and every compact survivor.
  The independent checker reconstructs the two outer quadratics, verifies the
  repeated derivative weight, the Euler remainder and cube resultant, the
  endpoint determinant and half-order torsion test, the infinity-cell quartic
  remainder and derivative-collision pattern, the selected-antipodal affine
  packet when applicable, all forty source torsion recurrences, primary and
  secondary gaps, canonical span, source distinctness, and the `J` divisor or
  root-count verdict. Keep large logs and factors remotely; vendor only
  manifests, compact survivors, and checker fixtures.

  **PASS** is coverage-complete emptiness of `(COLL1)` after all retained
  gates; it removes the minimum-support one-antipodal branch but leaves
  larger support open. **FAIL** emits one complete replayable candidate and
  changes the downstream DAG according to its independently checked status.
  **INCOMPLETE** preserves exact shard coverage and has no DAG effect. There
  is not yet a compressed evaluator, coverage proof, or credible cost model,
  so no run is authorized against the remaining local Modal balance. A pilot
  must publish CPU, RAM, storage, and a conservative dollar ceiling below
  `$1`; any larger campaign is an upstream request for donated compute.

  A valuable contributor result would be a coverage-complete classification
  of these invariant and large-mismatch alternatives that also preserves
  the outer Mobius matching. Raw enumeration of `mu_N`, arbitrary four-color
  partitions, or dense construction of the four degree-`2H-3` factors is
  forbidden: none is a complete or plausibly costed algorithm. A proposal
  must first give a compressed orbit/transition representation, prove that it
  covers every coloring satisfying the ladder, publish a small-order pilot,
  and state CPU, RAM, storage, and dollar ceilings.

  **PASS** is a parameter-uniform proof or independently checked certificate
  that no exactly-one-antipodal canonical coloring passes all source and
  completion gates; it removes this complete-candidate stratum without
  asserting primary-only emptiness. **FAIL** emits one official
  characteristic and a compact formula for `c,d,B,C,w_i` and the four cells
  from which a checker reconstructs the factorization, Fourier ladder,
  negation transitions, Mobius match, and downstream cycle packet.
  **INCOMPLETE** retains exact orbit/transition coverage and hashes but has no
  DAG effect. No coverage algorithm or cost model exists, so this is an
  upstream theorem/algorithm and donated-compute request only.

  A future request must be resumably sharded by official characteristic,
  fixed/reciprocal field chamber, and normalized orbit, with a conservative
  dollar ceiling and hard memory limit. Its independent checker must replay
  all forty scalar recurrences, distinctness, both coefficient gaps, and the
  parity verdict from compact emitted certificates. **PASS** proves C2-PAR
  and routes the surviving parity packets to the already shared CR-002 norm
  interface; it does not by itself close that norm interface. **FAIL** must
  print one replayable official row, `(t,S,P)` orbit, coefficients, and a
  nonparity quartet passing both gaps.
  **INCOMPLETE** must retain exact shard/orbit coverage, hashes, and partial
  witnesses and has no DAG status effect. This pre-request is suitable for
  an upstream PR asking contributors for algorithm design or donated compute
  after the missing compressed implementation, field ledger, and pilot are
  supplied.

  **Completed CR-002-C1AI (anti-invariant source residues; do not run).**
  Frobenius comparison of the six source traces reduces every anti-invariant
  non-`R0` lift to two fixed traces: `-8` for `R1/R2` and `6/5` for
  `P1/P2`; `P0` is algebraically impossible. Modal app
  `ap-6KQ2mJjoE3Qkq7VaKqnxlZ` checked all `2,247,721` odd-`k` moduli in the
  exact positive-quadratic interval with no hit. All 16 shards completed,
  the longest took 2.957014 seconds, and the compact digest packet and
  independent checker pass. This proves that `R1,R2,P0,P1,P2` source lifts
  descend to `F_p`; it does not reject their invariant packets.

  `R0` is the only source trace invariant under `r -> -r`. Its lift variable
  has now been removed analytically: the two traces over fixed `t=r^4` are
  the roots of

  ```text
  K_t(Y)=t(Y-2)^2+4(t-1)^2,
  ```

  and scalar elimination gives

  ```text
  t(S^2-4T)^2+4(t-1)^2T^2=0,
  4t(1+tH_(4M-1)(t)^2)^2+(t-1)^2=0.
  ```

  Any future CR-002-C1N implementation must use direct `F_p` source
  arithmetic on the five descended branches and the quadratic quotient
  compiler on `R0`. It must not allocate extension-field lift shards or
  repeat C1AI. The entire primary/torsion/constant packet now reduces further
  to seven degree-`2^36` Jacobi gcds per torsion sign. Exact lift norms
  collapse the six source roles to `R0`, common `R1/R2`, `P0`, and common
  `P1/P2` families. Their torsion prefilters are literally the same
  `R_-,R_+` norm pair already requested by CR-002-C. Do not request a
  separate `c=1` norm campaign. A compatible divisor must additionally pass
  one of

  ```text
  F_R0,epsilon,
  F_R(s), F_P0(s), F_P(s),       s^2=-epsilon.
  ```

  The remaining expensive issue is compressed evaluation of the shared
  norms and then the fourteen branch-specific scalar and later Euclidean,
  fourth-power, and gcd packets, not characteristic screening or duplicated
  norm construction.
- **deleted-pair final router:**
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_nonharmonic_scalar_router`.
  After the constant ODE, Mobius router, Euclidean reconstruction, and
  harmonic exclusion, it removes `q_out` from the search. For the three
  printed pairs `(a_j,b_j)`, completion is exactly

  ```text
  4b_jT=a_jS^2,
  y=4b_j/a_j-2,       y notin {2,-2},
  y_(m+1)=y_m^2-2,       y_38=2,
  S/(1+q_out) is a nonzero square,       X^2-yX+1=0.
  ```

  The final square verdict is invariant under
  `q_out<->q_out^(-1)`. A contributor should implement three one-variable
  certifiers in `r`, not a two-variable torsion search.

  The stronger proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_nonharmonic_fourth_power_router`
  removes even that root-independent `q_out` square verdict. With
  `chi=r+r^(-1)`, the three multipliers are the explicit squares

  ```text
  h_0^2=1/(4(chi-1)^2),
  h_1^2=(chi-2)^2/(4(chi+2)^2),
  h_2^2=chi^2/(4(chi-4)^2).
  ```

  Conditional on `T=(h_jS)^2`, the final square-pencil condition is exactly
  that `T` is a nonzero fourth power. This is the implementation endpoint.

  The first implementation stage begins with the proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_coefficient_gate`,
  but its terminal quotient has now been eliminated by the stronger proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_coefficient_legendre_collapse`.
  Define

  ```text
  H_n(t)=[z^n]((1-z)(1-tz))^(-1/2),       H=H_(4M-1)(t).
  ```

  Then `sigma=S(0)=2H`, and the three first-rejection gates are exactly

  ```text
  t H^2+(chi-1)^2=0,
  t(chi-2)^2H^2+(chi+2)^2=0,
  t chi^2H^2+(chi-4)^2=0.
  ```

  The sequence has the width-two recurrence

  ```text
  2(n+1)H_(n+1)=(2n+1)(1+t)H_n-2ntH_(n-1)
  ```

  and, for `t=r^4`, the Legendre form
  `H_n(r^4)=r^(2n)P_n((r^2+r^(-2))/2)`. A contributor should attack uniform
  torsion nonvanishing or provide a coverage-proved fast holonomic,
  diagonal, or cyclotomic-resultant evaluator. Do not reconstruct `R,S,T`,
  and do not iterate `2^37-1` recurrence steps for each torsion point.

  **Deferred large run CR-002-L (recorded for contributor compute).** Put
  `n=4M-1=2^37-1` and

  ```text
  K_n(t)=4^nH_n(t)
        =sum_(j=0)^n binom(2j,j)binom(2n-2j,n-j)t^j.
  ```

  After clearing the `r` and power-of-four denominators, the three branch
  polynomials are

  ```text
  B_0(r)=r^6K_n(r^4)^2+4^(2n)(r^2-r+1)^2,
  B_1(r)=r^4(r-1)^4K_n(r^4)^2+4^(2n)(r+1)^4,
  B_2(r)=r^4(r^2+1)^2K_n(r^4)^2
         +4^(2n)(r^2-4r+1)^2.
  ```

  The exact decision is whether any admissible official split-quadratic
  characteristic `p`, source order `ord(r)|2^40`, and branch `j` has
  `B_j(r)=0`, after applying the already proved distinctness, primary-gap,
  and characteristic filters. A negative result closes the scalar-gate
  portion of the generic deleted-pair sublane. A positive result must emit
  `(p,ord(r),j)` and the minimal common factor, then pass the existing full
  scalar, trace, gcd, and fourth-power checkers before it counts as a
  survivor.

  Source torsion must be inside the elimination ideal, not applied as an
  informal post-filter. The proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_primary_legendre_torsion_necessity_fence`
  gives one exact good-characteristic `M=1` primary-gap solution for each
  `B_j`; every row retains the required nonzero next coefficient, and every
  row fails `r^32=1`. Thus the pairwise primary/`B_j` resultant has genuine
  large-prime false-route hits. A contributor output that omits
  `r^(32M)-1` does not answer CR-002-L.

  The preferred lower-degree implementation is the proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_chebyshev_gegenbauer_sign_router`.
  Put `L=2M`, `y=(r+r^(-1))/2`, `x=2y^2-1`, and
  `epsilon=r^(8L)`. The coverage-equivalent system is

  ```text
  T_(8L)(y)=epsilon,       epsilon^2=1,
  C_L^(1/4)(x)=0,
  ```

  followed by one of

  ```text
  P_(2L-1)(x)=s(2y-1),
  P_(2L-1)(x)(y-1)=s(y+1),
  P_(2L-1)(x)y=s(y-2),       s^2=-epsilon.
  ```

  There are two sign choices in each line. These six unsquared systems are
  an exact intermediate endpoint; they retain source torsion and reduce the
  branch degree relative to `B_j(r)`.

  Apply the stronger proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_trace_gcd_router`
  before an official computation. Since `t!=1` forces `x^2!=1`, replace the
  torsion equation by

  ```text
  epsilon=-1: G_epsilon=T_(2L),
  epsilon= 1: G_epsilon=U_(2L-1).
  ```

  Put `C=C_L^(1/4)` and `R=P_(2L-1) mod C`. For each `s^2=-epsilon`, the
  three branch polynomials are

  ```text
  E_(0,s)=(R+s)^2-2s^2(x+1),
  E_(1,s)=2(R+s)^2-(x+1)(R-s)^2,
  E_(2,s)=(x+1)(R-s)^2-8s^2.
  ```

  Reduce `G_epsilon` and `E_(j,s)` modulo `C`. The exact official decision
  is now whether any of the six gcds

  ```text
  gcd(C, G_epsilon mod C, E_(j,s) mod C)
  ```

  is nontrivial in an admissible characteristic. Every representative has
  degree at most `L=2^36`. A PASS must provide compact Bezout or subresultant
  certificates for all six signs and every official characteristic class. A
  FAIL must print the common factor, reconstruct `y` using `(TGR6)`, and then
  replay the retained next-coefficient and downstream filters. A contributor
  may use the larger cleared `r`-polynomials as an independent checker, but
  should not make them the primary official-scale representation without a
  measured reason.

  Apply the proved even-Jacobi norm router before implementing this batch.
  With `L=2M`, `w=2x^2-1`, replace the primary polynomial by
  `J_M^(-1/4,-1/2)(w)`, replace the two torsion factors by `T_L(w)` and
  `U_(L-1)(w)`, and replace each signed trace polynomial `A_j+xB_j` by
  `A_j^2-((w+1)/2)B_j^2`. Reduce during construction. This is coverage-
  equivalent and lowers the maximum degree from `L=2^36` to `M=2^35`.
  It does not make a dense run affordable; the benchmark, certificate, and
  spending requirements below remain in force.

  **First external shard CR-002-J0 (torsion-only characteristic sieve).**
  Before constructing any of the six signed norm polynomials `F_(j,s)`,
  decide, without materializing them, whether either of the two
  primitive-integer cyclotomic resultants

  ```text
  R_- = Res_w(J_M^(-1/4,-1/2)(w), T_(2M)(w)),
  R_+ = Res_w(J_M^(-1/4,-1/2)(w), U_(2M-1)(w)),
  M=2^35.
  ```

  Consume the proved torsion cyclotomic-norm decomposition. For

  ```text
  H_M(z)=z^M J_M^(-1/4,-1/2)((z+z^(-1))/2),
  ```

  odd-prime screening of `R_-` is exactly screening the single norm
  `Res(Phi_(2^38),H_M)`. Screening `R_+` is exactly screening the `36`
  factors `Res(Phi_(2^j),H_M)`, `2<=j<=37`; these may be checked and
  short-circuited level by level. Their odd-prime valuations are twice the
  corresponding resultant valuations. A proposed implementation should
  target these modular norm pieces directly, not recover them from `R_+`.

  Equivalently, use the proved trace factorization

  ```text
  R_+=(2M)^M product_(j=0)^35 Res(J_M,T_(2^j)).
  ```

  Each trace factor is the square root of its cyclotomic norm level up to a
  printed power of two. This lowers the largest plus-branch torsion degree
  from `2M-1` to `M`; it does not make an explicit degree-`M` resultant
  affordable. A modular implementation may choose whichever of the paired
  trace and cyclotomic forms gives the cheaper independently checked shard.

  For the minus branch, use `theta^2=2` in the official field and

  ```text
  T_(2M)=(theta T_M-1)(theta T_M+1).
  ```

  The two degree-`M` resultants are Galois conjugates and their product is
  `R_-`; at official even `M`, either one has quadratic norm `R_-`. This also
  lowers the largest minus torsion degree from `2M` to `M`. Recursive trace
  splitting may be used for bounded-memory parallel shards, but it does not
  by itself reduce total work and is not authorization to enumerate roots.

  has an official-compatible prime divisor. Clear only the known powers of
  two from the Jacobi normalization and print the exact primitive numerator
  convention. A common root of any triple in
  `(EJN7)` first requires the official characteristic to divide `R_-` or
  `R_+`, according to its torsion sign. Thus:

  - **PASS:** certified modular/cyclotomic exclusion ledgers show that neither
    resultant has an official-compatible prime divisor. This closes all six
    deleted-pair trace-gcd branches before their signed norms are built.
  - **FAIL:** print every compatible `(p,epsilon)`, a compact factor
    certificate, and `gcd(J,K_epsilon) mod p`. Only these characteristic
    shards proceed to `F_(j,s)` and the downstream scalar/fourth-power gates.
  - **INCOMPLETE:** retain proved factors, cofactors, hashes, and interval or
    congruence exclusions; make no DAG status change.

  The route-selection pilot used exact rational resultants at small `M` and
  trial division only on the first three rows. The primitive numerator bit
  lengths are

  ```text
  M       8    16    24    32
  R_-   574  2411  5475  9910
  R_+   500  2244  5248  9541.
  ```

  They track roughly quadratically at these controls. Scaling the `M=32`
  ratios to `M=2^35` projects about `1.14e22` and `1.10e22` bits,
  respectively, or about `1.4e21` bytes for either integer. This is an
  empirical route-sizing observation, not a lower bound on the official
  resultants, but it decisively route-fences explicit integer output and
  factorization: an implementation must never form `R_-` or `R_+` as an
  integer.

  Under the standard Jacobi normalization its first exact primitive
  numerators include

  ```text
  M=1: R_-=-23,                       R_+=-1;
  M=2: R_-=3^4*47*39023,              R_+=3^3*17*47;
  M=4: R_-=5^8*7^8*97*641*33247*402078190242382847,
       R_+=3*5^7*7^9*13*97*182711*258045217.
  ```

  These are normalization and positive-factor controls, not scaling
  evidence. The official implementation must instead use a doubling
  recurrence, cyclotomic norm modulo candidate characteristics, or an
  equivalent coverage-proved compressed method. It must not materialize a
  dense degree-`2^35` polynomial or either integer resultant. First benchmark
  a power-of-two ladder and report asymptotic and measured cost per
  characteristic, total CPU/RAM/storage, aggregation strategy, and an
  explicit spending cap. The checker should verify the recurrence or norm
  certificate, primitive normalization, official field-ledger coverage, and
  any surviving modular common factors independently. Without such an
  algorithm and benchmark, CR-002-J0 is a theorem/algorithm request rather
  than a compute run; it is not authorized on the low-credit Modal account.

  The deterministic small control is vendored at

  ```text
  experiments/prize_resolution/cr002_j0_resultant_pilot.py
  ```

  and replays under `tools/ramguard tiny -- python3 <path>`.

  A responsible implementation should work by power-of-two cyclotomic norms
  modulo the official candidate characteristics or a comparably
  coverage-proved batch algorithm. It must emit compact recurrence,
  subresultant, or product-tree certificates with an independent streaming
  checker. An exhaustive root-by-characteristic
  sweep is specifically out of scope: the existing interval ledger contains
  `4,495,441` congruence moduli before primality, and each field can contain
  up to `2^40` source roots. Their Cartesian product has no reasonable cost
  envelope. The official batch is unauthorized here and likely well above
  the current sub-`$1` budget. Before requesting it, contributors must publish
  a small-order benchmark, a total CPU/RAM/storage estimate, a resumable
  shard plan, and a hard spending cap. Until then this item is a
  theorem/algorithm request, not a request to start containers.

  Apply the proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_fourth_root_gcd_gate`
  before extracting that fourth root. With

  ```text
  P=2N+kappa x^2U_0^3,
  ```

  every survivor satisfies `S|P^2` and `deg gcd(S,P)>=M-1`. A contributor
  should compute `P mod S`, its square modulo `S`, and a compact gcd-degree
  certificate. A proof that the gcd degree is always smaller than `M-1`
  closes this deleted-pair sublane without a fourth-power extraction.
- **pure harmonic first sieve:** before classifying any ramification passport
  or constructing the degree-`2^39` Fermat decomposition, consume the proved
  `rate_half_list_budget_three_antipodal_harmonic_torsion_characteristic_sieve`.
  The nondegenerate harmonic lift locus is empty in characteristic zero. At
  official lift order `2^40`, all finite survivors lie in the bad
  characteristics of one explicit unit ideal. Its pruned repeated-squaring
  presentation has `126` variables, `127` equations, and maximum degree
  three. An integer identity

  ```text
  Delta_H=sum_j H_jE_j,       Delta_H!=0,
  ```

  would confine the characteristic support exactly, but it is no longer an
  authorized first computation. The `F_97`, order-16 witness
  `(x,y,w)=(27,12,75)` confirms that finite bad characteristics are real.
  More importantly, exact aspect-ratio controls give nondegenerate normalized
  harmonic counts

  ```text
  N       16  32   64  128   256   512
  count    8  64  160  640  2040  5680,
  ```

  for primes scaled like `p approximately N^1.6`. At `N=512`, the count is
  `0.975` times the random main term `N^3/p`. The official relation
  `N=2^40`, `p approximately 2^64=N^1.6` has the same aspect and random main
  term about `2^56`. This is route-selection evidence, not a theorem about
  official primes, but it makes a characteristic-exclusion-only certificate
  unlikely to close the branch.

  Do not launch the `126`-variable Nullstellensatz computation merely to hope
  that its integer has no official divisor. First provide either a theorem
  showing official-aspect harmonic scarcity, or a certificate algorithm that
  couples harmonic lifts directly to the Fermat/passport equations. A
  surviving official
  characteristic must print `(p,x,y,w)`, replay the six distinct-square
  inverses and all `40` squarings, and only then proceed to the Fermat tests.
  The exact small control is
  `experiments/prize_resolution/rate_half_pure_harmonic_aspect_pilot.py`.

  The proved
  `rate_half_list_budget_three_antipodal_pure_harmonic_binary_quartic_norm_gate`
  now replaces relabelled cross-ratio tests by one support invariant. For the
  split deleted quartic `D`, its harmonic-lift resolvent is the product of the
  cubic binary-quartic invariant over eight sign classes. It is a symmetric
  degree-`24` polynomial in the four roots of `D`. Three iterated quadratic
  norms evaluate it exactly, and its factorization through the three harmonic
  pairings gives a short radical-free base-field formula. A guarded attempt
  to print the full symbolic expansion reached the tiny-local wall limit;
  this does **not** create a contributor compute request. The pairing norm is
  already the exact certificate, while a large coefficient expansion would
  neither exclude a support nor couple it to the Fermat equation.

  A valuable external harmonic computation must instead eliminate this
  compact support norm together with `Q=B^4+Z^4` or with one of the proved
  Euler/passport packets. Before launch it must provide a finite complete
  family, a succinct representation that avoids degree-`2^39` coefficient
  arrays, a measured pilot, total cost and storage ceilings, and a checker
  that emits either a Bezout/nonexistence certificate or a replayable matched
  support. Until such a coupling is specified, this remains a theorem and
  algorithm request rather than an authorized large run.
- **decision:** classify the saturated algebraic locus on which four
  pairwise-coprime monic quadratics `P_i=X^2+u_iX+v_i` satisfy

  ```text
  dim_(F(X^4)) span {1/P_0,1/P_1,1/P_2,1/P_3}=2.
  ```

  Determine whether the nondegenerate locus consists only of the antipodal
  component `u_0=u_1=u_2=u_3=0`, up to the exact scaling and permutation
  symmetries that preserve `F(X^4)`, or print every additional component.
- **algebraic input:** form `P=product_i P_i`, decompose each `P/P_i` in the
  basis `1,X,X^2,X^3` over `Z[u_i,v_i,Y]`, and impose every coefficient in
  `Y` of every `3 x 3` minor. Saturate by `2`, the four constant terms, the
  four discriminants, and all pairwise resultants. Any further normalization
  must come with a proved coverage map.
- **bounded pilot:** the complete pairing census over `F_13` has `50,856`
  rank-four, `1,104` rank-three, and `15` rank-two cases; all rank-two cases
  are antipodal. It runs in a few seconds with negligible memory and is
  vendored as an audit, but it is not a characteristic-free classification.
- **downstream posedness:** the antipodal component is already nonempty at the
  first nonconstant quotient boundary (`d=8` over `F_97`): an exact
  `26,880`-assignment census finds `192` algebraically valid Möbius-graph
  pencils.
  At arbitrary scale the proved descent and weld reduce it to

  ```text
  product_i(R+a_iS)=kappa (Y^d-1)/product_i(Y-a_i^2).
  ```

  Therefore an antipodal-only component classification does not close the
  rate-half node; it identifies this quartic norm equation as the remaining
  official-scale rigidity problem. Any follow-on symbolic attack on that
  equation must retain the odd-degree primitive condition and may discard
  quotient-pullback and four-coset components by theorem, with the discarded
  ideal factors named explicitly in its certificate. It must also parameterize
  only degree-drop directions in `2^36-2<=v<=2^37-2`; constant and low-degree
  translation components have already been excluded analytically. Split the
  outer-parameter ideal by `e_2`, then `e_3`: every `e_2=0` component must
  impose `v>=(2^38-4)/3`, and the `e_2=e_3=0` component must impose
  `v=2^37-2` together with the exact linear-residual Wronskian identity from
  the outset. In that pure component, require `U,V` squarefree and saturate
  away every branch with two roots of `UV` in `Z(D) union {0}`. None of the
  `192` exact `d=8` positives even has centered `e_2=0`.

  At the generic floor `v=2^36-2`, impose the exact linear identity

  ```text
  dDU-Y(D'U+4DU')=t_0+t_1Y
  ```

  and saturate away branches where `U` has two repeated, deleted-divisor, or
  zero roots. At the intermediate floor `v=(2^38-4)/3`, impose the analogous
  quadratic identity and saturate away branches with three such roots. Above
  either floor, separate components by the exact residual degree
  `r+4-q(r-v)`, which rises by `q` per added degree of `V`. A contributor run
  that omits these identities is not solving the posed downstream problem.

  The boundary identities now admit a stronger elimination and this should be
  used before introducing any coefficients of the official-degree `U`. Put

  ```text
  E(z)=product_(i=0)^3(1-b_i z),
  E(z)^(-1/4)=sum_(m>=0)a_mz^m,       b_i^d=1,
  s=2^37,       d=2^39.
  ```

  The monic `U` is uniquely the reverse of the truncation through `a_(s-1)`.
  A generic-boundary solution requires `a_s=a_(s+1)=0` and
  `a_(s+2)!=0`; an intermediate-boundary solution requires `a_s=0` and
  `a_(s+1)!=0`. The coefficients obey

  ```text
  4m a_m=-sum_(j=1)^4(4m-3j)eta_j a_(m-j),
  E=1+eta_1z+eta_2z^2+eta_3z^3+eta_4z^4.
  ```

  A valuable contributor-scale follow-on is an exact compressed
  nonvanishing/component certificate for these gaps on four distinct
  order-`d` roots, modulo common scaling and permutation, with the centered
  outer `q=2` and `q=3` conditions retained through the `a_i^2=b_i` lift and
  Möbius weld. PASS excludes the corresponding boundary; FAIL must print an
  admissible finite field, four roots, square-root lift, outer parameters, and
  replayable recurrence values. A point sample or a linear scan through
  `2^37` recurrence steps has no completeness claim. Use a compressed
  algebraic-series, diagonal, resultant, or cyclotomic representation and
  provide its coverage proof before a large run.

  In the generic `q=2` branch, the primary gap is only half of the posed
  certificate. Set `B=sum_(m=0)^(s-1)a_mz^m`, `h=2^36+1`, and

  ```text
  J=z^(-2h)(E^(-1)(1-z^d)-B^4)/B^2,
  P=(J/J(0))^(1/2),       P(0)=1.
  ```

  The normalized reverse of `V` is fixed by `P mod z^h`, and its degree
  `h-3` forces `[z^(h-2)]P=[z^(h-1)]P=0`. A generic-boundary PASS must exclude
  the simultaneous four vanishings

  ```text
  a_s=a_(s+1)=[z^(h-2)]P=[z^(h-1)]P=0,
  ```

  not merely the primary pair. A FAIL certificate must replay both nested
  series and then reconstruct the remaining outer-coefficient identities.

  The secondary series now has a cheaper exact interface. Write

  ```text
  d=8h-8,       r=2h-3,
  L=sum_(m<h)a_mz^m,       T=sum_(m<h)a_(2h+m)z^m.
  ```

  After `a_(2h-2)=a_(2h-1)=0` and `c=a_(2h)!=0`, the two secondary
  vanishings are equivalent to

  ```text
  L T=c C^2 mod z^h,       C(0)=1,       deg C<=h-3.
  ```

  The full shifted tail also satisfies the proved first-order equation

  ```text
  E'B+4EB'
    =-z^(2h-1)((zE'+8hE)T_hat+4zE T_hat'),
  ```

  whose parenthesized forcing has degree at most one. A contributor
  implementation should use this square-plus-differential gate before the
  canonical span test; it should not build the nested square root or either
  official-degree polynomial. A rejected packet may print the first failed
  square coefficient. A survivor must print the two coefficient windows,
  `c`, the normalized square root, and the two linear-forcing coefficients.

  Before the canonical span, apply the generic Euler divisor gate. Reverse
  the canonical truncations to monic `U,V`, form the linear residual

  ```text
  T=dDU-Y(D'U+4DU'),
  ```

  write `T=t_1(Y-tau)`, and first apply the scalar norm gate

  ```text
  t_1^2V(tau) in (F^*)^3.
  ```

  For a base field of order `q=1 mod 3`, certify this by exponentiation to
  `(q-1)/3`; when `q=2 mod 3`, skip it because cubing is bijective. A scalar
  rejection certificate needs only the canonical field, `t_1,tau,V(tau)`,
  and the cubic-character value.

  Next compute

  ```text
  N_T=Res(V,T),       N_Q=Res(V,(Y^d-1)/D).
  ```

  Require `N_Q` to be a fourth power and require the exact coupling

  ```text
  N_T^4N_Q^3=d^(4v).
  ```

  Use subgroup products or compressed resultants; do not expand the
  degree-`d-4` quotient. The certificate prints both norms, their character
  values, and the coupling residual. A coupled scalar survivor must then
  certify

  ```text
  (TU^3+d) mod V=0.
  ```

  Evaluate `U^3 mod V` in a compressed quotient-algebra representation and
  multiply by the linear `T`; do not materialize `TU^3+d`, whose degree is
  `6*2^36-2`. A remainder rejection certificate prints a hash-pinned nonzero
  remainder. Passing either gate is only a necessary-condition hit and
  continues to the span and split/Mobius stages.

  Shard any contributor implementation by the proved maximal-field character
  table. Over the ambient field, the fourth-power test is active in every
  branch. The cubic test is active in every quadratic-extension branch and in
  the prime-field `p=1 mod 3` branch; only prime-field `p=2 mod 3` packets
  skip it. A specialized packet whose data have been proved to descend from
  `F_(p^2)` to `F_p` must recompute both characters over `F_p`. The shard
  manifest must name the field in which each character was evaluated.

  There is now an exact deterministic reconstruction for that last step. Put

  ```text
  Q=(1-z^d)/E,                 Rbar=z^(-2h)(Q-B^4),
  alpha=Rbar(0),               Cbar=P mod z^h,
  S=Rbar-alpha B^2Cbar^2,
  X=z^hBCbar^3,                Y=z^(2h)Cbar^4.
  ```

  A complete generic candidate must satisfy `S=beta X+gamma Y`, where
  `beta=[z^h]S` and `gamma=[z^(2h)](S-beta X)`, and the centered quartic
  `W^4+alpha W^2+beta W+gamma` must split into four distinct parameters with
  the Möbius matching to square-root lifts of the `b_i`. The contributor run
  should therefore stream-reject in this order: primary gaps, secondary gaps,
  Euler cubic norm, Euler fourth norm, norm coupling, Euler remainder, full
  span equality, quartic splitting, Möbius matching. It must use compressed
  reversals and never materialize or retain official-degree `U,V` coefficient
  arrays.

  Common subgroup scaling preserves the certifier, so normalize one `b_i=1`;
  quotient by permutations as well. The certificate must include the inverse
  orbit-coverage counts. PASS means every normalized orbit rejects at one
  named stage. FAIL prints the first complete passing orbit and all compact
  canonical data. Prefix agreement in the span test is not a PASS.

  A bounded order-64 pilot (`ap-wLXZpGxaBiBlZ1NZ3MP14e`) exhausts all
  `C(64,4)=635376` quadruples over each of the first eight primes above the
  deliberately strong threshold `p>=64^2`, `p=1 mod 64`. It finds no primary
  double gap, although six fields contain between `64` and `192` single gaps.
  The `p=193` positive control reproduces all `64` members of the known
  double-gap scaling orbit and already has `p>d`. The square threshold is not
  a uniform official hypothesis: the maximal-row quadratic field branch has
  only `p>2^64` at `d=2^39`. The
  hash-pinned result and checker are
  `experiments/prize_resolution/rate_half_list_order64_primary_gap_result.*`.
  Do not turn this into a large fixed-order prime sweep: no proved transport
  makes additional order-64 fields complete for the official growing-order
  question. The valuable large request is the compressed, coverage-proved
  simultaneous-gap/span certificate above.

  A final bounded order-128 route pilot
  (`ap-K60XbR1aXkETENbT2n7A4b`, with orbit classifier
  `ap-CxjRuOXnLkrszE6llB1U4m`) exhausts all `C(128,4)=10668000`
  quadruples in each of the first eight split prime fields. Only `p=257` and
  `p=641` contain primary double gaps, with `192` packets apiece, and no
  packet passes the secondary two-window gate. Modulo common subgroup scaling,
  each positive field has one orbit of size `128` and one orbit of size `64`;
  the size-`64` orbit is two deleted antipodal pairs. The hash-pinned evidence
  packet is `experiments/prize_resolution/rate_half_list_order128_two_window_result.*`.
  This is the last justified raw fixed-order sweep. It selects a parity-
  reduced one-parameter sublane for algebraic treatment but supplies no
  transport to official order. Contributors should spend additional compute
  only on the coverage-proved symbolic request above, not on more primes or
  larger fixed orders.

  That sublane now has a proved exact router. If the deleted roots are two
  antipodal pairs and `d=16M`, normalize their squared ratio to
  `t in mu_(8M)\{1}`. One primary and one secondary zero are automatic; the
  remaining gate is `F_(2M)(t)=G_M(t)=0` with `F_(2M+1)(t)!=0`, where the
  `F_j` obey a second-order recurrence and `G_M` is one terminal coefficient
  of a length-`M+1` square root. A useful symbolic contributor subtask is a
  characteristic-explicit Bezout, resultant-factor, or torsion-nonvanishing
  certificate for this pair at symbolic `M`. A table of fixed `M` gcds is not
  the requested output and does not authorize a large recurrence campaign.

  The complete canonical survivor has a still stronger exact interface.
  Parity forces `beta=0` and gives

  ```text
  (1-w^(8M))/((1-w)(1-tw))
   =(B_0^2+lambda w^(2M+1)C_0^2)
    (B_0^2+mu     w^(2M+1)C_0^2),
  ```

  with two coprime degree-`4M-1` factors partitioning the undeleted torsion
  roots. This two-cell primitive square-pencil classification is the preferred
  contributor subtask: determine every possible root-cell partition under
  the displayed form, then impose the existing nonperiodic and Möbius-matching
  gates. The inverse-root cells have identical Fourier moments through
  frequency `2M`, and their first difference at `2M+1` is exactly
  `-(2M+1)(lambda-mu)`. A symbolic classification or prefix-flatness
  transcript has a DAG outcome; enumerating the `8M` roots or constructing
  official-degree factors does not.

  A proved primitive-resultant bound now removes the prime-field and nonsplit
  quadratic branches from this deleted-pair subtask. Any contributor
  classification should therefore work only in the split quadratic branch
  `q=p^2`, `p=1 mod 2^40`. A campaign covering either eliminated branch is
  obsolete. All quotient-pencil factors, outer parameters, and Möbius data in
  the surviving branch descend to `F_p`; an implementation should use
  `F_{p^2}` only for the full evaluation-domain check. The ordinary four-root
  orbit and the non-generic boundary strata remain separate CR-002 work.

  On the deleted-pair generic sublane, eliminate the generic direction before
  any CAS component calculation. In original half-degree coordinates every
  complete packet has

  ```text
  D=D_0(Y^2),       U=YU_0(Y^2),       V=V_0(Y^2),
  (16M-4)D_0U_0-2xD_0'U_0-8xD_0U_0'=kappa.
  ```

  For fixed monic quadratic `D_0`, the displayed constant-forcing ODE has at
  most one monic polynomial solution `U_0`; its coefficient recurrence has
  one terminal equation. Generate `U_0` from that recurrence and reject at
  the terminal equation before introducing `V_0,lambda,mu`. Preserve the
  forced simple root `U(0)=0`, but saturate away every second repeated,
  deleted-divisor, or zero root. A contributor transcript that allocates an
  independent official-degree `U`, or saturates away the zero root, does not
  cover the proved sublane.

  The outer ratio is no longer a free scalar either. Normalize the four
  deleted-root lifts to `(1,iota,r,iota r)`, put `q_out=mu/lambda`, and split
  the classifier into exactly the three reciprocal branches

  ```text
  r^2(1+q_out)^2=4q_out(r^2-r+1)^2,
  (r-1)^4(1+q_out)^2=4q_out(r+1)^4,
  (r^2+1)^2(1+q_out)^2=4q_out(r^2-4r+1)^2.
  ```

  For fixed `r`, each branch determines at most one unordered
  `{q_out,q_out^(-1)}`. Do not enumerate 24 point matchings and do not divide
  by `1+q_out`: the harmonic `q_out=-1` cases are retained by the cleared
  router equations. The official harmonic-exclusion theorem then removes
  all of them: app `ap-YVKd2kCRyMVnpUDLR9id5x` checked every one of the
  `4,495,441` exact characteristic congruence classes with no trace-recurrence
  hit. Allocate no `q_out=-1` shard. Impose `q_out^N=1` before any remaining
  polynomial solve; the two monic root-cell factors prove this from their
  constant terms.
  A complete contributor certificate should identify the selected pairing
  branch before applying the remainder-square router.

  In fact, do not solve for either of those objects. Once the ODE has produced
  `U_0`, form

  ```text
  Q=(x^N-1)/D_0,       A=xU_0^2,       R=Q-A^2.
  ```

  For `q_out!=-1`, Euclidean division `R=AS+T` is a complete router. Do not
  retain `q_out` as a variable. For pairing `j`, impose the exact identity
  `4b_jT=a_jS^2`, recover `y=q_out+q_out^(-1)=4b_j/a_j-2`, and apply the
  38-step trace gate above. The valuable contributor task is a compressed,
  coverage-proved uniform rejection of these three one-variable tests,
  followed by one exact fourth-power certificate for `T`. Allocating
  coefficients of `V_0`, sampling square prefixes, materializing `x^N-1`,
  sharding harmonic data, constructing `q_out`, duplicating reciprocal roots,
  or running the old polynomial-square test is obsolete.
  Before allocating full Euclidean data, reject at `(CCG3)` using the one
  terminal reversed-quotient coefficient. Only then reject unless `S|P^2` and
  `deg gcd(S,P)>=M-1`; compute these through modular remainders rather than a
  dense square. A PASS certificate for uniform nonexistence may consist of a
  coverage-proved strict gcd upper bound on all three scalar branches.

  The intermediate `q=3` floor now has a root-free preferred endpoint. In
  original coordinates form the canonical `U`, the exact quadratic residual

  ```text
  T=dDU-Y(D'U+4DU'),
  P=TU^3+d,       W=T'U+3TU'.
  ```

  **CR-002-I: RESOLVED ANALYTICALLY; DO NOT RUN.** Define

  ```text
  A=4YDT'+3T(dD-YD'),       J=dA^3+27T^7.
  ```

  The exact identity `4YDW=UA-3T^2` proves

  ```text
  gcd(P,W)|J,       deg J=18.
  ```

  But a survivor would force `deg gcd(P,W)>=(2^38-4)/3`. Hence the maximal
  intermediate boundary is empty. No holonomic, subresultant, modular, dense,
  or official-field run is needed; contributors should spend no compute on
  CR-002-I.

  The same annihilator closes the first higher-degree band. If
  `t=deg T=3v-2r+4>=5`, then `deg J=7t`, so a survivor requires

  ```text
  10v>=7r-14,       v>=96,207,267,429.
  ```

  Do not run any intermediate experiment for
  `v<=96,207,267,428`; all `4,581,298,449` degrees from the official floor
  through that endpoint are proved empty. The interval above
  `96,207,267,429` is not yet a ready large-compute request: first derive a
  new compression or annihilator that can decide degrees where `7 deg T`
  reaches `v`.

  The compact Hensel certifier remains below only as an audit trail and small
  analogue decoder. With `h=(2^37+1)/3`, form

  ```text
  Rbar=z^(-3h)(Q-B^4),       theta=Rbar(0),
  H=Rbar/(theta B),          C_*=H^(1/3),
  Delta=[z^(h-1)]C_*^2/B,   kappa=[z^(2h-1)]C_*,
  Delta_1=[z^h]C_*^2/B,     kappa_1=[z^(2h)]C_*,
  Delta_2=[z^(2h)]C_*^2/B,  Gamma_1=[z^h]C_*^3/B^2,
  kappa_2=[z^(3h)]C_*,       Delta_3=[z^(3h)]C_*^2/B,
  Gamma_2=[z^(2h)]C_*^3/B^2, Xi_1=[z^h]C_*^4/B^3,
  kappa_3=[z^(4h)]C_*.
  ```

  Stream-reject `Delta=0,kappa!=0`. If `Delta!=0`, test only the unique
  `u=3kappa/Delta` and require
  `u^2-uDelta_1+3kappa_1=0`. If `Delta=kappa=0`, test only the at-most-two
  base-field roots of `X^2-Delta_1 X+3kappa_1`; there is no longer a
  parameterized scalar branch. Reduce

  ```text
  81kappa_2-27uDelta_2+27u^2Gamma_1-35u^3
  ```

  modulo that monic quadratic and apply the printed linear gate `A u+B=0`.
  If `A!=0`, test only `u=-B/A`; if `A=0,B!=0`, reject. Only `A=B=0`
  reaches the next gate. Reduce

  ```text
  243kappa_3-81uDelta_3+81u^2Gamma_2-105u^3Xi_1+154u^4
  ```

  by the same quadratic and apply `C u+D=0`. On `A=B=0`, if `C!=0` test
  only `u=-D/C`; if `C=0,D!=0`, reject. Two roots remain only on
  `A=B=C=D=0`. A survivor must make the unique solution of

  ```text
  H=C_u^3(1+u z^h C_u/B)
  ```

  a polynomial of degree at most `2h-2`. The exact cube-part form is likewise
  retained for audit and reuse outside the now-closed maximal boundary:

  ```text
  Rbar=theta C_u^3(B+u z^hC_u),
  C_u^2 | gcd(Rbar,Rbar'),
  C_u | gcd(Rbar,Rbar',Rbar'').
  ```

  For each normalized cube divisor `C`, the exact cofactor test is

  ```text
  Rbar/(theta C^3)-B=u z^hC.
  ```

  Do not materialize dense official-degree polynomials or extend the Hensel
  coefficient hierarchy one term at a time. The degree-eighteen annihilator
  has already rejected every official maximal-intermediate candidate before
  this cofactor or its split/Mobius matching can arise.

  The pure `q=4` floor must use the harmonic-Fermat router. Choose lift signs
  `a_i^2=b_i`, quotient by common scaling and relabel to a harmonic ordering,
  then normalize `a_0=1` and generate

  ```text
  w=(2x-y(1+x))/(1+x-2y),       x^(2d)=y^(2d)=w^(2d)=1.
  ```

  Reject equality or antipodality among the four lifts. For every surviving
  orbit, test the exact coprime decomposition

  ```text
  Q=(1-z^d)/E=B^4+Z^4,
  B(0)=1,       ord_0Z=1,       deg B,deg Z<=2^37-1,
  ```

  together with the proved squarefree and linear-Wronskian constraints.
  Harmonicity itself is not a rejection stage: complete lift-subgroup scans at
  orders `16,32,64,128` already contain `4,40,500,3660` normalized harmonic
  sets. PASS must exclude the matched Fermat decomposition for every harmonic
  orbit; FAIL prints the lift orbit, `B,Z`, factor assignment, and Wronskian
  replay.

  Equivalently, and preferably for implementation, evaluate the proved
  binary-quartic support norm before selecting an ordering. A nonzero norm
  rejects all eight lift-sign classes at once. A zero norm prints one
  vanishing invariant factor and only then enters the Fermat and passport
  checks. Do not request or materialize the expanded degree-`24` symmetric
  polynomial; the three radical-free pairing norms, or independently the
  three-step quadratic-norm transcript, are the canonical certificates.

  The proved harmonic spectral quadratic gate now couples this test directly
  to the Euler reconstruction. If

  ```text
  D_Phi=(Y^2-SY+q)(Y^2-TY+u),
  ```

  one short difference-of-squares expression in `S,q,T,u` is exactly the
  eight-sign norm for that pairing; test the three quadratic splittings after
  the degree-four spectral gcd and fourth-power quotients. A contributor
  implementation should use this combined packet. Separate lift searches,
  cross-ratio scans, and support-resultant expansions are now redundant and
  should not be proposed as large runs.

  The complete `d=8,16` toy pilot finds no combined survivor in seven
  admissible field rows. Do not extrapolate this into a raw larger-order
  fleet: its `d=16` fourth-power reconstruction relies on `r=3<4`, where the
  first three coefficients determine `B` before `Z^4` begins. A contributor
  request at larger `r` first needs a complete uniform reconstruction or
  recurrence that resolves the overlapping `B^4` and `Z^4` coefficients.

  Convert every pure candidate to the exact Euler ramification packet before
  any official-degree coefficient elimination:

  ```text
  T=dDU-Y(D'U+4DU'),       C=4YD V'+V(YD'-dD),
  TU^3+d=e_4V^3C,
  T'U+3TU'=V^2L,          deg L=1.
  ```

  Verify the equivalent derivative identity
  `(TU^3)'=U^2V^2L`. Reject a nonlinear `L`, a second repeated-factor
  defect, or a critical value outside `{0,-d,(TU^3)(root(L))}`. A positive
  packet should encode the factorization and the linear critical factor,
  rather than materialize a dense second-derivative Wronskian. The remaining
  classification must still retain `D`, the harmonic lift matching, and the
  Fermat factor assignment.

  Apply the proved ramification-passport router next. Check the exact weld
  `Lambda=dL`, then label the packet as one of: `generic`, `U-T`, `double-T`,
  `V-C`, or `double-C`. The first is an almost-Belyi family with one moving
  simple branch value; the other four are exact Belyi passports. An
  official-degree enumeration of covers with these passports is not an
  authorized or useful large run. A valuable contributor computation would
  instead produce a symbolic uniform parametrization or recurrence that keeps
  the harmonic lifts and deleted quartic visible, with an independent
  coverage proof. Record such a proposal here with a cost estimate before
  launching it.

  For any proposed symbolic passport family, do not allocate `D,U,V`
  independently. From `Phi=sum phi_mY^m`, form the succinct Euler lift

  ```text
  S=1+sum_m phi_m/(d-m)Y^m
  ```

  and certify `deg gcd(S,Y^d-1)=4`, together with the two fourth-power
  quotients `(Y^d-1+S)/D` and `-S/D`. A contributor run is valuable only if
  it implements these operations on a recurrence, straight-line program, or
  comparably succinct cover representation and prints an independently
  checkable coverage certificate. Materializing `2^39` coefficients or
  launching a generic dense gcd is explicitly out of scope.

  Do not launch a raw harmonic-pair enumeration at official order without a
  compressed subgroup router and an orbit-coverage certificate.
- **required certificate:** a Groebner/regular-chain/primary-decomposition
  transcript over `Z[1/2]` or a justified characteristic-zero base; explicit
  saturated component ideals; nondegeneracy witnesses; and, for each claimed
  symmetry reduction, a machine-checkable inverse coverage map.
- **checker:** an independent exact script must verify ideal containment in
  both directions after saturation, replay every component parametrization,
  and check that discarded components lie in a named discriminant or
  resultant divisor. Probabilistic modular reconstruction alone is
  insufficient.
- **DAG outcome:** an antipodal-only result proves that the welded quartic norm
  equation is the complete direct fiber-four residual. Additional components
  become a finite, printed list of separate algebraic subcases and must each
  be transported to its own subgroup-product equation. A counterexample to
  the proposed component list repairs the classification target but does not
  affect the already-proved rank-three and rank-four exclusions. On the
  antipodal component, a useful next certificate must address the primitive,
  nonperiodic high-degree locus; a quotient-periodic or low-degree-translation
  census has no remaining DAG outcome. A pure-quartic certificate with
  `v<2^37-2` is likewise incompatible with the proved Wronskian theorem.
  Generic- or intermediate-boundary output with residual degree other than
  one or two, respectively, is incompatible with the proved reverse-residual
  theorem and must be treated as a generator or normalization error.
- **execution shape:** use a contributor machine or capped remote CAS job;
  checkpoint elimination stages and export compact bases plus hashes. Do not
  materialize large artifacts in WSL.
- **estimated resources:** unknown until a modular pilot; potentially
  multi-gigabyte and therefore outside the current laptop and sub-`$1` Modal
  policy.

A raw `d=16` or larger antipodal point census is not a third compute request.
The `d=8` positives already defeat scale-free emptiness, while a finite larger
negative cannot certify the official `d=2^39` quartic norm equation. Such a
run becomes responsible only after a proved lifting/classification theorem
makes a bounded range complete.

## CR-004: WCL terminal four-slot classification

- **2026-08-06 finish-inventory authorization:** before considering a resumed
  `(1,5)` fleet, run one metadata-only inventory of the persisted
  `weight5-recursive-norm-full-v2` volume.  One CPU, 1 GiB, one container,
  270-second hard timeout and 240-second partial-output timer; expected cost
  below `$0.02`.  It validates every present batch summary and prime shard,
  reports exact coverage and unresolved-tail counts, and emits compact
  missing ranges.  It performs no norms, factoring, repair, or residual
  launch.  Full details are preregistered in
  `notes/pilots_20260806/wcl15_finish/PREREG.md`; this authorization does not
  lift the external-full guard.
  App `ap-UTEn7QKVL578dJdILqaWrp` stopped normally with a valid partial after
  serially checking 1,325 of 21,332 present summaries in 240 seconds.  It
  found no invalid record, missing prime shard, or high-gate factor; 49
  unresolved norms and maximum `v_2(p-1)=29`.  One same-ceiling retry is
  authorized with at most 64 concurrent I/O threads; a second partial ends
  the inventory route.
  Retry app `ap-glG3TjqDK6BZ7fnKLzf0qw` completed and stopped normally.  It
  validates all 21,332 summaries and prime shards: 1,365,248 covered rows,
  111 distinct unresolved norms, 14,558 missing batches, no invalid/extra
  record, no missing shard, no official-gate factor, and maximum
  `v_2(p-1)=30`.  The complete inventory is
  `notes/pilots_20260806/wcl15_finish/inventory.json`, SHA-256
  `52aaac5ba078999383d62b586007874772c1f5bef909e639d8b0fe4076df754d`.
  **Wave-1 resume authorization:** schedule only the first 5,000 indices in
  that exact missing manifest, at most 320,000 rows.  Preserve the existing
  worker/checkpoint definition: 100 containers maximum, two CPUs and 2 GiB
  each, 2,100-second function cap and 60-second per-norm factor cap.  Expected
  cost is below `$0.75`, conservative ceiling `$1.25`; no aggregation or tail
  stage.  Complete details and outcomes are in
  `notes/pilots_20260806/wcl15_finish/EASY_RESUME_PREREG.md`.  A fresh
  inventory is required before any later wave.
  Packaging-only app `ap-Zz4V2PkJVwGCxmOICMrEov` was stopped after remote
  module import failed on a relocated local-path expression.  No
  representative, norm, factor, or checkpoint was processed.  One corrected
  retry of the identical wave is authorized with no ceiling change.
  Corrected app `ap-qYbLkmB7CKxnSWjPttlp1d` completed and stopped normally:
  5,000/5,000 batches, 320,000 rows, 319,987 fully factored, 13 hard tails,
  no error or gate factor, maximum `v_2(p-1)=26`, and one honest cache hit.
  Compact result SHA-256 is
  `ba210ccadf33b43801c8d740966a6215f581d8db7e0be5fbefe780c206aad43c`.
  One post-wave metadata inventory is authorized: one CPU, 1 GiB, one
  container, 420-second hard cap and 390-second partial timer, expected below
  `$0.03`; no norm or factor work.
  Inventory app `ap-9RWWVhxlPTB2FfXKAYCCQI` completed and stopped normally:
  26,332 valid batches, 1,685,248 rows, 124 distinct hard tails, no custody
  error or gate factor, and contiguous missing suffix 26,332--35,889.  Updated
  inventory SHA-256 is
  `d948248a8c5ef50f1d5c9dcb1722217a2458cdb6282c62b5315042b643d6f030`.
  **Wave-2 authorization:** process indices 26,332--31,331 under the identical
  5,000-batch caps and `$1.25` conservative ceiling.  No aggregation or tail;
  require another inventory before the final suffix.
  Wave-2 app `ap-OhRBjzWUFxlkiyknJAjQnj` completed and stopped normally:
  5,000 batches, 320,000 rows, 319,993 fully factored, seven hard tails, no
  error/cache/gate factor, and maximum `v_2(p-1)=27`.  Result SHA-256 is
  `6bc6f5a46670cb3fcf98acf3bb7aee7af4bc63fe441603135fb904364247f0e2`.
  One metadata-only post-wave inventory is authorized under the same
  420/390-second and sub-`$0.03` ceiling before the final suffix.
  Inventory app `ap-ecfcmrOq5GeVzA86bat8zG` completed and stopped normally:
  31,332 valid batches, 2,005,248 rows, 131 distinct hard tails, no custody
  error or gate factor, and missing suffix 31,332--35,889.  Inventory SHA-256
  is `0d99871c28c6d716e3a2542fd0b003a1c1fbf63e3f7b7522257681129e8b4801`.
  **Final easy-wave authorization:** process all 4,558 remaining batches and
  291,672 rows under unchanged worker caps; expected below `$0.70`,
  conservative ceiling `$1.20`.  No aggregation/tail stage; require a final
  complete inventory.
  Final-wave app `ap-lPz2qBADvEdizYneaGoS2a` completed and stopped normally:
  4,558 batches, 291,672 rows, 291,609 fully factored, 63 hard tails, one
  cache hit, no error or gate factor, maximum `v_2(p-1)=29`.  Result SHA-256
  is `c7cc723272f72cf9693e7b0391f79063eb89bc3de977c36fbbbd8f333f694221`.
  One final all-volume inventory is authorized under the same 420/390-second
  and sub-`$0.03` metadata-only ceiling.
  Final inventory app `ap-g4Ct3WA3vwpVbtQ6jvlGgM` completed and stopped
  normally: all 35,890 batches and 2,296,920 rows, 2,296,726 fully factored,
  194 distinct hard tails, no custody error or gate factor, maximum
  `v_2(p-1)=30`.  Final easy-inventory SHA-256 is
  `98f5a0b35ceb420519ed58589047f921ef962d9eb19efe36c1f5917ac02c131a`.
  **Hard-tail authorization:** compile the exact 194-norm manifest with one
  bounded parallel-I/O container, factor those norms in at most 100 one-CPU,
  2-GiB, 420/300-second workers, and emit a tail-only aggregate.  Expected
  below `$1.50`, conservative ceiling `$3`; no retry or easy-factor aggregate.
  Full protocol is
  `notes/pilots_20260806/wcl15_finish/HARD_TAIL_PREREG.md`.
  Hard-tail app `ap-9R3y73LE4xoHSDpoqUXGoN` completed and stopped normally:
  exact 194-norm manifest, 193 completely factored, 399 distinct primes, no
  gate factor, maximum `v_2(p-1)=17`; tail index 191 timed out at 300 seconds.
  Partial-result SHA-256 is
  `026fbd0d5665bc855bfcdd56f54b33bbea2b2a563aa98c79daf6e4f042ac0f4b`.
  One targeted ten-worker GMP-ECM/PARI/FLINT comparison for that 269-bit norm
  is authorized with 330/300-second caps and conservative `$0.50` ceiling;
  no broad retry.  See `notes/pilots_20260806/wcl15_finish/TAIL191_PREREG.md`.
  Targeted app `ap-qUcK72KF9ec7cN4chlxoA9` completed and stopped normally.
  All ten workers timed out at 300 seconds without a divisor; PARI confirms
  the 269-bit integer is composite.  Packet SHA-256 is
  `11cbae528206806d411efe4e0deb9da59956335358d9afae6dd729780e1eae6f`.
  **External request CR-004-W15-TAIL191-NFS:** completely factor
  `648504938724625892617537595827566622528651020454874372151735040370465231483079169`,
  return checkable primality certificates and every `v_2(p-1)`, and report
  resource telemetry.  Full custody and required output are in
  `notes/pilots_20260806/wcl15_finish/EXTERNAL_REQUEST.md`.  No further Modal
  factoring is authorized without a new cost estimate.
  **Independent easy-factor custody audit:** final app
  `ap-QctfVdgXi0IsLhxDIMLR0j` validated all 35,890 summary/shard pairs in
  186.861 seconds and reconstructed 6,177,403 shard records and 4,443,651
  distinct easy factors.  It independently finds no official-gate factor,
  maximum `v_2(p-1)=30`, and maximum factor size 262 bits.  Vocabulary
  SHA-256 is
  `1abfdfddbb9a168522b9413292cff6064308f9d7a0706b1f5cf34329a0d8bc3a`;
  compact-result SHA-256 is
  `25597e973edb63c822af4a8b8b71506e4ecf68f629046aabcdda19ea6d535a31`.
  This pays exact aggregation and shard custody only.  The 4.44-million
  vocabulary requires a separately priced sharded primality/replay design;
  no broad follow-up is authorized by this result.
  **Independent replay pricing pilot:** app
  `ap-ghDRZvjFIf7BFrEw2AM46h` passed all 16 fixed groups, 128 batches, 8,152
  rows, 21,762 FLINT primality checks, 23,091 factor records, four timeout
  norms, and every candidate/factor digest.  Selector digest is
  `90fcc2b4f17e6dba7c0b8f6038bcf18baf327e828d6e4b51454d72cdec01bf14`;
  compact-result SHA-256 is
  `928b644d878aea22465248a5a4371dfe2c7b71397555126fbd7ada15a086044c`.
  It projects 18,714.830 CPU-seconds and 187.148 idealized seconds at 100
  containers.  This fails the pilot's 7,200-CPU-second auto-scale gate but is
  compatible with a separately preregistered grouped audit below `$1`; the
  pilot itself authorizes no scale-up.
  **Full independent easy replay:** initial app
  `ap-0OBpQSj0V7998tTvkzixwx` completed 99 groups and checkpointed the sole
  slow group with 15 batches left; authorized resume
  `ap-y5FDRVADCUfOqoflndTSDg` completed that suffix.  Final coverage is all
  35,890 batches and 2,296,920 rows, with 6,177,403 FLINT primality checks,
  6,528,119 reconstructed factor records, exactly 194 retained timeout rows,
  no missing/duplicate batch, and no failure.  Global custody digest is
  `975220600606e8f9fac4de09d7d350121ea04ea3de23b9e492fb0651b331e033`;
  compact-result SHA-256 is
  `04dc6160585c122a9022b922d867bde6d64967a16a41359d6c327c4f03dd5c6c`.
  The easy census is now independently certified.  Remaining work is exactly
  the 194 hard tails: independent certification of 193 primary rows and a
  complete certified factorization of tail 191.
  **Independent hard-tail certificate:** corrected app
  `ap-beZVadXTE7z94tsQiEsGZ7` verifies the content-pinned 194-row manifest,
  all 193 completed products, 400 FLINT primality checks, 399 distinct primes,
  maximum `v_2(p-1)=17`, and no gate factor.  Manifest and prime digests
  reproduce; certificate digest is
  `f218fc0a26b2ec2bc1f4084bc5b0fd1eabb58c4b96e0f21aa6729350b0be0d40`;
  compact-result SHA-256 is
  `2292b2a5fccc61fba288dc8566904237b2ce4db05a0c7a83587720512d94c5ba`.
  Tail 191 is now the sole residual of the exhaustive `(1,5)` computation.
  **Tail-191 closure:** bounded official CADO-NFS app
  `ap-gyFwY6AxmBrU0NioPlsJ5C` completed in 80.457 seconds and split the exact
  269-bit norm into 112- and 158-bit factors. Independent app
  `ap-hMfVc7KQMaSvmDtSO5a9kS` proves both factors prime, multiplies them back,
  and computes `v_2(p-1)=9,12`; certificate digest is
  `4c18195abaa5932b7528cd5bf5c4dcc820525fb4b36a3aa184f4e57746b5c876`.
  The external tail request is retired. Together with the easy replay and
  193-tail certificate, `(1,5)` is complete with global maximum factor depth
  30 and no official-gate factor.

- **2026-08-03 interrupted-census checkpoint (Codex pin `8502b105`):**
  app `ap-f8oZLbaSVpbTXtCz4cPG2Z` extended the exact `(1,5)` recursive-norm
  stream to `21,332` matched batch-summary/prime shards, covering
  `1,365,248/2,296,920` affine-Galois classes (`59.44%`).  The completed
  indices reach `21,378` with `47` holes caused by preemption or cancellation;
  coverage is counted from present shards, not from the largest index.  The
  app was stopped when a protocol audit found that the campaign exceeded the
  standing five-minute/`$1` self-authorization gate.  Workspace metered cost
  rose from `$9.73` to `$12.76` (about `$3.03`); the free-credit billed amount
  remained `$0.00`.  No aggregate or hard-tail certificate was completed and
  this checkpoint changes no DAG status.  The launchers now require an
  explicit `--external-full` acknowledgement for a complete campaign.
  Finishing the residual `931,672` classes, filling the `47` holes, resolving
  every hard norm, and producing the independent factor/primality replay
  remain an external contributor request.  Do not infer emptiness from the
  partial zero-event stream.
  Two bounded attempts to audit the partial shards also produced no result.
  App `ap-QjcAetvd1xdF4oidExtEml` used 256-file groups and hit its 120-second
  task timeout.  App `ap-doWV5zWsavWNghr1FE27uR` used 32-file groups; its
  remote tasks drained, but the client map did not return before the
  five-minute campaign ceiling and was stopped.  Metered cost rose from
  `$12.76` to `$13.77` across these attempts, far above the estimated
  sub-`$0.10` cost.  No compact result was emitted.  Do not retry a
  many-small-file Modal audit; an external finisher should aggregate while
  writing the final sharded manifest, or first compact the volume server-side
  under an independently costed request.

- **2026-07-22 powered-screen update (pin `a222b5f5`):** deterministic
  samples covered 400 `(1,5)` core orbits, 256 `(1,6)` supports, 128 `(1,7)`
  supports, and 150 `(2,7)` router orbits. They found zero events or
  candidates; the largest observed `v_2(q-1)` was 24 against the official
  gate 41. Unresolved tails are excluded only for admissible primes with
  `60000`-powersmooth odd part. These 934 samples are falsification evidence,
  not completeness evidence, and remove no orbit from any slot obligation.
  Do not request a scaled repetition: the measured orbit populations range
  from millions to billions and the fixed unit-ideal endpoints below carry
  strictly more proof value. Large complete factoring, ECM tail work, or
  integer-certificate reconstruction stays in CR-004/CR-004-X6 for a
  contributor with an accepted resource ceiling.

- **status:** `(1,5)` CLOSED; DEFERRED EXTERNAL HANDOFF for the remaining
  slots. The complete direct census is now the proof of record for `(1,5)`.
  The fixed-dimensional unit-ideal endpoints remain the preferred routes for
  the nine open extended-window cells; no further broad census is authorized.
- **canonical sizing handoff (pin `d3996995`):** the measured report at
  `notes/kernel_basis/wclp_sizing_20260719/wclp_report.md` found that the
  direct `(1,5)` stream has already banked `1,066,688/2,296,920` classes
  (`46.44%`). Finishing the remaining `1,230,232` classes is estimated at
  `250--280` CPU-hours and `$45--$60` under the report's stated, unverified
  Modal price assumptions. This is valuable contributor work because almost
  half is already paid, but it exceeds the current credit and first needs
  sharded aggregation plus a hard-tail plan. The analogous direct `(2,7)`
  census has exactly `94,652,815` candidate orbits and is a **NO-GO**:
  `33,000--39,000` CPU-hours (`$6k--$14.3k`) as measured, or an unmeasured
  optimized estimate of `10,500--14,500` CPU-hours (`$1.9k--$5.3k`). The
  former `Norm(u)`-saturation gap is now repaired by the embedding-aware
  common-root quotient in
  `dli_wcl_ell2_weight7_quadruple_cubic_prime_filter_router`; this changes
  soundness, not the route size. Do not launch it; prefer a new batching,
  quotient, or joint-obstruction theorem.
- **canonical subfamily handoff (pin `0ae71ef1`):** the later read-only
  sizing packet reports an exact Burnside decomposition of the `(1,5)`
  space and isolates the order-256 mixed-parity coset layer. Its reported
  order-64, order-128, and symmetric exclusions are only at
  probable-prime level in the committed note: the generating/factoring
  artifacts and Pocklington certificates needed for a node-grade import are
  not present in this worktree. Treat the `31,860` reported event-free
  orbits as a handoff awaiting promotion, not as a proved subtraction.
  The associated external request, **CR-004-S1**, has two ordered stages:

  ```text
  S1a  vendor the exact orbit/factor manifests for the reported 31,860-orbit
       union; replay coverage and every resultant; replace probable-prime
       labels by checkable primality certificates and classify every factor
       with q<2^256 and v_2(q-1)>=41;
  S1b  sweep the complete order-256 mixed-parity layer at modulus 256
       (243,567 affine-Galois orbits, or 243,474 only after the 93 symmetric
       overlaps have passed S1a), using exact cyclotomic norms, complete
       factor handling, resumable shards, and the same independent checker.
  ```

  The canonical estimate for S1b is `7--25` CPU-hours and `$2--$5`, so it is
  valuable contributor work but is not authorized on the current Modal
  balance. Before launching it, compare its orbit manifest with the banked
  `46.44%` production stream to avoid paying duplicate rows. Passing S1a and
  S1b closes the full coset-of-`2Z_512` subfamily (`275,145` orbits, about
  `11.98%` of `(1,5)`); it does **not** close the `(1,5)` leaf. A failed row
  must return the exact support, norm factor, official prime certificate,
  and direct finite-field vanishing check.
- **consumer:** `dli_wcl_zone_coverage`, now conditional exactly on

  ```text
  dli_wcl_slot_1_5_emptiness,
  dli_wcl_slot_1_6_emptiness,
  dli_wcl_slot_2_7_emptiness,
  dli_wcl_slot_4_9_emptiness.
  ```

  These are the four residual zero-event slots after the proved global Newton
  cutoff and the exact `(2,5)` and `(2,6)` norm-gcd closures. Deeper weighted
  levels are already removed by the cutoff; a contributor must not enlarge
  this request into a raw tower census.
- **exact decisions:** over every official ambient row with
  `q<2^256` and `v_2(q-1)>=41`, decide whether a reduced signed relation
  exists in each of the following four scopes:

  ```text
  (1,5): five terms at order 512,   sum r_i=0;
  (1,6): six terms at order 512,    sum r_i=0;
  (2,7): seven terms at order 1024, sum r_i=sum r_i^3=0;
  (4,9): nine terms at order 2048,  sum r_i^j=0 for j=1,3,5,7.
  ```

  The exact signed-support convention, reduction predicates, affine/Galois
  ownership, and charge ledger are those in
  `background/nodes/dli_wcl_zone_coverage/official_terminal_attack.md`.
  Replacing them by an unsigned subset count or by terminal-level splitting
  alone changes the problem.
- **proved preprocessing:** weight three and four at `ell=1`, weights three
  and four at `ell=2`, and all weights `w<=2ell` are already excluded. At
  `(2,5)`, exact norm gcds over all `1,514` pair orbits have maximum
  `v_2(p-1)=18`; at `(2,6)`, the recursive-norm certificate covers all
  `404,740` quotient orbits with the same maximum. These packets establish
  the accepted orbit, saturation, Pocklington, and independent-checker
  format for CR-004.
- **preferred certificate representation:** consume the proved
  `dli_wcl_fixed_divisor_straight_line_lift`. For `N=2^m`, introduce the
  successive monic quotients and remainders

  ```text
  V_0=Y,
  V_t^2=V_(t+1)+GQ_t       (0<=t<m),
  V_m=1.
  ```

  Coefficientwise this scheme is exactly isomorphic over `Z` to
  `G | Y^N-1`; it introduces no extra components. After deleting the
  deterministic below-degree squarings and substituting `V_m=1`, its four
  exact implementation sizes are

  ```text
  slot     variables   equations   maximum degree
  (1,5)        52          54            3
  (1,6)        65          66            3
  (2,7)        88          91            3
  (4,9)       114         119            3.
  ```

  Seek a checked identity `Delta=sum_a H_a E_a`, where the `E_a` are these
  sparse equations. This avoids constructing the expanded coefficients of
  `Y^N mod G`. The direct remainder ideal is an exactly equivalent fallback
  for a CAS with efficient arithmetic-circuit or quotient-ring support; it
  must not be pre-expanded in SymPy.
- **`(4,9)` base classifier:** apply the proved
  `dli_wcl_ell4_weight9_quartic_divisor_descent`; do not enumerate signed
  nine-element supports. After the unique common dilation, every relation is
  exactly a monic quartic `A` satisfying

  ```text
  G(Y)=Y A(Y)^2-1 divides Y^1024-1.
  ```

  Its four-variable direct remainder ideal is the unit ideal over `Q` and
  the pruned straight-line lift above has `114` variables and `119` cubic-or-lower
  equations. The requested complete output is an integer identity followed
  by enough certified factorization of `Delta` to classify every
  characteristic compatible with the official fields. A report that the
  ideal is generically empty, without the integer identity, is incomplete.
- **`(1,5)` and `(2,7)` base classifiers:** apply the proved
  `dli_wcl_odd_next_boundary_square_divisor_descent`. The two exact systems
  are

  ```text
  (1,5): G=Y A^2-(bY+1)^2 divides Y^256-1, deg A=2;
  (2,7): G=Y A^2-(bY+1)^2 divides Y^512-1, deg A=3.
  ```

  Their direct remainder ideals have only three and four variables and are
  unit ideals over `Q`; their sparse lifts have the sizes printed above.
  Produce a checked integer identity in either exactly equivalent
  presentation, then classify its prime divisors under the complete official
  field scope.
  These fixed ideals supersede the weight-five support stream and a raw
  seven-root orbit census as proof endpoints. Existing stream output should
  be retained only for an independent factor/counterexample cross-check.
- **`(1,6)` base classifier:** apply the proved
  `dli_wcl_ell1_weight6_even_norm_divisor_descent`. Without choosing a sixth
  root for normalization, every relation is exactly

  ```text
  G=E(Y)^2-YB(Y)^2 divides Y^256-1,
  deg E=3 monic,       deg B<=1.
  ```

  The six direct remainders generate a five-variable unit ideal over `Q`,
  and its pruned sparse lift has `65` variables and `66` cubic-or-lower equations.
  Produce and factor a checked integer identity in either presentation. This
  endpoint
  supersedes the `185,569,028`-class blind weight-six route; the engineered
  nonambient witness is a required positive cross-check for any generator.
- **route fence:** the blind affine-Galois census has `2,296,920` classes at
  weight five and `185,569,028` at weight six. The latter is not an
  authorized implementation. A weight-six or deeper run must first provide a
  simultaneous-moment, recursive-norm, sparse-divisor, or comparably
  structured quotient with a proved inverse coverage map. Sampling prime
  rows, extending the bank of first primes, or factoring unsaturated norms
  cannot prove an official slot empty.
- **first action:** the exact straight-line generator is implemented. Plain
  Singular `std(I)` over `F_32003` with one global `dp` block and Singular's
  exact elimination of all 49 auxiliaries each timed out in 240 seconds on
  one CPU and 2 GiB. Native Singular quotient reduction reached exponent
  `128`, after which the successor FLINT kernel reproduced its exact term
  sequence and completed exponent `256` in `3.7290703449980356` seconds. The
  five coefficients contain
  `183162,191699,189670,186887,185330` terms and are pinned by content hashes
  in `dli_wcl_15_flint_quotient_result.json`. Do not recompute this expansion.
  The next contributor pilot should ingest or regenerate those five
  polynomials and use F4/F5, Magma/FGb, or another compiled basis engine.
  The local msolve pilot now consumes the exact hash-pinned input. Versions
  `0.7.5` and `0.10.1` made sustained F4 progress but timed out after `240`
  and `210` seconds respectively, with no basis and no mathematical verdict.
  The canonical msolve input has size `20,721,921` bytes and SHA-256
  `c7b87cdf08b13210480aa6d6cad4a0774247328954c81757226277bca54f46cf`;
  the complete bounded record is
  `dli_wcl_15_msolve_modular_pilot_result.json`. The five-minute local
  self-authorization gate did not land, so do not fund integer reconstruction
  or retry a longer local run. **External subrequest CR-004-MSOLVE-LONG:**
  ingest that exact input in a different F4/F5 implementation or ordering,
  preferably Magma/FGb or a checkpointable msolve workflow, under a declared
  resource ceiling. Return either a modular unit basis with an independently
  replayable identity or a compatible modular point; a timeout or bare
  no-solution assertion is incomplete.
  Do not start `(1,6)`, `(2,7)`, or `(4,9)` merely because the generator is
  available; authorize them only after the smallest pilot identifies a viable
  elimination order and hard resource envelope. Separately obtain the
  canonical `(1,5)` stream manifest, if available, and compare its factors or
  survivors against the reconstructed `Delta_1`; do not rerun its support
  fleet merely to finish an obsolete proof route.
- **SymPy route fence:** capped apps `ap-gWA4UOyBSv4c8C4tqDVd84` and
  `ap-4mxCfTnbtIf2yz274On6sh` both reached exponent `64` but timed out while
  forming exponent `128`; the corrected modular run took `8.663s` through
  exponent `64`, with up to `3,212` terms in one coefficient. Removing
  integer coefficient growth did not remove the sparse multiplication wall.
  Do not retry this representation. Use the proved straight-line lift, or a
  CAS that preserves quotient arithmetic without coefficient expansion. The
  complete checkpoint record is
  `experiments/prize_resolution/dli_wcl_15_unit_ideal_pilot_result.md`.
- **msolve route fence:** app `ap-i3qnWQSZ45Vr9x0QI1FHLk` ran current
  `msolve 0.10.1` on eight physical cores and `32 GiB`. It regenerated and
  hash-checked the five polynomials in `10.428s`, then timed out after
  `210.070s` of F4 with sustained trace output but no basis. Comparison app
  `ap-k2FBfUKS9IZb5wekKPXZfg` gave `msolve 0.7.5` `240.086s` with the same
  outcome and reached a similar trace band. All containers are stopped.
  These runs neither support nor refute the unit-ideal claim; they only move
  a longer/different-engine attempt to external subrequest
  `CR-004-MSOLVE-LONG`.
- **Singular image fence:** app `ap-o5JxJJpiYoJnPSIaUkeV2b` was cancelled
  during image initialization because Debian `apt_install("singular")`
  pulled a disproportionate Sage/Jupyter/development stack. The function
  never started and no Groebner computation ran. Do not retry that image.
  The minimal Micromamba successor fixed this infrastructure failure: it
  downloaded 56 MB, built in 15.67 seconds, and started Singular. However,
  app `ap-OkljVyyM1fPvNO3JEmhAnA` then reached the clean 240-second algebra
  timeout with only `WCL15_STD_BEGIN` under the exact program hash
  `201a1f...b8e3`. App `ap-wcQeDzPB9eNSB5q2VdaTMe` also reached 240 seconds
  on the exact 49-auxiliary elimination, with only `WCL15_ELIM_BEGIN`, under
  hash `5e0f1828...5a81`. Therefore do not buy more runtime for either
  lift-based Singular route. The native quotient app
  `ap-CbRAXvnzzd9oUxuxtqRe3F` also timed out at the final exponent-256
  squaring after printing the exact through-128 term sequence
  `1,1,32,240,1881,14831,117644` under hash `c6aa3dcc...f236`. Do not buy more
  Singular runtime. The FLINT successor has now paid that sparse squaring,
  reproduced the prefix, and pinned all five exponent-256 coefficients. The
  exact launchers and records are
  `experiments/prize_resolution/dli_wcl_15_pruned_singular_pilot_modal.py`,
  `experiments/prize_resolution/dli_wcl_15_pruned_singular_pilot_result.md`,
  `experiments/prize_resolution/dli_wcl_15_pruned_singular_micromamba_pilot_modal.py`,
  `experiments/prize_resolution/dli_wcl_15_pruned_singular_micromamba_pilot_result.md`,
  `experiments/prize_resolution/dli_wcl_15_quotient_singular_pilot_modal.py`,
  `experiments/prize_resolution/dli_wcl_15_quotient_singular_pilot_result.md`,
  `experiments/prize_resolution/dli_wcl_15_flint_quotient_contributor.py`,
  `experiments/prize_resolution/dli_wcl_15_flint_quotient_result.json`, and
  `experiments/prize_resolution/dli_wcl_15_flint_quotient_result.md`.
- **required PASS certificate:** for one slot, replay its proved divisor
  bijection and verify either `Delta=sum_a H_aE_a` for the sparse recurrence
  equations or the equivalent `Delta=sum_j H_jR_j` for direct remainders.
  Factor or otherwise exclude every prime divisor of `Delta` compatible with
  the complete official field scope. The identity checker must stream every
  coefficient exactly and reject a zero `Delta`. Prime certificates,
  valuation checks, modular reconstruction primes, hashes, worker errors,
  and retry history are part of the certificate. No support-orbit coverage
  table is required once the corresponding proved bijection is consumed.
- **required FAIL certificate:** print the exact ambient characteristic or
  field order, primitive root, signed exponent support, normalization orbit,
  and all required odd moments. The checker must verify exact root order,
  reduction, official ambient inequalities, and the node-specific
  vanishings. A nonambient prime, an isolated terminal witness, or a support
  with an antipodal cancellation is not a falsifier.
- **DAG outcomes:** a PASS promotes only the corresponding slot leaf. Four
  independently complete PASS packets promote `dli_wcl_zone_coverage` from
  conditional to proved through its existing amber ceremony. A valid FAIL
  refutes that slot and the current WCL route, requiring repair at the zone
  consumer. Incomplete output changes no node status.
- **spending gate:** each slot needs a small-order or bounded-orbit benchmark,
  total CPU/RAM/storage estimate, resumable shard plan, and accepted hard
  cost ceiling. Prefer contributor machines with existing FLINT/Pocklington
  infrastructure. Do not store large factors or orbit tables in WSL; vendor
  only manifests, compact certificates, checkers, and content hashes.
  The `114`-variable `(4,9)` pruned lift may still be a very large elimination even
  though its equations are sparse; its run is a contributor compute request,
  not an authorization to consume the remaining Modal credit.
  The same prohibition covers the direct `(2,7)` census above. A contributor
  may elect to finish the banked `(1,5)` stream only with an explicit budget
  and the checkpoint/aggregation repairs in the canonical sizing report.
  For the `(1,5)` certificate route, the disposable gzip coefficient dumps
  should be regenerated from the hash-pinned kernel rather than committed.
  A PR request should ask for the modular basis transcript, peak RAM, wall
  time, engine/version, and independently checked identity. If the modular
  ideal is the unit ideal, a second explicitly costed request may seek the
  rational/integer Nullstellensatz identity and factor or exclude its
  characteristic obstruction `Delta`; if it is not, return the modular
  witness instead of scaling.

CR-004 is intentionally one grouped request because all four leaves use the
same ambient split and certificate vocabulary. Contributors may close slots
independently, but should not open four incompatible compute frameworks.

### CR-004-W49-INV: one-run inversion-symmetric classification

- **authorization (2026-07-26):** exactly one route-pricing run of
  `experiments/prize_resolution/wcl49_inversion_symmetric_groebner_modal.py`.
  One CPU, 1 GiB, one container, 90-second function cap, and 75-second
  symbolic alarm; current-rate compute ceiling is below `$0.002` before the
  small cached-image build. No retry is authorized by this entry.
- **decision:** in the `(4,9)` Pell endpoint `P(Y)=YA(Y)^2-1`, classify the
  inversion-invariant root-set stratum. Such a monic degree-nine `P` is
  anti-reciprocal, giving the four exact equations
  `[Y^i]P+[Y^(9-i)]P=0`, `1<=i<=4`, in the four nonleading coefficients of
  the monic quartic `A`. Return the complete rational lexicographic Groebner
  basis, its digest, zero-dimensional verdict, and univariate factors.
- **PASS effect:** a small zero-dimensional basis selects an exact component
  certificate and subsequent divisibility check. Positive dimension or an
  unwieldy basis fences this symmetry split and returns work to the full
  `114/119` cubic endpoint. Completion alone proves no WCL emptiness.
- **partial output:** the exact equation list and digest are printed before
  elimination. Timeout is `INCOMPLETE`; no second run, support census, or
  official-scale certificate follows automatically.
- **checker:**
  `experiments/prize_resolution/check_wcl49_inversion_symmetric_groebner.py`
  reconstructs the equations and basis independently under RAMguard.
- **attempt result (2026-07-26): `COMPLETE`.** Modal app
  `ap-uGwcJZUDyu3EvGCS3q7hKx` returned a five-polynomial, zero-dimensional
  basis in `0.151924` seconds at `86 MB` peak RSS. The degree-14 univariate
  eliminant factors as
  `c0(c0-2)(c0^3-12c0-8)(c0^3-12c0+8)(c0^3-6c0^2+8)(c0^3-6c0^2+24)`.
  Exact output is pinned in
  `experiments/prize_resolution/wcl49_inversion_symmetric_groebner_result.json`.
  The authorization is consumed. This selects a branchwise divisibility
  certificate; it does not itself close the symmetry stratum.

### CR-004-W49-INV-DIV: branchwise divisibility certificate

- **authorization (2026-07-26):** exactly one follow-up run of
  `experiments/prize_resolution/wcl49_inversion_symmetric_divisibility_modal.py`.
  One CPU, 1 GiB, one container, 90-second function cap and 85-second client
  alarm; conservative compute cost is below `$0.002` using the cached SymPy
  image. No retry is authorized by this entry.
- **decision:** start from the four anti-reciprocity equations, eliminate by
  an explicitly checked quadratic/linear resultant, and cover all six
  factors of the degree-14 eliminant. On each rational or cubic branch,
  compute `(Y^1024-1) mod (YA(Y)^2-1)` by exact quotient-ring powering.
  Return the gcd of the nine coefficient obstructions, complete prime
  factors of every denominator and obstruction gcd, and the subset meeting
  the official `v_2(p-1)>=41` gate.
- **PASS effect:** if no exceptional prime meets the official gate, mint a
  proved inversion-invariant component exclusion and attach it as evidence
  to `dli_wcl_slot_4_9_emptiness`. This closes only that symmetry component,
  not the full `(4,9)` cell.
- **FAIL effect:** an official-compatible exceptional prime becomes a finite
  exact candidate for direct reconstruction or exclusion. Positive
  reconstruction falsifies the `(4,9)` target; exclusion narrows the branch.
- **partial output:** the router and every completed branch are printed
  independently. Timeout or incomplete factorization is `INCOMPLETE`; no
  DAG status changes and no automatic retry follow.
- **checker:**
  `experiments/prize_resolution/check_wcl49_inversion_symmetric_divisibility.py`
  reconstructs the router, quotient powers, resultants, factorizations, and
  official prime filter independently under RAMguard.
- **attempt result (2026-07-26): `COMPLETE`.** Modal app
  `ap-Qzy9Pu4EwpokldlVRzyoYg` completed in `11.55593` seconds at `98 MB`
  peak RSS. Its eight exhaustive branches all have divisibility-obstruction
  gcd `1`; router and parameter denominators have prime support exactly
  `{2,3,17,19}`, with maximum `v_2(p-1)=4`. No exception meets the official
  `v_2(p-1)>=41` gate. The exact result has certificate digest
  `71f5d0e915bcad0cc510b6ea7d616096040bd34056f280133a4e64385bd79f99`.
  The authorization is consumed, and the result is banked as the PROVED
  component `dli_wcl_ell4_weight9_inversion_symmetric_exclusion`. Launcher,
  checker, and result-file SHA-256 values are respectively
  `bf476b31eccf380c7c676b7aec7f5aa7b79c4a3b666dd95b6dea97d0a106d158`,
  `925f7c28521779da15ff15cfbcffa6eb85b66fc1440b4e4f9479bd2527707121`,
  and `726a8287d8965a6640c03a2f2b42cbcdb3c53aeed7e1d23191800c778d45e356`.

### CR-004-W16-DELTA: expanded rational certificate pricing

- **attempt result (2026-08-06): route fenced.** App
  `ap-WuMWiEvupHO6w3aghjgG1f` used a minimal Singular image, two CPUs, 4 GiB,
  and a 60-second exact subprocess cap.  Packaging completed with only 11
  added packages, but repeated squaring over `Q` did not finish constructing
  the six coefficients of
  `Y^256 mod (E^2-YB^2)-1`.  No Groebner basis or lift matrix was reached.
  Exact packet and preregistration are in
  `notes/pilots_20260806/wcl16_delta6/`.
- **decision:** do not retry the expanded-remainder representation and do
  not substitute the `185,569,028`-class direct census, currently projected
  at at least 36,000 CPU-hours and roughly `$6.6k`.  The sparse straight-line
  ideal remains an exact mathematical endpoint, but a follow-up needs a new
  gate-aware structural reduction, not a longer generic-CAS timeout.
- **DAG effect:** none.  This is a representation fence, not evidence for
  slot emptiness, and `dli_wcl_slot_1_6_emptiness` remains `TARGET`.

## CR-004-X6: WCL extended-window six certificate classification

- **status:** DEFERRED EXTERNAL HANDOFF. The proved node
  `dli_wcl_extended_six_slot_sparse_divisor_endpoints` gives a finite exact
  endpoint for every C1'-r3 widened leaf. No raw support scan and no current
  Modal run is authorized.
- **decision target:** compute a checked nonzero integer Nullstellensatz
  certificate for each of `(1,7),(1,8),(2,8),(2,9),(4,10),(4,11)`, factor or
  otherwise exclude every compatible prime divisor, and thereby close the
  corresponding leaf. The six squared-root divisor forms and exact pruned
  sizes are:

  ```text
  slot     divisor                         variables  equations
  (1,7)    YA^2-B^2 | Y^256-1                  76         78
  (1,8)    E^2-YB^2 | Y^256-1                  89         90
  (2,8)    E^2-YB^2 | Y^512-1                 103        105
  (2,9)    YA^2-B^2 | Y^512-1                  99        102
  (4,10)   E^2-YB^2 | Y^1024-1                129        133
  (4,11)   YA^2-B^2 | Y^1024-1                142        147
  ```

  Every equation has total degree at most three.
- **normalisation scope correction (2026-07-26):** failure of product-one
  normalisation at even weight does not add a missing router to this request.
  The proved parity-separated form `F(X)=E(X^2)-XB(X^2)` already gives the
  exact `(4,10)` descent and converse. The six jobs above are certificate
  extractions, not descent discovery.
- **route fence:** a blind affine-Galois census has rigorous class lower
  bounds `6,426,702,047`, `400,062,202,418`, `27,065,242,005,554`,
  `3,031,307,104,622,047`, `81,607,877,807,280,797,271`, and
  `15,045,525,108,469,586,987,666` in the same order. Do not request such a
  fleet. The fixed sparse ideals are the only current complete compute input.
- **execution order:** benchmark modular Groebner or regular-chain
  elimination on `(1,7)` only. Publish basis size, degree profile, peak RAM,
  wall time, reconstruction-prime count, and a hard total cost/storage
  ceiling before another slot starts. Prefer a minimal Singular/Magma/FLINT
  image or a contributor CAS installation; do not repeat the Debian Singular
  image failure recorded under CR-004.
- **required PASS:** replay the exact parity/squared-root bijection and verify
  `Delta=sum H_aE_a` coefficientwise over `Z`; reject `Delta=0`; certify all
  prime factors or a sufficient cofactor exclusion; check `q<2^256` and
  `v_2(q-1)>=41` against every surviving factor. Record hashes, modular
  primes, failed workers, retries, and factor certificates.
- **required FAIL:** print a compatible characteristic and full coefficient
  tuple, reconstruct the antipodal-free signed roots, and check every odd
  moment, exact ambient order, reducedness, and official field condition. A
  modular nonunit basis without a reconstructed point is not a falsifier.
- **partial output:** checkpoint elimination stages and modular images.
  Timeout is `INCOMPLETE`, never `PASS`; complete work must be reusable by a
  different CAS. No cost estimate is asserted until the `(1,7)` benchmark.
- **DAG effect:** each complete PASS promotes one widened slot. All six,
  together with the four CR-004 base slots, are required by the current
  ten-slot `dli_wcl_zone_coverage` ceremony. A valid FAIL repairs that WCL
  route and may falsify the extended C1'-r3 envelope.

## CR-003: Rate-half Hankel sharp-cap component classification

- **status:** PRE-REQUEST; THE FORMER EXACT DISTANCE-THREE FACE IS CLOSED.
  Do not run on the
  current laptop or the remaining low-credit Modal account. It is not yet a
  contributor-ready numbered run under this ledger's handoff convention:
  there is no coverage-complete implementation, measured pilot, hard resource
  ceiling, or compact nonexistence certificate. The exact contract below is
  algebraic preprocessing for such a request, not authorization to search.
- **consumer:** `rate_half_band_closure`, at strict budget `B=2^39` and
  half-distance budget `B=2^39+1`.
- **official field collapse:** both budgets are prime-field only. The proved
  `rate_half_residual_prime_field_collapse` reduces `q=p^f` by LTE to
  `f in {1,2,3,4}`, then exactly excludes all `46` quadratic candidates and
  the empty cubic/quartic residue intersections. Every official shard may
  assume `F=F_p` with `p=q>2^167`. Do not allocate extension-field,
  Frobenius-orbit, generated-field, or base-field-normalization variants.
- **proved routers:**
  `rate_half_ca_hankel_strict_a3_slope_slack_ledger` and
  `rate_half_ca_hankel_half_distance_a3_slope_slack_ledger`, together with
  `rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger`. At the
  official scale the counterexample families are indexed by

  ```text
  strict:         m<=e<=floor((4m-1)/3),  0<=h<=4(e-m),
  half-distance A=3:  m+1<=e<=floor((4m-1)/3),
                                            0<=h<=4(e-m)-1.
  half-distance A=1:  s in {0,1,2},
                      m+1<=e<=floor((4m-s)/(1+s)).
  ```

  This request concerns only `h=0` for `A=3` and `ell=0` for `A=1`. In both
  `A=3` shapes the generator is a degree-`e` rational normal kernel curve of
  exact separation rank `e+1`, its norm residual has degree at most `e`, at
  least `N-e` domain rows are saturated, and every geometric component degree
  is forced by a unique possible integer chamber. The strict matrix is
  `(4m+1) x 4m` with a unique right singular block and locator degree `rho`;
  the half-distance matrix is `4m x (4m+1)` with a unique left singular block
  and locator degree `rho+1`. In the latter case the degree-`rho` split
  `Q_gamma` is a factor of the locator with one additional distinct domain
  root. The `A=1` matrix has the same dimensions but full row rank `4m`, one
  right singular block, and a fixed core `s in {0,1,2}`. Its residual
  sharp-cap and norm degree are the exact `T_max,eta` of `(A1L4)--(A1L5)`.
- **decision:** for the complete analogues

  ```text
  m in {2,4,8,16},       N=16m,
  A=3: rho=4m-1, strict m<=e<=floor(rho/3),
       half-distance m+1<=e<=floor(rho/3), T=4e+1;
  A=1: rho=4m, s in {0,1,2}, d=rho-s,
       m+1<=e<=floor(d/(1+s)), T=T_max(s,e),
  ```

  and, for each `m`, the first three prime fields in increasing order with
  `N|(q-1)` and `q>N`, decide separately for each shape whether a syndrome
  Hankel pencil exists with the designated generic rank, minimal index `e`,
  no common degree-`r` domain-split locator, exactly `T` supported finite
  slopes, and exactly the designated fixed core (`s=0` for `A=3`). The solver
  must impose the appropriate Hankel coefficient chain, not merely search
  arbitrary biforms satisfying the norm identity.

### First meaningful analogue and raw-search fence

The smallest fixture already banked has `e=1,r=3,N=16` over `F_17`; it is a
positive route fence below the proved uniqueness threshold. The next useful
distance-three analogue on the maximal `A=1,s=1,e=2m-1` face is

```text
m=2,       e=3,       r=7,       N=32,       F=F_97.
```

After multiplicative normalization fixes the core point, there are still

```text
31 omitted rows x C(30,6) exceptional supports
  = 18,407,025 (x_0,A) packets,

31 x C(30,6) x C(24,3)
  = 37,255,818,600 (x_0,A,B) support packets.
```

Allocating the `15` perfect matchings of the six roots of `A` would inflate
this to `558,837,279,000` records. These are exact lower-level candidate
counts, not resource estimates, and they make a raw support or pairing fleet
unacceptable. A future implementation must apply the quadratic-character,
matching-free even-value polynomial, triple-power, and dual row-product
routers before reconstructing matchings or slope parameters. It should group
equal field signatures and stream only survivors.

A valid first pilot must report per-gate survivor counts for every one of the
`31` normalized omitted-row shards, preserve partial counts on timeout, and
replay the existing `e=1,F_17` positive fixture before claiming that a gate is
sound. PASS here means only that the compiler exhausts the first analogue and
emits either witnesses or a checkable no-hit certificate. A no-hit result is
route-selection evidence; it cannot close the official seam. A witness may
falsify an over-strong proposed exclusion but is not automatically an
official counterexample. Until source, pilot timing, RAM/storage ceilings,
and an independent certificate checker are banked, contributors should be
asked to help implement the compressed classifier rather than donate a raw
run.

A separate strict-`A=3` `m=1` fixture is now banked in
`rate_half_ca_hankel_strict_m1_corefree_five_slope_route_fence`: its
core-free constant-rank pencil has five split slopes against cap four, and a
complete `560`-locator census finds sixteen such Hankel-compatible lines.
This fixture is rank-two/separated and therefore not a model for the official
mixed component, but any proposed generic preprocessing gate must either
accept it or name the proved `m>1` rank/non-pullback input that excludes it.
No larger strict raw census is requested: without an official-scale
mixed-component classifier it would be evidence only.

- **preprocessing contract:** enumerate only component degree packets allowed
  by `(SSL19)--(SSL20)` or `(A1L14)--(A1L15)` and summing to the corresponding
  residual bidegree. Use the exact norm residual, complementary factorization,
  and clean-column count as early rejection constraints. Quotient by
  parameter `PGL_2`, common polynomial scaling, and cyclic domain
  automorphisms only with an inverse coverage map.
  On the `A=1,s=1,e=2m-1` sharp-cap face, impose the stronger proved packet:
  exactly one component has `(r_*,e_*)=(2e_*+1,e_*)`, every residual
  component has `(r_i,e_i)=(2e_i,e_i)`, their total parameter degree is at
  most `floor(e/5)`, and the dominant component has separation rank at least
  `ceil((e+1)/(b+1))`. Do not allocate shards to rank-at-most-four models on
  this face. Its contracted middle-Hankel matrix also satisfies the proved
  exact identity `adj M=lambda*q*q^T`, with one common linear factor and no
  other projective rank drop. A shard must divide the nonzero maximal minors
  by that same `lambda` and verify every quotient `q_iq_j`; do not treat the
  cofactors as independent elimination variables. For a surviving dominant
  component, impose its exact component norm identity with residual degree
  `e-5b-1+D_*`, `D_* in {0,1}`, and its complementary factorization over at
  least `14m+5b` residual domain rows. Output that component certificate
  separately from the balanced residual components, whose norm residual
  degrees are exactly `5e_i+D_i`. Finally impose the proved two-sided weld

  ```text
  W B-B_X E_Z=Q_* K,       V B+A E_Z=-P_X K,
  ```

  with the printed degree boxes. The external decision is now classification
  of this coupled matrix factorization together with
  `adj M=lambda*q*q^T`; independent searches for cofactors, norm factors, and
  complements are obsolete on this face. The current live handoff is:

  ```text
  B_X=X_0X_1,
  QV_a+P_XW_a=P,

  D_*=0:
    QA_a+P B_a=P_XX_1,
    W_aB_a-X_1=QK_a;

  D_*=1:
    QA_a+P_cl B_a=P_XX_1,
    W_aB_a-X_1E_Z=QK_a,
    K_a(gamma_0;X)!=0.
  ```

  Every root of `X_1` has a nonzero domain trace. Either `X_0=1`, or exactly
  one of the following boundary normalizations applies:

  ```text
  b=0,D_*=1,c=1: X_1=1 and the exceptional trace is active;
  b=0,D_*=1,c=2: X_1 has one active root with delta=1.
  ```

  The `c=1` exceptional-only boundary has a stronger proved endpoint and must
  not be sent as the generic active system above. Put `E=E_Z` and
  `q_0=Q(gamma_0;X)`. Then `q_0|P_X`, and the unique polynomial

  ```text
  J=B(gamma_0;X)/q_0,       deg J=D_0-r,
  ```

  gives the exact descended system

  ```text
  B=QJ+E B_1,       A_1=A+P_clJ,
  QA_1+PB_1=P_X,
  WB_1-1=QK_1,
  VB_1+A_1=-P_XK_1,
  deg_X A_1=D_0-r.
  ```

  A contributor shard should classify this corrected complement square
  directly. It must retain the final equality: the one-degree relaxation
  from `D_0-r-1` to `D_0-r` is why the trace-free exclusion does not close
  the profile. Do not allocate the old exceptional-only active-trace system
  or claim the trace-free contradiction after silently dropping `P_clJ`.

  Normalize the infinity block before allocating any remaining coefficients.
  With `q_inf=[X^r]Q=E q_bar`, `j_inf=[X^(D_0-r)]J`, and
  `v_inf=[X^(D_0-2)]V`, impose

  ```text
  [X^(D_0-r)]A_1=P_cl j_inf,
  [X^D_0]B_1=-j_inf q_bar,
  [X^(r-1)]W=-E q_bar v_inf,
  [X^(D_0-1)]K_1=j_inf q_bar v_inf.
  ```

  Hence `A_1` and `B_1` have exact corners `(D_0-r,T-1)` and
  `(D_0,e-1)`. Eliminate those four leading coefficients from the solver.
  Do not retain the old `deg_X B<=D_0-1` box after descent: the corrected
  `B_1` has exact `X`-degree `D_0`. The optional `v_inf` may be zero.

  Before any Hankel elimination, also require the compact two-sided
  resultant certificate. With `n_X=D_0-1`, print nonzero `c_t,c_X` and check

  ```text
  Res_t(P,Q)=c_tP_X^e,
  Res_t(P,A_1)=c_t^(-1)P_X^(T-e),
  Res_X(P_X,Q)=c_XP_cl^rE^(r-1),
  Res_X(P_X,V)=c_X^(-1)P_cl^(n_X-r)E^(n_X-r+1).
  ```

  Use product trees or subresultant certificates; do not materialize all
  official fibers merely to multiply them. A failed identity rejects the
  shard. Passing all four remains only preprocessing and does not certify the
  Hankel chain or irreducibility.

  Reduce the unit-intersection calculation further. Reuse the same `c_X`,
  put `[X^r]Q=E q_bar`, and let `m=deg_XW` after checking whether the optional
  infinity coefficient vanishes. Require

  ```text
  Res_X(Q,B_1)=c_X q_bar,
  Res_X(Q,W)=c_X^(-1)E^(m+n_X+1)q_bar^(m+n_X).
  ```

  The first resultant has degree only `e-1` in the parameter and is the
  preferred common-fiber certificate. A shard with any other irreducible
  resultant factor is invalid. Do not force `m=r-1` when `v_inf=0`, and do
  not infer that `q_bar` is root-free from this identity.

  Apply one reciprocal Euclidean step before allocating any lower
  coefficients. At the proved fixed degrees put

  ```text
  F(t,Y)=Y^rQ(t,1/Y),       G(t,Y)=Y^D_0B_1(t,1/Y),
  j_infF+EG=YL,
  Delta_inf=L(t,0)=j_inf[X^(r-1)]Q+E[X^(D_0-1)]B_1.
  ```

  Require the exact compact certificate

  ```text
  Res_Y(F,L)=c_XE^(r-1),       gcd(q_bar,Delta_inf)=1.
  ```

  The complete `q_bar` factor is thereby removed before the classifier:
  any nonexceptional irreducible factor in `Res_Y(F,L)`, or any common
  factor of `q_bar,Delta_inf`, rejects the shard. Use a subresultant or
  product-tree certificate; do not enumerate official fibers. Retain the
  exceptional `E`-supported contact and continue with the Hankel and
  splitting gates, since this reciprocal descent is necessary but not an
  exclusion.

  Do not allocate `Delta_inf` as a free coefficient. With

  ```text
  a_minus=[X^(D_0-r-1)]A_1,
  ```

  impose the proved leading Bezout ledger

  ```text
  P_clDelta_inf+E q_bar a_minus=1.
  ```

  Equivalently, compute `Delta_inf=P_cl^(-1) mod (E q_bar)` and retain
  `a_minus` as the quotient certificate. Reject immediately if either gcd
  with `E q_bar` is nontrivial or the exact polynomial identity fails. This
  modular inversion is preferred to adding coefficient variables or
  evaluating every official fiber.

  Use the full reciprocal complement rather than continuing coefficient by
  coefficient. Define

  ```text
  A_vee=Y^(D_0-r)A_1(t,1/Y)=P_clj_inf+YU,
  R_X=Y^(D_0-1)P_X(1/Y),
  ```

  and require

  ```text
  FU+P_clL=R_X.
  ```

  A shard should allocate `F,U`, test the coefficientwise divisibility
  `P_cl | (R_X-FU)`, and recover `L=(R_X-FU)/P_cl`. Do not allocate the
  lower coefficients of `L` independently. Then enforce
  `E | (YL-j_infF)` to reconstruct `G`; a packet passing only the first
  divisibility is incomplete. This replacement converts the lower
  reciprocal block into interpolation and two exact divisibility checks.

  Reduce the remaining unit square before allocating any companion forms.
  With `N=D_0+r-2` and the fixed-degree reciprocals of `V,W,K_1`, introduce

  ```text
  S=(j_infW_vee+EK_vee)/Y
  ```

  and require

  ```text
  LW_vee-FS=EY^N,
  V_vee=-UW_vee-P_clS,
  K_vee=(YS-j_infW_vee)/E.
  ```

  Thus a shard allocates only `F,U,W_vee,S`, then recovers
  `L,G,K_vee,V_vee` through the triangular ledger. Reject on any of the one
  `P_cl` or two `E` divisions, on the reduced unit identity, or on a
  recovered degree-box violation. Do not create independent coefficient
  blocks for the four recovered forms. Hankel and splitting tests still
  follow this preprocessing.

  Pin the middle-Hankel factor before checking any cofactor equations. On
  this exceptional-only shard the unique omission is at `E=0`, so print one
  nonzero base-field scalar `c_H` and require

  ```text
  adj M=c_HEqq^T,
  gcd(nonzero maximal minors)=E       up to scalar,
  (adj M/E)|_(E=0)=c_Hq(gamma_0)q(gamma_0)^T.
  ```

  The final matrix must be nonzero of rank one. With `q_r=E q_bar`, its top
  row and column are zero, while globally the top-top cofactor is
  `c_HE^3q_bar^2`. Reject a different common linear factor, a zero divided
  specialization, or any additional common cofactor factor. Do not absorb
  `c_H` into `q` unless a base-field square root is supplied explicitly.
  This pinned cofactor check is the first actual Hankel gate after the
  reciprocal reconstruction.

  Replace a generic exceptional-rank calculation by the proved kernel-plane
  gate. In a local coordinate `z=E/H`, extract `M_0,M_1,q_1`; from the
  degree-`r-1` exceptional polynomial form its two padded coefficient shifts
  `u,v`. Check

  ```text
  ker M_0=span{u,v},       M_0q_1+M_1u=0,
  u^TM_1u=0,       v^TM_1u=0,       v^TM_1v!=0.
  ```

  Use implicit Hankel convolution or structured minors, not a dense
  `(r+1) x (r+1)` matrix at large analogues. The final nonzero pairing is a
  mandatory first-order crossing check: generic rank recovery without it is
  insufficient because recovery could occur at higher order. A failure of
  any displayed relation rejects the shard before lower coefficient
  elimination.

  Collapse the three pairings to scalar convolutions before any shard is
  sent to a solver. If

  ```text
  (M_1)_(i,j)=h^(1)_(i+j),
  A(X)=sum_(i=0)^(r-1)a_iX^i,
  ```

  compute

  ```text
  Theta_s=sum_(i,j=0)^(r-1)a_i a_j h^(1)_(i+j+s),
  (Theta_0,Theta_1,Theta_2)=(0,0,nonzero).
  ```

  Prefer one polynomial convolution followed by three dot products, or the
  equivalent streaming source sums

  ```text
  Theta_s=sum_x omega_x x^s A(x)^2.
  ```

  Do not materialize `M_1`. Terms at roots of `A` may be skipped. The
  `omega_x` are contracted residual weights, not necessarily the original
  error values or nonzero. A packet passing these three sums still owes every
  lower Hankel, reciprocal degree-box, and split-fiber check.

  Apply the quotient-distance router before allocating any remaining source
  weights. Modulo the moment columns at the roots of `A`, the first-order
  syndrome has support distance at least three. At distance three, print one
  canonical unordered triple `{x_0,x_1,x_2}` and recover, rather than solve
  for, its coefficients as

  ```text
  omega_i=Theta_2/
          (A(x_i)^2 product_(j!=i)(x_i-x_j)).
  ```

  The triple is unique. The proved quotient-distance gap strengthens the
  other branch from distance at least four to

  ```text
  delta_A(h_1)>=2e/3+3=183251937965.
  ```

  Every distance from `4` through `183251937964` is empty by an exact
  incidence contradiction. A shard must not allocate a second support-three
  chart, arbitrary weights on one or two off-locator points, or any support
  in that killed interval. A second proved quotient-support double count
  removes every distance above `3(e+1)/2=412316860416`. Thus the surviving
  high-distance interval is

  ```text
  183251937965<=delta_A(h_1)<=412316860416.
  ```

  It still needs a theorem-level aggregate or dual certificate; enumerating
  supports in this interval is not an executable request. Passing either
  side remains preprocessing and does not waive any later splitting
  condition.

  The general quotient weights are no longer solver variables. The proved
  Forney-numerator normal form writes them uniquely as

  ```text
  omega_t=F(t)/(A(t)^2 B_T'(t)),
  deg F=deg B_T-3,       lc(F)=Theta_2,
  gcd(F,A B_T)=1.
  ```

  A future high-distance request must therefore begin with a finite
  classification or aggregate for the locator/numerator pair `(B_T,F)`
  coupled to the clean split locators. Enumerating support subsets or source
  weights is explicitly out of scope.

  The proved minimal-support uniqueness theorem makes this prohibition
  sharper. In

  ```text
  183251937965<=h<=274877906944=e+1,
  ```

  there is exactly one minimal support `T`; every minimum-complement ordinary
  fiber is internal and uses it. A contributor task in this interval must
  accept the single canonical Forney pair `(B_T,F)` as input or derive it by
  a coverage-proved symbolic rule. A fleet over candidate supports is
  mathematically redundant. Multiple minimal leaders are possible only in
  the still-live upper interval
  `274877906945<=h<=412316860416`, which likewise has no executable request
  until a finite aggregate replaces raw support enumeration.

  Distinct leaders now obey the exact intersection cap
  `|T intersect T'|<=2h-2e-4`. The resulting Johnson bound gives at most six
  leaders for `e+2<=h<=279180239468` and an explicit finite bound through
  `h=302646214511`. A future request in that range may accept a bounded
  symbolic leader packet, but it must derive or certify those leaders from
  the Hankel/Forney data; it may not search the ambient support family. The
  bound controls leader count, not candidate count, and therefore is not by
  itself an executable compute request.

  The sharp-ceiling theorem removes `h=412316860416`. At the retained
  endpoint `h=412316860415`, there are only two possible multisets of the
  `4e` ordinary complement sizes: all are `412316860416`, or one is
  `412316860415`, one is `412316860417`, and the rest are `412316860416`.
  Any future endpoint request must consume one of these two profiles and the
  corresponding exceptional-intersection multiset. A generic
  high-distance support search would discard the exact theorem input and is
  not a valid contributor task.

  The endpoint exceptional and complementary resultants are now completely
  prescribed as opposite `P_ord` powers, with at most one reversed
  linear-factor swap. A future endpoint computation must operate on this
  succinct pair and compare it with the reciprocal identities. Materializing
  either dense resultant is out of scope. Promote this to an executable
  request only after a subresultant or product-tree certificate has a
  measured total cost and an independent streaming checker.

  The reciprocal complement `V` completes these data to an exact `2 x 2`
  resultant matrix. Any endpoint compute proposal must preserve all four
  entries and their row/column product checks; computing only
  `Res_X(A,Q)` is now incomplete. The next useful certificate must test a
  corrected-square coefficient or coprimality condition not already forced
  by this matrix. Recomputing incidence multiplicities is redundant.

  On the quotient-distance-three chart, apply the exact MDS-escape router
  before allocating ordinary split fibers. Reconstruct the exceptional
  coefficients `beta_a`, the first-order coefficients `alpha_a`, and the
  canonical triple weights. For each ordinary slope `z`, count

  ```text
  j_z=#{a:beta_a+z alpha_a=0}.
  ```

  Exactly `e` slopes must have `j_z=2`; their cancelled pairs partition all
  `2e` roots of `A`, and their clean locator is forced to be the remaining
  exceptional roots together with the canonical triple. Exactly `3e` slopes
  must have `j_z=0`; each corresponding locator `G_z` is disjoint from that
  canonical support and must satisfy

  ```text
  G_z(t_0)/A(t_0)=G_z(t_1)/A(t_1)=G_z(t_2)/A(t_2).
  ```

  Reject `j_z=1`, `j_z>=3`, any other internal support, or any external
  support intersection. Across the `6e+4` outside points, external-root
  multiplicity is at most `e`, its total deficit is exactly `e`, and at
  least `5e+4` rows are saturated. A shard should encode the `e` disjoint
  pairs and this near-saturated external incidence structure, not enumerate
  `4e` unrelated split locators. Passing the router remains preprocessing;
  it does not certify the lower Hankel chain or the reciprocal square.

  Reconstruct the full residual generator from the internal data before any
  external split test. If the internal slopes are `xi_i`, their cancelled
  pairs have polynomials `D_i`, `B` is the canonical triple polynomial, and
  `Q(xi_i)=lambda_i B A/D_i`, use

  ```text
  Phi(z)=product_i(z-xi_i)/product_i(-xi_i),
  L_i(z)=product_(j!=i)(z-xi_j)/(xi_i-xi_j),
  Q(z;X)=Phi(z)A(X)
         +zB(X)sum_i(lambda_i/xi_i)L_i(z)A(X)/D_i(X).
  ```

  This formula is proved necessary and has separation rank exactly `e+1`.
  A distance-three shard should therefore encode only the perfect matching
  of the exceptional roots, the distinct nonzero `xi_i`, and the nonzero
  `lambda_i`; allocating an arbitrary `(r,e)` biform or independent clean
  locators is obsolete. The remaining split test asks for exactly `3e`
  other values of `z` at which this reconstructed polynomial has `r` roots
  in `D_res\(R_A union T)`, together with the exact outside-row deficit `e`.

  Apply the proved quadratic locator-rank gate to every proposed external
  block packet before constructing a dense resultant. If `g(x)` is the
  coefficient vector of the monic degree-`e` row locator on an active outside
  row, the matrix

  ```text
  (g_i(x)g_j(x))_(x,0<=i<=j<=e)
  ```

  must have rank at most `3e+1`. Hence its `6e+3` rows have nullity at least
  `3e+2`, and for `e>=4` the locator points satisfy at least `e(e-3)/2`
  independent quadrics. Reject a packet above this rank immediately. A
  contributor implementation should emit a row-reduction certificate or a
  basis of the vanishing quadrics; passing this gate is necessary only and
  does not replace the subgroup, residue, or resultant-power checks. The
  first `e=3` analogue is dimensionally vacuous for this gate, so its purpose
  there is replay compatibility; route-selection evidence begins at the
  first complete `e>=4` analogue.

  Apply the stronger complement-residue gate first whenever the external
  blocks are available. With

  ```text
  I(z)=product_i(z-xi_i),       H_x(z)=P_Z(z)/G_x(z),
  ```

  the `6e+3` residue classes `H_x mod I` must span dimension at most three.
  Before choosing `I`, the full complement polynomials must span dimension
  at most `e+4`; reject a larger coefficient rank immediately.
  Equivalently, either evaluation matrix

  ```text
  (H_x(xi_i))_(x,i),       (G_x(0)/G_x(xi_i))_(x,i)
  ```

  has rank at most three. This test is linear in the packet size after
  product-tree evaluations and needs no dense resultant. Emit three basis
  residues and coordinates for every `H_x`, or a rank-four minor as a
  rejection certificate. Exact biregularity is insufficient: the banked
  `e=4` control has 27 distinct four-blocks on 12 slopes, column degree nine,
  and complement rank four. A useful contributor classification should
  enumerate or characterize only the rank-three residue families, not all
  biregular designs. A contributor packet should therefore print both the
  full complement coefficient rank and the reduced rank-three certificate.
  The reduced rank is exactly the span dimension of the quadratic pair
  locators. Rank two is not an anonymous degeneration: the banked Mobius
  dichotomy proves that all exceptional pairs are orbits of one common
  projective involution. Route such packets to a subgroup/Mobius intersection
  classifier and report the involution matrix. Rank-three packets remain the
  generic complement-residue classification target.

  Do not promote the quadratic `rank<=3e+1` filter into an equality premise
  on that generic branch. The proved generic Schur-square saturation route
  fence constructs arbitrary-size rank-three pair families with product rank
  at most `3e`; its exact `F_101`, `e=12` fixture has ambient/product ranks
  `37/36`, while a one-pair negative control restores 37. A contributor run
  must retain rank-defective generic packets and test them against calibrated
  complement incidence, boundary, and resultant-power conditions.

  Rank-defective packets now have a mandatory deterministic classification.
  Solve the linear equations `D_i | R-y_iB`, `deg R<=2`; their nullity must
  equal `(3e+1)-rank(M_2)` and must be zero or one. A lower matrix rank or
  larger nullity rejects the claimed generic packet. A nonzero solution
  prints the projectively unique `R` and every `y_i`. All nonzero levels must
  be distinct, with at most one zero level satisfying `D_i|R`. Route nullity
  zero to the rank-`3e+1` saturated branch and nullity one to the rank-`3e`
  trigonal-fiber branch. Do not enumerate possible rational maps or discard
  a packet merely because its Schur rank is one below the cap.

  **Official trigonal branch closed; no compute request.** The proved
  `official_trigonal_subgroup_exclusion` now rules out nullity one on the
  official order-`2^41` domain. Its coincidence curve has at least `2e`
  subgroup points, while the worst admissible bidegree-`(2,3)` form has at
  most `1440N^(2/3)<2e`; the geometrically reducible case would require an
  order-three Mobius deck map, also impossible on this `2`-group. An
  official classifier may reconstruct the kernel as an audit check, but it
  must require nullity zero and quadratic rank `3e+1`. Do not enumerate
  trigonal rational maps or request a distributed trigonal search. Small-row
  trigonal fixtures remain valid route fences because the official numerical
  subgroup margin is load-bearing.

  **Saturated rank-shadow route fenced; retain calibrated residues.** The
  exact `F_151`, `e=5` cyclic control has `33=6e+3` distinct blocks,
  replication `11=2e+1`, quadratic rank `16=3e+1`, and complement span
  `9=e+4`. Thus a donated run that tests only biregularity and these two
  ranks can return a genuine survivor without deciding CR-003. The fixture
  fails the real modulo-`I` condition uniformly: every degree-five `I` with
  nonzero constant term leaves residue rank at least four. Every future
  packet and pilot must replay this control, print `I`, and certify the
  rank-three matrix `(H_x mod I)_x`; do not request a fleet over the weaker
  coefficient-span interface.

  **Optional audit CR-003-CLIFT -- saturated calibrated conic-lift
  classifier (not runnable yet).** The first nonvacuous official-shaped
  analogue of the now-closed official distance-three branch is

  ```text
  m=4,       e=7,       r=15,       N=64,       F=F_193.
  ```

  Its audit decision is whether a pair-Lagrange generator on this complete finite
  row realizes the exact external split design while simultaneously having
  quadratic locator rank `3e+1` and the actual calibrated residue rank three.
  This is the smallest analogue that sees both live generic constraints;
  `e=3` makes the quadratic rank gate dimensionally vacuous. A complete
  survivor would be a proof-relevant route fence and a template for the
  kernel-lift obstruction. A complete no-hit result would remain
  small-analogue evidence, but its first universally failing gate could
  suggest the missing uniform theorem.

  Enumerate canonical support/matching packets only after the already proved
  quadratic-character, matching-free even-value, `tau`-label, boundary, and
  dual row-product gates. Reconstruct `Q` from the pair-Lagrange formula and
  decide the external design through the sparse subgroup norm and
  resultant-power equivalence; do not allocate slopes, blocks, or arbitrary
  biform coefficients. On every reconstructed design, form

  ```text
  I(z)=product_i(z-xi_i),
  G_x(z)=monic(Q(z;x)),       H_x(z)=P_Z(z)/G_x(z),
  Htilde_x(z)=B(x)G_x(0)H_x(z).
  ```

  The proved `calibrated_conic_kernel_lift_normal_form` forces the unique
  degree-`<e` representative

  ```text
  Htilde_x mod I = R_0+xR_1+x^2R_2 mod I.
  ```

  Emit `R_0,R_1,R_2` and the complete kernel lifts

  ```text
  J_x=(Htilde_x-R_0-xR_1-x^2R_2)/I,       deg J_x<=e.
  ```

  Its leading coefficient must be `B(x)G_x(0)`, and the checker must also
  replay the exact product identity

  ```text
  product_x(Htilde_x)=kappa P_Z^(4e+2).
  ```

  Apply the proved cleared-lift quartic router before any generic lift-rank
  analysis. Compute the explicit `E_i,N_i` first-jet polynomials, construct
  the bidegree-at-most-`(2e,4e+6)` clearing `F`, and for every reconstructed
  external slope exact-divide

  ```text
  F(gamma;X)=K_gamma(X)T_gamma(X),       deg T_gamma<=4,
  ```

  where `K_gamma` is the monic locator of the `4e+2` nonincident active
  rows. Emit every quartic coefficient vector and division remainder. A
  nonzero remainder or degree above four rejects the packet or the
  implementation. Do not reject a nonsplit or varying quartic: the exact
  `F_17,e=1` replay proves both behaviors can occur below the official
  uniqueness threshold.

  Also reconstruct the global quartic weld

  ```text
  FQ=(AB)^2q_eP_Z+CzI^2Omega,       deg Omega<=(e-2,4),
  ```

  and verify
  `Omega(gamma)=ell_gamma T_gamma/(gamma I(gamma)^2)` coefficientwise
  at every external slope. Emit the five coefficient polynomials of `Omega` and
  their rank. This rank is a discovery diagnostic, not a rejection gate: no
  theorem currently forces the `P^4`-valued curve to be a line.

  Apply the proved exceptional-boundary CRT reconstruction before building
  the external cofactors. In `F[X]/(A)`, emit the pair-label class
  `delta=xi_i mod D_i`, the exact quotient

  ```text
  V_A=(sum_i D_iN_iL_i)/(z-delta),
  ```

  and the canonical remainder

  ```text
  Omega_A=rem_A(
    N^(-1)X(X-s)(X-x_0)A'Bq_e^2V_A
  ).
  ```

  Every coefficient of `X^j`, `5<=j<2e`, is an exact rejection gate and
  must be zero. Emit those high coefficients even on rejection, together
  with the quotient and remainder identities; do not report only the final
  degree. On passage, require `Omega_A=Omega` and replay the three identities
  `C(t)zOmega_A(z;t)=q_e(t)^2 sum_iD_i(t)N_i(t)L_i(z)` at the roots of `B`.
  This gate is cheaper and earlier than constructing all `T_gamma`. The
  coefficient rank of the surviving five low coordinates remains diagnostic
  only.

  Emit the equivalent dual-RS moment certificate as well. For every
  `0<=j<=2e-6`, stream the pair-algebra traces

  ```text
  M_j(z)=sum_k Tr_(F[X]/(D_k) over F)(
    X^(j+1)(X-s)(X-x_0)Bq_e^2V_k(z)
  )
  ```

  and require every coefficient to be zero. The checker must verify each
  trace from the degree-two remainder modulo `D_k`, reconcile the moments
  with the high coefficients of `Omega_A`, and retain the first nonzero
  `(j,z-degree)` coefficient on rejection. This is the preferred streaming
  certificate: it does not materialize the degree-`6e+3` active locator `C`.

  Before selecting internal slopes, build the support-only pair-crossing
  matrix `R_l` for every omitted pair `l`. Its row for
  `D_k=(X-a_k)(X-b_k)` is

  ```text
  (G_l(b_k)a_k^d+G_l(a_k)b_k^d)_(0<=d<=4),
  G_l=X(X-s)(X-x_0)B^4(A')^4D_l^2.
  ```

  Emit all ranks, kernel bases, and evaluations of each kernel basis on the
  roots of `A/D_l`. Reject immediately if one matrix has rank five or if all
  its kernel polynomials vanish at one retained root. A retained matching
  must print a quartic kernel polynomial nonzero on every other pair. The
  deterministic `e=4,5,6,7` controls must replay ranks `3,4,5,5` for every
  omitted pair. The fixed `e=6,F_113` control must also replay all `10,395`
  matchings with the exact four-pattern histogram in `(QPC7)` and zero
  all-deficient survivors. Do not enumerate internal slopes for a rejected
  matching.

  On the official row, do not propose a raw all-deficient support sweep.
  The proved `quartic_support_low_degree_fiber_reduction` has already reduced
  every such packet to global smooth antiweight or to at least `e-148`
  fibers of one rational map of degree two, three, or four. Any donated
  official-scale computation must first compile one of those four symbolic
  branches, quotient by its map automorphisms, prove coverage including the
  bounded normalization tail, and publish a measured pilot. The reduction
  is official-scale and does not prune the `e=7` analogue above; using it as
  an analogue rejection gate would be invalid.

  Its proved continuation removes degree three and reduces degree two to one
  antipodal or constant-product involution with at most forty tail pairs.
  Do not request a degree-three fleet. The proved bounded-tail row-codegree
  theorem now gives the first symbolic ledger: with `t` off-involution pairs,
  every nonidentical outside orbit has codegree at most `t`, and at most one
  orbit has identical normalized rows. Thus the official branch has
  codegree at most forty. The proved degree-two tail-rigidity continuation
  sharpens the exact-design branch to at most six antipodal tails or eight
  constant-product tails, and therefore to row codegree at most six or
  eight. The later residual-discriminant theorem excludes every resulting
  gcd-corrected complement, so tail enumeration is retired rather than an
  executable request.
  The exact internal-slice continuation also absorbs global antiweight into
  degree two or degree four, so no independent antiweight fleet should be
  requested. The abstract antiweight fixture remains a required mutation
  control for any support-only compiler.
  The remaining degree-four branch is already symbolically routed to a
  geometrically reducible coincidence divisor or the Laurent-end curve
  `XY[X^2+XY+Y^2+a(X+Y)+b]=d`. Do not request a generic quartic-map fleet.
  Any contributor computation must compile one of those two forms and state
  which theorem decision its output would settle; a raw coefficient sweep
  is not an executable request.
  The reducible half is now theorem-classified as `F(X^2)`, `F(X^4)`, or
  `F(X+c/X)`. The proved pullback-involution absorption now routes all three
  forms into the same six/eight-tail static Pade-gcd leaf. No
  reducible-factor or pullback-quotient fleet is useful.
  The absolutely irreducible Laurent-end branch is now theorem-excluded by
  the Corvaja--Zannier gcd bound. Do not request a Laurent coefficient sweep.
  Both the simultaneous-gcd compiler `CR-003-BT8` and the pullback compiler
  `CR-003-PB4` are retained below only as retired provenance.

  Only then, before selecting the `lambda_i`, build the internal-slice lambda-cube
  matrix `U` from only the support partition, matching, and internal slopes.
  Its `e(2e-7)` rows are the coefficients above degree four in `(QLK3)`, and
  its required kernel vector is `(lambda_i^3)`. Emit the component
  interpolants `Y_lk`, a row-reduction certificate, every single-column
  deletion rank, and one of:

  ```text
  REJECT_U_FULL_RANK: rank(U)=e;
  REJECT_U_COLOOP: rank(U without column i)<rank(U);
  SURVIVE_U_CUBE: a deletion-stable kernel containing an explicit
                  coordinatewise-cube vector.
  ```

  Full rank or one coloop rejects the entire support/pair/internal-slope
  packet without enumerating `lambda_i`. A deficient packet is not yet a
  survivor unless its kernel meets the coordinatewise cube subgroup; print
  the `lambda_i` preimages and verify `U(lambda_i^3)=0`.

  Only then, before constructing `P_Z`, `N_i`, `Omega_A`, or any external
  cofactor, build the proved torus-kernel matrix `T` from the retained pair
  partition, internal slopes, `lambda_i`, and `q_e`. Its rows are the
  coefficients of the derivative-free pair traces in `(QTK4)`. Emit a
  row-reduction certificate, the rank after each single-column deletion, and
  one of:

  ```text
  REJECT_FULL_RANK: rank(T)=e;
  REJECT_COLOOP: rank(T without column i)<rank(T);
  SURVIVE_TORUS: rank(T)<e and every column deletion preserves rank.
  ```

  The first two `T` outcomes reject the packet exactly. On `SURVIVE_TORUS`,
  emit a kernel basis; after `P_Z` is reconstructed, verify that
  `theta_i=xi_iP_Z(xi_i)/lambda_i^2` lies in that kernel. Do not enumerate
  kernel vectors: `q>e` makes deletion stability equivalent to existence of
  some full-support kernel vector. The deterministic controls at
  `e=3,4,5,7` must replay `U` ranks `0,4,5,7` and `T` ranks `2,4,5,7`; only
  the dimensionally vacuous `e=3` control is torus-eligible at both stages.

  Report the coefficient rank of the `J_x`, their exact coefficientwise
  interpolation degrees in the active row coordinate, and any certified
  decomposition into projective lines. These are discovery diagnostics, not
  rejection gates: the present proof does not bound the lift rank or degree.
  They are included because a moving-root argument applies to the conic
  residues only after the kernel lifts are controlled. Omitting `J_x` would
  reduce this request to the false uncalibrated rank-shadow route.

  Before promotion from pre-request, contributors must provide all of:

  1. an inverse orbit-coverage map for every support and matching
     normalization on the displayed row;
  2. a deterministic positive-certificate checker replaying the Hankel
     source, pair-Lagrange formula, sparse norm, perfect-power identity,
     reconstructed incidence, both exact ranks, and the `J_x` decomposition;
  3. a complete negative-certificate format with per-gate survivor counts
     and resumable shard hashes;
  4. a strictly smaller measured pilot with peak RAM, storage, wall time,
     retry allowance, and a conservative total dollar ceiling.

  Checkpoint by canonical `(support,triple,matching,xi,lambda)` prefix and
  preserve counts and witnesses on timeout. A found survivor is `FAIL` for
  any proposed uniform exclusion using these inputs and triggers theorem
  repair. Exhaustive no-hit is `PASS` only for this one finite analogue and
  causes no DAG promotion without a proved transport theorem. Incomplete
  output is evidence only. Cost is currently unknown and potentially large:
  do not launch this request on the local Modal balance or in WSL. When the
  rate-half packet is vendored upstream, include CR-003-CLIFT only under
  **Optional audits**, not as a missing proof step. A contributor may supply
  the compiler or pilot under an accepted resource cap if small-row route
  diagnostics are useful.

  The official subgroup/Mobius classifier is now theorem-complete for the
  nonspecial branch. Published explicit bounds give at most `32N^(2/3)`
  graph points, below `2^33`, versus the required `2^39-2`. Do not request a
  general Mobius fleet. A rank-two packet must be one of the two dihedral
  forms `a<->-a` or `a<->c/a`; apply the boundary root-unity and dual
  row-product gates symbolically to those forms. Large computation on the
  dihedral cases is not authorized until that substitution produces a
  finite compressed parameter space and a costed pilot.

  The boundary substitution is now complete. Either dihedral form requires
  `gcd(e,p-1) in {e/3,e}`. The apparent reciprocal five-point packet has
  exact form `c=sx_0`, `T={u,t,c/t}`, `u^2=c`, but the triple gate gives
  `(u/t)^(3e)=1`; coprimality with `N` then contradicts `u!=t`. Restrict any
  future rank-two implementation to the two high-order field strata, print
  the field-order gcd and the boundary involution orbits, and apply the dual
  `r`-th-power residue gate next. Do not spend compute enumerating fields or
  pairings outside this theorem-reduced list.

  **Completed arithmetic route fence (do not rerun).** Recursive Lucas
  certificates now exhibit an official-interval prime in each of the two
  retained gcd strata, with `gcd(r,p-1)=1` in both examples. Consequently a
  large prime or congruence scan has no closure value, and the dual residue
  gate cannot be a uniform exclusion. A useful large run must start from a
  coverage-complete compressed split-pencil parameterization, branch first
  on `gcd(r,p-1)`, and return a compact algebraic rejection certificate or a
  fully replayable survivor. Until such a parameterization and measured
  pilot exist, this remains a theorem task rather than a compute request.

  The dual residue gate is now compressed symbolically. For either dihedral
  branch it is the split-algebra equation

  ```text
  Y^r = kappa W(E')^2 mod E,       deg E=e, deg W=7, deg Y<e.
  ```

  Any future contributor implementation must operate on the orbit polynomial
  `E`, not on `2e` individual exceptional roots, and must emit the remainder
  identity plus an `r`-th-root witness or a power-residue rejection. Skip this
  gate when `gcd(r,p-1)=1`, where it is automatic, and apply the resultant
  perfect-power split-design test instead. A large official-degree solve is
  not yet authorized: the equation still has degree-`e` unknown data and no
  coverage-complete finite parameterization.
  A PR may request distributed compute only after an additional theorem
  reduces `E` to a finite resumable family and a small analogue measures the
  per-case cost. The replay certificate should contain `E`, the degree-seven
  `W`, `Y`, and the exact quotient in the displayed congruence; raw root or
  field enumeration is out of scope.

  The full sparse subgroup norm has also been descended to the involution
  quotient. Use

  ```text
  Res_U(U^(N/2)-1,V_-)                 (antipodal),
  fixed_Q_product * Res_U(Omega_c,V_c) (constant product),
  ```

  where both value polynomials have `U`-degree at most `r`, and `Omega_c` is
  recovered from `D_N(U,c)-2` by removing its zero or two fixed-point factors
  and taking the exact square root. Exact-degree external split slopes are
  equivalently the parameters where this degree-`r` value polynomial splits
  over the quotient set. A future large-run request should use
  cyclic-resultant or remainder-sequence arithmetic against these compact
  quotient locators and divide the known sparse-norm factors online. It must
  not enumerate `mu_N`, materialize a dense degree-`N` Dickson polynomial, or
  construct the active-row locator. No official run is authorized until a
  measured small analogue demonstrates sublinear storage, resumable shards,
  and a compact multiplicity/factorization certificate. This quotient norm
  interface is the specification contributors should implement when that
  pilot exists.

  A quotient implementation must also replay the external-product ledger

  ```text
  product_z monic(V_z)=C_2^(2e)C_1^e,
  epsilon in {0,1},
  sum_z double_roots(V_z)=epsilon e,
  sum_z simple_roots(V_z)=3er-2epsilon e.
  ```

  Here `epsilon` records the zero-or-one identical-row orbit. On the exact
  zero-tail branch, every nonexceptional paired row set has codegree zero;
  when `epsilon=1`, exactly `e` factors have the same one double root. An
  implementation should report this orbit, the simple/double histogram for
  each factor, and exact product-tree hashes for `C_1,C_2`. On the
  quartic-support branch with `t>0`, this ledger must not be asserted
  unchanged. The now-retired `CR-003-BT8` specification records the required
  row gcd and degree `d_u<=t` for regression purposes. These are rejection
  checks and compact certificates, not authorization for a large run. A
  future distributed request on a different open branch becomes valuable
  only after a theorem or complete parameterization makes its candidates
  enumerable without scanning fields, subgroup points, or arbitrary split
  polynomials. At that point contributors can shard by orbit-polynomial
  parameter and return the first failed ledger identity or a full survivor.

  The pair-complement trace gives a smaller certificate target. Every
  nonexceptional two-row orbit must emit a degree-`e` divisor

  ```text
  K_u=a_uI+chi(u)(u^2M_0-2uM_1+M_2),
  K_u | P_Z,
  ```

  and the packet must contain at least `3e-2` distinct projective divisors on
  the antipodal branch or `3e-3` on the constant-product branch. Their last
  three coordinates satisfy `b_1^2=4b_0b_2`. The abstract classification
  request has now been retired: the proved abstract-quadric route fence gives
  `6e+1` such divisor classes by three one-root-swap pencils. A computation
  enforcing only divisibility, a four-space, and the cone would therefore
  spend resources rediscovering genuine abstract survivors.

  **RETIRED contributor request -- zero-tail calibrated dihedral trace
  classification.** The proposed large run would have enforced, for every
  internal root `u_i`,

  ```text
  mu_i=P_Z(xi_i)/lambda_i^2,
  K_u(xi_i)=chi(u)mu_i(u-u_i)^2,
  K_u | P_Z,
  product_z monic(V_z)=C_2^(2e)C_1^e,
  ```

  as well as the official antipodal or constant-product subgroup orbit and
  the zero-or-one exceptional-pair rule. Do not launch it. The proved
  dihedral trace-collision exclusion rules out the exact zero-tail branches
  for every `e>=31` by combining the calibrated quadratics with the `e-4`
  minimum complement incidence. It does not by itself cover the at-most-8
  off-involution pairs produced by the quartic-support router. Preserve this
  specification only as provenance for the retired zero-tail route and as a
  regression template for the retired bounded-tail route.

### Retired pre-request CR-003-BT8: bounded-tail dihedral complement compiler

- **status:** RETIRED BY THEOREM. Do not launch or copy this request as live
  upstream work. The proved residual-discriminant exclusion rules out every
  aligned degree-one-through-four pencil and closes the complete
  all-deficient quartic-support branch. The specification below is retained
  only as provenance and as a regression interface.
- **former consumer:** the former bounded-tail degree-two branch of
  `rate_half_band_closure`, now theorem-closed.
- **proved router:** for an antipodal or constant-product involution, with
  `t<=6` or `t<=8` respectively, each nonidentical outside orbit
  `{x,tau(x)}` has

  ```text
  g_u=gcd(q_x,q_tau(x)),       d_u=deg g_u<=t,
  K_u=P_Z g_u/(q_x q_tau(x)),  deg K_u=e+d_u,
  ```

  and at most one outside orbit has identical normalized rows. The checker
  must also replay the degree-`t` eliminant `H/I_G`; it may not infer the
  codegree from sampled roots.
- **former mathematical decision:** classify every nonzero pencil

  ```text
  R(U,Z)=R_2(Z)U^2+R_1(Z)U+R_0(Z),
  1<=deg_Z R<=4,
  ```

  for which at least `e-33` antipodal or `e-44` constant-product coordinates
  `u` give distinct split squarefree divisors `R(u,Z)` of one fixed
  squarefree `P'=P_Z/P_H`, while every root of `P'` occurs at no more than
  two such coordinates. Exclude all four degrees or return a replayable
  pencil satisfying the complete packet interface. High-degree gcd,
  bivariate relation, nonzero-determinant, and individual-circuit searches
  are already paid and are not route-deciding. The residual-discriminant
  theorem supplies the uniform symbolic exclusion, so this decision is paid.
- **former pilot rows:** first replay symbolic `t=0,1,2` mutation fixtures. Then use
  only compiler-produced exact-design packets on `(m,e,N,p)=(4,7,64,193)`.
  A later threshold pilot may use `(16,31,256,257)`, but only after the first
  pilot supplies a measured per-packet cost and a complete normalized
  parameter cover. Neither pilot transports automatically to the official
  row.
- **former required artifact:** stream `R_0,R_1,R_2`, `P'`, the canonical aligned
  coordinate set, every exact division `P'/R(u,Z)`, split/squarefree
  certificates, the root-use histogram, and either a symbolic exclusion by
  degree or the first full survivor. Include mutation witnesses for degree
  drops, repeated factors, identical divisors, and roots used three times.
  Packet-level pilots must additionally emit `P_H`, `q_x,q_tau(x),g_u,K_u`,
  and exact division witnesses. A no-hit certificate must include canonical
  shard intervals, coverage counts, rolling hashes, and an independent
  checker that never materializes all subgroup points at once.
- **former resource contract:** unknown. Before promotion to a numbered request,
  bank a resumable launcher and a smaller measured pilot with hard CPU, RAM,
  storage, wall-time, retry, and dollar ceilings. Shard by canonical tail
  invariant, not by arbitrary pair tuples. Preserve the first witness and
  all completed shard totals on timeout.
- **retirement effect:** no finite pilot is needed. A replayable survivor
  would now be a falsifier of the proved residual-discriminant exclusion and
  should be reported as a proof bug with the complete packet interface. A
  no-hit computation has no additional proof value.

### Retired pre-request CR-003-PB4: quartic pullback quotient compiler

- **status:** RETIRED BY THEOREM. Do not launch or copy this request into an
  upstream PR. The proved pullback-involution absorption routes every
  quartic pullback into the bounded-tail interface, and the subsequent
  residual-discriminant exclusion closes that interface.
- **former consumer:** the former degree-four pullback branch of
  `rate_half_band_closure`, now absorbed into the static Pade-gcd leaf.
- **proved router:** every surviving quartic comparison field is one of

  ```text
  F(X^2),       F(X^4),       F(X+c/X),
  ```

  with at least `e-148` matched fibers. The generic irreducible, Laurent,
  reducible-factor, degree-three, and independent antiweight fleets are
  already retired by proofs.
- **mathematical decision:** after quotienting the complete deck action,
  decide whether the exact internal-slice, boundary-product, source, and
  external-design identities admit any quartic-pullback packet. The compiler
  must distinguish an order-two matching from an order-four fiber whose
  chosen pairs may mix deck involutions.
- **pilot:** use `(m,e,N,p)=(4,7,64,193)` only after an inverse normalization
  map proves complete ownership of every pullback packet. Reuse
  `CR-003-CLIFT` residues and kernel lifts rather than recomputing them. A
  larger run must wait for a measured pilot and a theorem identifying a
  finite quotient-parameter family.
- **required artifact:** canonical map/deck parameters, selected pair orbits,
  all at-most-148 normalization tails, exact product/source residuals, first
  failed identity or a full survivor, shard coverage hashes, and an
  independent streaming checker. Raw roots, arbitrary quartic coefficients,
  and dense degree-`N` locators are forbidden artifact formats.
- **retirement effect:** preserve this specification only as provenance for
  the discarded route and as a regression checklist for the absorption
  theorem. Any future counterexample must first falsify that theorem; absent
  such a witness, no donated compute belongs on the quartic-support branch.

  The outside-row condition is now exact, not merely a deficit budget. One
  point `x_0` outside `R_A union T` is omitted from every external locator;
  each of the other `6e+3` outside points occurs in exactly `e` of the `3e`
  external locators. If `C` is the monic polynomial on those `6e+3` points,
  require the compact identity

  ```text
  product_(z external) G_z(X)=C(X)^e,
  P_X(X)=A(X)B(X)C(X).
  ```

  A contributor should print the omitted row and a product-tree certificate
  for this power identity. Aggregate deficit alone is no longer an admissible
  certificate. The resultant-power equivalence below supersedes the former
  requirement to allocate or print the full biregular incidence matrix.

  A deterministic low-order route fence is now available at

  ```text
  background/nodes/rate_half_ca_hankel_distance_three_e1_hankel_design_route_fence/verify.py
  ```

  It exhausts all `1820` degree-four split locators and all projective slopes
  over `F_17`. The fixture is column-far and jointly passes the pair normal
  form, exact external design, affine Hankel ranks, first-order crossing,
  pinned adjugate, and supported-fiber product identity. It deliberately has
  four quotient-support triples at `r=3`, below the official `r>=4`
  uniqueness threshold. A contributor classifier must replay this fixture:
  rejecting it before an explicitly official-scale uniqueness or reciprocal
  gate signals an over-strong constraint. The next useful analogue is the
  first `r>=4` instance; a larger sweep of `r=3` fixtures has no proof value.

  Do not allocate contracted source weights or endpoint moments on a
  distance-three shard. Once the matching `D_i`, internal slopes `xi_i`,
  internal scalars `lambda_i`, and `Theta_2` are fixed, reconstruct

  ```text
  q_bar(z)=sum_i(lambda_i/xi_i)L_i(z),
  K_a=Theta_2 Delta_i /
      (Delta_0 A'(a)B(a)^2(lambda_i/xi_i)(A/D_i)(a)),
  beta_a=-xi_iK_a,       alpha_a=K_a,
  omega_t=Theta_2/(A(t)^2B'(t)).
  ```

  These coefficients uniquely determine `h_0,h_1` through degree `2r`.
  At an external slope the minimum-circuit scalar must replay as
  `Theta_2 Phi(z)/q_bar(z)`. Once all `3e` required external split fibers
  pass, the contracted Hankel identity, exceptional/ordinary ranks,
  first-order crossing, and `adj M=c_H z q q^T` are proved consequences of
  these reconstructed sources; replay them in the checker, but do not give
  them solver variables or treat them as independent search gates. Continue
  with the corrected-square converse below, then the original endpoint
  lift/column-far check and absence of extra split fibers.

  The corrected reciprocal square is no longer an independent search gate
  after the exact split design passes. For every saturated row, verify the
  degree-`e` divisibility `Q(z;x)|P(z)`; for every ordinary supported slope,
  verify `Q(z;X)|P_X(X)`. Coefficientwise interpolation then reconstructs

  ```text
  QV+P_XW=P,       QA_c+P_clB_c=P_X,
  WB_c-z=QK,       VB_c+zA_c=-P_XK.
  ```

  The proved exceptional factor-descent chain supplies every later
  reciprocal/resultant/Bezout identity. A checker should replay those
  identities, but a solver must not allocate complements, welds, reciprocal
  forms, resultants, or Bezout coefficients. Continue with the original-lift
  converse below.

  No original-lift or column-far search remains after the external design
  passes. For arbitrary endpoint scalars, recover the original moments from

  ```text
  y_(ell,0)=tau_ell,
  y_(ell,k+1)=s y_(ell,k)+h_(ell,k).
  ```

  The full locator `(X-s)Q` certifies all `4e+1` required close slopes. A
  common full locator is proved impossible: after contraction it would give
  one fixed support of at most `r+1` points, while MDS independence forces it
  to contain the `6e+3`-point union of the external locators. Additional
  close slopes only strengthen a counterexample and need not be excluded.
  Historically, CR-003's distance-three decision reduced exactly to:

  ```text
  does an official pair-Lagrange generator realize the exact external
  split design?
  ```

  The proved external split-design exclusion now supplies the complete
  official nonexistence theorem, so no official-scale computation should be
  launched for this decision. A positive small-analogue certificate remains
  a route fence, not an official counterexample.

  Apply the boundary root-unity router before allocating any remaining design
  variables. For every matched pair `D_i=(X-a)(X-b)`, compute

  ```text
  U=B(a)(A/D_i)(a)/(B(b)(A/D_i)(b)),
  zeta=-[P_X'(a)/P_X'(b)]/U^4,
  ```

  and require `zeta^e=1`. For two independent pairs `t,u` among the canonical
  triple, require

  ```text
  ([P_X'(t)/P_X'(u)]/
   ((A(t)/A(u))^4(B'(t)/B'(u))))^e=1.
  ```

  Evaluate derivatives directly as
  `N*x^(-1)/((x-s)(x-x_0))`. These gates depend only on `A,B,x_0` and the
  matching. Reject before choosing `xi_i`, `lambda_i`, external slopes, or
  blocks. Print the actual root-of-unity labels for every survivor; a bare
  pass bit loses information needed by later product constraints.

  Before even constructing the boundary value polynomial, apply the proved
  quadratic-character consequence

  ```text
  -A(0)A(s)A(x_0) in (F_p^*)^2.
  ```

  This depends only on the exceptional support and the two removed rows. A
  nonsquare rejects the support before the triple, matching, residue classes,
  slopes, or scalars are allocated.

  Before enumerating pair matchings, apply the matching-free form. Compute

  ```text
  Y_a=(P_X'(a)/(B(a)^4 A'(a)^4))^e       (a in R_A).
  ```

  The monic value polynomial `product_a(Y-Y_a)` must be even. This condition
  is equivalent to the existence of a boundary-compatible perfect matching;
  reconstruct only matchings that pair `Y_a` with `-Y_a`. On the triple,
  the three values

  ```text
  (P_X'(t)/(A(t)^4 B'(t)))^e
  ```

  must be equal. A classifier that allocates arbitrary pairings before these
  two tests is obsolete.

  Couple this evenness test to the dual row-product residue before
  reconstructing any matching. In `F_q^*/(F_q^*)^r`, put

  ```text
  c_a=C(a),       M=product_(t in T)C(t),
  Lambda(a)=(Y_a,[c_a]_r),
  tau(y,g)=(-y,[-M]_r g^(-1)).
  ```

  The label multiset must be invariant under `tau`; this is equivalent to
  existence of a matching satisfying both the boundary and `r`-th-power
  gates. It also forces the aggregate test

  ```text
  product_(a in R_A)C(a)/(-M)^e in (F_q^*)^r.
  ```

  Equivalently, test

  ```text
  Res(A,C)/(-Res(B,C))^e in (F_q^*)^r.
  ```

  Reconstruct only `tau`-paired matchings. Testing central symmetry and the
  pair residues in separate matching fleets is obsolete.

  Apply the dual row-product gate on the same support packet. The exact
  external incidence design forces

  ```text
  product_(C(x)=0) Q(z;x)=L P_Z(z)^(2e+1).
  ```

  Consequently every matched pair `D_i` must satisfy

  ```text
  R_i=product_(C(x)=0)B(x)/D_i(x) in (F_q^*)^(2e+1).
  ```

  Compute `R_i` from the compact resultant ratio
  `Res(C,B)/Res(C,D_i)`, or from the boundary values in `(DRP5)--(DRP6)`,
  and test `R_i^((q-1)/g)=1` for `g=gcd(2e+1,q-1)`. At official scale

  ```text
  e=3*174763*524287,
  2e+1=7*79*8191*121369.
  ```

  The two support-only gate families therefore occupy disjoint odd-prime
  field strata. Reject on either family before choosing `xi_i,lambda_i` or
  any external block. A contributor certificate must retain the `R_i`
  values and power-residue witnesses, not only pass bits.

  The complete external design is now one resultant test, not a block
  census. Put

  ```text
  q_e(X)=[z^e]Q(z;X),
  Delta(X)=Res_z(Q,partial_z Q),
  H(z)=Res_X(C,Q),       L=Res_X(C,q_e).
  ```

  First require `gcd(C,q_e Delta)=1`. Then compute the unique monic radical

  ```text
  P_Z=monic(H/gcd(H,H')).
  ```

  The exact necessary-and-sufficient condition is

  ```text
  deg P_Z=3e,       P_Z squarefree and split over F_p,
  H=L P_Z^(2e+1).
  ```

  The prime-field collapse gives `p>deg H`, so ordinary derivatives and the
  radical are exact. On a pass, reconstruct each block by
  `{x:C(x)=0,Q(gamma;x)=0}` for `P_Z(gamma)=0`; row squarefreeness and power
  multiplicity prove automatically that every block has `2e+1` distinct
  roots. Do not allocate external slopes, blocks, locators, an incidence
  matrix, or `P_Z` as solver variables. A contributor implementation should
  use a succinct resultant/norm representation and stream reconstructed
  blocks only for independent checking; materializing the degree-`<2^79`
  resultant in WSL is out of scope.

  Prefer the sparse subgroup-norm realization of that criterion. With
  `I(z)=product_i(z-xi_i)` and
  `R_D(z)=Res_X(X^N-1,Q(z;X))`, the proved router gives

  ```text
  z R_D(z)=
    kappa_0 Q(z;s)Q(z;x_0)(zI(z))^(2e+1)H(z),
  ```

  for the explicit nonzero scalar `(SSN3)`. Under a design this is

  ```text
  z R_D(z)=
    kappa_0 L Q(z;s)Q(z;x_0)
    (zI(z)P_Z(z))^(2e+1).
  ```

  Compute the norm against the two-term polynomial `X^N-1`, exact-divide by
  the two boundary-row forms and the known internal power, and apply the
  radical/splitting test to the quotient. This is the preferred executable
  path. It must still replay the row-discriminant gcd against `C`; the sparse
  norm replaces construction of `H`, not that independent transversality
  gate. A dense product over all active rows is a cross-check only.

  At each active domain root impose the exact gcd factorization

  ```text
  K_x=-H_xJ_x,       deg Qhat_x=delta_x+epsilon_x,
  N_x=Qhat_x/E_Z^epsilon_x,
  S_*=product_x N_x,       sum_x delta_x=C_*.
  ```

  When `D_*=1`, also impose the exceptional saturated gcd degree at least
  `e+3b` and complementary quotient degree at most `c+1`. Allocate no shards
  for `K=0`, the quartic boundary, a trace-free weld, arbitrary prime-factor
  allocations, a `Z_W` exceptional allocation, or a zero exceptional trace;
  all are proved impossible. Do not run the unreduced weld as one monolithic
  elimination. Each live shard must additionally certify the exact two-sided
  partitions

  ```text
  Q_gamma A_gamma=G_X/X_0       for every clean gamma,
  Q_x V_x=P                     for every saturated x,
  ```

  with squarefree disjoint factors of exact degrees
  `(r,D_0-deg(X_0)-r)` and `(e_*,T-e_*)`. Check the active bad-row clean
  incidence total `c e_*-C_*-E_bad` before attempting elimination. Do not
  introduce independent biform coefficients for a proposed partition packet.
  First build its saturated-row by clean-slope nonincidence graph, check the
  incidence relation in both directions, and label every edge by

  ```text
  theta_(x,gamma)=F_gamma(x)/G_x(gamma).
  ```

  The graph is proved connected. Recover its row/column potentials by one
  spanning-tree pass and reject on the first inconsistent cycle. With the
  recovered clean-fiber scalars `a_gamma`, test all `r+1` vectors

  ```text
  (a_gamma [X^j]F_gamma)_(gamma in Z_cl)
      in RS[Z_cl,e_*+1].
  ```

  These tests are necessary and sufficient to reconstruct the unique
  partition-compatible biform up to scalar, and they automatically verify
  every saturated fiber. Compute the ranks of the scaled clean-locator
  coefficient matrix, scaled saturated-locator coefficient matrix, and core
  value matrix; they must agree with `sr(Q)`, be at least
  `ceil((e+1)/(b+1))>=5`, and equal `e+1` when `b=0`. Only a packet passing
  this gate should acquire Hankel-chain, adjugate, irreducibility, or
  active-trace variables.

  The bounded prime-field reference prefilter and schema are

  ```text
  background/nodes/rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction/check_packet.py
  background/nodes/rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction/packet_schema.md
  ```

  It emits a canonical packet hash and all three ranks. It deliberately
  materializes the small-analogue core matrix and does not certify primality,
  the ambient domain/support, or any post-partition Hankel condition. Use it
  for bounded pilot shards only; a positive final certificate still needs the
  complete independent checker specified below.
- **positive certificate:** print the shape, field, domain generator, endpoint
  syndrome vectors `y_0,y_1`, the primitive `Q(U,V;X)`, its left or right
  KCF/minimal-index certificate, all `T` slopes and split locators, the
  column-far no-common-locator check, component factorization, incidence
  matrix, the corresponding norm identity, and the complementary
  factorization. For a
  half-distance `A=3` certificate, print and verify the extra locator root at
  every clean slope. For `A=1`, print the fixed core, residual generator,
  Euclidean remainder, and residual norm identity separately. The independent
  checker must rebuild every Hankel matrix and verify all ranks, roots,
  weights, and degree ledgers. For an `A=1,s=1` active partition packet it
  must also print the nonincidence graph, locator hashes, recovered potentials,
  zero Reed--Solomon parity syndromes, and the three matching rank
  certificates. A rejected packet should retain a compact inconsistent-cycle
  witness, a nonzero parity syndrome, or a rank mismatch.
- **negative certificate:** an exhaustive Groebner/regular-chain or finite
  enumeration transcript for every registered field and allowed component
  packet, including saturated ideals, symmetry coverage, and independently
  checkable inconsistency witnesses. Random sampling or a solver's bare
  `UNSAT` line is insufficient.
- **interpretation:** one positive small analogue is a route fence and a
  construction template, not an official counterexample. Complete negative
  small analogues are also evidence only, but can reveal which component
  chamber or Hankel-chain identity should be promoted into a uniform theorem.
  Neither outcome changes the critical status without a proved transport.

- **high quotient-distance endpoint handoff:** no large run is executable
  yet. A future symbolic classifier for the two exact endpoint resultant
  profiles must consume
  `quotient_clean_fiber_first_jet_transversality`, retain the reconstructed
  `F,U,L,S`, set `M=2^41` and `N_sq=M+r-3`, and emit for every clean
  selected incidence

  ```text
  F_t U W_vee=-P_cl' E y^N_sq,
  dot y=-(P_cl'E/M)y^(r-2)(1-sy)(1-x_0y)/W_vee.
  ```

  It must also verify all factors are nonzero and hash the complete
  incidence/velocity multiset. It must then consume the clean-fiber
  `W_vee` interpolation normal form and triangular unit reconstruction:
  construct canonical `W_0`, but do not allocate `A_W,B_W`. Instead stream
  the Bezout-reduced Euclidean remainders

  ```text
  C_k^0=f_0d_k+r_k,       deg r_k<e,       0<=k<r,
  rho_k=-r_k,             s_k=d_k+a_minus r_k.
  ```

  Stop at the first `deg r_k>=2` and emit that remainder with the complete
  predecessor hash as an exact rejection certificate. If every residue is
  affine, reconstruct `A_W,B_W` uniquely, form the deterministic exact
  quotient `S=(LW_vee-EY^N_sq)/F`, and emit all degree-box and Hankel
  remainders. Do not compute a modular inverse or repeat the exact division:
  `l_0P_cl+f_0a_minus=1` proves the displayed formulas. No endpoint search
  variable remains after the support and incidence packet is fixed.

  The square class

  ```text
  Xi_A=Res(A,q_1) Res(A,Phi)/(Res(A,B_T) Disc(A)).
  ```

  is a mandatory consistency gate, but the proved cancellation theorem gives

  ```text
  Xi_A=(-1)^e Norm_A(Beta) Res(A,q_1)^2.
  ```

  Weighted self-duality already makes the first factor square. Therefore no
  standalone official-scale `Xi_A` run should be requested: evaluating it
  from a complete packet only rechecks an existing determinant identity. A
  checker may verify the equality on a bounded positive certificate, but it
  must do so from streamed values and treat any nonsquare as an internal
  inconsistency. The only potentially proof-producing scalar contribution is
  a separate endpoint-profile formula for `Xi_A` derived without assuming
  the self-dual/Forney packet; that is a theorem request until such a formula
  exists, not a large-compute request.

  Do not spend compute on `Res(A,q_1)/Res(A,q_e)`. The proved endpoint
  derivative-resultant identity reduces it exactly to `P_ord(0)^k_0` in the
  flat profile and `(z_min/z_max)P_ord(0)^k_0` in the swapped profile. At the
  official odd `k_0`, its square class is obtained with at most three field
  elements. This ratio occurs squared in `Xi_A`, so it cannot strengthen the
  cancelled square gate. Retain it as the exact norm certificate for
  `p_(e-1)=q_e/q_1` in an MDS/non-MDS structural classifier; do not launch a
  resultant job merely to reproduce it.

  On the MDS branch, do not assume that codimension-one Schur square implies
  GRS. The proved half-dimension route fence gives a Euclidean self-dual
  `[8,4,5]` MDS counterexample with square dimension seven and an exact
  non-GRS syzygy certificate. Any donated classifier must consume the actual
  split-incidence polynomials and Forney unit. A generic MDS/Schur-square
  recognition run has no proof value here and should not be launched.

  On the non-MDS branch, never enumerate the `binom(2e,e)` maximal minors.
  The proved annihilating-pair router reduces a positive certificate to
  independent `u,v in U_q`, complementary `e`-set zero hashes, and
  `uv=0 mod A`. A bounded compiler may search for such pairs in a compressed
  small analogue and emit the two row-combination vectors plus the quotient
  remainder. It must also print `D_u=gcd(A,u)`, `D_v=gcd(A,v)` and route to
  either `max(deg D_u,deg D_v)>=e+1` or the exact certificate
  `D_uD_v=A`, `deg D_u=deg D_v=e`. At official scale, a run is requestable only after an
  endpoint-specific algorithm finds or excludes annihilators without listing
  subsets and supplies a peak-memory/operation bound. A raw minor or subset
  fleet is expressly out of scope regardless of available containers.
  Form each gcd from `A` and the unnormalized numerator
  `sum lambda_i q_(i+1)`; do not compute `q_1^(-1) mod A`.
  Record the common complementary rank deficiency `d`, bases for both
  shortening spaces, and all `d^2` cross pairs. One witness is insufficient
  when `d>1`.

  Every retained annihilator pair must then form the exact quotient
  `K=H_lambda H_nu/A` and verify

  ```text
  [X^(h-1)] rem_(B_T)(Phi K A^(-1))=0.
  ```

  Emit the exact-division witness, a Bezout certificate for `A^(-1) mod B_T`,
  and the top coefficient. Stop on a nonzero coefficient. At official scale,
  dense arrays of length `h` or `2e` are unauthorized; a donated run must
  first provide a compressed multiplication/reduction representation and a
  bounded pilot showing its memory profile. The scalar gate is useful only
  after an annihilator candidate is found; it does not justify a blind search
  over coefficient combinations.

  The checker may replace the support reduction by the proved equivalent

  ```text
  sum_a beta_a q_1(a)K(a)=0                         (deg K<=2e+1),
  sum_a beta_a q_1(a)K(a)=Theta_2 lc(K)             (deg K=2e+2).
  ```

  Choose whichever side has a certified compressed representation; do not
  materialize both. The transcript must state the degree branch and replay
  the boundary coefficient exactly for every one of the `d^2` cross pairs.

  Independently compute the second jets from

  ```text
  F V_vee+R_XW_vee=P_clE Y^N_sq
  ```

  along every selected root, interpolate `j_gamma=W_vee,t(gamma,Y)`, and
  emit

  ```text
  D_gamma=(j_gamma-W_0,t(gamma,Y))/P_cl'(gamma).
  ```

  Reconstruct `A_W,B_W` from the first two canonical clean slopes, stop on
  the first later failure of `D_gamma=gamma A_W+B_W`, and otherwise compare
  the pair coefficientwise with the unit-remainder pair. Retain the first
  failed slope or coefficient as the exact certificate; do not store the
  full Hermite table when a streaming comparison suffices.

  Implement each fiber through the proved quotient-ring compiler modulo
  `F(gamma,Y)`. Reduce the official powers to `Y^(r-3)` and `Y^(r-4)` before
  arithmetic, and emit Bezout witnesses for every inverted class. Root
  enumeration is unauthorized. Dense coefficient arrays of length
  `r=2^39-1` are also unauthorized and infeasible: a donated official-scale
  run is meaningful only after it supplies a compressed locator
  representation with certified multiplication, reduction, inversion, and
  equality checks. Until such a representation and a measured small pilot
  exist, this remains a proof-engineering request rather than a compute
  request, regardless of available container count.

  Before emitting any fiber polynomial, compute the quotient-algebra trace

  ```text
  Tr((j+w_Yv)w^(-1))
  ```

  and compare it with

  ```text
  (N_sq+1)E'/E+N_sq q_bar'/q_bar-(r-1)q_0'/q_0.
  ```

  Stop on the first mismatch and retain the trace certificate, the four
  logarithmic derivatives, and the quotient-ring inverse witness for `w`.
  The trace must be computed from a compressed trace/resultant oracle; a
  rootwise sum or dense companion matrix is not an acceptable official-scale
  implementation.

  Retain the coefficient-plane commitment

  ```text
  W_q=span{q_0,...,q_e},       dim W_q=e+1,
  W_q^T M_0 W_q=W_q^T M_1 W_q=0.
  ```

  Verify the two zero Gram operators and the endpoint intersections
  `W_q intersect ker M_0=span{q_0}` and
  `W_q intersect ker M_1=span{q_e}` through compressed linear-operator
  certificates. Do not emit or evaluate all `(e+1)^2` scalar pairings.
  A contributor proposal must first specify a deterministic compressed
  certificate format and its independent checker; randomized projections
  may be used as pilot diagnostics but are not proof certificates.

  The same certificate must append `v=Xq_0` and verify, without changing
  basis, that the restricted Gram operators on
  `H_q=W_q+span{v}` have ranks `(0,1)`, with the sole nonzero entry
  `v^TM_1v`. Do not allocate a separate regular Kronecker block: the proved
  rank-one flag identifies it with `H_q/W_q`.

  On the exceptional roots, emit a compressed generator commitment for the
  induced weighted self-dual code and certify `G D_beta G^T=0` and rank `e`.
  Any selected maximal minor must be paired with its complementary minor and
  checked against

  ```text
  Delta_J^2 product_J beta=(-1)^e Delta_I^2 product_I beta.
  ```

  Do not enumerate the `binomial(2e,e)` minors. A useful donated classifier
  should derive a small, profile-forced set of minors from the Forney and
  resultant data and test only those with exact determinant certificates.

  The bounded `e=3,F_101` flat frame in
  `hankel_exceptional_split_incidence_self_dual_frame/verify.py` is a required
  positive control. Future donated searches should test the first larger odd
  values of `e`, but a bare frame witness or no-hit result has no official
  force. A useful run must impose at least one additional official interface:
  the Forney weight equations, placement in one multiplicative smooth
  domain, or a proved scale-dependent invariant. Record any expensive
  large-`e` search here with a pilot cost before launch; none is authorized
  under the current local or Modal budget.

  For a candidate frame, normalize columns by `q_1(a)` and compute the
  product-space rank of `U_q^2` in `F[X]/(A)` through compressed pointwise or
  modular products. If the rank is `2e-1`, emit the unique annihilating
  functional and compare its representing class with
  `C=q_1 Phi/B_T mod A` up to scalar. If the rank is at most `2e-2`, emit two
  independent annihilators as the degeneracy certificate. The `e=3,F_101`
  positive control must report rank five and recover its unique diagonal
  weight line. Dense product matrices and unbounded rank searches remain
  unauthorized; larger runs belong in this ledger for contributors.

  The MDS-Schur router does not authorize a maximal-minor census. A donated
  packet may certify the MDS branch with a structural MDS proof plus one
  systematic generator and its `2e-1` independent product witnesses. On the
  non-MDS branch it should emit one dependent `e`-column set, its complement,
  and exact null vectors for both. Either output must then be checked against
  the Forney class; a probabilistic rank estimate alone has no proof value.

  A computation retaining only the four
  aggregate resultants is unauthorized because both endpoint profiles are
  already proved compatible at that level. Before requesting donated
  compute, bank a complete small analogue, an orbit-coverage map, a measured
  pilot, and hard RAM, wall-time, storage, and dollar ceilings. A replayable
  first-jet inconsistency would reject one endpoint profile; a finite no-hit
  result is evidence only.
- **execution shape:** checkpoint by
  `(family,shape,core,m,e,q,component packet)`, omitting `core` only for
  `A=3`; stream compact certificates and hashes; stop a shard before memory
  pressure rather than materializing all split locators. Contributors may
  parallelize independent shards, but each shard must have a declared wall,
  RAM, and dollar ceiling.
- **estimated resources:** unknown until `m=2,4` pilots; likely unsuitable for
  the current sub-`$1` policy and potentially multi-gigabyte at `m=16`.

## N11 deferred contributor certificate requests

These are prerequisite-gated requests, not authorization for a local Modal
run.  The current account is reserved for route-deciding pilots below one
dollar.  In particular, no contributor should spend compute merely to repeat
the refuted signed-core padding count in `generator_size_budget_check`: its
padding multiplicity consists of exact `e_1` collisions.

### N11-ICD: adopted-row integer distance certificate

- **consumer:** `integer_code_distance_cert`.
- **launch gate:** first bank an explicit adopted row descriptor or generator
  matrix, the intended support bound `2 l'`, and the complete cyclotomic
  relation basis.  The current node has no such fixed official object, so a
  search before this gate would not certify its statement.
- **task after the gate:** produce a proof-logged exact certificate that the
  corresponding integer relation code has no nonzero ternary kernel vector of
  support at most `2 l'`.  Suitable engines include checkpointed
  meet-in-the-middle, proof-producing SAT, or an exact lattice enumeration;
  a floating-point nearest-vector answer is not a certificate.
- **deliverables:** the canonical row object and hash, result JSON, complete
  relation/basis metadata, a deterministic independent checker, and retained
  checkpoints or proof logs sufficient to replay every excluded support
  chamber.
- **scale warning:** the existing `N'=128` cost ledger estimates about
  `2^38.34`, `2^43.46`, and `2^48.38` states at weights `12`, `14`, and `16`.
  A contributor must first run a bounded pilot and publish measured wall time,
  peak RAM, storage, and dollar cost.  Do not launch the full enumeration on
  WSL or under the present Modal budget.

### N11-U2: official Row-C per-row certificate

- **consumer:** `u2_per_row_certifier`.
- **launch gate:** first pin the exact adopted Row-C exhibit, coefficient
  domain, moment count `t`, constant `C`, and complete range of rows or `b`
  values.  Source code and a toy transcript do not satisfy this gate.
- **task after the gate:** rerun the exact multi-moment codimension-`t`
  lattice or meet-in-the-middle certification for every required row.  Claims
  involving two primes must retain both prime results and a deterministic
  checker; a Modal source file without banked outputs is not evidence.
- **deliverables:** canonical exhibit hash, per-`(prime,b)` result JSON,
  collision or exclusion certificates, an independent replay checker, and a
  manifest that proves complete coverage of the promised row range.
- **execution shape:** checkpoint separately by `(prime,b)` and retain partial
  results when a shard reaches its wall or memory cap.  Begin with one cheap
  pilot and publish measured resources before requesting a larger run.  Do not
  launch this request locally under the present Modal budget.

### N12-E1-256: completed named-field box falsifier (background exhibit)

- **status:** completed and retired from the critical route by the E1
  universal-quantifier audit. The unresolved named-field node remains
  background exhibit work; closing it would not close route-uniform E1
  control.
- **consumer:** background node `e1_folded_no_vector_certificate_256_payload`.
- **question:** does the pinned Pocklington field admit one nonzero
  `w in {-2,-1,0,1,2}^128` with `sum_i w_i rho_256^i = 0 mod p`?
- **promotion rule:** only an explicit vector accepted by
  `background/nodes/e1_folded_no_vector_certificate_256_payload/verify_falsification_campaign.py`
  falsifies the
  zero-vector leaf. A search miss is `INCOMPLETE` and changes no status.
- **campaign:** four deterministic Modal workers, seeds
  `{1729,2718,31415,65537}`, each `8` CPUs, `16 GiB`, hard timeout `240 s`.
  Each performs bounded LLL/BKZ reduction followed by exact signed sums of
  negacyclic shifts. Worker stage summaries survive ordinary completion.
- **budget:** authorized once under the route-deciding pilot rule; estimated
  total below `$0.30`, hard campaign ceiling `$0.50`, wall below five minutes.
- **artifacts before launch:** launcher and exact checker are banked; checker
  self-test rejects zero, out-of-box, non-kernel, and wrong-length mutations.
  SHA-256 pins: launcher `4d2e5f842b77dc604df58b8dad064fad6c23390aad90b8ed8b40d915f97cd326`;
  checker `cd13813d859aefb1d332a50d68dcc5b6cc08c6480dc3c447c25ee85800c94070`.
- **app/run:** `ap-uImvgijoKNeruVABf32Cc9`, completed. All four workers
  returned `NO_WITNESS_WITHIN_SEARCH_BUDGET` in `81.65--125.33 s`; campaign
  result SHA-256
  `3fcb4725226e996df9c274dd9e653e3a1354b6620c207e3c325289639f6cbcd2`.
  The exact checker reports `INCOMPLETE`, as required. The client did not
  expose a billed-dollar line; measured resources remain comfortably below
  the `$0.30` estimate. This authorization is consumed; do not scale the miss.

## CR-004 refresh (2026-07-22): the WCL slot register is now request-grade hardened

The ten-slot decomposition backing CR-004 is now MACHINE-CERTIFIED complete
(`critical/nodes/dli_wcl_zone_coverage/verify_slot_decomposition.py`, 5/5
mutation controls), conventions-audited against the closed (2,5)/(2,6)
certificates (no mismatch — a contributor sweep provably targets the right
space), exactly priced (Burnside, 3/3 calibration anchors), and
powered-sampled (934 orbits, zero events, max v_2 = 24 vs gate 41). Census
is live ONLY at: (1,5) finish (445 CPU-h total, 46.44% checkpointed),
(2,7) router (33k CPU-h; ~$2-5k after a GMP/flint gcd swap), and marginally
(1,6) (~$6.6k). The ell=4 cells are DESCENT-ONLY (proof work); (1,7)/(1,8)/
(2,8)/(2,9) need new exclusion algebra, not compute. MANDATORY implementation
constraint for any contributor: norm prime factors are NOT all == 1 mod n —
progression-based trial division is UNSOUND (full or certified-partial
factoring only; keep gp/ECM in the loop for ~150-450-bit hard cofactors).
PROMOTION GATE (unchanged): this becomes an outbound contributor request
only after (i) the order-1024 Norm(u)-saturation soundness fix lands and
audits, (ii) the GMP/flint gcd benchmark is measured, (iii) the unit-ideal
certificate pilot adjudicates (a land retires the census model entirely),
and (iv) for (1,5): the re-shard + ECM-tail repairs land.

## CR-L1-MCP: Mersenne first-checkpoint split-pencil certificate

**Status:** contributor research request; not authorized locally or on the
current Modal account. Its consumer is the `t=p` endpoint of
`l1_mixed_petal_amplification`, not the whole L1 node.

All other official minimum-width rows are theorem-classified. The only live
rows are:

```text
n            p           m
32768        8191        4
65536        8191        8
131072       8191        16
524288       131071      4
1048576      131071      8
2097152      524287      4
4194304      524287      8
8589934592   2147483647  4
17179869184  2147483647  8
```

For each row, only `2<=h<=m-1` can occur. At depth `d`, put
`u=n-hp` and `ell_h=u-d+p`; the complement theorem bounds records by
`floor(binom(n,ell_h)/binom(u,ell_h))`, and the depressed outer polynomial
has `ord_0(R)<=n-(h+1)p`. A valid implementation must exploit these facts
and the balanced prime-field cyclic-code formulation: the signed exponent
word has exactly `p` coefficients `+1`, exactly `p` coefficients `-1`, and
Fourier zeros on the full `p`-cyclotomic closure of `[0,p-1]`.
Consume `l1_mersenne_checkpoint_cyclotomic_normal_form` rather than building
that closure numerically: for `k=q(p+1)+b`, membership is decided by
`q=0` or `q=b-1 mod gcd(2b,m)`. All `p+1` consecutive frequencies in the
zeroth block vanish, and the target word has exact weight `2p` between the
proved BCH floor `p+2` and twice that floor. A proposed solver must operate
on this low-weight chamber representation and report how its quotienting
preserves the separate `+1` and `-1` weights.
Before emitting candidates, remove the exact embedded family from
`l1_mersenne_checkpoint_embedded_m2_family`: at depths `p,p+1`, each of the
`m/2` order-`2(p+1)` cosets contributes `p+1` antipodal pairs, for total
`n/2`. These are proved payload, not events. An `h=2` request must certify
that its pair is not in this family. Do not request `m=4,h=3` compute: the
Mason, Cartier, tangent, packet, and zero-`b` Euler chain proves every
official component empty. The checked two-Schur encoding remains a
conformance artifact, not a live shard. Prioritize explicitly nonembedded
`m=4,h=2` and the `m=8,16` value degrees.

**Requested outcome:** for a declared `(n,p,h,d)` shard, either emit one
fully replayable pair of disjoint split fibers, including `Q`, `G_Q`, the
complement, all divisibility checks, and its first-owner data; or emit a
proof-producing exclusion certificate whose independent checker establishes
complete coverage. A finite no-hit search is evidence only. Partial output
must preserve completed orbit or certificate blocks, hashes, elapsed CPU,
peak RAM, and the exact unprocessed range.

**Launch gate:** first supply a completeness-preserving orbit, cyclic-code,
SAT, or algebraic compression on a small analogue, then benchmark one shard
of the smallest row under explicit RAM, wall-time, storage, and dollar caps.
Raw enumeration of supports, complements, normalized `Q`, or field elements
is prohibited. The resource cost is currently unknown and could be large;
publish the pilot before requesting a full contributor run. A PR carrying
this request should include the six proved checkpoint nodes and state
exactly which PASS or witness changes the DAG.

The complete small pilot
`experiments/prize_resolution/l1_mersenne_checkpoint_analog_result.md`
exhausted all `3,365,856` seven-subsets at `(n,p,m)=(32,7,4)` in Modal app
`ap-X9B0VIv80tdRxDSfYnkG9o`. It found 16 two-fiber pencils, no `h>=3`
pencil, and maximum depth eight. The classifier rerun
`ap-mLyev4aS4qOOhZhKqcpK5i` shows all 16 observed pairs have the embedded
antipodal form. This satisfies only the small-analogue
conformance gate; it supplies no official-row throughput or cost estimate.

### CR-L1-MCP-A8: complete order-64 analogue

This is the next useful donated-compute falsifier and must not run on the
current account. Work over `F_(7^8)` on the order-64 subgroup, with
`(n,p,m)=(64,7,8)`. Enumerate all

```text
binom(64,7)=621,216,192
```

seven-subsets, group their monic locators by coefficients in degrees one
through six, and classify every group by exact split-value degree, maximum
checkpoint depth, subgroup-coset support, and the embedded antipodal test.
The result decides whether the complete `m=4` analogue behavior persists
when the quotient multiplicity doubles: any nonembedded `h=2` group or any
`h>=3` group is a replayable route-changing witness; complete absence is
evidence for an embedded-family/low-weight classification theorem.

A naive 16-byte record stream is about `9.26 GiB` before sorting, so the run
must shard by a prefix of the six-coefficient signature and merge only group
boundary summaries. Each shard must checkpoint its exact combinadic range,
record count, signature-prefix interval, rolling hash, group histogram, and
all groups of size at least two. An independent checker must rebuild every
reported locator and verify roots, common prefix, disjointness, depth, and
embedded status. Publish a one-shard benchmark with CPU time, peak RAM,
scratch storage, and projected dollar cost before requesting the full run.
Timeout or incomplete shard coverage is `INCOMPLETE`, never evidence of
absence. The order-128 analogue has `94,525,795,200` subsets and roughly
`1.38 TiB` of raw records, so it is not requested without a new structural
compression.

### CR-L1-MCP-NMCE: constant-Euler next-to-maximal passport classification

**Status:** every order-zero next-to-maximal chamber is theorem-empty and
RETIRED from this request: four `m=8,h=7` rows and the `m=16,h=15` row. Only
the order-one chambers remain a valuable outbound research-compute
pre-request with unknown cost. Benchmark and price one smallest unresolved
order-one chamber before any extension.

**Pre-registered bounded analogue pilot `HNF-TOY-GCD`.** One 1-CPU, 1-GiB,
120-second Modal task may compute the exact common-remainder gcd for
`(m,h,p,n)=(8,7,31,256)`, remove its `F_p` factor via `s^p-s`, and emit all
remainder and factor coefficients. Its deterministic local checker replays
the same low-degree algebra. A nonconstant outside-prime-field quotient
falsifies analogue emptiness; a unit quotient is calibration only, not an
official theorem. No second case or official row is authorized by this
pilot.

The first launch, Modal app `ap-zbyPpAZamkVE3AlXYQJzov`, failed during
setup: SymPy's `Poly.rem` could not coerce `F_31[s]` to its fraction field.
It returned no mathematical output. The corrected launcher declares
`F_31(s)` directly; because the divisor is monic in `W`, the computed
remainders remain in `F_31[s]`. One corrected retry remains within the same
bounded-pilot authorization.

The corrected pilot completed as Modal app
`ap-gT0DyToHmnD911PEFFilTd` in `2.805886` worker-seconds. Its exact common
gcd is `s-1`; this is wholly the `F_31` factor, so the outside-prime-field
quotient is the unit polynomial. The analogue therefore has no live
order-zero survivor. The full remainder payload is hash-pinned and locally
replayed by `check_l1_mersenne_hnf_toy_gcd.py`. This calibrates the proposed
gcd route but proves nothing on an official characteristic. No further local
or Modal case is authorized; official and larger rows remain outbound
contributor requests.

**Pre-registered bounded analogue pilot `FRG-SAT-P31`.** The new Frobenius
reciprocal gate authorizes one exact saturation benchmark at
`(p,m,h)=(31,8,7)`. One 1-CPU, 2-GiB Modal task has a 120-second hard stop and
must report resultant time, equation count/degrees, Groebner-basis
count/degrees, peak memory, and whether the saturation by `t-s` is unit. A
unit result is analogue calibration only; a nonunit result records the
candidate-component size. Timeout or setup failure is `INCOMPLETE`. No
official characteristic or second saturation is authorized by this pilot.

The pilot ran as Modal app `ap-0EK5ErTdMIAYixk0Leq78F`. Polynomial and
resultant construction took `0.067027` and `0.567595` seconds; by
`5.970123` seconds it had produced seven nonzero equations of maximum total
degree `112`. SymPy's generic grevlex Groebner saturation then hit the
120-second timeout. Status is `INCOMPLETE`: there is no unit/nonunit result
and no mathematical evidence. Do not retry this backend locally or on the
current Modal account. A contributor should use Singular, Magma, or a
structure-aware two-variable elimination and return either a checkable unit
certificate or a complete component decomposition. This measured algebra
task is now preferable to any expanded degree-`n` remainder campaign.

The later proved node
`l1_mersenne_hnf_m8_order_zero_reciprocal_elimination` supersedes that
incomplete analogue for every official `m=8` order-zero row. It reconstructs
the reciprocal coefficients by two independent exact implementations and
shows that the gcd of the first-three-equation eliminants has only prime-
field roots in all four official characteristics. Do not run an `m=8`
official saturation or classify cubic and higher `m=8` colors: that chamber
is closed.

The following order-zero specification is retained as historical provenance;
it is no longer live. The live part of this request is now only the order-one
residue of `l1_mersenne_next_to_maximal_hypergeometric_normal_form`. The
retired order-zero row was

```text
(m,h,p)=(16,15,8191),
```

The four former `m=8` triples and this `m=16` triple remain in the historical
pilot record only.

The outer stage has a monic depressed squarefree polynomial `G` of degree
`h` and a nonzero scalar `lambda=m alpha/q`. Put

```text
T=hG-YG',
r=ord_0(T),
S=the monic associate of T/Y^r,
B=(G-lambda Y)/(Y^r S).
```

Every survivor satisfies

```text
S is nonconstant and squarefree,
gcd(S,Y)=1,
deg T=h-2,
r in {0,1},
deg B=2,       B(R(0))=0,
deg rad(R-R(0))+deg rad(R-z)=p+m+1,                 (NMCE-OUT)
```

where `z` is the other root of `B`. The two radical factors reconstruct all
of `D`, and the corresponding two gcds with `R'` reconstruct all of `R'`.
In addition put

```text
P(W)=(z-R(0))^(-h)G(R(0)+(z-R(0))W).
```

The shifted-value theorem requires `P | W^(m(p+1))-1`. If `z!=0`, delete
every chamber for which both

```text
c=z/R(0),       theta=2[Y^(h-2)]G/(R(0)z)
```

lie in `F_p`: that entire branch is theorem-empty. The `z=0` chamber is also
theorem-empty. A retained chamber must include a direct Frobenius certificate
proving that at least one of `c,theta` is outside `F_p`.

The same theorem supplies a differential prefilter. With
`K=2[Y^(h-2)]G*lambda/(z-R(0))^(h+1)`, every normalized nonzero split value
obeys `x(x-1)P'(x)=K`. In the `ord_0(T)=0` chamber, require the exact identity

```text
W(W-1)P'(W)-K=(hW+b)P(W)
```

for some scalar `b`. In the `ord_0(T)=1` chamber, divide `P` first by the
known root `W=-R(0)/(z-R(0))` and require the resulting divisibility. Reject
before any inner stage if either differential check fails.

Do not begin from free coefficients of `G`. The proved normal form splits
the outer stage into exactly two low-dimensional tasks.

- For `ord_0(T)=0`, put `s=h/(c-1)` and use only

  ```text
  P_s(W)=sum_(r=0)^h binom(s+r-1,r)W^(h-r).
  ```

  First form

  ```text
  Q_s(Z)=Res_W(P_s(W),Z-W^m)=sum_(j=0)^h q_j(s)Z^(h-j)
  ```

  and compute the saturation by `t-s` of

  ```text
  Q_s(0)q_j(t)-q_(h-j)(s)=0,       0<=j<=h.
  ```

  This bounded-degree Frobenius reciprocal system is the first target. A
  verified unit saturation closes the chamber. For each retained component,
  impose `t=s^p`; only then compute the gcd over `F_p[s]` of the coefficient
  remainders of `W^n-1 mod P_s` and remove its gcd with `s^p-s`. A complete
  unit quotient closes the remaining chamber. Any retained irreducible
  factor must include an exact algebraic representation of `s`, replay of
  `s notin F_p`, and the zero remainder certificate.

  For the live `(m,h,p)=(16,15,8191)` chamber, `deg_s q_j<=16j`. The raw
  interpolation bounds for

  ```text
  Res_t(F_1,F_2),       Res_t(F_1,F_3)
  ```

  are respectively `11520` and `15360`. The latter exceeds `p`, so a
  base-field evaluation grid cannot certify the polynomial by ordinary
  interpolation. A contributor implementation must instead use exact
  symbolic elimination, extension-field interpolation with a replayable
  descent certificate, or a proved factor/saturation reduction. Before a
  full run, publish a measured pilot that constructs enough of one eliminant
  to validate the representation and gives a conservative peak-RAM,
  wall-time, and dollar bound. The local `m=8` timings (about 12 seconds for
  the primary verifier and 10 seconds for its independent audit) are not a
  cost model for this larger system.

  **One-eliminant Singular pilot authorization (2026-07-26).** The later
  under-five-minute and under-`$1` compute law authorizes exactly one
  route-pricing run of
  `experiments/prize_resolution/l1_mersenne_m16_r12_singular_pilot_modal.py`.
  It uses one CPU, 2 GiB, one container, a 180-second outer timeout, and a
  165-second Singular timeout. It may construct `Q_s` and only
  `Res_t(F_1,F_2)` at `(p,m,h)=(8191,16,15)`, returning degree, term count,
  digest, wall time, and peak RSS. It must not launch `R_13`, a saturation,
  extension-field interpolation, or a retry. Completion is representation
  and cost evidence only. Timeout or error is a route fence; a successful
  run authorizes no follow-on computation until its measured cost and output
  shape have been audited.

  **Attempt result (2026-07-26): `INCOMPLETE`.** The single launch was Modal
  app `ap-wGlT1diHx4C7gUii0LhVyq`. The default Debian package recipe selected
  891 new packages and 29 upgrades (1,077 MB of archives; 4,098 MB installed),
  so the app was stopped at package 310 before image completion or any
  algebra. The same-day billing report records `$0.00340405` CPU plus
  `$0.00007667` memory, or `$0.00348072` total. No retry or second eliminant
  ran. The launcher has been corrected to suppress Debian recommends, but is
  not authorized for another run by this attempt. Exact replay metadata is in
  `experiments/prize_resolution/l1_mersenne_m16_r12_singular_pilot_result.json`.
  This is an infrastructure fence only and yields no mathematical or DAG
  movement.

  **Resolved (2026-07-27): RETIRED.** Under the current sub-five-minute and
  under-`$1` compute law, the corrected exact pilot completed and was followed
  by one independent companion-matrix audit. The eliminants have degrees
  `11472,15296`; their degree-`9912` gcd has squarefree radical

  ```text
  s(s-1) product_(j=1)^15(s+j),
  ```

  which divides `s^8191-s`. The primary resultant construction and the
  companion-matrix/Newton construction reproduce all four polynomial hashes.
  `l1_mersenne_hnf_m16_order_zero_reciprocal_elimination` is therefore
  PROVED and the complete order-zero outer chamber is empty. Apps
  `ap-TFttWNnwIi68tCQ3n32vBn` and `ap-myN6sycfDSBAi2okj8hc2P` used one CPU,
  `110 MB`, and `16.75/12.79` seconds; the exact bill was not queried and the
  full campaign is conservatively below `$0.05`. Do not run any further
  `m=16` order-zero elimination, remainder, or color-degree job.

  A unit outside-prime-field locus closes the complete `m=16` order-zero
  outer chamber. A nonunit result must return an exact irreducible component
  or algebraic witness candidate, then impose `t=s^p` and the cyclotomic
  divisibility before it can count as an outer survivor. A timeout, modular
  no-hit, partial interpolation, or projected-cost estimate is `INCOMPLETE`.

- For `ord_0(T)=1`, normalize `g(y)=R(0)^(-h)G(R(0)y)`,
  `A=[Y^(h-2)]G/R(0)^2`, and `c=z/R(0)`. Generate every coefficient by
  the registered top-down recurrence (HNF3), put
  `rho=2A/[c(c-1)]`, and impose its closed-form last equation
  `Phi_h(rho,c)=[t^h](1-t)^(c rho)(1-ct)^(-rho)=0`.

  First consume
  `l1_mersenne_hnf_order_one_involution_component_exclusion`. Exact
  factorization gives

  ```text
  h!*Phi_h = content*rho*c*(c-1)*(c+1)*Psi_h.
  ```

  The first three factors are already outside the chamber, and `c=-1` is
  impossible by `(c-1)^n=1` on all five official rows. Saturate by `c+1`
  and use only `Psi_h=0`: its bidegree in `(rho,c)` is `(2,4)` for `h=7`
  and `(6,12)` for `h=15`. Do not send the deleted involution component to
  a Groebner worker.

  The generic reduced resultant is also retired as the primary
  representation. The bounded SymPy campaign
  `l1_mersenne_m8_order_one_reciprocal_profile` exhausted 315 aggregate app
  seconds without completing `Res_W(L,Z-W^8)`; apps
  `ap-2JqEoR1tUWnWY1uaGIpxzh`, `ap-0Zf035x3KMj8qBJ7V8FtBT`, and
  `ap-UxUdP4JCXNMzidTip4FogP` are `INCOMPLETE` and authorize no retry.
  Exact partial metadata pins the cancelled degree-six quotient at 77 terms
  with denominator `720*(c-1)^6`. There is no mathematical verdict.

  Instead consume
  `l1_mersenne_hnf_order_one_newton_reciprocal_reduction`. If `x_i` are
  the roots of `L`, generate the first three reciprocal equations as the
  Newton equalities between `(x_i^star)^m` and `x_i^(-m)`. This needs only
  traces at powers `8,16,24` for `m=8`, or `16,32,48` for `m=16`; it never
  materializes `Qtilde`. Then consume
  `l1_mersenne_hnf_order_one_full_trace_cancellation`: the known root has
  identical star and inverse `m`-power traces, so the same equations can be
  generated from the original degree-`h` polynomial `P` without first
  dividing by `W-x_0`. A future contributor computation should eliminate
  this full-`P` trace system on `Psi_h=0`, return every denominator and
  saturation factor, and use a second implementation to reconstruct the
  same full traces from the companion matrix. The divided `L` construction
  is now audit-only. Price the `h=7` first-three system before attempting
  `h=15`.

  For that `h=7` price, consume
  `l1_mersenne_hnf_m8_order_one_conic_reduction`. The residual input is

  ```text
  35u^2+14(11c^2+5c+11)u+120(c^4+c^2+1)=0,
  u=rho*c*(c-1),
  ```

  equivalently the conic `7w^2=247z^2+770z+775` plus
  `c^2-zc+1=0`. Benchmark both the direct quadratic and conic-pullback
  representations; retain the cheaper exact one. The `t=infinity`, tangent,
  and denominator-zero charts are mandatory finite shards. A generic reconstruction
  of the old ten-term `Psi_7` is no longer the preferred input.

  Apply `l1_mersenne_hnf_m8_order_one_basefield_conic_router` before pricing
  that system. The `z=-1` points and the complete `t in F_p` branch at
  `p=8191,131071` are theorem-empty. At `p=524287,2147483647`, the same
  branch has at most two packets:

  ```text
  zeta=-1, z=3, c^2-3c+1=0, 7w^2=5308,
  theta=(w-38)/5, rho=theta/(c-1), rho_star=-c*rho.
  ```

  **Retired by proof:**
  `l1_mersenne_hnf_m8_order_one_basefield_branch_exclusion` proves that the
  finite packets are empty too. Frobenius reflection leaves at most six
  possible split roots for the degree-seven polynomial. Do not replay any
  `t in F_p` packet. The only `h=7` elimination request is now
  `t notin F_p`.

  **Cheap exact request CR-L1-H7-Q2-PAIR:** consume
  `l1_mersenne_hnf_m8_order_one_quadratic_two_pair_univariate_reduction`.
  In the quadratic color chamber with two antipodal repeated pairs, use

  ```text
  F(X)=5X^8+10X^7-180X^6+672X^5+2862X^4
       -15516X^3+8199X^2-44172X+4860.
  ```

  For each of the four official primes, construct `F_(p^2)` explicitly,
  enumerate `zeta in mu_8`, and return

  ```text
  gcd(F(X),X^(p+1)-zeta)
  ```

  with monic factors and witnesses. There are exactly 32 degree-eight
  packets; modular exponentiation must reduce after every multiplication.
  Independently replay any nonunit gcd by substituting its roots into the
  conic and `r=-192/(18+X-X^2)`. A unit result in all 32 packets closes only
  the two-antipodal quadratic chamber. This should cost far below one dollar,
  but no launch is authorized while the current Modal workspace reports its
  spend limit exceeded. The resumable 32-container launcher is
  `background/nodes/l1_mersenne_hnf_m8_order_one_quadratic_two_pair_univariate_reduction/modal_gcd.py`;
  it uses 128 MiB and a 60-second hard timeout per packet and writes after
  every returned result.

  The aggregate alternative is the shared launcher
  `experiments/prize_resolution/l1_m8_h7_low_degree_norm_endpoints_modal.py`.
  Its four `q2_pair_degree8` rows replace the 32 individual color packets;
  split by `zeta` only if an aggregate gcd is nonunit. The equivalence is
  proved by `l1_mersenne_hnf_m8_aggregate_norm_gcd_compiler`.

  **Cheap exact request CR-L1-H7-Q2-ALL:** consume
  `l1_mersenne_hnf_m8_order_one_quadratic_hnf_intersection`. Construct the
  fixed degree-fourteen polynomial `R_2` from the factored resultant (QHI4),
  independently verify leading coefficient `-691200`, and compute

  ```text
  gcd(R_2(X),X^(p+1)-zeta)
  ```

  for all four official primes and eight `zeta in mu_8`. Return monic gcds
  and partial output after every packet. Unit gcds in all 32 packets close
  the complete quadratic-color chamber. Run the degree-eight
  `CR-L1-H7-Q2-PAIR` first or in parallel as an independent specialization.
  This packet is also tiny, but no launch is authorized while the Modal
  workspace spend limit remains active.

  The same aggregate launcher has four `q2_all_degree14` rows. Unit results
  there close the complete quadratic-color chamber and make the pair rows
  audit-only.

  **Retired exact request CR-L1-H7-C3-33:** the former request consumed
  `l1_mersenne_hnf_m8_order_one_cubic_two_triple_reduction`. Construct the
  degree-fourteen polynomial `R_33` from (CTR4), independently verify
  leading coefficient `-576000`, and compute

  ```text
  gcd(R_33(X),X^(p+1)-zeta)
  ```

  for all four official primes and eight `zeta in mu_8`. Return monic gcds
  and partial output after every packet. This packet must not be launched:
  `l1_mersenne_hnf_m8_order_one_cubic_two_triple_exclusion` proves the
  chamber empty from the unused `W^2` coefficient and the base-field norm
  obstruction. Every other cubic partition remains open.

  **Contributor request CR-L1-H7-C3-3COL:** consume
  `l1_mersenne_hnf_m8_order_one_cubic_three_color_remainder_router`. Start
  with the seven p-free color-set representatives in (TCR1). For each one,
  construct the monic HNF sextic `L_(r,d)`, a generic exact cubic `E`, the
  six coefficients of

  ```text
  rem_L product_(j in T)(E-omega^j),
  ```

  and the three nonempty-fiber resultants. Saturate by the HNF denominators,
  `d*(d+1)*r*(r-1)*g(1)*disc(L)*lc(E)`, and classify dimensions before any
  official-row norm equation. If a color-set core survives, split it into
  the six ordered `3+2+1` profiles and the one `2+2+2` profile using exact
  subresultant degree; only then shard retained components by four rows and
  eight norm colors. This is at most 49 profile cores before row sharding,
  not 56 triples times root assignments. Use 60-second shards, emit partial
  ideals/components after every packet, and report estimated cost before a
  larger continuation. Do not launch on the current spend-blocked account.

  For the `2+2+2` profile, replace the generic remainder stage by
  `l1_mersenne_hnf_m8_order_one_cubic_three_double_factor_reduction`.
  Expand

  ```text
  product_(i=1)^3 (W^2+u_iW+u_i^2-Uu_i+V)=L_(r,d)
  ```

  coefficientwise, adjoin the h=7 conic, and only then impose one ordered
  scale-free color ratio from (TDF4). This factor packet has variables
  `(u_1,u_2,u_3,U,V,r,d)` and seven carrying equations before the color
  ratio; eliminate symmetric functions of the `u_i` before any Groebner
  basis. Keep the generic remainder only as an independent audit.

  The symmetric elimination is now printed in
  `l1_mersenne_hnf_m8_order_one_cubic_three_double_symmetric_compiler`.
  Generate `s_1,V,s_3` from (TSC2), substitute into (TSC4)--(TSC6), clear
  `2*3*d*(r-1)` with inherited saturation retained, and classify the four
  equations in `(U,s_2,r,d)` before adding a color ratio. Record the cleared
  polynomials and their degrees even if the ideal is nonunit; those are the
  portable handoff, not a raw Groebner transcript.

  The exact next compiler is now
  `l1_mersenne_hnf_m8_order_one_cubic_three_double_linear_remainder_reduction`.
  Use its scaled variables `(x,b,q,d)` and retain `D_b=0`. The reduced fifth
  and sixth coefficient equations are affine-linear in `b`; the former has
  slope `-x(x^2+q/6)`. Classify the two exceptional branches `x=0` and
  `q=-6x^2` first. On the generic branch solve the fifth equation for `b`,
  substitute into both `D_b` and the sixth remainder, and eliminate only
  `(x,q,d)`. A determinant of the two linear remainders is not a complete
  replacement for the equations. Return factorizations and saturation
  factors branch by branch before any color or official-row sharding.

  **Pre-request CR-L1-H7-C3-222-GEN:** the generic compiler has since been
  sharpened analytically. Consume, in order,

  ```text
  l1_mersenne_hnf_m8_order_one_cubic_three_double_affine_color_compiler,
  l1_mersenne_hnf_m8_order_one_cubic_three_double_affine_invariant_formula,
  l1_mersenne_hnf_m8_order_one_cubic_three_double_quadratic_quotient_weld.
  ```

  Do not restore the individual `u_i`, enumerate 42 ordered roles, or form
  the raw value resultant. The seven affine color values have the exact
  polynomial

  ```text
  (T+50)(T^2-224T-578)(T^2-4T+54)
  (125T^2-2404T+13448),
  ```

  and become four rational homogeneous factors in `P^3,Q^2`. Modulo
  `D_b`, each factor is affine-linear in `p=b-12`. On
  `alpha=-(q-d)x(x^2+q/6)!=0`, each packet is equivalent to (QQW7): the
  conic, the `D_b/M_5` compatibility, the `M_5/M_6` compatibility, and one
  color/`M_5` compatibility, all in `(x,q,d)`.

  The requested decision is whether each of those four saturated rational
  ideals is unit. A PASS must provide a replayable Nullstellensatz or
  transformation-matrix certificate for every unit packet, with every
  denominator/content prime checked against all four official
  characteristics. A FAIL must provide a retained exact component or point,
  its saturation ledger, and substitution into the unreduced `D_b,M_5,M_6`
  and homogeneous color factor. Emit the four compiled ideals and hashes
  before starting elimination, then checkpoint every factor/component.

  This remains a **pre-request**, not authorization: a proof-producing CAS
  launcher, independently written certificate checker, measured one-packet
  pilot, and conservative total cost are missing. The current Modal workspace
  is spend-blocked. An incomplete or ordinary Groebner transcript is route
  evidence only and cannot close the generic branch.

  **Contributor request CR-L1-H7-C3-222-X0:** consume
  `l1_mersenne_hnf_m8_order_one_cubic_three_double_x0_quintic_reduction`.
  Independently reconstruct

  ```text
  P_5(X)=60X^5+407X^4+1147X^3+1659X^2+1218X+360
  ```

  from (XQ2)--(XQ6), then compute

  ```text
  gcd(P_5(X),X^(p+1)-zeta)
  ```

  for all four official primes and eight `zeta in mu_8`. Return every monic
  gcd and partial output after each packet. Unit gcds in all 32 packets close
  the complete `x=0` branch. For a nonunit gcd, recover `q` from (XQ5) and
  apply `D_b`, `M_6`, and the color ratio before any larger lift. This is a
  degree-five packet and should be priced below one dollar, but do not launch
  while the configured Modal workspace remains spend-blocked.

  **Contributor request CR-L1-H7-C3-222-Q6X2:** consume
  `l1_mersenne_hnf_m8_order_one_cubic_three_double_q6x2_degree12_reduction`.
  Independently reconstruct `E`, `F`, and

  ```text
  R_12=105F^2+7AFE+10BE^2
  ```

  from (QDR2)--(QDR7), verify degree 12 and leading coefficient `149868`,
  then compute `gcd(R_12(X),X^(p+1)-zeta)` for all four official primes and
  eight `zeta in mu_8`. Return every monic gcd and partial output after each
  packet. Unit gcds in all 32 packets close the complete `q=-6x^2` branch.
  For a nonunit gcd, reconstruct `y`, check the unsquared equation (QDR3),
  and only then apply `D_b`, `M_6`, and the color ratio. This is a degree-12
  packet and should be priced below one dollar, but do not launch while the
  configured Modal workspace remains spend-blocked.

  Both exceptional requests now share the bounded launcher
  `experiments/prize_resolution/l1_m8_h7_low_degree_norm_endpoints_modal.py`.
  It uses one 512 MB container, a 60-second hard timeout, and emits each
  completed endpoint/prime row immediately. Instead of constructing eight
  separate color fibers, it computes the equivalent aggregate gcd

  ```text
  gcd(P(X),X^(8(p+1))-1)
  ```

  over `F_p`; a unit result is equivalent to all eight individual gcds being
  unit after adjoining `mu_8`, by
  `l1_mersenne_hnf_m8_aggregate_norm_gcd_compiler`. There are exactly eight
  rows total: two cubic endpoint polynomials times four official primes.
  Together with the
  quadratic degree-eight and degree-fourteen endpoints, the launcher has 16
  rows total. Split by `zeta` only if
  an aggregate row is nonunit. The launcher is ready but remains unexecuted
  under the current spend block. Pass `--output PATH` to bank the returned
  JSON, then validate it with
  `experiments/prize_resolution/check_l1_m8_h7_low_degree_norm_certificate.py`.
  The source and checker digests are pinned in the roadmap.

  For the `3+2+1` profile, replace the generic remainder by
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_factor_reduction`.
  Parameterize monic cubics `F,G`, impose `FG=L_(r,d)`, and compare the three
  coefficients of

  ```text
  Res_W(G,X-F)=X^3-(2+lambda)BX^2
                    +(1+2lambda)B^2X-lambda B^3.
  ```

  Run the 42 color-role values of `lambda` only after a shared symbolic
  coefficient compiler is built. Saturate by `B`, discriminants, and exact
  gcd-degree subresultants; add official norm equations only to retained
  p-free factors.

  The shared compiler is now
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_common_quadratic_compiler`.
  Construct `Q,G,F` from (TQC1)--(TQC3), eliminate `a,g_2,B` with (TQC6),
  and substitute into (TQC5), the conic, and (TQC7). Record the five cleared
  equations in `(g_1,y,r,d)` once with symbolic `lambda`; specialize the at
  most 42 role values only after common factors and saturation branches are
  classified. Retain `a*B*(lambda-1)*Q(y)`, HNF denominators, squarefreeness,
  and exact gcd degree. Return p-free unit certificates or retained
  components before any official norm sharding.

  The role set is now compiled by
  `l1_mersenne_hnf_m8_cubic_three_two_one_role_polynomial_compiler`. Construct

  ```text
  Lambda_321(lambda)=
    Res_U((U^8-1)/(U-1),((1+lambda(U-1))^8-1)/(lambda(U-1)))
    /(lambda-1)^7
  ```

  using the equivalent polynomial `C(1+lambda(U-1))` formulation printed in
  (RPC2), verify degree 42, and adjoin it before the shared elimination.
  Factor or squarefree-reduce retained lambda components only afterward; do
  not specialize 42 role values at input.

  **Pre-request CR-L1-H7-C3-321-GEN:** the role endpoint is now smaller.
  Consume

  ```text
  l1_mersenne_hnf_m8_cubic_three_two_one_role_factor_compiler,
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_role_weld.
  ```

  `Lambda_321` factors over `Q` into four packets of degrees
  `6,12,12,12`. With

  ```text
  R=a(3y^2+2g_1y+g_2), S=B,
  A_0=S^2+RS+R^2,
  B_0=(2S+R)(S+2R)(R-S),
  ```

  the linear role equation gives `lambda=1+R/S`, and the four factors become
  the four homogeneous equations (TRW4). Each packet is exactly five
  equations in `(g_1,y,r,d)`: (TQC5), the conic, and one welded role factor.
  Do not include `lambda`, cyclotomic coefficient extensions, or scalar role
  enumeration in a new elimination.

  There is also an exact lower-degree representation from
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_galois_role_weld`.
  The 42 ordered roles split into three quadratic and nine quartic rational
  Galois packets. Homogenizing each packet at `lambda=1+R/S` gives an exact
  **disjunction** of twelve systems, each with a role equation of degree at
  most four. A pilot should benchmark this twelve-branch representation
  against the four-factor representation and retain the cheaper one. Never
  impose all twelve packet equations simultaneously.

  On the four official characteristics there is a third complete
  representation from
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_official_frobenius_role_split`.
  Since `p=7 mod 8`, the nine quartics split over `F_p` into eighteen
  irreducible quadratics; together with the three rational quadratic packets
  this gives 21 branches whose role equation always has degree two. Benchmark
  this official-field representation as well. Its square-root choice only
  swaps signed branch pairs, and its 21 equations are alternatives.

  The 21-branch input is printed without hidden substitutions by
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_scaled_quadratic_core_compiler`.
  Use its variables `(x,Y,q,d)`, equations `(E_4,E_5,E_6)`, the conic, and
  `Phi(R_D,S_D)`. The sixth equation forces `D=YV!=0`; the fifth equation
  has already cleared `q-d`. Do not restore `(g_1,y,r,B,lambda)` in the
  elimination input.

  The coefficient-matrix router further splits these ideals. On the generic
  `Delta!=0` branch use the two Cramer equations (CMR3). On `Delta=0`, retain
  both exact chambers in (CMR4). The `J=0` chamber has the especially small
  endpoint `(conic,F_J,F_W)` in `(q,d)` before `E_6`, role, and arithmetic
  filters. A pilot should try this chamber first and emit a rational
  resultant/Bezout certificate rather than a raw Groebner transcript.

  **Pre-request CR-L1-H7-C3-321-J0-GCD:** the `J=0` chamber is now a fixed
  degree-7/degree-10 gcd packet. Consume
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_singular_j0_univariate_reduction`
  and compute `gcd(P_W,P_C)` over each of the four official prime fields.
  PASS requires monic unit gcd plus extended-Euclidean Bezout coefficients
  replayed against the exact integer source polynomials. FAIL requires the
  complete monic gcd and its roots/factors, with `d=-144q/A(q)` replayed in
  `(F_J,F_W,Conic)` before applying `E_6` and role filters.

  The source-pinned packet is now written:

  ```text
  experiments/prize_resolution/l1_m8_h7_cubic_321_singular_j0_gcd_modal.py
  sha256 39ccbf6493dc3a421935dbbd0b1e31e761c4e13b2c3f48eaa3c6b87d44a987e0

  experiments/prize_resolution/check_l1_m8_h7_cubic_321_singular_j0_gcd_certificate.py
  sha256 a653511eb927b1627258d7c2e25e6b46439827140d1fabab743a2404e771469c
  ```

  Launch with `modal run ...gcd_modal.py --output PATH`; validate with the
  checker, adding `--require-all-unit` for a chamber-exclusion certificate.
  The checker independently reconstructs `P_W,P_C`, verifies monic
  divisibility and the emitted Bezout identity, and accepts exact HIT rows
  without misclassifying them as closure.

  This subrequest should cost far below one dollar: four gcds of degrees 7
  and 10 in one 0.125-CPU, 128 MB, 30-second, single-container job. Source,
  checker, timeout, memory, and cost ceiling are ready; no measured pilot or
  run exists because the current Modal workspace is spend-blocked. Do not
  launch until spend access changes explicitly.

  **Pre-request CR-L1-H7-C3-321-FPQ-QUOTIENT:** the final fully proportional
  generic coefficient pair is now a quadratic in `q` plus a compatibility
  polynomial of `q`-degree at most six. Consume
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_q_quotient_router`
  and
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_structural_consistency_compiler`,
  together with the parallel exceptional-`E_G` router and structural
  compiler, the exceptional singular-affine two-quartic router, and the
  exceptional `J_*=0` affine router.
  Its exact recurrence leaves `rho_1(b)q+rho_0(b)` modulo `F_b`; off the two
  printed singular charts it reconstructs `q` and leaves

  ```text
  U(b)=a_2rho_0^2-a_1rho_0rho_1+a_0rho_1^2,
  deg U<=58.
  ```

  The source-complete packet is

  ```text
  experiments/prize_resolution/l1_m8_h7_cubic_321_fully_proportional_q_quotient_modal.py
  sha256 421ef85dbe2f6a5154c348999de3cb79df182cb903d308ba3247575b3c3c2b16

  experiments/prize_resolution/check_l1_m8_h7_cubic_321_fully_proportional_q_quotient_certificate.py
  sha256 e42629a472339216a8dca3532b43300cb34202f539312458e7adca523bd2e61f
  ```

  It runs one independent one-CPU, 512 MB, 60-second task per official prime,
  with at most four containers and no retries. The driver atomically rewrites
  the output after every returned prime, so a timeout or task failure leaves
  a checkable partial certificate. Each row must provide a complete
  factorization of `U`, extended-Euclidean certificates for
  `gcd(rho_1,rho_0)` and for the fixed `a_2=0` chart, the complete factor list
  for `b`, the official cyclotomic-field subset of degrees `1,2,4,8`, and the
  degree-one/two subset as an explicit quadratic-subfield diagnostic. The
  coefficient-field router proves `b in F_(p^8)`, so the cyclotomic subset is
  an exact official-row filter. The quadratic subset alone is never a closure
  test. The packet also reconstructs the primitive integer numerators
  `Z_D,Z_Q,Z_R`, checks
  their proved total-degree bounds `18,10,15`, computes each `Zhat_i mod U`
  without allowing intermediate degree above 57, and emits a four-polynomial
  Bezout certificate for `gcd(U,Zhat_D,Zhat_Q,Zhat_R)`. The checker
  independently reconstructs all source polynomials, verifies factor
  multiplication, both pairwise Bezout identities, all three quotient-filter
  remainders, and the four-way Bezout identity. It accepts partial packets
  unless `--require-complete` is requested. In the same row it reconstructs
  `V_E,X_E,Zhat_D^e,Zhat_Q^e,Zhat_R^e`, reduces the last four modulo
  `V_E`, and emits an independently checked five-way Bezout certificate.
  Finally it reconstructs the degree-four singular-affine pair `H,K`, emits
  a pairwise Bezout gcd certificate, factors that gcd, flags every factor
  lying on the separately excluded `A=1575-247z=0` chart, lists every
  remaining legal factor regardless of degree, separately lists the exact
  degree-`1,2,4,8` cyclotomic-field subset, and lists the degree-one/two
  diagnostic subset. The checker independently reconstructs `A,H,K`, checks
  the gcd and factorization, and recomputes all three classifications.
  It also reconstructs the `J_*=L_*=0` coefficient-and-structural filters
  `Bhat,Ehat,Fhat,Xhat,Zhat_D^j,Zhat_R^j` of degrees at most
  `6,7,10,11,24,16`, emits a six-way Bezout certificate for their common
  gcd, factors that monic gcd, flags every factor dividing the proved
  denominator `T`, lists every remaining legal factor, separately lists the
  degree-`1,2,4,8` cyclotomic-field subset, and lists the degree-one/two
  diagnostic subset.
  The checker independently reconstructs all seven source polynomials,
  verifies the six-way Bezout identity and complete factorization, and
  recomputes the `T` guard and field-degree classifications.
  The packet now also constructs the 21 official role alternatives without
  intersecting them. For each role it instantiates the proved
  `Lhat_Phi,What_Phi` templates, emits an eight-way Bezout certificate for
  the six shared filters plus those two role filters, factors the common
  gcd, and repeats the `T`-guard and exact degree-`1,2,4,8` eligibility
  classification. The checker independently reconstructs the three base
  roles and nine signed `sqrt(2)` template pairs, verifies their nonzero
  nonsquare discriminants, re-instantiates both role polynomials, and checks
  all 21 eight-way certificates and classifications. The role-summary status
  is `ALL_EMPTY` only when all 21 alternatives are official-field empty;
  any eligible factor gives `HIT`, while any identically-zero family makes
  the summary `INCONCLUSIVE`.

  For every official-field-eligible role factor, the same source now compiles
  the proved J-zero guard ledger before any finite-field root construction.
  Each cleared guard reduces modulo the irreducible `b` factor and
  `c_0 eta^2+c_1 eta+c_2` to `u(b)eta+v(b)`. Its exact quadratic norm
  distinguishes `PASS`, `ONE_FAIL`, and `BOTH_FAIL`. The product of all
  guards is reduced independently and reported as `BOTH_ETA_BRANCHES`,
  `ONE_ETA_BRANCH`, or `ALL_ETA_REJECTED`; individual remainders and norms
  retain the named rejection reasons. This quotient-ring test consumes
  `b(b+3)D_*Tq d(d+1)(q-d)Delta W K_6R_j eta(eta+1)`, both scaled
  discriminants, and `Lhat(-1)`. It does not choose a normalized color pair,
  test the norm or degree-six outer congruence, or construct the inner lift.
  The checker independently regenerates every guard template, remainder,
  norm, per-factor ledger, and row summary.

  The four small degree-58 factorizations should cost below `$0.01`. This
  request gives a structural chamber verdict: a unit four-way gcd excludes
  the generic coefficient-and-structural chart for that prime. A nonunit gcd
  gives route data, not closure; only its surviving factors proceed to the
  role, `P_4`, saturation, and arithmetic-lift equations. The explicit
  `U_IDENTICALLY_ZERO` status is non-conclusive. No launch is authorized while
  the Modal workspace is spend-blocked. A unit exceptional five-way gcd
  likewise excludes the `a_2*S_1*J_*!=0` exceptional chart; a nonunit gcd or
  `V_E_IDENTICALLY_ZERO` remains open. For the singular-affine chart,
  `global_status=EMPTY` excludes the chart when the gcd has no non-`A`
  factor. More sharply, `cyclotomic_field_status=EMPTY` excludes the official
  chart when no legal factor has degree dividing eight; factors of all other
  degrees cannot contain `b in F_(p^8)`. `quadratic_subfield_status` remains
  diagnostic. This extension adds no containers, CPUs, memory, retries, or
  timeout. The same semantics apply to the `J_*=0` endpoint after removing
  `T` factors. In the role extension, `ALL_EMPTY` excludes the entire
  exceptional-`J_*=0` coefficient/structural/role/`P_4` chart for that row;
  a guard-summary `ALL_EMPTY` makes the same exclusion after all eligible
  factors fail both eta branches. A guard `HIT` retains the exact surviving
  eta multiplicity and still owes normalized-color matching, the norm and
  degree-six outer congruence, and the independent inner lift.
  `IDENTICALLY_ZERO_FAMILY` is explicitly inconclusive. The extended packet
  remains source-complete but unrun, and its completion within the fixed
  60-second task ceiling is unmeasured. Wait for an explicit spend-access
  change.

  The requested decision is whether every branch in one complete
  representation is unit on `a*B*Q(y)!=0` and the inherited HNF/fiber
  saturations: all four rational systems, all twelve rational Galois systems,
  or all 21 official quadratic Frobenius systems. PASS requires a
  replayable Nullstellensatz or transformation-matrix certificate with
  denominator/content primes checked against every official characteristic.
  FAIL requires an exact retained component or point substituted into the
  unreduced factor equations and exact gcd-degree conditions. Emit all four
  cleared ideals and hashes before elimination and checkpoint every retained
  factor.

  The broad 4/12/21-system request remains a **pre-request** only: no
  proof-producing launcher, independent checker, measured pilot, or cost
  ceiling exists for those multivariate ideals, and the current Modal
  workspace is spend-blocked. The narrow `J=0` gcd subrequest above is
  source-complete but unrun. A raw Groebner transcript is route evidence, not
  a closure certificate.

  **Contributor request CR-L1-H7-C3-INJ:** consume
  `l1_mersenne_hnf_m8_order_one_cubic_collision_free_value_router`. Build
  `V_E(X)=Res_W(L_(r,d),X-E)` once for a generic exact cubic. For each
  `delta=1,2,3,4`, compare the eight nonleading coefficients in

  ```text
  V_E(X)(X-1)(X-omega^delta)=X^8-1
  ```

  together with the h=7 conic. Saturate by `lc(E)*disc(L)*disc(V_E)` and
  HNF denominators. Classify the four p-free ideals before adding any row or
  norm equation; preserve partial generators and dimensions after each
  60-second shard. Do not launch on the current spend-blocked account.

  **Contributor request CR-L1-H7-C3-45COL:** consume
  `l1_mersenne_hnf_m8_order_one_cubic_four_five_color_value_router`. Build
  the generic value resultant once, then enumerate canonical cyclic orbits
  of `(M,D)` for the three profiles with counts `35`, `35`, and `54`. Impose

  ```text
  V_E(X)M(X)=(X^8-1)D(X)
  ```

  coefficientwise with the h=7 conic. Process the 35-packet profiles first
  and checkpoint every ideal; process the 54-packet two-double profile only
  after confirming the half-turn orbit normalization. Saturate by
  `gcd(M,D)=1`, squarefreeness of `M`, `lc(E)*disc(L)`, and exact fiber
  subresultants. Use 60-second shards, preserve partial generators, and do
  not add row/norm equations until a p-free component survives. Do not
  launch on the current spend-blocked account.

  Before the large torsion or remainder equations, shard by `zeta in mu_m`
  and substitute

  ```text
  c_star=1+zeta/(c-1),       rho_star=formal Frobenius image of rho,
  ```

  impose `Psi_h(rho_star,c_star)=0`, also saturating by `c_star+1`. Indeed
  `c_star=-1` would imply `c=-1` under inverse Frobenius. The zero split
  value is the known root `x_0=-1/(c-1)`. The following resultant formula
  remains the definition and an optional independent audit, not the primary
  construction:

  ```text
  L_(rho,c)(W)=P_(rho,c)(W)/(W-x_0),
  Qtilde_(rho,c)(Z)=Res_W(L_(rho,c)(W),Z-W^m),
  Ctilde_(rho,c)=Qtilde_(rho,c)(0),
  ```

  The equivalent reduced coefficient equations are

  ```text
  Ctilde_(rho,c)Qtilde_(rho_star,c_star)(Z)
    =Z^(h-1)Qtilde_(rho,c)(1/Z).
  ```

  **RETIRED BY PROOF -- CR-L1-H15-COLOR0:** consume
  `l1_mersenne_hnf_m16_order_one_constant_color_reduction`. Over `F_8191`
  compute and return monic gcds for

  ```text
  T16(S)=S(S^2-4)(S^2-2)(S^4-4S^2+2),
  gcd(T16,28S^2+29S+370),
  gcd(T16,28S^2+27S-1202).
  ```

  Independently replay by enumerating the sixteen powers of one primitive
  sixteenth root and their traces. The packet would cost negligibly, but no
  launch is needed:
  `l1_mersenne_hnf_m16_order_one_constant_color_exclusion` proves both gcds
  unit by modular pseudo-remainders. Do not spend Modal credit on this packet.

  The removed degree-one factor is automatic and must not be reintroduced
  into the elimination. Compute the exact saturation by the nonzero factor
  in (OFG7). A unit certificate closes the order-one chamber. For each
  retained component, impose `rho_star=rho^p` and
  `(c-1)^(p+1)=zeta`; only then test `P_(rho,c)|W^n-1` and any inner lift.
  A surviving point must carry exact coordinates and direct replay of every
  equation.

For the largest rows, a naively expanded degree-`n` remainder or resultant
may be prohibitively large. Benchmark the recurrence/Frobenius algorithm on
one analogue and one smallest official chamber, record peak memory and
intermediate degrees, and stop if the projected total is at least `$1` or
five minutes on the current account. A larger or unknown-cost exact run is a
contributor request; no field-element scan or raw degree-`n` coefficient
materialization is acceptable.

Classify `(NMCE-OUT)` by exact subresultant or ideal decomposition, sharded
only by the two values of `r` and the declared leading-coefficient chamber;
`deg S=h-2-r` and the quadratic endpoint are already forced. Prefer a
characteristic-uniform decomposition over the integers with its excluded
prime factors; otherwise run the five characteristics separately. Do not
enumerate field elements or the `p^(2(h-1))` coefficient space.

**Route-deciding outer outcome:** either emit independently checkable unit-
ideal/resultant certificates for every chamber, which closes the endpoint
before constructing an inner pencil, or emit a complete finite
parameterization of exceptional `(G,lambda)` passports. A single outer
passport is not a split-pencil witness; label it `OUTER-SURVIVOR`. It must
also carry the exact remainder of `W^n-1` modulo `P`; a nonzero remainder or
prime-field-normalized invariant rejects the passport before the inner stage.

Only for a certified outer survivor should a second stage impose

```text
G(R)D=X^(m(p+1))-alpha,
deg R=p,       deg D=p+m,
H=q,           h complete split fibers,
deg(XR')=p-m,  q=-2m[Y^(h-2)]G[X^(p-m)]R,
```

together with the proved facts that every nonzero tangent value is simple
and every corresponding `R-y` is squarefree, nonzero-rooted, and coprime to
`D`. Enforce the exact identities

```text
D=rad(R-R(0))/X * rad(R-z),
R' proportional to gcd(R-R(0),R')*gcd(R-z,R').
```

Equivalently normalize

```text
F=(R-R(0))/(z-R(0)),
F(0)=0,       deg F'=p-m-1,
D=rad(F)/X * rad(F-1),
F' proportional to gcd(F,F')*gcd(F-1,F').
```

All nonzero roots of `F(F-1)` must replay in the official order-`m(p+1)`
multiplicative domain. A computation that does not encode this Belyi and
domain support structure is outside the request.

The requested final output is either a replayable full pencil or a
proof-producing exclusion certificate for each outer passport. A modular
Groebner no-hit, timeout, or incomplete chamber list is `INCOMPLETE`.

Publish the exact polynomial ring, monomial order, chamber manifest,
generator hashes, certificate format, elapsed CPU, peak RAM, scratch space,
and projected dollar cost. Preserve completed chambers and their hashes on
timeout. The order-64 `CR-L1-MCP-A8` analogue remains useful because its
`p=7` lies below the theorem's `p>h^2` gate; it must not be presented as an
official endpoint classification.

### CR-L1-MCP-C31: adjudicate the order-128 two-Schur CP model

**Status:** RETIRED as a route-deciding contributor request. The model is a
valid incomplete nonofficial conformance artifact, but the complete official
`m=4,h=3` branch is now theorem-empty. Do not rerun it on contributor compute.

This is a bounded structural pilot for the next `m=4,h=3` analogue, not a
request for the raw order-128 subset census. The checked-in script
`experiments/prize_resolution/l1_m4_h3_two_schur_cpsat_modal.py` encodes
`(n,p,m,h)=(128,31,4,3)` with 128 four-color variables, multiplicities
`(35,31,31,31)`, and both required Fourier-code constraints. It expands the
word and coefficientwise-square equations into 240 congruences modulo 31.

The current-account pilot is `INCOMPLETE`. Apps
`ap-31urbcd0fvVu1adNueXzSz` and `ap-cwwCYjpZqT2nwd3vKu4XD6` exposed and
repaired two model-construction errors. The validated repair in app
`ap-m2tOKpIdLfCZOzoRUmRkyQ` hit its 60-second function cap before returning a
solver status. This supplies no existence or emptiness evidence and must not
be reported as a no-hit search.

**Requested outcome:** precompute and hash the `30 x 128 x 4` Fourier
coefficient table, or otherwise separate finite-field/JIT and model-build
time from search. Publish `CpModel.Validate()`, a serialized-model hash,
build time, actual CP-SAT wall time, status, branches, and conflicts. A
`FEASIBLE` result must include all four color classes and pass the independent
`F_(31^4)` replay already present in the script. An `INFEASIBLE` result is
complete evidence for this nonofficial analogue only; `UNKNOWN` or timeout is
`INCOMPLETE`. Benchmark before increasing CPUs or wall time, and state the
dollar cap in advance. No current-account rerun is authorized.

The analytic follow-up is complete. Nonzero-`b` zero valuation is removed by
the tangent and packet theorems, positive valuation by the tangent
multiplicity theorem, and zero-`b` zero valuation by the Euler/value-coset
contradiction. No donated solver extension remains for this shard.

### CR-L1-MCP-M4H2-C31: nonembedded order-128 signed-codeword classifier

**Status:** valuable outbound compute pre-request; not authorized locally or
on the current Modal account. Benchmark and price one shard before launch.

This is the next route-deciding analogue after the official `m=4,h=3`
closure. Work at `(n,p,m)=(128,31,4)` with ternary exponent variables

```text
b_i in {-1,0,1},       #(+1)=#(-1)=31,       #(0)=66.
```

Require the exact Mersenne cyclic-code condition from
`l1_mersenne_checkpoint_cyclotomic_normal_form`: the Fourier transform
vanishes on the complete `31`-cyclotomic closure of frequencies `0,...,30`.
For `m=4`, implement the closure by its residue chambers rather than by
extension-field exponentiation. There is no Schur-square constraint in the
two-fiber problem. Since maximal `h=4` and all `h=3` records are now
theorem-empty, every genuine pair on an official `m=4` row belongs to the
`h=2` endpoint.

Generate the 64 unordered embedded pairs supplied by
`l1_mersenne_checkpoint_embedded_m2_family` and both signed orientations,
then block their full orbit under cyclic shift, Frobenius multiplier, and
global sign. The blocking list must be independently regenerated from the
locator formula `R=Z(Z^2-b)^15`, not inferred only from support shape. Fix a
canonical first nonzero sign and least cyclic representative after proving
that these symmetries preserve the model.

**Requested outcome:** either emit one nonembedded ternary word with a direct
`F_(31^4)` Fourier replay and reconstruct its two monic split locators, or
prove that only embedded words exist in the declared quotient. A witness is
route-changing evidence against embedded-family exhaustion. An exclusion is
analogue evidence for a low-weight cyclic-code classification theorem, not
an official proof.

For a complete exclusion, prefer a SAT/SMT encoding with a checkable proof
certificate. A bare CP-SAT `INFEASIBLE` status is not a portable certificate;
it must be accompanied by an independently generated model hash and a second
complete solver replay. `UNKNOWN`, timeout, or incomplete symmetry coverage
is `INCOMPLETE`. Preserve partial orbit blocks, witnesses, model hashes,
elapsed CPU, peak RAM, and the exact unprocessed range.

**Launch gate:** publish model construction time and one symmetry-shard
benchmark with explicit CPU, RAM, storage, wall-time, and dollar ceilings.
Do not scale to official `p`, enumerate `binom(128,31)binom(97,31)` signed
supports, or infer a theorem from a no-hit heuristic run. If the compressed
model remains expensive, include this request in the upstream PR for
contributors with available compute.

### CR-L1-MCP-NU2 retirement record: normalized Belyi regular-fiber divisibility

**Status:** RETIRED by theorem; do not launch locally, on Modal, or as a
contributor request.

`l1_m4_h3_positive_tangent_multiplicity_exclusion` proves that every
repeated tangent multiplicity is the local order of the cubic
`X^nu H-kappa`. Since there are at most three tangent roots, either positive
stratum would force `p<=9`. Thus the parent `(nu,deg H)=(2,1)` stratum is
empty before the multiplicity-triple divisibility test. The specification
below is retained only to document the retired route and its valid
intermediate normal form.

This formerly targeted `p in {524287,2147483647}` and the then-surviving positive
`(nu,deg H)=(2,1)` stratum. For pairwise-distinct positive integers
`e_1+e_2+e_3=p`, the proved normal form constructs

```text
d_i=e_j-e_k,
w=product_i d_i^e_i,
q_i=3w/(4d_i),
F_e(W)=3/4+product_i (W-q_i)^e_i.
```

Frobenius and the fixed-fiber product prove that there is no additional
domain scalar. Any genuine record must pass exactly one sign test
`F_e(+1)=1` or `F_e(-1)=1` and admit a monic `E_e in F_p[W]` with

```text
(F_e(W)^3-2F_e(W)+1)E_e(W)=W^(4(p+1))-1.              (NU2-DIV)
```

The former route-deciding computation would either emit one multiplicity triple and
an independently replayable exact factorization, or certify that no triple
satisfies `(NU2-DIV)` for a declared official characteristic. Before the
retirement, a witness would have kept the stratum alive and supplied a
concrete split pencil; partial coverage would have been evidence only.

The naive universe has order `p^2` triples and degree-`3p` divisors, so raw
triple enumeration or dense polynomial expansion was prohibited. The former
promotion gates were:

1. a theorem-backed symmetry quotient or recurrence that covers every
   unordered multiplicity triple;
2. a sparse/product-tree or residue representation that checks `(NU2-DIV)`
   without materializing degree-`3p` polynomials per triple;
3. replay the checked-in complete `p=7,31,127` conformance oracle at
   `experiments/prize_resolution/l1_m4_h3_nu2_scalar_free_analogs.py`, then
   publish a measured official-compatible one-shard pilot;
4. checkpointed triple-range coverage, hashes, peak RAM, and elapsed CPU;
5. an independent checker that reconstructs every witness and verifies every
   exclusion certificate block.

Do not include this item in upstream PRs as live compute. Vendor the local
multiplicity exclusion instead; the normal-form artifacts may accompany it
as independently checked but superseded reductions.

### CR-L1-MCP-NU0-H0 pre-request: exceptional outer-packet lift or exclusion

**Status:** RETIRED by theorem; do not launch locally and do not copy into an
upstream PR as a live compute request.

This record formerly targeted the last surviving
`nu=0,b!=0,deg H=0` packet:

```text
p=2147483647:               (A,B)=(844833809,2002167159),
A=a/R(0)^2,                 B=b/R(0)^3.
```

The universal packet `(A,B)=(6,20)` was first excluded by
`l1_m4_h3_nu0_h0_universal_packet_exclusion`. The subsequent
`l1_m4_h3_nu0_h0_auxiliary_fiber_exclusion` proves that every exceptional
lift would force

```text
P_A(W)=W^3+1800058023W^2+664831389W+573306971
```

to divide `W^(4(p+1))-1`. Exact polynomial modular powering and an
independent companion-matrix replay both give the nonzero remainder
`876663072`. The exceptional packet is impossible, so the entire endpoint is
theorem-empty on all four official characteristics.

There is no remaining mathematical decision for donated compute. An upstream
PR should vendor the two proved exclusions and their compact checkers, and
should mention this retirement only to prevent contributors from repeating
the obsolete coefficient or lift search.

### CR-E1-E38-Q16: variance-76 quotient-Schur census

**Status:** COMPLETE by exact certificate; do not extend or rerun unless
auditing the pinned result.

This route-deciding campaign optimized the mod-16 residue-capacity bound for
the three exceptional `E=38,L<=22` magnitude profiles in `Z/128 Z` and in the
divided group `Z/64 Z`. The final preregistered implementation used 80
disjoint shards, one CPU and 256 MiB per shard, a 180-second hard per-shard
timeout, deterministic integer arithmetic, exact coverage counts, and an
independent local checker. It completed 43,153,083 allocations in under 20
seconds of campaign wall time. The configured worst-case campaign ceiling was
below `$0.25`; no further paid run is required.

Final complete run:

```text
ap-n57PHWIhpfTIODFu1x2CMu
```

Development and falsification runs, all non-load-bearing, were
`ap-7zDRVMlTTBSwe7TnVNO34t`, `ap-4E8RkbLTDjcmSeJq2sTI7y`,
`ap-w0BCehAMjrwWVEI80ATZvz`, `ap-PvmZeSqQGezJw3diejEqnD`,
`ap-4ayZeHGOYlEsxweNyZdUt1`, `ap-dNiFo0EV95jJZQiykdbR3F`, and
`ap-F0lwASenN9DKXigGtaPBnf`. A client-side 60-second RAMguard cutoff cancelled
the incomplete initialization run `ap-8QVwOZpPwsI7uSbc4bqYoc`; it supplied no
evidence.

The canonical packet and replay sources are:

```text
background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/
  e38_mod16_quotient_census.cpp
  e38_mod16_quotient_census_result.json
  e38_mod16_quotient_census_check.py
background/nodes/e1_n256_s16_e38_quotient_schur_exclusion/
  verify_census_remote.py
```

The complete maxima are `2782,2760,2580,2422,840,840`. Together with the
proved `4Z` subfield exclusion they imply `M_3<=2796<2806`, close `V=76`, and
advance the residual to positive even `V<=74`. `FAIL` would have been an
allocation above 2806 and a return to support-specific chord geometry;
`INCOMPLETE` would have changed no status. Neither occurred.

### CR-E1-E37-Q16: variance-74 quotient-Schur extension

**Status:** COMPLETE by exact certificate; do not extend or rerun unless
auditing the pinned result.

At `E=37`, the exact recurrence gives `L<=21`; 29 integer magnitude profiles
remain. The cubic-Hermite threshold is `M_3<=2592`, and only `(5,8)`,
`(8,5,1)`, and `(1,9)` have larger abstract caps. Extend the pinned E38 C++
census with two-layer profiles `(5,8)` and `(1,9)` and an outer-only 28-point
profile for the singleton-top-layer reduction. Run both the odd-support
`Z/128 Z` and divided-odd `Z/64 Z` chambers.

Use at most 48 one-CPU, 256-MiB shards, a 180-second hard per-shard timeout,
under five minutes total wall time, and a conservative total ceiling of
`$0.25`. The launcher must write exact per-shard counts and maxima even if a
subset fails; `INCOMPLETE` changes no status. The independent checker must
recount allocations by dynamic programming and evaluate every displayed
maximum before any theorem promotion.

`PASS` means both two-layer profiles are at most 2592 and the singleton
profile satisfies `R(A,A,A)<=720`, yielding a direct `V=74` closure. `FAIL`
means a complete quotient maximum exceeds one of those thresholds and
returns the corresponding profile to a support-specific layer coupling.
Record every app ID and measured campaign result here after launch. Do not
scale beyond these six finite optimization cells.

The complete campaign used three bounded development passes, all within the
declared aggregate ceilings:

```text
ap-kaS1w5aXwJKRvb8VGJvL7q   initial six-cell census
ap-kksQDQpMDHUnJDCTccPONM   B not subset 4Z chamber split
ap-CQM1N1zJGw5E0FXC4k6qim   final allocation-wise 174 refinement
```

The final 48-shard pass completed in under 20 seconds. It checked 19,732,753
allocations and returned full caps `2626,2576,2372,2168,678,678`. The only
raw cap above 2592 is the `(5,8)` order-128 chamber. Its
`B not subset 4Z` maximum is 2576; for `B subset 4Z`, independently checking
all `binom(15,8)=6435` inner layers gives `R(B,B,B)<=174`, and the refined
allocation-wise maximum is 2560. The resulting global live-row cap is 2576,
so `V=74` is excluded and the residual advances to positive even `V<=72`.

The source, result packet, checker, and registered remote launcher are
`e37_mod16_quotient_census.cpp`,
`e37_mod16_quotient_census_result.json`,
`e37_mod16_quotient_census_check.py`, and
`e1_n256_s16_e37_quotient_schur_exclusion/verify_census_remote.py`.

### CR-E1-E36-Q16: variance-72 quotient-Schur route decision

**Status:** COMPLETE by exact certificate; do not extend or rerun unless
auditing the pinned result.

At `E=36`, the exact recurrence gives `L<=20`, and 26 magnitude profiles
remain. The cubic threshold is `M_3<=2377`; only `(4,8)`, `(0,9)`, and
`(7,5,1)` exceed it abstractly. Run exact odd-support and divided-odd mod-16
cells for two-layer profiles `(4,8)` and `(0,9)`, and an outer-only 26-point
cell for `(7,5,1)`. Preserve the E37 chamber outputs: report the complete
`B not subset 4Z` maximum and maximize the allocation-wise replacement
`R(B,B,B)<=174` whenever `B subset 4Z`.

Use at most 48 one-CPU, 256-MiB shards, 180 seconds per shard, under five
minutes total wall time, and a conservative total ceiling of `$0.25`.
Write useful partial results and explicit errors on `INCOMPLETE`; no status
changes without all six cells. The independent checker must reconstruct
coverage counts and every displayed maximum.

`PASS` requires both two-layer profiles at most 2377 after valid chamber
refinement and `R(A,A,A)<=589` for the 26-point outer layer. `FAIL` returns
the exact failing allocation and component to support-specific coupling.
Do not launch a finer quotient or another solver from this authorization.

Initial complete run `ap-clS4xL2P7ek5EPTxyA54S0` checked 8,144,380
allocations in under 16 seconds. Five components close, but `(4,8)` has cap
2398 in both the order-128 and divided order-64 routes, 21 above threshold.
Both maximizers put the complete 16-point inner layer in `2 Z/128 Z`.
Accordingly the declared `FAIL` branch is active; no finer outer quotient is
authorized here.

Final refined run `ap-UO3twT5yf4p6bQ4Dy8sktP` incorporates the exact inner
theorem from CR-E1-E36-B64 allocation by allocation. For `(4,8)`, the
order-128 outside-inner-`2Z` chamber is 2208, its inner-`2Z` chamber is 2344,
and the divided order-64 chamber is 2332. The `(0,9)` cells are at most 2000,
and the outer-only cells for `(7,5,1)` are 556 and 540. Thus the global live
cap is 2344, below the exact cubic threshold 2377.

The source, result packet, checker, and registered remote launcher are
`e36_mod16_quotient_census.cpp`,
`e36_mod16_quotient_census_result.json`,
`e36_mod16_quotient_census_check.py`, and
`e1_n256_s16_e36_quotient_schur_exclusion/verify_census_remote.py`.

### CR-E1-E36-B64: exact inner-layer Schur maximum in Z/64 Z

**Status:** COMPLETE by exact certificate.

Enumerate every symmetric 16-point subset `B` of `Z/64 Z` avoiding 0 and 32.
Such a set chooses eight of the 31 negation pairs, so the exact universe is
`binom(31,8)=7,888,725`. Compute

```text
R(B,B,B)=#{(x,y,z) in B^3: x+y+z=0 mod 64}.
```

Use at most 16 one-CPU, 256-MiB shards, a 120-second hard per-shard timeout,
under three minutes total wall time, and a conservative ceiling of `$0.15`.
The packet must include exact lexicographic shard ranges, processed counts,
maxima, and maximizing representatives. An independent Python checker must
recount coverage and directly replay every displayed maximum. `INCOMPLETE`
changes no status.

`PASS` is maximum at most 219, which closes the remaining 21-point cubic gap
after replacing the quotient `R(B,B,B)` cap 240. `FAIL` is a maximum at least
220 and returns the exact inner layer for a coupled outer/inner attack. No
larger group or support size is authorized.

Run `ap-Rz22K5DtG8oBeelSyV39Zd` completed all 7,888,725 sets in under
13 seconds and found exact maximum 174. The source, compact result packet,
and independent checker are `e36_bbb64_census.cpp`,
`e36_bbb64_census_result.json`, and `e36_bbb64_census_check.py`. This result
is consumed only in the declared inner-`2Z` chambers. Its registered remote
launcher is
`e1_n256_s16_e36_quotient_schur_exclusion/verify_bbb64_remote.py`.

### CR-E1-E35-Q16: variance-70 quotient-Schur route decision

**Status:** COMPLETE by exact certificate. The outer-only sufficient criterion
returned `FAIL` by two counts and was repaired by exact nested coupling.

At `E=35`, the exact recurrence gives `L<=19`; 21 magnitude profiles remain,
and the exact cubic threshold is `M_3<=2162`. Only `(3,8)` and `(6,5,1)`
exceed it abstractly. Run the odd-support and divided-odd mod-16 cells for the
two-layer profile `(3,8)`, and the outer-only 24-point cells needed by
`(6,5,1)`. Reuse the already proved complete `Z/64 Z` theorem
`R(B,B,B)<=174` allocation by allocation; no new inner census is authorized.

Use at most 32 one-CPU, 256-MiB shards, 180 seconds per shard, under five
minutes total wall time, and a conservative aggregate ceiling of `$0.25`.
The launcher must retain useful partial results and explicit errors on
`INCOMPLETE`. The independent checker must reconstruct every allocation
count, objective, chamber maximum, and source hash.

`PASS` requires every valid `(3,8)` chamber at most 2162 and the 24-point
outer Schur term at most 458. Together with `54^32<2^250`, PASS closes
`V=70`. `FAIL` emits the exact obstructing allocation and component for a
support-specific theorem. `INCOMPLETE` changes no status. Do not launch a
finer quotient or another solver from this authorization.

Source, launcher, and checker:
`e35_mod16_quotient_census.cpp`,
`verify_e35_mod16_quotient_census_remote.py`, and
`e35_mod16_quotient_census_check.py`.

Setup-only runs `ap-0FGvj92aNnIyFpLCOoTJKC` and
`ap-9dJHjobg5LNfcSK5vU3HWf` failed before producing any census result because
of launcher path hydration. Final run `ap-Gwlrl9cLfJsa2bS83BFw4k` completed
all 2,946,287 allocations in under ten seconds. For `(3,8)`, the odd inner-2Z
refinement is 2152, the odd outside-inner-2Z chamber is 2010, and the divided
refinement is 2100. The `(6,5,1)` outer-only caps are 460 and 454. Thus the
pre-registered outer target 458 fails only in the odd chamber.

A deterministic exact follow-up enumerated all 104,750 odd outer allocations
and all 32,346 divided allocations. Exactly four odd allocations exceed 458,
all at 460. Exhausting all 276 compatible middle/top nestings gives complete
three-layer maximum 2054. Hence low odd cases are at most 2162, divided cases
at most 2158, and exceptional odd cases at most 2054. The exact cubic threshold
2162 is met, so `V=70` is excluded. The follow-up checker is
`e35_high_outer_coupling_check.py`; no second remote campaign was required.

### CR-E1-E34-NESTED-Q16-PILOT: variance-68 nested quotient route decision

**Status:** COMPLETE ROUTE CUT. The pilot found exact relaxation obstructions;
the full campaign is retired and must not be launched.

At `E=34`, the exact recurrence gives `L<=20`, and the cubic-Hermite
certificate closes the slice if `M_3<=1947`. Exactly six magnitude profiles
exceed that threshold under the abstract layer bound:

```text
(6,7), (9,4,1), (2,8), (12,1,2), (5,5,1), (14,1,0,1).
```

The exact nested-layer quotient compiler allocates every exact magnitude
layer over the nine modulo-16 negation-orbit categories, evaluates all
ordered layer triples by the minimum of the three target-fiber bounds, and
keeps the odd order-128 and divided-odd order-64 chambers separate. The
outer-`4Z` chamber is already theorem-excluded. The independent checker
recomputes witnesses and can recount all twelve complete state spaces by a
separate dynamic program.

Run one deterministic shard out of 128 in each of the twelve cells. Resources
are one CPU and 256 MiB per task, at most twelve concurrent containers, a
120-second hard function cap, and a 110-second subprocess cap. This is one
wave with a conservative campaign wall ceiling below three minutes and a
configured CPU ceiling of 1,440 CPU-seconds; its conservative dollar ceiling
is `$0.10`. The launcher checkpoints the compact packet after every returned
task.

`FAIL` is any exact quotient allocation with objective at least 1948; it
kills the unrefined nested mod-16 route but does not refute the mathematical
`V=68` exclusion. `SURVIVES` means every sampled objective is at most 1947;
it authorizes only a timing/cost decision for a possible complete campaign.
`INCOMPLETE` is evidence only. A complete theorem campaign would require all
sixteen shards in every cell, exact aggregate coverage 228,097,120, a passing
local checker, and a fresh pre-launch confirmation that two task waves fit
both active resource laws.

Sources:
`e34_nested_quotient_census.cpp`,
`e34_nested_quotient_census_modal.py`, and
`e34_nested_quotient_census_check.py` in the E1 sparse-L1 notes directory.

Modal app `ap-Ec22WlisgFjRNPFuigxlEy` returned all twelve pilot tasks in
18.91 seconds of client-observed app wall time. Five cells already exceed the
required cap: `(6,7)` at both orders with maxima 2132 and 2154, `(9,4,1)` at
both orders with 1990 and 2016, and `(12,1,2)` at order 128 with 1990. The
local checker independently reconstructs the exact allocation witnesses and
all twelve objectives. This is the registered `FAIL` outcome: it kills the
bare nested mod-16 upper-bound route without refuting `V=68`.

The launcher omitted per-worker durations, so this run cannot authorize a
scaled timing claim. That omission has no mathematical effect because no
sampled coverage is load-bearing and the compact obstruction witnesses replay
locally. Do not rerun for timing and do not launch the 228,097,120-state full
campaign. The next theorem must add chord-origin realizability, support-level
coupling, or a stronger analytic norm certificate.

#### CR-E1-E34-Q16-SURVIVORS: close the three unobstructed profiles

**Status:** COMPLETE WITH PARTIAL PASS. Two profiles close; `(2,8)` returns an
exact quotient obstruction.

The pilot obstructions occur only in `(6,7)`, `(9,4,1)`, and `(12,1,2)`.
Exhaust the remaining profiles `(2,8)`, `(5,5,1)`, and `(14,1,0,1)` in both
the odd order-128 and divided-odd order-64 chambers. Their exact aggregate
coverage is 42,413,558 allocations. Use sixteen shards per cell: 96 tasks,
one CPU and 256 MiB each, at most 100 concurrent containers, a 120-second
function cap, and a 110-second subprocess cap. This is one task wave with a
conservative wall ceiling below three minutes and dollar ceiling below
`$0.25`. The corrected launcher records per-worker duration and checkpoints
after each return.

`PASS` requires all six maxima at most 1947 and closes these three abstract
`V=68` profiles by the cubic-Hermite certificate and the existing outer-`4Z`
norm exclusion. `FAIL` emits the exact profile/order allocation above 1947
for support-specific coupling. `INCOMPLETE` changes no status. The independent
checker must reproduce every maximum and the exact 42,413,558 allocation
coverage before any theorem node is promoted. Do not include the three known
obstructed profiles in this run.

Modal app `ap-zx5C3lSHLdaYAZE2Ic0tZA` completed all 96 tasks and all
42,413,558 allocations in 29.84 seconds of client-observed wall time. Worker
durations range from 0.052 to 16.259 seconds and total 334.664 CPU-seconds.
The independent checker gives exact maxima

```text
(2,8):          2052 / 2008
(5,5,1):        1880 / 1828
(14,1,0,1):     1922 / 1922
```

where each pair is order 128 / order 64. Hence `(5,5,1)` and `(14,1,0,1)`
pass the 1947 threshold and are proof-closed. The `(2,8)` profile returns the
declared `FAIL` with exact allocations in the packet. Its largest order-128
quotient components are `(300,264,240,240)`, totaling 2052; replacing the
inner cubic by the proved cap 174 still leaves 1986. The order-64 obstruction
falls to 1942 under that replacement. Continue only with a chamber-exhaustive
inner-layer refinement for `(2,8)`; do not rerun the two closed profiles.

The launcher's terminal progress dictionary originally retained the last
returned shard rather than the maximum shard. The compact result packet was
unaffected, the independent checker found the correct maxima above, and the
summary source is repaired. No theorem relies on the incorrect terminal
print.

#### CR-E1-E34-P2-COUPLED: profile-(2,8) chamber close

**Status:** COMPLETE PASS. Profile `(2,8)` is closed.

Run two exhaustive pieces in one 64-container wave. The refined quotient
piece covers all 531,517 order-128 and 277,957 order-64 allocations, applying
the proved `R(B,B,B)<=174` cap in the order-64 and even-inner chambers and
reporting the order-128 inner-`4Z` split. The exact support piece covers all
`binom(15,8)*1232=7,927,920` weighted supports in the remaining
`B subset 4Z` chamber. Its outer supplement has two positive representatives,
at least one odd, and is disjoint from the eight inner representatives.

Use 16 shards at each quotient order and 32 support shards, one CPU and
256 MiB per task, at most 64 concurrent containers, 120 seconds per function,
and 110 seconds per subprocess. The conservative campaign wall ceiling is
below three minutes and the cost ceiling is below `$0.20`. The launcher
checkpoints every result and records worker durations. The independent checker
recounts both quotient universes, all 7,927,920 supports, every quotient
candidate, both source hashes, and every exact support maximum.

`PASS` requires the order-64 global refined cap, order-128 outside-inner-`4Z`
cap, and exact inner-`4Z` support cap all to be at most 1947. It closes the
profile `(2,8)` at `V=68`. `FAIL` returns an exact quotient allocation or
weighted support in the surviving chamber. `INCOMPLETE` changes no status.
Do not broaden the campaign to any other profile.

Modal app `ap-8xzV3fZniv8jms4V2EI19N` completed all 64 tasks in 22.02
seconds of client-observed wall time. Worker durations range from 0.031 to
0.673 seconds and total 17.624 seconds. The independent checker reconstructed
all 809,474 quotient allocations and 7,927,920 exact supports, obtaining

```text
order-64 refined quotient maximum          1942,
order-128 outside-inner-4Z maximum         1942,
order-128 inner-4Z exact support maximum   1536.
```

This is the declared `PASS`: profile `(2,8)` is excluded at `V=68`. The
result is consumed by `e1_n256_s16_e34_three_profile_reduction`. No rerun or
extension is authorized.

#### CR-E1-E34-QUARTER: normalized quarter-template close

**Status:** COMPLETE PASS. The quarter heavy-position template is closed; no
rerun or extension is authorized.

The heavy-template theorem normalizes the branch to `H={0,32,64}`, opposite
outer heavy signs, no light at `96`, 124 possible light positions, two middle
heavy signs, and sixteen light-sign patterns. The exact universe is
`binom(124,4)*32=300,200,032` vectors.

The primary implementation groups unordered signed chords. The independent
audit forms `F(X)F(X^-1)` directly in `Z[X]/(X^128+1)`. Each uses 121 shards,
one CPU and 256 MiB per task, 60-second function caps, at most 100 containers,
and partial packet writes. `PASS` requires exact shard coverage, shardwise
agreement on all counts and maxima, and `M_3<=1947` on every full-conductor
profile-`(6,7)` vector.

Modal apps `ap-kLTKBwJM3lNWUZA3hul5w7` and
`ap-XXTZkD7kcupvXULmbp2GKZ` completed in under 30 client-observed seconds
each, using 45.781851 and 52.691880 aggregate worker-seconds. They agree on

```text
E=34 vectors                       1,514,544,
profile-(6,7) vectors              1,181,056,
full-conductor profile vectors     1,031,680,
maximum full-conductor M_3              1188.
```

The combined conservative cost ceiling was `$0.15`; actual worker usage was
98.473731 CPU-seconds. The exact maximum is 759 below the cubic threshold, so
`e1_n256_s16_e34_quarter_template_exclusion` closes the branch.

#### CR-E1-E34-NONQUARTER-DIAMETER: exact weld-chamber decision

**Status:** COMPLETE PASS. The nonquarter-diameter template is closed; no
rerun or extension is authorized.

The proved weld reduction gives 31 normalized heavy triples
`H={0,64,t}`, `1<=t<=31`, and exactly 915,125 admissible light supports per
triple. With four residual heavy-sign choices and sixteen light-sign choices,
the complete chamber has 1,815,608,000 signed vectors.

The primary implementation groups 21 unordered signed chords. The independent
audit forms `F(X)F(X^-1)` directly in `Z[X]/(X^128+1)` and reconstructs weld
eligibility from circular distances. Each uses 31 one-CPU, 256 MiB tasks with
60-second function caps, at most 31 containers, and a partial packet write
after every return. Abort the campaign after five client-observed minutes or
any task timeout. The conservative combined cost ceiling is `$0.90`; do not
rerun or extend without a new route decision.

`PASS` requires exact coverage, 915,125 supports per `t`, shardwise agreement
of every count and maximum, and replay of retained witnesses. If the maximum
full-conductor profile-`(6,7)` moment is at most 1947, the inherited exact
cubic certificate closes the branch. Otherwise the packet must retain exact
extremizers and the branch remains open at the first failing `t`/sign class.

Modal apps `ap-EfGZditRQm7eDLLLWpNiSA` and
`ap-MQpKibQl8PBqzuhB5DKf2m` completed all 31 tasks without retries, using
271.301709 and 339.920267 aggregate worker-seconds. The two implementations
agree shardwise on

```text
light supports                       28,368,875,
normalized signed vectors         1,815,608,000,
E=34 vectors                           1,518,816,
profile-(6,7) vectors                  1,044,528,
full-conductor profile vectors          899,456,
maximum full-conductor M_3                  1560.
```

The combined 611.221976 worker-seconds remain below the declared conservative
`$0.90` ceiling. Since `1560<1947`, the inherited cubic certificate closes
the complete nonquarter-diameter branch.

#### CR-E1-E34-PROGRESSION: five-orbit exact chamber decision

**Status:** COMPLETE PASS. The progression template is closed; no rerun or
extension is authorized.

The proved progression reduction leaves 62 heavy-step forms, opposite outer
heavy signs, and 1,195,965 welded supports per form. Odd cyclotomic
automorphisms preserve every load-bearing invariant and reduce the complete
decision to representatives `t=1,2,4,8,16`, containing 191,354,400 signed
vectors in total.

The primary implementation groups unordered signed chords. The independent
audit forms the ordered negacyclic product and reconstructs the singleton weld
from circular distances. Each uses five one-CPU, 256 MiB tasks with 60-second
caps, at most five containers, and partial packet writes. Abort on any timeout
or incomplete shard. The combined conservative cost ceiling is `$0.20`; no
rerun or extension is authorized without a new route decision.

`PASS` requires exact five-shard coverage, 1,195,965 supports per
representative, shardwise agreement of all fields, replay of retained
witnesses, and exact weighting by orbit multiplicities `32,16,8,4,2`. A
maximum `M_3<=1947` closes all 62 progression forms by unit transport;
otherwise retain the first exact failing representative and keep the branch
open.

Modal apps `ap-i5ZUL3DXjsMVeoSd2KwzT4` and
`ap-x6NGO4WBkgu0GbaGBpeQim` completed all five tasks without retries, using
29.943997 and 50.977832 aggregate worker-seconds. They agree shardwise. The
five representatives contain

```text
supports              5,979,825,
signed vectors       191,354,400,
E=34 vectors             603,832,
profile-(6,7) vectors    404,212,
full-conductor vectors   329,776.
```

Exact orbit weighting gives 3,131,008 full-conductor profile vectors over all
62 forms. The maximum is `M_3=1722`, attained in the odd-step orbit. The
combined 80.921829 worker-seconds remain below the `$0.20` ceiling. Since
`1722<1947`, unit transport and the inherited cubic certificate close the
complete progression branch.

#### CR-E1-E34-GENERIC-ORBITS: affine three-weld route classifier

**Status:** COMPLETE PASS. The route classifier is banked; no rerun is
authorized.

Before any generic-vector census, classify all 325,376 generic heavy triples
under translations and odd cyclotomic units. The primary implementation maps
every triple to a canonical form. The independent audit generates full affine
orbits and removes them from the exact triple set. For each representative,
both compute the three heavy-light weld sets, all intersections, and the exact
four-light support count by inclusion-exclusion.

Run two one-CPU, 256 MiB tasks with 60-second caps and at most two containers.
Abort on any timeout or disagreement. The conservative cost ceiling is
`$0.05`. This campaign is route classification only: it may promote a proved
normal-form reduction, but it cannot exclude the generic template without a
separate signed profile/moment certificate.

Modal app `ap-RX2pnnmJRiFhsRSBEJS6To` completed both implementations in
1.110289 aggregate worker-seconds. They agree exactly: the 325,376 generic
heavy triples form 57 affine odd-unit orbits. The three-weld ledgers have
exactly three shapes:

```text
rows  weld sizes  pair intersections  triple  union  supports
 52    4,4,4           1,1,1             0      9     66,405
  4    3,4,4           2,1,1             0      7     72,486
  1    3,4,3           2,1,2             0      5     58,325.
```

After four heavy-sign and sixteen light-sign choices, the exact representative
chamber has 243,285,056 signed vectors. The campaign cost is below `$0.05`.
This closes route classification only; profile and moment remain unpaid.

#### CR-E1-E34-GENERIC-CENSUS: final affine-orbit chamber decision

**Status:** COMPLETE PASS. The generic template and E34 endpoint are closed;
no rerun or extension is authorized.

The proved generic affine-weld reduction leaves exactly 57 representatives,
58,325 to 72,486 supports per representative, and 243,285,056 normalized
signed vectors. The primary implementation groups unordered signed chords.
The independent audit uses ordered negacyclic multiplication and independently
reconstructs weld membership from circular distances.

Run 57 tasks per implementation with one CPU, 256 MiB, 60-second caps, and at
most 45 containers per app so concurrent usage cannot exceed 90 containers.
Write a partial packet after every return and abort on any timeout or mismatch.
The combined conservative cost ceiling is `$0.20`; no rerun or extension is
authorized without a new route decision.

`PASS` requires exact agreement with the orbit packet's support count, all 57
shards, shardwise count/max agreement, and retained-witness replay. A maximum
`M_3<=1947` closes the generic branch and therefore the full `E=34` endpoint;
otherwise retain the first failing orbit and keep E34 open.

Modal apps `ap-XpmKEOhClEfy8STvFbMH9y` and
`ap-GUW2NuOkVnhQDU4jUvepbZ` completed all 57 tasks without retries, using
34.471246 and 50.538048 aggregate worker-seconds. They agree shardwise on

```text
light supports                         3,801,329,
normalized signed vectors            243,285,056,
E=34 vectors                              793,742,
profile-(6,7) vectors                     505,466,
full-conductor profile vectors            418,464,
maximum full-conductor M_3                    1770.
```

The maximum occurs in orbit 14, represented by `H={0,1,19}`. The combined
85.009294 worker-seconds remain below the `$0.20` ceiling. Since `1770<1947`,
the inherited cubic certificate closes the generic template. Together with
the quarter, nonquarter-diameter, and progression exclusions, this closes the
complete `E=34`, `V=68` endpoint.

#### CR-E1-V36-WITNESS-NORM: full-conductor falsifier decision

**Status:** COMPLETE NO-HIT. No rerun is authorized for this witness.

The proved proper-conductor packet contains a full-conductor folded-`(3,4,0)`
vector at `V=36`. Compute its resultant with `x^128+1`, divide by the exact
2-adic valuation, and test the odd part for primality independently in FLINT
and PARI. A prime odd part in `(2^250,2^256)` is an immediate candidate
collision row and triggers exact pair-feasibility replay; a composite or
undersized odd part kills this particular falsifier without supporting a
universal exclusion.

Run one one-CPU, 256 MiB Modal task with a 60-second hard timeout and no
retries. The source prints a complete or explicit incomplete packet and both
engine outputs must agree. Conservative cost is below `$0.02`. App ID and
measured worker time are recorded after the single launch; no rerun is
authorized without a changed witness or a failed infrastructure launch.

Modal app `ap-w5NVLM6qks58oQP9KHXi9G` completed in `0.063751`
worker-seconds. FLINT and PARI agree on the 249-bit norm

```text
713716409960669519192598736974780038395771519667874695041952783752312355842.
```

Its valuation is one. The 248-bit odd part is prime and congruent to one
modulo 256, but is below `2^250`, so this exact vector cannot collide on the
pair-feasible branch. The compact packet is
`e1_v36_full_conductor_witness_norm_result.json`; its deterministic arithmetic
and source-hash checker is `e1_v36_full_conductor_witness_norm_check.py`.

#### CR-E1-E26-TOP-MASK-PILOT: actual-vector falsifier search

**Status:** COMPLETE NO-HIT. This bounded pilot is superseded by the complete
four-profile census below; no rerun is authorized.

The exact E26 odd-mask relaxation leaves every light mask alive, but ranks the
two cheap profiles `(4,1,2)` and `(6,1,0,1)` by attainable `M_3`. Census the
top 16 normalized light representatives for each profile, retaining the 32
highest-`M_3` full-conductor vectors per task for exact norm follow-up. The
pilot covers exactly `32*binom(124,3)*64=635,133,952` signed vectors; it makes no
claim about the other 1,202 masks.

Run 32 one-CPU, 256 MiB tasks with 60-second hard timeouts and at most 32
containers. The launcher writes a partial result after each return, checks
every actual maximum against the exact relaxation maximum, and aborts on any
timeout or malformed row. Conservative total cost is below `$0.10` and total
wall time below five minutes. A retained odd prime norm part above `2^250`
triggers independent collision replay; no hit only retires this ranked pilot.

Modal app `ap-L2vmgKMlAx8lsHkCxmzySB` completed all 32 tasks without retry,
covering exactly 635,133,952 vectors in `68.453854` aggregate worker-seconds.
It found 614 profile vectors, 560 above `M_3=228`, and 44 full-conductor
exceptions on seven masks. Their maximum full-conductor third moment is 624.
Modal app `ap-sSRw4M4r3Lo3CFYJzKwm74` completed dual FLINT/PARI norm and
primality evaluation of all 44 retained vectors. The engines agree on 22
distinct norms. The 247-bit maximum is

```text
206300578845256388660989325009715100926350250639065957504774519402224202242.
```

Six odd parts are prime, but none reaches the pair-feasible floor `2^250`, so
the pilot finds no collision row. The complete census and norm packet below
now covers the other 1,202 masks as well.

#### CR-E1-E26-FOUR-PROFILE-CENSUS: complete six-odd endpoint decision

**Status:** COMPLETE PASS. The four profiles and the full `V=52` endpoint are
closed; no rerun is authorized.

The proved six-odd atlas has exactly 1,234 odd masks and one affine light orbit
per mask. For every representative, choose all heavy triples from the other
124 positions and all 64 relative sign vectors. One pass therefore covers
exactly `1,234*binom(124,3)*64=24,492,353,024` vectors and classifies all four
live profiles simultaneously. The production engine uses folded signed
chords; the audit engine independently forms the direct negacyclic product.
Retain every full-conductor vector above `M_3=228` for dual exact norms.

Run the engines sequentially, each with 1,234 one-CPU, 256 MiB tasks, 60-second
task caps, and at most 100 containers. Checkpoint every 16 returns and abort
on timeout, malformed output, or row disagreement. The 32-mask pilot measured
`68.453854` worker-seconds for 635,133,952 vectors, projecting about 2,640
worker-seconds per engine. Conservative combined cost is below `$0.50` and
wall time below five minutes. A prime odd norm part above `2^250` triggers
collision replay; otherwise exact norms below threshold close the endpoint.

Infrastructure launch `ap-Jq5ilys1UDMuhHb04wAVdk` failed during worker module
import because local path resolution assumed the checkout directory depth.
It completed `0/1,234` production and `0/1,234` audit tasks and supplies no
mathematical evidence. One import-safe retry was authorized under the stated
budget; no computational retry was authorized.

Import-safe Modal app `ap-w01euXu1uuSZMynixEsU9m` completed all 1,234
production and all 1,234 audit tasks. Modal transparently restarted two
preempted containers on the same inputs. The two independent engines agree
row by row after 24,492,353,024 vectors each:

```text
profile       vectors   M_3>228   full conductor   max M_3   full max
(6,5)          51,562      48,918           32,096       1074       1062
(5,3,1)        23,884      23,232           12,632        942        942
(4,1,2)         1,614       1,590              408        870        690
(6,1,0,1)       1,788         874              272        606        606
total          78,848      74,614           45,408
```

The production and audit engines used `2707.686703` and `5063.911652`
aggregate worker-seconds. The proper-conductor theorem removes the
`74,614-45,408=29,206` imprimitive exceptions.

Modal app `ap-B13nYXtQQsbfCqFKDPTeUr` computed every remaining norm in FLINT
and PARI in 46 batches. The engines agree entry by entry on 45,408 vectors and
20,636 distinct norms. Their common maximum is

```text
1139098407599461804511111865916270680930143333943822578584573946997885235216
```

and satisfies `N_max<2^250<2*N_max`. No norm reaches `2^250`; hence no
pair-feasible collision survives, all four profiles are excluded, and the
live positive even frontier advances to `V<=50`.

#### CR-E1-E25-ROUTER: exact last-live-majorant route decision

**Status:** COMPLETE PASS. The exact router is banked; no rerun is authorized.

At `N=256`, folded profile `(3,4,0)`, and `V=50` (`E=25`), derive the exact
positive-half L1 bound, enumerate every compatible integer magnitude profile,
certify the cubic-Hermite sign change at `M_3=13/14`, apply diameter parity,
and price the surviving profiles against the already-proved one-diameter
light atlas. This is a router only and must not claim any profile exclusion.

Run one one-CPU, 256 MiB Modal task with a 60-second hard timeout. The local
launcher must write the complete JSON packet, and the prepared independent
checker must reconstruct the profile ledger, the exact rational sign change,
the atlas usage, and the direct-census floor. Conservative cost is below
`$0.01`. A large surviving router or a cutoff below all attainable moments is
a route boundary, not authorization for an undifferentiated norm campaign.

Infrastructure app `ap-0xK5g91qR7LZzevi5tScu5` failed while importing the
remote module because checkout-depth path resolution ran at module scope. It
completed no computation and supplies no mathematical evidence. The one
authorized import-safe retry follows; no further retry is authorized.

Import-safe app `ap-Bmu0kinryPMCm1zYI5CWas` completed the single task. The
independent checker confirms `L<=15`, 12 energy profiles, the exact
`M_3=13/14` sign change, and nine parity survivors: five with one odd class
and four with five odd classes. They occupy 111 proved affine light templates,
giving a direct floor of 2,203,120,896 vectors per engine. The router excludes
no profile by itself.

#### CR-E1-E25-NINE-PROFILE-CENSUS: exact actual-vector route decision

**Status:** COMPLETE PASS. The bounded primitive remainder authorizes the
dual exact-norm pass below; no census rerun is authorized.

Run the exact E25 router's 111 affine templates through folded-chord and
direct-negacyclic engines. Each engine covers
`111*binom(124,3)*64=2,203,120,896` signed vectors. Record exact per-profile
counts, minimum and maximum `M_3`, conductor counts, and every vector above
the cutoff `M_3=13`. This decides whether exact norms remain a bounded route;
it does not itself prove an exclusion.

Run 111 one-CPU, 256 MiB tasks per engine, sequential engine passes, 60-second
task caps, and at most 100 containers. Checkpoint every 16 returns and preserve
partial rows on failure. The prepared checker replays every retained vector
and compares the two engines row by row. The identical E29 router size and
measured E26 throughput put conservative cost below `$0.15` and wall time
below five minutes. If the retained primitive set is too large for a bounded
dual norm pass, stop and seek an algebraic filter instead.

Modal app `ap-GPkfA9swDimrWIrdVL3u7Z` completed all 111 production and all 111
audit rows without retry. Folded-chord and direct-negacyclic engines agree
exactly after 2,203,120,896 vectors each:

```text
profile       vectors   M_3>13   full conductor   min/max full M_3
(5,5)          12,156     12,156            6,944          60/900
(1,6)          11,884     11,628            6,888           0/720
(4,3,1)         5,526      5,526            2,868         120/696
(0,4,1)           416        352               32           0/276
(3,1,2)           632        632              116         120/480
(5,1,0,1)         238        238               56          96/384
(1,2,0,1)         812        748               80           0/240
(0,0,1,1)          16          0                0             --
(0,0,0,0,1)         6          0                0             --
total           31,686     31,280           16,984
```

The complete dual pass used `250.331735` aggregate production worker-seconds;
the audit summary agrees exactly. The proper-conductor theorem removes the
other `31,280-16,984=14,296` cubic exceptions. Since only 16,984 primitive
vectors remain, exact dual norms are bounded and cheaper than the completed
E26 norm packet.

#### CR-E1-E25-NINE-PROFILE-NORMS: exact endpoint decision

**Status:** COMPLETE PASS. The nine profiles and `V=50` endpoint are closed;
no rerun is authorized.

Compute `Res(g,x^128+1)` for all 16,984 full-conductor E25 vectors above
`M_3=13`, in 17 batches of at most 1,000. Compare FLINT and PARI entry by
entry, record profile maxima, and independently test every odd part in the
pair-feasible interval `(2^250,2^256)` for primality. A prime eligible odd
part becomes an explicit collision-row candidate requiring exact replay; if
all norms are below `2^250`, the nine profiles and the `V=50` endpoint close.

Run one-CPU, 256 MiB tasks with 60-second hard caps and at most 100 containers.
Checkpoint every four batches and preserve partial output on failure. The
prepared checker binds the census and source hashes, compares both norm
ledgers, reconstructs all profile maxima and candidate records, and checks
coverage. Based on the completed 45,408-vector E26 packet, conservative cost
is below `$0.10` and wall time below two minutes.

Modal app `ap-P7nLJ3MSSHmUrHb9P2RSoX` completed all 17 FLINT and all 17 PARI
batches without retry. The systems agree entry by entry on 16,984 vectors and
3,727 distinct norms. Their common maximum is

```text
689346143769176281255733260656192958605975198224651023251426809106119000068
```

and satisfies `2*N_max<2^250<3*N_max`. No norm reaches `2^250`; there are no
eligible odd parts and no candidate collision rows. All nine E25 profiles are
excluded and the live positive even frontier advances to `V<=48`.

#### CR-E1-E17-ROUTER: exact cutoff-free V=34 route decision

**Status:** COMPLETE PASS. The exact router is banked; no rerun is authorized.

At `N=256`, folded profile `(3,4,0)`, and `V=34` (`E=17`), derive the exact
positive-half L1 bound, enumerate every compatible integer magnitude profile,
apply the one-diameter parity constraint, and price the surviving odd profiles
against the already-proved one/three/five-odd light atlas. This is a router
only: it closes no profile and changes no DAG status.

Run one one-CPU, 256 MiB Modal task with a 60-second hard timeout. The launcher
writes a complete deterministic JSON packet. The prepared independent checker
reconstructs the slack minima, magnitude profiles, layer caps, parity split,
matching ledger, atlas use, and direct-census floor without importing the
primary implementations. Conservative wall time is below one minute and cost
below `$0.01`.

PASS records the exact finite router and permits a separately priced actual-
vector census only if the workload and expected retained residue are bounded.
FAIL falsifies the proposed E17 routing specialization and returns the route
to analytic derivation. INCOMPLETE is evidence only and authorizes no retry
without a repaired source or explicit new route decision.

Infrastructure app `ap-KqmsjnSeuKSHccRguoGspV` mounted only the entry file,
failed during worker import of a local helper, and was explicitly aborted. It
completed no mathematical task and supplies no evidence. The self-contained
repair below is the single authorized retry; no second retry is authorized.

Self-contained app `ap-c8VmO1f95T4RM21QCIoMbA` completed the single task. The
independent checker reconstructs `L<=11`, six profiles, rejection of the
nine-odd profile `(8,0,1)`, and five surviving profiles: three one-odd and two
five-odd. They occupy 111 proved affine templates, giving a direct floor of
`2,203,120,896` vectors per engine. The router excludes no surviving profile.

#### CR-E1-E17-FIVE-PROFILE-CENSUS: exact actual-vector route decision

**Status:** COMPLETE PASS. The primitive residue is banked; no rerun is authorized.

Run the exact E17 router's 111 one/five-odd affine templates through two
independent engines. The primary engine uses folded oriented chords; the audit
engine directly multiplies in `Z[x]/(x^128+1)`. Each covers
`111*binom(124,3)*64=2,203,120,896` vectors. Record exact profile and conductor
counts and retain every full-conductor vector for a separately priced norm
decision. This census alone proves no endpoint exclusion.

Use at most 100 one-CPU, 256 MiB workers with 60-second task caps, checkpoint
every 16 returns, and abort on timeout, malformed output, or row disagreement.
The completed same-size E21/E25 campaigns put conservative wall time below
five minutes and cost below `$0.15`. The prepared checker reconstructs every
retained vector by direct negacyclic multiplication and checks source hashes,
atlas coverage, conductor, profiles, engine equality, and one hostile mutation.

PASS authorizes an exact norm campaign only if the retained primitive set is
small enough to keep its own conservative cost below `$0.10`. FAIL returns to
the engine or atlas derivation. INCOMPLETE retains partial rows as evidence
only and authorizes no automatic retry.

Modal app `ap-wX3VHEQgXjopXqefRieIpQ` completed all 154 rows without retry.
The folded-chord and direct-negacyclic engines agree exactly after
`3,056,582,144` vectors each:

```text
profile       actual   full conductor   proper conductor
(4,3)            530              162                368
(0,4)              0                0                  0
(3,1,1)          158               16                142
(0,0,0,1)          0                0                  0
total             688              178                510
```

The dual pass used `959.740393` aggregate worker-seconds. The independent
checker replays all 178 retained vectors exactly. Exhaustive emptiness removes
two profiles, and the proper-conductor theorem removes another 510 vectors.
The 178-vector primitive residue authorizes the bounded norm decision below.

#### CR-E1-E16-FOUR-PROFILE-NORMS: exact endpoint decision

**Status:** AUTHORIZED, not yet launched.

Compute `abs(Res(g,x^128+1))` for all 178 full-conductor E16 vectors in one
FLINT batch and one independently evaluated PARI/GP batch. Strip the exact
2-adic valuation before applying the row-prime cutoff. Whole-norm size is
diagnostic only.

Use one CPU and 256 MiB per engine with 60-second hard caps and at most two
containers. Preserve partial packets on failure. Conservative cost is below
`$0.01` and wall time below one minute. The prepared checker binds the census
and source hashes, compares all 178 norms entry by entry, reconstructs 2-adic
valuations and profile maxima, enforces the odd-part cutoff, and mutates one
engine ledger.

PASS with every odd part below `2^250` closes all four routed profiles and
V=32. Any odd-part hit requires exact factor/divisibility replay and does not
close the endpoint. INCOMPLETE supplies no status change and authorizes no
automatic retry.

Modal app `ap-nuzv6imnkUH0ElJlCLyKRy` completed all 111 rows without retry.
The folded-chord and direct-negacyclic engines agree exactly after
`2,203,120,896` vectors each:

```text
profile       actual   full conductor   proper conductor
(5,3)            608              196                412
(1,4)          1,152              272                880
(4,1,1)          188               20                168
(0,2,1)           92                0                 92
(1,0,0,1)         10                0                 10
total           2,050              488              1,562
```

The dual pass used `651.957882` aggregate worker-seconds. The independent
checker replays all 488 retained vectors exactly. The proper-conductor theorem
removes the other 1,562 vectors; the 488-vector primitive residue authorizes
the bounded norm decision below.

#### CR-E1-E17-FIVE-PROFILE-NORMS: exact endpoint decision

**Status:** COMPLETE PASS. The five profiles and V=34 are closed; no rerun is authorized.

Compute `abs(Res(g,x^128+1))` for all 488 full-conductor E17 vectors in one
FLINT batch and one independently evaluated PARI/GP batch. Strip the exact
2-adic valuation before applying the row-prime cutoff: because every
admissible row prime is odd and exceeds `2^250`, an odd part below `2^250`
cannot vanish modulo that prime. Whole-norm size alone is diagnostic only.

Use one CPU and 256 MiB per engine with 60-second hard caps and at most two
containers. Preserve partial packets on failure. Conservative cost is below
`$0.01` and wall time below one minute. The prepared checker binds the census
and source hashes, compares all 488 norms entry by entry, reconstructs 2-adic
valuations and profile maxima, enforces the odd-part cutoff, and mutates one
engine ledger.

PASS with every odd part below `2^250` closes all five profiles and V=34.
Any odd-part hit becomes a candidate requiring exact factor/divisibility
replay and does not close the endpoint. INCOMPLETE supplies no status change
and authorizes no automatic retry.

Modal app `ap-YS86fN9k5a8svWi6zF2boU` completed one FLINT and one PARI batch.
The systems agree entry by entry on all 488 vectors and 108 distinct norms.
The whole-norm maximum is

```text
2816861446662266258222239103326104068711609833031798890850684996153986296836
```

and 16 whole norms reach `2^250`. Their exact 2-adic reductions have maximum
odd part

```text
744372174442013450465816409476894770650462784978029532566873973061928116737
```

with `2*odd_max<2^250<3*odd_max`. There are zero odd-part threshold hits.
The independent checker reproduces every norm, valuation, profile maximum,
threshold count, and maximizing index and rejects one mutated engine ledger.
All five E17 profiles and the V=34 endpoint are therefore closed; the live
positive even frontier advances to `V<=32`.

#### CR-E1-E16-ROUTER: exact cutoff-free V=32 route decision

**Status:** COMPLETE PASS. The router is proved; no rerun is authorized.

At `N=256`, folded profile `(3,4,0)`, and `V=32` (`E=16`), derive the exact
positive-half L1 bound, enumerate every compatible integer magnitude profile,
apply the zero/two-light-diameter parity constraint, and price the surviving
even profiles against the already-proved zero/two/four/six-odd light atlas.
This is a router only and changes no DAG status.

Run one one-CPU, 256 MiB Modal task with a 60-second hard timeout. The launcher
writes a complete deterministic JSON packet. The prepared independent checker
reconstructs the slack minima, magnitude profiles, layer caps, parity split,
matching ledgers, atlas use, and direct-census floor without importing the
primary implementations. Conservative wall time is below one minute and cost
below `$0.01`.

PASS records the exact finite router and permits a separately priced census
only if its workload is already calibrated below `$0.20`. FAIL returns to the
analytic derivation. INCOMPLETE is evidence only and authorizes no automatic
retry.

Modal app `ap-UNOcTGZLQStD1pUQnlIcQG` completed the single task. The
independent checker reconstructs `L<=10`, five energy profiles, rejection of
the eight-odd profile `(7,0,1)`, and four surviving profiles: two zero-odd and
two four-odd. They occupy 154 proved affine templates, giving a direct floor
of `3,056,582,144` vectors per engine. The router excludes no survivor.

#### CR-E1-E16-FOUR-PROFILE-CENSUS: exact actual-vector route decision

**Status:** COMPLETE PASS. The census is source-pinned; no rerun is authorized.

Run the exact E16 router's 154 zero/four-odd affine templates through two
independent engines. The primary engine uses folded oriented chords; the audit
engine directly multiplies in `Z[x]/(x^128+1)`. Each covers
`154*binom(124,3)*64=3,056,582,144` vectors. Record exact profile and conductor
counts and retain every full-conductor vector for a separately priced norm
decision. This census alone proves no endpoint exclusion.

Use at most 100 one-CPU, 256 MiB workers with 60-second task caps, checkpoint
every 16 returns, and abort on timeout, malformed output, or row disagreement.
The completed same-size E20 campaign puts conservative wall time below five
minutes and cost below `$0.15`. The prepared checker reconstructs every
retained vector by direct negacyclic multiplication and checks source hashes,
atlas coverage, conductor, profiles, engine equality, and one hostile mutation.

PASS authorizes an exact norm campaign only if the retained primitive set is
small enough to keep its own conservative cost below `$0.10`. FAIL returns to
the engine or atlas derivation. INCOMPLETE retains partial rows as evidence
only and authorizes no automatic retry.

Modal app `ap-wX3VHEQgXjopXqefRieIpQ` completed all 154 templates. The two
engines agree row by row after `3,056,582,144` vectors each. In profile order
`(4,3),(0,4),(3,1,1),(0,0,0,1)`, actual counts are `[530,0,158,0]`,
full-conductor counts are `[162,0,16,0]`, and proper-conductor counts are
`[368,0,142,0]`. Thus 688 actual vectors reduce to 178 retained
full-conductor representatives; both zero-odd routed profiles are exactly
empty. Aggregate dual worker time was 959.740 seconds. The independent
checker reproduces every retained vector and rejects one mutated row.

#### CR-E1-E16-FOUR-PROFILE-NORMS: exact endpoint decision

**Status:** COMPLETE PASS. The four profiles and V=32 are closed; no rerun is authorized.

Compute `abs(Res(g,x^128+1))` for all 178 full-conductor E16 vectors in one
FLINT engine and one PARI/GP engine. Record exact powers of two and odd parts,
because the pair-feasible row prime is odd and exceeds `2^250`. The campaign
uses two one-CPU, 256 MiB Modal tasks and is priced below `$0.01`.

PASS requires exact engine agreement, positive norms, and every odd part below
`2^250`. FAIL produces a candidate norm witness. INCOMPLETE is evidence only
and authorizes no automatic retry.

Modal app `ap-NKEaivIgiXPWHEwHeBgkkM` completed both engines. They agree on all
178 vectors and 78 distinct norms. The exact whole-norm maximum is

```text
3310692535087337739109785704249356622971820103039851493935549506897278325762
```

and ten whole norms reach `2^250`. Their exact 2-adic reductions have maximum
odd part

```text
1655346267543668869554892852124678311485910051519925746967774753448639162881
```

with `odd_max<2^250<2*odd_max`. There are zero odd-part threshold hits. The
independent checker reproduces every norm, valuation, profile maximum,
threshold count, and maximizing index and rejects one mutated engine ledger.
All four E16 profiles and the V=32 endpoint are therefore closed; the live
positive even frontier advances to `V<=30`.

#### CR-E1-E15-ROUTER: exact cutoff-free V=30 route decision

**Status:** COMPLETE PASS. The router is source-pinned; no rerun is authorized.

At `N=256`, folded profile `(3,4,0)`, and `V=30` (`E=15`), derive the exact
positive-half L1 bound, enumerate every compatible integer magnitude profile,
apply the one-light-diameter parity constraint, and price the surviving odd
profiles against the already-proved one/three/five-odd light atlas. This is a
router only and changes no DAG status.

Run one one-CPU, 256 MiB Modal task with a 60-second hard timeout. The launcher
writes a complete deterministic JSON packet. The prepared independent checker
reconstructs the slack minima, magnitude profiles, layer caps, parity split,
matching ledger, atlas use, and direct-census floor without importing the
primary implementations. Conservative wall time is below one minute and cost
below `$0.01`.

PASS records the exact finite router and permits a separately priced census
only if its workload is calibrated below `$0.20`. FAIL returns to the analytic
derivation. INCOMPLETE is evidence only and authorizes no automatic retry.

Modal app `ap-4uZGK1UWEjeAnhVm6de5UE` completed the single task. The
independent checker reconstructs `L<=9`, three energy profiles, rejection of
the seven-odd profile `(6,0,1)`, and the two surviving three-odd profiles
`(3,3)` and `(2,1,1)`. They occupy eight proved affine templates, giving a
direct floor of `158,783,488` vectors per engine. The router excludes no
survivor.

#### CR-E1-E15-TWO-PROFILE-CENSUS: exact actual-vector route decision

**Status:** COMPLETE PASS. The census is source-pinned; no rerun is authorized.

Run the exact E15 router's eight three-odd affine templates through two
independent engines. The primary engine uses folded oriented chords; the audit
engine directly multiplies in `Z[x]/(x^128+1)`. Each covers
`8*binom(124,3)*64=158,783,488` vectors. Record exact profile and conductor
counts and retain every full-conductor vector for a separately priced norm
decision. This census alone proves no endpoint exclusion.

Use eight one-CPU, 256 MiB workers with 60-second task caps and checkpoint
after every return. The completed same-size E19 campaign puts conservative
wall time below two minutes and cost below `$0.03`. The prepared checker
reconstructs every retained vector by direct negacyclic multiplication and
checks source hashes, atlas coverage, conductor, profiles, engine equality,
and one hostile mutation.

PASS authorizes an exact norm campaign only if the retained primitive set is
small enough to keep its own conservative cost below `$0.10`. FAIL returns to
the engine or atlas derivation. INCOMPLETE retains partial rows as evidence
only and authorizes no automatic retry.

Modal app `ap-xIQLyhRtHtlRxbQkOIS7Yp` completed all eight templates. The two
engines agree row by row after `158,783,488` vectors each. In profile order
`(3,3),(2,1,1)`, actual counts are `[258,36]`, full-conductor counts are
`[64,0]`, and proper-conductor counts are `[194,36]`. Thus 294 actual vectors
reduce to 64 retained full-conductor representatives; the second profile is
entirely proper-conductor. Aggregate dual worker time was 52.945 seconds. The
independent checker reproduces every retained vector and rejects one mutation.

#### CR-E1-E15-TWO-PROFILE-NORMS: exact endpoint decision

**Status:** COMPLETE PASS. Both profiles and V=30 are closed; no rerun is authorized.

Compute `abs(Res(g,x^128+1))` for all 64 full-conductor E15 vectors in one
FLINT engine and one PARI/GP engine. Record exact powers of two and odd parts,
because the pair-feasible row prime is odd and exceeds `2^250`. Use two
one-CPU, 256 MiB Modal tasks with 60-second caps. The E16 calibration puts
conservative cost below `$0.01`.

PASS requires exact engine agreement, positive norms, and every odd part below
`2^250`. FAIL produces a candidate norm witness. INCOMPLETE is evidence only
and authorizes no automatic retry.

Modal app `ap-4c65PlujVH2D5kNI12Bcac` completed both engines. They agree on
all 64 vectors and 28 distinct norms. The exact whole-norm maximum is

```text
3003171528471974836716922425205211633163258783488230570091067301168069285892
```

and 32 whole norms reach `2^250`. Their exact 2-adic reductions have maximum
odd part

```text
1263041506267492322130816623667822529962454800313964008196082776100356004097
```

with `odd_max<2^250<2*odd_max`. There are zero odd-part threshold hits. The
independent checker reproduces every norm, valuation, profile maximum,
threshold count, and maximizing index and rejects one mutated engine ledger.
Both E15 profiles and the V=30 endpoint are therefore closed; the live
positive even frontier advances to `V<=28`.

#### CR-E1-E14-ROUTER: exact cutoff-free V=28 route decision

**Status:** COMPLETE PASS. The router is source-pinned; no rerun is authorized.

At `N=256`, folded profile `(3,4,0)`, and `V=28` (`E=14`), derive the exact
positive-half L1 bound, enumerate every compatible integer magnitude profile,
apply the zero/two-light-diameter parity constraint, and price the surviving
even profiles against the already-proved zero/two/four/six-odd light atlas.
This is a router only and changes no DAG status.

Run one one-CPU, 256 MiB Modal task with a 60-second hard timeout. The launcher
writes a complete deterministic JSON packet. The prepared independent checker
reconstructs the slack minima, magnitude profiles, layer caps, parity split,
matching ledgers, atlas use, and direct-census floor without importing the
primary implementations. Conservative wall time is below one minute and cost
below `$0.01`.

PASS records the exact finite router and permits a separately priced census
only if its workload is calibrated below `$0.20`. FAIL returns to the analytic
derivation. INCOMPLETE is evidence only and authorizes no automatic retry.

Modal app `ap-rxPXBVj2USK33LIXWpg4Lo` completed the single task. The
independent checker reconstructs `L<=10` and four energy profiles. All four
survive parity: two have two odd classes and two have six. They occupy 1,321
proved affine templates, giving a direct floor of `26,219,123,456` vectors per
engine. The router excludes no survivor.

#### CR-E1-E14-FOUR-PROFILE-CENSUS: exact actual-vector route decision

**Status:** COMPLETE PASS. The census is source-pinned; no rerun is authorized.

Run the exact E14 router's 1,321 two/six-odd affine templates through two
independent engines. The primary engine uses folded oriented chords; the audit
engine directly multiplies in `Z[x]/(x^128+1)`. Each covers
`1321*binom(124,3)*64=26,219,123,456` vectors. Record exact profile and
conductor counts and retain every full-conductor vector for a separately
priced norm decision. This census alone proves no endpoint exclusion.

Use at most 100 one-CPU, 256 MiB workers with 60-second task caps, checkpoint
every 16 returns, and abort on timeout, malformed output, or row disagreement.
The completed identical-size E18 campaign puts conservative wall time below
five minutes and cost below `$0.15`. The prepared checker reconstructs every
retained vector by direct negacyclic multiplication and checks source hashes,
atlas coverage, conductor, profiles, engine equality, and one hostile mutation.

PASS authorizes an exact norm campaign only if the retained primitive set is
small enough to keep its own conservative cost below `$0.10`. FAIL returns to
the engine or atlas derivation. INCOMPLETE retains partial rows as evidence
only and authorizes no automatic retry.

Infrastructure app `ap-C2U6Lugoj5XbrqQWnS2rLs` failed while importing the
worker module because the repository path was evaluated inside the remote
container. It completed zero of 1,321 tasks, ran neither census engine, and
supplies no mathematical evidence. The path guard was repaired before the one
authorized clean rerun.

Modal app `ap-rQOuJb9DVQwka46OLEj4Er` completed all 1,321 templates. The two
engines agree row by row after `26,219,123,456` vectors each. In profile order
`(6,2),(2,3),(5,0,1),(1,1,1)`, actual counts are `[982,714,100,40]`,
full-conductor counts are `[540,184,8,4]`, and proper-conductor counts are
`[442,530,92,36]`. Thus 1,836 actual vectors reduce to 736 retained
full-conductor representatives. Aggregate dual worker time was 7,636.622
seconds. The independent checker reproduces every retained vector and rejects
one mutation.

#### CR-E1-E14-FOUR-PROFILE-NORMS: exact endpoint decision

**Status:** COMPLETE ROUTE REPAIR PASS. The norm ledger and exception audit are
source-pinned; no rerun is authorized.

Compute `abs(Res(g,x^128+1))` for all 736 full-conductor E14 vectors in one
FLINT engine and one PARI/GP engine. Record exact powers of two and odd parts,
because the pair-feasible row prime is odd and exceeds `2^250`. Use at most
eight one-CPU, 256 MiB Modal tasks with 60-second caps and batches of 200. The
completed E18 norm campaign puts conservative cost below `$0.03`.

The original PASS criterion required exact engine agreement, positive norms,
and every odd part below `2^250`. Failure produces candidate norm witnesses;
INCOMPLETE is evidence only and authorizes no automatic retry.

Modal app `ap-A7rhyHWVrOpGoAZM9bOuSs` completed four FLINT and four PARI
batches. The engines agree on all 736 positive norms, with 262 distinct
values. The whole-norm maximum is

```text
5848948255836721605243059534285585250067895734911016890819011517212606236162,
```

and 152 whole norms reach `2^250`. The maximum odd part is

```text
2924474127918360802621529767142792625033947867455508445409505758606303118081.
```

The original below-threshold shortcut therefore FAILS: six vectors have odd
part at least `2^250`. They comprise three distinct integers, all below
`2^251`, and supply the complete downstream candidate packet.

#### CR-E1-E14-LARGE-ODD-CANDIDATES: exact threshold-exception decision

**Status:** COMPLETE PASS. The classifier is source-pinned; no rerun is
authorized.

For an exceptional odd part `R_odd<2^251`, any pair-feasible prime divisor
`p>2^250` would force `R_odd=p`. Modal app
`ap-JtCD7equumzMV4qV44ziGe` ran independent PARI `isprime` and FLINT
`is_prime` classifiers on all six exceptions. The engines agree: there are
three distinct odd parts, all three are composite, and there are zero eligible
prime candidates. All three happen to be `1 mod 256`, so congruence alone does
not pay them. The independent checker reconstructs every vector, norm,
valuation, threshold, residue, and one hostile mutation. This exact repair
closes all four E14 profiles and the `V=28` endpoint; the live frontier is
`V<=26`.

#### CR-E1-E13-ROUTER: exact cutoff-free V=26 route decision

**Status:** COMPLETE PASS. The router is source-pinned; no rerun is authorized.

At `N=256`, folded profile `(3,4,0)`, and `V=26` (`E=13`), derive the exact
positive-half L1 bound, enumerate every compatible magnitude profile, apply
the one-light-diameter parity constraint, and price the survivors against the
proved one/three/five-odd atlas. This router changes no DAG status by itself.

Run one one-CPU, 256 MiB Modal task with a 60-second hard timeout. PASS requires
the independently structured checker to reproduce every slack minimum,
profile, matching ledger, atlas count, and exact direct-vector floor. FAIL
records a deterministic route inconsistency. INCOMPLETE is evidence only and
authorizes no automatic retry. Expected cost is below `$0.01`.

Modal app `ap-i2oKjwTWqN24exJmrNCPtQ` completed the single task. The independent
checker reconstructs `L<=9` and four profiles: `(5,2)`, `(1,3)`, `(4,0,1)`,
and `(0,1,1)`. Two have one odd class and two have five; no profile is rejected.
They occupy 111 proved affine templates, giving a direct floor of
`2,203,120,896` vectors per engine. The router excludes no survivor.

#### CR-E1-E13-FOUR-PROFILE-CENSUS: exact actual-vector route decision

**Status:** COMPLETE PASS. The census is source-pinned; no rerun is authorized.

Run the 111 one/five-odd affine templates through independent folded-chord and
direct-negacyclic engines. Each engine covers
`111*binom(124,3)*64=2,203,120,896` vectors. Record exact profile and conductor
counts and retain every full-conductor vector for a separately priced norm
decision. The census alone proves no endpoint exclusion.

Use at most 100 one-CPU, 256 MiB workers with 60-second task caps and checkpoint
every 16 returns. The completed identical-size E17 campaign calibrates cost
below `$0.15`. PASS requires row-by-row engine equality and independent replay
of every retained vector. FAIL returns to the engine or atlas derivation.
INCOMPLETE preserves partial rows and authorizes no automatic retry.

Modal app `ap-AhqC0lLGj9BYMLmRpKa1mj` completed all 111 templates. The engines
agree after `2,203,120,896` vectors each. In profile order
`(5,2),(1,3),(4,0,1),(0,1,1)`, actual counts are `[418,252,104,46]`,
full-conductor counts are `[112,0,16,8]`, and proper-conductor counts are
`[306,252,88,38]`. Thus 820 actual vectors reduce to 136 retained
full-conductor representatives. Aggregate dual worker time was 613.766
seconds. The independent checker reproduces every retained vector and rejects
one mutation.

#### CR-E1-E13-FOUR-PROFILE-NORMS: exact endpoint decision

**Status:** COMPLETE LEDGER PASS. Four threshold exceptions remain; no norm
rerun is authorized.

Compute exact cyclotomic norms for all 136 retained vectors in independent
FLINT and PARI engines. Record exact 2-adic valuations and odd parts without
assuming a below-threshold outcome. One batch per engine, 256 MiB per worker,
and a 60-second cap put conservative cost below `$0.01`. PASS means exact
engine agreement and a complete ledger. Any odd part at least `2^250` becomes
an explicit downstream prime candidate; it does not fail the ledger or close
the endpoint. INCOMPLETE authorizes no automatic retry.

Modal app `ap-cXvEeUhd1ym0Ep1InsluxC` completed one FLINT and one PARI batch.
The engines agree on all 136 positive norms, with 36 distinct values. The
whole-norm maximum is

```text
4937981356753691307652038461254907642619144628263052811320856547919621259264,
```

and 112 whole norms reach `2^250`. The maximum odd part is

```text
2099233185140600860850973089797376067771315496789913419840767568645748406017.
```

Four vectors have odd part in `[2^250,2^251)`. The below-threshold shortcut is
therefore false, and these four exact vectors form the complete candidate
packet for the next decision.

#### CR-E1-E13-LARGE-ODD-CANDIDATES: exact threshold-exception decision

**Status:** COMPLETE PASS. The classifier is source-pinned; no rerun is
authorized.

Run independent PARI and FLINT primality classifiers on all four exceptions.
Because every exception is below `2^251`, a pair-feasible divisor above
`2^250` must equal the whole odd part. Record primality and residue modulo 256
for every vector. Two 256 MiB workers with 60-second caps cost below `$0.01`.
PASS means exact engine agreement and a complete classification ledger; an
eligible prime is a genuine surviving collision candidate rather than a
checker failure.

Modal app `ap-a4p98JmkMEXvNaIRL7bXzV` completed both classifiers. The four
exceptions comprise two distinct odd parts. Both are composite, all four
values are `1 mod 256`, and there are zero eligible prime candidates. The
independent checker reconstructs every vector, norm, valuation, threshold,
residue, and one hostile mutation. This closes all four E13 profiles and the
`V=26` endpoint; the live frontier advances to `V<=24`.

#### CR-E1-PROFILE-36-M32-PRIMARY: exact cofactor-32 direct census

**Status:** COMPLETE PRIMARY AND AUDIT PASS. All authoritative packets are
source-pinned; no rerun is authorized unless a pinned source changes.

At `N=256`, profile `(3,6,S=18)`, and cofactor `m=32`, enumerate the complete
19,840-orbit multiplicity-five atlas. The exact product ledger contracts 1,834
`(E,q,L)` records to 474 live records through `E=60`; the direct engine then
uses the proved parity-radius filter, exact autocorrelation energy, and
Arb-audited 48-bit fixed-root intervals. Retain every high-side witness.

The calibrated one-CPU benchmark covers one orbit at every parity weight
`q=3,...,15`, agrees exactly with the pre-optimization engine on every count,
and projects about 10.5 worker-hours. Run 1,240 batches of at most 16 orbits,
at most 100 one-CPU 256 MiB containers, with 60-second hard task caps and an
atomic partial packet after every return. The conservative cost is about
`$0.50` and below the `$1` authorization. No task is retried automatically.
PASS requires exact atlas coverage, all structural count identities, agreement
between the long-double screen and rigorous intervals, zero unresolved
intervals, and one retained state per high-side interval. INCOMPLETE or FAIL
preserves the packet as evidence and authorizes no retry. A separate,
independently structured exact audit is required before theorem promotion.

Modal app `ap-blU0kVG1XoQdz0XWxgLKwz` completed all 1,240 primary shards and
all 19,840 affine orbits in 42,561.764 one-CPU worker seconds. It covered
5,857,561,600 unique heavy-position triples, 187,441,971,200 singleton-sign
distance tests, and 679,384,891,200 exact heavy-sign tests. Of 239,131,808
product-live vectors, rigorous intervals place 239,131,588 below the complete
`32p` interval and 220 above; none is unresolved, and all 220 high-side states
are retained. The screen and rigorous intervals agree on every live vector.

The complete audit traverses positions and singleton signs in reverse order,
constructs its chord columns separately, and directly rebuilds every
low-energy autocorrelation. Its 13-row benchmark agrees exactly with both the
primary engine and an independent reverse hash-block pilot at every parity
weight. Run batches of at most 12 orbits with the same one-CPU, 256 MiB,
60-second, 100-container, atomic-checkpoint, and no-retry constraints. Its
projected cost is about `$0.58`, below the `$1` authorization. PASS requires
exact equality with every proof-relevant primary total and complete energy
ledgers; only then may the cofactor-32 theorem node be promoted.

Modal app `ap-JcLLKV4WPUIDrn8rhERbNh` completed all 1,654 audit shards and
all 19,840 affine orbits in 44,023.162 one-CPU worker seconds. It independently
reproduces all primary totals, including 84,923,111,400 radius triples,
339,892,636 directly rebuilt low-energy autocorrelations, and the exact
239,131,588/220/0 interval split. The source-pinned node verifier replayed the
complete packet and all 220 high-side lower intervals on Modal app
`ap-RltPJOCiFf2VhH1gYQMtdw`. This promotes
`e1_prize_n256_s18_profile_36_m32_exclusion` to `PROVED`.

#### CR-E1-PROFILE-36-M64: exact two-atlas cofactor exclusion

**Status:** COMPLETE PASS. All authoritative packets are source-pinned; no
rerun is authorized unless a pinned source changes.

At `N=256`, profile `(3,6,S=18)`, and cofactor `m=64`, an exact product ledger
contracts `E=2,...,65` to 255 `(E,q,L)` chambers through `E=46`. A primitive
atlas normalizes an odd-separated singleton pair in `Z/128`; a separate
all-one-parity atlas divides to exact multiplicity three in `Z/64` and then
lifts. This two-atlas split was required after audit caught that the initial
primitive-only normalization was incomplete.

The final direct-triple and reverse hash-block engines cover 12736 affine
orbits, 407552 singleton-sign assignments, 10179448632 unique radius triples,
and 81435589056 exact heavy-sign tests. Arb-audited fixed-root intervals place
7191424 product-live vectors below the complete `64p` interval and 142 above;
none is unresolved. All 142 high-side states are retained.

Authoritative Modal apps:

```text
product ledger:             ap-vGLCNU73MLJj9RDeI3qeG2
primitive atlas:            ap-jsMfCK4V0ZOgCMYLHX8R7R
fixed-root generation/audit: ap-LWtv7vAuj73JwMclHhmQee
primitive primary:          ap-Ku7oS4IA5YTB6bMTAD68xf
primitive audit:            ap-8NxLniYGvXr1XY60JB2Rbb
primitive high witnesses:   ap-dMbnhlT62Afo9s0CXj7S3I
all-one-parity atlas:       ap-AZqE2K0OIwaJ72JJ8NC3JR
all-one-parity primary:     ap-8bHvHbIdNO7uEIZAXHJFzz
all-one-parity audit:       ap-GXPXxEWBsDAcVHfNG5iY7a
all-one-parity witnesses:   ap-gXAQR7y8tv1kbCbNclOHe0
```

Every worker had a hard timeout at or below 300 seconds. The campaign used at
most 96 containers concurrently, remained within the sub-dollar authorization,
and performed no scientific computation on the WSL host.

#### CR-E1-PROFILE-36-M16-TWO-DIVISIONS: exact branch exclusion

**Status:** COMPLETE PRIMARY AND AUDIT PASS. No rerun is authorized unless a
pinned source changes.

At `N=256`, profile `(3,6,S=18)`, and cofactor `m=16`, the complete support
atlas splits into primitive multiplicity four in `Z/128` (39,936 affine
orbits), once-divided multiplicity two in `Z/64` (9,080), and twice-divided
multiplicity one in `Z/32` (903). A 41-representative Modal benchmark covers
every realized `(branch,q)` class. Its measured weighted projections are
121.464, 26.819, and 2.077 one-CPU hours respectively. Only the twice-divided
branch is authorized for a complete census; the other two are deferred.

Run the 903 twice-divided orbits in batches of at most three, using at most 100
one-CPU, 256 MiB containers with 60-second hard task caps and no automatic
retry. Write an atomic partial packet after every return and retain every
high-side witness. The calibrated cost is about `$0.10`, comfortably below
the `$1` authorization. PASS requires complete atlas coverage, every structural
count identity, exact agreement between the long-double screen and rigorous
48-bit fixed-root intervals, zero unresolved intervals, and one retained state
per high-side interval. A separately structured reverse-direct audit must
reproduce every proof-relevant total before theorem promotion.

Modal app `ap-ozjw9RBwmTg6BmHBmn0HSf` completed and atomically recorded the
first three-orbit shard before the local `tiny` RAMGuard wall clock interrupted
the client. Source-matched resumable app `ap-1xutdz21Bfop112ugKr65k` preserved
that shard and completed the remaining 300. The aggregate covers all 903
affine orbits in 7,723.486 one-CPU worker seconds. It covered
266,601,720 unique heavy-position triples, 8,531,255,040 singleton-sign
distance tests, and 59,378,994,368 exact heavy-sign tests. Of 205,513,652
product-live vectors, rigorous intervals place 205,486,644 below the complete
`16p` interval and 27,008 above; none is unresolved, and all high-side states
are retained. The screen and rigorous intervals agree on every live vector.

Run the separately structured reverse-direct engine in batches of at most
three under the same 100-container, one-CPU, 256 MiB, 60-second, atomic
checkpoint, and no-retry constraints. The primary runtime projects another
roughly `$0.10`. PASS requires exact equality with every proof-relevant primary
total and complete live/above energy ledgers.

Modal app `ap-kmhgYnrF7vWYttQXorFm0w` completed all 301 reverse-direct audit
shards. It independently reconstructs all 497,496,976 low-energy vectors and
reproduces every primary total, including the exact 205,486,644/27,008/0
interval split and complete live/above energy ledgers. This promotes only the
twice-divided support subnode; the two larger m16 branches remain open.

One source-pinned node-verifier replay is authorized on Modal with one CPU,
at most 2 GiB, and a 290-second hard task cap. It must reconstruct the complete
quotient atlas, product partition, both census ledgers, and all 27,008 retained
high-side interval witnesses. Expected cost is below `$0.01`; no broad verifier
suite or scientific rerun is authorized.

Modal app `ap-IVF9ra2KWJyhXPplppzymj` passed the one source-pinned verifier in
9.817 seconds. It reconstructs all 903 quotient orbits, all 3,685 product
records, both complete census ledgers, and every retained high-side lower
interval, and catches a hostile witness-metadata mutation.

Two targeted structural replays are authorized for the global DAG validator
and critical-harness coverage checker. Each uses one short Modal task and no
scientific enumeration; combined expected cost is below `$0.01`.

Modal apps `ap-ygaLDQODvhgXc1CG3DtGR5` and
`ap-xysNDmOuY80dHYl5tXXXAS` passed the global DAG validator and critical
harness coverage checker respectively. No structural or registration gap was
introduced by the new branch theorem.

#### CR-E1-PROFILE-36-M16-LARGER-BRANCHES: deferred exact censuses

**Status:** ONCE-DIVIDED COMPLETE; PRIMITIVE PRIMARY COMPLETE; REVERSE AUDIT
PARTIAL. No relaunch is authorized while the Modal workspace is disabled.

The initial once-divided and primitive m16 branches projected to 26.819 and
121.464 one-CPU hours from complete parity-class benchmarks. The contraction,
primary, and audit history for both branches is recorded below. The primitive
reverse audit may resume only from its source-pinned atomic checkpoint after
the external Modal workspace is re-enabled.

One 15-representative optimization benchmark is authorized for the
once-divided branch. It removes the non-proof long-double diagnostic and skips
heavy triples whose three positions are even: together with the even singleton
support, those vectors are polynomials in `X^2`, so their degree-128
cyclotomic norm is a square and cannot equal `16p`. Use at most 15 one-CPU,
256 MiB, 60-second Modal tasks. Expected cost is below `$0.01`; the benchmark
does not authorize a complete census.

Modal apps `ap-uS90mwAgnXkmFsSjw4xxgc` and
`ap-Jwda0y53bpMXMNp0GjPBNp` completed the no-diagnostic/even-square and
rigorous early-cap benchmarks. Weighted projections fall from 26.819 to
19.529 and then 16.779 one-CPU hours. Modal app
`ap-bJ1BO3Mz3ciVx7Cnry7tUj` records the final projection. Every representative
retains the same fixed below/above/unresolved classification as the full
interval engine.

The once-divided primary census is now authorized. Run 2,270 batches of at
most four orbits, with four independent subprocesses in each four-CPU,
512 MiB Modal container, at most 100 containers, 60-second task caps, atomic
checkpoints, no script-level retries, and all high-side witnesses retained.
The calibrated 60,404 CPU-second projection costs about `$0.8`; four-way
container concurrency projects below five minutes wall time. PASS requires
all 9,080 affine orbits, the exact even-square omission count, all structural
identities, and zero unresolved fixed intervals. It authorizes no theorem
promotion without a separate reverse-direct audit.

Modal app `ap-6xxI9MGrLIK1n5crnIT6c3` completed that primary census. All
9,080 orbits passed in 2,270 four-way batches, with maximum task wall time
11.249 seconds. The exact totals are 2,680,779,200 raw triples,
76,819,415,040 post-square-omission sign-distance tests, 73,175,732,492
radius matches, 585,405,859,936 exact sign tests, 6,762,240,640 low-energy
vectors, and 1,816,625,504 product-live vectors. The fixed-root interval
classified 1,816,625,308 below and 196 above, retained all 196 high-side
witnesses, and left zero unresolved.

One 15-representative reverse-direct benchmark is authorized. It must use the
independent reverse enumeration, the original full fixed-root interval, and
the same exact square-norm omission. It must reproduce every primary count on
one orbit for each represented odd-chord weight before projecting the full
audit cost. This benchmark alone does not authorize the complete audit.

Modal app `ap-vysGPqGNw3Uo1bZm9osv0L` completed the reverse benchmark. All 15
odd-chord classes reproduce every corresponding primary count exactly. Modal
app `ap-mt8xdOni6TjNwFU6qkqBqE` projects 68,410.34 CPU seconds, or 19.003 CPU
hours, for all 9,080 orbits. This is approximately a sub-`$1` campaign at the
same rates as the completed primary, so one complete reverse-direct audit is
authorized: 2,270 four-orbit batches, four independent subprocesses per
four-CPU, 512 MiB container, at most 100 containers, 60-second task caps,
atomic partial output, and no script-level retries. PASS requires an exact
per-orbit match to the primary as well as the independent aggregate ledger.

Modal app `ap-HxT2OzXtS2r4jcKWzNH2a4` completed that audit. All 2,270 batches
and all 9,080 per-orbit comparisons passed. The reverse engine independently
reproduces 73,175,732,492 radius matches, 585,405,859,936 exact sign tests,
6,762,240,640 low-energy vectors, 1,816,625,504 product-live vectors, the
1,816,625,308/196 below-above split, and zero unresolved intervals. The
maximum four-worker task wall time was 13.321 seconds. This closes the
once-divided branch subject to the source-pinned node verifier; no additional
campaign under this request is authorized.

One primitive-branch optimization benchmark is authorized, with no complete
census implied. The primitive singleton support contains an odd position, so
the Galois involution `F(X) -> F(-X)` acts freely on the 32 normalized
singleton-sign patterns and permits 16 exact representatives. A second exact
optimization rounds each already-certified upper squared root factor upward
to a 16-bit dyadic mantissa and multiplies those upper bounds before invoking
the full interval. Benchmark one orbit in each of the 13 primitive odd-chord
classes, using at most 13 one-CPU, 256 MiB, 60-second Modal tasks. PASS
requires the full fixed-side ledger to be exactly half of the pre-involution
baseline in every class. Project cost before requesting further compute.

Modal apps `ap-csIUQ1ujheUPmHOCYAAirx` and
`ap-mE0wTipjjrqrejyw5lx958` completed that benchmark and projection. Every
class matches exactly. The weighted primary projection falls from 121.464 to
29.148 CPU hours (104,931.54 CPU seconds), but a complete primary plus audit
would still consume nearly all remaining credit, so neither is authorized.

One further 13-class benchmark is authorized at the same sub-`$0.01` scale.
Replace the 63-lag, eight-sign energy loop by its exact seven-coefficient
Walsh expansion, precomputing cross-vector dot products and replaying all 63
lags only for energy survivors to recover `L`. Retain the sign involution and
dyadic norm cap. PASS again requires exact half-baseline counts in every
class; project the cost before any larger request.

Modal apps `ap-o0Osge7eWPzD7RYeOZou0l` and
`ap-su7TzkrKQXDkLWG9g84C82` completed the fast-energy benchmark and weighted
projection. All 13 classes again match exactly. The full primitive primary now
projects to 25,008.33 CPU seconds, or 6.947 CPU hours, about `$0.33` at the
observed rate. One complete primary is authorized: 1,248 batches of at most
32 orbits, four independent subprocesses per four-CPU, 512 MiB container,
at most 100 containers, 60-second task caps, atomic checkpoints at bounded
intervals, no script-level retries, and all high-side representatives
retained. PASS requires all 39,936 affine orbits, exactly 16 sign-involution
representatives per heavy triple, exact Walsh/direct-energy agreement on
every low-energy survivor, structural count identities, and zero unresolved
fixed intervals. It does not authorize theorem promotion without an
independent reverse benchmark and audit decision.

Modal app `ap-tkhXMEdMpCXgm2LWUnXkEZ` completed the primitive primary. All
1,248 batches and 39,936 affine orbits passed in 22,736.06 worker seconds;
the maximum 32-orbit task wall time was 8.131 seconds. The exact
sign-involution ledger has 188,651,274,240 distance tests,
184,336,208,507 radius matches, 1,474,689,668,056 exact sign tests,
29,756,245,802 low-energy representatives, and 5,651,872,006 product-live
representatives. Certified intervals place 5,651,870,997 below and 1,009
above, retain all 1,009 high-side representatives, and leave zero unresolved.

One 13-class reverse benchmark is authorized. It must scan singleton signs
before descending heavy triples, construct its own chord columns, use an
independently inserted exact Walsh ledger, directly reconstruct every
low-energy survivor, and use the original complete fixed-root interval with
no primary dyadic cap. Use at most 13 one-CPU, 256 MiB, 60-second tasks. PASS
requires exact per-orbit agreement with the completed primary before a full
reverse cost projection is considered.

Modal apps `ap-cgOZPizDCrJE0YmFfdCkoh` and
`ap-dlfsihBSP21uvIM2RSslOr` completed the reverse benchmark and projection.
Every class agrees exactly, but the original full interval projects to
99,462.95 CPU seconds (27.629 CPU hours), above the automatic sub-`$1`
threshold; the complete audit is not authorized.

One final 13-class reverse optimization benchmark is authorized. Before the
full interval, independently compute and multiply all 64 certified integer
upper squared-root factors exactly (not with the primary's dyadic mantissas).
Strict-below products stop there; every residual still receives the original
full lower/upper interval. Use the same 13 one-CPU, 256 MiB, 60-second caps.
PASS requires exact agreement in all classes and a fresh cost projection.

Modal apps `ap-ATxdGYMJ3NJBvayKTp20Hc` and
`ap-AmrikHigBcehbCZ8jxlKb3` completed the exact-upper benchmark and
projection. Every class agrees exactly. The complete audit projects to
54,032.49 CPU seconds (15.009 CPU hours), about `$0.7`, so one full reverse
audit is authorized: 1,248 batches of at most 32 orbits, four independent
subprocesses per four-CPU, 512 MiB container, at most 100 containers,
60-second task caps, bounded atomic checkpoints, and no script-level retries.
PASS requires all 39,936 per-orbit primary comparisons, the complete
independent aggregate and energy ledgers, and zero unresolved intervals.

Modal app `ap-bvisSxyx7641bXRImfOwy8` reached batch 768 before Modal returned
`workspace ... is disabled` and terminated the campaign. The atomic packet is
valid and incomplete: 24,576 of 39,936 orbits and 768 of 1,248 batches pass
exact per-orbit comparison, with 3,477,665,782 product-live representatives,
3,477,665,087 below, 695 above, and zero unresolved. It records 35,110.54
worker seconds. Exactly 480 batches / 15,360 orbits remain. The resumable
launcher will skip the completed prefix; expected remaining compute is about
20,000--25,000 CPU seconds. Do not relaunch until the workspace is enabled and
the user confirms available credit. The primitive node remains unpromoted.

#### CR-E1-PROFILE-36-M16-GENERIC-THIRD-MOMENT: quantified no-go

**Status:** COMPLETE NEGATIVE ROUTE TEST. No rerun is authorized.

A generic layer-set third-moment/Hermite relaxation searched every integer
contact pair `1<=a<b<=144` against all live m16 product chambers. It excludes
only 7 of 436 distinct `(E,L)` pairs and leaves 949 of 967 live `(E,q,L)`
records, still through `E=89`. This generic relaxation is too weak to justify
further compute; any useful moment argument must exploit support-specific
structure rather than only the universal layer-set bound.

#### CR-E1-PROFILE-36-LOW-DYADIC-ORBIT-LEDGER: aggregate-first successor

**Status:** PROOF-ONLY PREFLIGHT COMPLETE; NO COMPUTE AUTHORIZED. The Modal
workspace is over its spend limit.

The remaining pure cofactors are `m=2,4,8`; candidate `m=16` awaits completion
of its independent reverse audit. Exact Hasse and Burnside packets give the
support interfaces

```text
m=2: 331359 primitive mu1 support orbits in Z/128
m=4: 159216 primitive mu2 orbits plus 18383 quotient mu1 orbits
m=8: 79360 primitive mu3 orbits; the affine support action is free
```

These counts do not authorize a radius census. The aggregate target should
count **full coefficient orbits with primitive-root incidence**, not support
orbits and not support-normalized vector rows. For a pure-dyadic collision
`Norm(F)=2^mu p`, `v_p(Norm)=1`, so exactly one primitive root is a simple
zero. Its signed translation slice contains exactly 256 oriented dictionary
vectors. The profile-only coarse allowance is therefore 367 full collision
orbits; orbit 368 fails.

Any future campaign must emit atomic partial packets and preserve, per full
coefficient-orbit representative:

```text
cofactor and exact 2-adic valuation;
canonical singleton and heavy supports plus all signs;
full affine canonical key, not only a singleton-support key;
exact norm interval and any row-prime candidate;
number of primitive-root incidences modulo that candidate prime;
translation stabilizer check and restored oriented-vector debit;
profile weight and cumulative exact weighted debit.
```

PASS may be either zero survivors or a certified weighted ledger within the
pair budget. Before any launch, first replay the tiny Hasse/Burnside/debit
verifiers and build a product/modular contraction. A generic census over all
588318 low-cofactor support orbits and broad energy windows is out of scope;
record it only as an external contributor request if no analytic contraction
is found.

#### CR-E1-PROFILE-36-CHARACTER-ELLIPSOID: certified sparse-associate preflight

**Status:** PREFLIGHT COMPLETE; GENERIC ENUMERATION REJECTED.

The proved `e1_conductor256_character_diagonal_exponent_router` replaces an
unbounded rank-63 unit search by one finite character-diagonal exponent
region for each fixed cofactor. A certified tiny implementation has completed
steps 1--2 below. Any future implementation must begin at step 3:

```text
1. DONE: certify outward intervals for all 63 nontrivial Fourier eigenvalues;
2. DONE: derive the conservative integer coordinate and Euclidean envelopes;
3. implement a **sparse-first** circular-unit multiplication and inversion
   recurrence in
   Z[X]/(X^128+1);
4. apply the cofactor boxes 1006,503,251,125 before the anchor product;
5. retain only exact profile-(3,6,S=18) products;
6. print a branch-and-bound node count, peak-RAM estimate, and dollar ceiling.
```

A floating-point FFT may guide subdivision but cannot accept or reject a
vector. Every boundary comparison uses directed intervals, and every
retained vector is replayed by exact ring arithmetic. The completed
preflight gives `|xi_t|<=7`, `sum xi_t^2<=101`, exactly
`16616854517524950208619690062355423946568371` coarse zero-sum vectors, and
at least `38,482,585,013,041` explicit vectors inside the weighted ellipsoid.
The subsequent inverse-kernel theorem sharpens the live body to
`|xi_t|<=3`, `sum|xi_t|<=60` while retaining the Euclidean bound.
Therefore coordinate-, Euclidean-, and ellipsoid-first enumeration are all
rejected; no fleet request should merely scale them up. A new request becomes
admissible only after an algebraic sparse-product/inverse recurrence has a
conservative state count under the limits, or after a small pilot establishes
early pruning independent of floating point. PASS of
the eventual enumeration requires a complete torsion-orbit count across
`mu=1,2,3,4` and comparison with `367`; it still does not pay lower-weight
profiles. No Modal credit is allocated by this entry.

#### CR-E1-CONDUCTOR256-L1-SVP-PROBE: route-deciding height pilot

**Status:** READY BUT BLOCKED BY WORKSPACE SPEND LIMIT. This is an exploratory
floating-point MILP, not a proof certificate and not a DAG promotion input.

The common-prime associate router gives `||lambda(u)||_1<77.202` for any two
live collisions in one cofactor. The certified spectrum and inverse-kernel
contraction bound the unique zero-sum exponent vector by
`-3<=xi_t<=3` and `sum|xi_t|<=60`. The launcher

```text
experiments/prize_resolution/e1_conductor256_l1_svp_modal.py
```

minimizes the actual 64-coordinate log `L1` norm subject to those integer
and aggregate bounds. It fixes cyclic and sign symmetry by putting a positive
largest-absolute coordinate at index zero. One two-CPU, 2-GiB container is
capped at 280 seconds; HiGHS is capped at 240 seconds and prints the incumbent,
dual bound, gap, node count, and a 70-decimal recomputation before shutdown.
The projected charge is cents, not dollars.

The proved Schinzel-height collapse now pays cofactors `4,8,16` without this
probe, so its only live E1 payoff is the residual cofactor-`2` family.

The first launch attempt on 2026-07-29 started no container and incurred no
compute. Modal returned

```text
Workspace ac-WIsI8fedhlHGSBu0g8EiyG has exceeded its spend limit
```

for the sole configured profile `allengrahamhart`. Do not bypass that account
control. Relaunch only after the workspace is enabled.

Route interpretation:

- an incumbent below `77.202` refutes the proposed torsion-only height shortcut;
  replay its integer exponent exactly in `Z[X]/(X^128+1)` and apply the sparse
  profile and inverse-coefficient filters;
- an optimum above `77.202` would collapse every fixed-cofactor associate family
  to one torsion orbit, but the floating solver result alone proves nothing;
- promotion after an above-threshold result requires a rational outer
  approximation and an independently checkable exact branch/LP, SAT, or
  lattice-cover certificate.

No fleet expansion is authorized. A single completed pilot decides whether the
proof-producing certificate is worth engineering.
## E1 profile-(2,10), cofactor-1028 low-energy certification

**Status:** superseded by proof. **Do not launch.**

The proved node `e1_s18_m1028_energy4_cubic_exclusion` replaced all 8,385
resultants by a complete cubic-moment screen. Its maximum cubic index is 24,
which gives the exact norm deficit `512/729` and puts every type below
`1028*p_min`. The launcher may be retained as an optional independent audit,
but it is no longer authorized serial-path compute.

The proved route originally left `m=1028=4*257` at autocorrelation energies
`E in {2,3,4,5,6}`. Exact small screens showed:

```text
E=2: four 257-compatible Galois types, all Norm/1028 above p_max
E=3: 329 compatible types, all exact Norm/1028 above p_max
E=4: 8,385 compatible types, all diagnostic log norms below p_min
```

Historical launcher command, no longer required:

```text
~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/e1_profile210_m1028_e4_norm_modal.py
```

The launcher submits 60 first-lag shard calls to one 512 MiB container with a
60-second per-call limit, and rewrites a local checkpoint after every returned
shard. It uses nine trial-division-certified 31-bit primes and CRT to
reconstruct every exact degree-64 resultant below the `18^64` AM-GM ceiling.
This is the same engine already certified on all 329 energy-three types and
five independent Bareiss norms. The expected terminal census is `8385` exact
quotients, all below `p_min`. Preserve partial JSON if the run is interrupted.

Launch log, 2026-07-29: one launch attempt was rejected before any container
started because workspace `ac-WIsI8fedhlHGSBu0g8EiyG` had exceeded its spend
limit. No app id was allocated and no credit was spent. Do not retry on this
workspace until its spend limit is explicitly restored.

Energies two, three, five, and six no longer require computation. The proved nodes
`e1_profile210_m1028_energy2_log_exclusion` and
`e1_profile210_m1028_energy56_log_exclusion` use the integral
autocorrelation bound `sum |A_d|<=E` and exact logarithm bounds to put energy
two above `1028*p_max` and energies five/six below `1028*p_min`. Do not launch
support classifiers for them. The 329-type energy-three ledger is now an
exact CRT-resultant certificate with digest
`d462adc241981e2e3aa9747a5ba582808d8ebf505e2df6a86fdad2df52a7d3cc`.
The only unpromoted computation in this request is the energy-four
certificate above. Reuse the modular engine rather than the slower Bareiss
fleet. A useful independent replay is a direct degree-128 negacyclic
resultant implementation.

## E1 profile-(0,18) joint low-energy/root falsification probe

**Status:** superseded by class descent. **Do not launch on the serial
route.**

The active weighted route needs at most five occupied cofactor-514 ideals.
The conditional class-descent theorem now gives at most two from one exact
`Q(zeta_128)` class-orbit certificate, without enumerating collision
profiles. The route-deciding compute is therefore
`CR-E1-QZETA128-P257-CLASS-ORBIT` below.

Historical rationale follows. It remains useful only as an adversarial audit
if compute is donated after the class certificate is replayed.

The proved singleton-completion no-go shows that local multiplicity one and
`F(s)=0 mod 257` alone admit all 128 ideals. The first useful experiment must
therefore impose the all-singleton realization and live energy window
`E=5,...,10` simultaneously. The all-unit energy-eleven and energy-twelve
profiles are excluded analytically and must not be retained.

Staged launcher:

```text
~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/e1_profile018_m514_low_energy_root_search_modal.py \
  --shards 16 --seconds 55
```

Resource cap: 16 containers, one CPU and 256 MiB each, at most 55 search
seconds per shard under a 70-second hard timeout. This is under 15 aggregate
CPU-minutes and is intended to remain well below `$1`; verify current Modal
pricing before launch. Every shard returns its best state even with no hit,
and canonical hits are retained in the final JSON.

Interpretation is deliberately narrow:

- a hit proves that the joint realization/root/energy gate is nonempty;
- no hit is heuristic evidence only and proves no emptiness statement;
- neither outcome proves or refutes five-ideal occupancy;
- the retained-hit filter omits the analytically excluded magnitude profiles
  `(9;1,2,0)`, `(10;6,1,0)`, and `(11;7,1,0)` while allowing the annealer to
  traverse them;
- exact resultant computation and grouping by `p=Norm/514` is a separate
  second stage, authorized only after genuine canonical low-energy hits;
- six equal exact official-prime quotients in distinct diagonal Galois orbits
  would be a true falsifier.

## CR-E1-QZETA128-P257-CLASS-ORBIT: J_63 fixed-field certificate - CLOSED

**Status:** RESOLVED LOCALLY; DO NOT LAUNCH. The exact Jacobi-sum residue
certificate supersedes the proposed degree-32 BNF computation.

### Mathematical decision and interface

The original 17-primary test is closed:

```text
J_65=(257,zeta_128-9)(257,zeta_128-248)
```

is nonprincipal by `e1_qzeta128_p257_j65_harbater_nonprincipality`.
Dembele's published Hilbert-class-field polynomial is irreducible modulo
257. Do not recompute this half.

Put

```text
beta=zeta_128-zeta_128^(-1),
E_63=Q(beta),
p_66=(257,beta-66).
```

Use the exact defining polynomial

```text
f_E63=Y^32+32Y^30+464Y^28+4032Y^26+23400Y^24+95680Y^22
      +283360Y^20+615296Y^18+980628Y^16+1136960Y^14
      +940576Y^12+537472Y^10+201552Y^8+45696Y^6
      +5440Y^4+256Y^2+2.
```

The repository verifies that it has 32 distinct roots modulo 257 and that 66
is one of them. It is obtained from
`Res_Z(Z^64+1,Z^2-YZ-1)=f_E63(Y)^2`.

The repository now certifies unconditionally that `p_66` is nonprincipal in
the degree-32 field `E_63`. Exact contraction gives
`p_66 O_(Q(zeta_128))=q_1q_63`; the ambiguous class-number calculation proves
that `E_63` has odd class number, so this transfer is injective on ideal
classes.

The certificate proves the last premise of
`e1_qzeta128_p257_two_involution_nonprincipality_certificate`; the 2-group
reduction promotes the 64-prime class orbit, class descent, and exact
profile-018 payment.

The proof constructs a 32-term Jacobi product `alpha` with
`(alpha)=(q_1q_63/(q_127q_65))^(2*21121)`. At
`r=5406977=256*21121+1`, a product of 32 power-residue characters kills the
full unit group and all `21121`st powers but maps `alpha` to `500235 != 1`.
Direct-character-sum and coefficient-polynomial verifiers agree.

### Superseded historical primary packet

The following BNF packet is no longer requested. It remains a possible
independent audit only:

1. construct `E_63` and its full ring of integers;
2. construct `p_66` and check that roots 9 and 57 both give fixed-field
   residue 66;
3. certify `p_66` nonprincipal unconditionally;
4. emit its exact nonzero class coordinate, certified class-character image,
   or another proof-producing obstruction, together with software versions,
   commands, relation data, and immutable hashes.

A direct PARI/GP primary should use a defining polynomial and integral basis
for the degree-32 fixed field, followed by:

```text
B = bnfinit(f_E63,1);
bnfcertify(B) == 1;
P = idealprimedec(B,257);
\\ identify p_66 by beta=66 in its residue field
\\ test bnfisprincipal(B,p_66,0)
```

The packet must check `#P=32`, the fixed-field identity, and one nonzero
certified class coordinate. The default `bnfcertify(B)` is required.
`bnfcertify(B,1)` only certifies that the true class group is a quotient of
the computed group and is insufficient for nonprincipality. Pin the PARI
version and official function contracts.

An alternative focused route may construct a certified ideal-class character
that is nonzero on `p_66`. `subcyclopclgp(128,21121)` can rigorously certify
the relevant minus-part size, but does not locate this ideal and is
insufficient alone. A class group computed under GRH is `INCOMPLETE`.

### Independent audit - satisfied

The primary verifier evaluates every Jacobi sum directly at all auxiliary
embeddings. The audit independently builds coefficient polynomials and
re-evaluates them. Both obtain `Psi(alpha)=500235`.

### Resource law

No container launch is authorized or needed. Both exact verifiers run in
well under one second with negligible memory.

Semantics:

- `PASS`: achieved - unconditional `p_66` nonprincipality plus independent
  exact audit;
- `FAIL`: an exact principal generator for `p_66`;
- `INCOMPLETE`: timeout, GRH-only output, unresolved principality, or one
  implementation only; evidence with no DAG status change.

## CR-K3-M2-R4-DIAGONAL-FACET-SAT: order-two whole-fiber defect classifier

**Status:** REQUEST DESIGN; not authorized for local or Modal execution
until the completeness router and proof-producing backend below exist.
This is a contributor request for the `K3` exact second-moment/source-facet
frontier, not a paid local fleet.

### Mathematical decision

The PROVED
`rate_half_kb_m2_r4_diagonal_fiber_resultant_interpolation_compiler` gives
the correct necessary symmetry for the diagonal stabilizer
`<tau x tau>`. For each quotient source label `p`, the two quadratic
component stars form a quartic divisor `R_p` and

```text
[R_bar(p)]=[tau^*R_p].
```

The automorphism need not preserve the source `X`-line. Therefore the
four root incidences over one complete `psi` fiber are transported as a
multiset and may be repartitioned into the two destination stars.
Individual-star transport is forbidden in this request.

Decide whether there exists any abstract packet satisfying all of:

1. the two source-label cases from Corollary 9.25,
   `L=I` or `|L intersect I|=5`, with
   `K subset I intersect L` and `|K|=5`;
2. one of the four complete two-regular pole-graph cycle types
   `6`, `4+2`, `3+3`, `2+2+2`, including every labeled
   diagonal-free graph and every canonical facet bijection
   `I -> L^c` up to a proved relabeling action;
3. one two-subset component star in each of the 24 divisor slots, with
   repeated slots allowed exactly as required by ramified degree-two
   fibers;
4. the `K`, `eta in L minus K`, and paired one-exchange facet
   containments of Corollary 9.27;
5. source degree four at every one of the twelve labels;
6. exactly four component-colored pole edges;
7. complete-source defect at most three; and
8. one fixed-point-free endpoint involution `bar` such that the
   four-incidence multiset over `bar(p)` is the `bar`-image of the
   multiset over `p`.

### Proof-producing output

A positive result must emit one canonical JSON survivor containing
`I,L,K`, the facet bijection, pole graph, endpoint involution, all 24
stars with divisor-slot multiplicities, color assignment, degree vector,
defect, and the twelve whole-fiber transport checks. The independent
checker must reconstruct every item from the raw records.

A negative result must emit an independently checkable UNSAT certificate
for every canonical stratum. Preferred formats are DRAT/LRAT with a pinned
SAT encoder and a second checker, or a smaller exact case certificate whose
completeness proof is readable without trusting the enumerator. A no-hit
search, optimizer lower bound without a proof object, or one labeled graph
does not promote a node.

If every stratum is UNSAT, the diagonal order-two orientation is deleted
before the `35 x 12` interpolation gate. If a survivor exists, it becomes
the sole input to that exact matrix gate and prevents further
facet/defect-only work.

### Pilot and resource law

A RAMguard pilot on 2026-07-30 fixed the aligned `L=I` case and one
`4+2` pole graph. An exact suffix-pruned check found no defect-at-most-three
survivor among the first 3,000 of 10,395 endpoint involutions before the
30-second hard stop. One isolated feasible involution was proved by complete
local enumeration to have minimum defect six. These are route-selection
observations only: the remaining involutions, other labeled graphs,
misaligned case, and other cycle types were not checked.

Do not resume this as repeated laptop shards. Before external launch:

1. prove the canonical-orbit router covers all labeled `I,L,K`, facet,
   graph, ramification, and involution data;
2. make the encoder resumable per canonical stratum;
3. cap each worker at one CPU and 512 MiB;
4. measure one complete stratum and publish the projected aggregate cost;
5. require compact proof artifacts and deterministic independent replay.

The expected computation is finite and small-memory, but no dollar estimate
is accepted until the canonical router and one proof-producing pilot are
measured. Large raw enumeration without certificates is out of scope.

## CR-K3-M2-R4-COORDINATE-VIETA-F29: signed-edge gate falsifier

**Status:** BLOCKED BEFORE START by the Modal workspace spend limit on
2026-07-30. No app id was allocated and no credit was spent. Do not retry
until the workspace limit is restored. One container only; no fleet.

The PROVED
`rate_half_kb_m2_r4_coordinate_k_fiber_vieta_rank_compiler` supplies exact
`10 x 8` positive and `10 x 7` negative common-`K` kernel gates. Before a
large symbolic elimination, test whether those gates can already be made
universally nonzero from the two allowed coordinate degree profiles.

The pilot fixes the exact field/configuration

```text
F_29,
I={+/-1,+/-4,+/-9},
J={+/-2,+/-3,+/-5},
xi=-9=20,
K=I minus {xi}={1,28,4,25,9}.
```

All five `K` values are squares. Exhaust the `15^5` ordered assignments of
the three antipodal edge orbits and the six nonantipodal edge orbits with
both lift orientations. Retain exactly the proved pair-degree profiles
`(4,4,2)` and `(4,3,3)` up to pair permutation and exact duplicate-edge
defect at most three. For every retained packet,
reconstruct the two exact Vieta matrices, require nonvanishing leading
support and a nonzero odd part, and test every aligned squarefree quadratic
`c` supported on two `J` labels against both full quotient identities.

Launcher:

```text
tools/ramguard modal -- ~/.venvs/modal/bin/modal run \
  critical/nodes/rate_half_band_closure/notes/kb_coordinate_vieta_f29_falsifier_modal.py
```

Resource cap: one CPU, 256 MiB, a 60-second hard container timeout, and an
internal 52-second partial-output deadline. Conservative cost is below
`$0.01`, hence below the campaign `$1` ceiling. The worker returns the first
exact positive/negative gate witnesses, complete counters, and any full
quotient witness. The independent local checker is
`verify_kb_coordinate_vieta_f29_witness.py`.

Semantics:

- `PASS` with a gate witness: exact falsification of any claim that the
  printed degree profiles alone force the corresponding determinant nonzero;
- `PASS` with a full quotient witness: stronger small-characteristic route
  falsifier requiring side-condition and liftability analysis;
- complete no-witness output: exact only for this fixed `F_29` label packet,
  evidence only for the universal coordinate branch;
- timeout: partial evidence only, with counters and any retained witnesses;
- no outcome closes or refutes the deployed-field coordinate orientation.

The blocked pilot has already been superseded for route selection by the
hand-constructed and independently replayed PROVED node
`rate_half_kb_m2_r4_coordinate_vieta_profile_only_f29_route_cut`. That node
gives one defect-two positive rank-seven witness and shows that its forced
colored quadratic is unsupported. A future launch is useful only as a
complete census of this fixed label packet, not as discovery of the first
witness.

## CR-K3-M2-R4-COORDINATE-COMPLETE-PRODUCT: canonical packet classifier

**Status:** EXTERNAL/DEFERRED.  Do not launch while the Modal workspace spend
limit is active.  No cost estimate is accepted until one canonical stratum
is measured; aggregate cost must remain below the campaign ceiling or be
explicitly reauthorized.

The PROVED
`rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler` replaces the
five-`K` determinant search by complete twelve-fiber product gates.  A
proof-producing classifier should:

1. canonically enumerate complete coordinate source-facet packets, including
   `I,L,K,eta`, the two paired degree profiles, all six complement records,
   pole-graph colors, and defect at most three;
2. form the exact `12 x 6` positive and `12 x 4` negative product matrices;
   for negative parity first apply the `6 x 3` paired-product involution
   matrix from `(KBNP-1)`; apply the same gate to positive kernels whose
   ratio `A_0/A_2` reduces to degree at most one;
3. emit a nonzero maximal-minor certificate for each deleted packet orbit;
4. emit every survivor with its exact product-map kernel and leading-support
   values, then lift only those survivors to the complete `q` system;
5. independently replay packet completeness, canonical-orbit ownership, and
   every minor from compact artifacts.

The negative lane now starts from only the five loop-budget survivors in
`(KBNL-2)`.  Apply the symbolic `(KBNP-3)` rule before any minors: two
distinct antisymmetric product pairs force every pair to be antisymmetric
and already delete the banked defect-zero fixture.  The positive lane must
use all twelve rows: the exact
defect-zero fixture has 140 of 5,040 `F_29` separator survivors, although no
assignment in that fixed family survives the complete product matrix.

Within the negative lane, shard first by loop count and use `(KBNQ-3)`.
The two loop-count-two skeletons require only signed `3 x 3` q determinants;
do not send their already-consumed loop rows to a generic `10 x 7` kernel.
After the product matrix passes, replace that determinant by `(KBNW-2)`:
the unique rank-three Mobius kernel fixes `B_2`, and two scalar product-to-q
welds are necessary and sufficient for all five common-fiber sum rows.  The
two labeled signed atlases have raw sizes 960 and 240.  Canonicalization must
retain edge-orbit orientations, and a negative answer must certify the
product minors or weld residuals for every orbit rather than report no hits.

The 960-row `(4,4,2)` atlas is now superseded by two PROVED symbolic
classifiers.  Its common-`K` survivors lie on only three antipodal label
loci, and all product-rank survivors are the six quadratic-linear rows
`(KB4P-3)--(KB4P-5)`, at most twelve geometric packets.  An external worker
must start from those rows and their two PROVED q-compatible orientation
classes, then compile the `eta` plus six `L^c` records.  Do not spend compute
rediscovering either common-`K` products or q signs.

The `(4,4,2)` outside graph is also PROVED unique and loop-free.  Its two
colored records are `C-D,C-E` with distinct `I` attachments, and its five
internal types are `D-E,+/-D-F,+/-E-F`, one of which is `eta`.  Any future
worker must combine this multiset with the six common-`K` product rows and
their two q orientations; arbitrary outside graph enumeration is obsolete.

The forced outside mate is now also PROVED for all six rows.  It is `-1` on
`H6` and `-l` on `H8`, with a printed product fraction whose protected norms
are `1,49,784,8464`; the two common pairs fix one explicit bilinear product
involution controlling the forced pair and the three residual pairs.  A
worker must start from this compiler, remove the forced value from the
seven-product outside multiset, and test one invariant binary sextic per
sign-gauged cell.  Re-solving a common Mobius map or enumerating fifteen
perfect matchings per row is outside the accepted request.

The accepted `442` paired-product input is exactly 36 invariant-form cells:
six common rows, `sigma=+/-1`, and three forced-`xi` location orbits.  The
seven products are `{cD,cE,sigma DE,+/-DF,+/-EF}`.  Remove the forced value,
then impose projective invariance of the residual binary sextic under the
printed row involution, product distinctness, and fixed-point exclusion.
Carry both q orientations only after a product cell survives.  The
horizontal variables `D,E,F` are independent of `l`; any task identifying
them with powers of `l` must be rejected.

If the 36 exact saturations are too costly, shard one cell per external
task with explicit memory/runtime limits and compact unit-ideal or survivor
certificates.  No local fleet is authorized.

The first 72 matching templates are now deleted symbolically: in forced
`cD` and `sigma DE` cells, the two unsigned residual products cannot pair.
Any external worker must skip those three matchings in each of the 24
affected cells, leaving cap 468 across all cells.

A bounded 30-shard pilot for `H8-L,tau=-1,xi=cD` is stored at
`critical/nodes/rate_half_band_closure/notes/kb_442_h8l_minus_cd_pairing_modal.py`.
Each shard uses one CPU, 512 MiB, and timeout 60 seconds, with explicit
partial `ERROR` rows.  The 2026-07-30 launch was rejected before any
container started because the Modal workspace had exceeded its spend limit;
cost was zero and no computational result was claimed.  This request may be
replayed externally after skipping the three already-proved templates.

That pilot target is now closed symbolically and must not be replayed for
discovery.  The common row descends to one quartic `P4(b)` and the residual
cell to two intrinsic variables; exact factor norms delete all 15 matchings
for both `sigma` signs.  The live `442` compute frontier has 34 cells and
matching cap 444.  Reuse the univariate descent for forced `sigma DE` and
`DF`; do not spend containers on the deleted `xi=cD` cells.

The remaining `H8-L,tau=-1` cells are now also PROVED empty.  Forced `DE`
and `DF` reduce to two intrinsic variables over the same quartic; exact
factor norms, six deployed-field unit ideals, and an alternate resultant
audit close every matching.  The entire common row is dead.  The accepted
`442` compute frontier is now five rows, 30 cells, matching cap 390.  Any
worker retaining `H8-L,tau=-1` is using an obsolete frontier.

The equal-degree loop exchange now also PROVES `H8-M,tau=-1` empty; no
compute is needed for that row.  The accepted `442` frontier is four rows,
24 cells, matching cap 312.  External workers must exclude both negative-
sign eighth-root singleton placements.

Both positive-sign eighth-root rows are now PROVED empty as well.  Exact
quartic factor norms, six deployed-field unit ideals, and a 54-case
alternate resultant audit close `H8-L,tau=+1`; positive loop exchange closes
`H8-M,tau=+1`.  The accepted `442` compute frontier is only the two H6 rows,
12 invariant cells, and matching cap 156.  Any external worker retaining an
H8 row is using an obsolete frontier.  These remaining rows have quadratic
base algebras and should be attempted symbolically before requesting any
container fleet.

The two H6 rows are now PROVED empty too, so the accepted `(4,4,2)` compute
frontier is empty.  The forced value `-b` either causes an immediate `DF`
product collision or reduces every aligned colored matching to the collision
divisor `a^2=b^2`; the opposite-sign cells have nonzero exact norms.  A
48-ideal deployed-field audit confirms the guarded deletion.  No external
worker should launch a `442` cell, matching, q-orientation, or interpolation
task.  The next already-routed negative two-loop compute frontier, if
symbolic work does not close it first, is the 20 invariant cells over
`M2/M3`.  The other three surviving `(4,3,3)` common-`K` ledgers
`X2/N1/L1` first require their own exact outside forced-mate/invariance
compiler and must not be folded into that 20-cell count.

The 240-row `(4,3,3)`
two-loop atlas is also superseded at the label level: `(KB43-3)` gives nine
one-parameter antipodal cells.  The first product-minor cut deletes
`X1,N2,Z1` and forces `b=-c^3` on `X2,N1,L1`.  At that intermediate stage,
only those three constrained cells and `M1,M2,M3` remained; the subsequent
paragraphs record their completed common-`K` classification.  Any replay
must use these symbolic ledgers, not the original labeled assignments.

The constrained cells are now fully compiled: `X2,N1` use one reciprocal
quartic in `M` plus a quadratic in `c`, and `L1` uses degrees `2 x 4` with a
linear locator.  Their total common-`K` cap is 24, with exact witnesses.
External work should not eliminate them again; carry them into complete
source-facet/seven-fiber assembly.  `M1` is now PROVED empty by a raw-boundary
resultant and an exact two-stage interior ideal certificate.  `M2,M3` are
also fully compiled: both use one shared reciprocal sextic followed by a
signed quadratic and a linear locator, with cap 12 per cell.  Thus all nine
`(4,3,3)` common-`K` cells are classified; the five surviving ledgers have
aggregate cap 48.  External work must start from those finite ledgers and
construct `eta` plus the six complementary source-fiber records.  Do not
spend compute on any common-`K` cell elimination.

For `M2,M3`, apply the PROVED outside-product compiler before enumerating
edge types.  It forces `xi=-M`, gives `p_xi` as an explicit rational function
whose numerator and denominator have resultant `2^32`, and fixes one
nonsingular bilinear involution for the singleton pair plus the three wholly
outside antipodal pairs.  Shard aligned `xi=eta` from unaligned `xi in L^c`
and, in the latter, colored from uncolored `xi`.  Only survivors of these
scalar gates should enter the full twelve-row Mobius interpolation.

The outside signed-pair graph is also PROVED unique.  There are no outside
loops; the two colored `I-J` records attach to distinct `I` pairs, and the
five internal multiplicities are `(1,2,2)`.  Up to pair names, enumerate
only `B-D,C-E,D-E,D-F(+/-),E-F(+/-)`, with one of the five internal signed
types assigned to `eta`.  A worker that generates arbitrary outside
multigraphs is outside the accepted request.

The accepted paired-product input is now exactly 20 invariant-form cells:
`M2/M3`, `tau=+/-1`, and five possible forced-`xi` edge types.  In each,
remove the forced product from `{bD,cE,tau DE,+/-DF,+/-EF}` and impose
projective invariance of the residual binary sextic under the printed
product involution, plus fixed-point and distinctness saturation.  This
replaces 300 perfect matchings.  The variables `D,E,F` are independent
horizontal coordinates; any worker substituting powers of the quotient
coordinate `M` is invalid and its output must be rejected.

If exact saturation or full-interpolation elimination for all 20 cells is
too expensive for the campaign budget, shard one cell per task with a hard
runtime/memory declaration, deterministic partial output, and a compact
certificate for every unit ideal or survivor component.  No such fleet is
authorized locally at present.

The 20 `M2/M3` cells are now PROVED empty and this request is obsolete.
Universal elimination of the two intrinsic horizontal variables gives 75
matching obstructions; all 300 sign/base evaluations are units in the exact
deployed rank-twelve quotient algebra.  Alternate projection and
multiplication-matrix audits replay every case.  Do not launch an `M2/M3`
product, interpolation, or q task.

The constrained `X2,N1,L1` cells are now PROVED empty as well.  Their exact
outside compiler gives three rank-eight base algebras, finite nonzero forced
products, and nonsingular bilinear product involutions.  The same 75
universal matching templates give 450/450 unit obstructions, independently
replayed by alternate projections and rank-eight multiplication matrices.
Thus the complete `(4,3,3)` paired-product frontier is empty.  No external
worker should launch a `433` cell, matching, q-orientation, or interpolation
task.  Together with the preceding `442` close, both currently compiled
negative two-loop skeletons are obsolete compute targets; recompute the live
coordinate skeleton census before posing another campaign.

Suggested pilot: one canonical packet stratum, one CPU, at most 512 MiB,
60 seconds, deterministic partial output, and no parallel fleet.  Modular
reconnaissance is evidence only; universal deletion requires symbolic or
proof-producing certificates whose saturations include distinct labels,
nonzero leading support, and the source-facet side conditions.

## Request: negative one-loop 442 sextic outside templates

The live common orbit `[9,10,12,13]` is now reduced to four rank-six sextic
quotients.  The two cubic factors of the former degree-12 gate are PROVED
empty.  In each live sign row the standard basis is

```text
{1,b,b^2,r,br,t},
S(b)=b^6-2b^5+7b^4-8b^3+7b^2-2b+1,
Norm(D_c)=2^19,       Norm(D_m)=652.
```

The explicit product involution is

```text
Phi(Y,Z)=(c+2b-b^2)YZ+b(c+b^2)(Y+Z)
         -b^2(c-b^2-2bc),
```

and the common singleton `c` has one forced outside mate `m`.  For each
fixed signed outside cell, choose one of seven products to equal `m` and one
of fifteen perfect matchings of the other six products.  The raw edge-sign
counts before target-sign symmetry are `S0=8`, `S1=16`, and `S2=1`; hence
`105` templates per signed cell, not per unsigned skeleton.

The target-representative sign quotient is now PROVED and must be used:

```text
S0: two parity cells tau_0=alpha beta gamma,
S1: two parity cells tau_1=alpha beta gamma delta,
S2: one cell.
```

Therefore the accepted cap is five signed cells and `525` templates per
common sign row, or `2100` over all four sextic rows, before quotienting by
the residual unsigned skeleton automorphisms.  A worker that expands the
original 25 sign cells is obsolete.

The residual template quotient is also now PROVED.  Simultaneous action on
the sign cell, forced record, full-pair members, and residual matching gives

```text
S0: 840 raw -> 64 canonical,
S1: 1680 raw -> 114 canonical,
S2: 105 raw -> 23 canonical.
```

The accepted compute cap is therefore 201 templates per common sign row and
804 over all four sextic rows.  The orbit-size distributions and a complete
enumerator are in the template-orbit classifier node.  External workers
must consume its deterministic representatives; the former 2,100-row cap
is obsolete.

The residual matching endpoint is now itself obsolete.  The PROVED binary-
sextic compiler replaces fifteen matchings by one invariant-form test after
the forced record is removed.  Quotienting signed forced records gives

```text
S0: 6 cells,       S1: 10 cells,       S2: 4 cells
```

per common sign row.  The accepted frontier is twenty invariant-form cells
per row and eighty over all four sextic rows.  The 804 matching orbits remain
an independent completeness audit only.  External workers must impose
coefficient proportionality of

```text
H(Alpha X+Beta Z,Gamma X-Alpha Z) and H(X,Z)
```

and must not enumerate residual perfect matchings.

The unknown-scalar formulation is now also obsolete.  The PROVED
binary-sextic eigenvalue compiler forces the exact identity

```text
H(M(X,Z))=Delta^3 H(X,Z),  Delta=Alpha^2+Beta*Gamma.
```

Its seven coefficient equations have rank three.  External workers should
reduce three independent equations per canonical cell and retain all seven
only as an audit.  They must not add a proportionality scalar or coefficient
minors.  The accepted workload is eighty cells times three scalar
conditions before outside sums and interpolation.

The row choice is now fixed as well.  The PROVED uniform-row selector shows
that `E_0,E_1,E_2` are independent in all four common sign quotients; their
`(h_0,h_1,h_2)` minor has deployed multiplication norm `1133299039`.
Workers should use those three equations exactly and should not spend a
shard selecting or row-reducing coefficient equations.

One caution is now exact.  The canonical `S1` forced-`DE` cell has a guarded
product-invariant `F_41` realization `(d,e,f)=(15,7,18)` on the printed
common witness, with all twelve products distinct.  A complete 1,600-pair
scan finds it uniquely.  Therefore a characteristic-independent
product-only contradiction does not exist for this cell.  Deployed shards
remain useful, but any deployed product survivor must be handed to the
seven outside source-fiber/`q` assignment; product survival is not packet
survival.

The representative deployed `S1` forced-`DE` task is complete and should no
longer be requested.  Sparse quotient multiplication gives three 25-term
polynomials; splitting the common algebra into its two irreducible cubic
fields gives the unit ideal after 79 S-pairs in each.  The accepted frontier
is now 79 cells.  External workers may reuse the checked sparse builder and
cubic-field solver on another canonical cell, but must pin its common signs,
outside signs, and forced record explicitly.

The opposite `S1` parity for the same forced-`DE/DF` type is also complete:
changing the first sparse factor from `dX+cmZ` to `dX-cmZ` again gives the
unit ideal after 79 S-pairs in both cubic components.  The accepted frontier
is 78.  Do not request either parity of this forced type in common sign row
`(1,1)`.

Both forced-`CE/CF` parity cells in common sign row `(1,1)` are now complete
as well.  Their three equations have 23 terms and reach the unit ideal after
56 S-pairs in each cubic component.  The accepted frontier is 76; these two
cells should not be requested again.

The two `tau_1=+1` forced-`EF+/-` cells in common row `(1,1)` are also
complete.  Their exact bases contain the forbidden coordinate `e`, after
435 S-pairs in each cubic component.  These are guard-saturated deletions,
not raw unit ideals.  The accepted frontier is 74.

The two opposite-parity forced-`EF+/-` cells are complete too: their 17-term
systems again finish with the forbidden equation `e=0` after 435 S-pairs in
both components.  Only two forced-loop `S1` cells remain in common sign row
`(1,1)`, and the accepted frontier is 72.

The two forced-loop `S1` cells in common sign row `(1,1)` are now complete
as well.  The forced equation `-d^2=m` is handled over the genuine quadratic
extension `theta^2=-m` of each cubic common component; nonsquareness of
`-m` is checked in both.  Each parity gives three 17-term equations.  Their
exact tower-field bases contain `1` after 57 S-pairs for `delta=-1` and 55
for `delta=+1`.  All ten `S1` cells in the representative row are therefore
empty, and the accepted frontier is 70.  Do not request another `(1,1)`
`S1` computation.  The next useful task is a proof of common-sign transport
or a separately pinned cell in another row; `S0` and `S2` also remain live.

Common-sign product transport is now PROVED, so no `S1` computation in any
of the four common rows should be requested.  Exact component reduction
shows that the reconstructed `c` and `m` coefficient triples are identical
in all eight row/component pairs.  The rational and forced-loop `S1`
systems are therefore coefficient-identical to the ten representative-row
systems.  All forty `S1` cells are empty and the accepted frontier is 40,
consisting of six `S0` and four `S2` cells per row.  This retirement applies
only to product invariance; source-root, `q`, and interpolation tasks are not
transported.

The forced-colored `S2` cell is also retired in every common sign row.
Forcing `sigma*cd=m` produces three seven-term equations; both cubic
components reach the raw unit ideal after seven S-pairs.  The forced sign
disappears and the all-row common-product identity transports the result.
Do not request this cell.  The accepted frontier is 36: six `S0` and three
`S2` cells per row.

The forced-`EF` `S2` cell is retired in every common row as well.  Its
denominator-cleared equations have seven terms and complete after 28
S-pairs with `e^2=0` in both cubic components.  This contradicts the
required nonzero outside representative, so it is a guard-saturated
deletion rather than a raw unit ideal.  The accepted frontier is 32: six
`S0` and two `S2` cells per row.

The forced-`DF` `S2` cell is retired in every common row.  Its three
seven-term equations complete after 28 S-pairs with both `d^2=0` and
`e^2=0` in each cubic component, contradicting the forced denominator guard
`d!=0`.  This is guard-saturated, not raw-unit.  The accepted frontier is
28: six `S0` and one forced-loop `S2` cell per row.

The forced-loop `S2` cell is retired in every common row, completing the
`S2` product close.  Once `-e^2=m` is forced, all six residual products form
three signed pairs, so no quadratic extension is needed.  The three
seven-term equations reach the raw unit ideal after seven S-pairs in both
cubic components.  Do not request any `S2` product cell.  The accepted
frontier is 24, all six `S0` cells in each common row.

Both forced-colored `S0` parity cells are retired in every common row.
Their three equations have eleven terms and reach the raw unit ideal after
29 S-pairs for both parities and both cubic components.  The accepted
frontier is 16: two forced-`EF` and two forced-internal `S0` cells per row.

Both forced-`EF` `S0` parity cells are retired in every common row.  Their
denominator-cleared twelve-term equations complete after 190 S-pairs with
`e^2=0` in all four parity/component runs, contradicting `e!=0`.  The
accepted frontier is eight: only two forced-internal parity cells per row.

Both forced-internal `S0` parity cells are retired in every common row.
Their fourteen-term equations complete after 406 S-pairs with `f=0` in all
four parity/component runs, contradicting the nonzero outside guard.  This
closes all `24+40+16=80` invariant-product cells for common orbit
`[9,10,12,13]`.  Do not request another product, q-placement, or
interpolation task for this orbit; determine the next live common orbit.

One local pilot has already been attempted and must not be interpreted as a
survivor.  It used common signs `(+,+)`, `S1` signs
`(alpha,beta,gamma,delta)=(1,-1,-1,1)`, forced `DE=m`, and residual pairs

```text
(CE,DF),       (CF,-EF),       (DD,EF).
```

The six common basis equations plus four outside equations reached the
60-second `ramguard tiny` cap before producing a Groebner basis.  No local
or Modal fleet is authorized.

An external run should shard one symmetry-reduced
`(common-sign row, signed skeleton cell, forced edge, residual matching)`
per task.  Every task must:

1. print its identifiers and equation degrees before elimination;
2. enforce a declared wall and memory cap and emit deterministic partial
   status on timeout;
3. return a compact unit-ideal certificate, or a guarded survivor ideal with
   dimension, basis, and all denominator/distinctness norms;
4. keep product-level survivors separate from outside sum and full
   interpolation claims; and
5. include an independently replayable reduction or multiplication-matrix
   audit before any DAG node is promoted.

Prefer a CAS with efficient finite-field quotient and elimination support
over generic SymPy Groebner.  A pilot should use one task only; estimate its
cost from that result before requesting parallel capacity.

## CR-KB-POS3-SAT: positive three-loop parametric saturation

**Status:** deferred theorem/algorithm and donated-compute request.  It is
not authorized for local or Modal execution.  The local exact compilers and
small-field pilots are complete; a raw point search is not requested.

**Target:** the eight signed lanes under the open critical node
`rate_half_band_closure`, specifically positive coordinate parity in the
residual KoalaBear `(m,r,delta)=(2,4,2)` row.

**Pinned inputs:**

- `rate_half_kb_m2_r4_coordinate_positive_three_loop_common_placement_atlas`:
  four loop-placement residuals `R_442,L`, `R_442,H`, `R_433,L`,
  `R_433,H`;
- `rate_half_kb_m2_r4_coordinate_positive_three_loop_signed_outside_vieta_atlas`:
  two cycle signs and seven target records per placement;
- `rate_half_kb_m2_r4_coordinate_positive_three_loop_outside_edge_eliminant_compiler`:
  the 22-term generic edge resultant and exact linear-product degree drop;
- `experiments/prize_resolution/rate_half_kb_positive_three_loop_fixed_kernel_groebner_probe.py`:
  four deterministic `F_17` algebraic-closure fixtures.  Seven of eight raw
  full ideals are units; the eighth has basis
  `d^2-4,e+1,f+1` and becomes a unit after target-collision saturation.

**Requested sharding:** one task for each
`(442/433, root-low/root-high, cycle sign)` lane.  Do not combine lanes in a
single basis computation.

For one lane, a worker should:

1. construct a primitive common-kernel vector from the `4 x 4` matrix
   cofactors and impose the corresponding common residual;
2. substitute that vector into the six noncycle edge eliminants, then append
   the selected cycle-sign eliminant;
3. split or saturate the generic `A!=0`, linear `A=0,B!=0`, and impossible
   constant branches without dividing away a degree drop;
4. saturate by `beta`, leading support at all five common labels, the common
   source-label differences, all six target-square differences, every
   outside/common root difference, and pairwise outside-root differences;
5. return either an exact unit-ideal/Nullstellensatz certificate or a
   positive-dimensional/zero-dimensional survivor basis with every guard
   norm and an original-row back-substitution witness.

**Acceptance standard:** a modular unit basis alone is route evidence, not a
theorem.  Promotion requires either an exact rational/integer certificate or
a modular reconstruction with independently replayed characteristic and
denominator bounds covering the official field.  A survivor must include
the seven guarded quotient roots, not only seven vanishing scalar
resultants.

**Pilot and cost gate:** first run exactly one 433 lane, because three of the
four fixed fixtures die before the cycle edge and this is the best candidate
for a short certificate.  Print input term counts, maximum basis size,
peak memory, wall time, and certificate size.  Estimate all eight tasks from
that pilot before parallel launch.  If the pilot exceeds its declared cap,
return the partial basis and do not retry at a larger cap without maintainer
approval.

## CR-KB-POS433-QPAIR: positive 433-1a quadratic outside-product systems

**Status:** deferred algorithm/certificate request.  Do not launch a raw
case fleet.  The exact interface is proved locally, but two representations
of one aligned case already exhausted 130-second and 180-second caps.

**Target:** the positive `433-1a -> O0b` route under
`rate_half_band_closure`.

**Pinned inputs:**

- the common-kernel uniqueness theorem and its full `A_2,A_0,B_1` vector;
- the quadratic paired-product resultant interface, including the separate
  `eta` and missing-mate `xi` choices;
- the seven-record outside-edge eliminant compiler, including generic,
  linear, and impossible-constant degree branches;
- the two signed `O0b` target lanes;
- the exact fifteen-cell common Vieta atlas and four pivot charts.

Each common row and cycle sign has a formal `5*7*15=525` outside-product
ledger.  This is not the requested shard count.  The residual target-sign
quotient is now exact: after the signed-edge gauge, the faithful stabilizer
has order two (`d -> -d`) and gives 39 aligned plus 228 near-aligned formal
orbits per common row and cycle sign.  The sealed certificate prints all
267 representatives.  The `EF` missing-mate subledger has 39 orbits; the
current A/B templates are gauge partners and cover five.  A subsequent
exact target-monomial calculation supersedes the proposed 34-template
fleet: all 267 representatives are relabelings of one universal system with
four necessary-and-sufficient product binomials, seven cleared squared-sum
equations, and explicit reconstruction of `d,e,f`.  Duplicate-role and
common-root-sign quotients are not yet composed.

A useful contribution should substitute this universal target compiler in
the guarded common-curve coordinate rings and quotient the resulting source
systems.  Do not derive more target-specific triangle templates.

For one canonical representative:

1. substitute the missing-mate product and squared-sum equations before
   elimination;
2. impose the three quadratic resultants without introducing source-root
   variables unless the resultant survivor must be lifted;
3. append at least one of the six remaining outside sum rows before running
   a standard basis;
4. saturate all common/outside leading-support, source-label, target-pair,
   and denominator guards;
5. return a replayable unit certificate or a guarded lifted survivor with
   all twelve original product/sum rows checked.

**Known pilot boundary:** direct source-pair variables timed out after 130
seconds in Modal run `ap-E6pJY7vJcqMmRTbdjiXkQ9`.  Three reduced quadratic
resultants exhausted the 180-second function cap in
`ap-ZAFf2iYtIe9hzMCa6lMD0g`.  These are failed algorithms, not survivors.
The exact `F_29` aligned probe with the missing-mate sum retains only 8
common points and 16 target triples in role cell `5`, cycle `+1`
(`ap-zH5YzdeJ1cG4hfyK6Q9eTJ`); this prioritizes but does not delete cells.
The near-aligned probe retains 32 common points and 64 target triples in
cells `4/-`, `5/+`, and `12/-` at `F_29`, while `F_13/F_17` are empty
(`ap-3u9hr5P3djUL4LhW10TZHm`, `ap-WmRDAbdJ2aYTgHG83lIHP8`,
`ap-k9y0M76KmbUE4qf16AhLNz`).  These also prioritize rather than delete.
Complete squared-sum `F_29` replays then delete every aligned and near-
aligned relaxation survivor (`ap-8dCdvjclUG5u1lmLxpkQGM`,
`ap-TabMc9Ck6pc6dVnLk4h6kY`).  Do not request more small-prime sweeps; the
open task is a deployed-field symbolic certificate for the lifted systems.

**Cost gate:** estimate the symmetry-reduced orbit count and run one case
with basis-size, peak-memory, wall-time, and partial-basis telemetry.  Do
not fan out unless that pilot has a plausible total budget and improves on
the known timeout.  Exact sparse elimination, triangular decomposition, or
finite-algebra methods are preferred over generic lexicographic Groebner.

### 2026-08-01 target-free refinement

The surviving `F_29` cell-5/cycle-`+1` lifts use two matching templates.
For both templates the target representatives `d,e,f` now eliminate
exactly.  The first version listed three necessary product-chain equations;
an exact lattice audit added the missing independent cross relation, so the
repaired chain has four product equations and one compact squared-sum cut in
the common rational maps `F,H` and source deck labels `u,v,w`.  See
`rate_half_kb_m2_r4_coordinate_positive_433_1a_triangle_target_elimination_compiler`.
The finite-field observation does not prove these two templates exhaustive.

The deployed-field cell-5 common chart is not finite: after exact guard
localization it has dimension one and a 23-element degree-order standard
basis (`ap-3NNIpulALnODMHqWkGTzM3`).  Direct expansion of either compact
target-free cut timed out (`ap-hiw5WgQAWd21qUlGGxugnw`), and an unsaturated
ambient seven-variable type-A standard basis hit 120 seconds
(`ap-5LekROrgmIeQwn2fIpVvVy`).

A useful contributed run should therefore:

1. ingest or reconstruct the 23-element localized common-curve basis;
2. compute a function-field, regular-chain, or quotient-ring presentation
   of that curve without expanding the target-free cuts ambiently;
3. reduce the four product-chain equations first, then append the single
   compact sum cut;
4. saturate source-pair distinctness and leading support only after the
   reduced system is zero-dimensional;
5. return a replayable unit certificate or a guarded original-row witness.

Do not rerun the ambient `dp` basis at a larger cap and do not fan out over
the 267 formal symmetry representatives.  The target exponent lattice is
already complete and universal; work on common-curve/source-system
quotients instead.

### 2026-08-01 signed-family regular-chain request

The PROVED cell-5 signed-family interface now eliminates the target roots
exactly.  For `DE+/DE-/BE` it gives four target-free unsquared equations in
three source roots; `DF+/DF-/CF` is identical with `b` replaced by `c`.
Exact relaxed probes found no independent seven-record Vieta completion
among 368 `F_17` or 1,072 `F_29` common survivors
(`ap-kFi1MWruL9asXhwnUqi5US`, `ap-oEfa1ita3OEaMxXD5yKsxH`).

The corrected saturated common quotient has dimension six and basis size
twelve after adjoining three source roots and two target roots.  In that
quotient the six original unsquared generators are sparse: each product row
has degree 15 and 96 terms, and each sum row degree 18 and 240 terms.  A
quotient-compatible generic `std` still exhausted 190 seconds
(`ap-uG1IwuZNXrj32LwEaDaO5b`).  The manually target-free presentation is
worse: cut sizes are 769, 78,105, 43,634, and 58,964 terms
(`ap-XvpdSEjqpJgkteo3AudUPb`).
The `BE` endpoint polynomial now factors exactly as a guarded unit times
`(z-t)R_b(z)` with `degree_z R_b=3`, total degree 14, and 120 terms.  The
known root `z=t` is forbidden for the outside edge.  Replacing the colored
product row by `R_b` did not make the combined generic basis finish
(`ap-OEAvKJxyhQn0ulMiNUF8Yq`), so use the cubic only after signed-pair
decomposition.
The signed pair by itself has common-quotient dimension five, basis size
twelve, and only four 96/240-term generators, yet generic `std` still timed
out (`ap-cGvpVPiwsv1wiGLv3z4FHK`).  This rules out “drop the colored row and
retry the same algorithm” as the requested contribution.

Requested contribution:

1. ingest the saturated projected common ideal, not the unsaturated
   three-minor ideal;
2. triangularize only the signed `DE+`,`DE-` pair first, preferably by a
   regular chain, subresultant sequence, or factor-by-factor norm;
3. report dimensions and guard norms for every component before appending
   `BE`;
4. append the colored edge only to surviving signed-pair components, then
   saturate `Delta D_0D_1D_2`, source collisions, and common/outside labels;
5. return a unit certificate or an original unsquared-row witness;
6. repeat for the `DF` family only if the first family survives.

Do not increase the generic standard-basis cap, run both families in
parallel, expand the four target-free cuts ambiently, or fan out over the
267 matching representatives.  The desired output is a component ledger,
not a longer timeout.

### 2026-08-01 finite-algebra refinement

The common compiler now accepts an explicit `(prime,iota)` and recomputes
all modular normalization at that prime.  This repairs an invalid discovery
shortcut that reduced polynomials already made monic modulo the deployed
prime.  The only banked small-field results below use a genuine square root
of `-1` in the probe field.

At `p=65521`, `iota=24297`, the saturated generic cell-5 fiber over
`F_p(t)` has dimension zero, basis size six, vector dimension four, and one
minimal component (`ap-9rQUOuge1TNoa1ufF3u9MR`).  FGLM gives a three-element
lex basis whose primitive `b` polynomial is a reciprocal quartic.  Direct
coefficient reversal and the lifted substitution `u=b+b^{-1}` independently
verify its descent to a quadratic (`ap-KCxeFPbJGAalI2aKR9nxem`).

After eliminating `r,c`, the signed `DE+`,`DE-` pair is one reciprocal
quartic plus four cuts of `(degree,terms)=(9,24),(8,32),(9,24),(8,32)`.
A four-minute `slimgb` pilot still timed out
(`ap-F0mNsrUqkAmnr1ADk2V20i`).  Do not rerun that basis with a larger cap.
Ordinary deployed block elimination subsequently produced the exact 19-term
reciprocal quartic and trace quadratic
(`ap-D4GXYWOVhTEiEfabnKO9Ht`), now banked as a PROVED child.  A second exact
run (`ap-3hVthJkmosYTdYTQ4Kc91v`) gives one guard-unit `r` formula and four
`c` charts; their simultaneous exceptional cubic has no deployed-field
root.  Compute the signed cuts separately on those four rational charts.
Only then append the residual `BE` cubic and sum row.

Singular 4.3.1 cannot lift this function-field workflow directly to the
deployed characteristic: its backend rejects characteristics above `2^29`
after the 12-element affine basis is computed
(`ap-JwQiY0HAW4TvF01vmVmtPj`).  A contributed implementation must use a
different exact finite-algebra backend or symbolic identities checked in the
deployed polynomial ring.  The `F_65521` result is evidence and a shape
compiler, not a deployed-field theorem.

### 2026-08-01 deployed colored-chart backend fence

Do not expand the target-free square cut at the deployed prime.  The
factored Singular assignment enters a backend capped at `2^29`; the Python
route expands other cuts to 58,964 terms before any basis step
(`ap-WHPxRTl9RMJGjEtD328bNO`).

The equivalent unsquared system with explicit `d,e` compiles cleanly with
signed-equation term counts `96,240,96,240,120,240` and a nine-term chart
guard (`ap-ixMbNHMyuEwVxEDbYXAUsT`).  Chart 2 nevertheless timed out after
240 seconds (`ap-UcfpDVxgnQOjNOoqELThke`); do not fan this basis to the other
three charts.  Algebraically eliminating `d` lowers the `DE+/DE-` ledger to
`769,4502,240` terms, but Singular rejects the deployed cubic-edge resultant
(`ap-EnuadAiVWmVBrNOExVkFDX`).

The next implementation should reuse the already-PROVED 22-term
quadratic-quartic edge norm.  Encode its coefficient definitions and norm as
a sparse auxiliary-variable circuit, or compute the one low-degree
resultant in a backend that supports `p=2130706433`.  Do not request a longer
generic basis.

The sparse norm circuit has now been implemented.  Its deployed chart-2
ledger has common equations `19,19,24` terms, reconstructed signed-pair
equations `769,4502,240`, and colored norm definitions bounded by 757 terms
with final pseudo-remainder/norm equations of `6,7,3` terms
(`ap-UygmUkG2dtvijTgXIIx5Xs`).  The combined circuit still timed out at 240
seconds (`ap-RMLTMaMIIjpqLWjEKaJ4ps`).  This localizes the next task: remove
the colored circuit again, triangularize the `769/4502/240` signed pair over
the rank-four reciprocal algebra, and append the colored norm only to its
component ledger.  Do not parallelize the same combined basis over charts
3--5.

The pair arithmetic circuit is smaller still: its six evaluation definitions
have at most 97 terms, its three signed-pair equations have `2,4,5` terms,
and its chart guard has nine terms (`ap-39oTPQR9XZaltpf0xAuYX8`).  Removing
all unused colored variables does not make either the elimination-block or
total-degree Singular basis finish at 240 seconds
(`ap-gysnK6QVGTEyVrlr64Rt7T`, `ap-9StDk2Yi93vpdKOnsgEft7`).

A direct SymPy implementation over `GF(2130706433)(t)` correctly detects the
rank-four primitive and denominator gcd certificates; SymPy's `invert` has a
false zero-divisor failure on the quadratic `c` denominator, repaired by
explicit `gcdex`.  Even with monomial-by-monomial degree-four reduction, the
six common coefficients do not finish within the five-minute wrapper
(`ap-xEl0f94ZLQjaPWCxVelMaE`, `ap-KVgOXwaAAJCZ3oNWUuC5Sf`).  Do not retry
this SymPy coefficient engine unchanged.  The requested computation is now
precise: implement the same four-generator system over
`GF(p)(t)[b]/(P)` in Nemo/FLINT/Magma (or another efficient rational-function
backend), return the signed-pair regular-chain/component ledger, and only
then append the compact colored norm.

### 2026-08-01 signed-pair stable-rank completion and revised request

The generic four-generator backend request above is now superseded.  The
Nemo/Groebner.jl route computes the exact chart-2 squared `DE+/DE-` quotient
over `F_2130706433(t)`: an 18-element Groebner basis gives vector dimension
64.  If `M` is multiplication by `g=d0*d1`, exact rational certificates give

```text
rank(M^2)=rank(M^3)=24,
dim A[g^-1]=24.
```

The upper bound is a checked factorization of all 64 columns through the
first 24 columns of `M^2`; the lower bound is the nonzero top-left minor at
the regular fiber `t=2`.  An independent checker clears denominators and
verifies all 5,160 polynomial identities with a 512-point NTT, above their
maximum degree 380.  A hostile audit rejects three certificate mutations.

Authoritative Modal apps, all stopped after bounded runs:

```text
ap-iL0NlhcML6PNSbeivvlEzy   M^2 normal forms
ap-EYSaER3gP4AUY24qgSBR9R   one-column retry
ap-8fGTO2L3xlaWIjHUftJLn3   exact structured rank factorization
ap-oXrrTGaRKqCJ4dWcE3nwht   cleared-denominator certificate
```

The revised contributed-compute request is not another standard basis.
Starting from the hash-pinned length-24 localized algebra:

1. determine its radical and residue-field factorization over `F_p(t)`;
2. certify nilpotent multiplicities if it is not reduced;
3. compute the finite exceptional-`t` discriminant and denominator locus;
4. restore the source-root square, nonzero, and distinctness guards on each
   surviving factor;
5. evaluate the compact colored `BE` norm factor by factor.

Return exact factor polynomials, guard norms, and independently replayable
certificates.  Do not call the length 24 a component count, sample only
special fibers, retry the failed generic basis, or append the colored norm
before the residue ledger is known.

### 2026-08-01 signed-pair generic-reducedness completion

The radical part of the revised request is now complete.  On the certified
24-dimensional stable image, exact multiplication by
`ell=x1+2*x0+3*b` was computed in all 24 columns and checked in all 64
ambient quotient rows.  At the regular fiber `t=2`, the first coordinate
vector is cyclic and the degree-24 minimal polynomial has derivative gcd
one.  Consequently `ell` is generically primitive and the localized algebra
is reduced over `F_2130706433(t)`.

The full two-column campaign completed ten shards and returned explicit
timeouts for columns 13--14 and 19--20 in
`ap-JbaRjWcp7CtiDT2nqnl8Sp`.  Exact one-column/matrix-method retries completed
the missing coverage in `ap-uAXb13GnCsiaM4LEhf3NLU`,
`ap-AfNdHRICf9Pb3bWsGVV0u0`, and
`ap-wn8HRH4Q7HLq0JKnI1RhbJ`.  All apps are stopped.

The new contributor request begins after radical computation:

1. compute the exact degree-24 characteristic/minimal polynomial of `ell`
   over `F_p(t)`;
2. factor it and report exact residue degrees and factor polynomials;
3. compute its discriminant and all source/denominator guard norms;
4. apply the residual colored `BE` product and unsquared sum on those
   factors.

Do not rerun radical algorithms or infer 24 components from degree 24.

### 2026-08-01 signed-pair primitive residue completion

The primitive polynomial and generic factor ledger are now complete.  Exact
Krylov elimination in `ap-oyB5HrYYmeguXMKmqODnsw` gives the monic degree-24
polynomial for `ell=x1+2*x0+3*b`; exact Nemo factorization in
`ap-yP081HXaVybgPvzsNW5FUX` gives irreducible degrees

```text
4,4,4,8,4
```

with every multiplicity one.  A standard-library checker reconstructs the
full rational-function product exactly and checks a regular pairwise-coprime
squarefree fiber.  SymPy 1.14 was tested as a second factor backend, but its
finite-field fraction-field conversion fails and multivariate finite-field
factorization is unimplemented; that failed audit is not evidence.

The revised contributor request starts in the five residue fields:

1. express the required source-square, collision, chart, and colored
   invariants as polynomials in `ell` modulo each factor;
2. compute exact guard norms and the finite exceptional-`t` locus;
3. evaluate the residual colored `BE` cubic and unsquared sum factor by
   factor;
4. return unit gcds/norms or exact surviving residue factors.

Do not recompute the pair quotient, stable rank, radical, primitive
polynomial, or factorization.

### 2026-08-02 signed-pair primitive coordinate completion

The first item in the residue-ledger request is complete.  Exact multiplication
columns for `x1,x0,b` were computed in `ap-9TDK6ccFWgwFvBjLsIIkwb`.
Three independent exact Krylov solves in
`ap-oJCcerqPq6wNwVNLasPkSx` express every variable as a degree-below-24
polynomial in `s=ell`.  A combined three-right-hand-side attempt
`ap-HpMM8Cb1LRiDU6cIvMUx0r` timed out and supplies no claim.  All apps are
stopped.

The exact map packet is
`001c959648176669651c87a913f2c830ad425a4f1e240041cc4edeb63d69a009`;
the coordinate-column packet is
`f5bfdb6cb515b6bbe54fa1abd19d1517759b0a584f501aa308e76f68e1ff1e25`.
The independent checker verifies `p_x1+2*p_x0+3*p_b=s` coefficientwise and
replays all three actions at `t=2`.

Requested next computation:

1. translate the already-defined source nonzero, collision, square, and chart
   guards into `s` with these maps;
2. reduce them modulo each exact primitive factor of degrees `4,4,4,8,4`;
3. compute exact resultants/norms over `F_2130706433(t)`;
4. distinguish an identically zero component from a nonzero norm with a finite
   exceptional-`t` locus;
5. append the compact colored `BE` condition only after this guard ledger.

Do not recompute the stable basis, primitive polynomial, factorization, or
coordinate maps.  Do not infer a source-root lift or component deletion from
the squared coordinate formulas alone.

### 2026-08-02 generic guard-unit completion

Whole-component guard degeneration is now excluded without a remote run.
At the exact regular fiber `t=2`, the five primitive factors, exact
`b,x0,x1` maps, and chart-2 `r,c` lift give 150 nonzero remainders:
22 declared common-chart guards and eight necessary squared
outside-incidence guards on each factor.  The canonical ledger hash is
`a48d3a028d422b19edda8d6ecac1f663bf2710fbc491a492b660b6b6e264bcb6`.
Therefore all 30 elements are units over `F_p(t)` in every residue field.

This does not print their rational norms or classify the finite
exceptional-`t` zeros.  The preferred next route-deciding computation is
the generic colored `BE` restriction on all five fields, with exceptional
guard-norm fibers kept as a separate ledger.  Do not spend a broad campaign
computing all 30 norms unless the colored restriction survives generically.

### 2026-08-02 cell-5 generic colored-gcd bounded campaign

**Decision.**  On each of the five proved primitive residue fields

```text
E_j=F_2130706433(t)[s]/(phi_j),   deg phi_j in {4,4,4,8,4},
```

compute the exact gcd in `E_j[e]` of the DE+ signed-pair necessary
polynomial and the compact colored `BE` necessary eliminant.  Then divide
that gcd by its gcd with the target-collision guard `e^2-1`.  This is the
route-deciding generic colored restriction requested in the preceding
ledger entry.  The upstream interface is the exact second-moment / primitive
shift-pair lane; exceptional `t` fibers and all other matching cells remain
outside the campaign.

**Completeness and parameters.**  The proved primitive factorization gives
exactly five factors and the proved coordinate maps express `x1,x0,b` in
each one.  The proved chart-2 atlas reconstructs `r,c`; the proved outside
edge compiler supplies the DE+/BE necessary equations.  The launch covers
factors `1,2,3,4,5` independently, with no sample-prime or sample-`t`
substitution in the primary computation.

**Source and command.**  Source commit is the current Codex worktree until
banked.  Launcher:

```text
tools/ramguard modal -- modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd_modal.py \
  --factors 1,2,3,4,5 \
  --output experiments/prize_resolution/rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd_result.json
```

**Ceiling and partial-output contract.**  At most five parallel containers,
one CPU and 8 GiB RAM per container, a 270-second Julia subprocess cap, and
a 300-second Modal function cap.  Conservative total wall time is five
minutes and conservative requested-resource cost is below `$1`.  Each shard
returns `COMPLETE`, `TIMEOUT`, or `ERROR` with elapsed time, provenance
hashes, program hash, and bounded stdout/stderr.  Completed factors remain
usable if another shard times out; incomplete output is evidence only and
changes no status.  The app is stopped after the bounded campaign.

**Certificate.**  Every complete shard returns the exact pair and colored
polynomials, their monic gcd, Bezout multipliers, the collision-guard part,
and the quotient outside that guard as rational functions in `t` and `s`.
The deterministic local checker
`check_rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd.py`
validates provenance and independently replays the Bezout, gcd, guard, and
quotient identities on every irreducible finite subfactor at the regular
fiber `t=2`.  A generic theorem still requires an independent exact audit;
the regular-fiber replay alone is not used to promote a node.

**Effects.**  PASS means every outside quotient is constant and authorizes
an exact generic colored-incompatibility theorem after the independent audit.
FAIL with a positive outside degree returns an exact surviving generic
factor and redirects the attack to that component.  INCOMPLETE has no DAG
effect.  Compact results are stored at the output path above; raw artifacts
remain in Modal and are identified by the app ID and program hashes.

The one-factor setup validation app `ap-pmWZTeSBvdQXSwTDiBctqD` stopped
before Julia was launched because the remote Python image omitted SymPy,
which regenerates the six pinned sparse-kernel expressions.  It produced no
mathematical result.  The launcher now pins `sympy==1.14.0`; the Nemo image
layer completed and is cached.

The corrected bounded campaign completed in apps
`ap-jcIuGHdW1WxLKephFQDv0O` (factor 1) and
`ap-IKaYuOEIwen2OhFi6ccFhg` (factors 2--5); both apps stopped normally.
Exact function times were respectively `24.33` seconds and
`16.35,24.01,233.42,20.45` seconds.  The four quartic factors have monic
gcd exactly `e^2-1`; the octic factor has gcd `1`.  Thus every quotient
outside the collision guard has degree zero.  The compact five-factor packet
has SHA-256
`710b438062fc2e80f5c7b14ffb987d8f36a02d4b57953b30419bb320b88877a7`.

The deterministic checker passes all five shards and every irreducible
finite subfactor at `t=2`, including the returned Bezout identities.  This
completes the bounded campaign but does not yet promote a theorem: an
independent exact audit must reconstruct the DE+/BE polynomials and verify
the generic identities before the result enters the DAG.

**Registered exact audit.**  At source commit `e774c74a`, run the independent
packet parser
`rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd_audit_modal.py`
on factors `1..5`.  It does not invoke the primary gcd routine: it rebuilds
each `phi_j`, parses every rational-function coefficient independently, and
checks the returned Bezout identity and exact common factor in
`F_p(t)[s]/(phi_j)[e]`.  Five one-CPU/4-GiB shards have 150-second subprocess
and 180-second function caps; conservative campaign time is three minutes
and cost is below `$1`.  Each shard returns explicit `COMPLETE`, `TIMEOUT`,
or `ERROR` telemetry and a program hash; partial output has no status effect.
The local audit script regenerates every program hash and checks all markers.
PASS completes the generic certificate audit but still leaves exceptional
`t` fibers and source-equation provenance as the stated boundaries.

The audit completed in apps `ap-cpk6ggojSG2qXUsMmJ8BP4` (factor 1) and
`ap-JDaA7cgwB2vcKgfWVNJzvG` (factors 2--5); both stopped normally.  Exact
function times were `9.26` seconds and `7.92,9.60,13.85,7.96` seconds.
All five exact generic identities pass.  The audit packet has SHA-256
`e1651bf40f716eeef1daafab71b0f0b49a010d2d38395aa6ecde1d3e82b7bb81`,
and its local hash/marker checker passes.  This pays the generic Bezout
certificate audit; it does not classify exceptional `t` fibers.

### 2026-08-02 cell-14 linear-pair exact census

**Decision and authorization.**  The user renewed the monthly Modal credit
and explicitly authorized valuable numerical experiments.  The campaign
tests the route-deciding cell-14 subfamily in which a `de` record is missing
and the two residual `de` records are paired.  All arithmetic is exact over
`F_2130706433`; no sampled-prime inference is used.  The campaign exceeded
the protocol's default five-minute aggregate window under that explicit
authorization, but retained per-task hard caps, at most 32 containers, and a
conservative cost below `$3`.

**Completeness router.**  The signed atlas gives four source signs, four
target lanes, seven missing outside records, and fifteen perfect matchings.
The selected subfamily is the exact Cartesian product of 4 source signs,
4 lanes, 3 missing `de` records, and 3 residual-`de` matchings: 144 logical
cases.  Quadratic-pair reduction gives one target-free linear equation.  Its
open resultant and every irreducible factor of the common-coefficient
boundary are checked separately.

**Execution.**  Final apps were `ap-L0KpNyaoVMYhGpecdOKI2R` (48 pairing-0
complete cases), `ap-vElucfytu5kl97fbXEr2lp` (96 open projections),
`ap-tXKscerl0pr5s0NY8Wx2Sn` (768 role-0/1 boundaries), and
`ap-1LVqOLunDONjPiKM5zLStF` (320 role-2 boundaries).  One role-2 factor
timed out in the parallel launch.  Isolated replay
`ap-wNUhANWcKOGTQbuK1NAwkQ` used identical definition and program hashes and
completed unit.  Every app stopped normally.

**Certificate and effect.**  The compact aggregate has 144 open and 1632
boundary unit ideals, with explicit Cartesian coverage, source/result hashes,
factor profiles, and timeout-replay custody.  The independent audit checks
the matching enumeration, two boundary profiles, exact missing-role identity,
and hostile count mutations.  PASS promotes only
`rate_half_kb_m2_r4_coordinate_positive_433_1b_cell14_linear_pair_outside_exclusion`;
1536 raw cell-14 outside cases remain open.

### 2026-08-06 XR fiber-rigidity boundary fixture

**Decision.**  Test the proposed field-independent `(FR)` mechanism for
`xr_band_forced_commonroot_syzygy_count` on one exact smooth boundary
fixture.  The construction has `q=193`, `n=64`, `k=4`, `d=13`, `h=18`,
`ell=2`, and `r=h-d=2ell+1=5`.  The remote task exhausts all
`C(64,4)=635376` interpolation anchors and all 194 projective slopes, checks
the global tangent ceiling, and applies the normative lexicographic
first-match selector.

**Scope.**  PASS with split selected blocks falsifies only the broad
field-independent/THEOREM-R-style reading of `(FR)`.  It does not falsify an
official-row conjecture restricted to the first unpaid affine dimensions or
post-envelope profiles.  The preregistration and full adjudication are in
`notes/pilots_20260804/fiber_rigidity/`.

**Execution.**  The packaging-only app
`ap-3mwM41d1SzL3tjsBGyEZoG` failed before mathematical work began and was
stopped.  Primary app `ap-z6h81Tc1oAr9HAKqIdbkxZ` completed and stopped
normally.  It exhausted all 635,376 anchors, retained 631,833 canonical
codeword pairs, found global maximum 22, exactly two live slopes, and
`L_P=2`; both selected blocks have profile `(2,1,1,1)`.  Certificate SHA-256
is
`91248465187ab72abd9cbb4e9debe6e0feef9e52d26afed7fb568a0826680ec2`.

Independent-audit app `ap-wQGFHF5dPs7XXgZEBMq9cC` completed and stopped
normally.  Its checker imports no constructor code, rebuilds all structural
algebra, repeats the complete anchor/slope scan, agrees on all per-slope
maxima and first-match supports, and rejects twelve hostile mutations.

```text
XR_FIBER_RIGIDITY_BOUNDARY_COUNTEREXAMPLE_PASS seed=20260806 subsets=635376 canonical_pairs=631833 live=2 Lp=2 profiles=2,1,1,1/2,1,1,1
XR_FIBER_RIGIDITY_INDEPENDENT_AUDIT_PASS full_scan=true mutations=12
```

**Effect.**  The broad mechanism is refuted, while the official
post-envelope `(FR)` remains open.  No DAG status or edge changes.  A repaired
statement must use an explicit official-subgroup, high-affine, or
post-envelope hypothesis; local primitive equations alone are insufficient.

### 2026-08-07 K3 degree-12 checkpointed parity instantiation

**Decision.** Do not rerun the expanded degree `22`/`23` leading-curve
Gröbner routes. Two direct 780-second runs completed exact dimension-one seed
bases of sizes 25 and 27 but timed out after row reduction; a separate exact
pseudo-division run lowered both rows to `x`-degree five but grew them to
`23616` and `23484` terms before the final timeout. These endpoints are
fenced in the degree-12 decomposition node.

**Tested route.** Instantiate the PROVED parity identity

```text
V^d P(-U/V) =
  sum_j a_(2j) V^(d-j) Z^j
  - sum_j a_(2j+1) U V^(d-j-1) Z^j       mod U^2-VZ
```

for the two literal remaining rows before expanding `U,V,Z`. The bounded
metrics-only phase completed in app `ap-jVjceB5Npmz4Rm1xlGdJWm` in `51.64`
seconds at about `0.42 GB` peak child RSS. The direct rows have `52336` and
`49949` terms; the parity representatives still have `52257` and `49848`.
Their exact hashes are bound by the parity-identity verifier.

**Custody and ceiling.** The uncheckpointed prototype is
`degree12_parity_reduced_evaluation_probe_modal.py`. App
`ap-4QZZtNn47Q0jNj4rJCqIQA` was preempted twice around five minutes and then
aborted, producing no mathematical packet. A rerun is authorized only after
adding durable phase checkpoints. Use one four-CPU/16-GiB container, a
15-minute hard cap per phase, partial output on timeout, and a total requested
resource cost below `$1` for the representative. The representative does not
compress materially, so phase two and other-cell replay are not authorized.
Any successor must first exhibit a block-level factorization or syzygy while
`U,V,Z` remain unexpanded.

### 2026-08-08 positive 433-1b cell-4 matching-11 exact replay

**Decision.** Close the last live cell-4 matching-exchange orbit by exact
quadratic-resultant elimination and complete finite-field replay. The user
explicitly permits longer valuable Modal computations and renewed the monthly
credit. The primary compiler retained eight source-sign/colored-lane rows,
hard completion semantics, compact output, and a deterministic independent
checker. Total one-CPU cost remained below `$1`; no WSL-heavy computation was
used.

**Execution.** Compiler app `ap-KZ72bRFmoRTN8VNueSuzDK` completed all eight
rows. The first verifier app `ap-YnHNxRzPD9DpVJQrqp9SLP` exposed a stale
expected eliminant degree (`8` instead of the recorded exact degree `6`), not
a theorem failure. After repair, app `ap-hD8LPsYApvAxTnBAJS5d37` reached the
generic 270-second replay cap. The content-identical replay with a 600-second
remote-only cap, app `ap-74kOL7uM1Y7OHlIhM5mI1A`, passed in 372.41 seconds.
All apps stopped normally.

**Certificate and effect.** The complete root union has 60 candidate `r`
values, 16 guarded source points, eight compatible `(z,q)` candidates, and
16 nonzero final `Pair(-q,sigma_o ef)` evaluations, with no witness, target
boundary, free branch, or unresolved row. The independent verifier
recomputes all degree-3864/3868 norm roots and every source lift. This closes
matching 11 directly; exact transports pay matching 14 and both xi4 partners.
Separate disjoint-cover verifiers then close all 105 cell-4 labels and the
duplicate-role orbit `[4,7]`.

### 2026-08-08 positive 433-1b cell-12 elliptic common-locus campaign

**Decision.** Select a compact exact presentation for the next unclosed
duplicate-role orbit `[12,13]` before compiling any of its 105 outside
labels. Cell `12` is the representative: `BC-` is singleton and the source
matching is `(LA,AB),(AC,BC+)`. All expensive standard-basis work was sent
to Modal; only hash, JSON, and low-degree polynomial audits ran under local
`ramguard tiny`.

**Route selection.** The initial four-pivot chart found one-dimensional
common ideals for every pivot. Exact subset searches showed that no triple
of the eight lex rows generates the full guarded affine ideal, even after
route localization. Four specific quadruples become exact after additionally
inverting their leading coefficients. The failed exploratory birational
launcher had parser/syntax faults, produced no evidence, and was deleted.
The corrected pivot app was `ap-xjoaAlJ031oiZi6jcVczhf`; the unsaturated
subset app was `ap-BeB5FduQYUhe8wyHKYqfvf`; and the final exhaustive
leading-localized subset app was `ap-deMSQ71aFOEXmluIwPriXF`. These packets
are route-selection evidence only and promote no separate node.

**Complete structure.** App `ap-UGTRxHvSZteecD6UcEscYD` checked the selected
`AC` pivot in all four source-sign rows and all six product-cofactor charts:
all 24 runs completed with dimension one, compact basis size `15`, lex basis
size `8`, and unit pivot boundary. App `ap-Jc9a3zuxX9HLZwWOJMpaGx` proved the
exact leading-open presentation by a quadratic in `t`, a palindromic
quadratic in `b`, and a linear recovery of `c`; an alternate linear recovery
gave the same localized ideal. Removing the doubled route factor from each
base discriminant leaves a square-free quartic, hence a genus-one normalized
base.

**Boundary and kernel.** App `ap-J73jbPfsrEcJzlKzj4LCVU` classified all 12
leading fibers. Four split `b` fibers give exactly eight guarded deployed
points; eight quadratic `c` fibers have no deployed points. App
`ap-jKyXbePmY48WoHuLsDi9EZ` then produced one sign-independent primitive
eight-coordinate kernel. Seven common-row pairings vanish identically and
the remaining three reduce to zero on all four exact common ideals. The
independent local audit also checks all 80 row pairings at the eight boundary
points.

**Effect and spend.** The campaign promoted two small PROVED structural
nodes: the complete elliptic common-locus decomposition and its global
common kernel. It closes no outside label and does not close cell `12`.
Each final app used at most four 4-GiB containers for under five minutes;
the aggregate final-certificate cost is conservatively below `$1`. The next
authorized computation is a cheap 105-label structural router against the
fixed kernel, not a broad norm campaign.

**Rational-boundary outside closure.** The immediate finite follow-up ran in
primary app `ap-WZvIMr7B4J34FR0TsNOTqZ`. It covered the exact Cartesian
product of eight rational leading-boundary points, four target lanes, seven
missing records, and 15 residual matchings: 32 shards and 3,360 labels. The
missing product and squared sum give four target lifts for roles `0..4`;
the two endpoint roles fail a source-only compatibility equation. All shards
completed with zero witnesses and zero unresolved branches.

Independent app `ap-LI2VGTAZjNrxqXGCFpBcS5` reconstructed the lifts with a
separate Tonelli-Shanks implementation, computed each common pair-equation
factor through `gcd(G,y^p-y)`, and removed every target-guard factor. It also
completed all 3,360 labels, with zero free branches and total guarded root
degree zero. A transient Modal heartbeat warning did not affect the remote
tasks or final complete output; the app stopped normally. The combined cost
was well below `$1`. This promotes the complete deployed rational-boundary
exclusion, but pays no point on the generic elliptic chart.

**Generic endpoint-role closure.** Source-only pilot app
`ap-gCH6oQc1fW2VTAZcNiuDon` adjoined the necessary endpoint equation
`(u^2+m)^2-Su^2=0` to the generic common curve. All eight source-sign and
endpoint cases became zero-dimensional with one exact `r` eliminant.
Deployed-root replay app `ap-wOtqklCmNfzcLPWGf9r6tS` lifted every linear
`r` factor through the proved tower and retained exactly 16 `BF` source
points and 24 `sigma_c CF` source points. No retained point lay on a route
or leading boundary.

The first full residual launch, `ap-utANE9kl0WA64d8VFvhZJj`, exposed only an
output-parser defect and produced no mathematical packet. After repair,
one-case validation app `ap-zdnEev7PHNSTrbRgZT8tua` paid 60 of 60 systems.
Primary app `ap-jrMESwKeGzouPFEPhqMscX` then completed all 32 source/endpoint
and target-lane shards: 2,400 of 2,400 guarded bivariate ideals were unit.
Independent app `ap-33sFbnRJM7VZHWz9dAKmVU` rebuilt the systems in SymPy and
computed unrestricted lex bases; all 2,400 were again unit, with zero
witnesses, target boundaries, finite residual branches, or unresolved rows.
Every app stopped normally. Aggregate cost was well below `$1`.

Together with the prior rational-boundary theorem, this promotes a scoped
PROVED node closing both endpoint roles in cell `12`: 30 labels, or 12 of
the 36 generic label orbits. The remaining generic workload is 24 orbit
representatives covering 75 labels. No complete-cell or Prize claim follows.

**Parallel-`DE` first-pair closure.** A direct eight-case Gröbner scout,
app `ap-ktQn2vT3AeMkBlys9jk7wS`, timed out during rational simplification;
a denominator-cleared, three-relation one-case retry,
`ap-PLvdEvwn66TRIQmwJ4xIii`, also reached the five-minute cap. Neither app
produced mathematical evidence. The retained four-basis formulation instead
completed a validation in `ap-wl1LaLm9HAbluHk5R5YR5h`, all rows in
`ap-mQsdrJxZ9czCBxKWyh4H2W`, and the final deterministic exact-coefficient
packet in `ap-IJFw7P0QEymI25xOtUvIER`. The two target-free cuts have norm degrees 350
and 362 and only eight and seven deployed roots per source-sign lane.

Final direct replay app `ap-g44ta4GmDCL8N8V1NUvI4B` accounted for all 116
case-labeled norm and inverse candidates. The negative-`DE` cut has no
generic zero; the positive-`DE` cut has two per source-sign lane. An initial
residual census and independent audit, apps `ap-0CVpkHNEHafBi9p0ZtE3MU`
and `ap-lZUhVykRbSdgKPG2YucyTD`, exposed a missing compiler equation: using
only `de=m` admits false projected witnesses. Restoring the mandatory Vieta
equation `(d+e)^2=S` makes every guarded residual ideal unit. Final primary
app `ap-OPmO1UlkaIs9vAkfUEA3Zl` and independent reduced-variable audit app
`ap-XtMGYHQ33046N1viWrJobe` agree on 96 of 96 unit systems, with no witness
or unresolved branch.

This closes nine labels, or four more generic orbits. The cell-12 frontier
is now 20 representatives covering 66 labels. The squared-sum omission is a
hard fence for every future missing-record compiler. Retained work cost was
below `$1`; the two failed direct scouts were bounded and are not to be
relaunched.

**Reciprocal-role matching-0 closure.** The already proved cell-4
reciprocal-square compiler is 1,139 lines, so it was not copied. A pinned AST
adapter extracts its `evaluate_case` function unchanged and supplies the
cell-12 tower through a six-slot schema shim. Initial app
`ap-uEmPUxl7Mnx1ZsXSP3RVfl` found one `FREE_B` terminal; exact evaluation
showed that it lies on the cell-12 `b`-leading complement. The adapter now
routes only coefficient-zero `FREE_B/FREE_C` terminals to the proved boundary
theorem. Validation app `ap-MPpJc7ic8DzACr3qnqtl33` then completed exactly.

Full app `ap-mMiXtJUDca1GdAHTkPorqD` completed all 24 source-sign, rational
`q`-branch, and `sigma_o` rows. A transparent container preemption was
retried by Modal and did not affect the complete packet. The exact census
contains 340 candidate roots, 472 guarded source points, 48 common `y` rows,
96 `(y,d)` candidates, and 192 final `sigma_c` lane evaluations. Every final
pair is nonzero; there are no witnesses or unresolved rows. An independent
local audit reconstructs all 89 unique norm/inverse finite-root sets and
checks every one of the 24 leading-boundary transports.

This closes missing `DF`, matching `0`, and its exact `D/E` partner: two
labels or one generic orbit. Cell `12` now has 19 representatives and 64
labels open. Total incremental Modal cost was well below `$1`.

**Reciprocal-role matchings-1/2 closure.** The same pinned-AST strategy
reuses the audited cell-4 reciprocal-linear compiler for cell `12`. The
missing Vieta quartic in `z=1/d` and the matching-specific quadratic have a
linear remainder in the exact four-basis algebra. One-row adapter validation
app `ap-VHGJqSCvU83mITBwKamC3h` completed before the complete 36-row run.

Full app `ap-fzs25UIEv1GTD1kKhPy0kG` covered all source signs, three rational
`q` branches, and the required matching anchors. The retained census has 244
target-norm roots, 620 total norm/inverse candidates, 1,040 guarded source
points, 80 common nonzero `z` candidates, and 192 final-lane evaluations.
All 36 rows are complete and every final value is nonzero. The 36 free-`b`
compiler exits evaluate exactly on the already-paid cell-12 leading
boundary; no other unresolved branch occurs.

An independent verifier reconstructs 125 unique finite-field polynomials,
all 576 profile visits, every candidate-root union and leading-boundary
transport, and all final lanes. This closes matchings `1` and `2` for missing
`DF` and their exact `D/E` partners: four labels or two generic orbits. Cell
`12` now has 17 representatives and 60 labels open. The run was bounded and
well below `$1`.

**Reciprocal-role matching-3/6 closure.** Matching `3` uses the colored
source pair to constrain `z=1/d`, followed by two target polynomials in
`q=de`. The pinned adapter reuses the audited cell-4 reciprocal-square and
sign-free compiler with the cell-12 tower. One-row validation app
`ap-8WEM4ndbuvRT6z3fZqW44E` completed before the full run.

Complete app `ap-gVXjM6KiAYRUMqc52sWMU7` covered all eight source-sign and
`sigma_c` rows. The retained packet has 68 target-norm roots, 120 total
norm/inverse candidates, 176 guarded source points, 40 common nonzero `z`
lifts, and 80 final `sigma_o` lanes. No final `q` candidate, witness, or
unresolved branch survives. Eight free-`b` exits evaluate on the proved
cell-12 leading boundary.

The independent verifier reconstructs 45 unique finite-field polynomials
and all 112 profile visits. It additionally rebuilds the source kernel at
every `z` lift and computes the two final `q` polynomials directly; all 80
gcds are constant. Duplicate-positive-`DE` exchange and exact outside `D/E`
transport close matching class `{3,6}` for both missing roles: four labels
or one generic orbit. Cell `12` now has 16 representatives and 56 labels
open. The bounded run cost well below `$1`.

**Reciprocal-role matching-4/9 closure.** Matching `4` requires the audited
nested sign-free reduction in `u=q^2`, `z=1/d`, and `y=z^2`. Initial
five-minute adapter probe `ap-KUjnRrPEPizCTHjRxOtxh1` timed out before the
resultant phase and is not evidence. Extended one-row app
`ap-8gPIxDrmfyKppQLrS3bNeF` completed in 398 seconds, justifying the four-row
parallel run.

Complete app `ap-bPXHMELqRWfL6mKQBLWGEF` finished in about 5.6 minutes wall
time. The exact packet has 32 target-norm roots, 72 total norm/inverse
candidates, 120 guarded source points, eight compatible `(z,q)` lifts, and
32 final target lanes. Every final pair is nonzero; four free-`b` exits lie
on the proved leading boundary, with no witness or unresolved branch.

Direct local reconstruction of all degree-up-to-5434 roots was intentionally
stopped after three minutes to preserve the host-compute policy. Independent
Modal app `ap-tXwZKeVrmXb8r4KclbW7hG` instead reconstructed 45 unique
profiles in parallel using SymPy/Galois tools. The fast local audit validates
all 64 profile visits and directly replays the kernel, Vieta relation, and
three paired equations at every lift. Exact transports close class `{4,9}`
for both missing roles: four labels or one generic orbit. Cell `12` now has
15 representatives and 52 labels open. Total cost remained well below `$1`.

**Reciprocal-role matching-5/12 closure.** The sibling nested sign-free
compiler fixes `sigma_c` inside its second pair, so eight source-sign/anchor
rows are required. With the measured matching-4 runtime, the full set was
launched directly under a 15-minute cap. Complete app
`ap-66X2RoJ3b0eWp3KHAleEXL` finished all rows; one preempted shard restarted
transparently.

The exact packet has 88 target-norm roots, 168 total norm/inverse candidates,
256 guarded source points, 16 compatible `(z,q)` lifts, and 32 final
`sigma_o` lanes. Every final pair is nonzero; eight free-`b` exits lie on the
proved leading boundary, with no witness or unresolved branch.

Independent root app `ap-anuKZnM08xltiExRoCP3DV` reconstructed all 45
degree-at-most-5388 profiles and 244 roots with the separate SymPy/Galois
implementation. Several inputs were preempted and automatically restarted;
the retained certificate is complete. The fast local audit validates all
128 profile visits and directly replays every equation at all 16 lifts.
Exact transports close class `{5,12}` for both missing roles: four labels or
one generic orbit. Cell `12` now has 14 representatives and 48 labels open.

**Reciprocal-role matching-7/10 closure.** This class uses a direct
quadratic-in-`q` resultant followed by the sign-free `z` reduction. One-row
validation app `ap-fcr4ueqVTji80aR1qmpdTD` completed in 144 seconds. Full
eight-row app `ap-AsoabwG2JvSRt8cgkWTAA1` then finished in under three
minutes wall time.

The exact packet has 56 target-norm roots, 112 total norm/inverse candidates,
160 guarded source points, 16 compatible `(z,q)` lifts, and 32 final
`sigma_o` lanes. Every final pair is nonzero; eight free-`b` exits lie on the
proved leading boundary, with no witness or unresolved branch.

Independent root app `ap-hiouIDHxqHvElOI6F3ZTLZ` reconstructed all 41
degree-at-most-4364 profiles and 192 roots. The fast local audit validates
all 112 profile visits and directly replays every equation at the 16 lifts.
Exact transports close class `{7,10}` for both missing roles: four labels or
one generic orbit. Cell `12` now has 13 representatives and 44 labels open.

**Reciprocal-role matching-8/13 closure.** This sign-swapped sibling uses the
same pinned quadratic-in-`q` resultant and sign-free `z` reduction. Complete
eight-row app `ap-R1zUSOfqjyRYFhIdmpwhaQ` covers every source-sign and
`sigma_c` row.

The exact packet has 56 target-norm roots, 112 total norm/inverse candidates,
160 guarded source points, 16 compatible `(z,q)` lifts, and 32 final
`sigma_o` lanes. Every final pair is nonzero; eight free-`b` exits lie on the
proved leading boundary, with no witness or unresolved branch.

Independent root app `ap-76MQUn2Qxxq9Mdkmz9zKJl` reconstructed all 41
degree-at-most-4364 profiles and 192 roots using a separate SymPy/Galois-tools
implementation. The fast local audit validates all 112 profile visits and
directly replays every equation at the 16 lifts with the matching-8 sign
placement. Exact transports close class `{8,13}` for both missing roles:
four labels or one generic orbit. Cell `12` now has 12 representatives and
40 labels open.

**Reciprocal-role matching-11/14 closure.** The final reciprocal class uses
the pinned quadratic-in-`q` resultant with `q` in both `BF/CF` pairs and
`-q` in the final `EF` pair. Complete eight-row app
`ap-nTsos4Qmbgwl8kZKnnxgf2` covers every source-sign and `sigma_c` row.

The exact packet has 60 target-norm roots, 108 total norm/inverse candidates,
136 guarded source points, 16 compatible `(z,q)` lifts, and 32 final
`sigma_o` lanes. Every final pair is nonzero; eight free-`b` exits lie on the
proved leading boundary, with no witness or unresolved branch.

Independent root app `ap-3rc86N9rjOcdikbsSFiFbn` reconstructed all 45
degree-at-most-4044 profiles and 220 roots using a separate SymPy/Galois-tools
implementation. The fast local audit validates all 112 profile visits and
directly replays every equation at the 16 lifts. Exact transports close
class `{11,14}` for both missing roles: four labels or one generic orbit.
All reciprocal-role labels are now paid; cell `12` retains 11 generic
representatives and 36 labels, all in the parallel-`DE` family.

**Parallel-DE pairing-3/6 closure.** The pinned nested-quadratic compiler
handles both direct representatives `xi=0` and `xi=2`. Pilot app
`ap-2iVXDzKzwYQCQDipBcT0Nn` completed one row in 49 seconds; complete app
`ap-m2bHGMiezmJOxXzIFQVN7M` finished all 32 source-sign/target-lane/`xi`
rows in about 72 seconds wall time.

The exact packet has 320 target-norm roots, 544 total norm/inverse
candidates, 752 guarded source points, 96 compatible `(u,v)` lifts, and 144
final `f` rows. Of these, 96 have a nonzero colored-pair cut and 48 have
`f=0`, hitting the explicit target boundary. There is no colored solution,
witness, or unresolved branch; 32 free-`b` exits lie on the proved leading
boundary.

Independent root app `ap-IW27Eb40wQbceojlxu9h8t` reconstructed all 49
degree-at-most-4216 profiles and 316 roots using separate SymPy/Galois tools.
Two preempted shards restarted transparently; the retained certificate is
complete. The local audit validates all 320 profile visits and directly
replays every first-pair quadratic, missing-sum equation, `f` lift, and final
colored pair. Exact transports close six labels in the two generic orbits
represented by `(0,3)` and `(2,3)`. Cell `12` now has nine representatives
and 30 labels open, all in the parallel-`DE` family.

**Parallel-DE pairing-4/7/9/10 closure.** The degree-eight sibling retains
`u=df` and `f` as the two variables. Its first two paired cuts are quadratic,
and its missing-sum condition is

```text
(u^2+eta*de*f^2)^2-S*f^2*u^2=0.
```

Pilot app `ap-KpOrM5LVlae8Q2sHw2KwKc` completed one row before full app
`ap-nSaTGMm4A5XeVgaDH7P2za` covered all 32 source-sign, target-lane, and
`xi in {0,2}` rows. One preempted primary shard restarted transparently. The
exact packet has 496 target-norm roots, 720 total norm/inverse candidates,
1,152 guarded source points, and 1,680 Cartesian `(u,f)` rows. Of these,
1,504 fail the missing relation, 128 have a nonzero colored-pair cut, and 48
hit the explicit `f=0` target boundary. There is no colored solution,
witness, or unresolved branch; 32 free-`b` exits lie on the proved leading
boundary.

External reconstruction app `ap-FhlAVavM8pW1fbbjGHMwpJ` covers all 37
degree-at-most-9,564 profiles and 252 roots by computing
`gcd(P,x^p-x)` and factoring its square-free linear part in FLINT. This is an
external custody and completeness check, not an independent-library root
algorithm. The bounded local audit independently evaluates every reported
root by sparse Horner replay and directly checks all paired quadratics,
missing relations, recovered variables, colored cuts, and boundaries. Exact
generic transport closes the eight labels in the two orbits represented by
`(0,4)` and `(2,4)`. Cell `12` now has seven representatives and 22 labels
open, all in the parallel-`DE` family. The retained campaign used bounded
parallel Modal jobs and was estimated in the low single-digit-dollar range.

**Parallel-DE pairing-5/8/12/13 closure.** The next degree-eight sibling
changes the second paired cut to `Pair(second_de,sigma_c*c*f)` and the
final colored cut to `Pair(sigma_o*v,b*f)`, while retaining

```text
(u^2+eta*de*f^2)^2-S*f^2*u^2=0.
```

Pilot app `ap-dhnwSn1GmmmAd1KD7Un06R` completed one row in 225 seconds.
Full app `ap-cLO3lWuVhVMVuRCGnPvcIi` then completed all 32 source-sign,
target-lane, and `xi in {0,2}` rows, with the slowest retained row reaching
the norm in 432 seconds. Transient client heartbeat warnings did not
interrupt the remote workers or the complete ordered result.

The exact packet has 448 target-norm roots, 672 total norm/inverse
candidates, 1,088 guarded source points, and 1,680 Cartesian `(u,f)` rows.
Of these, 1,472 fail the missing relation, 160 have a nonzero colored-pair
cut, and 48 hit the explicit `f=0` target boundary. There is no colored
solution, witness, or unresolved branch; 32 free-`b` exits lie on the
proved leading boundary.

External reconstruction app `ap-ZsSRVyTN3Jhzyt4viUa55b` covers all 37
degree-at-most-9,484 profiles and 240 roots with the compiled Frobenius/gcd
method. The local audit evaluates every reported root and directly checks
all paired quadratics, missing relations, recovered variables, colored cuts,
and boundaries. Exact generic transport closes the eight labels in the two
orbits represented by `(0,5)` and `(2,5)`. Cell `12` now has five
representatives and 14 labels open, all in the parallel-`DE` family.

**Positive-DE pairing-9/10 closure.** The retained positive omissions use
the degree-eight construction after exchanging the signed inputs:

```text
P_u(u)=Pair(-de,u),       P_f(f)=Pair(de,b*f).
```

Pilot app `ap-mMkjSAVuSKELxWNbD7SNwD` completed one row in 256 seconds.
Full app `ap-JGXYKD7wS4BWmagxL5VZEK` completed all 16 source-sign and
target-lane rows; the slowest retained row reached the norm in 391 seconds.
Transient client heartbeat warnings did not interrupt the complete result.

The exact packet has 224 target-norm roots, 336 total norm/inverse
candidates, 608 guarded source points, and 1,056 Cartesian `(u,f)` rows.
Of these, 992 fail the missing relation and all 64 survivors have a nonzero
colored-pair cut. There is no zero-`f` survivor, colored solution, witness,
or unresolved branch; 16 free-`b` exits lie on the proved leading boundary.

External reconstruction app `ap-9r303is5hkkfzCAeZVsvMJ` covers all 29
degree-at-most-9,294 profiles and 156 roots with the compiled Frobenius/gcd
method. The local audit evaluates every reported root and directly checks
all paired quadratics, missing relations, recovered variables, and colored
cuts. Exact positive-copy and matching transport closes
`{(0,9),(0,10),(1,9),(1,10)}`. Cell `12` now has four representatives
and ten labels open, all in the parallel-`DE` family.

**Positive-DE pairing-12/13 closure.** The second retained positive orbit
uses

```text
P_u(u)=Pair(-de,u),       P_f(f)=Pair(de,sigma_c*c*f).
```

Pilot app `ap-b0a2x2D6oRKaS0b9psYw2h` completed one row in 417 seconds.
Full app `ap-XdGOEs1KcCME9F0yBTjhR9` completed all 16 source-sign and
target-lane rows. Fifteen rows reached the eliminant in at most 122 seconds;
the slower sign row reached the norm in 418 seconds. Transient client
heartbeat warnings did not interrupt the complete ordered packet.

The exact packet has 240 target-norm roots, 352 total norm/inverse
candidates, 608 guarded source points, and 1,184 Cartesian `(u,f)` rows.
Of these, 1,088 fail the missing relation and all 96 survivors have a
nonzero colored-pair cut. There is no zero-`f` survivor, colored solution,
witness, or unresolved branch; 16 free-`b` exits lie on the proved leading
boundary.

External reconstruction app `ap-MvOBOt2watYIcoY87unfIV` covers all 29
degree-at-most-9,294 profiles and 160 roots with the compiled Frobenius/gcd
method. The local audit evaluates every reported root and directly checks
all paired quadratics, missing relations, recovered variables, and colored
cuts. Exact positive-copy and matching transport closes
`{(0,12),(0,13),(1,12),(1,13)}`. Cell `12` now has three representatives
and six labels open, all in the parallel-`DE` family.

**Parallel-DE pairing-11/14 closure.** The pinned common-`f` resultant
compiler was applied to cell 12 for `xi in {0,2}`, pairing 11. Pilot app
`ap-qhU3vIxx03uikcUop94SSi` excluded its row in about eight seconds of
algebra. Full app `ap-CYI7KjWXqvk5DnXzQlBPEi` completed all 32 ordered rows;
one preempted container restarted on the same input and the final packet is
complete.

The packet has 256 target roots, 464 total norm/inverse candidates, and 592
guarded source points. Direct replay classifies 96 points as
missing-impossible and 96 as zero-product boundary; the other 400 have no
compatible nonboundary quartic survivor. Exact duplicate and matching
transport closes `{(0,11),(1,11),(2,11),(2,14)}`.

**Positive-DE pairing-14 closure.** Pilot app
`ap-2FyH4kUBx9MJicqLGVwasG` excluded its row in about eight seconds. Full app
`ap-UrSRbKCPwD2vHbe07FCUcq` completed all 16 ordered rows. The packet has 120
target roots, 224 total norm/inverse candidates, and 304 guarded source
points. Of 64 compatible missing-quartic lifts, all 64 have nonzero colored
cut. Exact duplicate transport closes `{(0,14),(1,14)}`.

Shared external reconstruction app `ap-4MG5inRmcrsIbWpb0RpR86` covers all 57
distinct degree-at-most-1,224 profiles and 332 base-field roots by the
Frobenius/gcd method. The shared local audit evaluates every reported root,
replays all tower and missing equations, recomputes every quadratic and
quartic root set, and checks every colored cut. An exact 17-supplier
`30+9+36+30=105` label assembly now closes cell 12 completely.

**Cell-13 composition.** No new compute is required. The proved `B/C`
duplicate-role transport reruns its exact census of 20 common rows, four
target lanes, 420 lane/label maps, and 1,680 principal systems. Composing it
with complete cell-12 exclusion and the global rank-drop theorem closes role
orbit `[12,13]`. The remaining positive `433-1b` role orbits are `[5,8]`,
`[9,10]`, and `[11]`.

**Cell-9 global common curve.** A broad six-chart compact scout showed that
single-cofactor saturation is badly conditioned away from chart 1, so the
route was replaced rather than enlarged.  Modal app
`ap-XoLYM81yO2TrlOk6vbC2x2` completed chart 1 for all four source-sign rows:
each has dimension one, compact basis size 17, lex basis size 7, and empty
`AB` pivot boundary.  The inherited cell-4 three-relation presentation is
not exact.

Modal app `ap-9M4MIus4FHanMDnNWnCTNL` explicitly tested 120 generating
subsets.  In every sign row the full ideal is generated by each of
`{0,1,3,4,6}`, `{0,1,3,5,6}`, and `{0,1,4,5,6}`; every tested subset with
fewer than five elements fails.  The exactness flag is reconstructed from
all seven individual remainders, after catching an invalid preliminary
ideal-size diagnostic before it was banked.

Final app `ap-NEeUbdKCyo9j8gi6bgwYeR` saturates by the ideal generated by all
six product cofactors at once, rather than selecting one chart.  In all four
sign rows the global guarded rank-five ideal has dimension one and basis
sizes `17/7`, the primitive pivot boundary is unit after relocalization, and
both sets of seven mutual reductions between the global and chart-1 ideals
vanish.  Thus chart 1 is the complete global common curve.  This pays no
outside label; the next route is a global kernel and source-only outside
cuts before any matching-level census.

**Cell-9 global coefficient kernel.** Modal app
`ap-1gFa2n4GmRVFp3W7u8K69f` completed all four sign rows.  The primitive
kernel has coordinate degree/term shapes
`(14,38),(13,37),(11,38),(15,38),(15,37),(13,38),(15,66),(15,66)`.
Its first six coordinate digests agree in all sign rows.  The final two are
independent of the second sign and exchange when the first sign changes.
The five product pairings, `LA`, and the `AB` pivot vanish identically; all
ten pairings reduce to zero in the guarded global ideal, whose inverse-ring
basis size is 40.  This kernel is exact structural input only and pays no
outside label.  Pairing the seven outside records with it is the next
source-cut campaign.

**Cell-9 endpoint decomposition and exclusion.** Modal app
`ap-i4hLMM03qKEZAI74g2IoHC` computed the exact `BF` and `sigma_c CF`
compatibility schemes in all eight source-sign/endpoint rows.  Each scheme
has a five-polynomial triangular basis and exactly six deployed points.
Replay app `ap-nfsyyUV5Aor88EdzvONefh` separates four leading-open points
from two points on a shared section base locus.  The `b` and `c` base sets
agree sign by sign.

Modal app `ap-LwPNcB1VFD3eMUrHoQE1Ng` tested all four target lanes and 15
residual matchings at the 32 leading-open candidates.  All `1920/1920`
guarded ideals are unit.  The base points required a correction: the stored
polynomial kernel section evaluates to the zero vector there, so it cannot
be substituted as the pointwise kernel.  A failed pilot stopped on exactly
that condition before producing a claim.  The repaired compiler reconstructs
the ten common rows directly, proves rank seven, and obtains a unique
pointwise kernel with nonzero `A(-t^2)` at all eight distinct points.

Final app `ap-5AdOkV7s8XMpFQxWzAcvRF` tested every omitted outside role,
target lane, and residual matching at the regularized base points.  All
`3360/3360` systems are unit.  This closes the exceptional source stratum for
all roles and, together with the leading-open result, closes both endpoint
roles: 30 of the 105 raw cell-9 labels.  The remaining computation target is
the 75 leading-open labels in the other five roles, after deriving a
matching/label quotient and source-only cuts.  No further base-locus or
endpoint computation is requested.

**Universal outside-label quotient.** No remote compute is required.  The
two exact record involutions `(0 1)` and `(3 4)` preserve every positive
`433-1b` common role cell.  Deterministic enumeration partitions the 105
omitted-role/matching labels into 36 orbits with profile
`1:3,2:15,4:18`.  The endpoint subset is 12 orbits on 30 labels; its
invariant complement is 24 orbits on 75 labels with profile
`1:1,2:9,4:14`.  Full and complement orbit digests are respectively
`b5ec5e8418af3385dc83aeeb9aca9c8b851eae9e23794e6637f1b42a37576cb6`
and `c5c6f6b2e4af85cf2efd05fe106fa63a09bde9e6fa6ee07ed29a7f292f3b7353`.
For cell 9, future compute should run only these 24 representatives.

**Cell-9 parallel-DE first-pair closure.** Direct global-elimination pilots
`ap-JP8xUwOB2I8XLJaDNAFLaJ`, `ap-rluezptIAFnYDqdIBWBmhd`,
`ap-knDC5aS5HzEJonz5MtOkhb`, `ap-VtU26xmvKEU5wC9z7FohjT`,
`ap-wwIpM0PipwH43uVYavMt3L`, and `ap-Q0gQCcfpgLZ4GmbkEB4l0u` were stopped
without a claim after exposing the cost of global Gröbner/FGLM elimination.
They were replaced by a bounded four-basis route.

Tower pilot `ap-lI1X7nenqOpHLcyPodY99n` showed that no single leading chart
covers the curve.  Final cover app `ap-MSSmxHHKTONyeJo7CBevNz` proved the
two-by-three chart cover in all four source-sign rows: all 24 presentations
are exact, and the two `b` leading coefficients and three `c` leading
coefficients have empty simultaneous vanishing loci.

Norm pilot `ap-yFkxC4ErIsPRuq44KVDOc7` completed one degree-394 row.  Full
app `ap-fxkOE9P6jxLb1A0S3a1q4I` completed all 48 chart/sign/cut rows.  The
positive source norm has 11 deployed roots per sign and the negative norm
13; these root sets agree across all six charts.  Direct replay app
`ap-nDhmNjjP4BX2ANNLkSDcha` exposed a classification issue at `A=B=0` and
made no terminal claim.  Repaired replay app `ap-pdkwpojV89oRyV43buM0i4`
accounts for all 160 case-labeled norm/inverse roots, leaving four ordinary
positive and two ordinary negative cut zeros per source-sign row.  Its two
`A=B=0` points per row are exactly the already proved regularized base
points.

Target app `ap-sclQeuLHYymv3jFwSAbuaf` obtains the unit ideal in all 288
ordinary target systems.  Independent SymPy app
`ap-07EvSsJngQtZADRMed6JFq` eliminates the fixed `de` variable and again
obtains 288 unit ideals, with no finite fallback, witness, or unresolved
branch.  Universal transport closes four active representatives and nine
labels: the orbits represented by `(0,0)`, `(0,1)`, `(2,0)`, and `(2,1)`.
Cell 9 retains 20 representatives and 66 leading-open labels.

**Cell-9 pairing-11 common-`f` closure.** A pinned adapter applies the
audited pairing-11 common-`f` compiler to all six exact cell-9 tower charts.
Pilot app `ap-ZlkcJNvTofKAAaW9UyQwxN` completed one source-sign lane on all
six charts. Compact full scout `ap-lqie3UE9Ekhh7BMuDDr16k` and exact
sharded app `ap-llfwUbTao5pLC68j0Va8i6` then completed all 192 rows: four
source signs, four target lanes, two direct roles, and six charts. Every row
is excluded, with no witness, colored solution, or unresolved branch.

Independent root app `ap-iE2D95WiYBtId5Oh5dvQHe` reconstructed all 73
distinct norm/inverse profiles by FLINT Frobenius gcd. It found 364 deployed
roots, with maximum profile degree 1396. Independent six-chart replay app
`ap-bgDbh5uxC8E9US5Wxtqtkp` checked 2,496 source routes, 1,152 complete
quartic lifts, and 1,152 nonzero colored cuts. It also joined 192
`b`-leading and 384 `c`-leading exits to the proved tower boundaries and
384 missing-free exits to the proved regularized base systems.

Three audit-wrapper runs are retained only as diagnostics:
`ap-9UFYZP7CSTLtyo4fyEL1s0` failed at remote import because of a host-only
path expression, `ap-pI6kZZZM5xHREEDHL1L04G` reached the 300-second cap in
the monolithic replay, and `ap-1ooQ8MApl9YXVVpQQJUwK8` exposed a global-vs-
chart record-count assertion after the mathematical checks. None is cited
as evidence. The six independent 32-row chart jobs in the final app passed.

Universal transport closes the two active orbits represented by `(0,11)`
and `(2,11)`, namely four labels `(0,11),(1,11),(2,11),(2,14)`. Cell `9`
retains 18 representatives and 62 leading-open labels. Total retained
compute was bounded and well below `$1`.

**Cell-9 pairing-3 nested-quadratic closure.** Six-chart pilot app
`ap-QdiWgPfRBvZzLFN2vsH5JD` preserved the exact degree profile on every
chart: two quadratic paired cuts, a quartic missing-sum eliminant, and a
linear division-free pseudo-remainder. Full sharded app
`ap-QFMvBGEERf5oeUIRTAUxCX` completed all 192 source-sign, chart,
target-lane, and direct-role rows. Every row is excluded, with 960 paid
boundary records and no witness, unresolved branch, or colored solution.

Independent FLINT app `ap-Lm4DhyrU2udhJHjIkPXwII` reconstructed 69 distinct
norm/inverse profiles by Frobenius gcd, finding 360 deployed roots through
degree 4816. Independent six-chart replay app
`ap-hCLbES5z0O7sQq39C6gpYt` checked 2,784 source routes, all 4,352 Cartesian
`(u,v)` rows, 384 zero missing-sum pairs, 768 complete `f` lifts, and 768
nonzero colored cuts. It also joined 192 `b`-leading, 384 `c`-leading, and
384 regularized-base payments to their proved owners.

The full app printed a client asynchronous-generator close warning only
after writing all rows and the complete manifest. Independent verification
passes all six shard digests, 192 records, and 31,504,272 bytes. Universal
transport closes the two active pair-3/6 orbits: six labels represented by
`(0,3)` and `(2,3)`. Cell `9` retains 16 representatives and 56 labels.
Total retained compute was bounded and below `$1`.

**Cell-9 pairing-4 nested-quadratic closure.** Six-chart pilot app
`ap-REKIXZuusEbysA6NQEtBcY` completed its first six rows with no survivor.
Full sharded app `ap-WR056Dh1k0J8GvrO4jnQO8` then completed all 192
source-sign, chart, target-lane, and direct-role rows. Every row is excluded,
with 960 paid boundary records and no witness, unresolved branch, or colored
solution. The 69,213,912-byte primary ledger is split into six independently
verified shards.

Provider preemptions delayed one ordered row. Hedge app
`ap-dbFd4CtIQr2dd77MdUFCDH` independently completed that exact row, but the
hedge is not needed by the final packet because the original full app
completed all 192 rows. Independent FLINT app
`ap-uahZdq8BIufQlqW7Wd2RsG` reconstructed 61 distinct norm/inverse profiles
by Frobenius gcd, finding 308 deployed roots through degree 10,944.

The first direct-audit launch `ap-DakG3PbgZsqYnFcjU64kPF` failed before
arithmetic on a remote import-path expression and is retained only as a
diagnostic. Corrected six-chart app `ap-oIh1xPkupXQ3ZKXtBa9f0X` checked
4,032 source routes, all 7,040 Cartesian `(u,f)` rows, 960 zero-relation
lifts, and 960 nonzero colored cuts. It also joined 192 `b`-leading, 384
`c`-leading, and 384 regularized-base payments to their proved owners.

Universal transport closes the two pairing-4/7/9/10 orbits: eight labels
represented by `(0,4)` and `(2,4)`. Cell `9` retains 14 representatives and
48 labels. The next requested computation is the sibling pairing-5
compiler; its completion stream should be unordered and case-keyed so a
preempted row cannot block shard progress.

**Cell-9 pairing-5 nested-quadratic closure.** Six-chart pilot app
`ap-OzdO0AbBag4erxGQrr0ziK` completed all six pilot rows without a
survivor. Full unordered app `ap-W3vjE85wYdbr0lQoKcX3ND` flushed 189 of
192 complete rows before its Modal client terminated. The fail-closed
manifest remained incomplete. Exact recovery app
`ap-RezhzTvQc1VUSi1I3c8ech` recomputed only missing Cartesian indices
`175,176,177`; all three were complete and excluded. A checked key-join
merger rejected duplicates and nonterminal rows, required the exact
192-case cover, and rebuilt the primary ledger in canonical order. Its six
verified shards contain 68,182,568 bytes. Every row is excluded, with 960
paid boundary records and no witness, unresolved branch, or colored
solution.

Independent FLINT app `ap-dzdyzbeZvSleCpUZoFpk4N` reconstructed 61
distinct norm/inverse profiles by Frobenius gcd, finding 264 deployed roots
through degree 10,864. Independent six-chart replay app
`ap-gRTNcbJCYEsRcXXka5Vu3T` checked 3,072 source routes, 3,200 candidate
roots, 576 zero-relation lifts, and 576 nonzero colored cuts. It also joined
192 `b`-leading, 384 `c`-leading, and 384 regularized-base payments to their
proved owners; no colored solution or unowned boundary remains.

Universal transport closes the two pairing-5/8/12/13 orbits: eight labels
represented by `(0,5)` and `(2,5)`. Cell `9` retains 12 representatives and
40 labels. The next cheapest parallel-DE attack is positive pairing `9`.

**Cell-9 positive pairing-9 nested-quadratic closure.** Six-chart pilot app
`ap-i47DgQdgFkZ5oNy4cZn20L` completed all six chart rows with the exact
quadratic/quadratic/degree-eight/linear profile and no survivor. Full
unordered app `ap-GqdwWLInGrxmgVh6FLhQZ0` then completed all 96 source-sign,
chart, target-lane rows for positive direct role `xi=0`. Every row is
excluded, with 480 paid boundary records and no witness, unresolved branch,
or colored solution. The 33,746,580-byte primary ledger is split into three
independently verified shards.

Independent FLINT app `ap-2LXjDdvQOQAEDuJewBKVF3` reconstructed 53 distinct
norm/inverse profiles by Frobenius gcd, finding 208 deployed roots through
degree 10,674. Independent six-chart replay app
`ap-Yz5URg6VRTv3SRU0Mc5S1D` checked 1,728 source routes, 1,744 candidate
roots, 384 zero-relation lifts, and 384 nonzero colored cuts. It also joined
96 `b`-leading, 192 `c`-leading, and 192 regularized-base payments to their
proved owners. The audit directly implements matching
`((0,4),(1,2),(3,5))` and the pairing-9 target equations.

Universal transport closes the positive pairing-9/10 orbit: four labels
represented by `(0,9)`. Cell `9` retains 11 representatives and 36 labels.
The next cheapest parallel-DE attack is positive pairing `12`.

**Cell-9 positive pairing-12 nested-quadratic closure.** Six-chart pilot app
`ap-k30s4OoGHh4g8jlqgGO4r6` completed all six chart rows with the exact
quadratic/quadratic/degree-eight/linear profile and no survivor. Full
unordered app `ap-u10ZvqiLA7QkHDLM7jHSic` then completed all 96 source-sign,
chart, target-lane rows for positive direct role `xi=0`. Every row is
excluded, with 480 paid boundary records and no witness, unresolved branch,
or colored solution. The 33,716,536-byte primary ledger is split into three
independently verified shards.

Independent FLINT app `ap-QrImwY4BdQaLStAKu8kozT` reconstructed 53 distinct
norm/inverse profiles by Frobenius gcd, finding 208 deployed roots through
degree 10,674. Independent six-chart replay app
`ap-kAAEDFZU4AJ8OPyE5XAVkk` checked 1,728 source routes, 1,744 candidate
roots, 192 zero-relation lifts, and 192 nonzero colored cuts. It also joined
96 `b`-leading, 192 `c`-leading, and 192 regularized-base payments to their
proved owners. The audit directly implements matching
`((0,5),(1,2),(3,4))` and the pairing-12 target equations.

Universal transport closes the positive pairing-12/13 orbit: four labels
represented by `(0,12)`. Cell `9` retains 10 representatives and 32 labels.
The final parallel-DE representative is positive pairing `14`.

**Cell-9 positive pairing-14 common-f closure.** Six-chart pilot app
`ap-Wnf69ZTPtr4jWvfdm2Dr1G` completed all six rows in the
quadratic/quadratic/common-resultant profile with no survivor. Full
unordered app `ap-HCgP5AHlycUB1A9p6eyfDZ` then completed all 96 source-sign,
chart, target-lane rows for positive direct role `xi=0`. Every row is
excluded, with 480 paid boundary records and no witness, unresolved branch,
or colored solution. The 5,226,024-byte primary ledger is split into three
independently verified shards.

Independent FLINT app `ap-6Uje5hzKGnx3hlWLjej1cW` reconstructed 57 distinct
norm/inverse profiles by Frobenius gcd, finding 244 deployed roots through
degree 1,372. The first direct-audit app
`ap-bJwDmRKrRtgTZWdcO4isdr` failed before arithmetic on an exact metadata
string-order mismatch. Corrected app `ap-VdoQieJQotLgBLuhE8xTLr` checked
1,152 source routes, 1,600 candidate roots, 384 common-`f` quartic lifts,
and 384 nonzero colored cuts. It also joined 96 `b`-leading, 192
`c`-leading, and 192 regularized-base payments to their proved owners. The
audit directly implements matching `((0,5),(1,4),(2,3))` and the pairing-14
target equations.

Universal transport closes the positive pairing-14 orbit: two labels
represented by `(0,14)`. The parallel-DE family is exhausted. Cell `9`
retains nine representatives and 30 labels, all in the DF/EF family.

**Cell-9 reciprocal pairing-0 closure.** Six-chart pilot app
`ap-zkNt2Uw3wDeNhqgSrRfav7` completed all six rows in the exact
reciprocal-square profile with no survivor. Full unordered app
`ap-P1jZCZhqWA392qtZSo8z4s` then completed all 144 rows covering four
source signs, three exhaustive `q` branches, two `sigma_o` values, and six
charts. Each row checks both `sigma_c` colors. The 7,360,458-byte primary
ledger is split into five independently verified shards.

Independent FLINT app `ap-pwcV2I5u1g4UNdHJsoHzAc` reconstructed 113
distinct norm/inverse profiles by Frobenius gcd, finding 644 deployed roots
through degree 764. The first direct-audit app
`ap-2uD7sGWhewfpMupfwOzOqM` passed the arithmetic and failed only at final
aggregation on an obsolete count-field name. Corrected app
`ap-plWkGHPDxbdGycOjRvGrFu` checked 1,968 source routes, 2,424 candidate
roots, 288 common reciprocal-square roots, 576 complete `d/e/f` lifts, and
1,152 nonzero final colored cuts. It also joined 144 `b`-leading, 288
`c`-leading, and 288 regularized-base payments to their proved owners.

Universal transport closes the two-label orbit represented by `(3,0)`,
namely `{(3,0),(4,0)}`. Cell `9` retains eight representatives and 28
labels. The next canonical DF/EF representative is `(3,1)`.

**Cell-9 reciprocal-linear pairing-1 closure.** Six-chart pilot app
`ap-AwURhUNqbyqQ698VCisgnI` completed all six rows with a linear remainder
cut and no survivor. Full unordered app `ap-iWDncW0jIcza17OEMvVKJR` then
completed all 72 rows covering four source signs, three exhaustive `q`
branches, and six charts. Each row checks all four target colors. The
4,687,224-byte primary ledger is split into three independently verified
shards.

Independent FLINT app `ap-5jQKOBaFVW1E1cGYU7NLlq` reconstructed 121
distinct norm/inverse profiles by Frobenius gcd, finding 708 deployed roots
through degree 768. Independent app `ap-gr8JPiu2G8EADtQqPWbRuy` checked
1,296 source routes, 1,332 candidate roots, 144 common `z` roots, 144
complete `z/d/e/f` lifts, and 576 nonzero final colored cuts. It also joined
72 `b`-leading, 144 `c`-leading, and 144 regularized-base payments to their
proved owners.

Universal transport closes the two-label orbit represented by `(3,1)`,
namely `{(3,1),(4,1)}`. Cell `9` retains seven representatives and 26
labels. The next canonical DF/EF representative is `(3,2)`.

**Cell-9 reciprocal-linear pairing-2 closure.** Six-chart pilot app
`ap-w96YfyWkENePqJaMF2iO5T` completed all six rows with a linear remainder
cut and no survivor. Full unordered app `ap-Gj4xyIkqUpZbkQVpcpXz4j` then
completed all 144 rows covering four source signs, two anchor signs, three
exhaustive `q` branches, and six charts. Each row owns the anchor's two
target lanes. The 9,081,212-byte primary ledger is split into five
independently verified shards.

Independent FLINT app `ap-aMg0P5X4lwTv4iHnhsi0A9` reconstructed 121
distinct norm/inverse profiles by Frobenius gcd, finding 716 deployed roots
through degree 773. Independent app `ap-N9VKOuBESeRyu0BRwjcB2L` checked
2,304 source routes and 2,760 candidate roots. On all 1,584 ordinary routes,
the missing quartic and next-pair quadratic have no common reciprocal root,
so no `z/d/e/f` lift reaches a final colored cut. The audit also joined 144
`b`-leading, 288 `c`-leading, and 288 regularized-base payments to their
proved owners.

Universal transport closes the two-label orbit represented by `(3,2)`,
namely `{(3,2),(4,2)}`. Cell `9` retains six representatives and 24 labels.
The next canonical DF/EF representative is `(3,3)`.

**Cell-9 reciprocal-square pairing-3 closure.** Six-chart pilot app
`ap-SJlsfxUgYEzzlemUqv8nKr` closed all six rows. Full unordered app
`ap-1MlKMhkFELvgKYhCtdN8T9` then completed all 48 source-sign,
`sigma_c`, and chart rows, with 240 paid boundary records and no witness or
unresolved branch. The 3,385,114-byte primary ledger is split into two
independently verified shards.

Independent FLINT app `ap-ym5xoxlzFZtIvTrccBGyrX` reconstructed 69
norm/inverse profiles, 324 deployed roots, and degrees through 1,428.
Independent app `ap-X9Gs8vQB9ynZY3gWc5oLEB` checked 672 source routes,
896 candidate roots, 96 common reciprocal roots, and 192 final lane
records. Every antipodal/outside `q` intersection is empty. It also joins
48 `b`-leading, 96 `c`-leading, and 96 regularized-base payments to proved
owners.

Universal transport closes `{(3,3),(3,6),(4,3),(4,6)}`. Cell `9` retains
five representatives and 20 labels. The next canonical representative is
`(3,4)`.

**Cell-9 nested sign-free pairing-4 closure.** Six-chart pilot app
`ap-0eXYM1bIiL0jnkjwPGHPnF` closed all six rows. Full app
`ap-nGBMnIsNJk6A8qceTkMZ9Z` completed all 24 source-sign and chart rows,
with 120 paid boundary records and no witness or unresolved branch. The
5,680,636-byte primary ledger is one digest-pinned shard.

Independent FLINT app `ap-cjHiNPnu6Uv2B7iwUUoVqO` reconstructed 69
profiles, 320 deployed roots, and degrees through 6,282. Independent app
`ap-LcC9fgS0b9nGPORwGOCCWD` checked 384 source routes, 460 candidate roots,
and all 720 missing-quartic reciprocal lifts. Every antipodal/second-pair
`q` intersection is empty. It also joins 24 `b`-leading, 48 `c`-leading,
and 48 regularized-base payments to proved owners.

Universal transport closes `{(3,4),(3,9),(4,4),(4,9)}`. Cell `9` retains
four representatives and 16 labels. The next canonical representative is
`(3,5)`.

**Cell-9 nested sign-free pairing-5 closure.** The first adapter pilot
`ap-rbuHji3hWpAmAzq9OmUIu8` failed before algebra because the cell-4
template's `sigma_c` input had not been carried into the cell-9 cover.
Corrected pilot `ap-5GKTavHgRrUtGRaY1N7O6c` closed its row. Full app
`ap-hV2Vzlt0q1pWosIyPF2qLr` then completed all 48 source-sign,
`sigma_c`, and chart rows, with 240 paid boundary records and no witness
or unresolved branch. The 11,705,340-byte primary ledger is split into two
digest-pinned shards.

Independent FLINT app `ap-43r2bhsgMekpVKhtwyFdIk` reconstructed 69
profiles, 328 deployed roots, and degrees through 6,236. Independent app
`ap-M437a4BrpJZrRJd3mTlasc` checked 1,152 source routes, 1,016 candidate
roots, and all 2,976 missing-quartic reciprocal lifts. The
antipodal/second-pair intersections retain 288 common `q` roots; all 576
direct final target-lane cuts are nonzero. The audit also joins 48
`b`-leading, 96 `c`-leading, and 96 regularized-base payments to proved
owners.

Universal transport closes `{(3,5),(3,12),(4,5),(4,12)}`. Cell `9`
retains three representatives and 12 labels. The next canonical
representative is `(3,7)`.

**Cell-9 quadratic-resultant sign-free pairing-7 closure.** Pilot app
`ap-iOTxLlpbijYw7HfAgq5QMe` closed its row. Full app
`ap-JAQJTTMUz8Y6EAf1uPIZSD` then completed all 48 source-sign,
`sigma_c`, and chart rows, with 240 paid boundary records and no witness or
unresolved branch. The 9,244,692-byte primary ledger is split into two
digest-pinned shards.

Independent FLINT app `ap-yLcKreSx2UyRggOPA5TzgJ` reconstructed 65
profiles, 300 deployed roots, and degrees through 5,052. Independent app
`ap-eMFUeF0TBC7mEqzgRkBl2B` checked 816 source routes, 872 candidate
roots, and all 1,824 missing-quartic reciprocal lifts. The two quadratic
pair equations retain 240 common `q` roots; all 480 direct final target-lane
cuts are nonzero. The audit also joins 48 `b`-leading, 96 `c`-leading, and
96 regularized-base payments to proved owners.

Universal transport closes `{(3,7),(3,10),(4,7),(4,10)}`. Cell `9`
retains two representatives and eight labels. The next canonical
representative is `(3,8)`.

**Cell-9 quadratic-resultant sign-free pairing-8 closure.** Pairing 8
reverses the two inner `q` signs relative to pairing 7. Pilot app
`ap-YoIJpHmeajZbPglBqrWHD2` closed its row. Full app
`ap-FbTkYWrElchR6Mx8wdwgzF` then completed all 48 source-sign,
`sigma_c`, and chart rows, with 240 paid boundary records and no witness or
unresolved branch. The 9,244,084-byte primary ledger is split into two
digest-pinned shards.

Independent FLINT app `ap-6lGJT5DUhdaFddnBQUwyfv` reconstructed 65
profiles, 300 deployed roots, and degrees through 5,052. Independent app
`ap-rhbO91P4fvUFI2ydw58urn` checked 816 source routes, 872 candidate
roots, and all 1,824 missing-quartic reciprocal lifts under the reversed
sign convention. The two quadratic pair equations retain 240 common `q`
roots; all 480 direct final target-lane cuts are nonzero. The audit also
joins 48 `b`-leading, 96 `c`-leading, and 96 regularized-base payments to
proved owners.

Universal transport closes `{(3,8),(3,13),(4,8),(4,13)}`. Cell `9`
retains one representative and four labels. The final representative is
`(3,11)`.

**Cell-9 pairing-11 and aggregate complete closure.** Pilot app
`ap-I96pA8MQvOHjBP87iJhCbw` closed its row. Full app
`ap-qtPiSMxcBPP8wvd8SWP1jX` completed all 48 source-sign, `sigma_c`, and
chart rows after two preempted workers automatically replayed. The
8,454,588-byte primary ledger is split into two complete digest-pinned
shards, with 240 paid boundary records and no witness or unresolved branch.

Independent FLINT app `ap-5zqUz0RRUAmCDYIhf4PCcM` reconstructed 69
profiles, 312 deployed roots, and degrees through 4,732. Independent app
`ap-iI1IJQzMkge1LNCkkQi2b7` checked 672 source routes, 824 candidate
roots, and all 1,440 missing-quartic reciprocal lifts. The two quadratic
pair equations retain 144 common `q` roots; all 288 direct final target-lane
cuts are nonzero. The audit also joins 48 `b`-leading, 96 `c`-leading, and
96 regularized-base payments to proved owners.

Universal transport closes `{(3,11),(3,14),(4,11),(4,14)}`. A separate
executable composition checks that the 17 proved owner packets pay exactly
the router's 24 active orbits and 75 non-endpoint labels. Combined with the
30 endpoint labels, cell `9` is closed at 105/105. No further cell-9 compute
is requested; the exact packet should be exported through upstream PR #1152.

**Cell-3 upstream re-pin audit.** The advertised cell-3 `xi4` remainder was
already mathematically closed: the signed outside-role involution pays all
240 `xi4` systems, and the aggregate cell-3 theorem pays the common rank-drop
branch plus all 1,680 principal systems. Modal app
`ap-jYkVRdvSHQuofSrzIJzAG1` replayed the checked manifest prefix: 28 primary
verifiers and 28 independent audits all passed, with no timeout, hash
mismatch, or remote error. The canonical replay JSON has sha256
`2051784b7bff494045c7584c4bd491850725646f6a85b4619c005b1578774989`.
No new cell-3 computation is requested; package the public pin for PR #1152.

**Cell-5 common kernel and parallel-DE pairing-3/6 payment.** A bounded pivot
comparison (`ap-TazZVUDKUnb4W33eA12j4C`) selected cell `5` over cell `11`:
cell 5 had an exact compact quotient at all four pivots, while the tested
cell-11 quotient was nonexact throughout. Full cell-5 app
`ap-l9sLtKNA9myPWcxAq2cnTG` completed 24/24 sign/chart rows at pivot `1`.
Tower app `ap-5LwL71kEDRFiBhME2eZigW` found an exact recovery with both
leading boundaries unit, and kernel app `ap-V7eJJhNGmEeM7ZZcMrjmkx` found
one sign-independent common kernel with all 40 reductions zero.

Pairing-3 pilot `ap-RaHJBFQxB1e951pjNx0oQt` closed its row; full app
`ap-iHtf9zpPB2vLTkrdj7ipwH` closed all 32 rows with 496 candidate roots,
704 source-route points, 96 compatible lifts, and no witness or unresolved
exit. Independent app `ap-3GbNluq5oeArOZLXwAaKRn` reconstructed 53 profiles,
284 roots, and degrees through 3492. Exact transport pays six active labels
at pairings `3/6`; cell `5` retains 22 active orbits. No rerun is requested.

**Cell-5 parallel-DE pairing-4/7/9/10 payment.** Pairing-4 pilot
`ap-hr8ZV3Nn3WnqYhlclqiGod` closed its representative row, and full app
`ap-BLxgH4LYjVxTzCWUfBDCWn` closed all 32 rows with 560 candidate roots,
832 source-route points, 1,552 `(u,f)` rows, and no witness or unresolved
exit. Independent app `ap-uesgo05iEmKHKDVRYoNzlO` reconstructed 41 profiles,
200 field roots, and degrees through 7,848. Exact transport pays eight active
labels in two generic orbits, leaving 20 active cell-5 orbits. No rerun is
requested; the next bounded target is pairing `5`.

**Cell-5 parallel-DE pairing-5/8/12/13 payment.** Pairing-5 pilot
`ap-GouG45XwwpCLu2hkcDyCCG` closed its representative row, and full app
`ap-baEsdKRxUzIbKaN1v2gyaH` closed all 32 rows with 560 candidate roots,
864 source-route points, 1,424 `(u,f)` rows, and no witness or unresolved
exit. Independent app `ap-4mJWVSrvvA6XjKAEMgaPUn` reconstructed 41 profiles,
200 field roots, and degrees through 7,828. Exact transport pays eight active
labels in two generic orbits, leaving 18 active cell-5 orbits. No rerun is
requested; the next bounded target is pairing `9`.

**Cell-5 positive parallel-DE pairing-9/10 payment.** Pairing-9 pilot
`ap-WkEMrol1EtYM5mANO5hZ9x` closed its representative row, and full app
`ap-6cT9rObjVfDo12A6LtcYIw` closed all 16 rows with 336 candidate roots,
576 source-route points, 1,184 `(u,f)` rows, and no witness or unresolved
exit. Independent app `ap-XU03jH3lFC7PuisNoYlWZ7` reconstructed 33 profiles,
144 field roots, and degrees through 7,690. Exact transport pays four active
labels in one orbit, leaving 49 labels in 17 active cell-5 orbits. No rerun
is requested; select the next representative from the exact router.

**Cell-5 parallel-DE first-pair payment.** Four-basis norm app
`ap-JZOZS8657H8gFfCmYvdAOp` completed all eight source rows. Direct replay
app `ap-PC55fQq91WonxG2lM84EM4` exhausted 112 candidates: the opposite cut
has no ordinary zero and the equal-negative cut has eight in total, with no
unresolved branch. An initial residual pilot `ap-5kC67ZR4VQXfCi21tyFqvz`
failed closed because it retained the positive-role source-count assertion;
none of its output is used.

The corrected negative-role app `ap-kGgqzwqxGzFh1X8sE0rl8k` imposed
`de=-m` and `(d-e)^2=S` and obtained 96/96 Singular unit ideals. Independent
lex app `ap-VEb9bIRCgMd9aXMSMXuVba` independently obtained 96/96 unit ideals,
with no finite survivor, unresolved system, or witness. Exact transport pays
nine labels in four orbits, leaving 40 labels in 13 active cell-5 orbits. No
rerun is requested; the next bounded target is pairing `11`.

**Cell-5 parallel-DE pairing-11/14 payment.** Pilot app
`ap-Kncy0UoEXPfZEuPcriJhvF` closed its representative row. Full app
`ap-E5FgEIXjamRTpeiFPXIfR2` closed all 32 rows with 264 target roots, 464
candidates, 576 guarded source points, and no common-`f` lift, witness, or
unresolved branch. Independent app `ap-iBXSdbXdlFAm2iusD8UWzS` reconstructed
49 profiles, 236 deployed roots, and degrees through 992. Direct replay app
`ap-MpjO9DzT5FF3DHVml2tK2A` checked every candidate union and all 576 source
routes. Exact transport pays four labels in two orbits, leaving 36 labels in
11 active cell-5 orbits. No rerun is requested; the next bounded target is
positive pairing `12`.

**Cell-5 positive parallel-DE pairing-12/13 payment.** Pilot app
`ap-f9Tzml0vNhluFeiOXKo0cl` closed its row. Full app
`ap-ldOXXjHiD9UlMqtWtqi7lJ` closed all 16 rows with 304 candidates, 576
guarded source points, 1,056 `(u,f)` rows, and 96 nonzero final colored cuts.
Independent app `ap-hgwWbr7N2o5eXkPvOaAk1U` reconstructed 33 profiles, 124
deployed roots, and degrees through 7,702. Dedicated verifier replay
`ap-ykL1oFpfbx2Aed1wo1jdEr` checked all direct residuals and passed in 59.6
seconds. Exact transport pays four labels in one orbit, leaving 32 labels in
10 active cell-5 orbits. No rerun is requested; the next bounded target is
positive pairing `14`.

**Cell-5 positive parallel-DE pairing-14 payment.** Pilot app
`ap-oDZSc3atiWcEI9fkLqu6LJ` closed its row. Full app
`ap-Cft98d6QyKBakLyfWHA7Tq` closed all 16 rows with 96 target roots, 208
candidates, 240 guarded source points, 192 common-`f` lifts, and 192 nonzero
final colored cuts. Independent app `ap-NsAdkMWefu7DSfNmT6d2A1`
reconstructed 37 profiles, 136 deployed roots, and degrees through 984.
Dedicated direct replay `ap-PmAcydeJN9rw8vxgCXxipc` checked all 240 source
routes and all terminal classifications. Exact transport pays two labels in
one orbit, leaving 30 labels in 9 active cell-5 orbits. No rerun is requested;
the next bounded targets are the `xi=3` representatives at pairings
`0,1,2,3,4,5,7,8,11`.

**Cell-5 xi3 pairing-0 payment.** Pilot app
`ap-k0xagMKTLGhUToXTT5h1Xq` closed its row. Full app
`ap-M93N3JDUAYFLZANutbT0ZD` closed all 24 rows with 324 candidate roots,
416 guarded source routes, 160 reciprocal `(y,d)` candidates, and 320
nonzero final lanes. Independent app `ap-eMDAvbCs9CSGRO0xDZ7V9T`
reconstructed 93 profiles, 392 deployed roots, and degrees through 548.
Dedicated direct replay `ap-t8iRhYCgiuVirgmj3YBYtz` checked all route
relations and terminal ledgers. Exact transport pays two labels in one orbit,
leaving 28 labels in 8 active cell-5 orbits. No rerun is requested; the next
bounded packet is `xi=3` pairings `1/2`.

**Cell-5 xi3 pairings-1/2 payment.** Pilot app
`ap-FUqKOdbE21S1T8pUUJDxPB` closed its pairing-1 row. Full app
`ap-nmQOvYZaed4IjqgLRQJaS0` closed all 36 rows with 500 candidates, 712
guarded routes, 64 `z/d/e/f` lifts, and 224 nonzero final lanes. Independent
app `ap-oazobs3PP680DoKqwwUjCi` reconstructed 129 profiles, 596 deployed
roots, and degrees through 508. Dedicated direct replay
`ap-5RckhF73Lbvz3uGqKclZss` checked separate pairing-1 and pairing-2
ledgers. Exact transport pays four labels in two orbits, leaving 24 labels in
6 active cell-5 orbits. No rerun is requested; the next bounded family is
`xi=3` pairings `3/4/5`.

**Cell-5 xi3 pairings-3/4/5 payments.** Pairing-3 pilot
`ap-MPpRkT66xLx6Ds86ClR7ax` and full app
`ap-H0IIW2thzDFwlMIUs1N0Ig` closed all 8 rows with 88 candidates and 80
guarded routes. Pairing-4 pilot `ap-Ecx21odPCc08JkqkmHRaZb` and full app
`ap-XadN0KGQxn6OQnBbxLkk8c` closed all 4 rows with 80 candidates, 144
guarded routes, 24 compatible `q` lifts, and 96 nonzero final lanes.
Pairing-5 pilot `ap-Jdx1xl0uXWxWByUY2zolSb` and full app
`ap-5fFJNffd0PbaElqqI84YVS` closed all 8 rows with 128 candidates and 208
guarded routes.

Independent root app `ap-YDq3UwLeD4BRPYUnsWYE5t` wrote a complete packet
covering 69 profiles, 332 deployed roots, and degrees through 4560 before
the local Modal client was interrupted. Its retained sha256 is
`c4e2d14ca8bec16eaed65c40191fc70a1844bf086754c8a124118fa6b9f2f0c3`.
Dedicated direct replay `ap-yfMG7vQfVKsexBoGGb4Jxu` consumed that exact
packet and passed every pairing-separated ledger. Exact transport pays 12
labels in three orbits, leaving 12 labels in 3 active cell-5 orbits. No
rerun is requested; the next bounded family is `xi=3` pairings `7/8/11`.

**Cell-5 xi3 pairings-7/8/11 and active-label closure.** Pairing-7 pilot
`ap-JVAkbmNq1b4mAOKtYIt1dw` and full app
`ap-xlAamIanZVw5NgoF2jxw5W` closed all 8 rows with 100 candidates, 96
guarded routes, 8 compatible lifts, and 16 nonzero final lanes. Pairing-8
pilot `ap-W2bJPFYLwSp5SKtLSvBOQd` and full app
`ap-3ROjlQtUxKOPkuj5qd5Ayx` returned the same exact totals under its changed
source signs. Pairing-11 pilot `ap-a5Z8hUVMngFvtGJlwxC36x` and full app
`ap-P5jk6t0UaLcWiJ9blRRD3n` closed all 8 rows with 108 candidates, 120
guarded routes, 24 lifts, and 48 nonzero lanes.

Independent root apps `ap-sQjOrD7mWOSAen2kmmEl99`,
`ap-xqjrYDCvaZriiWWjg9sRQc`, and `ap-2DaEfR6hQbRZIVTQsAd5lG` each cover
45 profiles and respectively reconstruct 164, 164, and 172 deployed roots.
All three direct audits pass. Exact transport pays the final 12 active
labels in three four-label orbits. A separate zero-compute composition
checks that 16 proved owner packets pay exactly all 24 active orbits and all
75 labels with `xi <= 4`. No rerun is requested. The next bounded compute
target is the disjoint 30-label endpoint branch `xi in {5,6}`; it is not
claimed by the active-label aggregate.

**Cell-5 endpoint rootlessness and role-orbit `[5,8]` closure.** Exact
compatibility app `ap-eKyJeKljojhF7wqgT2WNhY` completed all eight
source-sign/endpoint ideals. Each has one univariate eliminant: degree 16 for
the four `b` rows and degree 11 for the four `c` rows. Replay app
`ap-cDjdfxWRQcs5eL4RgeKbQ3` found zero base-field roots, tower lifts, or
generic candidates in every row. Independent app
`ap-j1NvsU2Pzw7d8R5CrHhwYC` separately parsed the eliminants and certified
`gcd(E,r^p-r)=1` eight times. Thus all 30 endpoint labels close before any
target matching is introduced; the inherited 2,400-system residual census
was intentionally not launched.

Zero-compute exact compositions close cell 5 at `75+30=105` labels, verify
the B/C duplicate-role map over all 1,680 signed principal systems, and
close role orbit `[5,8]` using the proved rank-drop theorem. No rerun or
further compute is requested. Export the pinned closure certificate through
upstream PR #1152.
## Executed FPC5 Hankel/guard route probe

- **target:** `l1_fpc5_large_source_payment`
- **preregistration:** commit `468f04f1d`
- **canonical capture:** Modal app `ap-DlZD96lRzxt52OuV2msERv`
- **first run:** Modal app `ap-bXbMee2q6Gjl0eFBudI5Lo`
- **envelope:** 12 parallel workers, one CPU and 512 MB each, 60-second hard
  timeout and 54-second internal no-new-config deadline
- **completion:** 280/280 configurations and 504 fixed-background charts
- **result:** `NO_SEPARATION`; route evidence only

The rational FPC5 Hankel maxima were between `0.833` and `2.000` times the
matched random-Hankel maxima. Median untouched-petal guard survival was
between `0.917` and `1.000`. Neither preregistered alarm fired. The complete
emitted payload is pinned by SHA-256 in
`experiments/prize_resolution/fpc5_hankel_guard_probe_result.json`, and its
compact certificate has a deterministic checker with hostile mutations.

### Procedural limit

The v1 launcher returned completion counts but did not emit per-worker
elapsed times. Its conservative aggregate container ceiling is also twelve
minutes, although both parallel app runs completed in under one minute of
observed wall-clock time. It therefore remains non-load-bearing route
evidence under the strict compute rule and cannot support a `PROVED` status.
Do not rerun or enlarge it merely for audit completeness. A future theorem-
bearing campaign must preregister aggregate container-time accounting and a
full per-shard certificate before launch.
## K'=83 support-5/6 carrier-frontier diagnostic (INCOMPLETE)

- **target:** repair the claimed first wall at
  `rate_half_mca_rank11_k83_pairwise_atlas_triple_carrier_wall`
- **source start:** `714cd8458`; uncommitted experimental router and analytic
  theorem nodes were used after that pin
- **script:**
  `experiments/prize_resolution/rate_half_mca_rank11_k83_stratified56_lane_probe.py`
- **envelope:** one CPU and 1 GB per lane; measured peak RSS `60--61 MB`
- **status effect:** diagnostic only; no DAG promotion from this campaign

The first complete plain-frontier replay found two cells above the exact
premium ceiling `41364814251146263394918185689469529403097578120`:

```text
ordinary:       48823218479219528366674899867061323445817347365
  s2=44/s3=37/U23/s4=37/s5=37/c6F/c7F/c8F/c9F
carrier32:      47607497915597011275062723646851407786954935075
  s2=44/s3=43/s4=37/s5=37/c6F/c7F/c8F/c9F
```

The old offset-lane reruns completed lanes one through five. Lane one was
safe at `39633799344485339625076021189757227349617183809`. Lanes two
through five were unsafe only on cells deliberately left `plain` by the
K'=72-era implementation. Their maxima were respectively

```text
48783905667574087508920103887361714400981382257
48348402162021094645514147182990352368730621550
47912801724652164241916586247137000096365503413
47477104341394433057921308982733002380752506610.
```

The offset-six app timed out after 590 seconds and emitted no useful partial
certificate. The six old-lane apps in that launch wave were
`ap-QpukROdm56bYlGNaN50zKk`, `ap-oE2Y2Yks4BKveY5jEzw2fn`,
`ap-mHzkJ85vvxFSuNRik3YcHe`, `ap-j8ZR9KC0lmNegQziNNCEu6`,
`ap-byMLjB7ltmGiZYr6A8OAdT`, and `ap-FTO4glZYB671vfDc4JBmH2`.

The proof audit showed that these plain cells are covered by the already
proved full-completion pairwise-carrier atlas; the executable router had
only instantiated the subcases needed through K'=82. Corrected exploratory
apps `ap-2Y2o1UE58RDlmWcVzdCvnV`, `ap-0Ai6Bt9c5t4C8HCs7KwXbw`,
`ap-eLJZBZf17FWTVGjbDHtGrM`, `ap-X4Ln2LrAh3sev1ArEGT117`,
`ap-MIig66IDp5uszg7YiJsPA2`, `ap-ajWzfmdFDI28d1wsBvzsaq`, and
`ap-wIUyDQhqglQ3ZCHTA2u2eB` were all manually aborted when aggregate wall
time crossed the protocol limit. They emitted no retained result.

This campaign violated the intended preregistration order and did not have
resumable checkpoints. Do not cite it as a computational proof or rerun the
broad Cartesian product. A future replay must first Pareto-compress the
geometry signatures, emit deterministic per-lane checkpoints, and stop with
explicit `PASS`, `FAIL`, or `INCOMPLETE` output inside a five-minute aggregate
and `$1` campaign envelope. The analytic outputs that survive independently
are the adjacent-flat circuit coupling and its fixed-union support-5/6
corollary; both have proof-based node-local audits.

## Preregistered K'=83 threshold-pruned complete frontier replay

- **mathematical decision:** determine whether the proved pairwise-carrier
  atlas plus the proved fixed-union support-5/6 coupling closes the complete
  K'=83 rank-nine component frontier
- **lanes:** `ordinary`, `carrier32`, and exact offsets `1..6`; together these
  partition every support-2/3 position emitted by the proved finite router
- **primary:**
  `rate_half_mca_rank11_k83_threshold_frontier_replay.py`, SHA-256
  `e9cfef842bada08b53f1fb63d764f674b0f7a9374b5d8aff9f6c80ffad7847dd`
- **independent implementation:**
  `rate_half_mca_rank11_k83_threshold_frontier_audit.py`, SHA-256
  `2a196bcdca9c6155398df3bf7d0326b4461e394b8dd1a2294ab3c7cf3b0aff49`
- **formula source:** K'=83 stratified router SHA-256
  `069999aee001ee12cc0bfcaf2f8032594b4bef608163584ca06c452ae58e25d4`
- **dependency archive:** `/tmp/k72-deps.tar.gz`, SHA-256
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **code archive:** `/tmp/k83-threshold-frontier-code.tar.gz`, SHA-256
  `bcf3bfa31f91bdad88614f873e20ed27b4148dcc3f8597bf6b2e2c886db949f0`
- **runner:** `tools/modal_run_script_checkpointed.py`, SHA-256
  `8b387d5efaf7d4bfd434e98ac922324899bf8aa7d611ef4599757289eee07edf`

The threshold proof is exact: if the uncharged premium of one geometry unit
is already at most the ceiling, every fixed-union and joint charge can only
lower it, so the complete alternative product need not be expanded. Every
raw-unsafe unit is expanded through all exhaustive `T/A/F` alternatives.
Each lane flushes a complete checkpoint with source-unit, raw-row,
raw-safe-unit, expanded-unit, and geometry-row counts before the next lane.
The checkpointed runner returns these records even after a hard timeout.

Pilot: the nine diagnosed maximizers replay locally under RAMguard in 3.5
seconds at the previously measured 61 MB dependency footprint. Campaign
ceiling: two parallel one-CPU-equivalent/1 GB containers, 285-second child
hard stop, under five minutes observed wall and under `$1` conservative cost.

```text
PASS: primary and audit both cover 8/8 lanes, agree on the exact maximum,
      and place it at or below the ceiling; mint a K'=83 payment node.
FAIL: preserve the exact leading branch as the next analytic wall.
INCOMPLETE: retain complete lane checkpoints as evidence only; no promotion.
```

**Outcome:** `INCOMPLETE`. Primary app `ap-MoCjCkKzQdsFoaDpSgySte`
and independent app `ap-y3fYR39AKHhomN0R79gHTf` both reached the 285-second
child wall at 60 MB while processing the first combined ordinary lane. Each
returned only its `START` record, so no coverage or status claim is retained.
The failure is computational granularity, not mathematical evidence.

## Preregistered K'=83 offset-7 sharding pilot

The finite router decomposes the failed ordinary lane into a true plain
residue and offsets `7..36`. The revised primary SHA-256 is
`692218a499f84739a1e6ce671cadf184da279b53085431d7485989dffa82170d`;
the revised independent SHA-256 is
`e10ac6915fdf611d0703cbf6d1c57c71e7e9e1b14177cd1bb62b5a856c274a23`;
and the code archive `/tmp/k83-threshold-frontier-sharded-code.tar.gz` has
SHA-256 `6bfaf2ac8292645e39f50d4f0b2dbfb20266d477667aee423f87c084b3f1dc56`.
All other pinned sources and the checkpointed runner are unchanged.

Pilot exactly one lane, `offset7`, in primary and independent containers.
This lane has 32 support-2/3 source rows and 5,476 exact support-4/5 rows.
Both implementations flush progress every 1,000 source units and a complete
coverage record on success. Hard wall remains 285 seconds per child; campaign
wall is five minutes and conservative cost is below `$0.05`.

```text
PASS: exact maxima and coverage counts agree; use measured expansion and wall
      time to authorize or reject the 38-lane parallel campaign.
FAIL: retain the exact offset-7 wall.
INCOMPLETE: use progress counts to redesign the per-unit geometry optimizer;
            do not launch the 38-lane campaign.
```

**Pilot outcome:** `PASS`. Primary app `ap-jmgm9FhgNcjwq96l2zR3gJ`
and independent app `ap-l9ISWe18boAySpaly1diZi` agree on:

```text
source units:       175232
raw rows:           1226624
raw-safe units:     167536
expanded units:       7696
maximum: 41364700171905693710376221140276840019247232410
margin:     114079240569684541964549192689383850345710
active:  s2=47/s3=40/s4=32/s5=47/c6F/c7F/c8F/c9F/raw-safe
```

Primary deduplication evaluated 3,898,321 geometry rows; the independent
all-label implementation evaluated 3,945,508. Both returned the same exact
maximum. Peak RSS was 60 MB and observed wall was well below two minutes.

## Authorized K'=83 38-lane parallel completion wave

Launch primary and independent containers for each disjoint lane

```text
ordinary, carrier32, offset1, ..., offset36.
```

The 76-container peak is below the account limit of 100. Every child has the
same 285-second hard wall and periodic checkpoints as the pilot. Using the
offset-7 measured work as a conservative per-lane upper for the smaller
offsets and the published Modal CPU/memory unit scale, projected total cost
is below `$1`; observed campaign wall remains below five minutes because the
lanes run in parallel. Source hashes, archive hashes, theorem versions, and
PASS/FAIL/INCOMPLETE effects are exactly those of the offset-7 pilot.

To protect WSL RAM, the wave uses one local Modal client and remote
`starmap`, not 76 resident local clients. The batch runner is
`tools/modal_run_script_checkpointed_batch.py`, SHA-256
`9ca25d723d6ec0d616e334cc3fbd7354a0ef0752b1986f331e655dea5db59043`.
It allocates one CPU and 1 GB per remote child, returns each child's flushed
stdout independently, and emits a final expected/completed/failures ledger.

The wave is proof-usable only if all 38 primary lanes and all 38 independent
lanes complete, lane maxima agree pairwise, and the global maximum is at most
the exact ceiling. Any missing or disagreeing lane makes the wave
`INCOMPLETE`; no partial prefix promotes K'=83.

**Wave outcome:** `INCOMPLETE`, with exact route information. Batch app
`ap-FCVIzeLq0GH1yjqXU9SPha` completed all 76 jobs at 58--60 MB. Exactly two
jobs returned mathematical `FAIL`, namely primary and audit `ordinary`; no
job timed out. The other 37 lane pairs returned `PASS`. Raw batch SHA-256 is
`87bbe929745cd26acfe445bade74517325d79befe99b97da10ac08cdbbf84922`.

Both implementations agree on the ordinary wall:

```text
defects:  (73,37,37,37)
maxima:   (0,36,36,36)
high:     c6d3/c7d2/c8d1/c9d0
premium:  46067025990627744112258469425635158852400659940
deficit:   4702211739481480717340283736165629449303081820
```

The cell has an unconditional support-three completion carrier of size 38
and eight-dimensional annihilator. A focused exact replay applies that
`(38,8)` fixed-union charge plus the proved support-4/5 and support-5/6
couplings and obtains premium
`34180322136602231166354248419499424949751610015`, safely below the ceiling
by `7184492114544032228563937269970104453345968105`.

The same audit found a second completeness issue: pre-charge Pareto
compression of support-2/3 vectors cannot preserve offset-dependent carrier
provenance. Therefore the former lanes through offset 36 are evidence only.
The corrected exact partition is one ordinary lane plus offsets `1..72`,
with every exact defect pair retained before geometry.

## Preregistered exact-router repair pilot

- **primary SHA-256:**
  `bd55cb64beff7a2acc119030fed42968c8b251247131213cdc15d446aa5b7f55`
- **independent SHA-256:**
  `7022c625a3039b2aae96306e69ea1c1c09416a5498081978667ce5ea12c0868f`
- **code archive:** `/tmp/k83-threshold-frontier-exact-code.tar.gz`, SHA-256
  `f7af236d6886d1ad7681bd39e72306b3c25a91d26e6b1d3f54c8c0937bc979ac`
- **pilot lanes:** repaired `ordinary` and exact `offset7`, primary plus audit

The repaired ordinary router retains every positive single support-two or
support-three carrier before Pareto compression, while positive
`M3-M2=offset` rows are partitioned exactly for all offsets `1..72`.
The four pilot children use one CPU, 1 GB, periodic checkpoints, and the
285-second hard wall. Conservative campaign cost is below `$0.10`.

```text
PASS: both implementations agree and both lanes are safe; authorize two
      <=66-container exact-offset waves for offsets 1..72.
FAIL: retain the exact repaired wall.
INCOMPLETE: refine the failing lane only; no broad rerun.
```

**Pilot outcome:** `FAIL`, with a narrower exact wall. Modal batch app
`ap-IyNq9TiXnzgFvRFLmwRYqB` completed all four jobs at 57--60 MB without a
timeout. Primary and audit agree that exact offset 7 is safe, but the repaired
ordinary lane has

```text
defects:  (55,55,37,37)
maxima:   (18,18,36,36)
high:     c6F/c7F/c8F/c9F
premium:  44127003119745923941522954461412336564614624900
deficit:   2762188868599660546604768771942807161517046780
```

The broad exact-offset waves remain unauthorized until this cell is paid.

## Preregistered K'=83 adjacent-high fixed-union probe

The ordinary wall already has exhaustive support-2/3 alternatives
`T23=(u,g)=(39,7)` and `A23=(38,8)`. The generic adjacent-flat circuit
coupling applies not only to supports 5/6 but to every adjacent support pair
`d/(d+1)` with `g>=d+1`. The targeted script evaluates the exact wall under
all disjoint matchings of the available pairs `4/5,5/6,6/7,7/8`; overlapping
pairs are never charged simultaneously.

- **script:**
  `experiments/prize_resolution/rate_half_mca_rank11_k83_adjacent_high_support_probe.py`
- **scope:** one container, one CPU, 1 GB, 285-second child wall
- **expected cost:** below `$0.01`

```text
SAFE: both exhaustive T23/A23 alternatives are below the ceiling; generalize
      the adjacent-support fixed-union theorem and repair the exact router.
WALL: at least one exhaustive alternative remains unpaid; preserve it as the
      next analytic wall.
INCOMPLETE: retain no mathematical conclusion.
```

**Outcome:** `SAFE`. Modal app `ap-ltflETo1CTk9D8ndmZOGnD` used 63 MB and
returned in under one minute. The script SHA-256 is
`999c5a815285d4e989b4a176ec332526d9e266208e4e11fd91f5a10a76c892c3`.
Both routes select the support-disjoint pairs 4/5 and 6/7:

```text
T23 (39,7): premium 28580257237466146031071834658493035776688499195
             margin 12784557013680117363846351030976493626409078925
A23 (38,8): premium 28138384063262743811603676163266039013680815843
             margin 13226430187883519583314509526203490389416762277
```

## Preregistered adjacent-router exact pilot

The generic theorem has now been minted as
`rate_half_mca_sparse_circuit_fixed_union_adjacent_support_coupling`. The
primary and independent routers retain fixed-union provenance through
Pareto compression and optimize only over support-disjoint adjacent pairs.

- **primary SHA-256:**
  `1c19b328e667feb49b44c6e70744a37237c3a0dae8f09e55595108f31e9bf9b7`
- **independent SHA-256:**
  `77dabfcfa552f7a1c5939f110b5142742bacd5df3c71947b1d8090030b24a7bf`
- **archive:** `/tmp/k83-threshold-frontier-adjacent-code.tar.gz`, SHA-256
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **lanes:** exact `ordinary` and `offset7`, primary plus audit
- **envelope:** four one-CPU, 1 GB containers; 285-second child wall; below
  `$0.10` conservative cost

```text
PASS: both implementations agree on complete safe lanes; authorize the two
      exact offset waves.
FAIL: preserve the exact maximizing branch as the next analytic wall.
INCOMPLETE: reduce computational granularity without making a coverage claim.
```

**Outcome:** `PASS`. Batch app `ap-Qr5dCpKMRHiLusDi0QczQU` completed all
four jobs at 63 MB without timeout. The raw output SHA-256 is
`73d8348274b25911e7d0b13a404b2adb57ff24d022043be1b7d6ebed7548cb25`.
Primary and audit agree exactly:

```text
ordinary:  maximum 41363991498791696492883838631369698521229319916
           margin      822752354566902034347058099830881868258204
offset 7:  maximum 41364734718541076704831964436177797049983165655
           margin       79532605186690086221253291732353114412465
```

## Authorized adjacent-router exact offset waves

The remaining exact partition is offsets `1..72`. Run primary and audit for
offsets `1..36` in wave A and `37..72` in wave B. Each wave has 72 containers,
below the account limit of 100. Source, archive, dependency, runner, memory,
and timeout hashes are exactly those of the passing adjacent-router pilot.
The duplicated offset-7 pilot is intentionally rerun inside wave A so each
wave output is a self-contained interval certificate.

Conservative cost remains below `$1` across both waves based on the measured
pilot. A wave is proof-usable only if all 72 jobs complete, every primary and
audit lane pair agrees on coverage, maximum, and margin, and every margin is
positive. Any missing lane makes the K'=83 payment `INCOMPLETE`.

**Wave-A checkpoint:** the local Modal client was mistakenly launched under
RAMguard's five-minute `local` profile. It returned 64/72 remote checkpoints
before the local wall: all 36 primary lanes and 27 audit lanes were safe;
`audit:offset19` alone reached the 285-second child wall after 265,000 of
295,704 units, and audit offsets 20--28 were not returned. The partial output
SHA-256 is `dc2e285843645a3d5f0fa3e96dd2bab0a7b63ceffcf790db025405546dcf69f0`.
These complete per-lane checkpoints remain proof-usable after a successful
repair supplies every missing lane.

## Authorized wave-A audit repair

Rerun only audit offsets `19..28`. The mathematical source and archive are
unchanged. The batch runner now accepts one audit implementation, gives each
remote child a 645-second hard wall, and is itself launched under RAMguard's
12-hour `modal` profile. Its SHA-256 is
`bbe9f1100d8d6add611794e24e02d57ab0f57903a15195a944e6fe640ca98922`.
The ten-container repair remains below `$0.20` conservative cost. The longer
wall changes no theorem or search space; periodic checkpoints and the 1 GB
memory cap remain unchanged.

**Wave-B outcome:** `PASS`. Batch app `ap-cEUnaW2ssU1ObLbSSllkVv`
completed all 72 primary/audit jobs for offsets 37--72 without failure or
timeout. The raw output SHA-256 is
`e7714f76c755f4908c56bd55c551e2e0c6e39d025b00dad997fa81e9e36bb3e6`.
Its maximum occurs at offset 37:

```text
premium: 41347932347360629348777920971056540502170790055
margin:     16881903785634046140264718412988900926788065
```

**Wave-A repair outcome:** `PASS`. Batch app
`ap-DTDRrKPV8NvHxqZC4Q9ULg` completed all ten audit offsets 19--28 under
the extended wall with no failure or timeout. The raw output SHA-256 is
`b4adf54a2d0f776a40cd8698f1950be1875b9f709a581cabd85ab17b5e50930b`.

**Exact merger outcome:** `PASS`. The compact checker consumed the pilot,
partial wave A, wave-A repair, and wave B. It found all 146 required jobs
covering exactly `ordinary + offsets 1..72`; all primary/audit coverage keys
and maxima agree and all margins are positive. Its final certificate is

```text
lanes:                 73
jobs:                 146
global lane:          offset2
global maximum:       41364793335621487128860475977676014245181683050
minimum margin:           20915524776266057709711793515157915895070
primary geometry rows: 203167790
audit geometry rows:   393886640
```

The checker SHA-256 is
`c694c40dff948cff07d3fe8a0775047ae09ae2517063a2b654dc2a1cd713ad44`.
This authorizes a `PROVED` K'=83 payment node; no later row is claimed.
## Preregistered K'=84 adjacent-support route pilot

- **decision:** determine whether the first new row already breaks the
  proved K'=83 adjacent-support router, and identify the exact first
  obstruction if it does
- **scope:** `ordinary`, exact offsets `1`, `2`, `7`, and the new terminal
  offset `73`, in both primary and independent implementations
- **primary wrapper SHA-256:**
  `a3f55cf0627f63b9786d3f44f526bb44c62d223152424099f1039df04d272a20`
- **audit wrapper SHA-256:**
  `a9a323316bcbef966ad97ca3e24f66220aa41baf8d5115e7ca3f3205e3e37249`
- **hash-pinned K'=83 code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **batch runner SHA-256:**
  `bbe9f1100d8d6add611794e24e02d57ab0f57903a15195a944e6fe640ca98922`
- **envelope:** ten remote containers, one CPU and 1 GB each, 645-second
  child wall; projected cost below `$0.20`
- **local safety:** one RAM-guarded Modal client; no local enumeration

The wrappers change only the row parameters to `K'=84`, `q=74`,
`m'=67556`, and `n'=1048660`. The theorem and router sources imported by
the wrappers are the unchanged hash-pinned K'=83 implementations. The five
lanes are route-locating, not an exhaustive row certificate.

```text
PASS:       both implementations agree and all five lanes are safe;
            analyze the active templates symbolically before authorizing
            any remaining-lane wave
FAIL:       both implementations agree on an unsafe lane; retain its exact
            branch as the next analytic wall and do not launch broadly
INCOMPLETE: any timeout, missing lane, or implementation disagreement;
            retain no mathematical conclusion
```

No outcome of this pilot promotes `K'=84` or changes a DAG status.

**Outcome:** `PASS` as a route-locating pilot, with no row promotion.
Modal app `ap-Srv9CDnQL721xYGzAUZoR6` completed all ten jobs without a
timeout at 58--62 MB peak RSS. The raw capture SHA-256 is
`4024f6ad84c050540bfa3c32088e4768a3ca5abf798f95bc8624d054178f9ff4`.
Primary and audit agree exactly on every maximum:

```text
ordinary:  41388798786059119503097492734939028640066114130
           margin 44581160171407926086602515730765812413619
offset 1:  41388509655129434578015936172698056050247199551
           margin 333712089856333007643164756703355631328198
offset 2:  41387937303860893532474667943101838831996305858
           margin 906063358397378548911394352920573882221891
offset 7:  41388695386454290912259500164616925968496091874
           margin 147980764999998764079172837833437382435875
offset 73:   207313827489437078117773167012308731551794440
           margin 41181529539729853832905806170442450674326733309
```

The new leading branch is

```text
s2=74/s3=55/s4=45/s5=37/ordinary-single/
c6d3/c7d2/c8d1/c9d0/raw-safe.
```

Thus the adjacent-support router has not failed at the first new row, but
the maximizer changed from K'=83's offset-two/full-fallback template to an
ordinary single-support-three template. Analyze this branch and the
unsampled-offset domination problem symbolically before any full K'=84
wave.

## Preregistered one-sided raw-template scan

- **decision:** determine whether the new ordinary one-sided support-2/3
  envelope has a short stable family of active defect templates, and
  whether its exact ceiling margin crosses near the K'=84 frontier
- **interval:** every integer `K'=83..128`
- **script SHA-256:**
  `7946d6aa8174768494322aaae67b2472f351dd42fc2d9e82d07c698a23de84f1`
- **scope:** exact raw maximum over both one-sided branches, all
  support-4/5 Pareto vectors, and all support-6/9 Pareto vectors
- **envelope:** one remote CPU, 1 GB, 645-second wall; projected cost below
  `$0.02`

```text
CROSS:      report the first negative margin as the next raw analytic wall
STABLE:     extract the finitely many active affine defect templates and
            prove their binomial/floor margins on maximal intervals
PROLIFERATE: stop the scan route if active templates do not compress;
             do not replace proof by longer row enumeration
INCOMPLETE: retain no conclusion after timeout or malformed output
```

This scan ignores geometry-required cells and cannot close any row.

**Outcome:** `INCOMPLETE`, and the scan exposed a wrong endpoint rather
than a ceiling crossing. Modal app `ap-Rzy1Aw2D71418NHszc7XLf` reached its
645-second child wall at 61 MB peak RSS after printing complete rows
`K'=83..105`; the raw capture SHA-256 is
`20add11719a44044c14fe93d44a31ee3cc6068b6fac1e351b9a9fe9cf2a09787`.
All 23 completed rows have the same parity family

```text
source=3,
M3=floor(q/2),
s2=q,
s3=s4=s5=ceil(q/2),
c6d2/c7d1/c8d1/c9d0.
```

Its *raw* premium already exceeds the ceiling at `K'=83`; for example at
`K'=84` it is
`46986000759234275253755854037693521002636288520`, with margin
`-5597157392014984342732274700238761596757760771`. This is not a
counterexample to the adjacent-support route. The family lies in the
geometry-required support-three cell, where the theorem mandates the
single-completion carrier `(u,g)=(M3+2,8)`. The scan omitted exactly that
charge. Consequently no first-crossing or interval-stability conclusion is
retained, and extending this raw scan would test the wrong quantity.

The useful route information is the compressed parity family itself. The
next preregistered object must be its **post-charge** adjacent-support
premium, compared with the raw-safe ordinary leader and the other charged
families. A row or interval can be promoted only after that charged envelope
is bounded analytically and independently replayed.

## Preregistered support-three post-charge parity evaluation

- **decision:** identify the active adjacent-pair charge and exact margin of
  the isolated parity family after its mandatory single-completion carrier
- **interval:** every integer `K'=83..128`; this is 46 evaluations of one
  explicit template, not a frontier enumeration
- **script SHA-256:**
  `74f621ef2c8609c0a296d999a5a161fbad0811c3bfa5fcb3f11d3f5ec9e9c9e2`
- **template:** `q=K'-10`, `M3=floor(q/2)`,
  `s2=q`, `s3=s4=s5=ceil(q/2)`, high branch
  `c6d2/c7d1/c8d1/c9d0`, carrier `(M3+2,8)`
- **envelope:** one remote CPU, 1 GB, 120-second child wall; projected cost
  below `$0.01`

```text
STABLE:     one adjacent-charge choice per parity; extract and prove the
            corresponding exact floor/binomial inequalities
SWITCH:     finitely many charge changes; split the symbolic interval there
UNSAFE:     a negative post-charge margin is a genuine route obstruction
INCOMPLETE: retain no mathematical conclusion
```

This evaluation can reject or simplify the proposed symbolic route. It
cannot establish domination over the remaining K'=84 lane families and
cannot promote a row by itself.

Two setup-only launches preceded the hash above. App
`ap-QTHBoe6Q240zH2Vm65f0TS` used a stale dependency archive and failed
before its first row because that archive predates the all-adjacent router.
App `ap-tlQ731qAm1fuxQFA3G8VZ6` used the correct archive but timed out after
270 seconds because the script enumerated complete support-4/5 and
support-6/9 Pareto frontiers merely to retrieve named vectors; the generic
runner buffered stdout, so it returned no partial rows. Neither launch
produced mathematical evidence. The hash-pinned revision constructs those
same named vectors directly from `exact_cross_caps` and `source_options`.

**Outcome:** `SWITCH`, with a stable pricing choice and a genuine later
route obstruction. App `ap-rhsmO9Z7XoNV3I6u1ihRay` completed all 46 rows at
59 MB peak RSS. The raw capture SHA-256 is
`61a0884cc7d996512e6576c303b3746213db0c66122dce5cf29c28c94f665214`.
Every row selects the disjoint adjacent-pair charge `A45+A67`.

At the target row `K'=84`, the post-charge premium is
`30754765486431054133282031534055508984798589537`, safely below the exact
ceiling by `10634077880788236777741547803399250421079938212`. Thus the raw
support-three parity wall isolated above is not the K'=84 obstruction. The
same formula remains safe through `K'=110`, then first fails at `K'=111`
for odd `q` and `K'=112` for even `q`:

```text
K'=109: margin  509212654944121696349789160479105006945656208
K'=110: margin  296412497742911062432803390572960247010652784
K'=111: margin -289287180359720419070152831788781417392816816
K'=112: margin -502245759142497481996161240413431098141610146
```

The crossing limits this particular carrier formula; it does not falsify
the row theorem or affect K'=84. For K'=84 the full pilot's raw-safe
ordinary leader remains much larger than this charged family. The immediate
analytic task is therefore to prove the `A45+A67` reduction for the parity
cell and then establish domination over all other K'=84 ordinary and offset
families, without extending this formula past its observed crossing.

## Authorized K'=84 primary route-location wave

- **decision:** find the exact maximum and any unsafe lane among the complete
  partition `ordinary, offset1, ..., offset73`
- **primary wrapper SHA-256:**
  `a3f55cf0627f63b9786d3f44f526bb44c62d223152424099f1039df04d272a20`
- **hash-pinned K'=83 code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **batch runner SHA-256:**
  `bbe9f1100d8d6add611794e24e02d57ab0f57903a15195a944e6fe640ca98922`
- **envelope:** 74 remote containers, one CPU and 1 GB each, 645-second
  child wall; projected aggregate cost below `$1`

The parity evaluation has discharged the raw-wall ambiguity that blocked a
broad launch: its mandatory carrier is safe by more than `10^43` at K'=84.
This wave remains route-locating because it uses only the primary
implementation. It does not promote K'=84 even if every lane passes.

```text
PASS:       all 74 lanes complete and are safe; retain the exact maximum and
            authorize an independent replay of the active/near-active lanes
FAIL:       retain each exact unsafe lane as an analytic obstruction
INCOMPLETE: any timeout or missing lane; retain partial route information
```

**Outcome:** `PASS` as a complete primary route-location wave. App
`ap-1oAXY3d5xqakObFjYF0Ck6` completed all 74 lanes at 58--62 MB peak RSS;
the raw capture SHA-256 is
`884e7bc9ee9c78b49e1324bb3c11ca0ca3d6044114f2bc88dd4cee196b2c916a`.
The wave evaluated 15,651,063 source units, 109,557,441 raw rows, and
268,721,026 geometry rows. The exact global primary maximum is

```text
ordinary:
s2=74/s3=55/s4=45/s5=37/ordinary-single/
c6d3/c7d2/c8d1/c9d0/raw-safe
premium 41388798786059119503097492734939028640066114130
margin     44581160171407926086602515730765812413619
```

The two nearest offset lanes are offset 15, with margin
`53789790696241039676955645542199668046166`, and offset 23, with margin
`55884925238948819300051499174416861077550`. Every lane is safe, but this
primary-only result does not promote K'=84.

## Authorized K'=84 independent completion wave

- **decision:** independently replay the same complete 74-lane partition
  and test exact agreement of coverage keys, maxima, and margins
- **audit wrapper SHA-256:**
  `a9a323316bcbef966ad97ca3e24f66220aa41baf8d5115e7ca3f3205e3e37249`
- **archives and batch runner:** unchanged from the primary wave above
- **envelope:** 74 remote containers, one CPU and 1 GB each, 645-second
  child wall; projected aggregate cost below `$1`

```text
PASS:       all audit lanes complete, are safe, and agree exactly with the
            primary coverage and frontier; mint and verify a K'=84 node
FAIL:       retain every disagreement or unsafe lane; do not promote
INCOMPLETE: retain no row-closure conclusion
```

Unlike a near-active-only audit, this full replay can satisfy the existing
K'=83 node's audit bar for the new row and is therefore closure-directed.

**Outcome:** `PASS`. App `ap-CE1YUXVUmNXrwze1lDP6Wn` completed all 74
independent lanes at 59--62 MB peak RSS; the raw capture SHA-256 is
`11420a74fbebe5f63d717e633c9914c9089c3fb92546051e267c03b60ee1a850`.
For every lane, primary and audit agree exactly on source units, raw rows,
raw-safe units, expanded units, maximum, margin, and active branch after
normalizing the terminal label `raw-safe`/`raw`. The audit evaluated
520,900,317 labelled geometry rows, at least the primary's 268,721,026.
Both implementations therefore return the same ordinary global maximum and
the same positive margin printed above.

This completes the empirical frontier replay required for K'=84. Promotion
still requires a compact merger certificate, exact positive component-gap
arithmetic, a source-hash contract, independent static verification, and
the ordinary DAG gates.

## Preregistered K'=84 compact merger

- **decision:** accept the two full captures only if all 148 jobs are
  present, successful, memory-bounded, and lane-wise identical on the
  independently implemented coverage/frontier keys
- **script SHA-256:**
  `11ef8d98a1cc07db73f4f6e6a17ebb975210a475cf08a8eaa525c4a5ea2a415a`
- **primary capture SHA-256:**
  `884e7bc9ee9c78b49e1324bb3c11ca0ca3d6044114f2bc88dd4cee196b2c916a`
- **audit capture SHA-256:**
  `11420a74fbebe5f63d717e633c9914c9089c3fb92546051e267c03b60ee1a850`
- **envelope:** one remote parser job; expected peak below 128 MB and cost
  below `$0.01`

The merger additionally asserts the exact ordinary maximizer and margin,
the offset source-unit formula `(74-offset)*5625`, the broader audit
geometry count, and normalized primary/audit branch-label equality. A
failure blocks node creation.

**Outcome:** `PASS`. App `ap-UwcGaJZm4Wst0Ozq1NMRIp` completed at 72 MB
peak RSS. The merger capture SHA-256 is
`abc5638fba58fee000c0e8552ea449c4f8058713da3b784a989bf454235633a8`.
It certified 148 jobs, 74 lanes, 15,651,063 source units, 109,557,441 raw
rows, both input hashes, the two geometry totals, and the printed global
maximum and margin.

## Preregistered K'=84 component payment

- **decision:** substitute the merger-certified premium into the exact
  rank-nine ledger and require a positive integral component gap
- **script SHA-256:**
  `391232fc91db032d2599c18e47ad5f9368cf3b9650ede0634972ad118f941207`
- **input premium:**
  `41388798786059119503097492734939028640066114130`
- **envelope:** one remote exact-integer job; expected peak below 128 MB and
  cost below `$0.01`

The script independently reconstructs the row marks, kernel capacity, safe
ceiling, full-rank capacity, required incidence, and final gap from the
hash-pinned rank-nine ledger. A nonpositive gap blocks promotion.

**Outcome:** `PASS`. App `ap-H3we0j1uIdfDebkyKPSRbR` completed at 58 MB
peak RSS; the capture SHA-256 is
`58b8a3077d2dc80444b91a9b0057f6ad47a9fd07a0bce0456904522cc4d054c5`.
The exact total capacity is
`920610888896792835227342245208088849044544034113385622333558298`
against required incidence
`920611111786972543926647666320421141253960527393538734334971880`,
leaving positive gap
`222890179708699305421112332292209416493280153112001413582`.
Together with the merger certificate and the proved analytic dependencies,
this authorizes a K'=84 `PROVED` node; no larger row is authorized.
## Preregistered K'=85 adjacent-support route pilot

- **decision:** determine whether the first open row already breaks the
  proved adjacent-support router, and isolate the exact active obstruction
  or nearest safe competitors for a symbolic domination theorem
- **scope:** `ordinary`, offsets `1`, `15`, `23`, and the new terminal
  offset `74`, in both primary and independent implementations
- **primary wrapper SHA-256:**
  `363cae26e7c0258b27ec27da25b313f8214f6211aa1b891b8c7f506d4987d043`
- **audit wrapper SHA-256:**
  `b0bf02ad6dbf6a6c47556a0e8f8d59a82802f83feec1146d22e8ef4b1b7ecaec`
- **hash-pinned K'=83 code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **batch runner SHA-256:**
  `bbe9f1100d8d6add611794e24e02d57ab0f57903a15195a944e6fe640ca98922`
- **envelope:** ten remote containers, one CPU and 1 GB each, 645-second
  child wall; projected cost below `$0.20`
- **local safety:** one RAM-guarded Modal client; no local enumeration

The wrappers change only the row parameters to `K'=85`, `q=75`,
`m'=67557`, and `n'=1048661`. The theorem and router sources are the
unchanged hash-pinned implementations used to prove `K'=83,84`. The five
lanes are route-locating and are not an exhaustive row certificate.

```text
PASS:       both implementations agree and all five lanes are safe;
            retain the active templates as the symbolic comparison target
FAIL:       both implementations agree on an unsafe lane; retain its exact
            branch as the next analytic wall and do not launch broadly
INCOMPLETE: any timeout, missing lane, or implementation disagreement;
            retain no mathematical conclusion
```

No outcome of this pilot promotes `K'=85`, changes a DAG status, or
authorizes a further finite-row sequence. A complete row replay is permitted
only after the pilot yields a compressed analytic target.

**Outcome:** `PASS` as a five-lane route diagnostic, with no row promotion.
Modal app `ap-d16UIhECIz7nYzMEAZr8d7` completed all ten jobs without
timeout at 60--61 MB peak RSS. The raw capture SHA-256 is
`5a6ee4f212571eae022ed943c6062e95f6b6a2ccb186dbf4338f1b0cf2f45327`.
The compact checker SHA-256 is
`32aa55ce1a31605c7d72678e51855af808a92ccf70a70f029aeaa11d0930134f`.
It verifies capture custody, all ten unique jobs, memory bounds, the
`(75-offset)*5776` offset coverage formula, and exact primary/audit
agreement after normalizing `raw-safe`/`raw` labels.

```text
lane       premium                                             margin
ordinary   41412365746418147165613731954651963334663476202     504063437028248034586407861346996245585667
offset1    41411760082934660310280558759570874584832643708    1109726920515103367759602942435746076418161
offset15   41412416367203894003110488620063995835872421748     453442651281410537829742449314495036640121
offset23   41412551195797006461218092083466032200066465196     318614058168952430226279047278130842596673
offset74     210292675086224485821192607404237233442773250   41202577134768950927827125755109073097466288619
```

The sampled leader is offset 23 with branch

```text
s2=67/s3=44/s4=39/s5=54/offset23/c6F/c7F/c8F/c9F/raw-safe.
```

The ordinary leader changed to

```text
s2=75/s3=56/s4=46/s5=41/ordinary-single/
c6d3/c7d2/c8d1/c9d0/raw-safe.
```

Thus the K'=84 ordinary maximizer is not a stable adjacent-row formula.
The next analytic target is a domination certificate over the unsampled
offsets, beginning with the raw-safe full-fallback family containing
offsets 15 and 23. No complete K'=85 wave is authorized by this outcome.
## Preregistered K'=85 raw-threshold offset envelope

- **decision:** identify the exact global raw-safe leader over all 74 positive
  support-2/3 offset lanes, and isolate the complete residual population whose
  raw premium exceeds the safe ceiling and therefore needs carrier geometry
- **scope:** offsets `1..74`, both a primary exact traversal and an independently
  written reconstruction of the support-2/3 and support-4/5 vectors
- **primary SHA-256:**
  `b13ab1262105d53694407a9c448362bfa85b7914e6fce6242b715f2436c63b3b`
- **audit SHA-256:**
  `90380f5d1f8191172dae43e90b9802873ed6f680a2bc41a49d50d3dade10f59c`
- **dispatcher SHA-256:**
  `f305528a1336c949bccd321799e56ecfa9edd5a8a8757836a9a99afb9929b888`
- **merger SHA-256:**
  `28d9289be8c0e741a364a72884e171154ff0186ea732b1f1cdda3990c3ea333c`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** 148 remote jobs, one CPU and 256 MB each, 165-second child
  timeout and 180-second container timeout; conservative campaign wall below
  five minutes and projected total cost below `$1`
- **partial-output contract:** every completed `m2` slice prints exact safe and
  unsafe counts plus extrema before the next slice begins
- **local safety:** one RAM-guarded Modal client; no local enumeration

The scan evaluates only the pre-geometry raw threshold split. It does not
price any unsafe unit and cannot promote K'=85. The complete paired capture is
accepted only if all 148 unique jobs finish below 128 MB, both traversals agree
on every offset classification digest and profile, and the exact coverage
identity

```text
sum_{d=1}^{74} (75-d) * 76^2
```

holds. `PASS` names the exact raw-safe maximizer and a finite residual geometry
population. `FAIL` is any disagreement or malformed coverage. `INCOMPLETE`
retains only printed partial slices and changes no mathematical status.

The first launch, Modal app `ap-fxCF0n6O4e0LYYDe0MaIPP`, was
`INCOMPLETE`: Modal relocated the dispatcher module to `/root`, exposing an
invalid local-only `parents[2]` path during container import. No mathematical
job started and no output was retained. The repaired dispatcher uses
module-relative mounted paths in both environments; all mathematical sources
and the merger are unchanged.

The second launch, Modal app `ap-ld231Otrj4iOwrf8WgXUbz`, was also
`INCOMPLETE`: all 148 workers started, but the mounted archives were in `/tmp`
while the subprocess working directory was `/root`, so every worker failed the
same archive-discovery check before enumeration (22--24 MB peak, about 0.05
seconds each). The dispatcher now runs workers from `/tmp` and exposes a
four-job offset-1/offset-74 smoke mode that must pass before the full wave is
retried.

The repaired-directory offset-74 smoke, Modal app
`ap-mK2HJJflmciBb31TLyqtUv`, passed in both implementations at 28--29 MB.
It also exposed an unnecessary quadratic Pareto-frontier construction in the
primary traversal before low offsets were launched. Both traversals now cache
the raw value for duplicate local vectors; the primary constructs only the
exact support-4/5 rows required by this scan. The widened smoke tests both the
largest and smallest workloads.

The widened smoke passed as Modal app `ap-A4OvyImj1fVp8vssAhI202`: all four
jobs completed in about 17 seconds at 25--29 MB. Primary and audit agreed on
the complete classification digests. Offset 1 has 15,702 unsafe units and
safe maximum
`41411760082934660310280558759570874584832643708`; offset 74 has no unsafe
units and safe maximum
`210292675086224485821192607404237233442773250`. The smoke capture SHA-256
is `e7dd954638698b2fe4050ddcba35e2f17e9156ba542086d4982141dbfb209982`.
This authorizes the preregistered full wave, but no row promotion.

**Outcome:** `PASS` as an exact route decomposition, with no K'=85
promotion. Modal app `ap-rTfQtYZuTdgjfk5IWhal5W` completed all 148 jobs in
about 27 seconds. The capture SHA-256 is
`5832710721306c16477523b02303fb6f45fb293f6ea53c71e26bad2a9babac13`.
The preregistered merger accepted all 16,028,400 source units and
112,198,800 raw rows per implementation, with exact primary/audit agreement
on every offset profile and classification digest.

There are 15,696,867 raw-safe units and 331,533 raw-unsafe units. Every
offset `42..74` is entirely raw-safe; the residual is confined exactly to
offsets `1..41`. The global raw-safe leader is offset 11,

```text
s2=56/s3=45/s4=58/s5=37/offset11/c6F/c7F/c8F/c9F
```

with premium
`41412868016209776721228891386909879523306833354`, only
`1793645398692419426975603430807602228515` below the safe ceiling. Hence
K'=85 closes if every one of the 331,533 residual units, after its exhaustive
carrier case and adjacent-support payment, is at most this printed leader.
The next falsifier first removes adjacent-support pricing and asks whether
the fixed-union caps alone already imply that domination; a counterexample
will name the exact missing adjacent edge instead of authorizing a broad wave.
## Preregistered K'=85 fixed-union-only domination falsifier

- **decision:** test the deliberately stronger claim that every raw-unsafe
  residual carrier case is already at most the exact offset-11 leader after
  componentwise fixed-union caps, before any adjacent-support price
- **ordered scope:** offset 11 first; offsets 1, 23, and 41 only if every prior
  lane survives
- **falsifier SHA-256:**
  `a55a8353b837e3c83e39eb27fe65590c0f9f91eadcf9fa0d32ae2020ecc0502e`
- **independent witness audit SHA-256:**
  `3beb23b1ec7bfa09bf7e6c6ca67d8f450dde6707aed4d4661383965eb533b138`
- **dispatcher SHA-256:**
  `1efe1237d1ec5838aba4aceca30bd96cbe3ee045c66a22b1b3907017bc1aa14a`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **stopping rule:** stop at the first exact witness above the leader and replay
  only that witness in the independent implementation
- **envelope:** one CPU, 256 MB, 160-second scan wall and 15-second witness
  audit wall per launch; projected total cost below `$0.05`
- **partial output:** every completed `m2` slice prints units, unsafe units, and
  carrier cases checked
- **local safety:** one RAM-guarded Modal client; no local enumeration

`FALSIFIED` rejects only the fixed-union-only shortcut and names the exact
carrier case whose adjacent-support payment remains necessary. `SURVIVED`
authorizes the next offset but is not a proof outside the completed lane.
`INCOMPLETE` changes no mathematical status. No outcome promotes K'=85 by
itself.

**Outcome:** `FALSIFIED` at the first checked residual case, with independent
exact replay. Modal app `ap-319YToKIcY6UC4VZUEIZ0a` returned the offset-11
witness

```text
m2=1, m3=12, s2=74, s3=63, s4=s5=37, m4=m5=38
case=T23, fixed-union charge=(16,7), high=c6F/c7F/c8F/c9F
```

after 2,850 source units, one unsafe unit, and one carrier case. The raw and
fixed-union-only premiums are both
`42141786157949900288596401924882914598461995992`, exceeding the exact
offset-11 leader by
`728918141740123567367510537973035075155162638`. The independent witness
audit agreed on every coordinate, charge, branch, and integer. The capture
SHA-256 is
`2e9a646df4e4fd6dc1626360d9fe8a78bfdccf93766f002422a646dfdf07e4d1`.

Thus the fixed-union-only route is dead and offsets 1, 23, and 41 are not
launched. This does not refute the proved adjacent-support theorem or K'=85;
it localizes the next obligation to the support-disjoint adjacent edges
available for the single `(16,7)` charge.
## Preregistered K'=85 first-witness adjacent payment

- **decision:** on the independently replayed offset-11 `T23` witness, print
  every support-disjoint adjacent-edge price and decide whether the primary
  and independent atlas both reduce it below the exact raw-safe leader
- **scope:** one fixed witness, union 16, dimension 7, available edges 4--5,
  5--6, and 6--7; choices `none`, `4`, `5`, `6`, and `4+6`
- **analyzer SHA-256:**
  `2a63f64023dc04c3a33de293797873dbc9c4d9275dd8486eb31286af2f78724b`
- **dispatcher SHA-256:**
  `be2379bf01c3261489b619a550102e22fc10767e59a019396bda2be3b6e5ef10`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one CPU, 256 MB, 20-second child wall; projected cost below
  `$0.01`
- **local safety:** one RAM-guarded Modal client; no local mathematical run

`PASS` prints both exact option tables and their minimizing edge sets. A price
above the leader is a route wall, not a counterexample to the prize theorem.
`INCOMPLETE` changes no status. This witness calculation cannot promote K'=85.

**Outcome:** `PASS`. Modal app `ap-nJpFGfIsUMBAkL2Ni6Sh2O` completed the
exact analyzer, and the primary and independent formulas agreed on every edge
cap and every option price. The capture SHA-256 is
`9d64a2170614a3c0dae2aef3dd344be231410b1a1a856a38958208686688871e`.

The minimizing choice is the single support-4/5 edge. It lowers the witness
from `42141786157949900288596401924882914598461995992` to
`38031713645027467636162531245586474415179105992`, below the exact raw-safe
leader by `3381154371182309085066360141323405108127727362`. Choices `5`, `6`,
and `4+6` are all weaker on this witness. This identifies an edge-4-only
domination theorem as the next strict, falsifiable compression of the full
adjacent atlas.
## Preregistered K'=85 edge-4-only domination falsifier

- **decision:** test whether the support-4/5 adjacent edge alone pays every
  deduplicated carrier profile of every raw-unsafe unit below the exact
  offset-11 leader
- **ordered scope:** offset 11 first; offsets 1, 23, and 41 only after survival
- **falsifier SHA-256:**
  `b8899f40cec67c03924cb1944341b76010a574212f0889387ccdd3f14cd74440`
- **independent witness audit SHA-256:**
  `8c80fa8e1d338b0366017a15f2f02cd6f1af388c0101019baa733361eebed2d6`
- **dispatcher SHA-256:**
  `32e7b9c7dcc76d84f2703a5111c658c8b5e07c63e676d3eebf92c21add94acca`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **stopping rule:** stop at the first exact over-leader profile and replay it
  with the independent adjacent-pair formula
- **compression:** carrier labels with the same combined fixed-union vector and
  edge-4 cap are evaluated once per residual unit
- **envelope:** one CPU, 256 MB, 215-second child wall per offset; projected
  total cost below `$0.10`
- **partial output:** every completed `m2` slice prints source, unsafe, and
  deduplicated-profile counts

`FALSIFIED` identifies the next adjacent edge or multi-edge obligation.
`SURVIVED` proves only the completed offset. `INCOMPLETE` changes no status.
No pilot outcome promotes K'=85.

**Outcome:** `FALSIFIED` with independent replay. Modal app
`ap-9vbq0eXPV4MZrebuGnSVQr` reached offset 11, `m2=13`, after 73,163 source
units, 2,013 raw-unsafe units, and 238,306 deduplicated geometry profiles. The
first witness is

```text
s2=62, s3=51, s4=s5=50, m4=m5=25
case=F23__N4_t12__N5_t12
charges=(28,7),(29,6), high=c6F/c7F/c8F/c9F
```

The raw premium is
`41678537170179082697698056961638084480681707238`. Replacing supports 4/5
by the edge-4 cap alone gives
`41744966619586153218005378051509525640461543488`, still above the exact
leader by `332098603376376496776486664599646117154710134`; the real minimizer
would therefore reject that replacement in favor of the raw base or another
edge choice. Primary and audit agree exactly. Capture SHA-256:
`c3730780f2404242608fbb2f32dee46f4e7cfa4adbad9cbd7226b9eb945042fa`.

Thus offsets 1, 23, and 41 are not launched. The next exact action is to print
all support-disjoint prices on this two-charge witness and identify the
minimal additional edge set.
## Preregistered K'=85 two-charge witness adjacent payment

- **decision:** print every support-disjoint adjacent-edge price on the exact
  edge-4 counterexample and identify the minimal edge set in both the primary
  and independent atlas
- **scope:** offset 11, `m2=13`, `s4=s5=50`, case
  `F23__N4_t12__N5_t12`, charges `(28,7),(29,6)`
- **analyzer SHA-256:**
  `44faccd0305d374557650c8bfc3b40f3aaa97717e46b154568cbadb3ec77bf3a`
- **dispatcher SHA-256:**
  `d93bfb284f268fcbda93a75558c173538e341bb5420521c7692f45cf98427529`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one CPU, 256 MB, 20-second child wall; projected cost below
  `$0.01`
- **local safety:** one RAM-guarded Modal client; no local mathematical run

`PASS` prints both exact option tables. A best price above the raw-safe leader
is a current-router wall; a lower price identifies the next compressed edge
family. `INCOMPLETE` changes no status. No outcome promotes K'=85.

**Outcome:** `PASS`. Modal app `ap-mnimiGFuHSPQ7gNIcB3gMN` completed the
exact option table; primary and independent values agree entry by entry. The
capture SHA-256 is
`d1ba20be24f8f86e8da708613f89f899341a4c3f34ee3eca515ce0c4a5ba0b1a`.

The minimizing choice is the single support-6/7 edge, with price
`36771696071065385390668923925145098778166086838`, below the exact raw-safe
leader by `4641171945144391330559967461764780745140746516`. The disjoint
choice `4+6` is slightly weaker, while edges 4 and 5 alone do not identify the
minimum. This motivates a best-single-edge domination falsifier before any
full support-disjoint replay.
## Preregistered K'=85 best-single-edge domination falsifier

- **decision:** test whether the best of the raw base and every available
  single adjacent edge pays every deduplicated carrier profile below the exact
  offset-11 leader, while deliberately excluding multi-edge choices
- **ordered scope:** offset 11 first; offsets 1, 23, and 41 only after survival
- **adapter SHA-256:**
  `2c94b7432cd4c9d37a49288298761cbff9227a07f694fe80ec259ef19e724505`
- **base residual scanner SHA-256:**
  `b8899f40cec67c03924cb1944341b76010a574212f0889387ccdd3f14cd74440`
- **independent witness audit SHA-256:**
  `4e938710a8668ed013050f5f1e0979a8c0eb1db76d9dfd47d2c8edf24092b7f6`
- **dispatcher SHA-256:**
  `cdd76442d2e303214a13e8b17f9491975cab5464d8e437fc98a0d01d91574d4c`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **stopping rule:** stop at the first over-leader profile and independently
  maximize the best-single price over every high-support branch
- **compression:** reuse the exact residual router and deduplicate by combined
  fixed-union vector plus the complete adjacent-edge tuple
- **envelope:** one CPU, 256 MB, 215-second child wall per offset; projected
  total cost below `$0.10`
- **partial output:** every completed `m2` slice prints exact coverage counts

`FALSIFIED` demonstrates that a disjoint multi-edge choice is genuinely
needed. `SURVIVED` proves only the completed offset. `INCOMPLETE` changes no
status. No pilot outcome promotes K'=85.

**Offset-11 outcome:** `SURVIVED` exhaustively. Modal app
`ap-x4S2u8ZAef1I0q9N7AK45d` checked all 369,664 source units, all 12,281
raw-unsafe units, and 936,749 deduplicated carrier profiles. Every best-single
price is at most the exact raw-safe leader. Capture SHA-256:
`3b2e0e353e54a4c1f20ab35a5f2775c0a956beb2db6b5c3de411e326daf24989`.
This proves the printed finite offset-11 domination statement and authorizes
the next preregistered lane, offset 1; it does not promote the full row.

**Offset-1 outcome:** `SURVIVED` exhaustively. Modal app
`ap-Wl6GfzOdL4g1bsp7AD8kx8` checked all 427,424 source units, all 15,702
raw-unsafe units, and 181,450 deduplicated carrier profiles. Capture SHA-256:
`9b34ca0dfa9b28db03f3568af47c848e8e4728912273c57ed3166565d1ceec59`.
This proves the printed finite offset-1 domination statement and authorizes
the preregistered offset-23 lane; the full row remains open.

**Offset-23 outcome:** `SURVIVED` exhaustively. Modal app
`ap-ybr2br69sCjzR8D3bGRARc` checked all 300,352 source units, all 7,598
raw-unsafe units, and 2,018,406 deduplicated carrier profiles. Capture
SHA-256:
`539350d9dff7c463386adc9a571d3151e605b7711315c5ea293ab2e37003c3bb`.
This proves the printed finite offset-23 domination statement and authorizes
offset 41, the last lane containing any raw-unsafe unit.

**Offset-41 outcome:** `SURVIVED` exhaustively. Modal app
`ap-7Z7r5eg5OwghIbW5kYXbhj` checked all 196,384 source units, all 138
raw-unsafe units, and 124,168 deduplicated carrier profiles. Capture SHA-256:
`24da317a5c1ff321c46f4402d79c0680837ac04e2abe85e28e526f3032398855`.
The four preregistered stress lanes 1, 11, 23, and 41 all survive. This
authorizes a separately preregistered paired completion wave over every
raw-unsafe offset `1..41`; it does not itself prove the omitted lanes.
## Preregistered K'=85 best-single completion wave

- **decision:** prove or refute the exact best-single-edge domination statement
  on every raw-unsafe offset `1..41` with paired primary and independent
  traversals
- **scope:** 82 jobs; all 12,788,064 source units and all 331,533 raw-unsafe
  units from the paired raw-threshold envelope
- **primary adapter SHA-256:**
  `2c94b7432cd4c9d37a49288298761cbff9227a07f694fe80ec259ef19e724505`
- **independent adapter SHA-256:**
  `f9a01624b5a11fbc30f58a4f4afca2aa75d9af96b35c69edddcdc7eef5e1fa1f`
- **base residual scanner SHA-256:**
  `cd1e9d2706c48be390387953c4abeea46958af258f132700809cf2393a5e4a90`
- **dispatcher SHA-256:**
  `0f82c3311b5bae5fa69e5b7847c9dc777a0ad5e48658b4733c8a8dd26b5fd505`
- **merger SHA-256:**
  `e5c8012cd13ca6c17395fa1be91ce45f0af66042f65d2c58186c1feff3868040`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **preconditions:** offsets 1, 11, 23, and 41 survived exhaustive stress;
  offsets 42..74 are entirely raw-safe; the paired ordinary lane is below the
  exact offset-11 leader
- **envelope:** one CPU and 256 MB per job, 270-second child wall and
  285-second container wall; 82 containers, conservative campaign wall below
  five minutes and projected total cost below `$0.25`
- **partial output:** every worker retains completed `m2` progress on timeout;
  successful wrappers store exact coverage, output hash, and peak RSS
- **deployment gate:** paired offsets 2 and 41 must agree before the repaired
  full 82-job wave is launched

`PASS` requires all 82 jobs, exact primary/audit agreement on every lane count,
12,788,064 source units, 331,533 residual units, and no over-leader profile.
Together with the paired raw envelope and ordinary pilot, this authorizes a
compact K'=85 component-payment certificate. `FALSIFIED` retains the first
paired witness and blocks promotion. `INCOMPLETE` changes no status.

The paired deployment smoke passed as Modal app
`ap-io6hEGkfZQtfHfBccqWiHo`. Both offset-41 implementations report 196,384
source units, 138 raw-unsafe units, 124,168 profiles, and the same exact leader
at 31--33 MB peak RSS. The smoke capture SHA-256 is
`e51e3be06123a0e5a654a071eeded4b76b9aabcb2172828978b54d7669895b0d`.
This authorizes the full wave from the pinned sources; it does not itself
promote K'=85.

The first full launch, Modal app `ap-o86zjFxfuNrY2qg9YGj9aW`, was
`INCOMPLETE` before omitted-lane enumeration. The reusable base scanner still
enforced the stress-only input set `{1,11,23,41}`, so 74 jobs rejected their
offset at the input guard; all eight stress jobs again passed pairwise at
30--35 MB. The capture SHA-256 is
`c080c618af3a05c311e55039297405952ba011684234a21f6a7ae2d72d6f26ec`.
The repair widens only that guard to the already preregistered interval
`1..41`; formulas, traversal, adapters, and merger are unchanged. A new paired
smoke must pass before relaunch.

The repaired paired smoke passed as Modal app
`ap-cnvj6o0mqfgRMqdV9Pxrg4`. Formerly blocked offset 2 agrees exactly on
421,648 source units, 15,377 unsafe units, and 225,910 profiles; offset 41
again agrees on 196,384, 138, and 124,168 respectively. All four jobs used
31--32 MB. Capture SHA-256:
`2b2295688002ced4b1c35bcd377b2a82b0e1298ae509a23749be57371f76bb6e`.
This exercises the repaired guard and authorizes the full relaunch.

**Outcome:** `PASS`. The repaired full wave completed as Modal app
`ap-avKuaBEl3bNsvVug235bXS`. All 82 jobs passed below the memory limit, and
the preregistered merger accepted exact primary/audit agreement on all 41
offsets, 12,788,064 source units, all 331,533 raw-unsafe units, and 49,090,656
deduplicated carrier profiles per implementation. The capture SHA-256 is
`a2a47722b66ff40ed83b44c47dc725b341700ffc2c9653a61e63f7dff1fedfa8`.

Every residual profile is at most the exact raw-safe offset-11 leader
`41412868016209776721228891386909879523306833354`. Together with the paired
raw-threshold envelope, fully safe offsets 42..74, and the paired ordinary
lane, this certifies the complete K'=85 carrier frontier. Promotion still
requires the exact positive component-payment arithmetic and compact node
contract.
## Preregistered K'=85 component payment

- **decision:** substitute the merger-certified K'=85 frontier premium into
  the exact rank-nine ledger and require a positive integral component gap
- **input premium:**
  `41412868016209776721228891386909879523306833354`
- **expected safe-ceiling margin:**
  `1793645398692419426975603430807602228515`
- **payment script SHA-256:**
  `8e3fa571c1930f11a8c0a38b6595ff6e4b712158d2d84792912db5c88285ebe8`
- **dispatcher SHA-256:**
  `a054f7b2139bd7decae3a733e87558a23c9963acefeb3e44bb53a9ee4ab5decd`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one CPU, 256 MB, 20-second child wall; projected cost below
  `$0.01`
- **local safety:** one RAM-guarded Modal client; no local mathematical run

`PASS` independently reconstructs the marks, kernel, safe ceiling, full-rank
capacity, required incidence, and a strictly positive gap. This authorizes a
compact K'=85 `PROVED` node when combined with the paired frontier captures and
analytic DAG gates. `INCOMPLETE` or a nonpositive gap blocks promotion.

**Outcome:** `PASS`. Modal app `ap-9R6TUWXTLwS11AiqMsAem5` independently
reconstructed the exact row and returned safe-ceiling remainder
`15362028411627110`, full-rank capacity
`920664857300015914310061122145042076654631136279218382941612598`, total
capacity
`920761032600863899558839605552732140962924224823394196355672563`, and
required incidence
`920761041568462403301620608624242874288842867899367408189696564`.
The resulting component gap is

```text
8967598503742781003071510733325918643075973211834024001>0.
```

The capture SHA-256 is
`e3bf7fdbd3c6b87ea2bb82bd2520f6ffff5e76353e0698e8df7494bf75745799`.
Together with the complete paired frontier, this authorizes the compact
K'=85 `PROVED` node and extends the finite closed prefix to `10..85`.
## Preregistered K'=86 adjacent-support route pilot

- **decision:** test whether the complete K'=85 best-single mechanism still
  has positive room at the next row and identify the first exact unsafe lane
  if it does not
- **scope:** `ordinary`, offsets `11`, `23`, `41`, and terminal offset `75`,
  in both primary and independent implementations
- **primary wrapper SHA-256:**
  `ca6ffd6766d1e4aac72d98ea09fa30c5d1b100a01c2e51e5e7673bfc92f33106`
- **audit wrapper SHA-256:**
  `ceab00de841839ee0c76eb440e847f27aeb524d11dc6646742f774991817a2ef`
- **checker SHA-256:**
  `8373bebdc09e49f55281703c404ec44283fd10e1f766ad4d9eb066ef46b91eef`
- **hash-pinned K'=83 code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **batch runner SHA-256:**
  `bbe9f1100d8d6add611794e24e02d57ab0f57903a15195a944e6fe640ca98922`
- **envelope:** ten remote containers, one CPU and 1 GB each, 645-second
  child wall; projected cost below `$0.20`
- **local safety:** one RAM-guarded Modal client; no local enumeration

The wrappers change only the row parameters to `K'=86`, `q=76`,
`m'=67558`, and `n'=1048662`. The theorem and router sources are the same
hash-pinned implementations used at `K'=83..85`. An unsafe mathematical
lane exits normally and is retained as a route outcome; only timeout,
malformed output, or implementation disagreement makes the batch incomplete.

```text
SAFE PILOT:   both implementations agree and all five lanes are safe;
              locate unsampled and residual leaders before any broad wave
UNSAFE PILOT: both implementations agree and at least one lane is unsafe;
              retain the exact branch as the next theorem obstruction
INCOMPLETE:   timeout, missing lane, or implementation disagreement;
              retain no mathematical conclusion
```

No outcome promotes `K'=86`, changes a DAG status, or authorizes interval
extrapolation. A broader finite wave is permitted only if this pilot leaves
a sharply typed residual statement.

**Outcome:** `INCOMPLETE`, with exact partial checkpoints retained and no row
promotion. Modal app `ap-OP9ryrK2YdHRg463E43ktv` completed nine of ten jobs
before the local client reached its five-minute RAMguard wall. Capture
SHA-256:
`d343b18cfef00d6a1dff8634a2ffe8b8574d25a59cf44f43d4c3862e47c8a4d8`.
Primary and audit agree exactly, and remain safe, on ordinary and offsets 11,
41, and 75. Primary offset 23 is also safe. The sampled paired leader is the
ordinary lane with premium
`41436497718685364991538520386265961874369213524` and positive margin
`395858925488158871546979481504003419111314`.

Only audit offset 23 was missing. A one-job repair app
`ap-pejd1RneFmD0oc2yq2QjSZ` reached its preregistered 645-second child
timeout at 62 MB; repair-capture SHA-256:
`3a642fe1566ba8ffeb9282ed0d121928752c0ef69eabb58704cb9984455e7913`.
No longer full-geometry rerun is authorized. The next route action uses the
much cheaper complete paired raw-threshold envelope to locate every residual
offset before selecting any further geometry theorem.
## Preregistered K'=86 raw-threshold offset envelope

- **decision:** identify the exact global raw-safe leader over all 75 positive
  support-2/3 offsets and isolate the complete population requiring carrier
  geometry
- **scope:** offsets `1..75`, both the primary traversal and the independently
  written reconstruction
- **primary K'=86 adapter SHA-256:**
  `e37b36fec4eab6286e353e54027b87235f0369947c814e795bcbff7a7aa8a68d`
- **independent K'=86 adapter SHA-256:**
  `429336fefdf47623184b2d2f2e21953f50be7fe07dda2c1e8ba054e4af637d74`
- **primary base SHA-256:**
  `b13ab1262105d53694407a9c448362bfa85b7914e6fce6242b715f2436c63b3b`
- **independent base SHA-256:**
  `90380f5d1f8191172dae43e90b9802873ed6f680a2bc41a49d50d3dade10f59c`
- **dispatcher SHA-256:**
  `b7614800264d3b94798c5b36691bfde6225e9230727199d72b59b3a18555bdd6`
- **merger SHA-256:**
  `78d96a7ef3708d488966fe2425f49f7c84152839225a971e5fde7cb3d5ec45bc`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** 150 remote jobs, one CPU and 256 MB each, 165-second child
  timeout and 180-second container timeout; projected total cost below `$1`
- **local safety:** one `modal`-profile RAMguard client; no local enumeration

The adapters alter only `K'=86`, `q=76`, `m'=67558`, `n'=1048662`, and the
derived exact safe ceiling. They call the two independently implemented,
hash-pinned K'=85 scanners. A four-job offset-1/offset-75 smoke must pass
before the complete wave.

The full capture is accepted only if all 150 jobs finish below 128 MB, both
implementations agree on every offset classification digest and profile, and

```text
sum_{d=1}^{75} (76-d) * 77^2
```

source units are classified. `PASS` names the exact raw-safe maximizer and
finite residual population. `FAIL` is an implementation disagreement or
malformed coverage. `INCOMPLETE` retains partial checkpoints and changes no
mathematical status. This scan alone cannot promote `K'=86`.

The paired deployment smoke passed as Modal app
`ap-exYBHBmoQGphWMxVn85Cnz`. Primary and independent implementations agree
exactly on offset 1 (444,675 units, 19,178 unsafe) and terminal offset 75
(5,929 units, all safe), including both classification digests. All four
jobs used 25--29 MB. Smoke-capture SHA-256:
`11fb92f8c98a8e07bbadc87bc97b044479462bcb6da11863c894650dce7404c0`.
This validates both adapters and authorizes the preregistered full wave; it
does not itself promote `K'=86`.

**Outcome:** `PASS` as an exact route decomposition, with no `K'=86`
promotion. Modal app `ap-kjz4PvurdW9cunGO3pse1N` completed all 150 jobs.
The capture SHA-256 is
`7aa3c934e610aa717ba25b8b7acf424c0f59ad068ec294eac5b448d9abb81612`.
The checker accepted all 16,897,650 source units and 118,283,550 raw rows
per implementation, with exact agreement on every offset profile and
classification digest.

There are 16,482,237 raw-safe units and 415,413 raw-unsafe units. Every
offset `43..75` is entirely raw-safe; the residual is confined exactly to
offsets `1..42`. The global raw-safe leader is offset 32,

```text
s2=73/s3=41/s4=39/s5=57/offset32/c6F/c7F/c8F/c9F
```

with premium
`41436891148468120556440841127823744176664445997`, only
`2429142732593969226237923721701123878841` below the exact safe ceiling.
Hence `K'=86` closes if every residual profile is at most this leader after
a proved carrier charge.

The preregistered checker printed unsafe offsets in completion order. A
presentation-only repair sorts that list without changing parsing,
coverage, digest comparison, or extrema; repaired checker SHA-256:
`2a32a19df70f098fee290c96545d704f1de1479a995876c50876d8fc79d25f86`.
The pinned capture passes the repaired checker with unsafe offsets exactly
`1..42`.
## Preregistered K'=86 best-single-edge stress falsifier

- **decision:** test whether the best of the raw price and each available
  single adjacent edge pays every deduplicated carrier profile below the exact
  K'=86 raw-safe leader on four route-deciding offsets
- **ordered scope:** offsets `32` (the raw-safe leader), `1` (largest lane),
  `23` (interior stress), and `42` (last raw-unsafe lane), evaluated in one
  paired deployment
- **primary adapter SHA-256:**
  `8a2ec9877e317798e615e14d0e23b2f0c65d927a109985c7aec160c1cc65db97`
- **independent-pricing adapter SHA-256:**
  `ad37ddbfa7920e57ad912b523751d9415944f8e16459c49bb7973a86e386cd10`
- **shared K'=86 traversal core SHA-256:**
  `2eb7f85cf6fb4311874f453c75fc868796dbc726599462e12b640e98fe2a9939`
- **K'=85 primary formula adapter SHA-256:**
  `2c94b7432cd4c9d37a49288298761cbff9227a07f694fe80ec259ef19e724505`
- **K'=85 independent formula adapter SHA-256:**
  `f9a01624b5a11fbc30f58a4f4afca2aa75d9af96b35c69edddcdc7eef5e1fa1f`
- **K'=85 residual base SHA-256:**
  `cd1e9d2706c48be390387953c4abeea46958af258f132700809cf2393a5e4a90`
- **dispatcher SHA-256:**
  `dc2e0c69e0aa8928e24cc3777f744d3394716f70ebd6970e3c8bcf27b72fe325`
- **checker SHA-256:**
  `8961626415452cf5de84e8cc5194c47c40eba8d56d1a13f6c4f3989828d5d3cd`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** eight jobs, one CPU and 256 MB each, 300-second child wall
  and 315-second container wall; projected total cost below `$0.10`
- **local safety:** one `modal`-profile RAMguard client; no local enumeration

The adapters alter only `K'=86`, `q=76`, `m'=67558`, `n'=1048662`, the
derived exact ceiling, and the exact raw-safe offset-32 leader. They retain
the proved K'=85 carrier formulas. Both implementations share the explicit
row-generic source-unit traversal, while the adjacent-edge prices are rebuilt
by the primary router and the separately implemented audit formulas.

`FALSIFIED` requires a paired exact over-leader witness and blocks a full
best-single campaign. `SURVIVED` requires paired agreement on all four lanes,
1,221,374 completed source units, and every carrier profile at or below the
leader. `INCOMPLETE` retains partial checkpoints and changes no mathematical
status. Survival authorizes a separately preregistered completion wave over
offsets `1..42`; this stress campaign alone cannot promote `K'=86`.

**Outcome:** `SURVIVED`. Modal app `ap-5YQpAxDUQx8BshC5cCrqxM` completed all
eight jobs at 29--34 MB peak RSS. The paired checker accepted all 1,221,374
source units and 4,954,135 deduplicated carrier profiles per implementation,
with exact agreement on offsets 1, 23, 32, and 42. Capture SHA-256:
`8499f33db4c4bcd20b7c2e8b8bc170d3d6beb7f33421539d43f1e6165e5301ba`.
The raw-safe leader lane, the largest lane, the interior stress lane, and the
last raw-unsafe lane all survive. This authorizes the separately pinned full
completion wave; it does not promote `K'=86`.
## Preregistered K'=86 best-single completion wave

- **decision:** prove or refute the exact best-single-edge domination statement
  on every raw-unsafe offset `1..42` with paired primary and independent-price
  traversals
- **scope:** 84 jobs; all 13,571,481 source units and all 415,413 raw-unsafe
  units from the paired raw-threshold envelope
- **primary adapter SHA-256:**
  `8a2ec9877e317798e615e14d0e23b2f0c65d927a109985c7aec160c1cc65db97`
- **independent-pricing adapter SHA-256:**
  `ad37ddbfa7920e57ad912b523751d9415944f8e16459c49bb7973a86e386cd10`
- **shared K'=86 traversal core SHA-256:**
  `2eb7f85cf6fb4311874f453c75fc868796dbc726599462e12b640e98fe2a9939`
- **K'=85 primary formula adapter SHA-256:**
  `2c94b7432cd4c9d37a49288298761cbff9227a07f694fe80ec259ef19e724505`
- **K'=85 independent formula adapter SHA-256:**
  `f9a01624b5a11fbc30f58a4f4afca2aa75d9af96b35c69edddcdc7eef5e1fa1f`
- **K'=85 residual base SHA-256:**
  `cd1e9d2706c48be390387953c4abeea46958af258f132700809cf2393a5e4a90`
- **dispatcher SHA-256:**
  `4f47b9d541eddbd633e96d94d6aab473b3b1da9a8ede8c9726e1016cbe4ddc56`
- **merger SHA-256:**
  `d7e83244e5b674c05c710d4930b85616115616d9ac53bd068328a8db7dd1e932`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **precondition:** offsets 1, 23, 32, and 42 survived exact paired stress,
  including 4,954,135 carrier profiles per implementation
- **envelope:** one CPU and 256 MB per job, 300-second child wall and
  315-second container wall; 84 containers and projected total cost below
  `$0.50`
- **partial output:** every worker retains completed `m2` progress on timeout;
  successful wrappers store exact coverage, output hash, and peak RSS
- **local safety:** one `modal`-profile RAMguard client; no local enumeration

`PASS` requires all 84 jobs, exact primary/audit agreement on every lane
count, 13,571,481 source units, 415,413 residual units, and no over-leader
profile. Together with the paired raw envelope and fully safe offsets
`43..75`, this proves the finite best-single carrier statement for the
nonordinary K'=86 frontier. `FALSIFIED` retains the first paired witness and
blocks promotion. `INCOMPLETE` changes no status.

Even on `PASS`, promotion requires the ordinary-lane coverage contract and
the exact positive component-payment arithmetic to be stated and verified in
a compact DAG node.

**Outcome:** `PASS`. Modal app `ap-HSdSkI0KYmWfnz0jL0Bron` completed all 84
jobs below the memory limit. The merger accepted exact primary/audit agreement
on all 42 offsets, all 13,571,481 source units, all 415,413 raw-unsafe units,
and 62,159,220 deduplicated carrier profiles per implementation. Capture
SHA-256:
`bc67b9fa9ffa6b386d5d5f9e053e2d5a99a8451f2e9ae8d03c0095cc6f867349`.

Every residual profile is at most the exact raw-safe offset-32 leader
`41436891148468120556440841127823744176664445997`. Together with the paired
raw-threshold envelope, fully safe offsets `43..75`, and the paired ordinary
lane, this certifies the complete K'=86 carrier frontier. Promotion still
requires the exact positive component-payment arithmetic and compact node
contract.
## Preregistered K'=86 component payment

- **decision:** substitute the merger-certified K'=86 frontier premium into
  the exact rank-nine ledger and require a positive integral component gap
- **input premium:**
  `41436891148468120556440841127823744176664445997`
- **expected safe-ceiling margin:**
  `2429142732593969226237923721701123878841`
- **payment script SHA-256:**
  `fc2f9a1c6f406063ca305a6744852680fdf363c422fa6a9586db9b071752cc65`
- **dispatcher SHA-256:**
  `55e75f6cd7ee5bb5facdaf005d4bad397fc37c9b29a206c2b18d1f081333aaeb`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one CPU, 256 MB, 20-second child wall; projected cost below
  `$0.01`
- **local safety:** one RAM-guarded Modal client; no local mathematical run

`PASS` independently reconstructs the marks, kernel, safe ceiling, full-rank
capacity, required incidence, and a strictly positive gap. This authorizes a
compact K'=86 `PROVED` node when combined with the paired frontier captures
and analytic DAG gates. `INCOMPLETE` or a nonpositive gap blocks promotion.

**Outcome:** `PASS`. Modal app `ap-3mwC5dZ9yYxOTcOJx9JygE` independently
reconstructed the exact row and returned safe-ceiling remainder
`227261548525136411`, full-rank capacity
`920812197157351151323326240869770734642178201951825815213388613`, total
capacity
`920910981401515382507267812115889364849258449737790776660916953`, and
required incidence
`920910993546377878777553498313894622180137392955340138442435688`.
The resulting component gap is

```text
12144862496270285686198005257330878943217549361781518735>0.
```

Capture SHA-256:
`252d9dfa3f4c6e819a706a54e437aae1337907473e3dd3113bff460764007f3e`.
Together with the complete paired frontier and the separately checked
ordinary slice, this authorizes the compact K'=86 `PROVED` node and extends
the finite closed prefix to `10..86`.
## Preregistered K'=87 raw-threshold offset envelope

- **decision:** identify the exact global raw-safe leader over all 76 positive
  support-2/3 offsets and isolate the complete population requiring carrier
  geometry
- **scope:** offsets `1..76`, both the primary traversal and the independently
  written reconstruction
- **primary K'=87 adapter SHA-256:**
  `d85f91f5cfbfbaa4550377cc0096b194108bbc8bdd660b9e3f680ef6a83e08c5`
- **independent K'=87 adapter SHA-256:**
  `b968b55cd98d04224ed3ef36bc8e14b83614f8e60257a76546fdfe87200a41d8`
- **primary base SHA-256:**
  `b13ab1262105d53694407a9c448362bfa85b7914e6fce6242b715f2436c63b3b`
- **independent base SHA-256:**
  `90380f5d1f8191172dae43e90b9802873ed6f680a2bc41a49d50d3dade10f59c`
- **dispatcher SHA-256:**
  `188db97045b5d97162e5038822b016805a9fb4299ec6b61bd71883ed9d114de2`
- **merger SHA-256:**
  `e7dbbd4145bc9924806f9fc1e85d1593ec77c67d898e69633fe0c56e5b51ca38`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** 152 remote jobs, one CPU and 256 MB each, 165-second child
  timeout and 180-second container timeout; projected total cost below `$1`
- **local safety:** one `modal`-profile RAMguard client; no local enumeration

The adapters alter only `K'=87`, `q=77`, `m'=67559`, `n'=1048663`, and the
derived exact safe ceiling. They call the two independently implemented,
hash-pinned K'=85 scanners. A four-job offset-1/offset-76 smoke must pass
before the complete wave.

The full capture is accepted only if all 152 jobs finish below 128 MB, both
implementations agree on every offset classification digest and profile, and

```text
sum_{d=1}^{76} (77-d) * 78^2 = 17,801,784
```

source units are classified. `PASS` names the exact raw-safe maximizer and
finite residual population. `FAIL` is an implementation disagreement or
malformed coverage. `INCOMPLETE` retains partial checkpoints and changes no
mathematical status. This scan alone cannot promote `K'=87`.

The paired deployment smoke passed as Modal app
`ap-vTfGBIN3tpyW7Yp0fZhRM6`. Primary and independent implementations agree
exactly on offset 1 (462,384 units, 23,104 unsafe) and terminal offset 76
(6,084 units, all safe), including both classification digests and complete
`m2` profiles. All four jobs used 25--28 MB. Smoke-capture SHA-256:
`9abaa530060708007b1c1faa24653a448154997a8ef6268dccb8793586358e69`.
This validates both adapters and authorizes the preregistered full wave; it
does not itself promote `K'=87`.

The complete paired wave passed as Modal app
`ap-xwOdMdTBRKtC2aIHtpRSw0`. Capture SHA-256:
`2722d7811cf29e425bd67fd49a46f586efe2f21c0dda698e369dcfe4fd48b449`.
All 152 jobs completed below 128 MB, and the primary and independent
implementations agree on every offset classification and profile.

```text
source units per implementation       17,801,784
raw rows per implementation          124,612,488
raw-safe units                         17,290,107
raw-unsafe units                          511,677
unsafe offsets                              1..43
fully safe offsets                         44..76
```

The exact raw-safe leader is offset 9,

```text
s2=55/s3=46/s4=37/s5=30/offset9/c6F/c7F/c8F/c9F
```

with premium `41460899125475443837881046685022762331499044695`, strictly
below the exact safe ceiling
`41460914669043067085305042221812436226076443389` by
`15543567623247423995536789673894577398694`. The raw envelope is therefore
complete. The remaining `K'=87` obligation is a finite 511,677-unit
post-carrier payment over offsets `1..43`.
## Preregistered K'=87 best-single-edge stress falsifier

- **decision:** test whether the best of the raw price and each available
  single adjacent edge pays every deduplicated carrier profile below the exact
  K'=87 raw-safe leader on four route-deciding offsets
- **ordered scope:** offsets `9` (the raw-safe leader), `1` (largest lane),
  `23` (interior stress), and `43` (last raw-unsafe lane), evaluated in one
  paired deployment
- **primary adapter SHA-256:**
  `f2ef06960e42febe620dcfa7ecddf2d7207532462e764e0b767a98416f45de53`
- **independent-pricing adapter SHA-256:**
  `d4c6baed6e30a3acea25b808a6320589fc1b7aadd401da1a4fac0566b17df627`
- **shared K'=87 traversal core SHA-256:**
  `53b1d80cabff9cf1995043195b91e8b1e96013ffcb8aaacf5642591a88cd3e0a`
- **K'=85 primary formula adapter SHA-256:**
  `2c94b7432cd4c9d37a49288298761cbff9227a07f694fe80ec259ef19e724505`
- **K'=85 independent formula adapter SHA-256:**
  `f9a01624b5a11fbc30f58a4f4afca2aa75d9af96b35c69edddcdc7eef5e1fa1f`
- **K'=85 residual base SHA-256:**
  `cd1e9d2706c48be390387953c4abeea46958af258f132700809cf2393a5e4a90`
- **dispatcher SHA-256:**
  `951b2c2f3b560fd4df4dadf2da51d896c81207a8bd6890d468007f896144514d`
- **checker SHA-256:**
  `d03a0018a439f1fdde77fc8f74cd7388aef4520cdab9b5b5bdcce6179b0b1d7e`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** eight jobs, one CPU and 256 MB each, 360-second child wall
  and 375-second container wall; projected total cost below `$0.15`
- **local safety:** one `modal`-profile RAMguard client; no local enumeration

The adapters alter only `K'=87`, `q=77`, `m'=67559`, `n'=1048663`, the
derived exact ceiling, and the exact raw-safe offset-9 leader. They retain the
proved K'=85 carrier formulas. Both implementations share the explicit
row-generic source-unit traversal, while the adjacent-edge prices are rebuilt
by the primary router and the separately implemented audit formulas.

`FALSIFIED` requires a paired exact over-leader witness and blocks a full
best-single campaign. `SURVIVED` requires paired agreement on all four lanes,
1,411,488 completed source units, and every carrier profile at or below the
leader. `INCOMPLETE` retains partial checkpoints and changes no mathematical
status. Survival authorizes a separately preregistered completion wave over
offsets `1..43`; this stress campaign alone cannot promote `K'=87`.

**Outcome:** `FALSIFIED`. Modal app `ap-LHOZ5HAjGEZi9RzlEHSHZH` completed all
eight jobs at 30--34 MB peak RSS. The paired checker accepted 1,111,080
completed source units and 4,333,348 deduplicated carrier profiles per
implementation. Offsets 9, 23, and 43 survived exhaustively, while both
implementations returned the same first offset-1 witness:

```text
m2=27, m3=28, s2=50, s3=49, s4=48, s5=47
case=F23__N4_t2__N5_t0
charges=(32,7),(36,5), high=c6F/c7F/c8F/c9F
```

Its raw premium is
`46081464205190838687203932464720858867144442465`. The best single adjacent
edge leaves
`41535717484613459403166619514559682376379208865`, above the exact raw-safe
leader by `74818359138015565285572829536920044880164170`. Capture SHA-256:
`28384df190292e49aeb22ded3194f83037700654293fe5ba4518ffd2680a5501`.

The full best-single wave is therefore blocked. This witness has available
edges 4, 5, and 6, so the next bounded action is to print the complete
support-disjoint option table and test whether edge set `4+6` supplies the
minimal valid repair.
## Preregistered K'=87 residual-witness adjacent payment

- **decision:** print every support-disjoint adjacent-edge price on the exact
  best-single counterexample and identify the minimal edge set in both the
  primary and independent atlas
- **scope:** offset 1, `m2=27`, `s4=48`, `s5=47`, case
  `F23__N4_t2__N5_t0`, charges `(32,7),(36,5)`
- **K'=87 adapter SHA-256:**
  `a66f4235d0651bd35d3ccbe749beb6ea5f52c6b2198bc1460bf13f3fe7907a00`
- **base paired analyzer SHA-256:**
  `44faccd0305d374557650c8bfc3b40f3aaa97717e46b154568cbadb3ec77bf3a`
- **dispatcher SHA-256:**
  `64bca2a9e0ce3d6b0f69ed664db3a18e01e8348dcde9bc3e046ec6c4116c506e`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one CPU, 256 MB, 20-second child wall and 30-second container
  wall; projected cost below `$0.01`
- **local safety:** one RAM-guarded Modal client; no local mathematical run

The adapter changes only `K'=87`, `q=77`, `m'=67559`, the exact safe ceiling,
and the raw-safe leader. The base analyzer enumerates all support-disjoint
subsets of the available edges and independently reconstructs every adjacent
pair cap.

`PASS` prints both exact option tables. A best price above the leader is a
current adjacent-router wall; a lower price identifies the next compressed
edge family. `INCOMPLETE` changes no status. This one-witness calculation
cannot promote `K'=87`.

**Outcome:** `PASS`. Modal app `ap-wLdIVTwSfqoHqcbrTReo02` completed the
paired exact option table. Primary and independent values agree entry by
entry. Capture SHA-256:
`9edcb2b46da5f9cb3aa97bcc8f230e0725bc7b2cd72e214477f4c5ece34ba82b`.

The minimizing valid choice is the support-disjoint edge set `4+6`, with
price `37213564927666895824914633823577105351210858112`, below the exact
raw-safe leader by `4247334197808548012966412861445656980288186583`.
Every single edge remains above the leader:

```text
edge 4  41697268189301188466486299088841700382091277312
edge 5  41535717484613459403166619514559682376379208865
edge 6  41597760943556546045632267199456263836264023265
```

This repairs the single witness but not the row. It authorizes an exhaustive
paired offset-1 falsifier using the proved support-disjoint optimizer.
## Preregistered K'=87 support-disjoint offset-1 falsifier

- **decision:** exhaust the complete offset-1 residual lane using the best
  support-disjoint subset of available adjacent edges
- **scope:** paired primary and independent traversals of offset 1; no other
  offset is launched in this campaign
- **primary adapter SHA-256:**
  `9aa4ff7e6d71face083b427d06519486ec50a6c6554203007a7f9be07abdb5c8`
- **independent-pricing adapter SHA-256:**
  `f4d447913771dde26e085d56fbfdef0fec6ba702183f99f403dccfe2f2a98e22`
- **K'=87 best-single primary base SHA-256:**
  `f2ef06960e42febe620dcfa7ecddf2d7207532462e764e0b767a98416f45de53`
- **K'=87 best-single audit base SHA-256:**
  `d4c6baed6e30a3acea25b808a6320589fc1b7aadd401da1a4fac0566b17df627`
- **K'=87 traversal core SHA-256:**
  `53b1d80cabff9cf1995043195b91e8b1e96013ffcb8aaacf5642591a88cd3e0a`
- **dispatcher SHA-256:**
  `964a08d370022a2ce6fde495346e3bed3c3b8ed2907cc8ab9b0a8a210399ac6c`
- **checker SHA-256:**
  `8dd3942479fdcb34b93908629039ed1e33484015de07a314fcc55fef1950c02f`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** two jobs, one CPU and 256 MB each, 480-second child wall and
  495-second container wall; projected total cost below `$0.10`
- **local safety:** one `modal`-profile RAMguard client; no local enumeration

The primary adapter calls the proved `priced_all_adjacent` optimizer; the
independent adapter calls its separately implemented `price` reconstruction.
Both enumerate only edge sets with pairwise disjoint support pairs. No
overlapping adjacent charges are composed.

`FALSIFIED` requires a paired exact over-leader witness and blocks a complete
support-disjoint campaign. `SURVIVED` requires exact agreement on all 462,384
offset-1 source units and every deduplicated carrier profile. `INCOMPLETE`
retains partial checkpoints and changes no status. Offsets 9, 23, and 43
already inherit survival because this optimizer includes every best-single
choice. This campaign alone cannot promote `K'=87`.

**Outcome:** `FALSIFIED`. Modal app `ap-cJPrOXXEvVBCRydRzokVWK` completed
both jobs at 31--32 MB peak RSS. The paired checker accepted 168,060 source
units, 9,217 raw-unsafe units, and 144,439 deduplicated profiles per
implementation before both traversals reached the same witness:

```text
m2=28, m3=29, s2=49, s3=48, s4=48, s5=47
case=F23__N4_t0__N5_t0
charges=(34,6),(36,5), high=c6F/c7F/c8F/c9F
```

Only edges 4 and 5 are available, so no two-edge support-disjoint subset
exists. The optimized price is
`41489774300553901192839119028686282570642878551`, above the exact raw-safe
leader by `28875175078457354958072343663520239143833856`. Capture SHA-256:
`dcc663d48ea02daa4267f9a13b4af6889f66d8af9738e35af96df4e42c400e23`.

The complete support-disjoint campaign is therefore blocked. The next route
must strengthen one pair bound or derive a genuine simultaneous support-
`4/5/6` inequality from the shared dimension-six fixed union; overlapping
pair charges may not simply be added.
## Preregistered K'=87 simultaneous support-4/5/6 witness probe

- **decision:** test whether retaining the shared support-5 stratum in the
  two proved adjacent-flat inequalities pays the exact support-disjoint
  counterexample
- **scope:** one fixed witness and its dimension-six charge `(u,g)=(34,6)`;
  no residual lane scan
- **probe SHA-256:**
  `e4869f37c3eab008a2d17e829ec33bfba1612018c8b99be8f908af389fa7a986`
- **dispatcher SHA-256:**
  `d62f08a5741d4720bef0b0e43d15cb2d74617e0569e62db0b1ef20feb8bacfd3`
- **K'=87 witness adapter SHA-256:**
  `a66f4235d0651bd35d3ccbe749beb6ea5f52c6b2198bc1460bf13f3fe7907a00`
- **base witness analyzer SHA-256:**
  `44faccd0305d374557650c8bfc3b40f3aaa97717e46b154568cbadb3ec77bf3a`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one CPU, 256 MB, 20-second child wall and 30-second container
  wall; projected cost below `$0.01`
- **local safety:** one RAM-guarded Modal client; no local mathematical run

For each intersection stratum `i=0,1,2`, the probe simultaneously imposes
the proved `(4,5)` and `(5,6)` instances of `(FAS1)`, together with the
proved `(FAS2)` individual caps on supports 4 and 5. It maximizes the weighted
`C4+C5+C6` objective over the resulting rational polytope. One implementation
uses the explicit support-5 breakpoints; the audit independently enumerates
all LP vertices with exact rational arithmetic. The remaining strata use the
same direct completion caps printed in the proved fixed-union theorem.

This does not add overlapping pair bounds. It uses two simultaneous
inequalities sharing one variable and solves their joint feasible region.
`PASS` requires exact agreement of both LP implementations and prints the
resulting witness price. A nonpositive margin is a route wall. A positive
margin authorizes theorem packaging and a separately preregistered lane
falsifier; this probe alone cannot promote `K'=87`.

**Outcome:** arithmetic `PASS`, route wall. Modal app
`ap-D2TbRHCVUrcU61tRsOC4we` completed the probe, and the explicit-breakpoint
and independent vertex-enumeration LPs agree exactly in every stratum. The
simultaneous cap is
`26934334803635047410267405026838894905450545600`. Substitution leaves
premium `42322182171521728365206683472917703495213582545`, still above the
K'=87 leader by `861283046046284527325636787894941163714537850`. Capture
SHA-256: `e7a5bd7c42cf067f377aac6176d75c887f371c1c019b3e33fc9ee4bb2eb6e76f`.

Thus the valid shared-stratum consequence is weaker on this witness than the
existing strongest adjacent-pair option. It is retained as an exact route
cut and does not authorize a lane scan. The next candidate should retain the
raw global support-4 and support-5 caps inside the fixed-union `(4,5)`
stratum LP instead of applying them only after the weighted pair cap has been
collapsed.
## Preregistered K'=87 raw-clipped support-4/5 witness probe

- **decision:** test the proved `(36,5)` support-4/5 stratum inequalities
  after imposing the witness's global raw support-4 and support-5 caps before
  the weighted optimization is collapsed
- **scope:** one exact support-disjoint counterexample; no residual lane scan
- **probe SHA-256:**
  `fa24a164437f518ff5a441ccd03bd68e1aedc3b50e20045ade278a45d50f9293`
- **dispatcher SHA-256:**
  `eea1153b5436678bcc3d946d0d1ee5e6dcd54a21fdab82720813f94525d01bfa`
- **K'=87 witness adapter SHA-256:**
  `a66f4235d0651bd35d3ccbe749beb6ea5f52c6b2198bc1460bf13f3fe7907a00`
- **base witness analyzer SHA-256:**
  `44faccd0305d374557650c8bfc3b40f3aaa97717e46b154568cbadb3ec77bf3a`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one CPU, 256 MB, 20-second child wall and 30-second container
  wall; projected cost below `$0.01`
- **local safety:** one RAM-guarded Modal client; no local mathematical run

The primary implementation fixes the total support-4 count, fills uncoupled
strata first, and allocates the coupled count in increasing loss ratio. The
audit independently fixes total support 5 and allocates in the reverse dual
order. Both use exact rational arithmetic and must agree on the optimum and
the two aggregate counts. The raw selected-incidence caps are converted to
circuit caps by flooring against their exact extension factors, matching the
normalization already used by the proved adjacent-support router.

`PASS` requires exact agreement and prints the repaired witness price. A
nonpositive margin is a route wall. A positive margin authorizes packaging
the clipped fixed-union theorem and a separately preregistered offset-1
falsifier. This one-witness probe cannot promote `K'=87`.

**Outcome:** arithmetic `PASS`, route wall. Modal app
`ap-cCC7w2ZcDACsgqKNJS19Ij` completed the probe. The support-4-oriented and
support-5-oriented exact optimizers agree on cap
`15826982470121619978034510012906276872113956680`. The repaired premium is
`41987945497536424020866493137524475559167409625`, still above the K'=87
leader by `527046372060980182985446452501713227668364930`. Capture SHA-256:
`4f3bef9931e692f12b85432719730f433fcb0603cf894982c06a5e9458895120`.

The clipped support-4/5 route is therefore insufficient and does not
authorize a lane scan. The exact support-4 raw cap is active at the optimum,
so the clipping is nonvacuous; however, the witness's stronger existing
single edge is support 5/6. The next bounded action is the analogous
raw-clipped support-5/6 stratum LP for the `(34,6)` charge.
## Preregistered K'=87 raw-clipped support-5/6 witness probe

- **decision:** test the proved `(34,6)` support-5/6 stratum inequalities
  after imposing the witness's global raw support-5 and support-6 caps before
  weighted aggregation
- **scope:** one exact support-disjoint counterexample; no residual lane scan
- **probe SHA-256:**
  `d6dce1376dd21fb148eda763cecddca3e73ac1d7a81418c087e85fa8d4548d00`
- **dispatcher SHA-256:**
  `1e27476d06856eb3faf2983257ab401574143d59d860f55039723003c9019e68`
- **K'=87 witness adapter SHA-256:**
  `a66f4235d0651bd35d3ccbe749beb6ea5f52c6b2198bc1460bf13f3fe7907a00`
- **base witness analyzer SHA-256:**
  `44faccd0305d374557650c8bfc3b40f3aaa97717e46b154568cbadb3ec77bf3a`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one CPU, 256 MB, 20-second child wall and 30-second container
  wall; projected cost below `$0.01`
- **local safety:** one RAM-guarded Modal client; no local mathematical run

The primary implementation fixes total support 5 and allocates its coupled
strata in increasing support-6 loss ratio. The audit fixes total support 6
and traverses the reverse dual allocation. Both use exact rational arithmetic
and must agree on the weighted optimum and both aggregate counts. The raw
selected-incidence caps are normalized by their exact extension factors as
in the proved adjacent-support router.

`PASS` requires exact agreement and prints the repaired witness price. A
nonpositive margin is a route wall. A positive margin authorizes theorem
packaging and a separately preregistered offset-1 falsifier. This one-witness
probe cannot promote `K'=87`.

**Outcome:** `PASS` with positive margin. Modal app
`ap-0M46E2HegLDfuwCNvdJTUm` completed the probe. The support-5-oriented and
support-6-oriented exact optimizers agree on cap
`14207926136094898913594751174330524101924656533`. The repaired premium is
`39531805787455558517198440263313445158726451351`, below the K'=87 leader by
`1929093338019885320682606421709317172772593344`. Capture SHA-256:
`3f5c2073ae746ba1c546fbc49afa09941280438c94989b9f614bf812a8f42eab`.

The witness's exact raw support-5 count is active at the optimum, so the
pre-aggregation clipping is genuinely stronger than the previously deployed
support-5/6 cap. This repairs one witness, not the row. The next action is to
package the generic raw-clipped adjacent-support theorem with an independent
verifier, then preregister a paired offset-1 falsifier using it.
## Preregistered K'=87 raw-clipped offset-1 falsifier

- **decision:** exhaust offset 1 using the proved raw-clipped support-5/6 cap
  on every eligible carrier, combined only with support-disjoint adjacent
  edges
- **scope:** paired primary and independent traversals of offset 1; no other
  residual offset
- **generic clipped evaluator SHA-256:**
  `514cbeabc44f04ea4e153415dcddab1878069cefeaa12dea931f60edf9c0e18a`
- **charge-retaining traversal core SHA-256:**
  `ea0cc3fc67e7079a34a0bbabbe8c5953b0791944f05bc64659d80c9470036c13`
- **primary adapter SHA-256:**
  `27e0eaa88d6238de3d86205ab907d2caa1f997212ad0ea2b9ea4533f7924f8d8`
- **independent adapter SHA-256:**
  `289ade06dfcb706efb8dcb020f20afe1ec9ccf25061d450438867ef2f59deb72`
- **dispatcher SHA-256:**
  `ab148aeea28ca762620ce24784e8e28c27a2f92a20bfeebe5d8294e570f2eb36`
- **checker SHA-256:**
  `21de7c78cbf9200fc01d506ce7fd3b389a6546df0285627ca4fe4a61a6018c8f`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** two jobs, one CPU and 256 MB each, 720-second child wall and
  735-second container wall; projected total cost below `$0.15`
- **local safety:** one `modal`-profile RAMguard client; no local enumeration

The primary adapter evaluates the clipped LP by fixing support 5; the audit
fixes support 6. For each profile, the resulting edge-5 cap is minimized with
the previously proved adjacent cap. The final optimizer enumerates only
support-disjoint edge subsets. No overlapping pair bounds are composed.

`FALSIFIED` requires a paired exact over-leader witness. `SURVIVED` requires
agreement on all 462,384 source units and every deduplicated carrier profile.
`INCOMPLETE` retains partial checkpoints and changes no status. Survival
authorizes a separately preregistered complete offsets-`1..43` wave; this
campaign alone cannot promote `K'=87`.

**First deployment:** `INCOMPLETE`. Modal app
`ap-VqJehuBkAEPuuHaRhAYPg6` produced one complete primary survival and one
timed-out audit. The primary exhausted all 462,384 source units, all 23,104
raw-unsafe units, and 267,056 deduplicated profiles. The audit reached the
end of `m2=38` without a counterexample before its 720-second child wall.
Capture SHA-256:
`7fd211a2ca2a19de5f483eebcc69a29549e529cdaa713431b86645434f0f11ff`.

The primary result is retained, but this capture does not establish paired
survival and authorizes no full wave. A separately pinned cached audit resume
will rerun only the independent orientation under a longer Modal wall.
## Preregistered K'=87 clipped offset-1 audit completion

- **decision:** complete only the independent upper-oriented audit after the
  primary offset-1 traversal survived and the uncached audit timed out
- **starting capture SHA-256:**
  `7fd211a2ca2a19de5f483eebcc69a29549e529cdaa713431b86645434f0f11ff`
- **cached audit adapter SHA-256:**
  `9e4240355e5d5b1d59faf301d8087b63cf2fb2a1856d74f1551dc42e399f2296`
- **unchanged upper-oriented adapter SHA-256:**
  `289ade06dfcb706efb8dcb020f20afe1ec9ccf25061d450438867ef2f59deb72`
- **generic clipped evaluator SHA-256:**
  `514cbeabc44f04ea4e153415dcddab1878069cefeaa12dea931f60edf9c0e18a`
- **dispatcher SHA-256:**
  `1e8c9099c2485e7bc4d76e1dbd808fb1c80dfdbff4d363d3cea579ee25a69312`
- **merger/checker SHA-256:**
  `ce7f1b8ed7176434378bad780f6626a23fde00c50e30f92bb1333f2d89ad812d`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one CPU and 256 MB, 1,920-second child wall and 1,935-second
  container wall; projected cost below `$0.10`
- **local safety:** one `modal`-profile RAMguard client; no local enumeration

The cache changes no formula. It keys the exact upper-oriented cap by
`(union,dimension,raw5,raw6)` and reuses repeated rational evaluations across
deduplicated profiles. The merger accepts the earlier primary result only by
its pinned capture hash and requires exact equality of all terminal coverage
counts with the resumed audit.

`FALSIFIED` is a paired route wall only after comparison with the pinned
primary traversal. `PASS` requires both complete traversals to survive all
462,384 source units and 23,104 raw-unsafe units with equal profile counts.
`INCOMPLETE` changes no status.

**Outcome:** `PASS`. Modal app `ap-ce2sclOGAj09BOGbmk6i7Z` completed the
cached audit at 42 MB peak RSS with 34,051 exact cache entries. Resume-capture
SHA-256:
`da7e3ec56563f0af995a44fe7a264f5515b48ff759d18519593bc1d00f1d9831`.

The hash-pinned merger agrees with the original primary survival on all
462,384 source units, 23,104 raw-unsafe units, and 267,056 deduplicated
profiles. Offset 1 is therefore exhaustively paid by the raw-clipped theorem
in both orientations. This authorizes a separately preregistered paired wave
over every raw-unsafe offset `1..43`; it does not promote `K'=87` by itself.
## Preregistered K'=87 raw-clipped completion wave

- **decision:** exhaust every raw-unsafe offset with paired cached
  implementations of the proved raw-clipped adjacent-support router
- **scope:** offsets `1..43`, primary lower-oriented and independent
  upper-oriented traversals; 86 jobs total, below the account's 100-container
  limit
- **cached primary adapter SHA-256:**
  `dd652f005ee31ed3229bd16039f16a8961306fbfe21a45d95737406a3e716f31`
- **cached audit adapter SHA-256:**
  `9e4240355e5d5b1d59faf301d8087b63cf2fb2a1856d74f1551dc42e399f2296`
- **generic clipped evaluator SHA-256:**
  `514cbeabc44f04ea4e153415dcddab1878069cefeaa12dea931f60edf9c0e18a`
- **charge-retaining traversal core SHA-256:**
  `ea0cc3fc67e7079a34a0bbabbe8c5953b0791944f05bc64659d80c9470036c13`
- **dispatcher SHA-256:**
  `da4816e607f1eee7e9f7559ce3634e115350a7367a5d7e582d588b540a6158ff`
- **checker SHA-256:**
  `92caef3cb3872b2c75ffa91bad21e0a745f281c1b2a8590005b7632368bd3f5e`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one CPU and 256 MB per job, 900-second child wall and
  915-second container wall; projected total cost below `$1`
- **local safety:** one `modal`-profile RAMguard client; no local enumeration

Each implementation memoizes exact rational cap specializations but retains
its opposite allocation orientation. Every job emits per-slice progress and
either an exact paired counterexample or a complete survival. The merger
accepts `PASS` only if all 43 offset pairs agree, all 14,388,660 source units
and 511,677 raw-unsafe units are covered per implementation, and every
profile is at most the K'=87 leader.

`FALSIFIED` preserves every paired exact witness and blocks row promotion.
`INCOMPLETE` preserves completed jobs and changes no status. `PASS` closes
only the nonordinary post-carrier lane; the ordinary lane and exact component
payment remain separate obligations before `K'=87` can be promoted.

**First launch:** infrastructure `INCOMPLETE` before any remote job started.
Modal app `ap-CJGzce4t8apKw3zM04CRP9` stopped with local client error
`can't start new thread`. The WSL host already had about 376 live threads;
adding one dispatch thread per 86-job wave exceeded its local task headroom.
No mathematical result was produced and no capture is accepted. The identical
remote jobs will be sent as three sequential, hash-pinned shards of at most
30 jobs each.
## Preregistered K'=87 clipped completion shards

- **decision:** execute the unchanged 86-job clipped wave in three sequential
  shards to stay below the WSL client's thread ceiling
- **fixed shards:** offsets `1..15` (30 jobs), `16..29` (28 jobs), and
  `30..43` (28 jobs)
- **shard dispatcher SHA-256:**
  `ac42c17cc5b8f6c9b318cc07a43f2a300d9ab74e21936e4279ea0783d1e9860b`
- **shard merger SHA-256:**
  `660f99833062b5073393e0351d5b7067c47d2b8e77c3474715a377a6e974a964`
- **unchanged full-wave checker SHA-256:**
  `92caef3cb3872b2c75ffa91bad21e0a745f281c1b2a8590005b7632368bd3f5e`
- **cached primary adapter SHA-256:**
  `dd652f005ee31ed3229bd16039f16a8961306fbfe21a45d95737406a3e716f31`
- **cached audit adapter SHA-256:**
  `9e4240355e5d5b1d59faf301d8087b63cf2fb2a1856d74f1551dc42e399f2296`
- **envelope:** no more than 30 simultaneous Modal jobs, one CPU and 256 MB
  each, with the unchanged 900-second child wall; projected aggregate cost
  below `$1`
- **local safety:** shards launch sequentially under the `modal` RAMguard
  profile; no local enumeration

The merger validates each capture hash, exact shard boundary, job set, and
batch terminal before emitting one canonical 86-job capture. The original
full-wave checker then applies the unchanged mathematical acceptance
contract. Sharding changes only local dispatch concurrency.

`FALSIFIED`, `INCOMPLETE`, and `PASS` retain exactly the meanings in the
parent completion-wave preregistration. No shard result alone changes the
status of `K'=87`.

**First shard launch:** infrastructure `INCOMPLETE` before remote work.
Modal app `ap-Hh3xMzcVM9z85G3diycuXu` returned the same local
`can't start new thread` error for the 30-job first shard. The current WSL
task headroom is therefore below this dispatch size. No capture is accepted;
the unchanged shard dispatcher will be used with at most eight jobs per
launch.
## Preregistered K'=87 clipped completion microshards

- **decision:** dispatch the unchanged paired jobs in eleven sequential
  microshards of at most eight jobs
- **fixed offset partition:** `1..4`, `5..8`, `9..12`, `13..16`, `17..20`,
  `21..24`, `25..28`, `29..32`, `33..36`, `37..40`, `41..43`
- **unchanged shard dispatcher SHA-256:**
  `ac42c17cc5b8f6c9b318cc07a43f2a300d9ab74e21936e4279ea0783d1e9860b`
- **flexible contiguous merger SHA-256:**
  `2fc0c0408227dd3cfdf175304bfad6e7b13a77782d33a4a4041b8ff1f8fd12dd`
- **unchanged full-wave checker SHA-256:**
  `92caef3cb3872b2c75ffa91bad21e0a745f281c1b2a8590005b7632368bd3f5e`
- **envelope:** at most eight simultaneous Modal jobs, one CPU and 256 MB
  each; shards launch sequentially and retain the 900-second child wall;
  projected aggregate cost below `$1`
- **local safety:** one small dispatch client at a time under the `modal`
  RAMguard profile

The merger reads each shard's own `(start,end)` terminal, verifies every
capture hash and exact paired job set, proves that the ranges form a
nonoverlapping contiguous partition of `1..43`, and emits the canonical
86-job capture consumed by the unchanged checker. This is an infrastructure
repair only; all mathematical source hashes remain those of the parent wave.

**Observed launches.** Offsets `1..4` completed under Modal app
`ap-iXONaPwRxMHjwZR515sOyi`; both implementations survived all four offsets,
the batch terminal is complete, and the capture SHA-256 is
`544b603dac9fd1ea858c36e530bb0263f6e11392a6d3b284d3baa1c266b9f7ca`.
The next `5..8` launch, app `ap-tSoaoDf3sggiySe7XlduCG`, failed in the local
Modal client with `can't start new thread` before remote work. No capture from
that launch is accepted. Since even eight simultaneous dispatch calls are
not reliable at the current WSL thread ceiling, the remainder moves to the
two-container range protocol below.
## Preregistered K'=87 clipped completion ranges

- **decision:** retain the completed paired offsets `1..4`, then process the
  remaining offsets in five sequential ranges with exactly two remote
  workers per range
- **fixed remaining ranges:** `5..12`, `13..20`, `21..28`, `29..36`,
  `37..43`
- **range dispatcher SHA-256:**
  `97354bbbb4d1900e022028b569a46de00799f9724d79697e4281deb22cef1494`
- **flexible contiguous merger SHA-256:**
  `2fc0c0408227dd3cfdf175304bfad6e7b13a77782d33a4a4041b8ff1f8fd12dd`
- **unchanged full-wave checker SHA-256:**
  `92caef3cb3872b2c75ffa91bad21e0a745f281c1b2a8590005b7632368bd3f5e`
- **pinned completed range:** offsets `1..4`, capture SHA-256
  `544b603dac9fd1ea858c36e530bb0263f6e11392a6d3b284d3baa1c266b9f7ca`
- **envelope:** exactly two simultaneous Modal containers per launch, one
  primary and one independent audit, each with one CPU and 256 MB; offsets
  execute sequentially inside each container with the unchanged 900-second
  child wall and 7215-second range wall; projected aggregate cost below `$1`
- **local safety:** one two-call Modal dispatch client at a time under the
  `modal` RAMguard profile; no local enumeration or many-call fanout

Each remote worker emits the unchanged per-offset `JOB_RESULT` records. The
range terminal is accepted only when both implementations return one complete
result for every assigned offset, with exit zero and peak RSS at most 128 MB.
After all five launches, the existing flexible merger verifies capture hashes,
paired job sets, and the exact contiguous partition `1..43`; the unchanged
full-wave checker then applies the preregistered mathematical acceptance
contract. This changes dispatch topology only. It does not weaken the paired
independence, completeness, resource, or numerical criteria.

**Observed launches.** Range `5..12` completed under Modal app
`ap-dJ2eUU9a0u0jcJjXZiefIU`; both implementations survived every offset and
agreed exactly, with peak RSS `39..43` MB. Its capture SHA-256 is
`4f3f1d9e5f81aa3f8afdb3727d266eaa9f557ad2140b9d8b1c469919785918dd`.
The first `13..20` attempt, app `ap-Lgc9MUPG1puo4Eua60ex2D`, failed in the
local Modal client with `can't start new thread` before creating remote
objects. No capture from that attempt is accepted. Intermittent failure at
two calls motivates the one-call transport below.
## Preregistered K'=87 clipped completion single-call ranges

- **decision:** preserve the accepted offsets `1..12`, then execute each
  remaining fixed range through one remote Modal call
- **fixed remaining ranges:** `13..20`, `21..28`, `29..36`, `37..43`
- **single-call dispatcher SHA-256:**
  `56353323d5f4f322a9f26a6602228bd6245773d6a48979e3be2f7a39af4d38be`
- **flexible contiguous merger SHA-256:**
  `2fc0c0408227dd3cfdf175304bfad6e7b13a77782d33a4a4041b8ff1f8fd12dd`
- **unchanged full-wave checker SHA-256:**
  `92caef3cb3872b2c75ffa91bad21e0a745f281c1b2a8590005b7632368bd3f5e`
- **accepted prefix captures:** offsets `1..4` at
  `544b603dac9fd1ea858c36e530bb0263f6e11392a6d3b284d3baa1c266b9f7ca`;
  offsets `5..12` at
  `4f3f1d9e5f81aa3f8afdb3727d266eaa9f557ad2140b9d8b1c469919785918dd`
- **envelope:** one Modal container per launch, one CPU and 256 MB; primary
  and independent-audit children execute sequentially with the unchanged
  900-second child wall and a 14415-second range wall; projected aggregate
  cost below `$1`
- **local safety:** one synchronous Modal remote call under the `modal`
  RAMguard profile; the client inherits a 2 MB thread-stack soft limit while
  retaining RAMguard's 1536 MB address-space ceiling; no local enumeration,
  starmap, or concurrent dispatch

The remote container runs the unchanged primary and audit source files as
separate subprocesses and emits the same per-offset records. Sharing transport
does not share implementation state: each child starts a fresh interpreter,
constructs its own cache, and is hashed separately. Acceptance still requires
both implementations at every offset, exact count agreement in the unchanged
full-wave checker, exit zero, no timeout, and peak RSS at most 128 MB. The
single-call protocol changes only the local Modal client's thread demand.

**First single-call launch:** infrastructure `INCOMPLETE` before remote work.
Modal app `ap-vFYKr9rxnNXfxQ7m8XpvLQ` initialized but the local client again
returned `can't start new thread` before creating objects. No capture is
accepted. Inspection showed that this WSL host uses RAMguard's `prlimit`
fallback: the client has a 1536 MB virtual-address ceiling and an inherited
8 MB stack reservation per thread. The retry retains the address-space
ceiling and lowers only the inherited stack soft limit to 2 MB via
`prlimit --stack=2097152`. This transport adjustment does not alter remote
resources, source hashes, range boundaries, or acceptance criteria.

**Outcome:** `PASS`. The accepted range captures are:

| Offsets | Modal app | Capture SHA-256 |
|---|---|---|
| `1..4` | `ap-iXONaPwRxMHjwZR515sOyi` | `544b603dac9fd1ea858c36e530bb0263f6e11392a6d3b284d3baa1c266b9f7ca` |
| `5..12` | `ap-dJ2eUU9a0u0jcJjXZiefIU` | `4f3f1d9e5f81aa3f8afdb3727d266eaa9f557ad2140b9d8b1c469919785918dd` |
| `13..20` | `ap-xr0f01RFscUvWkrGvn7VGk` | `1406c04aef22bfa96037221ebb6c47a94258fb3e54014e117a5b9a6090dba2fb` |
| `21..28` | `ap-qFATW8MSFF0dzBoqm4ekA9` | `ee4c260ba13112abd17f02d37957c5eae131c713cc1f51254a9e2387b65cfc0c` |
| `29..36` | `ap-KzzGy55iKSUXT04uVv7UOh` | `28bbc2311b0845e7deba6b8e5f4cacdafb32ed65d5b9057871ac043aab98b55b` |
| `37..43` | `ap-TLGJytlHAZRLOm0pn0e8Oh` | `e9d41feff81a9e2e809b54bcb80c2c802c6d2c140d9481bc8f527a5f5b9df784` |

The flexible merger accepted the exact contiguous partition `1..43` and
emitted canonical capture SHA-256
`6f8064320850e0009c18c967e2b61ec5b4d77c51e1c2afb4bee6fc41921e5cd8`.
The unchanged full-wave checker reports 86 jobs, 43 offsets, 14,388,660
source units, 511,677 raw-unsafe units, and 77,179,660 carrier profiles per
implementation. Primary and independent audit agree exactly; all offsets
survive and no falsifying witness remains. Observed peak RSS was `31..45` MB.

This closes the K'=87 nonordinary clipped-support residual. It does not by
itself promote the row: the ordinary lane and exact component payment remain
separate required gates.
## Preregistered K'=87 ordinary-lane payment

- **decision:** replay the complete ordinary lane through the pinned primary
  and independent K'=83 routers after substituting only the K'=87 row data
- **primary adapter SHA-256:**
  `a9382db987ce51906dedd510d028ebf688a141455c147f617bda60a7c9b334c9`
- **audit adapter SHA-256:**
  `338d35ca79a5a54e6c869f913bf4a25f52e1cd0351b20ce3df3142494c735af3`
- **single-call dispatcher SHA-256:**
  `fce317eda0003bef6d515484f636b54d497cb6158a26907de13f7de4d3674565`
- **checker SHA-256:**
  `60fde0ea89ffccb94f61c9fd824faa5656ad2689af4c532d6aaea62a7131cdff`
- **hash-pinned K'=83 code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one Modal container, one CPU and 1 GB; fresh primary and
  audit subprocesses execute sequentially with 900-second child walls and an
  1815-second container wall; projected cost below `$0.20`
- **local safety:** one synchronous client under the `modal` RAMguard profile
  and a 2 MB inherited thread-stack limit; no local enumeration

The adapters set `K'=87`, `q=77`, `m'=67559`, and `n'=1048663`, then derive
the exact safe premium ceiling from the pinned ledger. The checker requires
both subprocesses to finish below 128 MB RSS and to agree exactly on source
units, raw rows, raw-safe units, expanded units, geometry rows, premium,
margin, and normalized active branch. It independently checks the seven-row
high-stratum multiplicity and recomputes safety from the printed ceiling.

```text
PASS:       paired exact agreement and nonnegative ordinary margin;
UNSAFE:     paired exact agreement but negative ordinary margin;
INCOMPLETE: timeout, resource breach, malformed output, or disagreement.
```

Only `PASS`, combined with the completed clipped nonordinary wave and a
strict exact component gap, permits a K'=87 proof-node promotion.

**Outcome:** `PASS`. Modal app `ap-t1IWAsyDidGwq0ZwwYO6yI` completed both
fresh subprocesses at peak RSS `33..37` MB. Capture SHA-256:
`06a550c1f65be3c2a7c4d96590188f5de6ca792c1f87e638f2fa7d5163b43519`.
The checker reports exact paired agreement on 542,840 source units, 3,799,880
raw rows, 121,895 raw-safe units, 4,385 expanded units, and 2,940,875 geometry
rows per implementation. The ordinary premium is
`41460244206367810395288131753780101229368111530`, below the safe ceiling by
`670462675256690016910468032334996708331859`. It is also strictly below the
clipped-wave leader, so it does not change the candidate global premium.
## Preregistered K'=87 exact component payment

- **decision:** insert the larger of the certified ordinary and nonordinary
  premiums into the pinned rank-nine component ledger and require a strict
  positive incidence gap
- **certified premium:**
  `41460899125475443837881046685022762331499044695`
- **payment script SHA-256:**
  `1e154be116c33854af85a5a01fd03e4a3c4e0b66d1e24bc1fe58c9f2f9c62713`
- **Modal dispatcher SHA-256:**
  `c8e111c4c1bdc4f62f56598f3a7fa56615f4ca09d1c9bbf580c29b7e9ea483ab`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one Modal container, one CPU and 256 MB, 30-second wall;
  projected cost below `$0.01`
- **local safety:** one synchronous client under the `modal` RAMguard profile
  and a 2 MB inherited thread-stack limit; no local calculation

The script independently derives the row marks, kernel capacity, record floor,
safe premium ceiling, full-rank capacity, required incidence, and strict gap
from the pinned ledger. It accepts only the exact K'=87 row and asserts both
the known ceiling margin
`15543567623247423995536789673894577398694` and a strictly positive component
gap. No rounded or floating-point quantity is used.

`PASS` authorizes construction and adversarial replay of the K'=87 proof node.
`INCOMPLETE` or a nonpositive gap leaves the row open.

**Outcome:** `PASS`. Modal app `ap-JAw6W5GHktZA9TXLxcpMUY` reconstructed the
exact row; capture SHA-256:
`883f659486162495750adbc80c97d3224cdae6b3bdebf3429492a33189d95312`.
The certified premium is below the exact safe ceiling by
`15543567623247423995536789673894577398694`. Total capacity is
`921060890011284709657056363808900069597352462765767795701103981`
against required incidence
`921060967723676391242250303252610946492991464556444164407248882`,
leaving strict component gap
`77712391681585193939443710876895639001790676368706144901`.
## Preregistered K'=88 raw-threshold offset envelope

- **decision:** classify every positive support-2/3 offset at the first open
  rank-nine row before funding any carrier-geometry wave
- **scope:** offsets `1..77`, paired primary and independently ordered scans
- **K'=88 adapter SHA-256:**
  `be5bf4f9ef32c9382f7c2e82d5bf9c9dd2317552b50d6521db794486563233f9`
- **dispatcher SHA-256:**
  `83cf6ac023747bf13c7cbb5baee04df0a6969edea7e8941659595ccd16df9679`
- **merger SHA-256:**
  `768fe2e7648efe6db0359c439ee46ba537c0939c9864ed629311301ae0438653`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** 154 jobs, one CPU and 256 MB each, 165-second child wall
  and 180-second container wall; no local mathematical enumeration

The adapter changes only `K'=88`, `q=78`, `m'=67560`, `n'=1048664`, and
the derived exact ceiling. Acceptance requires every job below 128 MB,
complete primary/audit agreement, and exact coverage

```text
sum_{d=1}^{77} (78-d) * 79^2 = 18,741,723.
```

`PASS` is an exact finite classification, not a row payment.
`INCOMPLETE` retains partial output and changes no mathematical status.

**Outcome:** `PASS`. Modal app `ap-fMO9ZkjfNolEyDBKhvmVL0` completed all
154 jobs at peak RSS 32 MB. Capture SHA-256:
`b06e4333df414db0cd898a20b17a75fc0e624c52456036682798cfab9742bb8d`.
The paired merger certified exact agreement on 18,741,723 source units and
131,192,061 raw rows per implementation.

```text
raw-safe units       18,118,828
raw-unsafe units        622,895
unsafe offsets              1..44
fully safe offsets          45..77
```

The exact raw-safe leader is offset 30,
`s2=74/s3=44/s4=59/s5=37/offset30/c6F/c7F/c8F/c9F`, with premium
`41484929797626437211705768761745630928736846700`. It is below the exact
safe ceiling by `3285081868187689871277591965202642736154`. The remaining
row obligation is a finite 622,895-unit raw-clipped carrier payment.
## Preregistered K'=88 raw-clipped stress

- **decision:** test the proved raw-clipped adjacent-support theorem at four
  route-deciding K'=88 offsets before considering a complete residual wave
- **ordered scope:** offsets `1` (largest residual), `22` (interior), `30`
  (raw-safe leader), and `44` (last raw-unsafe lane)
- **primary adapter SHA-256:**
  `402274ed8f4aede86b091a08ffcf500e72139653f154fd2113481d7780e60ecc`
- **independent adapter SHA-256:**
  `ee48fe44cbd5a8af0783d3be097439eb6727c73d63e4a4ab5738a39603f47d7c`
- **shared traversal core SHA-256:**
  `8c549dde77e560a21fb4dac67eec29ccf642ac861475b89ceb59d3ba57acb4ca`
- **dispatcher SHA-256:**
  `df170f0abd75c3871cdb42199e6108df477d6f7af6aec16594575e4d1be8be94`
- **checker SHA-256:**
  `b68e84202dae1c974f7126c1e1c7af4bd3056d739c1b1b2acf5f6e6d8676f4d1`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** eight jobs, one CPU and 256 MB each, 900-second child wall
  and 915-second container wall; projected total cost below `$0.20`
- **local safety:** one RAM-guarded Modal client; no local enumeration

The adapters substitute only `K'=88`, `q=78`, `m'=67560`, `n'=1048664`,
the derived exact ceiling, and the exact raw-safe offset-30 leader. They use
the two proved orientations of the raw-clipped theorem. A paired offset-44
deployment smoke must pass before the eight-job stress.

`FALSIFIED` requires the same exact over-leader witness from both theorem
orientations. `PASS` requires paired survival on all four offsets, exact
coverage of 1,341,815 source units and 51,707 raw-unsafe units, and no
over-leader carrier profile. `INCOMPLETE` includes timeout, malformed output,
resource breach, or disagreement and changes no mathematical status.
Survival authorizes a separate value assessment; it neither launches a full
wave automatically nor promotes `K'=88`.

The paired deployment smoke passed as Modal app
`ap-9SV6VYgvGX2ncNqkXrZ1d2`. Primary and independent orientations agree on
all 212,194 offset-44 source units, all 195 raw-unsafe units, and 202,207
carrier profiles. Both return `SURVIVED`; peak RSS was 32--37 MB. Capture
SHA-256: `04fe3e31de6b38ea3923c68ddbb782fb168267248245f19105e4c470ed67e31e`.
This authorizes the preregistered eight-job stress and has no standalone
mathematical status effect.

**Outcome:** `FALSIFIED`. Modal app `ap-wRAeaUK4rE5XK6sVdD5Ks4` completed
all eight jobs at peak RSS 32--45 MB. Capture SHA-256:
`728042953d357095b0defbde413041d683a9d40b5fe8e53288ba27d218df8bc2`.
Offsets 22, 30, and 44 survive exhaustive paired scans; both orientations
return the same first offset-1 witness:

```text
m2=32, m3=33, s2=46, s3=45, s4=45, s5=44
case=F23__N4_t0__N5_t2
charges=(38,6),(38,6), high=c6F/c7F/c8F/c9F
```

Its raw premium is
`49355312964508839635000536009148053954853701245`. Support-5/6 raw clipping
leaves `41549359934887745801059698148276349327209870125`, above the exact
raw-safe leader by `64430137261308589353929386530718398473023425`. The direct
K'=87 raw-clipped continuation is therefore blocked, and no complete K'=88
clipped wave is authorized.
## Preregistered K'=88 dual-adjacent offset-1 repair

- **decision:** test whether independently raw-clipping both available
  adjacent edges repairs the exact offset-1 witness left by the support-5/6
  scanner
- **scope:** the complete offset-1 lane, paired theorem orientations
- **primary adapter SHA-256:**
  `db58a642cd1cab29df1d356411fdf100b6cd5b7a8b8b58fde21b484799daeda1`
- **independent adapter SHA-256:**
  `78e7790c8b2f2eae87958c4716c9da67a44dbc8dd7b7a3e82cbc27143028b0cc`
- **dispatcher SHA-256:**
  `81e0b284c92ad5bbfb2afa059c4e7deb389dfeea7e9a9747411f20297bbfa21c`
- **checker SHA-256:**
  `8bdb851101b369e4d621243ba9234bc3500beb1ec674b29a6315533d9ebb0a2d`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** two jobs, one CPU and 256 MB each, 900-second child wall
  and 915-second container wall; projected total cost below `$0.10`
- **local safety:** one RAM-guarded Modal client; no local enumeration

For each fixed-union charge the primary adapter applies the proved lower-
oriented raw-clipped theorem separately at lower supports 4 and 5; the audit
uses the independently derived upper orientations. The resulting support-4/5
and support-5/6 edge caps enter the existing router as alternatives. Because
the edges overlap at support 5, they are never composed.

`FALSIFIED` requires an identical exact over-leader witness from both
orientations. `PASS` requires paired agreement on all 480,557 offset-1 source
units, all 27,562 raw-unsafe units, and every carrier profile. `INCOMPLETE`
changes no mathematical status. This probe tests one minimal repair only; it
cannot promote `K'=88` or authorize a complete wave by itself.

**Outcome:** `FALSIFIED`. Modal app `ap-aTuDyBgYFIDDAPQ92IvcS5` completed
both jobs at peak RSS 58--62 MB. Capture SHA-256:
`594c93e9528066be44fa3ab62115eb696a8c0e465fc01a7d65e6f4419d542ee1`.
Both orientations return the same offset-1 witness as the support-5/6
stress after 197,071 source units, 14,986 raw-unsafe units, and 216,326
carrier profiles. Independently raw-clipping support 4/5 lowers the repaired
premium by

```text
4547111877997214766571212941786435342449200,
```

but the resulting
`41544812823009748586293126935334562891867420925` still exceeds the leader
by `59883025383311374587358173588931963130574225`. Independent overlapping
adjacent-edge alternatives are therefore insufficient. The next finite
repair would need a proved joint support-4/5/6 cap or a different carrier
charge; neither is claimed here.
## Preregistered K'=88 joint raw-clipped 4/5/6 witness probe

- **decision:** decide whether a genuine three-support fixed-union LP can
  repair the exact witness that defeats both independent adjacent edges
- **scope:** one printed offset-1 witness, one fixed-union charge `(38,6)`
- **probe SHA-256:**
  `10fc0f244b87978bc0e479ca9409dd5ce004f6a6d4d1d121a6e0eb444de81ecf`
- **dispatcher SHA-256:**
  `d7ddd4e827f2ea8f8001441637e6f5da8b2539cb1452c2a8f537b6f13367ce7d`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one CPU, 512 MB, 105-second child wall and 120-second
  container wall; projected cost below `$0.02`
- **local safety:** one RAM-guarded Modal client; no local solve

The 14 nonnegative variables are the three support-4 strata, four support-5
strata, four support-6 strata, and three direct strata. The constraints are
both fixed-union incidence families, the exact direct caps, and the three
global raw circuit caps. Thus support 5 is shared inside one LP rather than
charged independently to overlapping adjacent edges.

This first probe deliberately uses floating-point HiGHS dual-simplex and
interior-point algorithms only to decide whether exactification is worth
pursuing. `PROMISING` requires both algorithms to agree well inside the
leader; `DEAD` means the estimated optimum remains above the leader;
`INCONCLUSIVE` includes solver disagreement or a near-zero margin. No output
from this probe is proof evidence, and it cannot move DAG status. A promising
result must be reconstructed as an exact rational primal/dual certificate
with an independent verifier before entering any theorem or larger scan.

**Outcome:** `DEAD` as a heuristic route. Modal app
`ap-meBQmnvkmsD3FoYCpUtHPJ` completed in 5.06 seconds at 182 MB peak RSS.
Capture SHA-256:
`f07bab7fc16b5917c0bee80d32325beeb73882ae177d316575228c031a394e47`.
Dual simplex and interior point return the same objective estimate. The
resulting repaired premium is approximately
`46573494499935690501632509827776156475058710877`, above the leader by
approximately `5088564702309253289926741066030525546321864177`.

This separation is decisive for route selection, so no exactification or
larger scan is warranted. The values remain floating-point heuristic output
and are not promoted as a theorem, proof node, or falsification of any
asserted DAG claim.
## Preregistered repeated-BC cell-11 guard-boundary classifier

- **decision:** determine whether the remaining registered function-field
  guards support any original guarded cell-11 source point
- **scope:** the complete 15-polynomial `BC+` and 27-polynomial `BC-` guard
  atlases already emitted by the sealed 720-case uncolored rank census
- **classifier SHA-256:**
  `028de7a757f27fa5179c9b79d0c41d194093b008e482f84493884cd98146f105`
- **core SHA-256:**
  `336aace4780acce09d9cb53cc969635d16a038af0a5379338a746e086758aac7`
- **tower SHA-256:**
  `e80940956518b958dafe74eb34e8ce4f00ce729e78646203bb0724057e6f7899`
- **principal-input SHA-256:**
  `a9c3f10fc7e368f88599bce085598d641d0a73352a1f7d54e06abcd9b4aabbf7`
- **guard-atlas SHA-256:** `BC+`
  `8f7e84f601514685dbb0079ec8f5b9851e5e051602dd815d06a82e0c34c8d1ec`,
  `BC-`
  `bae6700ba440c027ff97c40188f5fa6d33b82ad38183fffc3c70222ae84518c3`
- **envelope:** eight independent one-CPU workers, 1 GiB each, 120-second
  worker wall; projected cost below `$0.10`
- **local safety:** one RAM-guarded Modal client; no local factorization or
  source-fiber solve

Each worker factors the complete guard atlas for one source-sign/tower row.
Every deployed linear root is either assigned to the already-proved symmetric
tower chart boundary or lifted through the exact `x=bc`, `y=b+c` tower. Every
lift is replayed against the original six common equations and original
source guard from the principal-input certificate.

`NO_GUARDED_GUARD_BOUNDARY_POINT` on all eight rows authorizes an exact
cell-11 guard-complement theorem after an independent verifier is written.
`GUARDED_GUARD_BOUNDARY_PRESENT` produces the complete finite source-point
packet for direct outside replay. `REMOTE_ERROR` preserves all completed row
shards and authorizes only the failed rows to be resumed. No numerical or
generic conclusion can move DAG status.

**Outcome:** `GUARDED_GUARD_BOUNDARY_PRESENT`. Modal app
`ap-3TLwrDgciRiO4GZRVuf9HS` completed all eight rows. Result SHA-256:
`e01e1a6ceaf55f530c0bd62549c9d64b18e5eeacc5a95be24c543c18f6fbcac5`.
There are 160 guarded source points: 128 on the four `BC-` towers and 32 on
the four `BC+` towers, supported over six and two base values respectively.
Thus the registered guards are genuine specialized fibers, not merely
function-field pivot artifacts. The pre-registered consequence is the direct
finite outside replay below; no exclusion or DAG status change follows from
this classifier alone.
## Preregistered repeated-BC cell-11 guard-boundary direct replay

- **decision:** determine whether any of the 160 exact guarded boundary
  source points supports a colored or uncolored missing-record packet
- **scope:** all eight repeated-BC cell-11 source towers; missing `BE`, `CF`,
  `DE+`, `DF+`, and `EF`; both outside signs and all fifteen residual
  matchings where applicable
- **replay SHA-256:**
  `40639f55d76c628b28982d52bd1cb7751f33fceb5de035d98a7649ba89681617`
- **boundary packet SHA-256:**
  `e01e1a6ceaf55f530c0bd62549c9d64b18e5eeacc5a95be24c543c18f6fbcac5`
- **envelope:** eight independent one-CPU workers, 1 GiB each, 120-second
  worker wall; projected cost below `$0.10`
- **local safety:** one RAM-guarded Modal client; no local root extraction or
  packet enumeration

The replay reconstructs the common-kernel cofactors directly over
`F_2130706433` from each printed `(b,c,r,t)` point. It does not specialize the
function-field quotient algebra whose construction guard vanishes. The
missing product and squared sum are then used in two exact tests:

1. direct consistency for colored missing `BE` and `CF`;
2. exhaustive base-field endpoint roots for each uncolored missing record,
   followed by all three paired-product equations for both outside signs and
   all fifteen matchings.

`DIRECT_BOUNDARY_EXCLUDED` on all eight rows, zero denominator failures, and
an independent pure finite-field verifier authorize a PROVED registered-guard
boundary exclusion node. `DIRECT_BOUNDARY_CANDIDATE_PRESENT` prints every
candidate and sends only that finite packet to the original raw-system
replay. `REMOTE_ERROR` authorizes resumption of failed rows only. A candidate
is not by itself a counterexample: distinctness and the full raw cell system
remain downstream checks.

**Outcome:** `DIRECT_BOUNDARY_EXCLUDED` on all eight rows. Modal app
`ap-N2SEkWDjWZRMukWgjlgrHL`; result SHA-256:
`9b7f9907253e05c2d197b1e126962d3a8c9bc563be0e315353b368d47bd9efb0`.
The replay covers 160 source points, 320 colored cases, and 34,560 uncolored
formal endpoint/matching cases, with zero denominator failures and zero
candidates. The independent pure modular verifier reproduces every common-
kernel value and finds a constant three-equation gcd in all 34,560 uncolored
cases. The registered-guard boundary exclusion is therefore promoted in its
own PROVED DAG node; cell-11 assembly and cell-14 transport remain separate.
## Preregistered O0b split cell-0 component outside pilot

- **decision:** test the changed O0b outside ideal on a complete stratum
  subcover before authorizing the 708-representative campaign
- **scope:** 24 canonical representatives covering all 56
  `component/lane-orbit/outside-sign/missing-record` strata
- **launcher SHA-256:**
  `04ae51440703ad0116e33ce6a4c7f3312eff748cd8c3fa1a1d326c4d465f5d48`
- **checker SHA-256:**
  `74770cfadbfa1275fe58fbee187b40e00cea8e8526ff3dc07347a8011c8046b5`
- **outside-core SHA-256:**
  `5cd86020b601b68e9a4295d55d057ec0e029dede334397e6bc51f9d840e5561f`
- **representative manifest SHA-256:**
  `658ae5f1f3c0667df2cece818e0c89a752ce9cdf7c4f6f421fc4a721134b8fa4`
- **pilot representative-list SHA-256:**
  `47ef7c3a9a92ac2bcb08462377195c0576c2495b0ff1f7c0948103d10e02bc27`
- **component certificate SHA-256:**
  `2fd2d65ebd033d8cd784f428d31d9b49eb66c4b6a059326ed7efcd60d53ed100`
- **envelope:** at most 24 one-CPU workers, 2 GiB each, 180-second
  Singular child wall and 210-second container wall; conservative campaign
  wall below five minutes and projected cost below `$0.20`
- **local safety:** one RAM-guarded Modal client under a 300-second external
  hard stop; exact CAS work is remote and each returned row is checkpointed

The PROVED component router reduces the complete equal-sign ledger from
2,520 component cases to 708 representatives. Its pilot subcover contains
one orbit representative whose orbit meets each of the 56 coarse strata.
Each worker imposes the exact component relation, missing-product equation,
three paired-product resultants, missing squared-sum equation, and all source,
denominator, leading-support, and target-distinctness guards. The pure outside
core fixes the O0b record order `BE,CF,DE+,DE-,DF+,DF-,EF` and the two
repeated-lane variants.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 300s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_cell0_component_outside_modal.py \
  --scope pilot
```

`PILOT_ALL_UNIT` requires 24/24 `COMPLETE` rows, unit saturated ideals, exact
case hashes, and checker acceptance; it authorizes preregistration of the full
708-case campaign but has no theorem or DAG-status effect. Any complete
nonunit row is retained with its six generators and complete guard list for
route analysis. `TIMEOUT`, `ERROR`, `REMOTE_ERROR`, client interruption, or
an incomplete checkpoint is `INCOMPLETE` and authorizes only a bounded repair
or resumption. No pilot outcome closes cell `0`.

The first deployment smoke, Modal app `ap-6GEKxb3H9szvhPpQ0AyIIo`, is
`INCOMPLETE`: all 24 rows returned `REMOTE_ERROR` before CAS startup because
the validated pure outside core was not mounted into the remote image. The
checkpoint SHA-256 is
`a68188167e669240aff40d5df0cfc389eee8c2459d8438922ba6163b48f97c61`.
No row reached Singular and the run has no mathematical status. Launcher
`04ae5144...` adds the missing immutable core mount; all case, solver, wall,
and outcome contracts are unchanged for the bounded rerun.

**Outcome:** `PILOT_ALL_UNIT`. Modal app
`ap-4ye2CkHWY93ZYrySLOibPR` completed all 24 representatives. Result
SHA-256: `796378e75e7eee01924c8f7b64ccfb1dc6af07adf9db945b59b8e59728b32507`.
All rows are `COMPLETE`, all saturated ideals are unit, and the checker
accepts the exact ordered case cover with 3/3 hostile mutations rejected.
The run completed in about 14 seconds and authorizes the separately
preregistered 708-case campaign. It does not itself close any raw label.
## Preregistered O0b split cell-0 complete outside campaign

- **decision:** decide the changed O0b outside ideal on every canonical
  equal-sign cell-0 component representative
- **scope:** all 708 representatives covering 2,520 component cases and
  1,260 underlying raw labels
- **launcher SHA-256:**
  `04ae51440703ad0116e33ce6a4c7f3312eff748cd8c3fa1a1d326c4d465f5d48`
- **checker SHA-256:**
  `74770cfadbfa1275fe58fbee187b40e00cea8e8526ff3dc07347a8011c8046b5`
- **outside-core SHA-256:**
  `5cd86020b601b68e9a4295d55d057ec0e029dede334397e6bc51f9d840e5561f`
- **representative manifest SHA-256:**
  `658ae5f1f3c0667df2cece818e0c89a752ce9cdf7c4f6f421fc4a721134b8fa4`
- **full representative-list SHA-256:**
  `23d7e403e420307b5466ffaf6d2af59d0cf9a4a93766b4d0bcf68231aba1a741`
- **pilot authorization:** app `ap-4ye2CkHWY93ZYrySLOibPR`, 24/24 exact
  unit ideals, result SHA-256
  `796378e75e7eee01924c8f7b64ccfb1dc6af07adf9db945b59b8e59728b32507`
- **envelope:** at most 64 concurrent one-CPU, 2-GiB workers; 180-second
  Singular child and 210-second container walls; one 285-second external
  campaign hard stop; conservative simultaneous-resource cost below `$0.50`
- **local safety:** one RAM-guarded Modal client; results checkpoint in
  canonical order after every returned row

This run changes only `--scope all`. The complete PROVED router, component
relations, exact equations, guard set, image, and solver are byte-identical to
the successful pilot. The external stop bounds total active container time by
`64*285` seconds even if hard rows queue or time out. An interrupted run keeps
its ordered prefix and authorizes resumption only after an exact remaining-
case router is recorded.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 285s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_cell0_component_outside_modal.py \
  --scope all
```

`COMPLETE_OUTSIDE_EXCLUDED` requires 708/708 `COMPLETE` unit rows, exact
ordered case and source hashes, and checker acceptance. It authorizes a
separate PROVED outside-exclusion node after an independent algebraic audit
of the generated equations and guard semantics. A complete nonunit row is a
retained candidate locus, not a counterexample until replayed against the raw
system. Any timeout, remote error, malformed row, client interruption, or
missing representative is `INCOMPLETE` and causes no status promotion.

**Outcome:** `COMPLETE_OUTSIDE_EXCLUDED`. Modal app
`ap-iPfRgFxqrpfuNMG1WzzxIZ` completed all 708 representatives; result
SHA-256: `6aed35275a09c9ceaa55f2e47ad07409f7d3ed0ffd8f77010ce080ba862b95aa`.
Every row is `COMPLETE`, every sequentially saturated ideal is unit, and
there are 708 distinct program hashes. The independent audit checks the
ordered representative cover, exact O0b edge table, contiguous Singular
transcripts, stable unit tails, and guard profile `30:354,31:354`, with 3/3
hostile mutations rejected. The Modal client printed a nonfatal asynchronous-
generator shutdown warning after the complete checkpoint; it exited zero and
the checker accepts 708/708 rows. The separate PROVED cell-0 exclusion node
consumes this certificate.
## Preregistered O0b split cells-3/6 compact-curve outside pilot

- **decision:** determine whether the changed O0b outside records cut the
  proved cell-3 common curve uniformly before authorizing any 1,416-case run
- **scope:** 24 canonical representatives whose orbits meet all 56
  `lane-orbit/outside-sign/first-source-sign/missing-record` strata
- **launcher SHA-256:**
  `904955fd4b59e46c9f3595bb902c413ba33fff9d9d1afaaced1dff2a93a18376`
- **checker SHA-256:**
  `e924f7cf36caf9a09ee248384f8f9cc67cb70ed7952e5da3205b48b6722a06e6`
- **outside-core SHA-256:**
  `07d371aaf2beee7c3182e3ae2f65e0e3844a74e8730850d1d764714b07dfa46b`
- **representative manifest SHA-256:**
  `409e0e0851f2cef35501123b3dcb5818318380a291864090a7792accf599dfc2`
- **pilot representative-list SHA-256:**
  `a1853f2a70cd7fc46c173f1401e4b7e8820f9fa1c01e8a8b3571bfefa2969c96`
- **product-rank certificate SHA-256:**
  `ee4dcb25877e9101a544ee5896b9bf6890059d6398c78d7562127b0d1c53c293`
- **compact-kernel certificate SHA-256:**
  `e20ccb714b252f00ee3ce877ee68eff032f43deb877e2097919151436ddcf789`
- **envelope:** at most 24 one-CPU workers, 3 GiB each, 240-second
  Singular child wall and 300-second container wall; conservative campaign
  wall below six minutes and projected cost below `$0.50`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; all CAS work is remote and each returned row is checkpointed

Each worker compiles the three exact compact common-curve determinants, the
missing product and squared-sum equations, and the three residual pairing
equations for one canonical O0b label. Ordinary source/target guards are
saturated factor by factor. The product-rank-five open set is saturated once
by the ideal generated by all six stripped cofactors; this encodes that at
least one chart is nonzero and does not incorrectly require every chart to be
nonzero.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_cells3_6_outside_modal.py
```

`PILOT_ALL_UNIT` requires 24/24 `COMPLETE` rows, unit final ideals after the
six-cofactor saturation, exact ordered case custody, 24 distinct program
hashes, and checker acceptance. It is route evidence only and does not close
any raw label. A complete nonunit row is retained with equations, guards, and
cofactors for decomposition. `TIMEOUT`, `ERROR`, `REMOTE_ERROR`, interrupted
client, or incomplete checkpoint is `INCOMPLETE`; no larger campaign is then
authorized.

**First outcome:** `INCOMPLETE`. Modal app
`ap-feEnIyVR9k2To4heuY161N` returned 24/24 `REMOTE_ERROR` rows after every
worker hit the 300-second function wall. Result SHA-256:
`2a48b176a5c7a60f6a32ce9b234d18af57aa7b283142f4e1533065af0eb1d8fa`.
Incomplete-checker SHA-256:
`a62ab6cb6e7e5f725f65053f8f495d66f69113849deb61a8f9d2917dca124df8`.
No worker returned a program hash or Singular transcript, so the run has no
mathematical status. The failure rejects the architecture in which every
case independently recompiles the same high-degree compact determinants.
Do not rerun this launcher and do not authorize the complete campaign. The
bounded repair is to compile the four source-sign common packets once, pin
them, and make case workers consume those cached polynomials.
## Preregistered cell-3 cached common-input compilation

- **decision:** remove duplicated symbolic compilation from the O0b
  cells-3/6 outside workers and pin one reusable packet per source-sign row
- **scope:** exactly four source-sign rows; no outside labels and no Singular
  solve
- **launcher SHA-256:**
  `d9cb5dd8f5c66c69f9c5ed79f7d1b2b965ce306feddd0db865146d82c2bfbeba`
- **checker SHA-256:**
  `99e6f05bd9e97ffa091b3f9e347765cbb0b864ff61f56a567206a4aed6e36ae3`
- **product-rank certificate SHA-256:**
  `ee4dcb25877e9101a544ee5896b9bf6890059d6398c78d7562127b0d1c53c293`
- **compact-structure certificate SHA-256:**
  `2f8712f2a942bb46f153d5204c4f4c8f9bff08336c295db4f31aef10fb5d22b7`
- **compact-kernel certificate SHA-256:**
  `e20ccb714b252f00ee3ce877ee68eff032f43deb877e2097919151436ddcf789`
- **envelope:** four one-CPU workers, 3 GiB each, 180-second container
  wall; projected cost below `$0.10`
- **local safety:** one RAM-guarded Modal client under a 240-second external
  hard stop; no local symbolic algebra

Each row must reproduce the three compact-equation hashes already recorded
in the six-chart structure certificate and the eight kernel-entry hashes in
the global kernel certificate. The output packet stores Singular-ready text
for three equations, eight kernel entries, sixteen route guards, and six
rank cofactors. The checker requires all four ordered sign rows, exact source
custody, exact packet shape, and four distinct packet hashes.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 240s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_cached_common_input_modal.py
```

A complete checked result certifies only reusable representation of already
proved common algebra. It authorizes construction and preregistration of the
repaired 24-representative outside pilot; it excludes no outside system.

**Outcome:** `COMPLETE`. Modal app `ap-tR1KpzLy0sJ3HRhVkj0GRh` returned all
four ordered source-sign packets in about 17 seconds. Result SHA-256:
`28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`.
Packet SHA-256 values, in sign order `--,-+,+-,++`, are

```text
fbeda61593e73cdcb7bf1e2baa1ebe8b098a7025f834135b3e02d2c291d50cd9
0cf5d0801b2372dd5def2fa9696c42641b7b5f6cf14f507dd412e39c91375834
51278b32abf7a566d265db9c49748dedb3709b88d48efeebad669cc85153ce38
489da8fbad2072ed6518761aba2bb55208085283345b196ca78db445e1169f4c
```

The checker accepts all 12 equation hashes, 32 kernel hashes, and 24 rank
cofactors. The Modal client printed its known nonfatal async-generator close
warning after writing the complete checkpoint; the app exited zero and the
result is independently accepted.
## Preregistered O0b split cells-3/6 cached-input pilot

- **decision:** rerun the 24-representative pilot after removing all
  per-worker SymPy compilation; do not enlarge the representative domain
- **scope:** the same 24 canonical representatives and 56 coarse strata as
  request 51
- **launcher SHA-256:**
  `8a4409c16a44a6119f0e5e2d63fbb2aa0aca768371e1caacba2ab6b0e5169573`
- **checker SHA-256:**
  `c81565e84640732dc5bdbe0f611e95eec58117e27ca777d898e48190c10930a8`
- **string-compiler core SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **representative manifest SHA-256:**
  `409e0e0851f2cef35501123b3dcb5818318380a291864090a7792accf599dfc2`
- **pilot representative-list SHA-256:**
  `a1853f2a70cd7fc46c173f1401e4b7e8820f9fa1c01e8a8b3571bfefa2969c96`
- **envelope:** at most 24 one-CPU workers, 3 GiB each, 240-second
  Singular child wall and 300-second container wall; projected cost below
  `$0.50`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; exact algebra remains remote and every returned row checkpoints

The string compiler consumes the pinned source-sign packet and emits eight
named equations directly in Singular syntax: three common determinants, one
missing-product equation, three residual pairing equations, and one missing
squared-sum equation. It imposes 40 deduplicated ordinary guards and then
saturates by the six-generator product-cofactor ideal. There is no SymPy
dependency or polynomial expansion in a case worker.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_modal.py
```

`PILOT_ALL_UNIT` requires 24/24 complete unit rows, exact packet/case custody,
24 distinct program hashes, final six-cofactor saturation transcripts, and
checker acceptance. A complete nonunit is retained in full. Any timeout or
error remains `INCOMPLETE`; the full 1,416-representative campaign is not
authorized by this preregistration.

**Outcome:** `INCOMPLETE`; global seven-variable saturation rejected. Modal
app `ap-inXJOeBGmGffKFVY29yI3W` produced 23 ordered `TIMEOUT` rows before the
external six-minute wall; the remaining input was preempted and restarted.
The app still had two containers after the client wall, and they were
explicitly stopped with `modal app stop -y`. Result SHA-256:
`4d2471d23f0ac04f5e049b6a84cd08152f85911f5cb72b0b5ae3a436d414accf`.
Incomplete-checker SHA-256:
`77b434e7dd89ffb31ffca3a40b7a11d2956916ad0606c40a1d2cc641451cdc39`.

Every returned worker had an exact program hash and cached-packet hash but an
empty partial stdout: Singular did not finish the initial `slimgb(I)` before
the 240-second child timeout. Thus cached input fixed the first run's symbolic
duplication, but the raw eight-generator seven-variable Gröbner basis is
itself unsuitable. No row has mathematical status, and no batch rerun is
authorized. The bounded replacement is to cache the saturated common-curve
Gröbner basis first and test one outside case against that basis.
## Preregistered cell-3 guarded global common basis

- **decision:** replace the failed raw seven-variable Gröbner endpoint by a
  cached one-dimensional common basis before adding any outside equation
- **scope:** four source-sign rows, common variables `(t,r,c,b)` only
- **launcher SHA-256:**
  `c344181eecbec17bc6677a2751a31dc025035a714f3dff57dd50380e2a4116a6`
- **checker SHA-256:**
  `9a64da492f10fc051cd8b0748d7227c02a8210c954406f62818ec2ddc24949e6`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **envelope:** four one-CPU workers, 4 GiB each, 240-second Singular
  child wall and 270-second container wall; projected cost below `$0.20`
- **local safety:** one RAM-guarded Modal client under a 330-second external
  hard stop; no local CAS

For each sign row, Singular starts from the three pinned compact equations,
saturates all sixteen route guards, and then saturates by the ideal generated
by all six product cofactors. The latter restricts to the union of the six
rank-five charts, rather than requiring every cofactor nonzero. The complete
reduced basis is printed and checkpointed. Acceptance requires four ordered
rows, dimension one, nonempty complete bases with exact internal hashes,
sign-packet custody, clean transcripts, and three hostile mutations rejected.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 330s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_global_common_basis_modal.py
```

A checked result is a reusable algebraic representation of the already
proved guarded common curve. It authorizes one preregistered outside-case
diagnostic from the reduced basis; it does not authorize a 24- or 1,416-case
campaign and excludes no outside system by itself.

**Outcome:** `COMPLETE`. Modal app `ap-e7skPdzRi1PIPNxBo3VKdw` returned four
dimension-one bases, each of size 21, in about two minutes. Result SHA-256:
`bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`.
Basis SHA-256 values in sign order `--,-+,+-,++` are

```text
20d4032b93acc1f0918efea258978bf830a4a7de389442b519e9496f9b6e9df4
a27da16ead59ce535f5fd5017a97c7459de63fab60b1b27456cc82e7cbe20202
f9e7054412eae0ecbd2d0369bbd4ddb9e7ba80b29e59f02ca86cb24ef7a9725e
11e2e6e5abde49d1887ea4b677bcdbb0aefb02b9e7cf696f93e8b04f7b06b0b5
```

The checker accepts four distinct programs and bases and rejects 3/3 hostile
mutations. The known nonfatal Modal async-generator close warning occurred
after the complete checkpoint; the app exited zero.
## Preregistered O0b cells-3/6 global-basis one-case diagnostic

- **decision:** test whether one outside ideal becomes tractable when its
  initial generators include the proved 21-polynomial common basis
- **scope:** exactly case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=0,pairing=0)`
- **launcher SHA-256:**
  `5b7620a0c07b59b652c39efe6d61e481806243488d40ad0e9a6b713353c2a32f`
- **complete-unit checker SHA-256:**
  `614aea8cccfc02c1fe98b4320aa733de4cda278ed23ab692bae55719db51f03c`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **string-compiler core SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.05`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The initial ideal contains the 21 pinned `--` common-basis polynomials and
only the five case-specific outside equations. The ordinary guards and the
six-cofactor-ideal saturation are then replayed. The worker must print the
initial ideal dimension/size before any saturation, so a timeout after that
point still localizes the next obstruction.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_cells3_6_basis_diagnostic_modal.py
```

A checked unit result authorizes a small multi-stratum basis-fed pilot. A
complete nonunit is retained in full and becomes the next algebraic target.
A timeout or error authorizes only decomposition of this one case. No outcome
from this single diagnostic closes an orbit or authorizes the 1,416-case run.

**Outcome:** `COMPLETE_UNIT`. Modal app `ap-hbvBTuGWrmg6ezfjG93fX7`
completed the pinned case in about three minutes. Result SHA-256:
`e7ea616f603636f8286225e5cd851cdacd8ea1a32e56ba87825a9a2c9e46898d`.
The initial ideal has dimension 3 and basis size 108. After the first five
guard stages it remains dimension 3; saturation by guard 5, `b+1`, yields the
unit ideal, and every later stage remains unit. The complete-unit checker
accepts the exact source packet, 21-element common basis, five outside
equations, 40 guards, six cofactors, and final transcript. Thus every algebraic
solution lies on the forbidden target boundary `b=-1`. By the proved quotient
this excludes the four raw cases in one symmetry orbit. It authorizes only a
small cross-stratum basis-fed pilot, not the complete campaign.
## Preregistered O0b cells-3/6 six-case basis-fed cross pilot

- **decision:** test the validated basis-fed architecture across both lane
  orbits and all three represented missing-record orbit types
- **scope:** six unclosed representatives, one per
  `{S0,SDE/SDF} x {xi=0,xi=2,xi=6}`, with varied outside/source signs
- **launcher SHA-256:**
  `b5ee2cd7bb5233547498dafb4140a3dd776c6f30cdcfc2cc11304fa2483b3599`
- **outcome-neutral checker SHA-256:**
  `734801c516cd79790133f2116ea6319a3bef23ab5c7dd1109b3ed121e283031c`
- **case manifest SHA-256:**
  `dfbbee76c4d04f71d65b2c3b9fea83b9fbdb8e86cd0ff26f76fef591e1d49fbc`
- **ordered case-list SHA-256:**
  `2e1eea3589e0737e9efa7a3a49a0492d6fece4577b93a36eb1f6badf0b499b42`
- **basis-program core SHA-256:**
  `2298a72b7d45f6e920244836f4e7fa3589c80a8e5a254ca03ee9971053a57670`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **envelope:** at most six one-CPU workers, 4 GiB each, 240-second
  Singular child wall and 300-second container wall; projected cost below
  `$0.35`
- **local safety:** unordered result streaming with immediate checkpoints
  under one RAM-guarded Modal client and a 360-second external hard stop

The already closed diagnostic representative is excluded. Every worker starts
from the correct 21-polynomial source-sign common basis and adds five outside
equations. The output-neutral checker accepts exact complete unit or nonunit
rows and exact timed rows, while still requiring complete six-row collection,
ordered case reconstruction, source custody, and distinct program hashes.
The unordered map prevents a preempted low-index input from blocking later
checkpoints.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_cells3_6_basis_cross_pilot_modal.py
```

All-unit completion authorizes the full pinned 24-representative pilot after
subtracting already closed rows. A nonunit becomes the next algebraic target.
Timeouts authorize only a stratum-specific decomposition. This six-case run
does not authorize the 1,416-case campaign.

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app
`ap-HONZUndkEeMfHPJ450zO9c` returned all six pinned rows, each with status
`TIMEOUT`; result SHA-256:
`ebf5de0ff545dbba76db9f638aea5cd2bf0a013be51896c51aec5a7418ab3f11`.
The outcome-neutral checker accepts the complete ordered collection and
rejects all three hostile mutations. Rows 1 and 3 finished their initial
ideals, respectively at dimension/size `(3,114)` and `(3,120)`, then timed
out before completing the first guard saturation. Rows 0, 2, 4, and 5 did
not finish the initial basis within 240 seconds. Thus this result says
nothing about emptiness of any row. It rejects the six-case uniform campaign
as the next endpoint and authorizes only equation-order and first-guard
diagnostics on representatives of the two observed timeout modes.
## Preregistered O0b cells-3/6 initial-prefix diagnostic

- **decision:** locate the first hard outside equation in one representative
  whose full initial ideal timed out in the six-case cross pilot
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  independently test the common basis plus the first `1,2,3,4,5` outside
  equations in the compiler's pinned order
- **launcher SHA-256:**
  `19845e2caf2a57e54bb4c72572b0392f5a0ba1cbe10f81b1b80dc4a9b4509dff`
- **outcome-neutral checker SHA-256:**
  `917d3f9479ba981532ca4f339898aa927c9076847036c32a00b01e7b555e63d5`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** at most five one-CPU workers, 4 GiB each, 180-second
  Singular child wall and 230-second container wall; projected cost below
  `$0.25`
- **local safety:** unordered result streaming with immediate checkpoints
  under one RAM-guarded Modal client and a 300-second external hard stop

Every complete worker retains the exact reduced basis and its hash. Comparing
independent prefixes avoids making a long stage chain disappear behind one
timeout. The result is diagnostic only: completion of a prefix proves no
emptiness statement, and a timeout has no mathematical status. The maximal
completed prefix may be reused as a certified computational input for a
single-equation extension. This run does not authorize any multi-case or full
1,416-case campaign.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 300s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_cells3_6_initial_prefix_modal.py
```

**Outcome:** `INCOMPLETE_BOUNDARY_LOCALIZED`. Modal app
`ap-ujtvs7abKxrqiT8MlFc6re` returned all five pinned rows; result SHA-256:
`486c36b63335f0b30aa17008481df341869f5d37b32456d58fc40438deb7daa6`.
The outcome-neutral checker accepts the ordered collection and rejects all
three hostile mutations. Prefix 1, the 21-polynomial common basis plus `q3`,
completed at dimension 3 with a retained 51-polynomial basis. Its canonical
polynomial payload has 119,241 characters. Prefixes 2 through 5 all timed out
without output, so the first matching equation `q4` is the exact obstruction
in the compiler order. No emptiness statement follows. The retained prefix-1
basis authorizes independent single-equation extensions by each of
`q4,q5,q6,q7`, with the aim of finding an easier equation order before the
hard `q4` step.
## Preregistered O0b cells-3/6 single-equation extensions

- **decision:** search for a tractable ordering of the four equations hidden
  behind the first-prefix `q4` bottleneck
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  independently extend the retained `q3` basis by one of `q4,q5,q6,q7`
- **launcher SHA-256:**
  `97dc167ee95336920cf54acccb30f09d381aa8f69b429448a39ef70d4e8bb577`
- **outcome-neutral checker SHA-256:**
  `af1029828d47963ecbfa1d93a68668903281c554f8536df1d16a6b63cd1595e0`
- **initial-prefix result SHA-256:**
  `486c36b63335f0b30aa17008481df341869f5d37b32456d58fc40438deb7daa6`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** at most four one-CPU workers, 4 GiB each, 180-second
  Singular child wall and 230-second container wall; projected cost below
  `$0.20`
- **local safety:** unordered result streaming with immediate checkpoints
  under one RAM-guarded Modal client and a 300-second external hard stop

Each worker begins with the exact retained 51-polynomial basis of the common
ideal plus `q3`, reduces its one new equation modulo that basis, records the
normal-form degree and term count when available, and retains the exact new
basis on completion. An easy `q5`, `q6`, or `q7` extension authorizes a staged
ordering experiment from that basis; a timed `q4` row merely confirms the
localized computational obstruction. No row proves emptiness, and this run
does not authorize another representative or a full campaign.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 300s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_cells3_6_single_extensions_modal.py
```

**Outcome:** `INCOMPLETE_Q7_ROUTE`. Modal app
`ap-sS7K2kC529Y60lYzF2EsvC` returned all four pinned rows; result SHA-256:
`ce0396a9f6d951270a5ec3ba9b8371919020dcac75ca11af488d9fabc5e0edb9`.
The outcome-neutral checker accepts the collection and rejects all three
hostile mutations. The `q7` extension completed at dimension 3 with a retained
128-polynomial basis, hash
`679c448e3587f4bb11f39a6742aa7439d9b909ad68cf19834ca463d634c5aceb`.
The `q4`, `q5`, and `q6` extensions timed out. Their recorded reductions had
respective degree/term counts `(50,7593)`, `(48,2829)`, and `(48,7512)`;
`q7` had `(24,1500)`. Singular warned that the reconstructed source ideal was
not flagged as a standard basis. This does not invalidate the ideal equality
or the completed `q7` basis, because each reduced polynomial differs from its
source equation by an element of the retained ideal, but it makes the four
normal-form size measurements noncanonical. The next diagnostic must set the
pinned standard-basis attribute explicitly. The smallest observed hard
extension authorizes only the chain `q3 -> q7 -> q5`.
## Preregistered O0b cells-3/6 `q3 -> q7 -> q5` transition

- **decision:** test the cheapest supported continuation from the only
  completed single-equation extension
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  extend the retained `q3+q7` basis by `q5`
- **launcher SHA-256:**
  `7af2927ea5a209bfb1d0919f5a2a3f2b5ebd114039e33d2ab4c221bd9c30491f`
- **outcome-neutral checker SHA-256:**
  `058482e49eea43ba7369dbd8c9b2c1d54f27d02bc7f550e502dca56fa767dda9`
- **single-extension result SHA-256:**
  `ce0396a9f6d951270a5ec3ba9b8371919020dcac75ca11af488d9fabc5e0edb9`
- **source `q3+q7` basis SHA-256:**
  `679c448e3587f4bb11f39a6742aa7439d9b909ad68cf19834ca463d634c5aceb`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.06`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The reconstructed 128-polynomial source is explicitly marked with Singular's
`isSB` attribute before reduction; custody of the exact `slimgb` output makes
that assertion valid and removes the noncanonical-reduction warning from the
preceding diagnostic. A complete result retains the new basis and authorizes
only the next single-equation transition. A timeout has no mathematical
status and calls for algebraic decomposition of `q5` modulo the pinned source.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_cells3_6_q7_q5_modal.py
```

**Outcome:** `INCOMPLETE_CANONICAL_REDUCTION_TIMEOUT`. Modal app
`ap-PsMF23qtEZ5Lg6Ns1QWKJJ` returned the pinned row with status `TIMEOUT`;
result SHA-256:
`6181b927a81f77e973baffdf551628a77e04185ba04613e34900a68843200e64`.
The outcome-neutral checker accepts the exact row and rejects all three
hostile mutations. No normal-form marker was printed: after the valid `isSB`
attribute was set, canonical reduction of `q5` modulo the 128-polynomial
`q3+q7` basis did not finish within 240 seconds. This has no mathematical
status. It rejects further equation-order tuning as the immediate endpoint;
the next route should decompose the three matching resultants into their exact
projective common-root charts before attempting another basis computation.
## Preregistered O0b all-infinity projective-chart pilot

- **decision:** test the smallest leaf of the proved eight-chart resultant
  decomposition
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  chart mask `(infinity,infinity,infinity)`
- **launcher SHA-256:**
  `1c9b81d9377c6e06edd5b1953e955c5ebffb0d3a9592485fe00d3c5c11dfbeb3`
- **outcome-neutral checker SHA-256:**
  `c8ce618837d678d19dced46b9ff250d0141d3ac7e61f579372192b4e1a9f9876`
- **projective-chart program core SHA-256:**
  `277ad3a0d4489470eee9cef2c374b28d73aad333149ea415a3e55ea05549f4c5`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.06`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The all-infinity chart replaces each of `q4,q5,q6` by the two corresponding
leading-coefficient equations. It has the original seven variables, the
proved 21-polynomial common basis, `q3`, `q7`, six chart equations, all 40
ordinary guards, and the six rank cofactors. A checked unit result closes only
this one exact chart. A checked nonunit is retained as the next algebraic
target. A timeout has no mathematical status and does not authorize the other
seven charts or another representative.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_chart_all_infinity_modal.py
```

**Outcome:** `COMPLETE_UNIT`. Modal app `ap-qkhSkBXGe1rYbrHca5zY6I`
completed the exact chart in under ten seconds. Result SHA-256:
`545a130914d9896d84a5215865fea7333a2af9f1f7f9d08bfc14d3587770bcaf`.
The outcome-neutral checker accepts the transcript and rejects all three
hostile mutations. The initial chart ideal has dimension 3 and basis size 54.
It remains dimension 3 through the first five guard stages; saturation by
guard 5, `b+1`, yields the unit ideal. Thus every all-infinity solution lies
on the forbidden boundary `b=-1`, and this one chart is closed exactly. The
result authorizes a small pilot across the other seven chart masks for this
same representative, not a second representative or the full quotient.
## Preregistered O0b seven-chart completion pilot

- **decision:** test every remaining leaf of the proved projective-chart split
  for the same representative whose all-infinity chart is closed
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  the seven masks in `{finite,infinity}^3` other than all-infinity
- **launcher SHA-256:**
  `99eaffabe8f10e1b303421fdec25f7d958f33f1dcc4e0dc05eac78da04333777`
- **outcome-neutral checker SHA-256:**
  `902c15e5dd3316957efab6342d3feec4df881e9ddb7d7ec1315762f4e007d5fb`
- **projective-chart program core SHA-256:**
  `277ad3a0d4489470eee9cef2c374b28d73aad333149ea415a3e55ea05549f4c5`
- **closed all-infinity result SHA-256:**
  `545a130914d9896d84a5215865fea7333a2af9f1f7f9d08bfc14d3587770bcaf`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** at most seven one-CPU workers, 4 GiB each, 240-second
  Singular child wall and 300-second container wall; projected cost below
  `$0.40`
- **local safety:** unordered result streaming with immediate checkpoints
  under one RAM-guarded Modal client and a 360-second external hard stop

Each row uses the same common basis, `q3`, `q7`, six exact chart equations,
40 guards, and six rank cofactors. Finite branches add exactly one auxiliary
root variable apiece. Seven checked unit rows, together with the already
closed all-infinity chart, close this representative. A nonunit is retained
as the next algebraic target. Timeouts have no mathematical status and permit
only mask-specific decomposition, not another representative or the complete
quotient campaign.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_chart_remaining_pilot_modal.py
```

**Outcome:** `INCOMPLETE_FOUR_CHARTS_CLOSED`. Modal app
`ap-Ie9cKPqFBjPpGsDFqbuo8X` returned all seven rows; result SHA-256:
`09d854294bb4b0f3d33fc45f140f12ca86eebbb568c1f845a061b4143c50dba0`.
The outcome-neutral checker accepts the collection and rejects all three
hostile mutations. Every mask with exactly one finite root completed and
became unit at guard 5, `b+1`: `FII` had initial dimension/size `(4,57)`,
`IFI` had `(4,74)`, and `IIF` had `(4,62)`. Together with the all-infinity
result, four of eight charts are closed. The masks `FFF`, `FFI`, `FIF`, and
`IFF` timed out before printing an initial basis and have no mathematical
status. Their repeated `b+1` boundary pattern authorizes a four-row direct
Rabinowitsch test of the open set `b+1 != 0`, bypassing the raw initial basis.
## Preregistered O0b multi-finite direct-boundary pilot

- **decision:** bypass the timed raw initial bases and test the repeatedly
  observed `b=-1` boundary directly on the four open chart masks
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  masks `FFF`, `FFI`, `FIF`, and `IFF`
- **launcher SHA-256:**
  `fefeac8a66f7443193aedc039523dde2f2c1661531971724181b479cdbd45921`
- **outcome-neutral checker SHA-256:**
  `605b0ea8a76640f31270ac92ce8468e4b0888427541283b2a16cb5d4eb317c1c`
- **Rabinowitsch chart-program core SHA-256:**
  `de224a472ce32dc98bb2c52e6aef987ef6864abd4be83e3741477f5a22050d38`
- **seven-chart pilot result SHA-256:**
  `09d854294bb4b0f3d33fc45f140f12ca86eebbb568c1f845a061b4143c50dba0`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** at most four one-CPU workers, 4 GiB each, 240-second
  Singular child wall and 300-second container wall; projected cost below
  `$0.25`
- **local safety:** unordered result streaming with immediate checkpoints
  under one RAM-guarded Modal client and a 360-second external hard stop

For each chart ideal `I`, the program adds one variable `w` and the exact
Rabinowitsch equation `w*(b+1)-1`. The resulting ideal is unit exactly when
`V(I)` has no point with `b+1 != 0`. This is stronger than applying the other
ordinary guards and is sufficient to close a chart because `b=-1` is already
forbidden. Four checked unit rows would finish all eight charts and close the
representative. A nonunit program is retained; a timeout has no mathematical
status and authorizes only chart-specific algebraic decomposition.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_chart_multifinite_boundary_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app `ap-Ko0Ogcm5COQw1JY6C655Bp`
returned all four pinned rows with status `TIMEOUT`; result SHA-256:
`9e5dd9324b1fe7575c7d16135465bd1c560f3cce9d3effbee5ecece6391109c6`.
The outcome-neutral checker accepts the collection and rejects all three
hostile mutations. No worker printed a transcript, so none completed its
direct Rabinowitsch basis. This has no mathematical status and neither proves
nor weakens the `b=-1` boundary hypothesis. It rejects a uniform direct
Singular campaign as the next endpoint. Further work must either exploit the
finite common-root equations structurally or compare a genuinely different
Groebner architecture on one mask before any four-mask rerun.
## Preregistered O0b `FFI` kernel-lifted boundary diagnostic

- **decision:** compare a genuinely sparse graph-lifted formulation against
  the timed substituted-kernel boundary ideal
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  chart mask `FFI` only
- **launcher SHA-256:**
  `aa6ddf1a87175b4e9d238189bc91f952e2e4db73b0b6d191a898cb0ba555cf44`
- **outcome-neutral checker SHA-256:**
  `74783c856fffb0c1aed80bf139193be0bef28621371df729e1d35e32451e9529`
- **lifted boundary-program core SHA-256:**
  `af075097d890859b5ce077d2fafa77d8c4eb2755853217e46fb691f7dde21f62`
- **direct boundary result SHA-256:**
  `9e5dd9324b1fe7575c7d16135465bd1c560f3cce9d3effbee5ecece6391109c6`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.06`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The program introduces variables `z0,...,z7` and the eight exact graph
equations `zi=ki(t,r,c,b)`. All outside equations are then written sparsely in
the `zi`, with two finite root variables and the Rabinowitsch inversion of
`b+1`. Projection along the graph variables is an isomorphism with the direct
substituted system, so a unit result is an exact chart proof. Completion
authorizes transport to the other three multi-finite masks. A timeout retires
this lifting architecture; it does not authorize a larger run.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_chart_ffi_lifted_boundary_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app `ap-fUoFJO8Eerf3cNt42uc2ex`
returned the pinned row with status `TIMEOUT`; result SHA-256:
`5853ed157ae0badde2180fb1b3f21fe8d7ef957ab9052117b6e9884a0cce08aa`.
The outcome-neutral checker accepts the exact graph-equation ledger and
rejects all three hostile mutations. No transcript was printed before the
240-second wall. Thus the sparse eight-variable kernel lift has no
mathematical status and is retired as the next Singular architecture. It must
not be expanded to the other masks. The four multi-finite charts now require
either a structural common-root reduction or a one-mask comparison with a
genuinely different algebra engine.
## Preregistered O0b `FFI` msolve F4 comparison

- **decision:** compare one genuinely different exact Groebner engine after
  all pinned Singular architectures timed out on the multi-finite frontier
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  lifted chart `FFI` with direct inversion of `b+1`
- **launcher SHA-256:**
  `aba99e284f29e21e141dd89662bc115dd20c7ad4aec5804801049bd7dd53d4a6`
- **outcome-neutral checker SHA-256:**
  `c3be965f5dfe87584f1c65683fc0a021788640db46dfee49b3b3c4a9407b3c12`
- **explicit-input exporter SHA-256:**
  `3775ca175d8d9e848637cd58e8337a84400ff6b9f5155a1d0dc4a924539dcc8b`
- **msolve prime-field smoke result SHA-256:**
  `4bf0791c422e83438b65c2c871119eee0a7124be1e2a6d508185ce7a13e11d70`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** one CPU, 8 GiB, 240-second msolve child wall and 330-second
  container wall; projected cost below `$0.10`
- **local safety:** one RAM-guarded Modal client under a 390-second external
  hard stop; no local CAS

The Debian trixie package supplies `msolve 0.7.5`. A pinned smoke test confirms
that it accepts characteristic `2130706433` and prints the canonical basis
`[1]` for a unit ideal. Singular is used only as a deterministic `short=0`
polynomial formatter: it exports the 38 exact graph-lifted generators with
explicit multiplication and powers. The full msolve input and its hash are
retained before the single-threaded `-g 2` F4 computation.

A checked `[1]` basis closes `FFI` off `b=-1` exactly and authorizes one-mask
transport to `FIF` and `IFF`. A complete nonunit is retained. A timeout or
engine error retires msolve on this frontier and does not authorize a larger
run.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 390s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_ffi_msolve_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app `ap-JJorYivOpEN8Skp6k2dJtx`
returned the pinned row with status `TIMEOUT`; result SHA-256:
`f0846e25f26981e045d4416233bd81d36dac6c3a44b0da7b2cd19912a02c57dd`.
The outcome-neutral checker accepts the exact 18-variable, 38-polynomial
input and rejects all three hostile mutations. msolve `0.7.5` reported the
correct characteristic, 18 variables, 38 valid equations, DRL order, sparse
exact linear algebra, and one thread, but produced no basis output within 240
seconds. This has no mathematical status and retires F4 on the unreduced
lifted system. The retained 15,897-byte explicit input exposes a structural
reduction in the `q6` infinity equations: admissibility forces `z2=z5=0`,
which is the next exact route.
## Preregistered O0b `FFI` leading-collapsed pilot

- **decision:** exploit the proved infinity-pair implication `z2=z5=0` before
  computing the `FFI` boundary ideal
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  chart mask `FFI` only
- **launcher SHA-256:**
  `b622498b9b812eaf018ad65a227f75d334fef77549ec09bcec3ef44fb42372d1`
- **outcome-neutral checker SHA-256:**
  `318345ac994f056f85ff66d92f44c920c83fdc9b7841518ec841d9ec8d870886`
- **collapsed program core SHA-256:**
  `37c2e59eaa893327e409a67fdf719f8c99aa7fa1e03ac766a37c6c6826535bf9`
- **explicit msolve input/result SHA-256:**
  `f0846e25f26981e045d4416233bd81d36dac6c3a44b0da7b2cd19912a02c57dd`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.06`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The proved collapse removes lift variables `z2,z5`, replaces their graph
equations by `k2=k5=0`, and makes both finite matching pairs linear in `u4`
and `u5`. The 16-variable, 36-generator system inverts exactly
`f*(d^2-e^2)*(b+1)`: the first two factors justify the collapse and the last
is the repeatedly observed forbidden boundary. Therefore a checked unit basis
proves admissible `FFI` emptiness. Completion authorizes the analogous `FIF`
reduction. A timeout permits only further structural elimination in `FFI`.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_ffi_collapsed_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app `ap-CUpVsyqTjfJYECd7zUqcL8`
returned the pinned row with status `TIMEOUT`; result SHA-256:
`86d8686abf3d178bef2e1adaa17ca62e7d8b6dc0f5021b95cc8ee2f398f64335`.
The outcome-neutral checker accepts the exact collapse and guard ledger and
rejects all three hostile mutations. No transcript was printed within 240
seconds. This has no mathematical status. The next structural reduction may
eliminate `u4,u5`: after `z2=z5=0`, each finite common-root pair consists of
two linear equations in one root, so vanishing of its `2 x 2` coefficient
determinant is necessary. Proving the resulting root-free superset empty is
sufficient to close `FFI`.
## Preregistered O0b `FFI` root-free determinant superset

- **decision:** replace each finite common-root pair in the proved
  `z2=z5=0` collapse by its necessary `2 x 2` coefficient determinant
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  chart mask `FFI` only
- **relation to the exact chart:** necessary superset, not an equivalence
- **launcher SHA-256:**
  `9ad375b539c95c3471e78d9a37ccbe51eb7c468f21f889e879f11de2a446706b`
- **outcome-neutral checker SHA-256:**
  `1c7568f25696684263c32f6fa29453ab3c4e48b3e59a1fd9291edbd7332d31b1`
- **root-free program core SHA-256:**
  `dfdbfb078ab594d18b53e511e8e17b0375b25a551aa4d58a7d1fc82c7b3689eb`
- **collapsed timeout/result SHA-256:**
  `86d8686abf3d178bef2e1adaa17ca62e7d8b6dc0f5021b95cc8ee2f398f64335`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **input ledger:** 14 variables, 34 generators, no finite-root variables;
  six retained kernel lifts and one Rabinowitsch variable
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.06`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

After the proved infinity equations force `z2=z5=0`, each finite pair has
the form `a0+a1*u=0`, `b0+b1*u=0`. A common root implies
`a1*b0-a0*b1=0`; replacing both pairs by these determinants can only enlarge
the exact chart. The system retains the common basis, all eight kernel graph
equations, `q3`, `q7`, both determinants, and the exact guard
`f*(d^2-e^2)*(b+1) != 0`. Therefore a checked unit basis proves the exact
admissible `FFI` chart empty. No nonunit or timeout outcome has proof status.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_ffi_rootfree_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app `ap-uPS6ojTUMH6RZEV8jPGt44`
returned the pinned row with status `TIMEOUT`; result SHA-256:
`4c88245bd500ce7e9f9c40c34483b8e07f0017b095e622023b6194039cfe85e6`.
The outcome-neutral checker accepts the exact necessary-superset ledger and
rejects all three hostile mutations, including an attempted upgrade from
necessity to equivalence. No transcript was printed within 240 seconds. This
has no mathematical status. Further work must factor or branch on the two
explicit determinant equations; repeating a broad 14-variable basis run is
retired.
## Preregistered O0b `FFI` exact root-free chart

- **decision:** strengthen the timed-out determinant superset by the proved
  first-slope guards `m4p1*m5p1 != 0`
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  chart mask `FFI` only
- **relation to the exact chart:** equivalence, using the proved collapsed
  finite-slope-anchor node
- **launcher SHA-256:**
  `0cb0662bd9838914634c2754b0945c65234acd510bfcac5aadbf29f37d777c1a`
- **outcome-neutral checker SHA-256:**
  `d6cb810186922e42a6b2a041083ff39e86ca92a0f33f5ab56901e826b47185b5`
- **exact program core SHA-256:**
  `0d0c2da7847897a53997e50c81dc351f4490a455b3b54596623fa61b9996b9a2`
- **root-free source core SHA-256:**
  `dfdbfb078ab594d18b53e511e8e17b0375b25a551aa4d58a7d1fc82c7b3689eb`
- **collapsed timeout/result SHA-256:**
  `86d8686abf3d178bef2e1adaa17ca62e7d8b6dc0f5021b95cc8ee2f398f64335`
- **finite-slope-anchor verifier SHA-256:**
  `1059e49271b06104353ad61c2e3c766c56e253ae3480c0410fb6afa08802ac99`
- **input ledger:** 14 variables, 34 generators, no finite-root variables;
  determinants `x4,x5` and exact slope guards `m4p1,m5p1`
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.06`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

On the collapsed locus each finite first polynomial is linear with proved
nonzero slope. Its common root is therefore fixed, and the corresponding
`2 x 2` determinant is exactly equivalent to the second polynomial
vanishing at that root. The system retains the common basis, eight kernel
graph equations, `q3`, `q7`, both determinants, and one Rabinowitsch
equation for `f*(d^2-e^2)*(b+1)*m4p1*m5p1`. A checked unit basis proves
admissible `FFI` emptiness. Timeout or nonunit output has no proof status.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_ffi_exact_rootfree_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app `ap-u6iyFxMytHuEldy71Db9JF`
returned the pinned row with status `TIMEOUT`; result SHA-256:
`da545e840fdcecaafb789df62444d3f8da68039d900cfec83c999f09e192daed`.
The outcome-neutral checker accepts the exact slope-guard ledger and rejects
all three hostile mutations. No transcript was printed within 240 seconds.
This has no mathematical status. Monolithic `FFI` basis runs in this
coordinate order are retired; the next work must factor or branch the
determinants under `q3`.
## Preregistered O0b collapsed four-variable common basis

- **decision:** impose the proved `k2=k5=0` collapse before adjoining any
  outside variables
- **scope:** the `epsilon=(-1,-1)` saturated common component underlying the
  canonical `FFI` and `FIF` charts
- **relation to the admissible locus:** necessary common superset; the
  already-saturated common ideal is intersected with `k2=k5=0` without a
  second guard saturation
- **launcher SHA-256:**
  `45336a48a27c06ea3eadd31fa3186a9dd4d29a5ea1a82811581a4e8c4e474659`
- **outcome-neutral checker SHA-256:**
  `681cdc37686d6f8e7dacfeb56f06edb9124f0341259925b3b1dfe077d4d88b94`
- **program core SHA-256:**
  `eced1e03746a6da568cff8a6e7e0b93e42aeb8d9eb9d0d011dc70896c71f303c`
- **input ledger:** variables `t,r,c,b`; 21-element global common basis plus
  the two exact kernel equations `k2=k5=0`
- **envelope:** one CPU, 2 GiB, 60-second Singular child wall and 90-second
  container wall; projected cost below `$0.01`
- **local safety:** one RAM-guarded Modal client under a 150-second external
  hard stop; no local CAS

A checked unit basis proves the necessary collapsed common superset empty and
therefore closes both `FFI` and `FIF`. A checked nonunit basis has no
emptiness status, but provides an exact four-variable generating set for
reducing `q3`, `q7`, and the finite determinants. Timeout retires this
ordering without changing the DAG.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 150s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_collapsed_common_basis_modal.py
```

**Outcome:** `COMPLETE_NONUNIT`. Modal app `ap-LAvxbcgb5gFcMXRlAAlUiR`
completed in about five seconds with a 43-element, dimension-zero basis;
result SHA-256:
`01a48b8003766b3e34d6b47423c8aaaf8ad8e521f77b1ce01cd1a9b5a6a7f65d`.
The outcome-neutral checker accepts the complete basis ledger and rejects all
three hostile mutations. This does not prove emptiness because the computed
necessary common superset is nonunit. It does prove that all exact
`FFI/FIF` base points lie in a finite four-variable scheme, making
finite-base specialization or FGLM the next gate.
## Preregistered O0b collapsed common FGLM audit

- **decision:** measure and triangularize the checked dimension-zero
  four-variable collapsed common basis
- **scope:** the 43-element `epsilon=(-1,-1)` basis containing every
  canonical admissible `FFI/FIF` base point
- **relation:** exact change of monomial order for the recorded finite scheme
- **launcher SHA-256:**
  `7d1ea7cf573830151f0c3e09ce99dd08415fe00491ce44074b50f029cd2f2022`
- **outcome-neutral checker SHA-256:**
  `3e2b9f1442dbf750e0e1ec9cb312ac4c20e3f08b19f49d5564767da14023fac1`
- **program core SHA-256:**
  `0bebc1df7b26991035541e545207c8c3f92eb17ffe136cca31e89a6bb08b9f34`
- **source basis/result SHA-256:**
  `01a48b8003766b3e34d6b47423c8aaaf8ad8e521f77b1ce01cd1a9b5a6a7f65d`
- **input ledger:** variables `t,r,c,b`; 43-element degree-order basis;
  print `vdim` before converting to lexicographic order
- **envelope:** one CPU, 4 GiB, 120-second Singular child wall and
  150-second container wall; projected cost below `$0.03`
- **local safety:** one RAM-guarded Modal client under a 210-second external
  hard stop; no local CAS

The pre-FGLM transcript prints the vector-space degree, so a timeout still
records the finite scheme size. Completion must preserve dimension and degree
and returns the full lexicographic basis. This is a representation theorem,
not an emptiness claim.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 210s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_collapsed_common_fglm_modal.py
```

**Outcome:** `COMPLETE`. Modal app `ap-i9TwFIx6T8gWO23DUhKlcQ`
computed vector-space degree 65 and a 20-element lexicographic basis; result
SHA-256:
`a72b2fe045538562352b3954b016dab60c5f8fdb01a22839088e72512d61f53f`.
The outcome-neutral checker verifies dimension and degree preservation and
rejects all three hostile mutations. The custodied factor verifier gives the
first eliminant exactly as
`b^3(b-1)^4(b+1)^5(b+8244070)(b+25179288)`. Thus the printed
`b,b-1,b+1` guards leave only two possible `b` fibers,
`2122462363` and `2105527145`, before the remaining guards are reapplied.
## Preregistered O0b collapsed-common admissible saturation

- **decision:** reapply all base admissibility conditions to the checked
  degree-65 collapsed common scheme
- **scope:** exact base locus for canonical `FFI` and `FIF` after
  `k2=k5=0`
- **relation:** exact route-guard and rank-cofactor saturation
- **launcher SHA-256:**
  `092ef33bf4bfcee1faac6ac5d7bbe59e9a900aecfe3c6344d0f766e9633cc5c3`
- **outcome-neutral checker SHA-256:**
  `ff9e43a54913a0d7d69b5ffdd4abf9bf06a3fd921a4361b144b98a804b089538`
- **program core SHA-256:**
  `a5c1c2a111088f34f0ac7563e4b6b06daabb8c955a98412edf35c02e3ba9b643`
- **source basis/result SHA-256:**
  `01a48b8003766b3e34d6b47423c8aaaf8ad8e521f77b1ce01cd1a9b5a6a7f65d`
- **FGLM result SHA-256:**
  `a72b2fe045538562352b3954b016dab60c5f8fdb01a22839088e72512d61f53f`
- **eliminant-factor verifier SHA-256:**
  `8d0c74703d84ff3eebaf43e5c867fc23ed6ea387a05497f8acc7fafed2a570e1`
- **input ledger:** variables `t,r,c,b`; 43-element degree-order basis;
  16 sequential route-guard saturations and one six-cofactor ideal saturation
- **envelope:** one CPU, 2 GiB, 60-second Singular child wall and 90-second
  container wall; projected cost below `$0.01`
- **local safety:** one RAM-guarded Modal client under a 150-second external
  hard stop; no local CAS

The prior common ideal was saturated before `k2=k5=0` was imposed. The new
intersection can acquire boundary points, as witnessed by the eliminant
factors `b^3(b-1)^4(b+1)^5`. This run removes every printed route boundary
again and then enforces the rank condition by saturation with the ideal of
six cofactors. A checked unit basis proves the exact admissible collapsed
base locus empty, closing both `FFI` and `FIF`. A nonunit result retains
the exact finite base for outside specialization.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 150s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_collapsed_common_admissible_modal.py
```

**Outcome:** `COMPLETE_UNIT`. The first launch
`ap-fT30bgqX6RwFGXiXVLwkGG` stopped locally on a mistyped custody hash and
performed no algebra. After the custody-only repair, Modal app
`ap-x3xOmQraUhfnUdjTM5KJwC` completed in about four seconds with a unit
basis; result SHA-256:
`38a44a30aa3421a67161acf5268d4bbfbe9e33903547e50259fc3f0da77efd03`.
The basis remains dimension zero through guard index 4 and becomes unit at
guard index 5, exactly `b+1`; the later stages and cofactor saturation stay
unit. The outcome-neutral checker accepts the complete 16-stage ledger and
rejects all three hostile mutations. This proves the exact admissible
collapsed common locus empty and therefore closes both `FFI` and `FIF`.
## Preregistered O0b `IFF` four-variable rational reduction

- **decision:** remove the already-closed `k2=0` infinity branch, solve the
  surviving `be=cf` branch for `d,e,f`, and clear all denominators
- **scope:** canonical `IFF` chart for
  `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`
- **relation:** necessary superset; `q5,q6` are retained through their
  scaled resultants, which also admit roots at infinity
- **launcher SHA-256:**
  `747b049182276b1feb785f5ce525ac14e70db79d8ae07cb3972310d56f3da13e`
- **outcome-neutral checker SHA-256:**
  `e6b895464bb43663ba0428a949eacd57628d1329ffdd12eda6ccb6221d12de54`
- **program core SHA-256:**
  `ce5ef23fee81c3065dbf66c35298abaa799198a4756ae1869a19b2382263d2ad`
- **collapsed-unit result SHA-256:**
  `38a44a30aa3421a67161acf5268d4bbfbe9e33903547e50259fc3f0da77efd03`
- **input ledger:** variables `t,r,c,b`; 21-element common basis; cleared
  equations in order `q7,q5,q6`; 16 route guards; denominator guards
  `k2,k5,a2m`; six rank cofactors
- **envelope:** one CPU, 4 GiB, 180-second Singular child wall and
  210-second container wall; projected cost below `$0.05`
- **local safety:** one RAM-guarded Modal client under a 270-second external
  hard stop; no local CAS

On the surviving infinity branch,

```text
e = k5/(b k2),
f = k5/(c k2),
d = a0m*b*k2/(k5*a2m).
```

The program verifies these substitutions symbolically, constructs scaled
quadratic resultants for the two finite pairs, and clears the `q7`
denominator. A checked unit basis proves this necessary superset empty and,
together with the closed `k2=0` branch, closes `IFF`. A nonunit result
provides a four-variable residual basis; timeout has no proof status.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 270s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_iff_rational_reduction_modal.py
```

**Outcome:** `COMPLETE_UNIT`. Modal app `ap-PDSXYqsKDmAp67vmdUw9kU`
failed before Singular because the remote builder unnecessarily imported
SymPy; app `ap-eoY557eS0JQZdQkGNwz10v` then exposed and preserved a staged
ideal-extension syntax error. After those non-mathematical repairs, app
`ap-1yCnh8r1A0yyUafO6gOTBR` completed with a unit basis; result SHA-256:
`5485816c745c18d1514200cc1bba057662c03319f7820883e7010ecb723b93c3`.
The equation stages are `q7: (dim 0,size 42)`,
`q5: (dim 0,size 44)`, and `q6: (dim 0,size 44)`. Route saturation
becomes unit at guard index 5, again exactly `b+1`; every later stage
remains unit. The checker accepts the complete ledger and rejects all three
hostile mutations. Together with the closed `k2=0` branch, this proves
`IFF` empty.
## Preregistered O0b `FFF` six-variable ratio reduction

- **decision:** use `q3` and `s=f/e` to eliminate `d,f`, then retain
  the cleared `q7` equation and all three scaled matching resultants
- **scope:** the last open canonical chart `FFF` for
  `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`
- **relation:** necessary superset; each finite common-root condition is
  weakened to scaled quadratic-resultant vanishing
- **launcher SHA-256:**
  `7d6ef24e5c3c50010ea714ef04e1e357887918692c3074c740ff9b9fa84c4232`
- **outcome-neutral checker SHA-256:**
  `86ecfcac32363a0e8546b34cc62d6cba104a57c460ba917df101041f536a7db2`
- **program core SHA-256:**
  `e1e7d17d0269b739d4952d2951f0ea094e819aa3b8c4827e781abff729b196c0`
- **IFF-unit result SHA-256:**
  `5485816c745c18d1514200cc1bba057662c03319f7820883e7010ecb723b93c3`
- **input ledger:** variables `e,s,t,r,c,b` with ordinary `dp` order;
  21-element common basis; equations in order
  `q7,q5,q4,q6`; 16 route guards; guards `e,s,a0m,a2m`; six rank
  cofactors
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.07`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The exact substitutions are

```text
f = e*s,
d = a0m/(e*a2m).
```

The standalone core verifies the substitutions, all six record values, and
the cleared `q7` numerator. The three scaled resultants retain all finite
roots and may additionally retain roots at infinity, so unit ideal for this
larger locus proves `FFF` empty. Completion with a unit basis closes the
last chart in the canonical representative; nonunit or timeout output has no
closure status.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_ratio_reduction_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app `ap-VtWKDIyM7gsbgbG2eyLP2S`
exposed a large-characteristic incompatibility in Singular's block-order
polynomial expansion and performed no valid basis computation. After
switching only to the already-validated ordinary `dp` order, app
`ap-EeRYmLyJl6zlU6zfjeELpW` completed the `q7` stage with
`(dimension 2,basis size 50)` and timed out while adjoining `q5`; result
SHA-256:
`0f9cb1df4d58e5c55ac742beb9d041a7c23ec9d282101c43d67acb4bfabfb4f5`.
The outcome-neutral checker accepts the retained stage transcript and rejects
all three hostile mutations. This has no closure status. The next route
replaces `e` by `E=e^2` for the `q7,q5,q6` subsystem before adjoining
the square root and `q4`.
## Preregistered O0b `FFF` square subsystem

- **decision:** replace `e` by `E=e^2` and test the necessary
  `q7,q5,q6` subsystem before adjoining `q4`
- **scope:** a strict necessary superset of the last open canonical
  `FFF` chart
- **relation:** necessary superset; `q4` is deliberately omitted and the
  two retained finite pairs are weakened to scaled resultants
- **launcher SHA-256:**
  `62df8e472a5409912e53d435da221750f3f1a44ad159e9f38c4355fe89df80ff`
- **outcome-neutral checker SHA-256:**
  `9c9ac1a611856cac9477be9701aa4aba77756cce17901667899c5e094d7227ae`
- **program core SHA-256:**
  `c5eca188068083699e94ba321858710f5225f423380a71821f9cea90135c4e72`
- **ratio-timeout result SHA-256:**
  `0f9cb1df4d58e5c55ac742beb9d041a7c23ec9d282101c43d67acb4bfabfb4f5`
- **input ledger:** variables `E,s,t,r,c,b`; 21-element common basis;
  equations in order `q7,q5,q6`; 16 route guards; guards
  `E,s,a0m,a2m`; six rank cofactors
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.07`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The substitution turns the cleared `q7` equation into

```text
lm*bm^2*E - (a0m + E*a2m)^2 = 0.
```

The `q5` resultant depends only on `s` and the base; the `q6`
resultant depends on `E,s`. Every `FFF` solution maps into this subsystem,
so a checked unit basis closes `FFF` without needing `q4`. A nonunit
result becomes the finite or lower-dimensional input for adjoining
`e^2=E` and `q4`; timeout has no proof status.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_square_subsystem_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app `ap-ZyjARWuvmq8EWOITABCBu5`
completed the `q7` stage with `(dimension 2,basis size 54)` and timed out
while adjoining `q5`; result SHA-256:
`cefc9fc49863ab0d20291c7cc009553bc45b8eb2946550c97c3daca154b595af`.
The outcome-neutral checker accepts the retained stage transcript and rejects
all three hostile mutations. Replacing `e` by `E` does not remove the
`q5` bottleneck. The next architecture reduces `q5` explicitly modulo
the common basis and adjoins it before `q7`.
## Preregistered O0b `FFF` reduced square subsystem

- **decision:** reduce the `q5` square-subsystem polynomial explicitly modulo
  the 21-element common basis, adjoin it first, then reduce and adjoin `q7,q6`
- **scope:** the same strict necessary superset of the last open canonical
  `FFF` chart used in section 73
- **relation:** necessary superset; `q4` remains deliberately omitted and the
  retained finite pairs remain weakened to scaled resultants
- **launcher SHA-256:**
  `bf9f5478cadf7888751aa00fe227850fefc8a6d328fc39fe2c2eb2d120ae73ac`
- **outcome-neutral checker SHA-256:**
  `fe361e54601f64077c0ec202dc35560bccb5ae9cc986d0af31717724cf0de423`
- **normal-form program SHA-256:**
  `ef7169e4c2e0044ddda34b8ecdd165fcc71699b9e7afbce848a036c27ddec1b1`
- **source square core SHA-256:**
  `c5eca188068083699e94ba321858710f5225f423380a71821f9cea90135c4e72`
- **source square timeout SHA-256:**
  `cefc9fc49863ab0d20291c7cc009553bc45b8eb2946550c97c3daca154b595af`
- **generated Singular SHA-256:**
  `d1e03febe23e00b5c5867aa737827c7ce2f0c701b759399afc28bc7fc6460a73`
- **input ledger:** variables `E,s,t,r,c,b`; 21-element common basis;
  normal forms and equations in order `q5,q7,q6`; 16 route guards; guards
  `E,s,a0m,a2m`; six rank cofactors
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.07`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

Section 73 reached a dimension-two, 54-element basis after `q7` and timed
out adjoining `q5`. This run uses the same equations but computes each
new polynomial's normal form before adjoining it and starts with the observed
bottleneck. Every `FFF` solution still maps into the tested subsystem. A
checked unit basis therefore closes `FFF`; a checked nonunit result supplies
a smaller exact basis for the omitted `q4` step; timeout has no proof status.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_reduced_square_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app
`ap-MhIhFWNqjNHO5cnOhY7yX9` completed the explicit `q5` normal form with
degree 90 and 4,717 terms, then timed out while adjoining that polynomial;
result SHA-256:
`c4406f815ddbcc33618a91ddce56b8a51c4f2c541f746d28f2873df377d0f7ba`.
The outcome-neutral checker accepts the retained transcript and rejects all
three hostile mutations. Whole-polynomial normal-form reduction therefore
does not remove the basis-construction bottleneck. The next architecture
decomposes the input by its low `s`-degree and reduces the coefficient
polynomials separately before rebuilding the equation.
## Preregistered O0b `FFF` ratio graph

- **decision:** introduce the exact guarded ratio graph
  `a2m*x-a0m=0` before adjoining the compressed `q5,q7,q6` equations
- **scope:** a strict necessary superset of the last open canonical
  `FFF` chart
- **relation:** necessary superset; `q4` remains deliberately omitted
- **launcher SHA-256:**
  `149547f42cfe4a31ad656272d361c0cc86006c6a19f991360a79cd0881b45a74`
- **outcome-neutral checker SHA-256:**
  `fede939b35864af09999feb26964e043a84b12777ba12617ae5bfa29a189e409`
- **program core SHA-256:**
  `4375aa57ad1b1ec1aa85afd323e6bed5d4e6b7bd1c33e4ab15492a623a443898`
- **generated Singular SHA-256:**
  `5c184f0bc3d20a5293e479d8c19aa16c12fb664710af6de1fbc9000dfd628cc7`
- **source reduced-square timeout SHA-256:**
  `c4406f815ddbcc33618a91ddce56b8a51c4f2c541f746d28f2873df377d0f7ba`
- **input ledger:** variables `E,s,x,t,r,c,b`; 21-element common basis;
  graph `a2m*x-a0m`; equations and normal forms in order `q5,q7,q6`;
  16 route guards; guards `E,s,x,a0m,a2m`; six rank cofactors
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.07`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

On the graph and under the already required `a2m != 0` guard, exact symbolic
identities give

```text
q5_original = a2m^4 * q5_graph
q6_original = a2m^2 * q6_graph
q7_original = q7_graph
```

Thus every admissible `FFF` point lifts to the graph subsystem and the
removed factors cannot vanish there. A checked unit basis closes `FFF`; a
checked nonunit basis supplies a compressed exact input for the omitted
`q4` step; timeout has no proof status. The launcher retains graph, normal,
and equation prefixes on timeout.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_ratio_graph_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app
`ap-WC4Rt0hC5xsMcfle0ioaP9` completed the ratio graph with
`(dimension 3,basis size 53)` in the full `E,s` ring and reduced
`q5` to degree 46 with 3,126 terms, then timed out while adjoining that
normal form; result SHA-256:
`9992611165f31733a3c497b27b93c39f65b621f9e3acc1489ab46c3d78e7096e`.
The outcome-neutral checker accepts the retained stage prefix and rejects
all four hostile mutations. The graph compression almost halves the normal
form degree and removes 1,591 terms, but a global `q5` basis remains the
bottleneck. The next architecture applies the required guard saturations to
the one-dimensional base graph before constructing any outside-equation
basis.
## Preregistered O0b `FFF` admissible ratio graph

- **decision:** construct the ratio graph in `x,t,r,c,b` and saturate
  only by the new base guards `x,a0m,a2m`
- **scope:** the admissible common-base projection required by every
  canonical `FFF` solution
- **source admissibility:** the 21-element common basis is already saturated
  by all 16 route guards and the six-cofactor rank ideal
- **launcher SHA-256:**
  `9b8eb716542e1b1530a2285aee9fc079c2b4686148a4ca6350affc6a633266e0`
- **outcome-neutral checker SHA-256:**
  `700c6c324ccdfd5c00f238cb0922b5ee674decf378152e81156d522bea53c2aa`
- **post-run stdout-tail repair checker SHA-256:**
  `6817767d7ea29bc1685447ccebce79494f36dda1b22bacf5b305981bc76923ad`
- **program core SHA-256:**
  `ca31838daef0f684d5bfffe82e0336e490707ef8acb023af6a323e0a169c7aa3`
- **generated Singular SHA-256:**
  `ca28ba87e35991836b713d32217fa842c700027dcb8b1ad6a2ec071c26a6b436`
- **source ratio-graph timeout SHA-256:**
  `9992611165f31733a3c497b27b93c39f65b621f9e3acc1489ab46c3d78e7096e`
- **input ledger:** variables `x,t,r,c,b`; 21-element dimension-one
  common basis; graph `a2m*x-a0m`; inherited 16 route guards and six
  rank cofactors; new guards `x,a0m,a2m`
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.07`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

Every admissible `FFF` point has `a2m != 0`, so it maps to this graph
with `x=a0m/a2m`; `a0m != 0` also makes `x != 0`. A checked unit
basis closes `FFF` before outside equations are needed. A checked nonunit
basis is retained exactly for coefficient-wise `q5` reduction and
low-degree `s,E` resultants. Timeout has no proof status.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_admissible_ratio_graph_modal.py
```

**Outcome:** `COMPLETE_NONUNIT`. Modal app
`ap-yefWfdW7toawtaFcRFwAG1` produced an initial graph basis of
`(dimension 1,size 53)`; saturation by `x` retained size 53,
`a0m` reduced it to size 48, and `a2m` retained size 48. The final
basis SHA-256 is
`7f59b5557597f429a3a56914cd5aad5c988902af6d88a3ef01580aaacbdd5d9e`;
result SHA-256:
`5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1`.

The preregistered checker rejected the otherwise valid payload because the
48-polynomial basis pushed the earlier `UNIT=0` marker outside the retained
30 kB stdout tail. The repaired checker removes only that redundant marker
test and instead requires the explicit nonunit field, dimension, basis
cardinality, and independently recomputed basis hash; it accepts the result
and rejects all three hostile mutations. The graph is nonempty, so this is
an exact input reduction rather than a chart closure.
## Preregistered O0b `FFF` q5 coefficients

- **decision:** decompose compressed `q5` exactly as
  `C0+C1*s+C2*s^2` and reduce each coefficient separately modulo the
  48-element admissible base-graph basis
- **scope:** exact normal-form data for the last open canonical `FFF`
  chart; no outside equation is adjoined
- **launcher SHA-256:**
  `890436d585a6f02c7d0b732b393e084cfc9300be8135dd9ffc1df14c0c4da49a`
- **outcome-neutral checker SHA-256:**
  `bd2938881150d021a7c2b86b437b4a6139b44d8aa129db0e2316123270046720`
- **program core SHA-256:**
  `2cdcfbc96ed4855637fd96d5b5e70eb65eb2887b87158fda391a2e808fc15baf`
- **generated Singular SHA-256:**
  `3cf13a1df4b48d26810e4c6234fbadcf1e76219c4267ab61f4fb2418dee5d055`
- **source graph result SHA-256:**
  `5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1`
- **source graph basis SHA-256:**
  `7f59b5557597f429a3a56914cd5aad5c988902af6d88a3ef01580aaacbdd5d9e`
- **input ledger:** variables `x,t,r,c,b`; coefficient order
  `0,1,2`; `s` degree 2; 48-element dimension-one graph basis
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.07`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The core independently verifies the generic identity

```text
(p2*q0-p0*q2)^2-(p2*q1-p1*q2)*(p1*q0-p0*q1)
  = C0 + C1*s + C2*s^2
```

for affine-linear `qi(s)`. Each completed coefficient is retained in full
with its own SHA-256. Completion supplies exact input for factorization and
low-degree `s,E` resultants; timeout retains a checked coefficient prefix.
Neither outcome alone closes `FFF`.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_q5_coefficients_modal.py
```

**Outcome:** `COMPLETE`. Modal app
`ap-1GgCht615t6eZJCKSKStPA` retained all three coefficient normal forms:

```text
C0: degree 44, 761 terms, SHA-256 98f5a959174f9899da07cb09736ef86dc449e1513821a6741dce19e749bfe913
C1: degree 44, 782 terms, SHA-256 b7defd8474f7a3b04011776833e0b4b9dce44de2c88e41633b797d4b9ce1cf9a
C2: degree 44, 799 terms, SHA-256 3f1f3db22008656b9e98b1966ad0f6f3cff897544d02b48d1ddfc14b6e48990e
```

Result SHA-256:
`25b3ac23d74e0bb710c50d636048c0f95ea4b94d51f3c5e02634cbfdfddf5f6e`.
The checker accepts the complete coefficient ledger and rejects all three
hostile mutations. This replaces regeneration of the 3,126-term whole
normal form but does not close `FFF`.
## Preregistered O0b `FFF` R76 coefficients

- **decision:** form `R76(s)=Res_E(q7,q6)` by the exact quadratic
  resultant identity and reduce its nine possible `s)-coefficients
  separately modulo the admissible base graph
- **scope:** a necessary common-`E` equation for the last open canonical
  `FFF` chart; no equation is adjoined
- **launcher SHA-256:**
  `dd023822f098b72c15504e8176417a21b75b7882fb0451ecaf1029aa51849130`
- **outcome-neutral checker SHA-256:**
  `0e9f1a2c44907dc58b74c40bf28c63d045cfb7acae0f98b58ab285d939199370`
- **program core SHA-256:**
  `7cb0d1b17e2c8175afd59a90be30b84f9409fdad457f3df454119fe2262a22f6`
- **generated Singular SHA-256:**
  `0cf19ceb9bba5f6c2b604f8d352a36c924bc34015538ee7cffe66565768c8d59`
- **source graph result SHA-256:**
  `5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1`
- **source graph basis SHA-256:**
  `7f59b5557597f429a3a56914cd5aad5c988902af6d88a3ef01580aaacbdd5d9e`
- **input ledger:** base variables `x,t,r,c,b`; both input equations
  have `E)-degree 2; coefficient order `0,...,8`; maximum
  `s)-degree 8; 48-element dimension-one graph basis
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.07`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The core reconstructs `q6` from coefficient convolutions, applies

```text
Res(p,q) = (p2*q0-p0*q2)^2
           - (p2*q1-p1*q2)*(p1*q0-p0*q1)
```

to `q7,q6`, and independently verifies the resulting degree-eight bound
symbolically. Each completed coefficient is retained in full with its own
hash. Completion supplies exact input for eliminating `s` against the
banked quadratic `q5`; timeout retains a checked prefix. Neither outcome
alone closes `FFF`.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_r76_coefficients_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app
`ap-VxiiWJZtzNSkcAlUHhTorY` timed out before coefficient 0. The retained
transcript contains only Singular's standard-basis warning, so eager
expansion of the intermediate resultant arrays is the bottleneck, not a
specific final coefficient reduction. Result SHA-256:
`741bd7a2bfb06f3074fe59809a40d5399ec98b65d94386eea6d6cfc95e2fe3b0`.
The outcome-neutral checker accepts the empty exact prefix and rejects all
three applicable hostile mutations. The next architecture performs every
intermediate multiplication in the quotient ring, reducing immediately
modulo the 48-element basis. This eager-expansion program is retired.
## Preregistered O0b `FFF` progressive R76 coefficients

- **decision:** evaluate the same `R76(s)=Res_E(q7,q6)` coefficient
  formulas through progressive reduction modulo the 48-element graph basis
- **scope:** exact quotient-ring rearchitecture of compute request 78; no
  equation is adjoined
- **launcher SHA-256:**
  `fc1ae32daccb795d0ed1ee04b1ac0e3f1757776f37c438ec9513dc01cd2fa5cd`
- **outcome-neutral checker SHA-256:**
  `41e5e3c518d84837502e3345b431f06b6e73eab819f4d204536b34fe2dac994c`
- **program core SHA-256:**
  `4faa057513f7249d75a29143560c397f3a58db265621388450e0b81358ced61b`
- **repaired program core SHA-256:**
  `b73c4e888dc69353bc823c787babdf7c4b8b5d2a4c7efe708ffef16604f045ca`
- **generated Singular SHA-256:**
  `5319dc99297235aaf21a036e1d73c648187b854c06bee004eb55034bc424d6d2`
- **source raw core SHA-256:**
  `7cb0d1b17e2c8175afd59a90be30b84f9409fdad457f3df454119fe2262a22f6`
- **source raw timeout SHA-256:**
  `741bd7a2bfb06f3074fe59809a40d5399ec98b65d94386eea6d6cfc95e2fe3b0`
- **source graph result SHA-256:**
  `5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1`
- **input ledger:** base variables `x,t,r,c,b`; coefficient order
  `0,...,8`; maximum `s)-degree 8; 61 intermediate reductions and
  nine final reductions; 48-element certified standard basis
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.07`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The eight kernel entries and every convolution layer are reduced before the
next multiplication. Raw temporaries are killed after use. The source core's
independent symbolic verification still fixes the resultant identity and
degree-eight bound; only evaluation order changes. Completion retains all
nine coefficients. Timeout retains 61-stage intermediate and nine-stage
coefficient prefixes. Neither outcome alone closes `FFF`.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_r76_progressive_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT` after a repaired rerun. Initial app
`ap-URgjIQYKcEHCmB9QuIKlcd` stopped before Singular because the remote
build path redundantly called the local SymPy verifier, while the minimal
image does not install SymPy. No algebraic stage ran. The repaired core
removes only that remote verifier call; the raw core was reverified locally,
and the generated Singular hash and 70-reduction ledger are unchanged.

Repaired app `ap-Xoiw5moScs3NwvQPlhFuNs` completed all 61 intermediate
quotient reductions and timed out on final coefficient 0. In particular,
`M0[2]=0`, `M1[0]=0`, and the 12 nonzero `M)-coefficients have
1,117--1,202 terms. Result SHA-256:
`0a2173e080a4a5029713aa8fa8feea73056a5e84b8139bc780684d5545117d95`.
The checker accepts all 61 stages and rejects all three applicable hostile
mutations. Since coefficient 0 is exactly `M0[0]^2`, its raw square is the
localized bottleneck. The next architecture retains the 14 `M)-array
representatives before chunked quotient multiplication.
## Preregistered O0b `FFF` R76 bracket bank

- **decision:** rerun the successful 61-stage progressive prefix, retain
  all five `M0`, five `M1`, and four `M2` representatives, and
  exit before final convolution
- **scope:** exact reusable quotient-ring inputs for the nine
  `R76` coefficients; no final product or equation is formed
- **launcher SHA-256:**
  `c5f6acdc04d8598b624bffe23301af808db09977071bd2edfd9d45de93c030e9`
- **outcome-neutral checker SHA-256:**
  `d208460426d0d449bd38636bf4a6e11ed94a852b29f144e468fbddf8e3e2e10b`
- **program core SHA-256:**
  `263de903e787c082d8e426519e50f5112eec7e10093109d9c57340160398949b`
- **generated Singular SHA-256:**
  `2a8614651ff141c5183ce0b69ada1c3fbeb80035f30ea9720525ebacae3486e0`
- **source progressive core SHA-256:**
  `b73c4e888dc69353bc823c787babdf7c4b8b5d2a4c7efe708ffef16604f045ca`
- **source progressive timeout SHA-256:**
  `0a2173e080a4a5029713aa8fa8feea73056a5e84b8139bc780684d5545117d95`
- **input ledger:** 61 intermediate reductions; bracket layout
  `M0[0..4],M1[0..4],M2[0..3]`; 14 outputs; expected exact zeros
  `M0[2]` and `M1[0]`; 48-element certified standard basis
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.07`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The generated program is identical to the successful progressive program
through all 61 intermediate reductions. It then prints and hashes the 14
brackets and exits before `M0*M0-M1*M2` is expanded. Completion creates
the sole source for deterministic chunked products; timeout retains checked
intermediate and bracket prefixes. Neither outcome closes `FFF`.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_r76_brackets_modal.py
```

**Outcome:** `COMPLETE`. Modal app
`ap-WkUJ6xUaL50A2ireij9cYb` completed all 61 intermediate stages and
retained all 14 bracket representatives. The two preregistered zero slots
are exact, and the 12 nonzero slots match the degree/term ledger from compute
request 79. Result SHA-256:
`08dc7fefd108d4b8d17a1c7a5345f37312b65b9a74389cf7e7dfc94827b0446f`.
The checker recomputes every bracket hash, accepts the exact zero pattern,
and rejects all four hostile mutations. This is the canonical source for
final `R76` product sharding; it does not close `FFF`.
## Preregistered O0b `FFF` R76[0] block-square pilot

- **decision:** split `a=M0[0]` into canonical 128-term blocks and test
  the square of block 0 before launching a full product wave
- **scope:** one exact summand of `R76[0]=a^2`; no coefficient assembly
  or equation is formed
- **launcher SHA-256:**
  `b3cfcfffedb25d543bfa8661fbe8cab674e8bbd522e03e4a6060929206b0b9b5`
- **outcome-neutral checker SHA-256:**
  `fd67bc6a4f96cce7fd6346cd9fb1a8f5fed047018d20eff09a92068641843168`
- **program core SHA-256:**
  `e42f2fb807ac8d3813cc6670ea249daefc310965f0cb86d6d57dc0943deb1f7c`
- **generated Singular SHA-256:**
  `6cecc2164f63001457929bf0cde0be287381a482d89ed124b1725484fca73f60`
- **source bracket result SHA-256:**
  `08dc7fefd108d4b8d17a1c7a5345f37312b65b9a74389cf7e7dfc94827b0446f`
- **source polynomial SHA-256:**
  `4dc6a43d99611455c3ffadf53c2f2489f0e252371c280c138377ecc2b0a44839`
- **input ledger:** source has 1,152 canonical terms; block size 128;
  block index 0; half-open term interval `[0,128)`; square multiplier 1;
  48-element certified standard basis
- **envelope:** one CPU, 2 GiB, 60-second Singular child wall and
  90-second container wall; projected cost below `$0.01`
- **local safety:** one RAM-guarded Modal client under a 150-second external
  hard stop; no local CAS

The term splitter verifies exact round-trip reconstruction of Singular's
canonical serialization and checks its 1,152 terms against the retained
bracket stage. Completion retains the reduced block square in full. Timeout
retains the child transcript. This pilot only calibrates deterministic
sharding and has no proof status for `R76[0]` or `FFF`.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 150s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_r76_r0_block_pilot_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app
`ap-At0hOIj97ZuTPfosolIzNn` expanded the 128-term block square to degree
128 with 1,232 terms, then timed out reducing it. Result SHA-256:
`de86481d0a26482f125eb81533f1313996603b2c92453d9ae2f2e4aa55e061d6`.
The checker accepts the timeout and rejects all three applicable hostile
mutations. The bottleneck is high-degree reduction, not raw term count.
Smaller term blocks would create hundreds of shards without addressing the
one-dimensional coefficient geometry, so term-block multiplication is
retired. The next architecture passes to the generic zero-dimensional fiber
over `F_p(t)` and records every denominator as an exceptional finite leaf.
## Preregistered O0b `FFF` generic-t basis

- **decision:** transport the 48-element admissible graph basis from
  `F_p[x,t,r,c,b]` to `F_p(t)[x,r,c,b]` with Singular `imap`, then
  compute and retain the generic zero-dimensional basis
- **scope:** generic fiber of the one-dimensional FFF base graph; all
  coefficient denominators remain explicit open exceptional fibers
- **launcher SHA-256:**
  `fda29f0bf534c6df593140afdd3e80f7e6628d061d278ea3ba088596f9a1e230`
- **outcome-neutral checker SHA-256:**
  `4b4d6ee692eeb7df7e5f239a60cf28699985c562a57a43626f7a76fc9929c854`
- **program core SHA-256:**
  `052089c55b078181415b9fddbac8c9cc1921fe9e768b8fcdb5168ffc465c0e50`
- **generated Singular SHA-256:**
  `bb1a5f9ebfadbe0ab1495be0bed42741516b25011be582d1dd9b72dd23e4a3ad`
- **source graph result SHA-256:**
  `5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1`
- **input ledger:** parameter `t`; fiber variables `x,r,c,b`;
  source dimension 1, basis size 48; target coefficient field
  `F_2130706433(t)`
- **envelope:** one CPU, 2 GiB, 60-second Singular child wall and
  90-second container wall; projected cost below `$0.01`
- **local safety:** one RAM-guarded Modal client under a 150-second external
  hard stop; no local CAS

The pilot retains target dimension, basis size, vector-space dimension, and
the full generic basis with a hash. Completion only establishes the generic
fiber algebra. Every denominator introduced by the basis or later reductions
must be collected, factored over the base field, and handled as a separate
finite-fiber leaf before any FFF promotion. Timeout has no proof status.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 150s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_t_basis_modal.py
```

**Outcome:** `ENGINE_REJECTED`. Modal app
`ap-xIYe6cHFkUBtFeoIUlmDUD` reached the `imap/std` line and Singular
rejected the transcendental coefficient field with
`characteristic is too large (max is 2^29)`, then faulted. No generic
basis was produced and no mathematical status changes. This is the same
engine limitation previously observed for large-prime block orders.
Singular generic-t computation at the deployed prime is retired. The
repository's existing AbstractAlgebra/Groebner.jl pipeline supports
`GF(2130706433)(t)` and is the registered replacement.
## Preregistered O0b `FFF` generic-t Julia basis

- **decision:** convert all 48 admissible graph polynomials from Singular
  compact notation and compute a deterministic, certified Groebner basis in
  `GF(2130706433)(t)[x,r,c,b]` with AbstractAlgebra/Groebner.jl
- **scope:** generic fiber plus a complete rational-coefficient denominator
  ledger; denominator roots remain open finite-fiber leaves
- **launcher SHA-256:**
  `82dc73e5e0abac1015c33a69418d3f9f026f563c052588c969aeffffe7f8c7ee`
- **outcome-neutral checker SHA-256:**
  `106406f18fdc558da9ba0697d080bbdc55cedb078513b589fc969fa70a883b50`
- **program core SHA-256:**
  `a20f75acf0bbe4654ef3467b2a0c05e0e1ec4a3d4cf50439f913abf4ae5a39d1`
- **generated Julia SHA-256:**
  `cd0c5960503ceafb2cca92e072dc2e762035ba1c540b17acb3a2752e84026b0d`
- **source graph result SHA-256:**
  `5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1`
- **input ledger:** parameter `t`; fiber variables `x,r,c,b`; 48
  converted source polynomials; deterministic linear algebra, one task;
  `isgroebner` assertion; quotient-basis dimension
- **output ledger:** full basis; every term coefficient serialized as
  numerator/denominator coefficient arrays in `F_p[t]`; deduplicated
  denominator list and hashes
- **envelope:** one CPU, 4 GiB, 240-second Julia child wall and
  300-second container wall; projected cost below `$0.10`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The parser self-tests compact monomials such as `x2tr3` and converts all 48
source polynomials before launch. Completion requires Groebner.jl's
`isgroebner` certificate, dimension zero, positive quotient dimension, and
complete basis and coefficient ledgers. Every nonconstant denominator
remains an exceptional-fiber obligation. Timeout has no proof status.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_t_julia_modal.py
```

**Outcome:** `COMPLETE`. Modal app
`ap-dshGHUIh6cSEc6EJmDphMN` converted all 48 source polynomials and
certified a dimension-zero, 10-polynomial Groebner basis with quotient
dimension eight. The serialized basis has SHA-256
`661fcbaa51996c4051f799c6ac3c56d95ea213f56305818ffedb6d0859531aa2`.
Its 90 rational-function coefficient entries contain 44 distinct
denominators, whose ordered ledger has SHA-256
`cf5f6cd0bcf52fbc0cd58e5da63d573cabdbea87bda7c91867a3d135ae7f1985`.
The complete result SHA-256 is
`c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e`.

The hostile checker reconstructs the producer's declared coefficient-record
order after the enclosing sorted-key JSON write and rejects all four
mutations. Its repaired SHA-256 is
`f4a88c1fc115c20eb0b584daf2a1b03b7bfb0c05d14052a096978f066a9c2f17`.
This result proves the generic base graph is a finite algebra; it does not
yet impose `q5,q7,q6`, and all denominator roots remain open exceptional
fibers.
## Preregistered O0b `FFF` generic denominator roots

- **decision:** collect every deployed-field root of the 44 generic-basis
  denominators before imposing the FFF necessary subsystem
- **scope:** basis-denominator exceptions only; later generic reductions may
  add further denominator roots
- **source result SHA-256:**
  `c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e`
- **launcher SHA-256:**
  `f6c461bcafcc1f13b3f082d72ac2120f5fa6eb2cd430f07750b304edc01a1cf3`
- **outcome-neutral checker SHA-256:**
  `c99b027800ac50fbc4a5301cdd506d795db5882418ade1428f3a8c38751faaaf`
- **method:** for every denominator compute `gcd(D,t^p-t)` and factor its
  square-free field part; independently repeat on the denominator LCM and
  require equality with the per-denominator root union
- **input ledger:** 44 distinct denominators; degree range 0--42; raw degree
  sum 1,013; field `GF(2130706433)`
- **output ledger:** per-denominator roots and reconstructed linear root
  polynomial; LCM degree/hash; combined root polynomial and exact root list
- **envelope:** one CPU, 1.5 GiB, 180-second container wall; projected cost
  below `$0.03`
- **local safety:** one RAM-guarded Modal client under a 240-second external
  hard stop; no local factorization

The combined root list is exactly the finite set where the current generic
basis may fail to specialize. It has no proof status for `q5,q7,q6`, and it
does not include any denominator introduced by their future reductions.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 240s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_t_denominator_roots_modal.py
```

**Outcome:** first launch `ap-xqXYpg7uKj6R6yoCrP5nRa` was rejected before
factorization because the pinned `fmpz_mod_poly` API has no convenience
`.lcm()` method. No mathematical output was produced. The exact-division
repair completed in Modal app `ap-OWgH6QIeyDAsAMnej0nU6T` in 0.017 seconds.

The raw degree sum 1,013 collapses to an LCM of degree 49. Its deployed-field
root set is exactly

```text
0, 1, 16711679, 666570304, 676802667, 1141382033,
2113994754, 2130706432
```

The per-denominator root union agrees with the independent LCM Frobenius
gcd. The hostile checker reconstructs all 44 linear root polynomials and
rejects all four mutations. Result SHA-256:
`7489a4c860059240395ed0e1b264f5643ba58fe257076781a0bb596e582738b0`.
These eight values are the complete basis-denominator exceptional set;
future reductions may enlarge it.
## Preregistered O0b `FFF` generic necessary subsystem

- **decision:** adjoin `q5,q7,q6` to the certified 10-polynomial generic
  base graph and compute the exact extension over `GF(p)(t)`
- **scope:** generic branch of the necessary subsystem; `q4` remains omitted,
  so emptiness is sufficient for `FFF` but a survivor is only a superset
- **source generic result SHA-256:**
  `c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e`
- **source packet SHA-256:**
  `fbeda61593e73cdcb7bf1e2baa1ebe8b098a7025f834135b3e02d2c291d50cd9`
- **source cache SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **program core SHA-256:**
  `4fb572a9b524f9e05533c7f844f58c529470a1f4aaf25f9de3c9f62a0c61a2d7`
- **launcher SHA-256:**
  `49ea921659240e80303875708169a040c2d45fe76525b2ea0b9df3392597ad51`
- **outcome-neutral checker SHA-256:**
  `509b6b4635007702f464ae89e2225d030cbfae2bb30b86adfda035f6559bc07b`
- **generated Julia SHA-256:**
  `51c308daf9d8136fc26f29f51252a4b6b0a15f1b8ab6efda2c3e73dc3850a260`
- **input ledger:** ten certified base polynomials, quotient dimension eight,
  equations in order `q5,q7,q6`, fiber variables `E,s,x,r,c,b`
- **output ledger:** certified full basis, unit/dimension/quotient profile, and
  all output coefficient numerators and denominators
- **envelope:** one deterministic task, one CPU, 8 GiB, 300-second Julia
  child wall and 360-second container wall; projected cost below `$0.20`
- **local safety:** one RAM-guarded Modal client under a 420-second external
  hard stop; no local CAS

The generic output alone cannot promote `FFF`. Even if it is the unit ideal,
the computation must expose or replace its transformation denominators before
specialization; output-basis denominators and the eight known basis exceptions
are retained but are not presumed complete for the unit certificate.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 420s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_system_julia_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app
`ap-WmwCjoXxq9zHBUxYo4xL44` validated and constructed all 13 input
polynomials, then exceeded the 300-second Julia wall during the first
Groebner computation. It produced no basis or mathematical status. Result
SHA-256:
`13cc45ebcda366c4a659e032f3ea63bddddc2267dc2877f3574d250ca4c84ef5`.
The checker accepts the exact timeout transcript and rejects all three
applicable hostile mutations. The monolithic extension is retired; continue
incrementally with `q5`, then `q7`, then `q6`.
## Preregistered O0b `FFF` incremental generic `q5`

- **decision:** normal-form `q5` modulo the certified generic base and adjoin
  only that quadratic-in-`s` equation
- **scope:** first stage of the incremental `q5 -> q7 -> q6` route
- **source generic result SHA-256:**
  `c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e`
- **source packet SHA-256:**
  `fbeda61593e73cdcb7bf1e2baa1ebe8b098a7025f834135b3e02d2c291d50cd9`
- **program core SHA-256:**
  `7f4845437a558d10ae9a68ad51592bdaea0801eaea17a4abc05a411b944ad2e6`
- **launcher SHA-256:**
  `66da2de96e2e45d12afa5f2d293d02729215d1d60623e72e4c8866ccb4cdfcd8`
- **outcome-neutral checker SHA-256:**
  `847cd8e77d582a58fbc728cfe9e5a3427076f14362ebeca7afa8984bc5eb0b2c`
- **generated Julia SHA-256:**
  `f8b3a2ff817e5651f48c74b3421201a45305de1c7877cf7c23e2a2e1a9caeb5a`
- **input ledger:** ten base polynomials, quotient dimension eight, one
  equation, fiber variables `s,x,r,c,b`
- **output ledger:** full `q5` normal form and hash; certified extended basis;
  quotient profile; combined normal-form and basis coefficient denominators
- **envelope:** one deterministic task, one CPU, 8 GiB, 300-second Julia
  child wall and 360-second container wall; projected cost below `$0.20`
- **local safety:** one RAM-guarded Modal client under a 420-second external
  hard stop; no local CAS

The normal-form and output-basis denominators are retained separately.
Transformation pivots remain open, and no generic stage alone promotes
`FFF`.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 420s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_q5_julia_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app
`ap-G2DYAjHI53OT1Ui7998KuR` exceeded the 300-second Julia wall before the
raw `q5` normal form completed. It produced no normal form, basis, or
mathematical status. Result SHA-256:
`5565e674db92a598d78f9bafcfdf7f2ffab04536ff8e99a223b2e0d9521fe46f`.
The checker accepts the transcript and rejects all three applicable hostile
mutations. Retire raw-resultant reduction and import the already certified
three-coefficient `q5` bank instead.
## Preregistered O0b `FFF` generic `q5` coefficient normals

- **decision:** reduce the three certified coefficients of
  `q5=C0+C1*s+C2*s^2` independently in the eight-dimensional generic base
- **scope:** exact replacement for the retired raw-resultant normal form
- **source q5 bank SHA-256:**
  `25b3ac23d74e0bb710c50d636048c0f95ea4b94d51f3c5e02634cbfdfddf5f6e`
- **source generic result SHA-256:**
  `c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e`
- **program core SHA-256:**
  `d421246f3510b6738c21a45e10532d0b86441377ab27cb5ec17ba736c58a1b37`
- **launcher SHA-256:**
  `3e0793200520967f073f45cfba0fd7fc3150ee8e72521ec6e1a0a803fa3d9fc8`
- **outcome-neutral checker SHA-256:**
  `c520ba5ddc9b41c4201956d271b2be9c9376cb6d2358005a63ed7db80b7e0f48`
- **generated Julia SHA-256 values:**
  `6d5f6107ae3b41ff0976fe9cbc04a51d63be849e39bc604ae65c6009caf266e0`,
  `bcb63f54ccdf2441f7e2cfe7475589209bfc59d41bce73c4b6f07f1b167ab792`,
  `97b935a28c16421fa1ba539f62e97b9d1f4c41394644647e6f1d9a449877f74e`
- **input ledger:** coefficient hashes
  `98f5a959174f9899da07cb09736ef86dc449e1513821a6741dce19e749bfe913`,
  `b7defd8474f7a3b04011776833e0b4b9dce44de2c88e41633b797d4b9ce1cf9a`,
  `3f1f3db22008656b9e98b1966ad0f6f3cff897544d02b48d1ddfc14b6e48990e`
- **output ledger:** one full normal form and rational coefficient ledger per
  coefficient; exact source and generated-program hashes
- **envelope:** three parallel deterministic tasks, one CPU and 6 GiB each,
  300-second Julia child wall; projected aggregate cost below `$0.50`
- **local safety:** one RAM-guarded Modal client under a 420-second external
  hard stop; no local CAS

Completion of all three rows permits exact reconstruction of the generic
quadratic in `s`. A timeout remains local to that coefficient and does not
invalidate completed siblings.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 420s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_q5_coefficients_julia_modal.py
```

**Outcome:** partial exact completion. Modal app
`ap-fjg7OlClGiYgb3VTpj1ygf` completed coefficients 0 and 2; each generic
normal form has fiber degree two and exactly eight quotient-basis terms.
Their hashes are

```text
C0 e008780fd3d46e30c2471900384068de9b384cf3f3a99fbb038d00364b3428c3
C2 e890823e9f38e2919f38a73bcd0b7d20c52882e5ea069a05abfa147f637f8ce8
```

Coefficient 1 timed out before output and remains open. The result SHA-256 is
`29a3236a322bf5ec1b797615fed99ccbb0b584981656eec04bd41da00989700c`.
The checker accepts statuses `[COMPLETE,TIMEOUT,COMPLETE]`, verifies both
complete coefficient ledgers, and rejects all four hostile mutations. Retry
only coefficient 1 under a longer bounded wall.
## Preregistered O0b `FFF` generic `q5` coefficient-1 resume

- **decision:** retry only the sole open coefficient `C1` with its identical
  generated Julia program and a bounded 660-second child wall
- **scope:** complete the middle coefficient of the generic `q5` quadratic;
  do not recompute completed `C0,C2`
- **source frontier SHA-256:**
  `29a3236a322bf5ec1b797615fed99ccbb0b584981656eec04bd41da00989700c`
- **generated Julia SHA-256:**
  `bcb63f54ccdf2441f7e2cfe7475589209bfc59d41bce73c4b6f07f1b167ab792`
- **launcher SHA-256:**
  `deffef33d4335323f938b1aea6be783c8c1d978536999aa0fd746069765a604f`
- **outcome-neutral checker SHA-256:**
  `82d55452bdb88823b494af4ffce651f48379782d41c1ad843cd30ef7d70a8538`
- **envelope:** one deterministic task, one CPU, 8 GiB, 660-second Julia
  child wall and 720-second container wall; projected cost below `$0.30`
- **local safety:** one RAM-guarded Modal client under a 780-second external
  hard stop; no local CAS

If this retry times out, the direct normal-form route for `C1` is retired in
favor of evaluation through the four 8-by-8 quotient multiplication
matrices.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 780s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_q5_c1_resume_modal.py
```

**Outcome:** `COMPLETE`. Modal app
`ap-cAjaWfMQ5IXbHuWAoxPmXR` reduced `C1` to fiber degree two with exactly
eight quotient-basis terms. Normal-form SHA-256:
`76be8227ceaae91dd6e96df64fbc80ee40f058fb9bb94bebaf7f69df66ee702d`.
The result retains eight coefficient entries and six distinct denominators;
result SHA-256
`899f7706130a8ef3d6556ecc14aeda397868dcd8261db5f6df96c85519d3fc1c`.
The checker verifies the complete ledger and rejects all four hostile
mutations. Together with the frontier artifact, all three generic `q5`
coefficients are now complete.
## Preregistered O0b `FFF` generic `q5` bank extension

- **decision:** form the exact 24-term generic quadratic from the three
  completed coefficient representatives and adjoin it to the base basis
- **scope:** certify the first finite extension in the incremental route
- **source generic SHA-256:**
  `c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e`
- **source coefficient frontier SHA-256:**
  `29a3236a322bf5ec1b797615fed99ccbb0b584981656eec04bd41da00989700c`
- **source C1 resume SHA-256:**
  `899f7706130a8ef3d6556ecc14aeda397868dcd8261db5f6df96c85519d3fc1c`
- **program core SHA-256:**
  `fdf8a466238f47623c2ae27771aeb6453a2eece3b736d4793b689d63ad1851ad`
- **launcher SHA-256:**
  `23fd894379f41f34f6891b68b25b6094a98fbd59a445961052b55b794a7c957c`
- **outcome-neutral checker SHA-256:**
  `d4accdf4176b4dfec0660b00298141017504604d33b2cbb9f368981fb297c093`
- **generated Julia SHA-256:**
  `1b0c106ffcc473e138113ed8fd3c48d071dbf6ec66cc802be7f867cc5ea43bc3`
- **output ledger:** input term count, certified basis and quotient profile,
  complete output coefficient denominator ledger
- **envelope:** one deterministic task, one CPU, 8 GiB, 360-second Julia
  child wall and 420-second container wall; projected cost below `$0.25`
- **local safety:** one RAM-guarded Modal client under a 480-second external
  hard stop; no local CAS

The coefficient normal forms are already exact modulo the base ideal, so
adjoining their quadratic generates the same generic extension as adjoining
raw `q5`. Transformation denominators remain open.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 480s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_q5_bank_extension_modal.py
```

**Outcome:** `COMPLETE`. Modal app
`ap-h3NTK3YvbAxOLtnLf7sLZ4` adjoined the exact 24-term quadratic and
certified a nonunit, dimension-zero basis of size 16 with quotient dimension
16. Basis SHA-256:
`bd4b2bf32d58c5f344d8d244eb2632646f0a7ca807bbefc5cf1c9c3737d6ab3b`.
The 192 output coefficient entries contain 100 distinct denominators, whose
ledger SHA-256 is
`125dfc37ef1bf4d8b093b66624408be8120299cc978ecef399f28cfb1df4ccdc`.
Result SHA-256:
`b5320657fc191da5adf2743ad020ab6a30934fd584f7f3f3a995caf9a712953c`.
The checker verifies the complete basis and rejects all four hostile
mutations. Continue with coefficient-wise `q7` over this finite extension.
## Preregistered O0b `FFF` generic `q7` coefficient bank

- **decision:** reduce `a2m,bm`, their squares, and the three coefficients of
  `q7=D0+D1*E+D2*E^2` in the dimension-eight base algebra
- **scope:** staged coefficient construction before adjoining `q7` to the
  dimension-16 `q5` extension
- **source generic SHA-256:**
  `c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e`
- **source packet SHA-256:**
  `fbeda61593e73cdcb7bf1e2baa1ebe8b098a7025f834135b3e02d2c291d50cd9`
- **program core SHA-256:**
  `1a68448c922c0b2bed65973949cf1a19a1bb1459f403da767d85cfdc753fd6cf`
- **launcher SHA-256:**
  `68047af97107271170b16ad6828810cd3480a880a5a72cefe560960d9c5f8c63`
- **outcome-neutral checker SHA-256:**
  `a7194893ed46a3f1df187194dbaa4abeef965d2b5b2813083aa241568264cfb6`
- **generated Julia SHA-256:**
  `69a4e7e889e40fa249aec6ab16f0e5bb7602ce6c8b500fdf6485068716ebc050`
- **output ledger:** seven ordered representatives and profiles, including
  every intermediate; complete rational coefficient denominator ledger
- **envelope:** one deterministic task, one CPU, 8 GiB, 360-second Julia
  child wall and 420-second container wall; projected cost below `$0.25`
- **local safety:** one RAM-guarded Modal client under a 480-second external
  hard stop; no local CAS

All three `Di` are independent of `s`, so their base-algebra representatives
embed unchanged into the `q5` extension. Transformation denominators remain
open.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 480s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_q7_coefficients_modal.py
```

**Outcome:** `COMPLETE`. Modal app
`ap-34Gk6WjaK7Ptlv0Jy93XKc` retained all seven staged representatives.
Every value has fiber degree two and exactly eight quotient-basis terms. The
`D0,D1,D2` hashes are

```text
D0 175919493e8500089bd1d528d2d768b83f9e47df021048ceea6ea637bf9a5b34
D1 1d7f55723f5a0cee8ebe409c879a480637a0b0bd6fa5fb9d2b4a95f25cb7f8dd
D2 d52a21d795e753e4aa04582fa3d67f65003a48b3406383db4a84730b528e961d
```

The 56 coefficient entries contain 24 distinct denominators. Result
SHA-256:
`37e2f17f8546e195024c23766f63cd36ba8681c115f3bf18f7410c19c902c45d`.
The checker verifies every staged hash and rejects all four hostile
mutations. The exact `q7` quadratic is ready for the `q5` extension.
## Preregistered O0b `FFF` generic `q7` extension

- **decision:** adjoin the exact 24-term `q7` quadratic to the certified
  dimension-16 `q5` quotient
- **scope:** second finite extension in the incremental `q5 -> q7 -> q6`
  route
- **source q5 extension SHA-256:**
  `b5320657fc191da5adf2743ad020ab6a30934fd584f7f3f3a995caf9a712953c`
- **source q7 coefficient SHA-256:**
  `37e2f17f8546e195024c23766f63cd36ba8681c115f3bf18f7410c19c902c45d`
- **program core SHA-256:**
  `a0a7cc0c305491c613aeee6d3cace4a84bc488b725e07b35ae186858f582c4fd`
- **launcher SHA-256:**
  `92edd81728c857a154766f933fe03d5ba59acc265b5d788ed99f3276b239212c`
- **outcome-neutral checker SHA-256:**
  `b8c917a95c6191f6fb5424988b894afa0bd6b388f4ab9e82c7b93991f0e383b5`
- **generated Julia SHA-256:**
  `f0977dece0b591d0e84e2e5a6a054eb2f38d70d43e83f1ded53a38da1d2ed98a`
- **output ledger:** input term count, certified basis and quotient profile,
  full coefficient denominator ledger
- **envelope:** one deterministic task, one CPU, 16 GiB, 600-second Julia
  child wall and 660-second container wall; projected cost below `$0.50`
- **local safety:** one RAM-guarded Modal client under a 720-second external
  hard stop; no local CAS

Completion either gives a finite `q5,q7` algebra for the final `q6` test or
proves the generic subsystem already unit. Transformation denominators remain
open in either case.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 720s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_q7_extension_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app
`ap-cPK9VPOH7bzcXjc8ME08LD` constructed the exact 24-term `q7` input but
exceeded the 600-second Julia wall during the Groebner extension. No basis or
mathematical status was produced. Result SHA-256:
`a3d3dd55da213b58af78e415df88c1004348b838e7430c8150234bdb732e0b22`.
The checker accepts the transcript and rejects all three applicable hostile
mutations. Retire the Groebner extension and construct the quadratic
dimension-32 algebra from multiplication matrices instead.
## Preregistered O0b `FFF` `q5` multiplication bank

- **decision:** extract the 16-dimensional quotient basis, regular
  multiplication matrices for `s,x,r,c,b`, and base normal forms of `k0..k5`
- **scope:** reusable exact input for the explicit quadratic `q7` extension
  and final `q6` determinant
- **source q5 extension SHA-256:**
  `b5320657fc191da5adf2743ad020ab6a30934fd584f7f3f3a995caf9a712953c`
- **source generic SHA-256:**
  `c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e`
- **program core SHA-256:**
  `269cc2bea1efb9ee4a16d9a03e6d420df04a88907454f7899324725cdc4508b1`
- **launcher SHA-256:**
  `d1e2239314201b6f68403204b96054547484692c2f5093853412954c7ecfd08f`
- **outcome-neutral checker SHA-256:**
  `8a7770f3df90457124863fca9c4a31c5922a1d7342fd5a2a5faa29e819687f8e`
- **generated Julia SHA-256:**
  `a0e7912ef2092d9fc3a1754f9b261c808c5a6faf5d88a57fa4cc9bb9c5310e4e`
- **output ledger:** ordered quotient basis; five sparse 16-by-16 matrices;
  six kernel representatives and rational coefficient ledgers
- **internal checks:** imported basis is Groebner; quotient dimension 16;
  every variable product reduces into the basis; all five matrices commute
- **envelope:** one deterministic task, one CPU, 16 GiB, 600-second Julia
  child wall and 660-second container wall; projected cost below `$0.50`
- **local safety:** one RAM-guarded Modal client under a 720-second external
  hard stop; no local CAS

This bank is structural. It does not itself impose `q7` or `q6`, and all
matrix-entry denominators remain open specialization obligations.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 720s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_q5_multiplication_bank_modal.py
```

**Outcome:** `COMPLETE`. The first app was interrupted with its local client
at the context transition and left only the fail-closed incomplete
checkpoint. The identical rerun, Modal app
`ap-an7VJ4q5e54gxEGpu8967G`, certified the 16-element quotient basis and five
pairwise-commuting multiplication matrices with 736 nonzero entries. All six
`k0..k5` representatives have fiber degree two and eight terms. Quotient
basis SHA-256:
`aa3090c6c61b29e8a19f456d5a04b826423d9b08eb625d78c62b725ee00b5c8b`;
matrix ledger SHA-256:
`29300862188e3e23b2b4a855c38ca82c0cc93c082932d6bff0fb517f7b71942e`.
Result SHA-256:
`3d216da7d91c82a1360f932673ce3529278c90f81e6a8a6767f14a34ad73a45e`.
The checker verifies every ledger and rejects all four hostile mutations.
## Preregistered O0b `FFF` `q6` block determinant

- **decision:** represent the quadratic `q7` extension as a 32-dimensional
  block algebra and test whether multiplication by the final necessary
  equation `q6` is invertible
- **scope:** exact generic-fiber emptiness for the sole remaining O0b chart;
  exceptional transformation and determinant fibers remain separate
  obligations
- **source multiplication-bank SHA-256:**
  `3d216da7d91c82a1360f932673ce3529278c90f81e6a8a6767f14a34ad73a45e`
- **source q7-coefficient SHA-256:**
  `37e2f17f8546e195024c23766f63cd36ba8681c115f3bf18f7410c19c902c45d`
- **program core SHA-256:**
  `fff178007fdea5ae7c14a0bee59fde6053aacc1a47f7a23f5d0c3bc654ab6224`
- **launcher SHA-256:**
  `7a2dc088c8a9667dde5ec73e5408552d0fc11f6c719ec46b7f5b51a45f570261`
- **outcome-neutral checker SHA-256:**
  `65e2b29fbfc728a2494a137d7d50e5a0d7c2d2fcab5db6bb719fb5f94c2ef19d`
- **generated Julia SHA-256:**
  `d6e3b1aae07a3e89f24c0b65b120d064f665541611dfa858de9db8fd55f754cd`
- **algebra:** first certify `det(M_D2) != 0`; then use
  `M_E=[[0,-M_D2^-1 M_D0],[I,-M_D2^-1 M_D1]]`; verify the exact `q7`
  matrix identity; evaluate `q6`; take its 32-by-32 regular determinant
- **partial-result discipline:** before symbolic determinants, evaluate the
  complete construction exactly at `t=2` over `GF(2130706433)`. A nonzero
  `q6` determinant there proves the rational determinant is not identically
  zero. The witness is flushed and retained even if the later symbolic
  determinant times out.
- **full output:** exact numerator and denominator coefficient ledgers for
  `det(M_D2)` and `det(M_q6)`, suitable for the next exceptional-root pass
- **internal checks:** five source matrices commute; every source denominator
  is defined at the witness; `D2` is a unit; the 32-dimensional `q7` identity
  vanishes; the witness and symbolic `q6` determinants are nonzero
- **envelope:** one deterministic task, one CPU, 24 GiB, 1,200-second Julia
  child wall and 1,260-second container wall; projected cost below `$0.25`
- **local safety:** one RAM-guarded Modal client under a 1,320-second external
  hard stop; no local CAS

Launch command:

```text
RAMGUARD_TIMEOUT=24m tools/ramguard modal -- \
  timeout --signal=TERM --kill-after=15s 1320s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_q6_block_determinant_modal.py
```

**Outcome:** `TIMEOUT` with a complete exact generic witness. Modal app
`ap-KU787KXt0DsHdu2SHy4dhq` evaluated the full 32-dimensional construction
at `t=2`, verified the `q7` matrix identity, and obtained

```text
det(M_D2) = 1573108971 != 0
det(M_q6) =  443644136 != 0
nonzero entries of M_q6 = 1024
```

in `GF(2130706433)`. Therefore the rational `q6` multiplication determinant
is not identically zero and the generic `FFF` fiber is empty. The symbolic
phase also completed `det(M_D2)`, with numerator degree 360 and denominator
degree 60, before timing out while constructing the symbolic q6 matrix. It
did not emit determinant coefficient ledgers, so exceptional roots remain
open. Result SHA-256:
`1757ba06042604cd55e73c923195864ad8214e90fba2ff366574e5d2075f9be7`.
The checker accepts the fail-closed timeout payload and rejects all four
hostile mutations.
## Preregistered O0b `FFF` `R76` multiplication determinant

- **decision:** replace the timed 32-dimensional inverse-based norm by the
  direct quadratic resultant `R76=Res_E(q7,q6)` in the 16-dimensional `q5`
  quotient and test whether multiplication by `R76` is invertible
- **scope:** exact generic-fiber emptiness plus a retained symbolic
  determinant polynomial for exceptional-fiber routing
- **source multiplication-bank SHA-256:**
  `3d216da7d91c82a1360f932673ce3529278c90f81e6a8a6767f14a34ad73a45e`
- **source q7-coefficient SHA-256:**
  `37e2f17f8546e195024c23766f63cd36ba8681c115f3bf18f7410c19c902c45d`
- **source block-program SHA-256:**
  `fff178007fdea5ae7c14a0bee59fde6053aacc1a47f7a23f5d0c3bc654ab6224`
- **program core SHA-256:**
  `ac73c2251e90e6a84b45574dd171474c682586ff56415206d3453f355d49e33f`
- **launcher SHA-256:**
  `d3b296eb0ef62a7260ed725233ee17e390679f45c3bcadfad76eaa1e853d0a9b`
- **outcome-neutral checker SHA-256:**
  `c638bd5b045f92670b47b84046cf3b99652edca69965663917365fb71483ad3d`
- **generated Julia SHA-256:**
  `5f72b5b9f53b6a1c6d9138052fbd9e6f379b4fa617b47ad72d5daa98989c5eb9`
- **resultant identity:** write `q6(E)=y0+y1 E+y2 E^2`; then
  `R76=(D2*y0-D0*y2)^2-(D2*y1-D1*y2)*(D1*y0-D0*y1)`
- **route advantage:** no inversion of `D2` is used. If multiplication by
  `R76` is invertible, `q7` and `q6` cannot have a common root, including at
  fibers where the quadratic leading coefficient degenerates.
- **witness control:** at `t=2`, the determinant must equal `244686406`,
  independently forced by `1573108971^2 * 443644136` in the prime field
- **full output:** numerator and denominator coefficient ledgers of the
  16-by-16 `R76` multiplication determinant
- **envelope:** one deterministic task, one CPU, 24 GiB, 1,800-second Julia
  child wall and 1,860-second container wall; projected cost below `$0.25`
- **local safety:** one RAM-guarded Modal client under a 1,920-second external
  hard stop; no local CAS

Launch command:

```text
RAMGUARD_TIMEOUT=34m tools/ramguard modal -- \
  timeout --signal=TERM --kill-after=15s 1920s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_r76_multiplication_determinant_modal.py
```

**Outcome:** pending.

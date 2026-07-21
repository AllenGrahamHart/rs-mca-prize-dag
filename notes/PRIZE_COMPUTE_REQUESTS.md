# Proximity Prize deferred compute requests

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

## Request queue

| priority | request | readiness | contributor action | current authorization |
|---|---|---|---|---|
| P1 | CR-002 quotient-pencil rank-two classification | matched `c=0` and generic `c=1` norm contracts are complete; c2 parity shares them conditionally on C2-PAR; minimum support in the one-antipodal route is reduced to one explicit pair-collision curve; compressed implementations and pilots are missing | screen the `M=2^35` top norm and 36-level tower first; use `CR-002-C2CELL-COLL` for the separate one-pair design request | algorithm request only; cost unknown |
| P2 | CR-001 H3 high-excess certificate | blocks are formula-generated; a complete dense `n=8` Taylor conformance oracle is banked; sparse/distributed implementations and comparative cost pilots are missing | first match the `n=8` hashes and support sets, then compare Smith, Taylor cutoffs `2<=c<=35`, and three-resultant screening on larger complete orders; evaluate `(36,1)` only on retained official primes | no large run; cost unknown |
| P3 | CR-003 rate-half Hankel sharp-cap census | ready for an external exact pilot | enforce the distance-three `e+3e` MDS router, then price the first complete chamber | external request only; cost unknown |
| P4 | CR-004 WCL terminal four-slot classification | all four slots have fixed unit-ideal endpoints | compute and factor four compact integer certificates, beginning with the three-variable `(1,5)` ideal | external request only; do not duplicate support fleets |

Priority records expected proof value, not an instruction to spend. A request
remains unauthorized until a contributor accepts its resource cap. If a PR
cannot vendor the proved router, the checker, and the PASS/FAIL DAG contract,
it should link this ledger as future work rather than solicit the computation.
Cost estimates are conservative ceilings and must include failed shards and
retries; raw artifact storage is separate.

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

Requests are added only after algebraic preprocessing has made the search
space auditable. At present CR-001 through CR-004 are the only large runs
meeting that bar; the other open critical lanes still need theorem-level
compression before a large computation would be responsible. CR-004 is a
handoff record, not permission to duplicate work that may already be running
in the canonical worktree.

### Grande Finale v3 handoff index

The current reviewed upstream snapshot is
`przchojecki/rs-mca@57e39fba`. Contributor requests should use its six-input
vocabulary and state which interface the computation serves:

| upstream v3 input | local request | handoff status |
|---|---|---|
| row-sharp finite Q / prefix max-fiber | QF pre-request below; parts of W3 | needs a complete profile compiler before large compute |
| exhaustive first-match atlas and residual charts | W3, XR, and L1 pre-requests | theorem/algorithm work first; raw witness sweeps are not complete |
| Sidon/Fourier or effective-image MI+MA | QF pre-request; F2 falsification dossier | no proof-grade large run currently defined |
| residual ray compiler | CR-001 plus XR and HGE4 pre-requests | CR-001 is direct local certificate work; support counts alone do not pay rays |
| exact extension and quotient payments | CR-002 and CR-004 | bounded symbolic endpoints exist; preserve every field ledger |
| summed integer certificate per adjacent row | CR-003, W3, and the eventual final compiler | exact pilots or specification materialization, never exponent-only evidence |

The mapping is many-to-many. A local request may support an upstream input
without being equivalent to it. In particular, CR-001's H3 collision target
is stronger and more specialized than generic max-fiber Q, while a Q or SP
certificate cannot be reported as an MCA ray certificate unless the packet
also includes the required RS incidence multiplicities.

### Pre-request QF: row-sharp finite Q / Sidon certificate

This pre-request separates two problems that must not be conflated:

1. `f2_growing_order_myerson` is a universal growing-order max-to-mean
   theorem on Frobenius moving sectors. Its extensive finite watch has not
   found a falsifier, but no finite campaign can prove its asymptotic
   quantifier.
2. Grande Finale v3's deployed-row Q obligation is a finite, row-sharp
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

The current upstream benchmark packets identify necessary ceiling-normalized
moment orders `94196`, `94991`, `641594`, and `680397` for their four stated
adjacent routes. These are route diagnostics, not an instruction to enumerate
all `r`-tuples. A responsible algorithm must use symbolic recurrences,
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

### Pre-request W3: official residual-envelope certificates

The critical leaf `ww_row_envelope_clause` asks for an exact per-word,
first-match challenger bound against the residual integer allowance left by
the paid QA.22 columns. A complete external certificate campaign would be
high value: PASS would close the only open truth input of
`worst_word_challenger_pricing`, while FAIL could produce an official word
that forces a revision of the safe-side profile.

It is not runnable from the present repository. The bounded source audit in
`critical/nodes/ww_row_envelope_clause/specification_frontier.md` identifies
four missing inputs: a complete official-row registry, the exact field line
for each row, the exact paid-column subtraction table, and a full-scope
paid/residual ownership theorem. Without those data, neither
`B_chal(c)` nor the residual first-match input space is machine-defined.
Additional toy or selected-row challenger censuses therefore do not count as
progress on W3 and should not be requested.

Promote this item to a numbered contributor request only after one
machine-readable materialization packet supplies:

1. every row key `(characteristic, extension degree, n, k, sigma)` and its
   exact generated field;
2. exact `q_line`, `B*=floor(q_line/2^128)`, the minimum-#493 branch, and
   every paid-column integer subtraction;
3. a proved exhaustive, disjoint first-match ownership map for paid and
   residual challengers; and
4. a finite residual-cell compiler covering all layouts, scalar choices,
   and received words.

The eventual campaign must stream one independently checkable certificate
per official row. PASS must verify that all residual cell allocations sum to
at most `B_chal` and upper-bound every cell for every word. FAIL must emit one
replayable official row, word, ownership trace, and exact challenger total
exceeding the residual. Incomplete output may reveal a missing cell class but
cannot alter W3's status. The first contributor task is thus specification
materialization and theorem-backed compilation, not a large Modal census;
there is no responsible cost estimate or authorization yet.

### Pre-request XR: nondeep tangent/support-mismatch atlas

The support-wise audit adds the critical target
`xr_tangent_support_mismatch_bridge`. A smooth exact rate-`1/4` fixture shows
why it is necessary: outside the deep range, one globally tangent pair can
have more support-wise bad slopes than the `n-A+1` tangent slot. The fixture
is a regression test, not evidence about an official candidate.

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

There is no responsible large run yet. A raw search over pairs, supports, or
Maxwell cores would have no finite completeness boundary and could not prove
the official universal statement. A future contributor-scale computation is
valuable only after a theorem supplies all of:

1. a finite aggregate compiler for the union of generic full-external-zero
   charts, avoiding a sum over all zero sets;
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

After those items exist, promote this to a numbered request. PASS must emit a
complete cell manifest proving the two slot bounds at every routed official
row. FAIL must emit one replayable official pair and its witness supports.
Incomplete runs may improve the atlas but cannot change a node status. Until
then this is an upstream theorem/algorithm request, with no cost estimate and
no authorized Modal or external run.

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
- **Exact input:** a declared dyadic level `m`, characteristic `p` containing
  `mu_m`, and every width `4<=h<=m/4-1`. The proved complement-third,
  dual-gap, and cyclotomic-norm gates make every larger width empty;
  generating those shards is a checker failure, not conservative coverage.
  Generate left-anchored near-square
  bases `(S,a)` satisfying `S(1)=a`, the non-full condition,
  `S^2-a^2 | X^m-1`, and `S^2-a^2` not dividing `X^(m/2)-1`. Apply the exact
  primitive stabilizer test and canonicalize scaling orbits.

  Before allocating any live lower-quarter shard, write `h=m/4-d`, put
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
  them, and charge no positive necklace debit. The live range is exactly the
  lower-quarter region `e>=h+4`.

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
  necklace debit and compares the lower-quarter total with `(21/2)m^2`.
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
  differential identity. Reject every production width with `h>=m/4` and
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
  Burnside necklace formula. Reject any production manifest containing
  `h>=m/4`. Replay the historical necklace value `286` for `(32,9,5)` as a
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
first-match source-chart key. The support-pattern and syndrome enumeration is
already polynomial for fixed `P`; recomputing it cannot change the DAG.

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
from a finite aggregate owner for the non-intrinsic source charts.

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
or aggregate first-match overlap across source charts. The thin next-strip
region now has its own `q^p` CRT theorem, so it is also excluded from future
raw sweeps. Fixed-boundary quotient-core enumeration is mathematically
redundant.

The symmetric core-polarity closure removes another misleading experiment:
large one-sided boundary caused by almost-full fibers is already polynomial
when the number of holes is bounded. Any future L1 computation must target
growing symmetric core polarity, not merely growing `beta`. It still needs a
finite normal form or stabilization theorem and a cross-chart ownership
contract before becoming a numbered request.

The finite normal form is now known algebraically but not yet finite in the
growing parameter: `F_D L_H=L_S product(P-a)` with
`deg L_H+deg L_S=p_core`. A future contributor request must operate on this
signed quotient-mark system and certify a degree-independent component
classification, stabilization threshold, or explicit natural-scale owner.
Enumerating defect subsets, full-fiber choices, or bounded signed marks is
out of scope; none can decide the remaining uniform theorem.

Intrinsic source-chart enumeration is also redundant: one complete-fiber
partition has at most `3^(n/ell)=poly(n)` canonical charts at the cutoff, and
the dyadic scale count is logarithmic. A future compute request may address
chart multiplicity only after a finite model for partial-core or
non-intrinsic/contributor-dependent charts is proved. Raw generation of
intrinsic chart assignments cannot affect the DAG.

Bounded partial-core charts are now redundant compute targets as well. The
triple-polarity closure counts them globally using layout polarity,
core-defect polarity, and petal polarity. A future intrinsic-chart request
must target a theorem-compressed growing-polarity regime and emit a signed or
natural-scale classification; sampling cores with fixed exception counts
cannot advance the frontier. Non-intrinsic chart requests still require a
finite complete chart generator before promotion to this ledger.

Promote this to a numbered compute request only after either item 1 or item 2
is proved:

1. a degree-independent component/normal-form theorem reducing the
   sub-Johnson, unbounded-cross-slack affine one-direction cells and all `c`
   to a finite symbolic classification for each fixed `P`; or
2. an explicit stabilization bound `c_0(P)` together with a complete theorem
   covering `c>c_0(P)`, plus a finite generator for the residual cells.

Any global first-match request additionally needs a finite canonical generator
for the non-intrinsic source charts in scope.

The resulting request must classify the complete finite residual, retain the
source chart, missing-equation syndrome, homogenizing direction, and the
coprimality conditions `gcd(F,J)=gcd(F,A_i)=gcd(F,A_j)=1`, and emit a
counterexample witness or a checkable component certificate. Until that gate
is met, an upstream PR should present the affine split-pencil compiler as a
theorem frontier and invite the missing uniform argument, not request a large
sweep.

## CR-001: H3 fixed-order high-excess / double-accident certificate

- **status:** BLOCKED ON AN EFFICIENT OFFICIAL-SCALE CUTOFF-35 SCALAR
  ELIMINATION ALGORITHM. The candidate support is exact; no measured
  implementation exists. The complete toy-order benchmark is done; do not
  launch a raw orbit fleet.
- **consumer:** `f3_h3_mobius_excess_half` (C36').
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
  estimate.
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
  dollars on a strictly smaller complete order; until then total cost is
  unknown and no local Modal launch is authorized. Completed shards must
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

- **status:** DEFERRED EXTERNAL HANDOFF. All four slots now have exact
  fixed-dimensional unit-ideal endpoints. The canonical ledger's reported
  `(ell,w)=(1,5)` support stream is evidence and an independent cross-check,
  not the preferred proof route. No current Modal run is authorized.
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
  optimized estimate of `10,500--14,500` CPU-hours (`$1.9k--$5.3k`). It also
  has an unresolved `Norm(u)`-saturation soundness gap. Do not launch it;
  prefer the sparse certificate lift or a new quotient/obstruction theorem.
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
- **first action:** implement the generic straight-line equation generator
  and independent identity checker, then benchmark modular Groebner or
  arithmetic-circuit elimination on `(1,5)` in FLINT/Singular/Magma. The
  pilot must emit a replayable transcript and estimate the eventual integer-
  coefficient and factorization cost. Do not start `(1,6)`, `(2,7)`, or
  `(4,9)` merely because the generator is available; authorize them only
  after the smallest pilot identifies a viable elimination order and hard
  resource envelope. Separately obtain the
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
- **Singular image fence:** app `ap-o5JxJJpiYoJnPSIaUkeV2b` was cancelled
  during image initialization because Debian `apt_install("singular")`
  pulled a disproportionate Sage/Jupyter/development stack. The function
  never started and no Groebner computation ran. Do not retry that image.
  Use a prebuilt minimal Singular image or a contributor installation. The
  exact generator and record are
  `experiments/prize_resolution/dli_wcl_15_pruned_singular_pilot_modal.py`
  and `experiments/prize_resolution/dli_wcl_15_pruned_singular_pilot_result.md`.
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

CR-004 is intentionally one grouped request because all four leaves use the
same ambient split and certificate vocabulary. Contributors may close slots
independently, but should not open four incompatible compute frameworks.

## CR-003: Rate-half Hankel sharp-cap component existence census

- **status:** EXTERNAL EXACT PILOT REQUEST. Do not run on the current laptop or
  the remaining low-credit Modal account.
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
  Therefore CR-003's distance-three decision is now exactly:

  ```text
  does an official pair-Lagrange generator realize the exact external
  split design?
  ```

  A positive certificate is a genuine far-CA counterexample to the proposed
  cap; a complete nonexistence certificate closes the distance-three chart.

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
- **execution shape:** checkpoint by
  `(family,shape,core,m,e,q,component packet)`, omitting `core` only for
  `A=3`; stream compact certificates and hashes; stop a shard before memory
  pressure rather than materializing all split locators. Contributors may
  parallelize independent shards, but each shard must have a declared wall,
  RAM, and dollar ceiling.
- **estimated resources:** unknown until `m=2,4` pilots; likely unsuitable for
  the current sub-`$1` policy and potentially multi-gigabyte at `m=16`.

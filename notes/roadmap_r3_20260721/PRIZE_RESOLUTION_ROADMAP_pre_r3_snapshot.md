# Provenance snapshot (2026-07-22): master PRIZE_RESOLUTION_ROADMAP.md immediately before the r3 date-free supersession (custody #104). The divergence-era content is preserved verbatim below.

# Proximity Prize full-resolution roadmap

Status: working research charter and execution roadmap.

Date: 2026-07-12.

Authority: `dag.json` is the local status and dependency authority. The
critical surface is described by `critical/CRITICAL.md`. Przemek's current
upstream research priorities are stated in the upstream `agents.md`, with
`experimental/asymptotic_rs_mca_frontiers.tex` as the asymptotic manuscript.

Snapshot reviewed for this revision: canonical `prize` commit `ec226d6` and
Przemek upstream main commit `36de5bfc`.

This document is not itself a proof and does not change any node status. Its
purpose is to make progress cumulative: every successful increment should
close a claim, replace a false claim by a correct one, or reduce a named open
claim to strictly smaller obligations whose dependency graph is explicit.

## 1. Objective and final certificate

Resolve both official problems:

1. support-wise MCA for every admissible smooth Reed-Solomon row and every
   official rate `rho in {1/2, 1/4, 1/8, 1/16}`;
2. the corresponding list/interleaved-list problem for every constant
   interleaving arity required by the official statement.

For each input row `C`, the final output is a certified map `f(C)` returning
the largest safe radius. In agreement coordinates, the certificate has the
adjacent form

```text
B* = floor(epsilon* Q_C)
U_C(a0 + 1) <= B* < L_C(a0),
```

where:

- `Q_C` is the exact denominator for the object being bounded;
- `L_C(a0)` is a proved lower count giving an unsafe witness at agreement
  `a0`;
- `U_C(a0 + 1)` is a complete proved upper ledger at the next agreement;
- endpoint and closed-ball conventions convert `a0 + 1` to the returned
  `delta*_C` without ambiguity.

The proof problem is therefore two-sided. An upper theorem alone cannot prove
maximality, and a lower obstruction alone cannot prove safety.

## 2. Current proof frontier

At the date above, the critical orbit contains:

```text
186 PROVED
 27 CONDITIONAL
 14 UNPROVED
```

The red leaves (fourteen at authoring; twelve after the 2026-07-12 ww-cluster
import: W2 proved, W1 walled) are the atomic decomposition of three broader kernel
families. This compression is useful for strategy, but it is not permission to
assert one universal kernel theorem without proving each consumption bridge.

The full-DAG validator additionally reports three root-critical artifact
closure targets: `compiler`, `dossier_partial`, and `harness`. They are not
additional mathematical conjectures, so they do not appear among the fourteen
truth-apt leaves. They remain mandatory engineering deliverables and are
handled in WP8.

### 2.1 K2-centered rigidity and ray family: nine leaves

| node | actual open content | nearest useful deliverable |
|---|---|---|
| `f2_growing_order_myerson` | growing-order Gaussian-period/max-to-mean control | a source-specific theorem within the very generous F2 consumer tolerance |
| `f3_h3_three_to_one_c36` | the corrected C36' three-to-one count | an algebraic proof of the printed count, or a weaker filtered count that still pays `R_3` |
| `f3_hge4_aggregate_budget` | fully stripped aggregate over every `h >= 4` | a uniform aggregate theorem, not a list of unrelated fixed-`h` computations |
| `xr_highcore_collision_count` | high-core post-strip slope count | a collision-core classification and actual-ray count within the allocated budget |
| `xr_lowcore_spread_heart` | low-core anti-concentration in sup form | a source-specific spread/ray theorem at the six clean-rate candidates |
| `dli_prime_weighted_large_block_support` | correlated joint reserve at nested conditional junctions | a precise C2''-type joint-reserve theorem; factorized transfer is not available |
| `ww_row_envelope_clause` | DIRECT per-word/per-cell count-vs-allowance envelope (W1's certificate obligation absorbed, R2; min-#493 branch baked in) | an independently checkable per-row upper certificate at the exact residual allowance |

The enlarged K2 schema is a coordination device. Its real frontier splits into
at least four mathematically different tasks:

1. realized-image max-fiber/Sidon control;
2. small-core and higher-dimensional ray classification;
3. exact finite constants where less than one bit is available;
4. joint reserve across state-dependent tower junctions.

An attempted reduction to K2 counts as progress only when it proves an
instance map and leaves an obligation strictly simpler than the original
consumer. Renaming a consumer as an instance of K2 is not a reduction.

### 2.2 K4 petal and image-fiber family: four leaves

| node | actual open content | nearest useful deliverable |
|---|---|---|
| `petal_g1_layer_maps` | exhaustive layer-map supply for arbitrary received word, with joint chart multiplicity | a witness-exhaustive layer compiler with actual per-word multiplicity control |
| `petal_g2_support_forcing` | current closure form is vacuous; the true issue is the small-scale/pricing seam | prove the stabilizer partition, then reassign scales `M <= t` explicitly to G3/K4 or a named paid column |
| `petal_g3_pricing_multiplicity` | per-word codeword multiplicity for canonical staircase data, plus the repaired conversion identity | prove the general conversion identity and the sub-`k` per-word charging bound |
| `petal_k4_primitive_bound` | primitive auxiliary image-fiber bound in the consumed top band | a chart-level primitive theorem after periodic contributors are charged separately |

The periodic staircase lower floor is real and must remain a separate paid
profile. A generic image-fiber theorem that ignores it is false.

### 2.3 K5 rate-half razor family: one leaf

`rate_half_band_closure` asks for the exact determination of the narrow
rate-`1/2` razor band. This is a lower-witness problem if the current predicted
crossing is correct. It may instead be resolved by a stronger safe-side theorem
that moves the crossing. Either outcome is acceptable; preserving the current
conjecture is not the objective.

K5 is intentionally isolated. Upper-bound rigidity or petal theorems cannot by
themselves construct unsafe witnesses through the band.

### 2.4 Scope debt outside the fourteen leaves

The grand-list statement quantifies over each constant `m`, while the current
green `m_handling` note explicitly covers only the affordable range (roughly
`m <= 16..31`, depending on the row) and says larger constants require
`a_regularity_forcing` or an equivalent theorem. That node is currently outside
the critical root ancestry.

Before claiming full list resolution, do one of the following:

1. wire the large-`m` obligation into the critical DAG and prove it;
2. prove a different uniform-in-constant-`m` conversion;
3. narrow the root statement, with an official-source justification that the
   narrower scope is the complete challenge rather than partial credit.

Closing the fourteen current leaves is not, by itself, permission to ignore
this boundary.

## 3. Crosswalk to Przemek's five hard inputs

Use upstream terminology in upstream-facing work. The older `Q/BC/SP` names
may appear as cross-references, but the primary descriptions should be the
five current frontiers-paper inputs.

| upstream hard input | local critical content | exact missing output |
|---|---|---|
| witness-exhaustive first-match atlas | G1, the corrected G2/G3 routing, worst-word taxonomy, and the proved payment taxonomy | every actual bad slope enters exactly one first-match cell, with no omitted witness and with projection degree priced |
| image-scale MI+MA or direct Sidon payment | F2 summit, XR low-core, W3, primitive K4, and portions of the quotient boundary | a theorem at the realized image scale, not at a formal ambient codomain |
| residual ray compiler for higher-dimensional balanced cores | F3 C36'/HGE4 and XR high/low-core predicates | an actual distinct-slope bound after all named strips; support counts or moments alone do not suffice |
| complete profile-envelope comparison with the target | G3, W1/W3, quotient/field-drop profiles, and the corridor compiler | a complete `U_C(a)`, including every field-drop and remainder profile at its own natural scale |
| lower reserve/unsafe-side comparison | W2, simple-pole/distinct-ray witnesses, and K5 | an explicit `L_C(a)` crossing the target at the adjacent unsafe point |

Two local/upstream claims are equivalent only after a written bridge checks:

- the exact object (MCA, CA, list, interleaved list, line decoding);
- the exact row and field scope;
- support representatives versus realized images or actual slopes;
- sup, mean, averaged, or existential quantifier order;
- generated, base, ambient, line, challenge, and list fields;
- finite constants versus exponent-only asymptotics;
- endpoint and agreement conventions.

A same-name match is evidence for a bridge, not a proof of one.

## 4. Dependency-ordered execution program

### WP0. Specification and bridge integrity

Deliverables:

1. an object/field/endpoint dictionary shared by the critical DAG and the
   upstream frontiers paper;
2. a checked mapping from every upstream hard input to the exact local
   consumer edges;
3. repair of the large-`m` list scope debt;
4. a bounded audit of the latest upstream experimental packets, promoting
   only statements whose hypotheses and proofs have been independently read.

Exit gate: every claimed bridge has a short proof or remains explicitly
conditional. No root claim has an admitted scope not represented in its req
ancestry.

### WP1. Witness-exhaustive structural router

Build the complete first-match router before proving a primitive theorem about
its residual. Include quotient, dihedral, planted/petal, field-descent,
rank-defect, orientation, image-collapse, ray-saturation, and balanced-core
profiles.

The router must prove both:

1. detection/exhaustiveness: every actual bad slope is assigned;
2. payment: each detected class has a theorem or exact certificate controlling
   its actual slope projection.

Constructibility, support cardinality, or a raw collision moment is not
payment.

Local targets: G1; G2 disposition; the algebraic half of G3; the relevant W1
and W2 taxonomy seams.

Exit gate: a first-match partition theorem plus a ledger table in which every
cell is marked `PAID_BY_THEOREM`, `PAID_BY_EXACT_CERTIFICATE`, or
`CONDITIONAL_ON_NAMED_INPUT`. There is no anonymous residual.

### WP2. Primitive realized-image theorem

Prove the analytic payment on the genuine primitive residual. The current
high-value route is a source-specific exponential-regime inverse
Littlewood-Offord/max-fiber theorem for moment-curve or weighted-Vandermonde
subset-sum maps. A different direct Sidon payment is equally acceptable.

Do not target an unrestricted ambient identity-normalized theorem: upstream
has counterexamples. Preserve effective image size and representation
multiplicity throughout.

Candidate consumers, each needing its own verified bridge:

- F2 growing-order Myerson;
- XR low-core spread;
- W3 row envelope;
- primitive K4 auxiliary lists.

DLI joint reserve remains a sibling task unless the theorem explicitly handles
state-dependent nested junctions.

Exit gate: at least one official consumer closes, and every additional claimed
consumer has a checked instance map rather than an analogy.

### WP3. Residual ray and shift-pair compiler

Attack actual slope counts after the five strips. The recommended order is:

1. C36' at `h=3`, because it is a pure finite count with a large observed
   margin and an exact conditional close;
2. XR high-core collision count, using the pair-moment identity only as an
   instrument;
3. XR low-core spread heart, coordinated with WP2;
4. HGE4 as a uniform aggregate theorem.

Fixed-`h` proofs are valuable only when they feed a proved width cap or a
uniform summation argument. Accumulating many small-`h` results without such a
bridge does not close HGE4.

Exit gate: the upstream residual-ray input is proved on the required
smooth/circle classes, and the local F3/XR consumers receive exact finite
constants.

### WP4. Petal/image-fiber closure

After WP1 fixes routing and WP2 supplies the primitive theorem:

1. prove arbitrary-word layer-map supply and joint chart multiplicity;
2. make the G2 stabilizer statement green and move its real pricing debt to
   the correct node;
3. prove G3's per-word sub-`k` multiplicity and conversion identity;
4. instantiate the primitive theorem on each supplied chart.

Exit gate: `petal_growth` and then `imgfib` promote through wired modus ponens,
with the periodic staircase floor retained as an explicit profile.

### WP5. Complete upper envelope and clean-rate MCA

Construct `U_C(a)` from the paid cells. For prime/no-field-drop rows, use the
proved identity-dominance criterion where applicable. For field-drop rows,
retain every quotient profile at its own generated-field scale.

Resolve exact constants only after the profile list is complete. The finite
adjacent rows cannot consume `poly(n)`, `K^{O(1)}`, or unspecified
subexponential losses when the margin is sub-bit.

First prize milestone: exact MCA determinations at rates `1/4`, `1/8`, and
`1/16`.

Exit gate: for every clean-rate row, a replayable adjacent certificate
`U(a0+1) <= B* < L(a0)`.

### WP6. Clean-rate list side

Close the petal and worst-word packages, then resolve the large-constant-`m`
scope. Keep list size, image-fiber size, line slopes, and interleaved common
support distinct.

Second prize milestone: exact list determinations at rates `1/4`, `1/8`, and
`1/16` for the full required constant-`m` scope.

### WP7. Rate-half endgame

First formalize the precise per-row worst-word/pincer crossing used by K5.
Then pursue genuinely different mechanisms:

- a new priced witness family beyond the `n/256` quotient plateau;
- a joint/averaged conversion that preserves actual distinct slopes;
- a B2b-type balance theorem;
- a stronger safe-side theorem that moves the crossing.

Do not reopen killed AQB, dihedral-window, or fixed quotient-depth routes
without a materially new mechanism.

Exit gate: adjacent MCA and list certificates at rate `1/2` for every razor
row, regardless of whether the final crossing agrees with the current window
law.

### WP8. Certified compiler, formalization, and submission

Turn the proved ledger into a deterministic compiler that emits:

- input descriptor and all field ledgers;
- `B*`, `a0`, `a*`, and `delta*`;
- every upper-ledger term and lower witness count;
- exact adjacent inequalities;
- endpoint conversion;
- provenance hashes and replay commands.

Add an independent verifier that reads only the certificate and public row
descriptor. Promote stable theorem statements into the paper and formalize the
small logical spine after the mathematics has stopped moving.

Exit gate: both grand nodes and packaging are `PROVED`, the critical validator
passes, and a clean checkout reproduces every official certificate.

## 5. Incremental claim discipline

### 5.1 One increment, one claim contract

Before doing proof work, write a claim contract containing:

```text
claim id:
mathematical statement:
quantifiers and row scope:
consumer node and exact slot:
current status:
dependencies already proved:
new open content:
falsifier or failure witness:
proof route being attempted:
replay command, if computational:
upstream hard-input mapping:
```

The statement must be the weakest convenient form that the consumer accepts.
Do not strengthen it for elegance.

### 5.2 Directed acyclic subgraphs for new propositions

Conditional proofs may introduce new propositions recursively, but every such
decomposition must be recorded in `dependency_subdag.md` beside the frontier
node or in an equivalent machine-readable manifest.

Rules:

1. edges point from prerequisite to consumer;
2. every leaf is either already `PROVED` or is an honest open target;
3. no speculative conditional chain may hide multiple untested conjectures;
4. a decomposition is accepted only if at least one leaf is materially simpler,
   independently attackable, or reusable by another consumer;
5. an equivalent-strength restatement is marked `BLOCKED`, with a reopening
   criterion, rather than counted as progress;
6. if a proposed decomposition grows faster than it closes, retract to the
   nearest comprehensible frontier under `CHAIN_COMPRESSION_POLICY.md`.

### 5.3 Status promotion law

- `PROVED`: a complete human-readable proof exists. Every logical dependency
  is proved down to leaves. A computation claim additionally has a pinned
  certificate and replayable verifier.
- `CONDITIONAL`: the implication from exact wired hypotheses to the claim is
  proved. Every hypothesis appears as a req edge.
- `TARGET`: an open truth claim and a logical leaf, except for staged artifact
  closure allowed by the critical validator.
- `EXPERIMENTAL` or `AUDIT`: useful evidence outside the critical status
  taxonomy; never silently consumed as a theorem.
- `COUNTEREXAMPLE`: the attacked statement or mechanism is false. Repair or
  re-route before further consumption.

No node is promoted because a route looks routine, a computation has no
counterexample, or a stronger conjecture is widely believed.

### 5.4 Proof audit gate

Every proposed proof promotion receives two reads:

1. construction read: verify the algebra, inequalities, and referenced inputs;
2. consumer-backward read: grant the statement and verify that it actually
   supplies the consumer's quantifier, object, field, and constant.

For high-impact or nontrivial claims, the second read should be fresh-context
and independent. It should receive the statement and required interfaces, not
the author's preferred proof narrative.

The audit checklist is:

- exact statement copied from the claim contract;
- no missing hypotheses or prose-only assumptions;
- no sup/mean, support/image, moment/slope, or base/extension drift;
- boundary and degenerate cases handled;
- cited theorem hypotheses checked at the actual parameters;
- no circular use of the target or an equivalent-strength lemma;
- constants and normalization independently recomputed;
- verifier mutation/tamper test fails when a load-bearing value changes;
- consumer implication replayed after any statement repair.

Audit outcomes are `NO ISSUE`, `FIXED`, `OPEN GAP`, or
`COUNTEREXAMPLE_NEW_FLOOR`.

### 5.5 Computation discipline

The laptop is a coordination and light-replay machine. Use Modal for nontrivial
enumeration, algebra systems, large exact integers, or parallel sweeps.

#### Local RAM safety

The local WSL instance has about 7.5 GiB RAM and 2 GiB swap. On 2026-07-13,
three unguarded Python runs reached 6.4, 6.9, and 7.1 GiB resident memory and
forced WSL restarts. Two failures came from a supposedly probe-only audit that
materialized `set(range(...))` at an official parameter near `2^40`; the other
came from an unguarded local validator. A stated state-count estimate is not a
memory limit.

No autonomous agent may launch an unguarded local Python, Sage, algebra-system,
compiled experiment, or wrapper that invokes one transitively. Use the
repository cgroup wrapper:

```text
tools/ramguard tiny  -- python3 <static-or-small-verifier.py>
tools/ramguard local -- python3 <proved-bounded-local-check.py>
tools/ramguard local -- tools/dag_commit.sh
tools/ramguard modal -- ~/.venvs/modal/bin/modal run <remote-job.py>
```

The profiles cap the complete local process tree:

| profile | RAM max | swap max | wall limit | intended use |
|---|---:|---:|---:|---|
| `tiny` | 256 MiB | 64 MiB | 60 s | static checks and small deterministic verifiers |
| `local` | 1 GiB | 256 MiB | 5 min | explicitly bounded local replay only |
| `modal` | 1.5 GiB | 256 MiB | 12 h | local upload/orchestration/result client; remote resources are unaffected |
| `agent` | 2.5 GiB | 512 MiB | 24 h | optional outer fail-safe for an autonomous Codex/Fable process |

The `agent` profile is defense in depth: where the launch surface permits,
start each autonomous agent with
`tools/ramguard agent -- <agent command>`. Its cap includes the agent and all
forgotten local children, so a violation may kill that agent session but
should not kill WSL. Commit or checkpoint before long runs.

Do not raise a local profile to rescue a computation. Move the work to Modal.
An exception is allowed only for non-computational packaging whose measured
working set is understood and whose reason is recorded in the campaign
ledger. `RAMGUARD_TIMEOUT` may extend a wall limit, but it does not alter the
memory ceiling.

#### Modal safety

Modal functions may request as much remote RAM, CPU, and duration as the
mathematical job justifies. RAMguard constrains only the local Modal client.
Every Modal job must:

1. declare remote `memory`, `cpu`, and `timeout` explicitly;
2. upload only the required source/data subset, or record and inspect the
   bounded repository upload size;
3. checkpoint partial results remotely before timeout;
4. shard independent rows and stream reductions rather than collecting all
   shard payloads into one local list;
5. keep large artifacts in a Modal Volume or equivalent remote store and
   return only compact structured certificates;
6. put a deterministic local checker under `tiny` or `local`, never replay the
   expensive search locally;
7. treat a local-client RAMguard kill as a job-design failure: reduce upload
   or return volume instead of increasing the laptop limit.

Default rules:

1. pre-register the quantity, falsifier, and interpretation before running;
2. use a 60-second first-pass job and write partial results incrementally;
3. use longer Modal jobs only when the first pass shows a concrete reason and
   the script still checkpoints partial output;
4. shard independent rows instead of building one memory-heavy process;
5. pin seeds, parameters, image versions, wall time, and peak-memory estimate;
6. write structured JSON plus a small deterministic checker;
7. validate the script on a brute-force row where the answer is independently
   known;
8. do not infer a proof from survival, scaling plots, or absence of a found
   counterexample.

Numerics should decide between proof routes, find counterexamples, calibrate a
constant, or validate a certificate. Endless auditing without a decision is
not progress.

## 6. Integration and one-writer workflow

### 6.1 Worktree hygiene

Every autonomous campaign starts from a fresh clone or worktree of the latest
canonical `prize` branch and uses its own branch. Never edit canonical `prize`
or another agent's worktree directly.

The campaign keeps a ledger with, for every increment:

```text
date and commit
claim id
consumer and dependency edge
artifact paths
proof/audit/falsification verdict
replay commands and resource use
status or DAG change
upstream portability classification
next blocking obligation
```

One writer performs DAG surgery and canonical integration. Contributors submit
small commits whose mathematical scope is explicit.

### 6.2 Local node packet

A mature local increment should contain, as applicable:

```text
critical/nodes/<id>/statement.md
critical/nodes/<id>/proof.md or conditional.md
critical/nodes/<id>/attack.md
critical/nodes/<id>/frontier.md
critical/nodes/<id>/dependency_subdag.md
critical/nodes/<id>/verify.py
critical/nodes/<id>/cert/
```

Proof text is primary. Verifiers check finite algebra, arithmetic, certificates,
and mutation guards; they do not replace an unformalized general proof.

After any status, node, or edge change, run:

```text
tools/ramguard local -- tools/dag_commit.sh
```

Commit generated orbit artifacts only through that ritual.

### 6.3 Upstream-ready packet

An increment is upstream-portable when it helps one of Przemek's five current
hard inputs and can be understood without the local DAG vocabulary.

Preferred packet shape:

```text
experimental/notes/<lane>/<descriptive_upstream_name>.md
experimental/scripts/verify_<descriptive_upstream_name>.py
experimental/data/certificates/<packet>/...
experimental/agents-log.md entry
```

Each upstream note must include:

1. status label: `PROVED`, `CONDITIONAL`, `CONJECTURAL`, `EXPERIMENTAL`,
   `AUDIT`, or `COUNTEREXAMPLE`;
2. theorem or counterexample in upstream terminology;
3. proof with every imported hypothesis named;
4. exact connection to one of the five hard inputs and relevant paper labels;
5. explicit nonclaims;
6. verifier and certificate semantics;
7. lightweight replay commands and resource expectations;
8. the next open mathematical line.

Use standard-library verifiers where reasonable. Avoid local path assumptions,
large generated artifacts, and edits to paper TeX/PDF unless the maintainer asks
for promotion. Group tightly related lemmas into one coherent PR; do not open a
PR per tiny DAG node.

Before publishing upstream:

1. replay from a clean checkout;
2. run syntax/compile checks and `git diff --check`;
3. perform the consumer-backward audit;
4. verify that every nonclaim in the local packet remains explicit;
5. compare against current upstream main to avoid duplicate or stale work;
6. open as a draft for experimental integration unless a theorem promotion was
   explicitly requested.

Negative packets are valuable when they provide a replayable counterexample,
identify the exact false premise, and state the repaired frontier. A report that
only says a route failed is not upstream-ready.

## 7. Prioritization rule for each autonomous turn

At the start of each turn:

1. update from canonical `prize` and inspect current upstream main;
2. re-run the critical validator and read the active frontier ledger;
3. choose exactly one primary increment by this order:
   - repair a root-scope or wiring defect;
   - finish a proof that can immediately promote a node;
   - prove a shared lemma that closes or strictly reduces multiple consumers;
   - falsify a high-risk red premise at its actual crux;
   - perform a bounded experiment that decides between named proof routes;
4. state its claim contract before working;
5. finish proof, verifier, audit, DAG update, and ledger entry before switching
   targets;
6. if the increment closes, move to the next highest-value target;
7. if it decomposes, choose between proving a new leaf and returning to an
   existing leaf based on downstream leverage and truth confidence;
8. if it fails, bank the negative result and change the route instead of
   repeating a cosmetically different version.

Suggested near-term order:

1. WP0 cross-spine and large-`m` scope repair;
2. C36' as the cleanest genuine finite theorem opportunity;
3. G2 disposition and W2 endpoint/taxonomy closure as small exact repairs;
4. first-match projection-degree payment;
5. realized-image inverse-LO/Sidon theorem;
6. XR ray compiler and HGE4 aggregate;
7. petal K4 closure;
8. clean-rate adjacent certificates;
9. K5 rate-half endgame.

This order may change when a proof or counterexample materially changes the
DAG. Do not change it merely because a computation lane is easy to continue.

## 8. Credit-bearing milestones

The project should publish partials as soon as they are genuinely complete:

1. unconditional asymptotic MCA theorem under no-field-drop or another fully
   proved row class;
2. exact finite MCA determinations at clean rates;
3. exact finite list determinations at clean rates and the covered `m` range;
4. full constant-`m` list theorem;
5. exact rate-half MCA determination;
6. exact rate-half list determination;
7. uniform certified compiler and complete submission.

Each milestone must state its row, rate, field, object, and `m` scope. Partial
credit is not permission to title a narrower theorem as the full prize.

## 9. Full termination conditions

The resolution campaign ends only when all of the following hold:

1. every logical leaf needed by both grand roots is `PROVED` down to its leaves;
2. every conditional on the root paths auto-discharges or has a direct proved
   replacement;
3. the large-constant-`m` list scope is either proved or officially shown not to
   be part of the full challenge;
4. every official row has adjacent safe/unsafe certificates;
5. the compiler and independent verifier reproduce those certificates from a
   clean checkout;
6. object, denominator, field, and endpoint audits have no open axes;
7. the critical DAG validator and generated orbit pass;
8. the results are packaged in a submission-quality paper/dossier;
9. upstream-relevant proved results and counterexamples have been offered to
   Przemek in coherent, replayable packets.

## 10. Proposed standing goal text

```text
Resolve the two Proximity Prize problems represented by the canonical `prize`
repository. Work in a fresh clone or worktree of the latest canonical branch,
never directly in `prize`. Continue autonomously until every required critical
leaf is PROVED down to proved leaves, every root-path conditional discharges,
the full constant-m list scope is covered, and replayable adjacent safe/unsafe
certificates plus a certified `f(C)` compiler exist for every official row.

Use `notes/PRIZE_RESOLUTION_ROADMAP.md` as the execution charter. On each turn,
choose one primary increment: repair a scope/wiring defect, close an existing
red node, or decompose a node into strictly simpler named propositions. Record
every new dependency as a directed acyclic subgraph. Do not create speculative
conditional chains, count equivalent-strength reformulations as progress, or
promote numerical survival to proof. A node is fully closed only when its proof
is complete down to proved leaves and it can be promoted to PROVED under the
critical three-color law.

Maintain a claim contract and campaign ledger for every increment. Audit each
proof both forward and consumer-backward, independently for high-impact claims.
Use Modal for nontrivial computation; default to checkpointed 60-second probes,
extend only with a documented reason, and keep laptop work light. Run every
local Python computation through `tools/ramguard tiny|local`, and run the local
Modal launcher through `tools/ramguard modal`; never raise a laptop memory cap
to avoid moving work remote. Stream or remotely persist large shard results
instead of collecting them in local memory. Verify every counterexample
against the real object and bank negative results as repaired frontiers or new
explicit floors.

Keep local work upstream-portable. For every result relevant to Przemek's five
hard inputs, prepare a self-contained experimental note, lightweight verifier,
certificate where appropriate, explicit status and nonclaims, current paper
label mapping, and agents-log entry. Prefer coherent grouped draft PRs over one
PR per node. Use upstream terminology: witness-exhaustive first-match atlas;
image-scale MI+MA or direct Sidon payment; residual balanced-core ray compiler;
complete profile-envelope comparison; and lower reserve/unsafe-side comparison.

When one node closes, update and validate the DAG, then proceed to the next
highest-leverage obligation. Do not stop at a plan, a conditional theorem with
untracked premises, or a volume of small-case evidence. Stop only at full
termination under section 9 of the roadmap, or when explicitly paused by the
user.
```

---

## Master addendum r1 (2026-07-12, post-integration; maintainer)

1. LEAF-TABLE RECONCILIATION: master's surface carries ELEVEN red leaves,
   not ten — the K4 petal family (section 2.2) is three leaves: G1, K4,
   and `petal_small_scale_staircase_census` (minted as the price of the
   G2 flip: the M <= t class needed an OWNER node, not only a routing
   assignment — KB #33, catch #80). The section's own prose ("the
   periodic staircase lower floor is real and must remain a separate
   paid profile") already agrees; the table predated the bundle.
2. WP2 STALL CRITERION (amendment): WP2 (realized-image inverse-LO/Sidon
   theorem) is the plan's single hardest bet with four consumers. Pin a
   fallback: if no WP2 increment survives audit within a bounded number
   of attempts, the consumers decouple onto their independent lanes
   (summit -> the Dedekind/L-function lane; W3 -> the direct certificate
   route; XR low-core -> the E27/SCK program; K4 -> chart-level census).
   The switch trigger is a route decision to be taken explicitly, not by
   drift.
3. EARLY RATE-HALF WITNESS LANE (amendment): WP7's witness hunt starts
   NOW at low intensity, not after WP5/WP6 — it is the plan's terminal
   risk and the highest-information falsification target for the window
   law (either a new priced family beyond the n/256 quotient plateau, or
   sustained absence sharpening the first-moment confidence). Runs in
   the falsification track alongside the proof program.
4. #493 DEPENDENCY (WP5): the sub-bit-margin constants discipline is
   gated by the pending upstream conventions ruling (issue #493); both
   branches are pre-planned (constant-exact vs poly), and the W3-direct
   min-branch baking means a ruling can only relax the ww lane.
5. DIVISION OF EXECUTION: Codex's loop runs sections 4/7 (proving);
   master runs the audit gate (every import cluster-audited at a pinned
   SHA — KB #32-#35 pattern), the falsification track (red-quality
   Q-SURV lanes), and upstream mining. One-writer on master unchanged.


## Master addendum r2 (2026-07-13, wave-4)

Section 2.2 update: K4 is CLOSED at the chart level (wave-4 package with
the weighted G1 atlas; KB #46). The petal family's open leaves are the
G1 atlas supply and the unified row-level sub-Johnson successor
(quotient_row_subjohnson_bound — also the census gate's lemma). Section
2.1 update: dli holds M1+M2 survived rounds and the M3 posing; W3 carries
the aggregate allocation law (R1'). The e0a2aa7 arity-scope
reconciliation is accurate and incorporated; note the branch copy of this
file lost addendum r1 (catch #122) — master's copy is authoritative.

## Integration note r6 (2026-07-13, exact quadratic MCA rows; imported
## wave-6 with w6-C2 rewording)

Upstream `rs-mca@9262f63c` supplies a self-contained quadratic mean-overlap
theorem. Independently reconstructed locally, it proves that the support-wise
full-field MCA numerator is exactly `r+1` whenever

```text
(n-r)^2 >= n(k+r).
```

Four certified power-of-two multiplicative-subgroup rows, one at each official
rate and with `k=2^40`, place the target `2^-128` exactly on the adjacent
quadratic boundary. If `B=floor(p/2^128)`, their safe real-radius set is
`[0,B/n)`, their largest safe grid radius is `(B-1)/n`, and the supremum
`B/n` is unsafe. The local packet replays all four Proth witnesses, target
divisions, and adjacent signs using exact integers.

This realizes the milestone-2 shape on four particular eligible rows (the
first exact full-MCA determinations at all four official rates); the corridor
clean-rate rows and the WP5 exit gate remain open (w6-C2). It does not close
a critical red: the canonical roots quantify over separately frozen
near-capacity/corridor rows, `rate_half_band_closure` fixes a different
roughly 256-bit razor row and also contains an ordinary-list obligation, and
the quadratic theorem makes no list claim. The DAG records an evidence edge
to `mca_grand`, with all critical leaves unchanged.

## Integration note r7 (2026-07-13, wave-7: the WCL-ZONE ladder;
## consolidates the branch's r11-r17 + schedule note per w7-C7
## renumbering)

Eight Codex commits audited at pin 554144a3 and imported with repairs:
the raw-ledger interface guardrail (decision 4(a) settled by theorem —
C1' consumes the RAW primitive ledger; catch #198 was a misapplied
ledger), the schedule correction r2 (w7-C1: production dims are the
dyadic tower (2^32,...,2,1,1), t = 2^33 — not N_L = 256L), the
terminal weight-3/weight-4 ambient exclusion censuses (no q < 2^256
with v_2(q-1) >= 41 divides any weight-3/4 cyclotomic norm on 256
exponents), the weight-5 first-64-primes MITM probe (w7-C4 scope
sentence added), the ell-2 weight-3 census + weight-4 Newton
exclusion, and the NEWTON SHORT-WINDOW CUTOFF THEOREM (w <= 2ell
impossible, sharp at 2ell+1, field-uniform) which closes every window
at ell >= 8 — 30 of 34 production levels outright. Maintainer
ratifications 4(a)/(b)/(c) recorded 2026-07-13. NET: WCL-ZONE is now
EQUIVALENT to six finite zero-event emptiness slots (ell,w) =
(1,5),(1,6),(2,5),(2,6),(2,7),(4,9), all q-dependent (the A1-PROD
density-vs-row gap). Full record: notes/kernel_basis/
WAVE7_AUDIT_FINDINGS.md.

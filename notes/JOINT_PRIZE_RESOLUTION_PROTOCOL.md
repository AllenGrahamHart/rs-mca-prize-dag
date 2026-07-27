# Joint Proximity Prize resolution protocol

This is the operating contract for the joint-resolution goal. It governs
work in the Codex tree, exchange with `przchojecki/rs-mca`, and the evidence
required for completion. It does not prove a mathematical claim or change a
DAG status.

Current strategy remains in `PRIZE_RESOLUTION_ROADMAP.md`. The ranked
export/harvest inventory remains in
`convergence_ledger_20260724/CONVERGENCE_LEDGER_R1.md`. Correspondence data
remain in `correspondence/JOINT_CROSSWALK.json`, and deferred computation
remains in `PRIZE_COMPUTE_REQUESTS.md`. This file controls procedure when a
dated plan or ledger conflicts with the current goal.

## 1. Mission and terminal condition

Resolve both Proximity Prize grand challenges, ordinary LIST and MCA, for the
actual challenge specification. A counterexample that relocates a threshold
is a valid route to resolution; preserving a conjectured threshold is not an
objective.

The goal is complete only when all of the following are established from the
current trees and clean replays:

1. `list_grand`, `mca_grand`, and `prize` are unconditionally `PROVED`.
2. The complete critical requirement closure is green. No `TARGET`,
   `CONJECTURE`, `PROVABLE`, unresolved `CONDITIONAL`, or truth-apt artifact
   remains on a critical route.
3. Every false critical premise has a certified counterexample and a correct
   proved replacement route.
4. The maximal-safe map, or an equivalent certificate procedure, proves the
   returned numerator safe and the adjacent numerator unsafe for every row
   required by the challenge.
5. Every shared terminal in the joint crosswalk is discharged locally and is
   bankable or accepted in Przemek's completion program.
6. The dossier, provenance, crosswalk, exact certificates, proof sources,
   endpoint conventions, and clean-checkout deterministic replays are
   complete.
7. An adversarial completion audit checks the original prize definitions and
   rejects completion by a special case, chosen ledger, conditional compiler,
   numerical experiment, or formalized conjecture.

Official acceptance by prize judges is external to the proof audit. The
internal terminal is a submission-ready, peer-auditable resolution of both
mathematical problems and a matching bankable upstream completion package.

## 2. Authority and workspace custody

Use these authorities in order:

1. the actual Proximity Prize definitions and row contracts;
2. proved source mathematics and exact certificates;
3. `dag.json` for our current statuses and dependency graph;
4. current upstream `agents.md` and its named live compiler for upstream
   workboard status;
5. this protocol for procedure;
6. the roadmap, convergence ledger, crosswalk, and compute ledger for their
   declared roles.

The canonical directory `/home/u2470931/smooth-read-solomin/prize` is
read-only ground truth controlled by Fable. Work only in the designated Codex
clone or a purpose-made outbound PR clone. Fetch canonical changes and
fast-forward or integrate them without modifying canonical files or reverting
Fable's uncommitted render artifacts.

Treat `/home/u2470931/smooth-read-solomin/rs-mca` and
`przchojecki/rs-mca` as read-only upstream sources during harvest. Prepare an
outbound PR in a dedicated branch/clone. Never overwrite Przemek's stable
papers; upstream packets begin in the current `experimental/` interface unless
his workboard says otherwise.

At the start of a work cycle, record:

```text
our branch and SHA
canonical prize SHA
upstream main SHA
open upstream PR numbers relevant to the selected lane
critical TARGET/CONDITIONAL counts
crosswalk validation status
```

Unmerged upstream PRs are provisional. They may supply warnings, possible
counterexamples, or methods, but are not established suppliers. Do not race a
live PR. An independently reconstructed theorem may be used only with its own
complete proof and explicit provenance/non-overlap audit.

## 3. Work-cycle selection

Each substantial cycle must combine movement toward the local critical DAG
with the two-way integration program. Select work in this order:

1. a critical node or exact child with a plausible closure, falsification, or
   threshold-relocation event;
2. a shared crosswalk terminal where one proof can pay both programs;
3. an upstream harvest with a concrete `ev -> req` promotion test against a
   critical node;
4. a fully proved local result that maps cleanly to a current upstream
   workboard item;
5. required dossier or reproducibility work attached to one of the above.

Do not substitute infrastructure volume for mathematical movement. A status
map, schema, survey, Lean skeleton, toy scan, or additional necessary
condition is not progress by itself.

Every cycle ends with a short burn-down record:

```text
starting and ending pins
node/workboard item attacked
result: CLOSED / FALSIFIED / NARROWED / HARVESTED / EXPORTED / NO MOVEMENT
DAG status or dependency delta
upstream terminal delta
delta-star bracket movement, in bits when defined
new assumptions and whether they are shared
live compute requests
next route-deciding action
```

Two complete export-plus-harvest cycles with zero joint bracket movement
trigger the convergence strategy's self-kill: retain sound results, stop
spending cycles on exchange machinery, and return effort to direct critical
red closure. This changes strategy, not the terminal condition.

## 4. Mathematical and DAG status discipline

Statuses are truth claims, not confidence labels.

- `PROVED`: a complete proof exists at the printed scope and all required
  dependencies are proved. Computational proofs additionally satisfy section
  9.
- `CONDITIONAL`: the printed implication is proved, but one or more exact
  named hypotheses remain open. Each hypothesis has an owner, falsifier, and
  dependency edge.
- `TARGET`: an unresolved statement currently required by a live route.
- `CONJECTURE` or `PROVABLE`: useful classification only; neither is green.
- `REFUTED`: an exact counterexample invalidates the printed statement. No
  live critical route may continue to require it.

Prefer complete proved statements. Mint a conditional child only when it is:

1. exact and unambiguous;
2. logically necessary or sufficient for a named consumer;
3. materially smaller than its parent;
4. independently falsifiable;
5. assigned a recursive attack; and
6. wired in an explicit acyclic dependency subgraph.

Do not promote a node from survival evidence, failed falsification, a bounded
sample, a nonunit component, or a verifier that checks only arithmetic around
an unproved theorem.

For every new theorem node, bank at least:

```text
statement.md
proof.md or an exact proof certificate
claim_contract.md
dependency_subdag.md
audit.md
result.md
lineage/provenance information
primary verifier and an independent audit where computation is load-bearing
```

Keep `req` and `ev` edges distinct. An `ev` edge becomes `req` only after an
explicit transport theorem binds the supplier's field, row, object, scope,
normalization, quantifier, unit, and owner chronology to the consumer.

## 5. Falsification and threshold relocation

For every red premise and high-risk amber premise, state the smallest useful
falsifier before testing it. Check exact algebraic constructions before broad
searches. An amber implication is normally attacked at its premise; if the
implication itself fails, record that separately.

When a counterexample lands:

1. replay it independently using exact arithmetic;
2. identify its precise kill scope;
3. mark the false statement `REFUTED` and remove it from live critical
   requirements;
4. propagate regressions through every dependent node;
5. repair the statement only if the corrected scope remains useful and true;
6. otherwise rewire toward the correct threshold or proof architecture;
7. update the maximal-safe map and unsafe floor if the challenge threshold
   moves.

Failed attempts to falsify are evidence only. Record the tested domain,
coverage, power, and blind spots; never call resistance a proof.

## 6. Crosswalk and two-axis status

`notes/correspondence/JOINT_CROSSWALK.json` is the correspondence source of
truth. Primary local node IDs never rename. Prefer upstream terminology in
conversation and PRs; store it as aliases.

Relations mean:

- `IDENTICAL`: identical only at the printed scope and backed by a
  machine-verified or proof-checked chain;
- `OVERLAP`: useful common structure, with no substitution theorem;
- `ANALOGY_ONLY`: no proof transport; `chain` remains null and the blocking
  mismatch is printed;
- `OURS_ONLY` / `HIS_ONLY`: no current counterpart.

Never widen a scoped identification silently. In particular, the current F2
identification is zero-prefix only, the current L1 identification is `e=0`
only, and the rate-half band/Q row is analogy-only.

Track two independent axes:

```text
status_ours: mathematical truth in our DAG
status_his: upstream bankability/acceptance at the pinned upstream scope
```

A complete local proof may set `status_ours=PROVED` without waiting for PR
triage. Upstream acceptance must not manufacture local truth. A shared item is
jointly complete only when the local theorem is proved and the upstream
bankability key is satisfied. This two-axis rule supersedes any older wording
that kept a mathematically proved local statement conditional solely because
upstream review was pending.

After each upstream integration wave, re-pin every affected row, run
`tools/verify_crosswalk.py`, and attach a crosswalk diff to the wave audit.
The critical snapshot and crosswalk travel with substantive mathematics; do
not submit them alone as progress.

## 7. Harvest procedure

For an upstream theorem:

1. pin immutable upstream commit, file, label, and exact statement;
2. classify it as refutation, proved harvest, conditional harvest, route cut,
   method only, duplicate, or irrelevant;
3. reconstruct the proof independently and replay all exact arithmetic;
4. audit field, domain, object (LIST/CA/MCA), quantifier, projection, unit,
   endpoint, normalization, and first-match ownership;
5. state what the theorem does not prove;
6. mint a local supplier only after the audit supports its status;
7. add an `UPSTREAM_IMPORT_LEDGER` row and scoped crosswalk update;
8. wire `ev` first unless a complete transport theorem justifies `req`;
9. print the exact promotion test that could turn evidence into a requirement;
10. run the relevant DAG, verifier, and mutation checks.

Synthesis papers are indexes, not proof sources. Follow their citations to the
actual theorem or certificate. Static/hash/schema success is preflight only.

## 8. Outbound PR procedure

Normally keep at most two open PRs, in distinct upstream lanes. Before
drafting, fetch current main and all open PR metadata, check the TAKEN/RACED/
CLEAR registry, and perform a theorem-subtraction audit against the current
upstream papers. Consolidate rather than opening a stream of small PRs.

Every packet uses current upstream terminology and begins with the bankability
contract required by current `agents.md`:

```yaml
workboard_item: K0/K1/K2/K3/K4/K5/M0/M1/M2/L/T
row: exact row name
object: MCA/LIST/CA/LINE/OTHER
target_epsilon: exact value or not applicable
agreement: exact integer
B_star: exact integer or not applicable
direct_statement: exact theorem or inequality
architecture: DIRECT or exact architecture id
partition_digest: required unless DIRECT
atom_or_cell: exact owner/atom, or DIRECT
quantifier: exact maximum/uniform/existential statement
projection_and_unit: slopes/rays/codewords/supports/pairs
claimed_bound: exact integer or symbolic theorem
status: PROVED/CONDITIONAL/CONJECTURAL/EXPERIMENTAL/AUDIT/COUNTEREXAMPLE
impact: ROW_CLOSURE/ROW_COUNTEREXAMPLE/BANKABLE_ATOM/ARCHITECTURE_BRIDGE/ROUTE_CUT/LOCAL_ONLY
falsifier: explicit invalidating condition or witness
replay: commands and immutable source hashes
```

Also include:

- proof and dependency source pins;
- independent replay and mutation results;
- exact nonclaims and remaining bridge to the row numerator;
- local node and scoped crosswalk mapping;
- overlap/race audit against current main and open PRs;
- provenance and attribution;
- a distinct **Compute requests** section when section 10 applies.

Do not sell an MCA slope numerator as a LIST bound, a support census as a
slope/codeword count, a local payment as a bankable first-match atom, an
asymptotic loss as an exact finite reserve, or a formalized hypothesis as a
theorem. A correspondence/status artifact accompanies a theorem packet and
is never the packet's claimed mathematical progress.

If an outbound wave remains untriaged for more than ten days, keep working in
our tree, consolidate the next wave, and use an already negotiated register
channel where applicable. Do not duplicate or pressure-review the stalled PR.

## 9. Verification and reproducibility

Analytic proof review checks every hypothesis, denominator, exceptional
characteristic, endpoint convention, quantifier, and local-to-global step.
At least one audit should reconstruct the argument without relying on the
author's verifier.

A load-bearing computational result requires:

1. exact inputs and immutable source hashes;
2. a proved finite completeness router;
3. deterministic integer or exact-field arithmetic;
4. canonical compact output with coverage accounting and hashes;
5. a primary implementation and independently written checker;
6. hostile mutation tests;
7. resumable checkpoints and useful partial output;
8. explicit PASS, FAIL, and INCOMPLETE semantics;
9. registration in the verifier manifest.

Use focused checks under RAMguard. Typical commands are:

```text
tools/ramguard tiny -- python3 <node>/verify.py
tools/ramguard tiny -- python3 <node>/verify_audit.py
tools/ramguard local -- python3 tools/verify_prize_dag.py
tools/ramguard local -- python3 tools/verify_crosswalk.py
tools/ramguard local -- python3 tools/verify_critical_harness_coverage.py
tools/ramguard local -- python3 tools/run_all_verifiers.py --run --match <scope> --jobs 2 --timeout 30
tools/ramguard local -- python3 tools/run_all_verifiers.py --refresh-manifest
```

Run manifest refresh only when registered assets change. A bounded or partial
full-suite run must be reported as such. Before committing, run
`git diff --check`, inspect all status/edge changes, and ensure generated DAG
artifacts are refreshed when required by repository policy.

## 10. RAM and computation law

The WSL host is RAM-fragile. All local commands run through `tools/ramguard`.
Use `tiny` for reads, exact arithmetic, and short node verifiers. Use `local`
only for bounded orchestration or verifier batches known to stay below 1 GiB.
Do not run exploratory enumeration, large CAS elimination, broad compilation,
or memory-uncertain computation locally.

Modal is permitted only when all of these hold:

1. the task is route-deciding for a named node or pre-registered falsifier;
2. conservative total wall time is below five minutes;
3. conservative total cost is below `$1`;
4. a certificate, deterministic local checker, checkpoints, partial-output
   contract, and hard shutdown are prepared before launch;
5. the launch and app ID are logged in `PRIZE_COMPUTE_REQUESTS.md`.

Use the `modal` RAMguard profile for the local Modal client. Total campaign
cost/time, not per-container cost/time, controls authorization. Parallel
containers do not multiply the budget. No run costing tens or hundreds of
dollars is in scope.

Any valuable run exceeding either limit, having unknown cost, threatening the
remaining credit, or lacking a complete checker is not launched. Record it as
a pre-request or contributor request in `PRIZE_COMPUTE_REQUESTS.md` and carry
it into the relevant upstream PR. A request must state:

```text
mathematical decision and upstream interface
proved completeness router
exact rows/parameters
source commit and command
small pilot and measured cost, if available
hard CPU/RAM/time/dollar ceiling
checkpoint and partial-output contract
certificate and independent checker
PASS effect on the DAG
FAIL effect on the DAG
INCOMPLETE: evidence only, no status change
raw-artifact location and compact manifest hashes
```

No unbounded search is a contributor request. First vendor the algebraic
compression and identify the missing compiler, pilot, or coverage theorem.

## 11. Governance and shared completion

Maintain a who's-on-it field or companion board for shared/raced objects.
Attribute every theorem and certificate at node level in both directions.
When a cross-repository defect is found, repair the proof source first, regress
both status ledgers, update every dependent node/packet, and preserve the
counterexample/audit provenance.

The current upstream terminal checklist is `(S)` spread routing, `(A)`
large-owner control, `(E)` exception routing, and list completion, plus its
exact row-certificate workboard. This list is a snapshot, not a permanent
definition; refresh it from current `agents.md` and the live compiler before
every outbound packet.

The final completion audit must reconcile:

- all local critical TARGETs and CONDITIONAL assumptions;
- all current upstream terminal inputs;
- every `IDENTICAL` and `JOINT` crosswalk row at its exact scope;
- every official row's maximal safe and adjacent unsafe certificate;
- the maximal-safe function/compiler against the proof statements;
- clean-checkout deterministic replay and statement-to-source matching;
- a nonclaim ledger with no assertion needed by the final theorem.

No PR count, green hash, successful build, paper draft, or partial award
posture satisfies this terminal audit.

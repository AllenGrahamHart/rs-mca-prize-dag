# PREREG — k3_orientation_assembly (round 30)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation beyond the two
named anchors. AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `critical/nodes/rate_half_kb_m2_r4_k3_orientation_assembly/node.json`
2. `critical/nodes/rate_half_kb_m2_r4_k3_distinct_slope_budget_ledger/node.json`

## Mandate

The K3 arm of the decomposed band red has four open leaves; this node
(TARGET) is the routing theorem: every unpaid same-owner balanced-core
bad-slope witness in the active KoalaBear m2 r4 first-match residual is
routed exhaustively and without overlap into the source-line,
coordinate, or source-cover orientation, preserving received-line
owner, support reconstruction, affine slope, and chronology, and
outputting the exact integer U_sourcecover. Codex closed the raw 433-1b
workboard (wave 55) and is working the eleven-route census; NOBODY is
working this routing theorem. YOUR JOB: build it to draft grade.

## Deliverables

**D1 — THE OBJECT MAP.** Locate, with file:line, the three orientation
images the statement names: the declared c2(1,1,2) source-line
workboard, the signed negative/positive coordinate workboards, and the
source-cover objects, all in the ACTIVE first-match residual manifest.
State the active row/partition contract (which manifest, which digest,
which chronology). If any named object does not exist under that name,
that is a finding — say so precisely.

**D2 — WITNESS CLASSIFICATION.** Enumerate the types of "unpaid
same-owner balanced-core bad-slope witness" in the active residual.
For each type: which orientation must receive it, and which of the four
preserved quantities is at risk in that routing.

**D3 — THE DRAFT ROUTING THEOREM.** A proof skeleton at audit grade:
the disjoint-exhaustive routing map plus the preservation lemmas.
Every gap is an explicit named obstruction with a pre-registered
falsifier. POSE, do not claim. If a piece is already proved in-repo
under another name, cite it (CATCH-24A greps first).

**D4 — U_sourcecover.** State exactly what integer this node must
output. If it is computable today from banked certificates, compute it
(compute law below) and pre-register the value with its manifest
digest. If not, name the exact missing certificate.

## Constraints (binding)

- COMPUTE LAW: never bare python3. `tools/ramguard tiny -- python3 ...`
  (256M/60s) for peeks, `tools/ramguard local -- python3 ...` (1G/5min)
  for real runs, from the repo root, literal `--`. This includes JSON
  peeks and file patching. Stdlib only. No Modal, no network, no git.
- RAM DISCIPLINE: file-at-a-time reads; NEVER open dag.json (use
  critical/nodes/*/node.json shards + grep); stream-parse large result
  JSONs; no bulk loads.
- WRITE SCOPE: you write ONLY inside
  notes/pilots_20260810/k3_orientation_assembly/. No dag/, nodes/,
  tools/ edits. No git operations. Do not read or write the Codex
  worktree (any path containing prize-codex-); all banked results are
  in this repo.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md at
  any line. Never read the sibling round-30 dirs
  (k3_allocation_inequality, k3_splitbc_transport, k3_chain_seams).
  Prior-round dirs are readable.
- BLIND PRIORS: after reading ONLY the two anchors, append "## Pilot
  registrations" below with your priors (expected shape of the routing
  theorem, expected obstruction count, probability the theorem is
  already implicit in a banked certificate) BEFORE any further read.
- REPORT: final artifact is REPORT.md in your dir. MISSES-FIRST: lead
  with what you could not do. Every quantifier claim quoted file:line
  (CATCH-24C). Own-repo greps before any novelty claim (CATCH-24A).
  Zero-power declarations on any max-quantified claim you make.
- Banked scripts run from scratch copies only (copy into your dir).

## Pilot registrations

Registered 2026-08-10 by pilot k3_orientation_assembly AFTER reading exactly
two files (the two named anchors' node.json) and BEFORE any further read,
grep, or interpreter invocation. Interpreter invocations so far: 0.

**P0 — expected shape of the routing theorem.** I expect a three-branch
total function `route: W -> {sourceline, coordinate, sourcecover}` on the
witness set W of unpaid same-owner balanced-core bad-slope witnesses in the
active first-match residual, defined by a *priority* case split (first
matching branch wins), not by three independent predicates. Predicted
skeleton, in order:
  (a) a *well-definedness / discriminator* lemma — the branch predicate is a
      function of data already carried by the witness (received-line owner +
      the pair generating the bad slope), so `route` is single-valued;
  (b) an *exhaustiveness* (trichotomy) lemma — no witness escapes all three
      branches, i.e. the residual has no fourth orientation. I expect this to
      be the enumeration-backed half, discharged by a manifest/certificate
      replay rather than by algebra;
  (c) a *disjointness* lemma — with a priority split this is nearly free for
      (a),(b) but NOT free at the image level: the statement demands the
      images be *exactly* the declared workboards, so I expect a separate
      *surjectivity onto the declared image* obligation per branch, and I
      predict that is where the real work is;
  (d) four *preservation* lemmas, one per preserved quantity (received-line
      owner, support reconstruction, affine slope, chronology). I predict
      owner and affine slope are cheap (routing does not move the received
      line or rescale), support reconstruction is medium (re-indexing under
      the source-cover branch), and chronology is the one that actually bites,
      because a source-cover object is naturally *later* than the witness it
      absorbs and a naive route can invert first-match order;
  (e) a *source-cover trichotomy*: each source-cover image is (i) proved
      empty, (ii) bijected into the source-line or coordinate image, or
      (iii) paid by a printed exact distinct-affine-slope integer; and
  (f) `U_sourcecover = sum over the (iii) class`, disjointly.
I predict the node's own attack.md already names something close to (c)+(d).

**P1 — expected obstruction count.** Point estimate **5** named obstructions
at the end of D3 (80% interval 3-8). Predicted composition: >=1 on
exhaustiveness (a fourth orientation / an unclassified residual bucket),
>=1 on image-exactness (declared workboard not equal to the routed image),
>=1 on chronology, >=1 on the source-cover payment being *exact* rather than
bounded, and >=1 arithmetic/allocation obstruction inherited from the
sibling nodes I am not allowed to read.

**P2 — probability the theorem is already implicit in a banked certificate.**
  - Full disjoint-exhaustive routing theorem, statement-complete, already
    banked under another name: **0.15**.
  - The *exhaustiveness half only* (an enumeration certificate showing every
    residual witness falls in one of the three orientations): **0.55**.
  - At least one of the four preservation properties already proved in-repo
    under another name: **0.65**.

**P3 — D1 object existence.** Probability that all three named object
families (declared c2(1,1,2) source-line workboard; signed negative AND
positive coordinate workboards; source-cover objects) exist under
recognisable names inside the ACTIVE first-match residual manifest:
**0.55**. Probability that at least one is a naming mismatch or lives only
in a *non-active* (superseded) manifest, which the brief says is itself a
finding: **0.45**. Probability the active manifest carries a digest I can
quote verbatim: **0.7**.

**P4 — D4 computability.** Probability `U_sourcecover` is computable today
from banked certificates without new mathematics: **0.35**. Probability I
end D4 by naming a missing certificate instead: **0.6**. Probability I can
at least print an exact *upper bound* or a candidate value flagged
unverified: **0.75**. Prior on the magnitude of `U_sourcecover`, if it
exists: small non-negative integer, median 0-2, 80% interval 0-12; I give
**0.4** to the value being exactly 0 (all source-cover images empty or
bijected away).

**P5 — zero-power warning registered in advance.** If the active residual
manifest turns out to be stored only inside a large results JSON that I must
stream-parse, any claim I make of the form "no witness of type X exists" is
at risk of being a search-shaped-hole rather than a fact; I pre-commit to
labelling such claims ZERO-POWER in the report rather than reporting them as
negative results.


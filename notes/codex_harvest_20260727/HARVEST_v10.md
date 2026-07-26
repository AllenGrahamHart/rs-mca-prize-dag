# Codex v10 harvest — 2026-07-27 (awareness only; integration is audit-gated)

Branch `prize-codex-resolution-v10-20260722`, ~75 commits in six hours. Read-only.

## Headline: Codex demotes a node we hold as PROVED, and adds a 24th red

| | ours | codex v10 |
|---|---|---|
| dag nodes | 1224 | 1245 |
| math orbit | **260** | **242** |
| PROVED / CONDITIONAL / TARGET | 201 / 36 / 23 | 180 / 38 / **24** |

**All 23 of our TARGETs are still TARGET in their tree — none closed.** The
difference is one *additional* red:

```text
+ unsafe_crossing_family_instantiation      [TARGET, absent from our dag]
```

wired **req** into `unsafe_at_crossing`, and consequently:

```text
unsafe_at_crossing :   ours = PROVED   |   codex = CONDITIONAL
   our req-parents  : averaged_slope_conversion, qfloor_exact
   their req-parents: averaged_slope_conversion, qfloor_exact,
                      unsafe_crossing_family_instantiation
```

### The new obligation, verbatim

> For every admissible row and its proposed safe agreement `a_safe`, supply an exact
> certificate at `a_safe - 1` of at least one of: **(Q)** a quotient order satisfying
> every `qfloor_exact` hypothesis, endpoint alignment, and `Acl(N',ell') > B*`;
> **(V)** an explicit family of more than `B*` pairwise-distinct bad slopes; or
> **(M)** a deterministic post-paid support family `A` with exact strict-overlap
> profile and occupancy `nu(A) = E[N(A)] - (q/2) C_t(A) > B*`. The certificate must
> use the ambient MCA slope field and account for generated-field transfer and
> first-match ownership.

## Why this matters, and why I have not acted on it

If Codex is right, **our `unsafe_at_crossing` is over-claimed as PROVED**, our board
is 24 reds rather than 23, and a PROVED node sits in our critical orbit without its
adjacent-unsafe witness family. That is a defect in *our* tree, found by comparison
— exactly what a harvest is for.

**Not acted on, deliberately.** Demoting a PROVED node on the critical surface is a
status flip requiring the full artifact chain plus the planner's audit, and the
brief reserves retirements and status flips of critical nodes to Fable/the user.
Codex raw branches are read-for-awareness only. **This is surfaced, not applied.**

## What the planner needs to decide

1. Is `unsafe_at_crossing = PROVED` sound in our tree, or does it silently assume an
   adjacent-unsafe witness family it never supplies? Our two req-parents
   (`averaged_slope_conversion`, `qfloor_exact`) do not obviously deliver the
   `(Q)/(V)/(M)` certificate above.
2. If Codex is right, our census line `260 = 201/36/23` is wrong in the
   **over-claiming** direction — the more dangerous one.

## Also observed (not audited)

Their orbit is 18 nodes *smaller* with 21 fewer PROVED, so v10 has rewired
substantially, not merely added. Any integration is a wave-scale audit, not a
cherry-pick.

---

## INDEPENDENT AUDIT (2026-07-27): Codex's demotion looks CORRECT, from our own notes

I audited `unsafe_at_crossing = PROVED` in our tree without using Codex's argument.
Its proof is a two-branch dichotomy — collision-free via `qfloor_exact`, collided
via `averaged_slope_conversion` — flipped to PROVED on the note *"both branches are
now proved, so the adjacent unsafe witness follows."* Both branch parents have
problems:

**1. `averaged_slope_conversion` (collided branch) carries an undischarged row-use
caveat, in its own notes:**

> *"Their honest caveat: stated for post-paid support families — row use still needs
> the paid-excluded strict-overlap profile."*

That is **exactly** Codex's requirement (M): *"a deterministic post-paid support
family `A` with exact strict-overlap profile"*. The node is proved for post-paid
support families; `unsafe_at_crossing` consumes it **at row level**, which the note
says needs something not supplied.

*(A second note — "REGRESSED with the averaged_xr exponent question … discharges
when `xr_ledger_exponent_reconciliation` lands" — IS discharged: that node is
PROVED. But it is **not wired** as a req-parent of `averaged_slope_conversion`,
whose req-parents are only `fm1` and `averaged_xr`. Benign, but the discharge is
unrecorded structurally.)*

**2. `qfloor_exact` (collision-free branch) has an EMPTY statement field.** We
cannot check what the other branch even claims.

**Verdict: Codex's demotion is independently supported.** One branch parent has no
statement at all; the other is proved only for post-paid support families while
being consumed at row level. The flip note "both branches are now proved" does not
establish the row-level witness.

**Still not applying it** — this is a PROVED-to-CONDITIONAL flip on the critical
surface, reserved to the planner. But the planner should now treat it as *likely
warranted* rather than merely *claimed by Codex*.

## Systemic finding: 37 critical PROVED nodes have empty statements

`qfloor_exact` is not alone. **37 of the 201 PROVED nodes in the math orbit carry an
empty `statement` field** — including `fm1`, `v8_ledger`, `staircase`, `list_unsafe`,
`cap_theorem`, `acl_count`, `paid_*_fn` and others. The validator's precision
invariant covers only *open dominators* and *CONDITIONALs*, so PROVED nodes escape
it entirely. A PROVED node with no statement cannot be audited, cannot be
Lean-targeted, and cannot be checked against upstream — and 18% of our proved
critical surface is in that state.

A pinned guard is added (`verify_prize_dag.py`) so the count cannot grow silently.

## Root cause: 82 PROVED nodes have no in-tree proof artifact

`qfloor_exact` is PROVED with `refs = ['proof_sketch/s2_paid_ledger.md#3']`, an empty
`statement`, an empty `notes`, an empty `notes/` directory, and a `proof.md` that
says only *"Vendored from the working record; primary artifact(s):
proof_sketch/s2_paid_ledger.md#3"*. **That path does not exist in this repository.**

It is not an isolated case. Scanning every node's `statement.md` for cited
`proof_sketch/` paths:

```text
109 nodes cite a proof_sketch/ artifact absent from this repo
   PROVED 82 | CONDITIONAL 23 | TARGET 3 | PROVABLE 1
including prize, mca_grand, list_grand and packaging themselves
```

**Stated fairly:** these are labelled *"refs (legacy repo)"*, so the artifacts
presumably live in a predecessor repository rather than nowhere. This is not a claim
that the proofs do not exist. But the consequence for *this* tree is concrete:

> For those nodes, **neither the statement nor the proof is checkable in-tree.**
> `verify_prize_dag.py` nonetheless reports `PASS: structure, refs, ...`, because its
> refs check does not resolve legacy paths.

That is exactly how `qfloor_exact` — a req-parent of `unsafe_at_crossing`, the node
Codex demotes — reached PROVED with nothing verifiable behind it in this repository.
Combined with the 37 empty statements, a substantial fraction of the proved critical
surface cannot be audited here at all.

**For the planner.** Two separable questions: (1) is the legacy `proof_sketch/` tree
recoverable and should it be vendored in, and (2) until it is, should nodes whose
only artifact is a dangling legacy ref be treated as PROVED on the critical surface?
The `unsafe_at_crossing` adjudication depends on the answer.

## Planner question (1) RESOLVED: the legacy tree is NOT recoverable

Searched exhaustively:

```text
prize/ working tree ................... no proof_sketch/
prize/ git history, --all branches .... no proof_sketch/ ever committed
sibling directories (all) ............. none contain proof_sketch/
Codex branches v8, v9, v10 ............ none
rs-mca-packets, rs-mca-vendor ......... none
find . -name "s2_paid_ledger*" ........ nothing
mirror AllenGrahamHart/rs-mca-prize-dag  no proof_sketch/; code search
                                         for "s2_paid_ledger" returns 0 hits
```

**The legacy `proof_sketch/` artifacts are not recoverable from any accessible
source.** So the 82 PROVED nodes citing them reference proofs that cannot be
produced, re-checked, audited, or Lean-formalized from anything we have.

**What this does and does not mean.** It does *not* mean those nodes are wrong —
the proofs may well have existed and been checked when the refs were written. It
means they are **unverifiable now**, and that `verify_prize_dag.py` reports
`refs PASS` while 109 nodes point at nothing.

That is the honest state of the proved critical surface, and it bears directly on
what the census line means: `201 PROVED` counts 82 nodes whose proof artifact is
absent, of which 37 also have an empty statement.

**Planner question (2) is therefore the live one:** should a node whose only
artifact is an unrecoverable legacy ref count as PROVED on the critical surface? A
"no" would move a large number of nodes and change the census materially. A "yes"
needs a recorded justification, because the current position is undocumented rather
than decided.

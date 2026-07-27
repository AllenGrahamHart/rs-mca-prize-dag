# The `proof_sketch/` refs: found, and what they actually say

**Date:** 2026-07-27 (Fable, planner). **Status: this CORRECTS the record.**

## The legacy tree is NOT unrecoverable

`notes/WORKLOG_OPUS5.md` session 7l concluded "**No `proof_sketch/` anywhere**"
and treated the tree as lost. That conclusion is **wrong**. All twelve files are
live on upstream `origin/main` right now, nested one level deeper than the search
looked:

```
experimental/notes/roadmaps/proof_sketch/
    prize_proof_sketch_spine.md      s3b_iii_2_displacement_spectral.md
    s2_paid_ledger.md                s3b_iii_3_fibers_and_noanchor.md
    s3a_regular_window.md            s4_reserve_dictionary.md
    s3b_ii_strip_periodic.md         s5_s0_statements_and_object.md
    s3b_iii_1_divisor_pencil_incidence.md   s6_extension_lift.md
    s7_list_side.md                  s8_s9_assembly_and_negative.md
```

Read them the standard way (hard law 6):
`git -C ../rs-mca show origin/main:experimental/notes/roadmaps/proof_sketch/<f>`

The search failed because it looked for a top-level `proof_sketch/` path and did
a mirror code search; the tree lives under `experimental/notes/roadmaps/`. Our
node refs are written in the short form `proof_sketch/<file>#<section>`, which
resolves nowhere locally — hence the false "lost" verdict.

## The real defect is status inflation, not loss

The files are **proof SKETCHES**, and each section carries its own status tag in
its heading. The port that created this repo (first commit 4c523cbc, "node-per-
folder layout ... legacy-ref vendoring semantics") vendored refs to these
sections as if they were proof artifacts, **without checking that the cited
section supports the node's claim**. `verify_prize_dag.py` then skipped the refs
as "legacy fork pointers", so nothing ever re-checked, and `auto_discharge.py`
propagated PROVED upward by modus ponens (30 critical PROVED nodes are
auto-discharged).

**The smoking gun.** `zone_b` is PROVED in our dag and cites
`proof_sketch/s2_paid_ledger.md#3`. That section is headed:

```
## 3. The quotient term: three zones [PROVED-cited / CONJECTURE]
```

and says of exactly `zone_b`'s range:

```
zone (b) 80 < N' < ~512: mass CONJECTURAL, bracketed by
         [DdH floor rho(1-rho)N'^2 , 2^{beta N'(1-o(1))}] — the collision
         question for e_1-value-sets mod p, WHICH IS prob:perfiber AT sigma = 1
```

**Our source says CONJECTURAL; our dag says PROVED.** This independently
confirms Codex's `zone_b` demotion, and it is the mechanism behind the wider
over-claim. (Note the same section's zone (c) *does* prove unsafe at
`eta = 2^-9` regardless of zone (b) — a likely origin of the confusion: a
neighbouring zone's proof was read as covering the node.)

## Scope of the re-grading job — bounded, not a research program

49 distinct sections are cited, 161 citations total. The load concentrates:

| section | citations | critical PROVED depending on it |
|---|---:|---:|
| `s2_paid_ledger.md#3` | 27 | 14 |
| `s3b_iii_3_fibers_and_noanchor.md#1` | 19 | 15 |
| `s3b_iii_2_displacement_spectral.md#3` | 12 | 0 |
| `s3b_iii_1_divisor_pencil_incidence.md#3` | 7 | 0 |
| `s3b_iii_3_fibers_and_noanchor.md#3` | 7 | 0 |
| `s3b_iii_2_displacement_spectral.md#2` | 7 | 0 |

Two sections carry 29 of the ~80 affected critical PROVED nodes. **Reading ~10
sections re-grades most of the board.** This is a day of careful reading, not a
re-proving campaign.

## Method for the re-grade (proposed)

For each cited section, in citation-count order:
1. Read the section and record its **own** status tag verbatim.
2. For each citing node, decide whether the section proves *that node's exact
   statement at its consumer's scope* — the failure mode is a neighbouring
   zone's proof being read as covering the node (`zone_b`), or a weakened
   typicality target discharging a per-row obligation (the e1 chain).
3. Re-grade: PROVED only if the section proves it outright; otherwise
   CONDITIONAL on a named open predicate, or TARGET.
4. **Re-point the ref** to the resolvable upstream path so
   `verify_prize_dag.py` can check it instead of skipping it.

Step 4 should also remove the `continue  # legacy fork pointer` skip in the refs
check — the justification for it is now known to be false.

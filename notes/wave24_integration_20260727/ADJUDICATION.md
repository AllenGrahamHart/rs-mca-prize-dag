# Wave-24 integration — adjudication of Codex's 12 status changes

**Date:** 2026-07-27. **Planner:** Fable. **Method:** every demotion was
adjudicated against the *recovered* `proof_sketch/` sources upstream
(`git -C ../rs-mca show origin/main:experimental/notes/roadmaps/proof_sketch/<f>`),
not against Codex's argument — see `notes/PROOF_SKETCH_PROVENANCE.md`.

**Directive:** promote a node back if its sketch proof can readily be made real;
demote if the proof is genuinely too weak. **Outcome: 0 promotions back, 11
demotions accepted, 1 promotion accepted.** I looked for upgrades in every case;
the reasons none was available are recorded below, because "we checked and it
does not upgrade" is the load-bearing part.

## The crossing cluster

| node | verdict | reason |
|---|---|---|
| `zone_b` | **demote — CONDITIONAL** | Cited `s2_paid_ledger.md#3`, whose heading reads `[PROVED-cited / CONJECTURE]` and whose text says of exactly this range: *"zone (b) 80 < N' < ~512: mass **CONJECTURAL**"*. Our source says conjectural; our dag said PROVED. Not upgradable — the section states it is an open collision question (`prob:perfiber` at sigma=1). |
| `unsafe_at_crossing` | **demote — CONDITIONAL** | Two-branch dichotomy; the collided branch (`averaged_slope_conversion`) is proved for *post-paid support families* and was consumed at **row** level, and the collision-free branch (`qfloor_exact`) had an empty statement so its claim could not be checked. Genuine scope drift. |
| `mca_unsafe` | **demote — CONDITIONAL** | As stated it needs the witness **at the adjacent grid point**, which is `unsafe_at_crossing`. Not upgradable *as stated*. |

**What survives, and it is not nothing.** `s2_paid_ledger.md#4` records
`cap (proved): eta = 2^-9 (2^-10 at rho=1/16)`, and section 3's zone (c) says the
Paper D cap "proves unsafe at eta = 2^-9 **regardless of zone-(b) resolution**".
That real result is already carried by **`cap_theorem` (PROVED)**, which remains
a req-parent of `mca_unsafe`. So we keep the bracket `delta* <= cap`; what we
lose is the claim to have *pinned* `delta*` at the adjacent point. Codex's
removal of the `zone_b --req--> mca_unsafe` edge (retained as `ev`) matches the
sketch's own logic exactly.

*Likely origin of the original over-claim:* zone (c)'s genuine proof sits in the
same section as zone (b)'s conjecture, and was read as covering the node.

## The e1 chain (8 nodes)

These carry no `proof_sketch` refs — they were PROVED by
`tools/auto_discharge.py` (modus ponens up the cone). The chain bottoms out in
two nodes, and neither supports a per-row claim:

- `e1_folded_no_vector_certificate_128_payload` — a **real** Modal/fpylll BKZ
  computation (shortest norm 31.67 > box threshold 16.0), but over **one named
  250-bit Pocklington field**. An exhibit, not the admissible family.
- `e1_folded_no_vector_certificate_256_payload` — despite the name, **not a
  certificate**: a first-moment union bound giving the property *"for all but a
  `p^-0.24` fraction of admissible row primes"*. Its own text calls it *"the
  WEAKENED density target (o(1)-sparsity, not zero-survivor)"*, and records
  *"cited script NOT ON DISK, notes/ empty — catch #61"*.

The prize quantifier is per-code (*determine for each admissible C*), so a
typicality statement cannot discharge it — the exceptional set is exactly what a
referee asks about. **Not upgradable cheaply:** closing it needs either a
family-uniform argument or certificates for infinitely many fields; a
first-moment bound has no easy route to either.

## The promotion (accepted)

`rate_half_list_chamber_affine_rank_bridge` TARGET -> **PROVED**. Not in conflict
with Opus's negative result: Codex proves the *translation* from the chamber
atlas to `(d_1,d_2,d_3)` exists; Opus proves that even with it the compiler's cap
cannot exclude four codewords. Both wire it **ev** into
`rate_half_list_adjacent_crossing` — same conclusion about its usefulness.

## Re-pricing

```text
math orbit  260 = 201/36/23   ->   242 = 180/38/24
submission  275 = 213/38/24   ->   257 = 192/40/25
```

19 e1 nodes left the critical orbit entirely (the `zone_b -> mca_unsafe` rewire
cut the path). The board is **24 open targets, not 23** — the new one is
`unsafe_crossing_family_instantiation` (TARGET), Codex's honest replacement for
the over-claimed crossing. Our merged census now matches Codex's independently
computed `242 = 180/38/24` exactly.

All pins widened per hard law 8 with dated justification, never silenced:
`verify_orbit_census`, `verify_critical_harness_coverage`,
`verify_conditional_propagation`, and the two guards in `verify_prize_dag`
(hollow 197->196, empty-statement 37->36).

## Correction applied to a guard comment

`verify_prize_dag.py` carried the claim that the legacy tree "is not recoverable
from the working tree, git history, any sibling directory, the Codex branches, or
the public mirror". That is false — the tree is live upstream. Comment corrected
in place and pointed at `notes/PROOF_SKETCH_PROVENANCE.md`.

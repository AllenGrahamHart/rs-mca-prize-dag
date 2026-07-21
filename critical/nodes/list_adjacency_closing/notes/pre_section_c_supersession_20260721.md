# Provenance snapshot (2026-07-21): statement.md + conditional.md immediately
# before the Section C list-corridor supersession (maintainer-ratified this
# date; wave-15 w15-C1). Preserved per custody #104.

## statement.md
# list_adjacency_closing

- **status:** see dag.json (single source of truth; dag status CONDITIONAL) [header retrofit 2026-07-10, catch #69 — was: TARGET]
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s7_list_side.md']

## Statement

For each admissible row and constant m: exhibit adjacent delta with sup_U |Lambda(U, delta-1)| > eps*|F| >= sup_U |Lambda(U, delta)| (per the official m-quantifier). The determination's list half, previously unpriced — the exact mirror of adjacency_closing.

## Attack surface

the hardness SWAPS sides vs MCA: unsafe witnesses are CONSTRUCTIVE (planted families = explicit codewords), the safe half is imgfib + integrality; the residue is worst-word extremality + exact planted arithmetic

## Falsifier

n/a (composite obligation)

## Weakening Applied 2026-07-06

The direct `worst_word_planted` input is support/evidence for this node, not a
separate logical premise.  The exact arithmetic child
`list_planted_arithmetic` already consumes worst-word extremality and challenger
pricing, then supplies the priced two-column crossing arithmetic used here.

## Ledger (migrated notes)

AUDITED TRUE RED (ring-1 sweep): the local content is the final quantitative corridor arithmetic — not promotable by referee argument; this is genuine open work.

## conditional.md
# list_adjacency_closing conditional proof

- **status:** CONDITIONAL
- **closure:** proof from predicate nodes

## Predicate nodes

- `list_crossing_localization`
- `list_planted_arithmetic`
- `rate_half_band_closure`
- `list_corridor_ledger`

Convention/evidence guards:

- `worst_word_planted`
- `rules_m_reading`
- `rate_half_coverage_gap`

## Claim

Conditional on the predicate nodes, for each admissible row and each constant
interleaving arity `m`, there is an adjacent agreement-index `delta` satisfying

```text
sup_U |Lambda(U, delta - 1)| > eps*|F| >= sup_U |Lambda(U, delta)|.
```

## Proof

`rules_m_reading` fixes the quantifier convention: the list challenge is a
family of determinations indexed by constant `m`.

For a fixed admissible row and fixed constant `m`, `list_crossing_localization`
proves that the worst-word list-size function is integer-valued and monotone in
the agreement-index convention. Therefore once the relevant window is bracketed
there is a unique adjacent crossing of `eps*|F|`.

The unsafe side is constructive. The predicate `list_planted_arithmetic`
packages the two-column inventory needed here: its own predicate chain consumes
`worst_word_planted` and `worst_word_challenger_pricing`, then prices the
planted sunflower and classified E15 challenger columns by exact combinatorial
formulas. Thus the lower side of the crossing can be exhibited explicitly
without taking `worst_word_planted` as an additional direct premise of this
assembly node.

The safe side is supplied by the corridor predicates. `list_corridor_ledger`
closes the clean-rate corridor from the list-side arithmetic columns, while
`rate_half_band_closure` supplies the missing rate-`1/2` band identified by
`rate_half_coverage_gap`. Together they cover every admissible row class in the
current split.

Thus, for each row and constant `m`, the exact planted/challenger arithmetic
exhibits the last unsafe index, the safe ledger controls the next index, and
monotonicity turns those two inequalities into the adjacent crossing displayed
above.

If any predicate fails, the parent does not claim more than bracket-grade
information for the corresponding row or band.

## Weakening

WEAKENING 2026-07-06: the direct edge
`worst_word_planted -> list_adjacency_closing` is evidence rather than a
logical requirement.  The transitive dependency remains through
`list_planted_arithmetic`, whose statement is exactly the arithmetic reduction
that uses worst-word extremality.

---

## PREDICATE SWAP (2026-07-16, wave-8 audited import)

The rate-1/2 list predicate this packet consumed as
`rate_half_band_closure` (open red, list half) is replaced by the PROVED
`rate_half_cyclic_rotated_prefix_floor` (req-wired at import): the
residual band's list crossing is determined by theorem, so the
list-side hypothesis is discharged. The OLD predicate reference is
retained here as history; rate_half_band_closure itself stays TARGET on
its remaining MCA/CA half (which this packet does NOT consume — the
MCA-side hypotheses are unchanged, see the trigger-separation guard in
that node's statement addendum).

---

## CORRECTION to the predicate swap above (2026-07-17, w9-C3)

"The list-side hypothesis is discharged" OVERCLAIMS: the PROVED cyclic
floor supplies only the UNSAFE side of the rate-half list crossing; the
SAFE side has no owner post-swap (the "banked safe side above sigma*"
was planning prose — w9-C2). Until a safe-side theorem lands, this
packet's claim for the rate-half row is BRACKET-GRADE (unsafety proved
through sigma_0; crossing location open). The req wiring stands (the
floor is a genuine hypothesis-supplier); what changes is the claim
scope recorded here.

## OWNER UPDATE to the w9-C3 correction (wave-10, 2026-07-18)

The rate-half list SAFE side is now OWNED: the TARGET pose
rate_half_list_adjacent_crossing (req-wired into this packet) is the
w9-C3 repair vehicle. Unsafe side proved through excess 2^34-1 (the
optimized floor); the list crossing is DETERMINED for budgets
B* in {1,2} (a_L = 3n/4, rate_half_list_low_budget_exact_crossing
PROVED); bracket-grade for larger budgets pending the pose.

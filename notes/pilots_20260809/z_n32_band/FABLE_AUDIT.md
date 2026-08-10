# FABLE_AUDIT — z_n32_band (round 25)

Coordinator: Fable. Date: 2026-08-09. Pilot: Opus (task ab9fe08fa658a522c,
~78 min, 141 tool uses). Quarantine marker: ledger line 3731, observed.
The pilot issued its final report twice (near-identical text; the second
adds UMITM RSS 542-575 MB and the cache-thrash detail) plus a stable-state
confirmation; REPORT.md holds the recovered longest version verbatim —
the duplicates carry no divergent claims.

## Verdict

**BANKED. The named decisive computation from round 24 is EXECUTED: the
N=32 wall is broken (BBM), the record C >= 1.7681 stands (no cell beat
it), and the ladder verdict is the honest, uncomfortable one — the
matched decay is not significant, the census's own growth law missed the
N=32 max by 10x, and the mechanism (low-weight mu_64-orbit spikes) is
one the SD-based extrapolation cannot see. Z-CEILING survives, repriced
weaker.**

## Replays (all by me, under ramguard)

| what | result |
|---|---|
| ez.py escape suite | **15/15 PASS**, incl. P-Z9: N=16 record TMASS=159/64, CRATIO=1.7680688810, NKER=289 exact; RBUCK-invariance; negation identity; Z-FLOOR 0 violations on the 1305-cell line |
| analyze.py (seeded 20260809) | deterministic; ALL verdict numbers reproduced: plain quantile 0.3483, sigma-stratified 0.2278, sd quantile 0.0000, exponent -0.02614, EVX extrapolation 1.881633 |
| record cell p=4683696257, THIRD variant (my driver: reversed perm + RBUCK=101 — internals disjoint from both pilot derivations) | **AGREE**: TNUM 11700545024, NKER 392641, 47.3 s |

Not replayed: the other 71 N=32 cells (33 have the pilot's two-way
BBM-ALT coverage incl. all top-12; VERIFY.alt.s*.tsv shows 0
disagreements; 1402 checkpoints allow resumption); the 1305-cell N=16
line (spot-anchored by the record cell + Z-FLOOR pass inside ez.py).

## Audit judgements

- **BBM's correctness case is strong**: exact Fraction agreement with
  the round-24 zcore on 26 cells, bit-identical output across four
  bucket counts, a negation identity, a character-sum cross-check to
  6.4e-14, and a three-way record cell. The single-code-path caveat on
  39/72 tail cells is real and disclosed; none of the verdict's leading
  cells depends on them.
- **The verdict statistics are fair**: the sigma-stratified null was
  added because the N=32 sample is designed, and it moved the quantile
  AGAINST the pilot's registered prediction direction. The seeded
  analysis makes the whole verdict replayable.
- **The 10x miss of round-24's law is the finding, not a flaw**: P-Z1
  (its own headline prediction) missed by 10x in (MAXCR-1), reported
  first. Round-24's P4d ("grotesque room") is repriced NOT SUPPORTED —
  applied to the f2 node as an addendum, no status flip.
- **Compliance**: 1G never relaxed (RAMGUARD_TIMEOUT only for walls),
  no Modal, draft-only, no node/tool/git writes, registrations at
  PREREG lines 61-301 before compute. Contention with the two sibling
  pilots halved throughput; tier cuts declared, not silent.

## Corrections applied

- background/nodes/f2_z1_mass_knife_edge/statement.md — round-25
  addendum: wall broken, grid, ladder verdict, mechanism, kappa lead
  (hedged), named follow-on now = UMIN-targeted spike search + the
  declared post-hoc kappa=2 exhaustive band. No status flip.

## Follow-ups filed (not executed)

- UMIN-targeted spike search at N=32 (weight-enumerator triage, ~3x a
  cell) — the highest-value Z-CEILING computation now.
- The exhaustive kappa=2 band (266 cells, post-hoc declared, never
  run) — would settle the kappa-direction lead at N=32.
- The 39 single-algorithm tail cells can be finished from ckpt/ by
  ver.py at leisure; nothing in the verdict waits on them.

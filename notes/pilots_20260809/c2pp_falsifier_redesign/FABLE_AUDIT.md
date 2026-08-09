# FABLE_AUDIT — c2pp_falsifier_redesign (round 25)

Coordinator: Fable. Date: 2026-08-09. Pilot: Opus (task aaf6505beb45d0c59,
~104 min, 85 tool uses). Quarantine marker: ledger line 3731, observed.

## Verdict

**BANKED. Mystery 3 (C2''-r3) moves from "unmeasurable at depth" to
"measured, with a powered falsifier that stayed silent." The telescoping
lemma converts the un-escalatable multi-junction window into per-level
censuses; G-c is the first falsifier this conjecture has had that passed
a synthetic power control BEFORE being proposed, and it is SILENT. The
GB-5 4.5x — round 24's headline non-stacked datapoint — is repriced as a
saturation artefact: the official shape lives in deep pre-saturation,
where the measured window sum is ~0. And the toy closed form rebuilds
the official ledger's own constants 5/5, explaining 107 = 128 - 21.**

## Replays (all by me, under ramguard, scratch copy with pinned R24 path)

| what | result |
|---|---|
| escalate.py phase A (fresh checkpoint) | **PR-A PASS** (telescoping lemma vs independent 2^16 brute force, 4 configs) + positive control 8/8 on BANKED_F2B |
| power.py (fresh run) | power_results.json **IDENTICAL** to the pilot's banked file — the powered-falsifier claim is fully reproducible |
| analytic.py (in place, read-only) | all D3 anchors reproduced: ledger rebuild 5/5 True, S_200 = 1.4426950409 = 1/ln2, R3_full [law] = -6.59e-3 across log2 q in [41, 255.9], reserve-break scale 255.999999987544 = 256 - 107/2^33, the C25-5 catch printed |
| escalate.py phase B (fresh checkpoint) | **86/98 closed-form rows re-verified exact, 0 mismatches** (my 9-min timeout truncated the run; the pilot's own checkpointed pass is 98/98) |
| 107/2^33 decimal | independently computed: 1.245644e-08 — the JSON's 1.24556e-05 is wrong, catch confirmed |

Not replayed: phases C/D (275 exact level-census rows + 78 window rows,
multi-hour Proth-prime censuses; their raw values live in ckpt.json and
feed analytic.py, whose outputs I replayed end-to-end).

## Audit judgements

- **The lemma is the round's best structural find on this node**: it is
  elementary (containment of events), brute-force verified by
  independent machinery, and it dissolves the exact wall that round 24
  declared. The window/level distinction should have been seen earlier.
- **The power-control discipline held exactly as briefed**: thresholds
  calibrated on synthetic worlds, frozen, then applied; the blind zone
  (the knife edge) declared in advance rather than discovered in
  excuse. F3 (sqrt-stratum) is undetectable but demonstrably harmless
  to the break scale — an honest limitation, stated.
- **The GB-5 repricing is a genuine interpretive correction of round
  24's banked framing** — the measurement stands bit-exactly (and is
  now known to be the FULL tower), but the 4.5x lives in the saturated
  regime the official row does not occupy. Applied to the node as
  addendum text; the round-24 addendum is left verbatim with its
  weight moved, not rewritten.
- **The symmetric not-evidence clause is respected**: G-c silence is
  banked as a survived powered test on toys, explicitly NOT as
  uniform-stacking evidence for the official row; every official-scale
  number is labelled [law] with its licensed range (log2 q <= 232),
  its undecidable band ((232, 256]), and the regime where the law
  itself predicts breakage (within 107/2^33 of 256 — exactly where the
  packet's own two 256-bit rows sit).
- **Self-corrections**: 7, all disclosed; two were the pilot walking
  into effects it had itself registered as cautions (conditioning
  dropped in a check; freeze-scale q choice), both caught by its own
  controls; one registered cell dropped as a shift-0 (CATCH-19B)
  never-measurable, not post-hoc filtered. Divergence D-14 (Proth
  primes to bypass the trial-division primitive-root helper) is
  declared and is what bought the 260-octave range.
- **Compliance**: quarantine held, RAM discipline held (checkpointed
  phases), stdlib only, draft-only, no git/Modal; round-24's
  gb_probe.py reused verbatim with nothing written into its directory.

## Corrections applied

- critical/nodes/dli_c2pp_joint_reserve/statement.md — round-25
  addendum (8 numbered items: lemma, G-c silent, GB-5 repriced,
  ledger rebuild, [law] junction-sum estimate, two new laws, the
  freeze-tail named obstruction, C25-5). No status flip.
- notes/pilots_20260802/c2pp_nullity_structure/results/
  official_scale.CORRECTION_C25-5.md — sidecar constant correction
  (banked JSON left verbatim; fraction correct, decimal 10^3 off).

## Follow-ups filed (not executed)

- The freeze-tail cutoff law (named obstruction) — the next
  theorem-shaped target; the measured freeze scales (14.5..67) are in
  ckpt.json ready for a fit-and-prove attempt.
- S_inf = 1/ln 2 deserves a three-line proof (it looks like a known
  binomial-entropy telescoping identity) — mint candidate alongside
  R3inf ~ 0.4427 n.
- If a future round wants the (232, 256] band: the per-level freeze
  law says only levels 0/1 matter there, which may make a targeted
  exact census reachable after all.

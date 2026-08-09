# FABLE_AUDIT — m7_falsifier_hunt (round 26)

Coordinator: Fable. Date: 2026-08-09. Pilot: Opus (task a65e35334108d236e,
~46 min, 91 tool uses). Quarantine marker: ledger line 3872, observed.

## Verdict

**BANKED. The registered falsifier FIRED at an admissible live cell —
and the hunt is exactly what the falsifier was registered FOR: round
25's kill conclusion survives, but its mechanism line was false for the
large-source family and is now corrected. The kill's honest leg is the
pricing (156/408 threshold-passing rows are all ~10^11 bits short of
the polynomial target). Two structural gains beyond the mandate: the
sharp overlap cap (a corollary of (CJ2) un-summed, 0/8336, attained,
deletes the pencil stratum) and the EMPTY charge (71.38% of the
residual d-mass has no compatible codeword by the node's own list
threshold — the third instance of the claims-(i)/(ii) bookkeeping
mechanism, replayed byte-identical, adoption gated on the full-grid
distinct-d computation). Red 3's membership stays UNDECIDED by honest
refusal.**

## Replays (all by me)

| what | result |
|---|---|
| d4_bo_sieve.py (the EMPTY/SINGLETON charge) | output **BYTE-IDENTICAL** incl. the CJ3 baseline 0.01969549 byte-match |
| d1_cells.py (13-cell admissibility + codim identity) | output **BYTE-IDENTICAL** |
| d2_hunt.py C8 8 20260809 (the firing cell, 8-config grid) | summary **IDENTICAL** (only elapsed_s differs) |
| C8 admissibility arithmetic | verified BY HAND: S = 11 = 5*2+1, N = 9, u = 1 <= b = 1, h = 6 >= d+g = 6, r_J = 4, J_plain = 25-36 = -11 <= 0, 2d-N = +1 |
| the firing mechanism | verified BY HAND: defect sets are d-subsets of the core so |U| <= N; sigma = |U|-kappa <= N-kappa and a = d-kappa, so N+kappa < 2d forces sigma < 2a. Exact arithmetic, as claimed |
| the EMPTY logic | verified BY HAND: a contributor at defect d in a t-cell forces u = d-(t-1)ell background agreements; u > b = |B| is impossible, so those (row,d,t) cells are empty — the banked sieve never charged this |
| escape tests | the pilot's d4_cj3 replay byte-identical (matches my own two prior replays); its d0_compat reproduced round-25 arm-A config-by-config, 32/32, first_mismatch null |

Not replayed: the other 27 runs (the pilot's own compat harness anchors
the generalized chart against the coordinator-replayed arm-A code
path); d3_realrows/d3b_pricing (deterministic arithmetic over the
banked 408-row grid — the same grid d4_bo_sieve consumed on my
byte-identical replay).

## Audit judgements

- **This is the registered-falsifier system working as designed.** A
  kill was banked with a checkable reopening condition; one round
  later the condition was hunted in its named cheapest ground and
  FIRED; the conclusion survives on its other leg and the mechanism
  text is corrected. Both round-25 and round-26 reports stay banked
  verbatim — the correction is an addendum, not a rewrite.
- **The C9 matched control is what makes the firing believable**:
  identical cell parameters except M (so 2d-N flips sign), 0/64
  firings — the switch is exactly at 2d = N, as the arithmetic says.
  And the power control shows the guards SUPPRESS the firing
  (random fires more), so this is not guard structure.
- **The EMPTY charge is the round's largest number and is correctly
  gated**: the pilot itself refuses to headline 71% (3-point
  ell-sample denominator, (row,d) vs distinct-d, CJ3-band overlap
  uncomputed — its P18 declared NOT COMPUTED). Banked as
  replayed-but-not-adopted; the full-grid distinct-d computation is
  the named highest-value follow-up.
- **The (SING) novelty subtraction fired correctly** (CATCH-24A run
  BEFORE the claim; (BO2) of l1_background_overlap_singleton_payment
  is the same statement; 17 of the 156 firing rows are already
  singletons by it).
- **Red 3: the honest refusal is right on both grounds** — the 2.3h
  enumeration was priced not spent, and the 23b functional failed
  its power control at accessible cells (indistinguishable from
  matched-random), so a cheap answer would have been a wrong answer.
  Membership stays UNDECIDED; the board is unchanged.
- **Misses handled correctly**: P7's wrong registered cap became the
  sharp-cap discovery; P5's wrong gloss reported as wrong; the grid
  enlargement kept side-by-side with the registered n8 runs; two
  no-signal cells reported empty rather than aggregated.
- **Compliance clean**: quarantine held, compute law total
  (RAMGUARD_TIMEOUT 600-2400s documented), RAM discipline held,
  draft-only held (two scratch temporaries went to the sanctioned
  session scratchpad, disclosed), stdlib only, no subagents.

## Corrections applied

- background/nodes/l1_rootfree_rational_q_projective_packing/
  statement.md — round-26 correction: the falsifier FIRED (C8/F1,
  156/408 transfer, the 2d > N mechanism), the round-25 mechanism
  line scoped to the m4 family only, the kill re-founded on the
  pricing leg (0/156 polynomial, ~7.3e11 bits vs 123-129), the
  b -> ell intuition refuted.
- critical/nodes/l1_fpc5_large_source_payment/statement.md —
  round-26 addendum: the sharp overlap cap (corollary of (CJ2),
  0/8336, attained, pencil stratum deleted), the EMPTY 71.380% +
  SINGLETON 0.679% charge with binding caveats and
  adoption-gate, red 3 UNDECIDED of record.
- No status flips; no board change (mystery 7 intact — the wall
  classification never depended on the threshold line).

## Follow-ups filed (not executed)

- THE named follow-up: full-grid distinct-d EMPTY/SINGLETON/CJ3
  computation over the 408 rows (disentangling the bands). If it
  confirms anywhere near 71%, the large-source residual shrinks by
  ~3.6x and the row hardness map changes.
- File the sharp cap as a formal corollary note on
  l1_joint_core_background_johnson_bound (one-paragraph mint).
- The 139 genuinely-open firing rows (156 minus 17 BO2 singletons)
  are the honest hard core of the large-source red at 2d > N.

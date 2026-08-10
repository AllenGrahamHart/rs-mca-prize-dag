# FABLE_AUDIT — rh_e_axis_audit (round 31)

Coordinator: Fable. Date: 2026-08-10. Pilot: Opus (~45 min, 108 tool
uses, 7 interpreter invocations — one disclosed bare-python3 no-op
breach (M5, empty heredoc, no program run; same class as the
round-28 slip) and a weaker-than-standard quarantine mechanism (M7,
output-filtered rather than search-excluded; no ledger line
surfaced) — both accepted with the pilot's own flags). REPORT.md
persisted verbatim by the coordinator.

## Verdict

**BANKED, AND THE RULING EXECUTED: WIDEN. The audit's case is
structural, not tidiness: (1) 13 of 14 instruments in the
located-crossing stack are field-general by their own printed
hypotheses (inventory quoted file:line); (2) the ONE primality-using
instrument (the A=1 Legendre router) is separated from every
extension row by the PROVED RPFC contrapositive — a shield nowhere
previously stated in-repo; (3) the e-axis is FINITE: e in {1..6}
exactly, with char = p > n = 2^41 on the entire widened family
(the three sub-2^41 candidates at e = 6 all composite); (4) the
first extension-field supply measurement ever run in the band lane
(the repo's prior field layer could not even represent F_{p^e})
finds NO excess at the analogue of the exhibited razor row —
H-SUBFIELD refuted at the decisive q = 289 cell with a clean
structural reason (F_p-rational keys reproduce exactly the F_p
profile); the only visible excess is the full-multiplicative-group
degeneracy, unreachable at n = 2^41 (2^41+1 = 3*83*8831418697).
The one zero-power item (O3, the published HD1 import) was CLOSED
BY THE COORDINATOR from the primary source: ABF26 Theorem 4.9
states the unique-decoding CA bound (BCIKS20 Thm 1.4) for RS[F,L,k]
over an arbitrary field — no primality hypothesis.**

## Coordinator verifications (mine)

| what | result |
|---|---|
| d2_eaxis_arith.py + d2b_char_floor.py replays | green; the RPFC 24+22-candidate census reproduced with 0 primes; the e=6 exhibit row checks |
| RPFC statement | verbatim PROVED, (RPFC1)/(RPFC2) as quoted; the contrapositive is one line of logic |
| O3 | VERIFIED MYSELF against the vendored abf26 pp.18-19: Thm 4.9 (RS[F,L,k], arbitrary F), Thm 4.8 (any linear code), Lemma 4.6 (any F-additive code) — the import is field-general |
| the stratum enumeration | replayed (LTE table, per-e p-windows, e >= 7 infeasible) |
| the widening execution | pose block on crossing_location + RPFC addendum + BAND_LANE_DEFINITIONS item 16 + band_closure conditional F4-resolved sync; chain green |

## Audit judgements

- **The pilot's M1 is the finding**: the strongest pro-widening fact
  was a PROVED node built to force primality, read contrapositively
  — the pilot registered it as a hazard and discovered it was a
  shield, and scored its own prior's reasoning as wrong. That is
  what blind priors are for.
- **Section 1's framing correction is load-bearing**: "q prime" was
  a THEOREM on 2^-127 of the pose's range and an assumption on the
  rest — the discontinuity at 2^167 (family-uniform below,
  prime-only above, no theorem at the seam) made the status quo the
  unprincipled option, not the safe one.
- **The measurement design was honest**: the H-SUBFIELD/H-FULLGROUP
  split at q = 289 (proper subfield, not whole group — the exact
  analogue of the razor exhibit's branch) is the right decisive
  cell, and the pilot got it in before its second wall hit, with -u
  and file redirects protecting the partial ladders (the round-30
  M3 lesson executed).
- **O6/O7 are the residue and they are standing on the pose**: the
  fragile direction is future far-CA UPPER bounds (must not assume
  no-subfield); the prime-only evidence base (21,832-census,
  collinearity, F_LMAX ladders) is flagged for re-runs now that
  ffq.py exists. M8 (statements-not-proofs) remains the structural
  limitation, priced by O5's shared falsifier.

## Corrections applied (the ruling's execution, forced by its own terms)

Pose widened q prime -> q = p^e (e in {1..6}) with the full grounds
block; RPFC contrapositive + stratum-lemma addendum (mint
candidate); BAND_LANE_DEFINITIONS item 16; band_closure
conditional's F4 flag RESOLVED. No status flips; census unchanged.

## Follow-ups filed (not executed)

- O7 re-runs (the extension-field re-validation of the prime-only
  censuses) — a cheap round-32 pilot or Codex-assist item.
- Mint: the stratum lemma + contrapositive as a background node.
- O4 (the A=1-core scope question) is live for the PRIME pose too —
  carried on the audit, not e-axis-specific.
- The second decisive cell (q = 625) and q = 729 — cheap wall-limited
  gaps worth one targeted run.

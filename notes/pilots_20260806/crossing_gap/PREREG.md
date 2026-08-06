# PRE-REGISTRATION — THE CROSSING GAP: the prime-row emptiness question (round 20, GENERATIVE + one adversarial check)

Round 20, 2026-08-06. Coordinator-authored brief; the pilot appends
its own registrations BEFORE any computation. The crossing low-w
core at PRIME rows (tau = 2, subcritical — EMPTINESS is the target
per the phase transition): the official primes sit provably in the
gap between the two closed ends (SP-COVER from below, CS from
above, 2^4.69 wide in w). Close or narrow the gap; and re-verify
the cliff the whole bracket stands on.

## 0. The state (quote verbatim before working)

- background/nodes/es_ternary_suppression_instruments — THEOREM CS
  (+ CS-M's window-free upgrade via LEMMA BR,
  notes/pilots_20260806/tern_master_statement/), SP-COVER/COS/
  SP-UNIFORM, SP-TERNARY, CATCH E-3 (the gap; re-labelled a
  shared-row property by the round-19 adversary bank).
- background/nodes/tern_master_threshold — tau = 2 at these rows;
  the per-tau target (emptiness); COROLLARY PT-2 (the 0.336-bit
  cliff); the untested cell (constant-weight Z-FLOOR at I2 — "the
  one place a genuinely new instrument might live").
- notes/pilots_20260806/efloor_sparsity/ — the even-condition lead
  (residual 5: "even-window conditions are used in none of the
  proofs, yet the census shows they matter... An even-condition
  SP-COVER would lower every threshold — the most obvious next
  step").

## 1. Pre-registered deliverables

- **(C1) THE EVEN-CONDITION EXTENSION.** Round 18's named next
  step: extend SP-COVER to use the EVEN window conditions. By
  LEMMA OE the even conditions live on sigma (the next stratum) —
  so an even-condition SP-COVER is a RECURSIVE statement: coverage
  at stratum a plus coverage of the reduced instance. Formalize the
  recursion, prove the extended coverage criterion, recompute
  w_cov(p) — the census says p = 7 empties at w = 7 while
  odd-alone never suffices: your extension must reproduce that
  cell. Then: how much of the 2^4.69 gap closes?
- **(C2) THE UNTESTED CELL — constant-weight Z-FLOOR at I2.** The
  round-19 adversary's residual 6. Z-FLOOR-M's scope note says the
  difference-multiplicity weighting is NOT the constant-weight
  functional — derive the constant-weight analogue: a floor for
  #{S of weight exactly r' : window conditions} via the collision
  identity restricted to the weight shell. If it exists, it is a
  NEW instrument at exactly the crossing instance; if the
  restriction breaks the identity, prove why (that too is new).
- **(C3) THE PT-2 CLIFF RE-VERIFICATION (adversarial check).** The
  bracket's lower endpoint w = 2^34 rests on RHL-LB (the proved
  floor a_L >= k + 2^34) and clears the supercriticality threshold
  by 0.336 bits. Re-derive RHL-LB's constant from its source with
  fresh eyes (the exactness of "2^34" — is it exact, floored, or
  conventional?); recompute the clearance under both the new-part
  and nested readings and both Lambda parities; state whether ANY
  banked reading places the endpoint below the threshold. If one
  does, that is a MAJOR catch (prime rows supercritical =>
  emptiness is false at the endpoint) — reproduction script + stop.
- **(C4) THE GAP VERDICT.** After (C1)-(C3): the exact remaining
  (p, w) gap for the prime-row emptiness question, and the honest
  list of what could close it (with the dead routes named — the
  SPD union bound is proved vacuous; do not resurrect it).

## 2. Pre-registered falsifiers / honesty clauses

- (C1)'s extension must reproduce the p = 7, w = 7 census cell or
  report the mismatch as a defect in the extension.
- (C3) is adversarial: the desired answer does not exist; report
  the clearance as computed, whichever way it falls.
- 2-power lengths; no shift-0 cells; name the functional
  (weighted/unweighted) in every measured claim (CATCH-19C rule).

## 3. Rules of engagement

- DRAFT ONLY: write only inside notes/pilots_20260806/crossing_gap/.
  Never edit dag.json, node shards, tools/, or push. Do NOT read
  notes/pilots_20260806/gamma_shell/ (sibling this round). Do NOT
  read CAMPAIGN_LEDGER entries appended after the "ROUND 20
  LAUNCHED" marker.
- COMPUTE LAW: never bare python3, INCLUDING file patching and JSON
  peeking — tools/ramguard tiny|local -- python3 ..., literal --,
  from repo root /home/u2470931/smooth-read-solomin/prize.
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report; the
  coordinator persists it verbatim.

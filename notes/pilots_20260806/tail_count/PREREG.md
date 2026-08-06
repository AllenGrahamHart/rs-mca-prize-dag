# PRE-REGISTRATION — THE TAIL-COUNT CRITERION attacked (round 20, GENERATIVE)

Round 20, 2026-08-06. Coordinator-authored brief; the pilot appends
its own registrations BEFORE any computation. The F2 mass terminal's
open form (post-route-(b)): the TAIL-COUNT criterion. No named route
exists; two leads do. Attack them.

## 0. The state (quote verbatim before working)

- background/nodes/f2_z1_mass_knife_edge (post-corrections) — the
  terminal: Z_1 <= 2^{o(m)} at k = e iff the tail count
  |{u in F_p^R : P(u) >= 2^{cS}}| <= 2^{(1-c)S + 46 + o(S)} for
  every c in [0,1], where P(u) = prod_{s<S}(1 + cos(2 pi
  f_u(zeta^s)/p)) — the exact 1+cos form (round-19 tern_route_b,
  machine-verified; the object is a sum of NON-NEGATIVE terms, no
  cancellation exists).
- notes/pilots_20260806/tern_route_b/{REPORT.md, PROOFS.md} —
  PROPOSITION 10 (LEAD 1): log2 P(u) EXACTLY as a doubling-map /
  log-sine functional (Dedekind-sum-shaped, strictly finer than
  V_1; no bound known); LEMMA 2 (complete subgroup sums); LEMMA 5
  (AM-GM); THEOREM 7 (the 2^{0.8908 S} baseline to beat);
  COROLLARY 8's family trap (any argument ending in a low-l1
  relation count re-enters the dead family — your route must not).
- notes/pilots_20260806/tern_small_scale_laws/{REPORT.md, PROOFS.md}
  — (LEAD 2) the p = 7, w = 4 484x OVER-representation: 9 orbits
  where 0.019 expected — an unidentified mechanism that CREATES
  ternary codewords. Understanding creation is the flip side of
  bounding tails: the tail count is large exactly where creation
  mechanisms operate.

## 1. Pre-registered deliverables

- **(T1) LEAD 1 — bound the doubling functional.** Prop 10 writes
  log2 P(u) through the value multiset {n_c(u)} and the doubling
  map c -> 2c with log-sine weights. Attack lines in order:
  (a) the doubling map's orbit structure on F_p^* (2 has order
  ord_p(2) — the functional telescopes over doubling orbits; does
  orbit-averaging bound the log-sine sum? Dedekind-sum literature
  shapes apply?); (b) equidistribution of {f_u(zeta^s)} for typical
  u via the value-multiset second moment (which is NOT a low-l1
  relation count if routed through n_c directly — verify you evade
  Corollary 8's trap and SAY HOW); (c) the large-P(u) structure:
  P(u) >= 2^{cS} forces the multiset to concentrate near c = 0 —
  what does concentration force on u? A structure theorem for
  large-P u ("the tail is structured") would convert the tail
  count into a parametrized family count.
- **(T2) LEAD 2 — the creation mechanism.** Identify the p = 7,
  w = 4 mechanism exactly (the cell is tiny: enumerate the 288
  codewords, find the algebraic pattern — subfield? norm form?
  quadratic residue structure?). Then: does the mechanism have an
  analogue at the F2 object's parameters (split primes, all-odd
  windows)? If provably NOT (like TWT), that is a tail-count
  constraint banked; if YES, it is a creation lower bound the
  terminal must respect — either way the terminal sharpens.
- **(T3) THE CRITERION AT TOY SCALE.** Measure the actual tail
  profile |{u : P(u) >= 2^{cS}}| exactly at the round-19 toy rows
  (G1-G6 shapes) — the empirical tail law vs the criterion's
  requirement. Does the measured tail obey (1-c)S-type decay with
  a bounded additive constant? Pre-register the grid; 2-power
  lengths; NO shift-0 cells (the integer layer).
- **(T4) THE VERDICT.** One of: a proved tail bound for some c-range
  (partial progress, state exactly which c); a structure theorem
  for the tail (route-shaped); a proved obstruction (the criterion
  needs input the object does not supply — name it); or honest
  null with the measured tail law banked.

## 2. Pre-registered falsifiers / honesty clauses

- Corollary 8's family trap is a MANDATORY self-check at every
  step: any bound consuming a distance theorem + a counting step
  must be flagged and its threshold computed — landing at p <= O(1)
  again means the route re-entered the dead family.
- AK-UNIT: no congruence conclusions about counts.
- Measured tail laws are evidence, never proof; label throughout.

## 3. Rules of engagement

- DRAFT ONLY: write only inside notes/pilots_20260806/tail_count/.
  Never edit dag.json, node shards, tools/, or push. Do NOT read
  notes/pilots_20260806/f2_repose/ (sibling this round). Do NOT
  read CAMPAIGN_LEDGER entries appended after the "ROUND 20
  LAUNCHED" marker.
- COMPUTE LAW: never bare python3, INCLUDING file patching and JSON
  peeking — tools/ramguard tiny|local -- python3 ..., literal --,
  from repo root /home/u2470931/smooth-read-solomin/prize.
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report; the
  coordinator persists it verbatim.

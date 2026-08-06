# FABLE_AUDIT — tern_route_b (round 19, pilot 3 of 4 to report)

**Auditor:** Fable, 2026-08-06. **Verdict: BANKED — ROUTE (b) IS DEAD
AS POSED: the minted node's "factor-2 headroom" sizing dropped the
DEGREE factor (restored: deg·sqrt p = 2^65 vs |H| = 2^39 — Weil
vacuous by exactly 26.000 bits), and the only executable substitute
(AM-GM + Z-2 moments) lands on THEOREM Z-NOGO's own p <= 8
threshold, gap 60.95 bits in log2 p. FORCED CORRECTION APPLIED to
f2_z1_mass_knife_edge (the second this round): the terminal now has
NO NAMED ROUTE — the open form is the TAIL-COUNT criterion. What the
pilot banked on the way out is substantial: the exact 1+cos
character identity (gate PASSED, machine-exact), PROPOSITION 3 (the
object is a sum of p^R NON-NEGATIVE terms — cancellation between
tuples does not exist in principle; the route was mis-CONCEIVED, not
just mis-sized), two favourable reductions that defeat both feared
round-15 loss modes (LEMMA 2: oddness makes every sum a COMPLETE
subgroup sum; LEMMA 5: AM-GM makes it a first-moment statement),
THEOREM 7 (unconditional Z_1 <= 2^{0.8908·S} — the first
unconditional nontrivial mass bound, 3.0e10 bits below trivial), and
PROPOSITION 10 (the doubling/log-sine exact identity — the recorded
lead).**

Replay: verify_route_b.py 137/137 exit 0 (coordinator re-run under
ramguard local). Anchors verified verbatim: z1 PROOFS.md:394 (the
1+2cos line — CATCH-B1 confirmed: it computes the UNWEIGHTED count;
explicitly disclaimed as non-theorem at :545-546, so nothing
downstream breaks); the minted node's route-(b) sizing lines
(CATCH-B3 — corrected this bank, dag recompiled, verify PASS).

ADOPTED:
- **PROPOSITION 3 + 4 + THE LEDGER**: no cancellation exists in
  principle; the trivial-character term reproduces the knife edge to
  0.005 bits (decomposition validated); the R2 literal target is
  unsatisfiable and the true criterion is the tail count
  |{u : P(u) >= 2^{cS}}| <= 2^{(1-c)S+46.02+o(S)} for all c — THE
  OPEN FORM OF THE F2 TERMINAL from here on.
- **LEMMA 2** (complete subgroup sums — answers the brief's
  half-vs-full question outright, favourably) and **LEMMA 5**
  (first-moment in V_1 only, no L2->Linf step) — the two round-15
  loss modes provably do not bite; the fatal one is DEGREE, which
  the brief did not name (CATCH-B4: my brief's because-clause
  mis-cited the round-15 mechanism — the record says L2->Linf, and
  square-root cancellation actually HELD in the round-15 bulk;
  coordinator brief defect accepted, and the "1-2 orders" gloss is
  re-labelled: the ratios track sqrt p).
- **THEOREM 7 + COROLLARY 8** (with the honest constants note:
  8.30 is the most generous provable threshold; the SHAPE is
  constant-free) — landing on Z-NOGO's threshold is structural (the
  moment route consumes distance + count, so it is IN the family
  Z-NOGO killed); Z-2's hypothesis exactly load-bearing (the k <= R
  cap is sharp at G2).
- **PROPOSITION 9** (the quadratic/quartic Gauss evaluations govern
  the OPPOSITE object — my brief's 2-power-Gauss chase was
  misdirected; the pilot chased it and killed it properly) and
  **PROPOSITION 10** (the genuine 2-power exactness: log2 P(u) as a
  doubling-map/log-sine functional — Dedekind-sum-shaped, exact,
  strictly finer than V_1; A LEAD, no bound known, and any argument
  ending in a low-l1 relation count re-enters Corollary 8's family).
- The toy table: Parseval exactly right in the bulk (RMS = sqrt|H|
  to three digits) — route (b)'s problem is ENTIRELY in the tail;
  max/|H| rising with p (0.43 -> 0.63).
- CATCH-B1/B2/B4 as brief/bank corrections (B2: additive not
  multiplicative characters — my brief's label wrong, its
  local-factor hint right).

BOARD CONSEQUENCE OF RECORD (stated as plainly as the pilot did):
with (a) dead-quantified, (c) localising only, distance+counting
killed by Z-NOGO, and (b)'s sizing refuted, **the F2 knife edge has
no route with a named instrument behind it.** The open form is the
tail-count criterion; the leads are Prop 10's doubling identity and
whatever the master-statement/adversary pair surfaces. HONEST
LIMIT: this is implementation-death, not Z-NOGO-strength — a third
supply (e.g. via Prop 10, or moments not routed through Z-2) is not
excluded.

HONEST RESIDUALS accepted (tail count open; no max|V_1| lower bound
claimed — the §3.4 construction correctly flagged heuristic;
Theorem 7's constant not optimal; shift-0 scope inherited and
satisfied by the official window). Process clean; sibling never
read. DRAFT-ONLY confirmed.

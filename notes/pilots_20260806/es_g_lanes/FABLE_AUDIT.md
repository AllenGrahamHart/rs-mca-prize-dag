# FABLE_AUDIT — es_g_lanes (round 17, pilot 2 of 4 to report)

**Auditor:** Fable, 2026-08-06. **Verdict: BANKED, MAINTAINER-LEVEL —
the FOUR-LANE UNIFICATION IS BROKEN AS WIRED. Only u2c can cite
(ES-G) (its pin is the global form verbatim); the rate-1/16 band row
and the dli RES row are above global balance at EVERY admissible
parameter (routing BROKEN); the crossing lane fails at w = 2^34 at
all 19 admissible (p-class, e) pairs under the adopted stratum
clause; and the four lanes' field requirements are MUTUALLY
UNSATISFIABLE — no single row satisfies all four. The "unified
terminal" framing is WITHDRAWN of record and replaced by a
regime-split terminal family.**

Replay: esg_selftest.py 1413/1413 exit 0 (coordinator re-run under
ramguard local). Anchors verified by the coordinator directly, all
verbatim-exact: THEOREM Q (crossing_w2_opening/REPORT.md:69);
DLI_CLOSE_PINNED.md:164-166 (2^N >= q^L) + the H2 hypothesis
(dli_c1r3_gated_envelope_bound/statement.md:12); the round-15
"discharges all four consumers" line (mun REPORT.md:53); the
per-weight functional at
notes/pilots_20260803/sl2_unstructured/descent.py:211-213.

ADOPTED — THE TERMINAL RE-SCOPE OF RECORD (coordinator adjudication;
statement-level; wiring changes to mint-4):
- The round-15/16 claim "(ES)/(ES-G) is the unified terminal of four
  lanes" is WITHDRAWN. The statement of record becomes:
  (a) **u2c**: (ES-G) verbatim — the lane's own pin; the five
      round-16 witnesses confirmed excluded by independent
      recomputation (P5).
  (b) **crossing**: (ES-G) applies at w >= 2^37 (19/19 admissible
      pairs, deep strata included); at w in {2^34, 2^35, 2^36} the
      DEEP STRATA are a separate named obligation — the n_a = 256
      one-condition instance, small enough for direct attack. At
      w = 2^34 no admissible row clears the binding stratum (the
      requirement log2 p >= 256 IS the rules cap).
  (c) **band (both nodes)**: (ES-G) is NOT available at rate 1/16 at
      any (d, q) (deficit >= 512 bits at the cap), nor at the
      low-depth 22.5% of rates 1/4-1/8 scope at the banked pin. The
      band lanes need either a re-posed weight-aware balance form
      (the retired per-weight heuristic does predict suppression
      there but is refuted as a theorem) or a non-balance argument.
  (d) **dli RES**: (ES-G) is UNWIRED — the lane is above global
      balance by its own proved scoping hypothesis (H2/A2); its
      above-balance flatness instruments (C1'/C2''/WCL-ZONE) are the
      route of record, as they already were. The round-15 "discharges
      all four consumers" claim is REFUTED for this lane (mun
      FABLE_AUDIT addendum #2 written this bank).
- **The mechanism finding adopted**: by THEOREM Q, extension rows
  (e >= 2) get no balance credit while e divides log2 p — tower rows
  are the adversary's best choice against (ES-G). This goes into the
  crossing lane's obligation statement and any future Pro brief.
- **|Z_w| closed forms banked** for all 8 admissible p-classes, with
  CATCH-B (bracket top never attained at delta = 4 — 33% over-credit)
  and CATCH-C (orbit merge at w = 2^38, 2^39; ratios not w-uniform).

CATCHES ACCEPTED (all to the mint-4 / maintainer queues):
- CATCH-D: the band q >= 2^209 pin computes the RETIRED per-weight
  threshold — 47.5 bits short of (ES-G) at its own depth; the pin
  must be re-derived under whatever form the band adopts.
- CATCH-E: the u2c node carries three different bases in one
  statement (q^t / |B0| / p^{|Z_w|}) — pin to one (THEOREM Q says p,
  the least favourable, for the crossing instance); the "~2%" prose
  corrected to the 0.089-bit sliver; and the MUTUAL UNSATISFIABILITY
  of the four lanes' field regimes — the reading of record: each
  lane's obligation ranges over ALL admissible rows in its scope
  (rules quantifier), so no shared-row discharge was ever available;
  the unification was of STATEMENT SHAPE, not of regime.
- CATCH-F: as above (dli RES unwired).
- CATCH-A (self-caught float defect, fixed by its own PREREG clause,
  all verdicts from the certified 140-digit comparator) — the
  discipline working as designed.

HONEST RESIDUALS accepted, one elevated: the BAND EFFECTIVE-BASE
question (if the band analogue of catch #11/#13 moves the base to the
generated field, every band verdict worsens) — a named next-round
item; also the syzygy rank-bracket end and the stratum-scope
softening clause (11/19 still fail at a = 0 with the explicit
exhibit, so the crossing finding survives any stratum-scope repair).
Two of six own predictions self-refuted and reported as refutations —
accepted. DRAFT-ONLY confirmed; sibling never opened.

Coordinator note: this pilot plus round 16 completes a full
falsification cycle on the terminal: posed (round 15) -> split by
reading (round 16) -> re-scoped per lane (this bank). What survives
is SMALLER and TRUE: u2c pinned correctly all along; the crossing
high-w regime is (ES-G)-covered; everything else now has a named,
honest obligation instead of a borrowed one.

## ADDENDUM (2026-08-06, coordinator, from round-18 crossing_low_w)

1. P4's 19/19 deep-stratum balance failure at w = 2^34 was DETECTING
   A REAL REFUTATION: THEOREM DSA proves accidents exist at every
   admissible tower row in the pigeonhole regime, with a verified
   witness at n = 2^41 (the same p = 3·2^41+1, e = 6 row as this
   pilot's exhibit). The balance verdict was not a pricing artefact.
2. Hygiene: REPORT.md:105's log2 S(2^34) = 117.149 is the
   per-sig-class shell; the structural count is C(128,63) =
   2^124.149 (exactly log2 128 larger). Do not interchange.
3. The GLOBAL functional's deep-stratum requirement (log2 p >= 256)
   and the retired per-weight one (251.6) are BOTH mis-priced there:
   the correct primitive count is ternary (3^L, requirement 202.9,
   orbit-corrected 194.9). See crossing_low_w LEMMA TC.

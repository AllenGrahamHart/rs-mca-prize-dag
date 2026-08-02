# Fable audit of the P-B |Gamma| exposure pilot — 2026-08-02

**Verdict: ACCEPTED — and it corrects the campaign's own framing
twice, in the productive direction both times.** (1) Kill line K1 is
CLOSED for the entire split-fibre construction class by an elementary
proved lemma: the self-collision identity |S_J ^ S_J'| = g + m|J^J'|
puts every planted slope at pairwise core A - m >= K (because the
recipe's own range m <= h forces it), so the family contributes
exactly ZERO to Gamma_lo at every q — the adversarial audit's M-family
can never attack P-B, structurally, independent of any selector.
(2) The FM3-era re-target "bound |Gamma|" is REFINED: P-B's obligation
is |Gamma_lo| (as always stated); the FM3 official-scale story is
right for the random supply and wrong for the planted part. The
residual exposure is construction-free, confined to RowC 1/4 on an
explicit q-window, and decided by a genuine q-scope ambiguity in the
tree (two banked specifications, both cited to file:line, answering
oppositely). That adjudication is SURFACED.

## Independent verification record

- Replayed the three gates this session: census.crosscheck()
  (bit-exact against all 12 banked k1_Q*.json — totals, live slopes,
  full per-slope histograms), score.py (frozen predictions: C1 fails
  10/32, C4 4/4, C5a 0/79, C5b 7/8 — exactly as reported; corrected
  law ratios 0.47-1.30 over 100 points), qpin_ledger.py (the RowC 1/4
  window arithmetic: mean generic live slopes 2^64.29 = 2.63e9 x 8n^3
  at the window floor; envelope pin above L3 => pinned row safe).
- Hand-proved the self-collision identity: supports = g-point core +
  a fibres of width m chosen by J from F - g; intersection = core +
  shared fibres = g + m|J ^ J'|; max at |J ^ J'| = a - 1 gives
  g + ma - m = A - m; m <= h gives A - m >= A - h = K. Elementary,
  correct, and the reason is structural (the recipe cannot make its
  planted family a distance->=4 constant-weight code).
- Hand-derived the exposure criterion: window [L1, L3) non-empty <=>
  (C.2^128)^{1/h} < (C/8n^3)^{1/(h-1)} <=> C > (8n^3)^h.2^{128(h-1)}.
  Correct.
- The pre-registration discipline held and produced the round's most
  honest moment: the pilot's own expectation (C5a: low density
  restores the construction) failed 0/79 — the measurement overruled
  the design intuition, in P-B's favour.

## Findings adopted

1. **K1 CLOSED for the split-fibre class** (structural, selector-free).
   The P-B lane note is amended: the obligation is |Gamma_lo|; the
   planted family lives entirely in Gamma_hi; the adversarial surface
   for (H4) shrinks to "constructions planting a distance->=4
   constant-weight witness family above 8n^3", which the split-fibre
   recipe provably cannot produce.
2. **The named exposure is SURFACED as the lane's top adjudication**:
   RowC 1/4, q in [2^192.29, 2^200.11), |Gamma_lo| up to 2.63e9 x
   8n^3 from the RANDOM supply alone — live iff the (P1)
   family-uniform scope governs P-B; dead under the (P2) envelope
   pins (q >= 2^250, >= 49.9 bits slack). The scope call is the
   coordinator/maintainer's, informed by the fact that
   official_row_primes_pinning is itself PROVED and demands
   family-uniform certificates absent a transport theorem. Queued for
   the Pro round alongside the (PB-SUPPLY) discharge skeleton.
3. **RowC 1/16 flagged FRAGILE** (2.31 bits from exposure; 58.6% of
   the budget consumed at its worst admissible q). Any few-bit
   correction flips it; recorded as a standing sensitivity.
4. **The row-soundness observation routed to the maintainer**: the
   2^189 char-0 (2^55 rigorous single-field) distinct-bad-slope
   pencil is a matching LOWER bound for the gap the tree already
   records at xr_agreement_raise_quotient_safe_sum_fence ("one active
   summand already exceeds B*"). Not a P-B item; belongs in the next
   upstream coordination message.
5. **My earlier "safe by field size" conjecture is REFUTED** (no row
   has q_max < 8n^3 under either specification — safety comes from
   witness supply). The OFFICIAL_SCALE_REFRAME note and the
   CAMPAIGN_LEDGER A.5 item are amended accordingly.
6. **(PB-SUPPLY) adopted as the lane's candidate discharge shape**:
   P-B reduces to (H4)-restricted (non-split-fibre concentration)
   plus the (H3)/scope decision at RowC 1/4. This is the sharpest
   statement of what remains of P-B, and it goes to Pro.

## Caveats kept (endorsed)

- The Gamma_lo purity at official scale is an FM3-type extrapolation
  (toy-scale random collisions vanish as Pi -> 2^-693) — in the
  UNFAVOURABLE direction for P-B, honestly labeled.
- N_split char-0; single-field rigorous to ~2^55 only.
- (H2) is an operationalization of "sufficiently large", not a banked
  node; L1 moves with any banked floor.
- The self-collision lemma covers the split-fibre recipe only; (H4)
  outside that class is open.
- Nothing proved about P-B itself; the margins are exact integer facts.

> [AMENDED same day — pb_h4_hunt pilot.] (SF-SELFCOLLISION)'s
> Gamma_lo = 0 conclusion is a JOINT identity + support-keyed-selector
> theorem (adjacent partners live at other slopes; uniform selector
> leaves ~q e^{-nu}, official nu = 3.0 => ~2^187; support-lex 0 at
> 18/18). K1 remains closed for the class — now verified at the
> official ratio — but (PB-SUPPLY)'s (H4) clause must state the
> selector hypothesis, re-coupling K1 to the PP4.0 A1 fork. Also:
> strip/genericity gates must be stated gauge-invariantly (on
> (alpha,beta) mod RS_K). See pb_h4_hunt/{REPORT,FABLE_AUDIT}.md.

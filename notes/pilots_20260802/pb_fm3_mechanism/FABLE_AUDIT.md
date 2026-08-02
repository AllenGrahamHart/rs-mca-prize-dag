# Fable audit of the FM3 mechanism pilot — 2026-08-02

**Verdict: ACCEPTED — and this is the campaign's most consequential
strategic finding.** The support-keyed collapse that survived K1 is a
SMALL-q/n PHENOMENON: the parameter-free greedy-depletion model
(validated at 15 shapes, pre-registered predictions 5/6 PASS, block
sizes exact) extrapolates to (K-chi)/sigma ~ 18-20 at official RowC
scale, i.e. Gamma_hi EMPTY and Gamma_lo = Gamma for every order. The
corroborating model-free count Pi (expected >=K-core partners in the
population) is 2^-73.5 at official RowC 1/4 — the pairs are not in the
population for ANY selector to find. FM3 as a "Gamma_lo is small"
theorem is dead at official scale; the R2 partition is a routing device
with no compressive content; and P-B's real obligation is BOUNDING
|Gamma|, not partitioning it.

## Independent verification record

- Replayed `fm3_score.py` against the frozen `PREDICTIONS.json`:
  C1/C2/C4/C5/C6 PASS, C3 FAIL at R2 exactly as reported (the honest
  miss, in the known low-density bias direction). The pre-registration
  discipline held: predictions frozen before R1-R3 were run, the
  script refuses overwrites.
- Hand-checked the Pi formula: partners at core c of a fixed A-support
  number C(A,c)C(n-A,A-c); the witness density per support across all
  slopes is q x C(n,A)/q^h / C(n,A) = q^{-(h-1)}; summing c from K to
  A-m gives Pi = SUM C(A,c)C(n-A,A-c)/q^{h-1}. Consistent, and
  validated by the pilot against true population counts (ratio
  0.97-5.3 at h = 2,3).
- Checked the structural argument that kills the K-prefix
  asymptotically: L* is set by density/rate (not n) while K = rate.n,
  so the block deficit d = K - L* grows linearly in n. Sound — the
  withdrawn FM3 wording was not just false at small scale but
  anti-scaling.
- Checked the hash-null observation directly: the null comparators key
  on blake2b(mask) — a function of the support alone — so they ARE
  support-keyed total orders. The K1 pilot's class label was wrong;
  the collapsing property is greedy coordinate-sequential minimality
  (the "compression order" definition). My PP4.0 recommendation is
  CORRECTED accordingly (see below).
- The null-ladder logic (N0-N3) and the population factorisation
  P_sel = P_unif x STRUCT x TILT are internally consistent with the
  banked K1 data (which I previously replayed end-to-end at Q1).

## Findings adopted (several correct MY prior positions)

1. **PP4.0 recommendation CORRECTED (still surfaced):** freeze the
   COMPRESSION-ORDER class (greedy coordinate-sequential: lex/colex
   under any coordinate permutation), NOT "support-keyed" — the
   support-keyed class admits the RED hash nulls. This supersedes the
   wording in my pb_selector_orders audit and the CAMPAIGN_LEDGER.
2. **The P-B lane RE-TARGET is surfaced as the top strategic item:**
   at official scale the binding constraint is |Gamma| <= 8n^3 (P-B
   alone carries it; Gamma_hi is empty; the R2 partition never
   compresses — |Gamma_hi| + |Gamma_lo| = |Gamma| identically). The
   lane's question becomes: can a split-fibre construction realize
   more than 8n^3 LIVE SLOPES for one received pair in one field at
   an official row? The adversarial audit's M = 1.3e11 vs
   16n^3 = 1.7e10 at RowC must be re-examined on this footing —
   noting |Gamma| <= q automatically, so rows with pinned q < 8n^3
   are safe by field size alone, and the exposure is confined to rows
   whose q exceeds the budget. This adjudication (which rows, which
   q pins) is queued as a coordinator pass, then to Pro.
3. **The n=44/48 fleet item is RE-SCOPED**: its target is Pi, not the
   budget clause. Sharp pre-registered prediction: at n=44, rate 1/2,
   q = 1.33e6, Pi = 2^-4.4 < 1 and Gamma_lo = Gamma for EVERY order
   including lex. One measurement, confirms or destroys the central
   claim. CAMPAIGN_LEDGER updated.
4. **FM3 as drafted by the mechanism pilot is a CONDITIONAL statement
   whose entire content is (H)** — equidistribution of elementary
   symmetric functions over subsets of mu_n (Weil/character-sum type,
   not known). Recorded as such; NOT a proof target for the lane in
   the small-scale regime where it holds, since the regime is not the
   official one.
5. **The exchange/swap route is closed** (the third refutation of my
   original FM3 framing): per-slope minimality gives swapped sets no
   standing in the new fibre, and the validated independence of the
   N3 model leaves no exchange-induced correlation to harvest.

## Caveats kept (endorsed, and they matter here)

- The official-scale verdict is a 5-doubling MODEL EXTRAPOLATION
  (though conservative in direction: the Poisson-binomial
  approximation over-estimates P at small n).
- (H) fails measurably at Q11 (x55, the designed fibre family = 41%
  of a tiny population); the extrapolation rests on that being a
  small-population artifact (the fibre fraction is ~2^-588 at official
  scale). This is exactly the kind of assumption Pro should attack.
- Nothing measured has both the official fibre shape AND selector
  competition (unreachable below n ~ 44).
- The clustering term (over-dispersion of the >=K graph) is
  unmodelled; c_1 is fitted.
- No part of FM3 or (H) is proved; everything is measurement + a
  validated parameter-free model.

## Cross-pilot consistency note

This finding harmonizes with (not contradicts) the K1 pilot: at every
COMPUTABLE scale the compression-class collapse is real, one-sided,
and strengthens with density — all confirmed here with the mechanism
identified. What changes is the extrapolation: the collapse's driver
(the greedy block deficit K - L*) grows with n, so the phenomenon
inverts at official scale. Mechanism verdicts survive; the density
framing (my adopted wording) is corrected to the deficit framing.

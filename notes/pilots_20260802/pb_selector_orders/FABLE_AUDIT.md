# Fable audit of the P-B selector-orders / K1 pilot — 2026-08-02

**Verdict: ACCEPTED.** The A1 fork (what object the selector order keys
on) is outcome-deciding and one-sided: all five support-keyed orders
survive K1 (retention 0.000-0.078 at every dense n=32 scale, against
null controls at 0.79-1.00), all three polynomial/codeword-keyed orders
reproduce the adversarial audit's super-budget family shape (retention
0.938-1.000). The collapse STRENGTHENS with witness density — the
direction of the official scale. This is the evidence base for the
surfaced PP4.0 decision; the decision itself remains surfaced.

## Independent verification record

- Replayed `k1_summary.py` (aggregation + table build): reproduces
  K1_TABLE from the banked per-case JSONs.
- Re-ran case Q1 END-TO-END (`select` then `stats`) into scratchpad and
  diffed against the banked `k1_Q1.json`: selected families
  (`selected_masks`), `Gamma_lo`, K1 class and exact budget ratio match
  across ALL 13 orders — zero mismatches. Combined with the pilot's own
  bit-exact cross-validation at the nine parameter points shared with
  the prior pilot (which I audited independently on 2026-08-01), the
  computation chain is closed.
- Hand-proved all three structural claims:
  (1) ERRLEX reversal: for S,T subset D with |S|=|T|=A,
  (D\S) Delta (D\T) = S Delta T, and min(S Delta T) in D\S iff it is in
  T, so S <_ERRLEX T iff T <_LEX S. Exactly reverse-lex.
  (2) Slope-major degeneracy: z is constant on each W_z, so the leading
  key never separates and the selection equals the tail order's.
  (3) Budget untestability: |Gamma_lo| <= live <= min(q, #witnesses),
  #witnesses ~ C(n,A)/q^{h-1}, and a split-fibre pencil forces
  h >= m >= 2, so testing |Gamma_lo| > 8n^3 needs q > 8n^3 AND
  C(n,A) > (8n^3)^2 — first reachable at n = 44, rate 1/2. Sound; all
  GREEN/RED verdicts are mechanism verdicts, correctly labeled.

## Findings adopted

1. **PP4.0 evidence (decision stays SURFACED).** My recommendation to
   the maintainer/user, now with data: freeze PP4.0 as a
   SUPPORT-KEYED CLASS specification — any total order keyed on the
   agreement support (lex as the canonical representative), with a
   class justification rather than a single-order coin-flip, since all
   five class members collapse the kill-line family identically.
   The freeze must EXPLICITLY exclude polynomial-keyed, codeword-keyed
   and procedural (decoder-enumeration) readings: each of those is RED,
   and at the first budget-testable scale (n=44) a retention of 1.000
   would be an actual budget violation. Two forks recorded as closed:
   slope-major is degenerate; error-support-lex is reverse-lex.
2. **FM3 as previously drafted is FALSE and is hereby withdrawn** (my
   own proposed wording from the 2026-08-01 pilot): the selected
   supports do NOT share a K-prefix (global common block 3-11 << K at
   every dense point; three collapsing orders have common block 0).
   The operating mechanism is global-block + pairwise birthday over
   ~q^2/2 slope pairs. The exchange-lemma target must be re-worded
   from that mechanism. Addendum written into the prior pilot's
   FABLE_AUDIT.md.
3. **The quantifier warning is now multi-order.** Pairwise low-core
   subfamilies retain 33-45% of live slopes everywhere; only the
   "meets EVERY other" quantifier ejects them. Any exchange theorem
   must engage the quantifier honestly, and any repair that weakens
   it (e.g. pairwise low-core) would change P-B's truth value.
4. **The re-routing observation links to the bridge repair.** Collapsed
   slopes land in Gamma_hi — mass moves into P-A1, not out of the
   ledger. Consistent with (and further motivation for) the R2 bridge
   partition and the widened P-A1 obligation adjudicated today.
5. **Highest-value follow-up adopted**: a bit-packed/native enumerator
   run at n=44/48 (first budget-testable split-fibre scales) on a
   larger box — the single experiment that could turn a mechanism
   verdict into a budget verdict. Queued for the fleet/Modal lane, not
   the 1G law.

## Caveats kept (endorsed)

- All verdicts are mechanism verdicts; the budget clause is provably
  invisible below n=44 (pilot's own proof, checked).
- Nothing tests the official fibre width m=4 under competition; that
  needs C(n,A) >> q^4, unreachable at n <= 32.
- The 4-orders-of-magnitude density trend is read against a 195-bit
  extrapolation to official scale; favourable and monotone, but a
  trend.
- ORD-POLYHI erratic (no mechanism claimed); ORD-DEGLEX's RED rests on
  the densest point.
- Support-keyed class agreement is evidence, not a transport lemma.

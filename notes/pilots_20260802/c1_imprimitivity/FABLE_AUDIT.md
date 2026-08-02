# Fable audit of the C1 imprimitivity pilot — 2026-08-02

**Verdict: ACCEPTED — the imprimitivity conjecture is REFUTED**, and
the refutation is the strongest-certified result of the campaign: an
exhaustive scan at 2N=64, w=11 (all 12 chunks, 316M polynomials via
the calibrated ~850x affine reduction) with a primitive argmax whose
norm I re-derived independently this session (sympy resultant of the
claimed argmax = 186873311^2 = 34,921,634,364,102,721 >
184,497,889^2 = the law's prediction; mixed-parity support confirmed).
The lane's "next theorem" is dead one round after it was posed —
before anyone spent proof effort on it. This is the falsifier-first
rhythm working exactly as designed.

## Independent verification record

- Replayed the w=11 certificate from `merged_n32big.json`: support
  {0,1,2,6,7,9,11,12,16,17,18}, Norm = 186873311^2 exactly, beats the
  law, primitive (mixed parity). Parts 0-11 of 12 all present.
- Inspected `verify_sympy.json`: the law-confirming maxima at
  2N=64 w=8,9,10 each carry three-path agreement (sympy resultant,
  Bareiss, descent) on the argmax; w=8's argmax is exactly iota of
  the published 2N=32 argmax, as the law demands.
- Checked the arithmetic primitivity certificate logic (imprimitive
  => Norm is a perfect square, since Norm_N(iota g) = Norm_M(g)^2):
  contrapositive is sound; 14760962 = 2 x 7380481 is not a square
  (3842^2 = 14760964), so the 2N=32 w=8 break was already certified
  arithmetically. Neat and correct (one-directional only — a square
  norm does NOT imply imprimitivity; the w=11 refutation witness has
  square norm and is primitive).
- Checked the mechanism table: the law forces delta to SQUARE at each
  doubling while fresh primitive constructions hold delta roughly
  constant — so failure at large w was structurally inevitable and
  the earlier "breaks only at w = N/2" reading was an artifact of
  N <= 16 (break weights 3, 7, 10 at N = 8, 16, 32: not N/2 at the
  third point). Sound.
- Exhaustiveness of the scans rests on the pilot's calibration record
  (the affine scanner reproduces the entire published 2N=32 table and
  the 2N=8/16 brute-force tables exactly; covering property validated
  at three levels with 0 uncovered) — strong, though I did not re-run
  the 316M-element scan itself.

## Findings adopted (binding on the C1 lane)

1. **The imprimitivity conjecture is REFUTED and retired as a lane
   target.** Dated correction appended to the sandwich node's
   "Explicitly NOT claimed" context section (the node's four PROVED
   claims are untouched — the pilot re-exercised all of them).
2. **What the lane actually keeps is unconditional and unaffected**:
   the router threshold q > w^(N/2) (Lemma B alone) and the
   saturating family {1,2,3,7}. The lane's census/threshold tools
   never depended on the exact doubling law; the refutation removes a
   would-have-been-wasted proof program, not a capability.
3. **Corrected picture of the doubling law**: holds exhaustively for
   w <= 10 at 2N=64 (and w <= 6 exhaustive + w = 7 proved at 2N=128);
   fails from w = 11 (exhaustive) with certified primitive witnesses
   at 12, 14, 15, 16; the c_w table gains certified constants at
   8-11 (c_9 = 79 now on two ladder points); c_w < w^2 STRICTLY at
   w = 4, 16, 64, ... unconditionally (the no-flat-at-4^t argument —
   a genuinely pretty piece of arithmetic: total ramification of 2 +
   Kronecker).
4. **Mint queue additions (small, proved, verified):** Lemma C
   (odd-autocorrelation monotonicity — exhaustively verified at N=8),
   the rotation identity (prod over the odd-twist family =
   Norm_M(p^{2M} + q^{2M})), and the two arithmetic tools
   (Norm == w mod 2; imprimitive => square). These are lane
   infrastructure, worth banking when the C1 lane next composes;
   queued in the CAMPAIGN_LEDGER, not minted today.
5. **Proof-attack necrology recorded**: majorization dead (explicit
   Schur-violation certificate), local moves dead (U-shaped value
   function with crossing branches — the two-branch structure with a
   gap of exactly 2 at (16,6) is the fingerprint of why every smooth
   argument failed), autocorrelation true-but-insufficient. Any
   future attempt on maxnorm structure starts from this map.

## Caveats kept (endorsed)

- w = 13 at 2N=64 honestly unresolved (expected to fail; not claimed).
- w = 12,14,15,16 failures are lower-bound certificates, not exhaustions.
- 2N=128 above w=6 and 2N=256 are hunt-only, and the hunter is weak
  at large N (0.51/0.65 of target at 2N=128 w=7/9) — no-beat there is
  weak evidence, correctly labeled.
- The affine reduction returns a covering (not exact) set of orbit
  representatives — sufficient for maximisation, validated as such.

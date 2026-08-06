# FABLE_AUDIT — efloor_sparsity (round 18, pilot 3 of 4 to report)

**Auditor:** Fable, 2026-08-06. **Verdict: BANKED — the first
unconditional sparsity theorems (SP-COVER + SP-UNIFORM: a = 0 bad
primes must satisfy p > sqrt(w+1); p = 3 dead for all w >= 6 at
every n; the bad-prime range is now TWO-SIDED with round-17's
CS-EXCL as the upper end), the densest-family adversarial search
finds NO refutation of CC-sparsity (the best family carries 49% of
the floor mass at 116x density and still dies at one step of w),
and round-16's unreached n = 64 flag is CLOSED (plus n = 128) by a
new exact meet-in-the-middle census over ALL subsets. But the
pilot's two structural catches force an honest DOWNGRADE of
round-17's conditional: E_floor is a TAUTOLOGY given THEOREM CS,
and CC-sparsity is (ES) AGAIN — at half length, over a ternary
alphabet — not a lemma beneath it.**

Replay: verify_sp.py self 52,510/0 exit 0 (coordinator re-run under
ramguard local; the full 10-stage suite totals 56,542/0 per the
pilot's persisted outputs, fail-closed proven by the injected-failure
stage). The CATCH E-3 gate arithmetic checked by the coordinator:
official rows force v_2(p^2-1) >= 41+1, so SP-COVER's threshold
2^{v_2(p^2-1)} exceeds the w-bracket cap 2^39 — the mechanism is
structurally blind exactly at the official primes, as claimed.

ADOPTED:
- **THEOREM SP-COVER / LEMMA COS / THEOREM SP-UNIFORM** (the
  two-sided bad-prime range: sqrt(w+1) < p <= the CS3 ceiling) and
  **THEOREM SP-TERNARY** (the second mechanism, per-(n,p,w)
  certified). **LEMMA AB** — the engine, and the third appearance of
  the TERNARY object this round (see the convergence note below).
- **LEMMA QS + the F1 quarter-shift family** (0.42% of sets, 49% of
  floor mass, dies at w+1) — the adversarial half's honest null:
  CC-sparsity SURVIVES its densest known attack, with the trade-off
  law measured (2^-7.9 size vs 2^+6.9 density, net negative).
- The n = 64 / n = 128 census closure (round-16 flag CLOSED, by two
  independent routes, quantization law reproduced) and the
  meet-in-the-middle method itself (all 2^32 subsets exactly — a
  scale jump over the round-17 orbit census; banked as machinery).
- **(CONV)** — the exact u2c conversion statement, with the honest
  verdict that the official q sits PROVABLY in neither closed end.
- The SPD honesty: the registered union-bound shape was PROVED
  VACUOUS in every regime (dual distance ~p^2 log n needed, BCH
  delivers ~n/|Z_w|) — pre-registered as the expected outcome and
  delivered as such; the middle of the prime range needs a
  non-character-sum idea.

CATCHES ACCEPTED — THE ROUND-17 DOWNGRADE OF RECORD:
- **CATCH E-1**: round-17's (K5) conditional "(CC-sparsity
  restricted to w <= 2^37.31) => (ES) on the remaining 28.84%" is
  RE-LABELLED of record: the E = E_strat u E_floor decomposition is
  a RESTATEMENT, not a reduction — the conditional's hypothesis is
  as hard as its conclusion. THEOREM CS and its unconditional 71.16%
  coverage are UNTOUCHED. Addendum written to the es_coprimality
  audit this bank.
- **CATCH E-2 (structural, the round's second unification signal)**:
  CC-sparsity = ternary vectors in a p-ary cyclic code at half
  length; (ES) = binary vectors in a p-ary cyclic code. COORDINATOR
  CONVERGENCE NOTE: this is the THIRD independent appearance of
  "ternary vectors in a p-ary code" as the primitive object this
  round — crossing_low_w's LEMMA TC (the deep stratum's primitive is
  epsilon in {0,±1}^L), this pilot's LEMMA AB, and the z1 pilot's
  entire mandate (ternary mass of a GRS code). The true shared
  terminal of the campaign may be the TERNARY-IN-CODE question, not
  (ES) — to be tested against the z1 report at its bank, then posed
  as the round-19 unification candidate if it survives.
- **CATCH E-3**: the official v_2(q-1) >= 41 gate is exactly
  SP-COVER's blind spot; the two proved exclusions (SP-COVER from
  below, CS-EXCL from above) do not meet, gap 2^4.69 in w. The
  low-w crossing core at official primes remains open — now with
  both of its closed ends proved.
- The pilot's own P2 miss (w_cov sharp in 1 of 6 cells) reported
  honestly — accepted.

HONEST RESIDUALS accepted; two elevated as leads: the p = 5, w = 2
zero-ternary anomaly (exact 0 vs ~110 flat prediction — something
suppresses ternary codewords beyond counting; possibly the same
mechanism z1 needs), and the even-condition SP-COVER extension (the
census shows even conditions matter; every threshold would drop).
COMPUTE LAW: ZERO breaches — the hardened brief clause worked; first
fully clean pilot since the pattern was flagged. DRAFT-ONLY
confirmed (find-based sweep); sibling never read.

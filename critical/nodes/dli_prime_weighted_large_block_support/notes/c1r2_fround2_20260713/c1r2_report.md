# C1' F-ROUND 2 — REPORT

## VERDICT: **KILLED** (C1', node `dli_dyadic_k_core`, r2 level-scaled pose)

The pre-registered LITERAL kill line (K' > 4, equivalently E-1 > 4r(1+W_cl))
FIRED at three independently-verified in-hypothesis rows. Worst **K' = 6.199084
at L=1, q=63361** (N=32). The predicate is REFUTED as stated.

## Kill-line outcomes (pre-registered in `c1r2_falsifiers.md`)

- **KILL-LITERAL (K'>4) — FIRED.** L=1 rows q=63361 (6.199), q=65921 (4.481),
  q=204353 (4.285). All prime, q=1 mod 64, 2^32>=q, N>=16. Independently
  re-derived with the banked M1/M2 kernels.
- **KILL-AMBER (K'>=1) — FIRED (12 rows)** including q=204353 (the node's own
  motivating cluster row).
- **KILL-SCALING — FIRED (literal).** K' exceeds 4 at three separate octaves
  (2^15,2^16,2^17); the accident envelope (E-1)/r rises to ~477 by q~63000
  while the window ledger does not keep pace — no extrapolation needed, K' is
  already above 4 at multiple scales.
- **KILL-ASPECT — FIRED at the smallest posed aspect.** The failure occurs at
  N=32, L=1 (the lowest analogue aspect the pose covers), for q well inside the
  2^N>=q^L hypothesis. The universally-quantified claim is false already here;
  the official large-N regime is not needed to break it.

Positive control (q=7937 -> K'=0.2469, raw==M2) and mutation control (W_cl:=0 ->
kill fires) both PASS, so the machinery is sound and the kill is real.

## Worst K' observed
**6.199084** (exact `2029645184561543/288230376151711744 ÷ (7937... )`; see
`c1r2_results.md`) at q=63361. Guaranteed to be the global max over the L=1 scan
to 262144, because K' <= (E-1)/r and every row with (E-1)/r > 6.199 was
enumerated.

## Evidence weight — HIGH / decisive
- Exact-rational throughout; two independent E paths agree (A_total DP ==
  banked signed_all_census) and match all 12 banked M2 rows.
- W_cl reproduced by the verbatim banked enumerator; positive control exact.
- Multiple kills (3) + 12 ambers, not a single fragile point; robust to the
  ledger-window cutoff (w<=7 still leaves K'=2.5-3.4).
- The kill uses NO weakened convention (raw ledger, w_max=L+5, 4-allowance all
  as posed). This is the opposite of "weaken to survive" — nothing was relaxed.

## Honest scope
Analogue rows at N=32 (n'=64): L=1 over primes q=1 mod 64 up to 262144 (fully
enumerated, W_cl computed for all 77 rows with (E-1)/r>=1); L=2 up to 4001. The
OFFICIAL dyadic tower (N~2^32, ~33 levels) is beyond direct reach as always —
but the refutation does not need it: C1' is false at the smallest posed aspect.
Deeper L=2 (q>4001) is DEFERRED (grid DP timeout) — corroborating, not required.

## What this means for the DAG (recommendation, not surgery — I am a worker)
- `dli_dyadic_k_core` (TARGET, "survived ZERO adversarial rounds" per its own
  note) has now FAILED its second adversarial round. Its status/attack_surface
  should record the refutation; its falsifier ("one row with excess exceeding
  4r(1+W_cl)") is satisfied by q=63361.
- Any downstream use of C1' as evidence toward marginal baseline coverage / the
  DLI route / B-WEAK should be treated as REFUTED at the r2 window, not merely
  "unproved". The r2 restatement's ">16x margin" claim (from M2) is false out of
  sample.
- **The named-conjecture amber flip this round was gating must NOT proceed** on
  C1' in its posed form.

## Round-3 design (for whoever re-poses)
The mechanism (c1r2-C4/C5) is precise, so a repose is testable:
1. **The real question is the SHADOW, not the window.** A lone weight-3 primitive
   orbit pumps the residual by ~200-480 while contributing 8 to the window
   ledger. Round-3 should price the weight-3 orbit's FULL multiplier-shadow +
   additive-cluster + level-lift mass (the raw ledger the guardrail demands)
   across ALL weights, not a truncated [L+1,L+5] window. Test: does
   `sum over ALL primitive orbits (any weight) of 2N*2^-w` bound (E-1)/r within
   some constant? (i.e. drop w_max entirely). Pre-register the constant BEFORE
   scanning q up to 2^20.
2. **Calibrate the true constant.** With the full-spectrum ledger, measure the
   worst ratio (E-1)/(r(1+W_full)) over q up to 2^20 at L=1,2 and see whether it
   stabilizes (candidate a proved bound) or still grows (kills the ledger idea).
3. **Weight-3 accident density.** Characterize which primes carry a weight-3
   orbit with sparse higher-weight companions (the killer shape: w3=1, small
   w4..w6). These are the norm-divisibility primes q | Norm(zeta^a+/-zeta^b+/-zeta^c);
   a number-theoretic handle on their density vs W_cl growth is the crux.
4. **L=2 literal kill.** Reach q>4001 at L=2 by sharding the (q,q) A_total DP
   (project one key coordinate, sum over the other — same projective trick as
   the M1 census strategy C) to confirm the mechanism is level-uniform.
5. Keep the exact `(E-1)/r` upper-bound scan as the round-3 workhorse: it makes
   any candidate bound falsifiable over the entire prime range at negligible cost.

## Deliverables on disk (scratchpad, prefix c1r2_)
`c1r2_falsifiers.md` (pre-registration), `c1r2_census_modal.py`,
`c1r2_verify_kill.py`, `c1r2_window_probe.py`, `c1r2_ground.py`,
`c1r2_results.md`, `c1r2_findings.md`, `c1r2_report.md`.

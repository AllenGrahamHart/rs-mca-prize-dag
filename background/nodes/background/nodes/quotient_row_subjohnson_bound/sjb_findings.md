# sjb_findings — proof worker on quotient_row_subjohnson_bound (2026-07-13)

Worker: fresh-context proof worker. Repos read-only; all files here are sjb_-prefixed scratch.
Catch ledger continues from #123.

## TURN 1 — reading pass (dag node, qrl packet + audit, tail-collapse chain, supply law, Paper D calibration)

Read verbatim: dag.json node `quotient_row_subjohnson_bound`; qrl_packet_20260713
(statement/proof/catches/shard spec/qra_findings); petal_top_band_tail_collapse +
petal_full_touched_set_injection + petal_retained_zero_effective_degree
(statement+proof each); rate_half_band_closure statement + witness-hunt scripts
(rh_c3_fiber_mtm_v2.py — the moment-map fiber reduction); census gate +
intrinsic_scale_geometric_ledger + descent + ESP statements; Paper D v13
thm:johnson-list, thm:deep-mca, prop:list-calibration, rem:quotient-borne,
prob:band, thm:capf-planted.

## HEADLINE (to be machine-verified before final): THE MINTED CLAIM IS FALSE — REFUTED, NOT OPEN

Six-line constructive argument (the t=1 truncated-locator/moment-map family, i.e. the
board's OWN supply-law framework pointed at the quotient row):

For tau in F_q let W_tau(X) = X^{k'+1} - tau X^{k'} = X^{k'}(X - tau), received word =
its evaluation on the n'-point domain D = H^M. For a codeword c (deg < k'),
W_tau - c is MONIC of degree exactly k'+1, so it has AT MOST k'+1 roots; its exact
agreement support has size exactly a = k'+1 iff W_tau - c = L_S (the monic locator
of an (k'+1)-subset S of D), which happens iff c = W_tau - L_S with the X^{k'}
coefficient matching: e1(S) = sum of S = tau. Hence

    L_P(W_tau, k'+1)  =  #{ S subset of D : |S| = k'+1, e1(S) = tau }   ... EXACTLY,

a bijection (c <-> S), and every such support is APERIODIC for free: |S| = k'+1 is
ODD (k' = rho n' = 2^{s'-c} is even for k' >= 8) while every nontrivial stabilizer in
Z_{n'} (a cyclic 2-group) has even order dividing |S|. Summing over the q values of
tau: sum_tau L_P(W_tau, k'+1) = C(n', k'+1). PIGEONHOLE:

    max_tau L_P(W_tau, k'+1)  >=  ceil( C(n', k'+1) / q ).

The minted cap is min((63/128) n'^6, (q-3n')/2). So the claim is FALSE at every
(row, scale, q) with C(n',k'+1)/q above the cap. Exact instances (verified below):

- (s=13, rho=1/2, M=128, n'=64, a=33): every admissible prime q in [2^26, ~1.88e9]
  violates the (q-3n')/2 branch: C(64,33)/q ~ 2.6e10 >> (q-3n')/2 ~ 3.4e7 at q~2^26.
  n'=64 IS the first open quotient size.
- (s=13, rho=1/2, M=64, n'=128, a=65): C(128,65) ~ 2^124.4; at q ~ 2^26 the floor
  ~2^98 exceeds BOTH branches (n'^6 cap = 2^41.98) by >= 2^56.
- rho=1/4: (s=13, n'=128, a=33); rho=1/8: (s=13, n'=128, a=17) via branch 2;
  rho=1/16: (s=13, n'=256, a=17). ALL FOUR RATES have refuted P1-OWN instances.
- At ALL prize fields (q < 2^256): FALSE for every scale with C(n',k'+1) >
  q(63/128)n'^6 — rho=1/2: all n' >= 512; per-rate thresholds computed below.

Also refuted: the node's "conjectural true size O(n'^2)" (the pigeonhole floor is
exponential in the fiber-rich regime); and catch #115's strength pin is
UNSATISFIABLE-BY-TRUTH at minimal fields (the true max exceeds (q-3n')/2 whenever
log2 q < ~(n'H(rho)+1)/2 — no provable lemma can feed ESP there, strengthening #109
from "the minted bound doesn't transport" to "the truth doesn't transport").

## Upstream calibration (Paper D agrees — the board's red overshot Paper D's own left edge)

- prop:list-calibration (v13 line 4707): "No uniform subexponential L_Q exists in the
  band; only the aperiodic term CAN be uniformly polynomial" — Paper D's aperiodic-
  polynomial hope is a CONJECTURE, and its band prob:band (line 4624) starts at
  a > k + 2n/N — STRICTLY ABOVE a = k+1. The strip (k, k+2n/N] was deliberately
  excluded; the board's minted red claims polynomiality INSIDE the excluded strip.
- My family shows the aperiodic count is exponential precisely in the strip
  a - k' < ~ n'H(rho)/log2(q), which sits BELOW Paper D's left edge 2n'/N' at razor
  fields — no contradiction with Paper D anywhere; instead it vindicates their left
  edge and kills the board's a = k'+1 claim.
- The witness words X^{k'}(X - tau) are exactly the t=1 "graded locator prefix" /
  truncated-locator moment-map words of the banked supply law (rh_c3: word =
  X^k L_{T0}); the count is the t=1 e1-fiber. The witness hunt's cells were
  FIBER-STARVED (q^t > C(n,k+t)); the quotient rows at their minimal fields are
  FIBER-RICH (C(n',k'+1) >> q) — the same law, opposite regime, and the Poisson
  "background" term IS the exponential mass.

## Machine verification plan (all ramguard tiny; no risky computation)

1. sjb_falsify_exact.py — exact integer instance table + q-windows + prize-field
   thresholds + doubling monotonicity + sub-Johnson/band membership per instance.
2. sjb_semantics_tiny.py — EXHAUSTIVE semantics validation at (n'=8, k'=4, q=17):
   the bijection L_P(W_tau, 5) = e1-fiber(tau) for ALL tau by enumerating ALL 17^4
   codewords; the averaging identity; the mass identity sum_c C(A_c,k') = C(n',k');
   aperiodicity-for-free.
3. sjb_n64_fiber_demo.py — EXACT complete e1-fiber distribution at the QRL-MODAL-1
   grid cell (n'=64, k'=32, q=65537, n=256, M=4): int64 DP (34 x 65537 states),
   total == C(64,33) exact; expected every fiber ~ C(64,33)/q ~ 2.71e13 vs minted
   cap min(3.38e10, 32672) and vs QRL-MODAL-1's pre-registered "max <= 2n' = 128";
   explicit witness (word, codeword, support) verified in vivo; DP cross-validated
   against brute force at (n'=16, q=257).

## TURN 2 — machine verification COMPLETE (all three scripts ALL PASS, ramguard tiny)

1. sjb_falsify_exact.py: ALL CHECKS PASS. Highlights (exact integers):
   - (1/2, s=13, n'=64, q0=67239937): floor 26,429,085,977 > cap 33,619,872 (~786x).
     REFUTED at the FIRST OPEN SIZE, minimal admissible field. Also s=14 (~49x), s=15 (~3.1x).
   - (1/2, s=13, n'=128): floor ~2^98 vs cap 3.36e7 — margin 2^73; n'^6 branch alone
     fails for every q in [2^26, ~2^83]. (1/2, s=13, n'=4096): margin 2^4038.
   - All four rates refuted at P1-OWN: 1/4 (13,128) 2^50; 1/8 (13,128) 2^18; 1/16 (13,256) 2^35.
   - Prize-wide (q < 2^256): word-uniform n'^6 impossible from n' = 512 (rho 1/2, 1/4)
     resp. 1024 (rho 1/8, 1/16); doubling persistence verified.
   - ESP capacity < truth at minimal fields (catch #125 exhibits, all rates).
   - Honest boundary: (1/2, n'=64, s>=16) NOT refuted by pigeonhole — the
     fiber-starved remnant survives as an open (smaller) statement.
2. sjb_semantics_tiny.py: ALL CHECKS PASS — exhaustive bijection/aperiodicity/
   averaging/mass-identity validation at (8,4,17) over all 83,521 codewords x 17 tau.
3. sjb_n64_fiber_demo.py: ALL CHECKS PASS — exact complete e1-fiber census at the
   QRL-MODAL-1 grid cell (n'=64, k'=32, q=65537): total == C(64,33) exact;
   min fiber 27,111,731,756,096, max 27,116,735,434,620 (concentration 0.02%);
   EVERY word of the family beats the n'^6 cap ~802x, the (q-3n')/2 cap ~8.3e8x,
   and QRL-MODAL-1's pre-registered "<= 2n' = 128" by ~2.1e11x; explicit
   (word, codeword, support) triple verified in vivo; DP cross-validated vs brute
   force at (16, 257).

## VERDICT: REFUTED — packet banked

- sjb_refutation_statement.md (the refuted claim, the refutation theorem, the
  instance table, prize-wide corollary, in-vivo exhibit, what survives)
- sjb_refutation_proof.md (six-line proof; why every audited step was true yet
  the target false; Paper D calibration — prob:band's left edge k + 2n/N excludes
  the strip the red claimed; catches #124-#127; SUCCESSOR-A chart-carrying
  descent + SUCCESSOR-B fiber-starved remnant; Q1/Q2 answered)

Catches minted: #124 (refutation), #125 (ESP dead-by-truth, strengthens #109/#115),
#126 (QRL-MODAL-1 falsifier structurally blind; O(n'^2) conjecture false),
#127 (red overshot Paper D's prob:band left edge; aperiodicity restriction void at
the odd consumed cell).

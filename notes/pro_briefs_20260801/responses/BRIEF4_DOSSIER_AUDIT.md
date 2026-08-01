# Fable audit of the Brief-4 Pro dossier — 2026-08-01

**Verdict: SOUND, with two corrections OF OUR OWN BRIEF accepted.**
Planning document; no DAG status changes. Every load-bearing constant
replayed exactly on our side (script PASS under ramguard; independent hand
checks of the packing caps R_2=6,327 / R_1=128 / R_1=224, the GV ball
formula, the Sidon greedy count 2m^3+m^2, the paid fraction
6328/8192 = 791/1024, and the distinct-support lemma). Import audit: Pro
read our tree at `026d8be7` faithfully — including the w10-X2
correction-of-record (17,17,15, not the stale 16,16,15) and all ten
spot-checked Appendix-A nodes.

## The two corrections to Brief 4 (accepted)

1. **"May be a known design-theory lemma" — REFUTED.** Brief 4's sharpest
   question implied the missing aggregation might be support-only
   combinatorics. The Sidon fence (dossier §6) proves support-only
   families satisfying every P-B set condition can exceed the budget by
   >270 bits with all difference multiplicities equal to one. The missing
   theorem is necessarily RS-specific. This is the same class of
   correction Codex made to the square-mass node (wave 30): the fence
   redirects the campaign before it is mis-launched.
2. **"Multiplicity <= 2 might suffice" — REFUTED on RowC 1/4.** Exact
   arithmetic: the banked bands consume 791/1024 > 1/2 of the producer
   baseline, and a multiplicity-two owner delivers only 1/2. Live
   options: multiplicity-one owner, near-K sharpening below 4,096, or the
   rank-five fallback for that row.

## What I checked and how

- Ran Pro's replay script under `ramguard tiny`: PASS (all asserts).
- Recomputed by hand: R_2(RowC 1/4) = floor(C(516,2)/C(7,2)) = 6,327;
  R_1(RowC 1/8) = floor(770/6) = 128; R_1(RowC 1/16) = floor(898/4) = 224;
  paid fraction (6327+1)/8192 = 791/1024.
- Distinct-support lemma: equal supports at slopes z != w give
  c_1 = (p_z-p_w)/(z-w) of degree < K with v = c_1 on an A-set — a joint
  explanation, contradicting global genericity. Sound.
- Sidon greedy: in Z^N (torsion-free), each of x-b_i = b_j-b_k,
  b_i-x = b_j-b_k, 2x = b_i+b_j forbids at most one x per index tuple:
  <= 2m^3 + m^2 total. Sound; the extraction preserves the intersection
  cap (subfamily). Consequence verified: abstract families kill any
  universal Boolean energy producer — RS realization is load-bearing.
- Naive-recursion loss (§10): at M ~ 8N^3, per-fibre cubic bounds give
  E_mid <~ 512 N^9 vs baseline ~512 N^7 — the claimed N^2 gap. Sound.
- Selector-transport caveat (§9): correct — our puncture compiler
  produces genuine exact-A' witnesses but NOT necessarily the child's
  first-match selection; "apply P-B verbatim to children" is invalid
  without a transport lemma. Option S2 (decorated closure class) is the
  right repair and matches how our compiler is actually stated.

## Points of caution (not defects)

- The producer target `D_* <= N^2(M-1)` is a CONJECTURE. Nothing banked
  implies it; the dossier is explicit about this. The producer pilot
  (PP4.2) is genuinely the first falsification gate, and it may kill the
  owner form. The weighted (13.2) and rectangle (13.3) fallbacks keep the
  route alive if it does.
- The "producer compatibility ceilings" (mu table) are ceilings BEFORE
  any middle-width debit; they are not campaign targets.
- Pro's node-grammar proposal (§18) is sensible but node minting stays
  with us; names/edges will follow our conventions when Phase 0 starts.
- The dossier's Track-B import "L <= 256/299/480" (Maxwell core block
  bounds by row) was not re-derived here; it is used only for the
  finiteness caveat ("480 blocks is not a practical census"), which is
  conservative in the safe direction.

## Adopted posture

CONDITIONAL GO, exactly as proposed:

1. **PP4.0 semantic freeze** — cheap, immediate, ours to write.
2. **PP4.1 RecPB definition + puncture-closure theorem** (Option S2).
3. **PP4.2 producer pilot** — exhaustive small-row enumeration with
   support-only negative controls and multiple selector orders. THE
   decision gate: kills or calibrates the producer before any fleet work.
4. **PP4.3 exact six-row budget checker** — built before any middle-band
   theorem, so over-budget proposals are rejected mechanically.

NO fleet campaign, NO middle-width census, NO recursive application of
P-B to puncture children until gates G0-G1 pass. Track B (RowC rank-five
atlas) may proceed independently as finite algebra when worker capacity
allows — it is m2-shaped already.

## Watch items

- Whether the producer survives PP4.2 — either outcome redirects the lane
  sharply (a counterexample would be the most informative single artifact
  this program could produce).
- RowC 1/4 is the constant bottleneck everywhere; decisions should be
  taken there first.
- Reusable spillover: the high-rank dual-trade circuit theorem (Track B's
  missing boundedness input) is also Brief 3 material.

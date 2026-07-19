# C1'-r3 F-ROUND 1 — findings (catches c1r3-C1 .. c1r3-C9)

## c1r3-C1 — VERDICT MIXED (the headline)
C1'-r3 survived both refuting kill lines on the complete in-gate analogue census
(33 rows, 5 octaves, all exact): no literal kill (worst K'_r3 = 1.0245 vs
allowance 4) and no trend kill (LS crossing at log2 q = 32.74 > 32, saturating).
The pre-registered amber watch K'>=1 tripped at q=81788929 (1.008154437 exact)
and q=246415361 (1.024517293 exact) => MIXED, blocking any amber promotion this
round. No convention was weakened mid-round.

## c1r3-C2 — BOTH repair levers independently neutralize every r2 killer
(1) Gate: v_2(q-1) = 7/7/6 at 63361/65921/204353, all below the analogue gate 20
(mirroring the official theorems: weight-3 max depth 18 < 41, weight-4 max 29 <
41). (2) Extended ledger, gate ignored: the w7/w8 orbit populations at the
killers (131+510, 119+470, 45+128) reprice K' from 6.199/4.481/4.285 down to
1.768/1.309/2.071 — all under the allowance. The r2 refutation is doubly out of
scope under r3; ungated rows remain refuted forever (r3 resurrects nothing).

## c1r3-C3 — the gate-mirror is THEOREM-GRADE at analogue scale
Exact CRT-certified census of all 19,840 order-64 reduced signed weight-3 norms:
24 unique norms, 22 distinct prime divisors, max v_2(p-1) = 16. So NO gated prime
of any size carries a weight-3 relation — the exact analogue of
`dli_wcl_weight3_ambient_exclusion`, by the same method (split-prime CRT + root
bound). All three r2 killers appear among the divisors (consistency). CAVEAT
(honest): the deepest analogue accident prime is 65537 = F_4 at v_2 = 16 — only
4 dyadic levels below the gate, vs official margins 23 (w3) and 12 (w4). The
analogue mirror holds but with a thinner margin than the official one; the gate
value 20 is doing real, not comfortable, work at this scale.

## c1r3-C4 — the in-gate accident spectrum below 2^32 is almost empty
Direct vanisher scan at ALL 401 gated Proth primes q < 2^32: weight-3, weight-4,
weight-5 channels EMPTY everywhere; weight-6 nonempty at exactly ONE row,
q=918552577 (v_2=22, 32 signed w6 vanishers). That row is beyond the exact-DP
envelope (q > 2^28) and is DEFERRED — the single known accident row in the r3
analogue hypothesis below 2^32, and round 2's priority target.

## c1r3-C5 — the gated bulk converges to the IID BASELINE; the amber line
## measures iid noise, not accident pressure
Under iid fibers E-1 = (q-1)/2^N, i.e. (E-1)/r -> 1. The per-octave worst
envelope (0.3075 -> 0.4487 -> 0.5919 -> 1.0082 -> 1.0245) saturates at exactly
this line: step slope collapses from +0.61 to +0.015 bits/octave and the worst
excess over iid across all 33 rows is +2.45%. Both amber rows have EMPTY
extended ledgers — they are iid-scale fluctuations at near-balance (r -> 1), not
accident rows. Consequence: the K'>=1 watch line (calibrated in r2's accident
context) sits ON the bulk asymptote and will trip forever as q -> 2^N regardless
of accident structure. Round 2 should re-arm amber at K'>=2 (pre-registered
BEFORE new scanning); the literal 4 = 4x iid headroom is untouched. NOT applied
this round (frozen falsifiers govern; hence MIXED).

## c1r3-C6 — the extended window does real quantitative work in-gate
9 of 33 gated rows carry w7/w8 orbits (7340033, 13631489, 26214401, 28311553,
70254593, 141557761, 147849217, 163577857, 186646529; w2..6 are empty at ALL 33,
matching C4).
Under the r2 window [2,6] those rows would have had EMPTY ledgers, and FOUR of
them would have been ambers on bare envelope (7340033 at 1.230, 26214401 at
1.036, 147849217 at 1.222, 186646529 at 1.123). The [2,8] ledger reprices all
four below 1 (0.308, 0.592, 0.978, 0.749): without lever (a) this round would
have recorded SIX ambers instead of two — and the two survivors are pure-bulk
rows no finite window can touch. The window lever is load-bearing exactly on the
accident-adjacent rows, as designed.

## c1r3-C7 — near-balance is the only tension regime (aspect probe)
At N=64 (r = q/2^64 ~ 10^-12) the same gated primes give (E-1)/r = 0.0099 and
0.0058 with K'_r3 bounds <= 0.00141 / 0.00064 — margins > 700x. All observed
growth of the envelope lives in r -> 1. Official L=1 rows CAN sit near balance
(q close to the 2^256 pin with N_1 = 256), so the near-balance saturation
question is officially relevant, and the decisive analogue data is q in
[2^30, 2^32) — round 2's segmented-DP target. Also: at N=64 the gated rows DO
carry w5/w6 orbits (one w5 + one w6 at 7340033; four w6 at 13631489) — accident
weights shift with aspect; the window's level-scaling (L+1..L+7) is doing the
right relative work.

## c1r3-C8 — machinery facts
(a) Optimized numpy subset-sum primitivity enumerator == verbatim banked kernel
on every cross-validated count (w2..6 at 4 rows; w7 vs the banked probe 131/119/
45), and is ~50x faster at w=7/8. (b) The memory-lean single-axis DP handles
q <= 2.6e8 in a single 270s shard (peak 5.7GB); PAIRS of such rows time out (two
shards shrunk to singles and rerun — no data gap). (c) The mod-p CRT DP (3
primes < 2^60) makes N=64 exact A_total (< 4^64) feasible with int64 arrays +
exact CRT reconstruction; mass invariant checked mod each prime. (d) hi/lo
32-bit split gives an exact 4^N mass invariant without object-dtype sums.

## c1r3-C9 — pose-level accounting is unchanged downstream
With WCL-ZONE-ext <= 1/32, E_L <= 1 + 4(33/32) = 41/8 exactly as before;
41^34 = 6833624772958324635768660320234188206281715423144834961 <
2^202 = 6427752177035961102167848369364650410088811975131171341205504
(19.84 bits slack); the assembly tolerates allowance up to 6 ((32+33*6)^34 <
32^34*2^100 true; allowance 7 false). Cost: six new emptiness slots at ell in
{1,2,4}; ell >= 8 extended windows are Newton-empty (L+7 <= 2L for L >= 7).

## Integrity notes
- Falsifiers frozen before any round computation; the only pre-round computation
  was the mandate-sanctioned pose arithmetic (41^34, killer v_2, Newton bound).
- Exact-rational verdict path everywhere; the two ambers are exact integer-ratio
  facts (numerator > denominator asserted).
- The in-gate family below 2^28 is a COMPLETE census (33/33 rows evaluated,
  including all five pre-named adversarial high-v_2 rows; deepest v_2 = 25 at
  167772161 survives at 0.883).
- M3 degraded to M2 exactly as pre-registered (no gated row has (E-1)/r > 4 —
  itself evidence that the gate removes the accident envelope the r2 kill rode).

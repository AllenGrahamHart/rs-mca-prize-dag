# C1'-r3 F-ROUND 1 — pre-registered falsifiers

- **predicate:** C1'-r3 as frozen in `c1r3_pose.md` (same directory). Gate H3
  analogue instantiation v_2(q-1) >= 20; window [L+1, L+7]; allowance 4; RAW
  ledger; exact-rational verdict path.
- **written BEFORE any round computation** (house law #1). The only computation
  performed so far is the pose-instantiation arithmetic sanctioned by the mandate
  (41^34 vs 2^202; v_2 of the three r2 killers; Newton emptiness inequality),
  recorded in `c1r3_pose_arith.py`. No family enumeration, no DP, no orbit
  enumeration, no census has been run. Timestamp 2026-07-19.
- **machinery of record (reused):** `c1r2_census_modal.py` conventions (A_total
  DP `E = q^L*A_total/4^N`, verbatim m2 primitive-orbit enumerator + orbit_key,
  structural bound K' <= (E-1)/r), c1r2_verify_kill.py banked kernels for any
  kill verification. New for r3: an optimized (numpy subset-sum) primitivity path
  for w=7,8 — it MUST be cross-validated against the verbatim kernel (below)
  before its output counts.

## Exact quantities

All of `c1r2_falsifiers.md` section "Exact quantities" carries over verbatim,
with the single change `w_max(L) = L+7`:

```text
K'_r3 := (E-1) / ( r * (1 + W_ext) ),   W_ext = RAW primitive signed-shift orbit
                                        ledger, weights L+1..L+7, mass 2N*2^-w
LITERAL kill:  K'_r3 > 4    (equivalently E-1 > 4 r (1+W_ext))
AMBER watch:   K'_r3 >= 1
Structural bounds (both exact, both pre-registered):
  (i)  K'_r3 <= (E-1)/r                       (W_ext >= 0)
  (ii) K'_r3 <= (E-1)/(r*(1+W_partial))       for ANY partial sub-ledger
       W_partial <= W_ext (e.g. weights L+1..L+5 only). Partial-ledger ratios
       are therefore valid for SURVIVAL verdicts only; a kill verdict requires
       the full [L+1, L+7] ledger. A partial-ledger ratio > 4 is NOT a kill.
```

## The r3-admissible analogue family (intensional definition; enumerated in-round)

- **Primary (full-spectrum slice, exact K'_r3 verdicts):** L=1, N=32, n'=64;
  q prime, q = c*2^k + 1 with odd c and k >= 20 (hence v_2(q-1) = k >= 20 and
  q = 1 mod 64), q < 2^28 (exact-DP envelope on the 16GiB Modal worker),
  q <= 2^32 (H2). ALL such primes are scanned — this is a complete census of the
  in-gate family below 2^28, not a sample.
- **Scales:** rows are binned by octave [2^j, 2^{j+1}). The family spans
  q ~ 2^22.8 (7*2^20+1, if prime) up to ~2^27.3 (5*2^25+1, if prime) — at least
  3 populated octaves expected; NONEMPTINESS of >= 3 octaves is asserted (#137);
  if fewer are populated the round is DEFERRED as underpowered, not scored.
- **Adversarial high-v_2 rows** (deep-split Proth rows, the honest analogue of
  official admissibility; membership subject to in-round primality): candidates
  named in advance: 7*2^20+1 = 7340033, 13*2^20+1 = 13631489, 11*2^21+1 =
  23068673, 25*2^22+1 = 104857601, 5*2^25+1 = 167772161. Any that are prime and
  < 2^28 MUST be in the scan (they are in the family by definition).
- **Accident scan (no DP, no K' verdict):** ALL Proth primes q = c*2^k+1, k >= 20,
  q < 2^32 — direct exact enumeration of weight-3/4/5 (and weight-6 if it fits a
  shard) signed vanishers mod q. Purpose: the GATE-MIRROR control and locating
  kill candidates beyond the DP envelope.
- **Aspect probe:** N=64, n'=128, L=1 on the two smallest in-gate primes
  (gate rows are automatically 1 mod 128 since k >= 20 >= 7). Exact (E-1)/r plus
  partial ledger w <= 6 (full [2,8] ledger is not enumerable at N=64:
  C(64,8)*2^7 is out of budget). Survival-only instrument per bound (ii).
- **L=2 in-gate at N=32 is EMPTY** (gate q > 2^20 vs H2 q <= 2^16) — recorded as
  a scope fact, not scanned.

## KILL LINES (verdict governed by these; frozen)

- **KILL-LITERAL (refutes C1'-r3):** any exact in-hypothesis row (H1 + H2 + H3
  analogue gate) with `K'_r3 > 4` on the FULL extended ledger. => verdict KILLED;
  bank the witness (q, N, L, A_total, exact E-1, r, per-weight primitive orbit
  counts w = L+1..L+7, W_ext, exact K'_r3) + independent verification via the
  banked c1r2_verify_kill.py kernels extended to w <= 8.
- **KILL-AMBER (blocks any amber promotion; does not logically refute):** any
  exact in-hypothesis row with `K'_r3 >= 1`. => verdict MIXED.
- **KILL-TREND:** the per-octave worst K'_r3 over the full-spectrum slice is
  monotone increasing across >= 3 populated octaves AND its log2-linear
  extrapolation in log2(q) crosses 4 before q = 2^32 (the L=1 in-hypothesis
  ceiling). => KILLED-TREND. Amber variant: crosses 1 before 2^32 => MIXED.
  (The r2 analogue: the envelope (E-1)/r grew ~477 by q~2^16 ungated; the gate
  bets that in-gate rows do not reproduce that growth.)
- **KILL-GATE-MIRROR (integrity of lever (b)):** the analogue weight-3 norm
  census (order 64: all 19,840 reduced signed weight-3 polys, exact CRT-certified
  norms Res(X^32+1,P), full factorization) exhibits a prime divisor p with
  v_2(p-1) >= 20 — i.e. the analogue gate does NOT close the weight-3 channel
  the way v_2 >= 41 provably does officially (depths 18/29 < 41). Consequences,
  pre-registered: (a) it is a FINDING (mirror broken) whatever else happens;
  (b) every such p < 2^32 is an in-hypothesis accident row and MUST be added to
  the accident scan, and to the full-spectrum slice if p < 2^28; (c) if any of
  them then trips KILL-LITERAL, the verdict is KILLED with the same standard as
  any other row. The same applies to any gated prime the direct vanisher scan
  finds carrying a weight-3 or weight-4 relation.
- **Integrity failures (DEFER, not kill):** incomplete signed-shift orbits,
  optimized-vs-verbatim enumerator mismatch, DP mass-invariant failure, CRT
  modulus not exceeding 2*3^32 (weight-3 census), Modal timeout on a required
  shard (shrink + DEFER per compute law), family nonemptiness assert failure.

## NOT-KILLS (explicitly)

- Any row FAILING the gate (v_2(q-1) < 20) violating the inequality — that is
  r2's refuted regime, out of r3 hypothesis by design (PC2 documents the three
  known ones). No amount of ungated failure scores against r3.
- Large W_ext at an in-gate row (it only helps the RHS).
- Bulk in-gate rows with K'_r3 -> 0 (expected DLI cancellation).
- A partial-ledger ratio > 4 (aspect probe or any truncated ledger) — survival
  instrument only, per structural bound (ii). It triggers a full-ledger follow-up
  where enumerable, else DEFER.
- Weight-5/6 accidents EXISTING at gated rows (the gate does not claim to close
  them; only their PRICED ratio matters).
- Float excursions (verdict path is exact rational; floats are display).
- The (E-1)/r envelope growing at UNGATED rows (known, r2 forensics).

## POSITIVE CONTROLS (must all pass BEFORE any verdict is read)

- **PC1 (machinery / r2 kill reproduction):** with the r2 window [2,6] and the
  gate ignored, the three r2 killers must reproduce EXACTLY:
  q=63361: K' = 6.199084..., E-1 = 2029645184561543/288230376151711744, W_cl=76,
  orbits {2:0,3:1,4:3,5:10,6:36};
  q=65921: K' = 4.481241..., E-1 = 723593725193615/144115188075855872, W_cl=72;
  q=204353: K' = 4.284843..., E-1 = 1498428331827445/144115188075855872, W_cl=50;
  plus the M2 anchor q=7937: K' = 0.246909432..., W_cl=236,
  E-1 = 15584479363607/144115188075855872, orbits {2:0,3:2,4:8,5:31,6:126}.
- **PC2 (gate exclusion of the killers):** v_2(q-1) = 7, 7, 6 for q = 63361,
  65921, 204353 — all < 20: each killer violates H3 => OUT of r3 hypothesis.
  Assert all three.
- **PC3 (repricing of the killers under the r3 ledger, gate ignored):** exact
  K'_ext on window [2,8] at the three killers. Consistency gates: the w=7
  primitive orbit counts must reproduce the banked window-probe values
  131 / 119 / 45, and K'_ext must be <= the banked w<=7 values 3.3497 / 2.4689 /
  2.9732 (window monotonicity). Expected < 4 at all three (repricing); recorded
  either way — PC3 is a measurement control, its numeric outcome is not a kill
  line (these rows are out of hypothesis; see NOT-KILLS).
- **Enumerator cross-validation:** the new numpy w=7/8 primitivity path must
  agree with the VERBATIM banked kernel on all per-weight counts w in [2,6] at
  q in {7937, 63361, 65921, 204353} and on w=7 counts vs the window probe (131/
  119/45). Any mismatch = integrity failure => DEFER.

## MUTATIONS (required to trip — detector liveness)

- **M1 (must fire):** q=63361 evaluated with the gate DROPPED and window forced
  to r2's [2,6] must yield K' > 4 and fire the literal-kill detector on the r3
  code path (identical numbers to PC1). Proves the detector still fires on a
  true positive after the r3 changes.
- **M2 (must fire):** allowance lowered to 10^-6: every scanned in-gate row with
  E-1 > 0 must then fire the detector (detector live on the GATED path too).
  Assert E-1 > 0 at every scanned row (it is a sum of squares with the lambda=0
  term removed; a zero would be an integrity failure).
- **M3 (must fire):** W_ext := 0 at the in-gate row with the largest (E-1)/r:
  IF that row has (E-1)/r > 4 the detector must fire (ledger load-bearing on the
  gated path); if NO in-gate row has (E-1)/r > 4, record that fact — it means
  r3 survives at this scale even with an EMPTY ledger, and M3 degrades to M2
  (noted, not a failure).

## NONEMPTINESS ASSERTS (#137)

(1) in-gate family below 2^28 nonempty and listed; (2) >= 3 populated octaves;
(3) at least one row with v_2(q-1) >= 21 (strictly above the floor 20) in the
scan; (4) PC1/PC2/PC3 rows all evaluated; (5) accident scan covers every gated
prime < 2^32 (count printed and > the count below 2^28); (6) the weight-3 census
CRT modulus exceeds 2*3^32 (exactness) and covers all 19,840 polys.

## SCOPE (honest, up front)

Exact K'_r3 verdicts: L=1, N=32, in-gate primes q < 2^28 (complete). Accident
channels only (no K'): gated primes in [2^28, 2^32). Aspect: N=64 partial-ledger
probe, survival-only. NOT reachable this round: L=2 in-gate (empty at N=32,
grid-infeasible at N=64 — the projective/sharded DP is round-2 work), official
aspect N=256L (as always). SURVIVED means: no kill line tripped within this
scope; it does NOT prove C1'-r3, WCL-ZONE-ext, B-WEAK, or the DLI node, and by
itself justifies no DAG surgery and no amber flip.

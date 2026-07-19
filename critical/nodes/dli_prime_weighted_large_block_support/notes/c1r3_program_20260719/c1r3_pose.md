# C1'-r3 — official-scoped, extended-ledger re-pose of the REFUTED C1' (r2)

- **predicate node:** `dli_dyadic_k_core` (status REFUTED at r2; this is the round-3
  candidate successor, NOT a DAG edit — worker output for maintainer triage).
- **pose of record it repairs:** `critical/nodes/dli_prime_weighted_large_block_support/notes/C1PRIME_LEVEL_SCALED_POSE.md`
  (r2 restatement in the node statement, 2026-07-13). ALL conventions of that pose
  are kept verbatim (T, E, r, RAW primitive signed-shift orbit ledger per
  `dli_wcl_raw_ledger_interface_guardrail` and maintainer decision 4a, exact-rational
  verdict path, #137 normalization discipline) EXCEPT the two changes below.
- **kill record being repaired:** node statement REFUTED block + packet
  `critical/nodes/dli_prime_weighted_large_block_support/notes/c1r2_fround2_20260713/`
  (kills K' = 6.199084 / 4.481241 / 4.284843 at q = 63361 / 65921 / 204353;
  L=1, N=32, q ≡ 1 mod 64, RAW ledger, window w ∈ [L+1, L+5]).
- **design authority:** the two maintainer-approved repair levers — (b) official
  scoping, (a) extended ledger. Both are used. Pose written 2026-07-19, before the
  F-ROUND 1 falsifiers were armed and before any round computation.

## Candidate statement (C1'-r3)

Let `(q, n'=2N, L)` be a generated prime-field full-half-section row with

```text
(H1)  q prime,  q = 1 mod n',
(H2)  2^N >= q^L,  N >= 16L,
(H3)  OFFICIAL-ADMISSIBILITY GATE:  v_2(q-1) >= 41        [official ambient form]
      — at analogue validation scale (N=32, n'=64):  v_2(q-1) >= 20.
```

Put, exactly as in `C1PRIME_LEVEL_SCALED_POSE.md`,

```text
T(lambda) = prod_{y=0}^{N-1} cos^2(pi a_y(lambda)/q),
E   = 1 + sum_{lambda != 0} T(lambda),
r   = q^L / 2^N,
```

and define the EXTENDED RAW ledger (change (a); the only ledger change is the
window upper end L+5 -> L+7):

```text
w_max_r3(L) = L + 7,
W_ext(q,N,L) = sum_{primitive signed-shift orbit O, L+1 <= w(O) <= L+7} 2N * 2^{-w(O)}.
```

The candidate C1'-r3 inequality is

```text
E - 1 <= 4 r (1 + W_ext).                                (C1'-r3)
```

The allowance is 4 — UNCHANGED from r2 (not weakened; see budget section).

## The gate (H3): what it is and why it is legitimate

At the OFFICIAL rows the gate is **vacuous**: every official DLI production row has
ambient field prime `q = k*2^41 + 1` (the ambient split; see
`dli_wcl_weight5_first64_mitm_exclusion` "For q=k*2^41+1, the first 64 prime
rows...", and `dli_wcl_weight3_ambient_exclusion` "Such a relation would require an
ambient field prime with 2^41 | q-1"). So C1'-r3 restricted to official-admissible
rows still covers EVERY official row: the downstream assembly loses nothing.
The gate only shrinks the ANALOGUE validation domain — and it shrinks it exactly
away from the accident channel that killed r2:

- **Every r2 killer sits at minimal dyadic depth.** v_2(q-1) = 7, 7, 6 at
  q = 63361, 65921, 204353 (bare minimum for q = 1 mod 64 is 6). Verified as
  positive control PC2 in the round.
- **Every r2 killer is a weight-3 accident row.** Kill table orbit profiles
  {2:0, 3:1, 4:3, 5:10, 6:36} / {0,1,3,9,34} / {0,1,3,6,18} — each killer's engine
  is a LONE weight-3 primitive orbit (w3 = 1) whose multiplier-shadow/cluster mass
  pumps (E-1)/r to 477 / 327 / 219 while the window ledger stays 76 / 72 / 50
  (catch c1r2-C4).
- **That channel is PROVABLY EMPTY at official-admissible primes.** Master theorems
  (all PROVED, closure=computation):
  - `dli_wcl_weight3_ambient_exclusion`: among all C(256,3)*2^2 = 11,054,080 reduced
    signed weight-3 polynomials at order 512, no cyclotomic norm
    Res(X^256+1, P) has a prime divisor q < 2^256 with v_2(q-1) >= 41; the maximum
    depth is 18. No official row carries a terminal weight-3 relation.
  - `dli_wcl_weight4_ambient_exclusion`: same for weight 4 (1,398,341,120 polys,
    44,599 distinct prime factors, max depth 29 < 41).
  - `dli_wcl_ell2_weight3_ambient_exclusion` (order-1024 census, max depth 21 < 41)
    and `dli_wcl_ell2_weight4_newton_exclusion` (Newton identities): the ell=2
    siblings.
  - `dli_wcl_newton_short_window_exclusion`: no relation of weight w <= 2*ell at
    level ell — at ell >= 8 the whole (even extended) window is empty.

  A weight-3/4 accident prime q must divide one of those norms; official-admissible
  primes divide none of them below 2^256. So the specific mechanism that produced
  ALL THREE r2 kills (and both refutations before it — q=204353 is the node's own
  motivating k=7 cluster row) cannot occur at any official row. The r2 refutation
  lives in a region of parameter space that official rows provably never visit.

- **Analogue instantiation v_2(q-1) >= 20, justification.** The official gate 41 is
  unreachable at analogue scale (a q = 1 mod 2^41 prime is >= 2^41, far beyond the
  exact-DP envelope). The analogue proxy keeps the gate's structural role:
  (i) *deep-split character*: official 41 exceeds the terminal level's own root
  requirement v_2 >= 9 (n'=512) by 32 dyadic levels; analogue 20 exceeds the
  analogue requirement v_2 >= 6 (n'=64) by 14 — both are "field splits far deeper
  than the level needs", which is what starves the accident spectrum;
  (ii) *populated*: rows are engineered via Proth primes q = c*2^k + 1 with k >= 20,
  odd c — these exist in quantity at small scale (e.g. 7*2^20+1, 13*2^20+1,
  11*2^21+1, 25*2^22+1, 5*2^25+1), giving a nonempty in-gate family (#137
  nonemptiness asserted in-round);
  (iii) *mirror-verified, not assumed*: the round computes the ANALOGUE of the
  exclusion theorems — the full order-64 weight-3 norm census
  (C(32,3)*2^2 = 19,840 reduced signed polys, exact CRT-certified
  Res(X^32+1, P), max v_2 over prime divisors) AND a direct vanisher scan proving
  which gated primes q < 2^32 carry weight-3/4/5 relations. The pre-registered
  expectation is max weight-3/4 depth < 20 (official mirror: 18/29 < 41). If the
  mirror FAILS (an analogue accident prime with v_2 >= 20 exists), those rows are
  in-hypothesis kill candidates and MUST be scanned — the gate is falsifiable, not
  rigged.

## The extended ledger (change (a)): why L+7, and why the gate alone is not enough

The gate provably closes weights 3 and 4 (and, at ell=2, 3-4; at ell >= 8,
everything) at official rows — but weight-5..8 accidents are NOT all excluded
(open slots below). The r2 forensics (catch c1r2-C5) showed the w <= L+5 window
underprices even the in-window shadow: widening to w <= 7 demoted the r2 kills
only to K' = 2.5-3.4. The r3 window [L+1, L+7] adds two more dyadic weight
classes of pricing at every level, so residual accidents in the channels the gate
does NOT close are charged more of their true mass. L+7 is chosen because:
(i) it strictly contains every window probed in the kill packet;
(ii) it is finitely enumerable exactly (verdict path stays exact-rational);
(iii) at official aspect it stays Newton-finite: for every scheduled level
ell >= 8, L+7 <= 2L, so `dli_wcl_newton_short_window_exclusion` proves the whole
extended window EMPTY — the official obligation remains a finite slot list.
A full ledger (no w_max) was considered and rejected for this round: no proved
tail bound exists (trivial counts diverge), so it cannot sit in an exact
assembly. It remains the round-2 escalation if r3 survives (report section).

Honest note: at rows where W_ext > W_cl the r3 per-row inequality is WEAKER than
r2's — that is the design (the r2 window provably underpriced the ledger), not a
mid-round weakening. The r3 pose as stated here is FROZEN for F-ROUND 1: no
hypothesis, window, or allowance may move during the round. A kill is a finding.

## Why each r2 killer is out of scope AND repriced (both levers, both checks)

| q | v_2(q-1) | r3 gate (>=20) | K' (r2 window [2,6]) | K' (w<=7 probe) | r3 status |
|---|---|---|---|---|---|
| 63361 | 7 | FAILS -> out of hypothesis | 6.199084 | 3.3497 | excluded by H3; repriced under W_ext (exact value in-round, expected < 4 by the w<=7 probe + w=8 mass) |
| 65921 | 7 | FAILS -> out of hypothesis | 4.481241 | 2.4689 | same |
| 204353 | 6 | FAILS -> out of hypothesis | 4.284843 | 2.9732 | same |

Both facts are POSITIVE CONTROLS of the round (falsifiers doc): (PC1) the r2 kill
K' values must reproduce EXACTLY (exact fractions) under the r2 window — machinery
check; (PC2) all three rows must fail the gate — scoping check; (PC3) all three
rows must be repriced under the r3 extended ledger (exact K'_ext computed; the
w<=7 probe values above bound it from above by monotonicity of the window).
IMPORTANT honesty item: repricing ALONE does not save the predicate — the accident
envelope (E-1)/r grows with q (c1r2-C4/C5), so a fixed window without the gate
fails at larger q. The gate is the load-bearing lever; the window buys margin in
the channels the gate does not provably close.

## Downstream-assembly consequence (explicit arithmetic)

The assembly `dli_marginal_baseline100_coverage` (conditional.md, schedule r2,
34 levels ell_j = (2^32,...,2,1,1), field pin q < 2^256 giving r_j < 1) consumed
r2-C1' + WCL-ZONE (W <= 1/32). Under r3 it needs the EXTENDED zone bound

```text
WCL-ZONE-ext:  W_ext(R,L) <= 1/32  at every official production level.
```

Then, per level: E_L - 1 <= 4 r_L (1 + W_ext) <= 4 (1 + 1/32) = 33/8, so
**E_L <= 41/8 — the SAME bound as before** (the allowance did not move), and

```text
A(R) = prod_{j=0}^{33} E_j <= (41/8)^34 < 2^100
  <=>  41^34 < 2^202
  41^34 = 6833624772958324635768660320234188206281715423144834961
  2^202 = 6427752177035961102167848369364650410088811975131171341205504
  41^34 < 2^202: TRUE, slack = 19.8432 bits (exact integers above).
```

So the 2^100 aggregate closes with the identical ~20 bits of slack. (Headroom
note, computed exactly: the assembly tolerates allowance up to 6 —
(1+6*33/32)^34 < 2^100 holds, (1+7*33/32)^34 fails — so a modest future
recalibration has room; r3 does NOT spend it.)

**New obligation created by the extended window (honest cost):** WCL-ZONE-ext is
strictly stronger than the wired WCL-ZONE. At scheduled levels ell >= 8 it is
FREE (Newton-empty, above). At ell in {1 (x2), 2, 4} the per-orbit official
masses (2N_L * 2^-w, N_L = 256L) exceed 1/32 throughout the window, so the bound
is again EQUIVALENT to slot emptiness (same shape as finding wz-C1). Against the
current dag (PROVED: (1,3),(1,4) ambient censuses; ell=2 w<=4 Newton, w5 norm-gcd,
w6 recursive-norm; Newton w<=2ell everywhere) the open slot list becomes:

```text
existing open slots: (1,5), (1,6), (2,7), (4,9)          [dag TARGETs today]
NEW slots from L+7:  (1,7), (1,8), (2,8), (2,9), (4,10), (4,11)
```

Ten emptiness slots total (six new). This is the price of lever (a); the round-2
design in the report discusses trading window width against slot count if any new
slot resists.

## Honest DIFFERENCES from r2 (complete list)

1. **New hypothesis H3** (official-admissibility gate) — vacuous at official rows,
   restricts the analogue domain to v_2(q-1) >= 20 (Proth-engineered family).
2. **Window L+5 -> L+7** — per-row RHS weakly larger (never smaller ledger).
3. **Downstream zone obligation widened** — WCL-ZONE-ext over [L+1, L+7]; six new
   emptiness slots at ell in {1,2,4}; unchanged (free) at ell >= 8.
4. **Allowance 4, E_L <= 41/8, and the 41^34 < 2^202 arithmetic: UNCHANGED.**
5. **Validation domain shrinks**: the r2 analogue family (all q = 1 mod 64) had
   ~thousands of rows to 262144; the r3 in-gate family is the sparse Proth set.
   L=2 analogue at N=32 is EMPTY in-gate (gate needs q > 2^20, hypothesis H2 needs
   q <= 2^16) — the round therefore adds an N=64/L=1 aspect probe instead, and
   L=2 in-gate testing is honestly out of reach this round (report lists it).
6. **Status**: r3 is a fresh conjecture; it has survived ZERO adversarial rounds.
   The r2 refutation history stands untouched; r3 does not resurrect any r2 claim
   at ungated rows — those are refuted forever.

## What would prove/refute r3 (attack surface, carried forward)

Refute: one exact in-hypothesis row (official or analogue-gated) with
E-1 > 4r(1+W_ext) — the census + exact-E machinery computes both sides; OR a
gated-family trend whose extrapolation crosses the allowance inside hypothesis
range (falsifiers doc). Prove (official): WCL-ZONE-ext slot emptiness (10 slots)
+ a bound on gated-row residual mass — the number-theoretic crux is now the
weight-5..8 accident spectrum at q = k*2^41+1, where the norm-census machinery of
the weight-3/4 nodes is the natural tool (weight-5 already has the first-64-rows
MITM exclusion as finite evidence).

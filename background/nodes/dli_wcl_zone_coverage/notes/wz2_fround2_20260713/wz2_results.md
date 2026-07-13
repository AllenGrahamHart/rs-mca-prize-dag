# wz2_results.md — F-round 2 exact tables (WCL-ZONE-COVERAGE)

Pre-registration: `wz2_falsifiers.md` (written before any computation).
Dedup spec: `wz2_dedup_spec.md` (written first, per the round-2 mandate).
Enumerator: `wz2_census_modal.py`; evaluator: `wz2_eval.py`; raw shard
JSON `wz2_shard_*.json`; Modal stdout `wz2_log_*.txt`; aggregate
`wz2_eval_report.json`. All W_cl values exact fractions end to end;
floats only in Poisson design predictions (as pre-registered).

## Modal app ids (all exit 0)

| shard | app id | wall |
|---|---|---|
| replay (T1-T10, M-A..M-C) | ap-wSl9T7IWIfTirpjyRhXH1y | 25.5s |
| c1audit | ap-pm0Q3Xmwm2820HjzBjmHvx | 37s |
| xcheckl3 (V1) | ap-FRYAncSaTfxWC9lyM4r1LW | 30.4s |
| xcheck96 (V2 + k=3 identity) | ap-tiqxQldYp2xIUI86uZZ7mo | 2.0s |
| o96_l1 (incl. T7, M-D, M-E) | ap-2f557BtiorTmwUvclQjaUn | 7.1s |
| (o96_l1 first attempt, output > 40k stdout cap, discarded) | ap-4dvEAIixznuDzBb58rntoD | 9.2s |
| band_b15 (b14-deep + b15) | ap-pQgvzfWZ8Wwneqk9RLexH2 | 45.4s |
| band_b16 | ap-k5QaWCBGh2zgfBx6IJ2EOf | 34.7s |
| o96_l2a (b13) | ap-HkitBt4Eq7sPHGuvgmagcJ | 13.5s |
| o96_l2b (b14) | ap-skus3LVl0zAmO1plKxZi2G | 17.5s |
| o96_l2c (b15) | ap-EYMxYTIJXTGfQ3W1wpq1VU | 15.4s |
| o96_l3 (b13, exploratory) | ap-lP8oPF7tYLHb1Zbt6xYoZE | 13.5s |
| o192_l1 | ap-C5QRXr8DTA1hixkI555t5B | 22.2s |
| o192_l2a (b16) | ap-yaUN4wzXTQrhlj9nO9ZHBl | 108.5s |
| o192_l2b (b17) | ap-6dEHWTwndTLvOovlS2qj4i | 105.2s |

## Integrity gates (all green)

- Replay shard 12/12: T1a (q=7937 L=1: banked prim counts 0/2/8/31/126
  and W_cl=236 exact, direct==mitm), T1b (q=193 L=2: 0/0/4/24/176,
  W=120), T2a (A/b21 q=2107073: raw 4, round-1-convention dedup 1 with
  exactly 5 links), T2b (B/b14 q=21569: the single w=7 orbit with the
  recorded rep, W=1/2), T2c (C/b21 q=2100353: raw 44, round-1 shadow 34
  with exactly 10 links), T3 (synthetic (1+z)P links; base chosen with
  non-adjacent support so the product is genuinely ternary), T5 (owner
  set invariant under 3 input shuffles), T6 (idempotent), T8 (weight-<=3
  sweep links a subset of division links on all 167 sources of the 7937
  window).
- Mutation controls all tripped: M-A (primitivity off: w=6 126 -> 224 ==
  banked M1), M-B (ternarity gate emptied: T3 link lost), M-C (owner
  order reversed: owner set changes on A/b21), M-D (non-ring lift map:
  0 -> 1 misses at the first O96L1/b21 prime), M-E (tag against the
  wrong factor: F96 tag control breaks).
- Engine validation: V1 xcheckl3 — L=3 mitm == direct at q=193, N=32 on
  a NONEMPTY cell (64 w=7 + 160 w=8 hits; wz-C5 vacuity rule respected).
  V2 xcheck96 — N=96 direct == mitm at w<=4 on a nonempty cell
  (F192 found, 32 w=3 hits at q=33555073). k=3 lift identity verified on
  data: all 96 D_3 images of (193, N=32) w=3 vanishers vanish at
  (193, N=96) level 1.
- c1audit: all 8 banked rows reproduce raw counts + W_cl EXACTLY (mitm).
- Plants: forced orbit F = Phi_96 present in the RAW ledger of ALL 72
  O96L1 cells; F192 = Phi_192 present in ALL 36 O192L1 cells; zero
  missing-plant exceptions. Negative plants: F/F192 absent from every
  L=2 and L=3 ledger (as the 2-3-norm exclusion predicts).
- Forced sub-ledger q-independence: the Phi_{n'}-tagged primitive set is
  IDENTICAL across primes in every L=1 band (it is exactly {orbit(F)});
  semi_orbits = 0 at L=1 everywhere.
- Lift control: lift_miss_total = 0 across all shards (every admissible
  companion orbit's k-lift found in the target enumeration).
- Norm control C-7: every semi-forced witness verified — integer
  resultant Res(Phi_96, P) nonzero and divisible by q (exact, sympy).
- Degenerate-orbit flags: ALL degenerate orbits carry the Phi_{n'} tag
  (whitelisted class, counts in `deg_tagged`); zero anomalous flags
  (no closure misses, no untagged degenerates) in any shard.
- #137 band-stream guards: all bands nonzero candidate streams
  (smallest: o96_l3 with 19.5M join candidates across 12 primes).

## PART 0 — canonical dedup results (spec conformance + findings)

- Round-1-convention replays are EXACT (T2a/T2c above). The canonical
  module agrees with round-1 on A/b21 (W 4 -> 1) and C/b21 (44 -> 34;
  canonical counts 9 undirected links where round 1 logged 10 directed
  accepts — same components, convention noted).
- Composition order was NOT material on any replay/audit cell
  (`order_material` false everywhere it was computed) — but remains
  material in principle (RATIFY-8 stands).
- **Banked-number changes under the canonical spec (findings, NK-5):**

| row | W_raw (banked) | W_canon | K'_raw | K'_dedup | C1'(deduped) |
|---|---|---|---|---|---|
| L=1 q=3137 | 368 | 298 | 0.0000 | 0.0000 | holds |
| L=1 q=5569 | 191 | 159 | 0.0000 | 0.0000 | holds |
| **L=1 q=7937** | **236** | **8** | **0.2469** | **6.5019** | **FAILS (exact)** |
| L=1 q=12289 | 89 | 78 | 0.0000 | 0.0000 | holds |
| L=2 q=193 | 120 | 102 | 0.0012 | 0.0015 | holds |
| L=2 q=257 | 67 | 125/2 | 0.0018 | 0.0019 | holds |
| L=2 q=449 | 35/2 | 17 | 0.0034 | 0.0035 | holds |
| L=2 q=577 | 29/2 | 23/2 | 0.0344 | 0.0427 | holds |

  At q=7937 the canonical dedup (lift: 3 orbits owned by the admissible
  N=16 companion; shadow: 1240 links collapsing 164 surviving orbits to
  owners) leaves W_canon = 8, and the EXACT check gives
  `E - 1 > 4 r (1 + 8)`: **C1' with the deduped ledger is refuted at the
  banked accident row.** Pre-declared NK-5: a spec-level finding about
  the M3 interface, not a WCL-ZONE kill (see wz2-C1 in wz2_findings.md).

## PART 1 — family B (L=2, N=32, n'=64)

Kill sequence (b10/b12/b14 frozen round-1 K=24; b15/b16 new):

| band | n | nonempty | Phat | Ppred | rho |
|---|---|---|---|---|---|
| b10 (r1) | 24 | 12 | .500 | .310 | 1.615 |
| b12 (r1) | 24 | 5 | .208 | .087 | 2.395 |
| b14 (r1) | 24 | 1 | .042 | .009 | 4.648 |
| **b15** | 384 | 1 | .0026 | .00072 | **3.62** |
| **b16** | 384 | 0 | .0000 | .00028 | **0.00** |

- KILL-B: **no trip** (monotonicity broken at b15; 1 witness in
  b15+b16 vs >= 4 required; b16 has 0 vs >= 2 required).
- Turnover branch: rho(b15)=3.62 <= rho(b14)=4.648 AND
  rho(b16)=0 <= rho(b15). New bands Poisson-consistent: b15 observed 1
  vs 0.277 expected (P(>=1) ~ .24); b16 observed 0 vs 0.106 expected.
- b14-deep diagnostic (K=96, outside the kill sequence): 3/96 nonempty,
  rho 6.71 (P(>=3 | 0.447) ~ 1.1% — the b14 octave is genuinely the
  richest, but the enrichment does NOT persist upward).
- Witnesses (all single w=7 generic orbits, W=1/2): q=21569 (the
  round-1 witness, re-found exactly), 27457, 33409 (33409 appears in
  both b14-deep and b15 — deterministic band overlap, per-prime null
  unaffected). Mechanism diagnostic on witnesses: P(level-2 | level-1)
  per orbit ~ 1/207..1/415 vs 1/q ~ 1/21569..1/33409 — each witness is
  individually a ~1% orbit-level coincidence; aggregate excess over all
  five bands ~ 2x the null (O(1) correlation factor, consistent with the
  banked f2/f2b level-correlation studies), with NO growth in scale.

**PART 1 VERDICT: SURVIVED-WITH-EXPLANATION** (pre-registered branch:
turnover + Poisson-consistent new bands; the round-1 monotone trend was
a small-K artifact of the enriched-but-bounded b14 octave).

## PART 2 — odd-n' mixed channel

### O96L1 (N=48), O192L1 (N=96): forced channel, L=1

| family | band | nonempty | gen_nonempty/n | Ppred | rho_gen |
|---|---|---|---|---|---|
| o96_l1 | b21 | 24/24 | 23/24 | .876 | 1.094 |
| o96_l1 | b23 | 24/24 | 12/24 | .407 | 1.227 |
| o96_l1 | b25 | 24/24 | 5/24 | .123 | 1.698 |
| o192_l1 | b25 | 12/12 | 12/12 | .991 | 1.009 |
| o192_l1 | b27 | 12/12 | 9/12 | .696 | 1.078 |
| o192_l1 | b29 | 12/12 | 5/12 | .257 | 1.619 |

- Forced ledger = EXACTLY {orbit(F)} (mass 12) resp. {orbit(F192)}
  (mass 24) at every prime — the pre-hoc prediction that all other
  ternary Phi_{n'}-multiples in window are imprimitive held with zero
  exceptions across 108 cells.
- Lift ownership (spec E4 prediction, exact): F is lift-owned by the
  N=24 row at ALL b21/b23 cells and NOT owned at any b25 cell (N=24
  inadmissible there); F192 is lift-owned (via D_2 from N=48) at ALL
  36 O192L1 cells. The forced mass is charged once at its minimal
  admissible row, exactly the census principle.
- Generic population: no saturation anywhere (top bands: rho_gen 1.70
  and 1.62, both within Poisson wobble of their small expectations).

### O96L2 (b13/b14/b15), O192L2 (b16/b17), O96L3 (b13)

| family | band | n | nonempty | gen_ne | semi orbits | Ppred | rho_gen |
|---|---|---|---|---|---|---|---|
| o96_l2 | b13 | 24 | 12 | 11 | 3 | .349 | 1.314 |
| o96_l2 | b14 | 24 | 8 | 7 | 2 | .128 | 2.278 |
| o96_l2 | b15 | 24 | 3 | 1 | 3 | .039 | 1.073 |
| o192_l2 | b16 | 10 | 6 | 6 | 1 | .569 | 1.054 |
| o192_l2 | b17 | 10 | 3 | 3 | 0 | .200 | 1.497 |
| o96_l3 | b13 | 12 | 0 | 0 | 0 | .0006 | — |

- KILL-O1: **no trip.** No saturation; zero generic orbit keys recurring
  at even 2 distinct primes (the recurrence scan covers all odd-n'
  cells); no >= 5-prime recurrence.
- KILL-O2: **no trip.** Semi-forced rates .125 / .083 / .125 across
  b13/b14/b15 — not monotone increasing; roughly FLAT, which is the
  norm-divisor-statistics expectation for a FIXED candidate family
  (each candidate's norm has prime divisors at all scales at roughly
  constant density per octave; the pre-registered per-prime q^-1
  phrasing is about single-vector probability, not band totals — noted
  as wz2-C4).
- Semi-forced witnesses: ALL of them tag-{Phi_32}, ALL weight 6 (the
  even-weight prediction), all with exact resultant verification; ZERO
  tag-{Phi_96} witnesses at L>=2 (the 2-3-norm exclusion held exactly);
  no witness key recurs at 2 primes.
- O96L3 (exploratory): completely empty at all 12 primes — no
  unexpected L=3 channel.

**PART 2 VERDICT: SURVIVED** (forced + semi-forced structure exactly as
the pre-hoc algebra predicts, generic channel at the Poisson null,
no q-robust structure beyond the algebraically forced orbit).

## Kill-line outcomes (pre-registered section 4)

- KILL-B: no trip (turnover; explanation branch satisfied).
- KILL-O1: no trip (no saturation, no generic recurrence at >= 3).
- KILL-O2: no trip (semi-forced rate not increasing).
- KILL-3: no integrity failure; all required-to-trip controls tripped.

**ROUND VERDICT: SURVIVED** (both parts), with the PART 0 spec debt
discharged and one major spec-level finding (deduped-C1' exact failure
at q=7937 — wz2-C1).

# wz2_falsifiers.md — F-round 2 pre-registration against WCL-ZONE-COVERAGE

- **Date:** 2026-07-13, written BEFORE any round-2 computation (the only
  arithmetic below is design arithmetic: binomial sums, Poisson design
  targets, and exact hand algebra on fixed cyclotomic polynomials; no orbit
  enumeration has been run at pose time).
- **Target node:** `dli_wcl_zone_coverage` (status TARGET, F-rounds 1/1
  survived; round-1 packet
  `background/nodes/dli_wcl_zone_coverage/notes/wz_fround1_20260713/`).
- **Round-2 mandate:** PART 0 dedup canonical spec (#191/wz-C2, done first:
  `wz2_dedup_spec.md` in this scratchpad); PART 1 family-B trend
  (#193/wz-C4); PART 2 odd-n' mixed channel (#192/wz-C3).
- **Repos READ-ONLY.** All artifacts in this scratchpad, prefix `wz2_`.

## 0. Normalizations (pinned; #137 discipline)

All of round-1 `wz_falsifiers.md` section 0 is inherited VERBATIM (row
family, mass convention/N_L map, pinned embedding, vanisher/level
conditions, reduced orbits, primitivity, exactness). The round-2 enumerator
reuses the round-1 `wz_census_modal.py` definitions (`primitive_root`,
`row_powers`, `normalize`/`shift1`, `eval_levels`, `is_primitive`,
`orbit_partition`, `_side`/`_full_join`/`enumerate_mitm`,
`enumerate_direct`, `ledger_census`, `mult_matrix`/`inv_mod`) rather than
re-deriving them. Deltas, each pre-declared here:

1. **Dedup convention** = the canonical spec `wz2_dedup_spec.md`
   (lift-first then shadow, RATIFY defaults). Round-1-convention outputs
   (shadow-only, lift-only) are ALSO computed on replay cells for exact
   comparison; divergences are findings, never silent substitutions.
2. **L=3 mitm key**: level values packed as `((v1*q)+v2)*q+v3` with the
   guard `q^L < 2^62` (exact int64); validated direct-vs-mitm (V1 below).
3. **#137 guard redesign (pre-declared, needed at deep-sub-volume cells):**
   round 1 asserted per-cell candidate streams nonempty. At `L>=2` with
   `q^L` far above the mitm side product, ZERO join candidates is the
   correct outcome for an empty cell, so the per-cell assert would
   false-trip. Round 2 asserts: (i) both mitm sides nonempty per cell;
   (ii) per-BAND total candidate stream nonempty for the bands listed in
   section 3 (guard table); (iii) at every odd-n' L=1 cell the forced orbit
   (below) is a PLANT that the enumerator must find — a per-cell
   completeness trip wired by algebra; (iv) orbit-closure invariant at
   every cell (round-1 mechanism).
4. **Degenerate-orbit flags**: `DEGENERATE_ORBIT_k` is EXPECTED at odd n'
   exactly for orbits divisible by `Phi_{n'}` (they live in the
   2-power-factor component where some `z^j` acts as scalar `-1`;
   at n'=96: normalized orbit size 16; at n'=192: size 32 or 64). Eval rule:
   ORBIT_CLOSURE_MISS is always fatal; DEGENERATE flags are fatal only on
   an orbit NOT divisible by `Phi_{n'}` (tag computed in-shard).
5. **Tags**: each window orbit rep `P` is classified by exact polynomial
   remainder against the cyclotomic factors of `z^N+1`:
   N=48: `Phi_32 = z^16+1`, `Phi_96 = z^32-z^16+1`;
   N=96: `Phi_64 = z^32+1`, `Phi_192 = z^64-z^32+1`.
   Level `l` is COVERED by the factor `Phi_d` with `d = n'/gcd(2l-1, n')`.
   `u(P)` = number of levels `l <= L` not covered by P's tag. Population:
   FORCED (u=0), SEMI-FORCED (0<u<L), GENERIC (u=L). Predicted incidence
   scaling: `q^-u`.

## 1. Pre-hoc structural analysis (recorded before computing)

**(a) Official-transport lemma (extends round-1's pure-subgroup exclusion
to the ENTIRE fixed-vector mixed channel).** Claim: at every official level
`L`, NO fixed integer vector `P != 0` in `R_{256L}` is a level-`1..L`
vanisher for more than finitely many official primes. Proof. Let
`m = odd(L)` (so `n'_L = 512L = 2^{9+v2(L)} m`). For fixed `P`, vanishing of
level `l` at infinitely many `q` forces `P(zeta) = 0` at a primitive
`(n'_L/g_l)`-th root of unity, `g_l = gcd(2l-1, m)`, i.e.
`Phi_{n'_L/g_l} | P` (bounded-height algebraic value with unboundedly many
prime divisors is zero; rationality of P turns one conjugate into the whole
factor). For each divisor `g | m` take `l = (g+1)/2 <= (m+1)/2 <= L`: then
`2l-1 = g` and `g_l = g`. So all factors `{Phi_{512L/g} : g | m}` divide P.
Their degree sum is `sum_{g|m} 2^{8+v2(L)} phi(m/g) = 2^{8+v2(L)} m = 256L`,
and they are exactly the cyclotomic factors of `z^{256L}+1`; hence
`(z^{256L}+1) | P`, i.e. `P = 0` in the ring. QED. Consequences: (i) the
odd-n' analogue forced families do NOT transport to any official cell;
(ii) any official-row kill via the mixed channel must be q-DEPENDENT
(constructions varying with q) — which is what saturation statistics, not
key recurrence, detect. Banked as a round-2 positive lemma (wz2 findings).

**(b) Forced/semi-forced structure of the round-2 odd-n' cells (all exact
hand algebra on fixed polynomials, verified in-run).**
- n'=96, L=1 (levels covered by: l=1 -> Phi_96): `F = Phi_96` itself
  (w=3, support {0,16,32}, signs +,-,+) is a forced primitive (q>3) window
  orbit at EVERY prime. Predicted forced ledger = EXACTLY {orbit(F)}, raw
  mass `2N/2^3 = 12`: ternary multiples `F*(1+z^a)` (w=6) contain F as a
  sub-vector when supports are disjoint (hence imprimitive at L=1), and the
  overlapping cases collapse (`z^16 F = -F`, `z^32 F = F`) to 0 or
  non-ternary vectors. Any OTHER Phi_96-tagged window orbit is a finding.
- n'=96, L=2 (l=1 -> Phi_96, l=2 -> Phi_32): forced impossible
  (`Phi_96 * Phi_32 = z^48+1 = 0`). Tag-{Phi_96} semi-forced (level-2
  accidental) is predicted EMPTY for q > 3: the only ternary Phi_96
  multiples in the window have level-2 values `3` or `3(1 +- omega^{3a})`
  whose norms are products of 2's and 3's. Tag-{Phi_32} semi-forced
  (level-1 accidental, predicted scaling q^-1) is the LIVE mixed channel:
  ternary multiples of `z^16+1` have EVEN weight (mod-2 argument), so
  w in {4,6} within the window [3,7].
- n'=96, L=3 (l=3 -> Phi_96 again): tag-{Phi_96} again predicted EMPTY
  (same norms); tag-{Phi_32} needs TWO accidents (levels 1,3; conjugate
  conditions), scaling ~ q^-2; generic q^-3. The L=3 cell is therefore
  predicted almost empty — it probes for unexpected channels.
- n'=192, L=1: forced = {orbit(F192)}, `F192 = Phi_192 = z^64-z^32+1`
  (w=3), raw mass `2N/2^3 = 24`. L=2 (l=2 -> Phi_64): tag-{Phi_192}
  predicted empty (same 2-3-norm argument via `F192 ≡ 3 mod Phi_64`);
  tag-{Phi_64} = live semi-forced channel, even weight, q^-1.
- LIFT structure: `F = D_2(Phi_48-vector)` with the `(q, n'=48)` row
  admissible iff `q <= 2^24` -> F is lift-owned at O96L1/b21,b23 but NOT at
  b25; `F192 = D_2(F)` with `(q, n'=96)` admissible at all O192L1 bands ->
  F192 always lift-owned there. Kill statistics are therefore computed on
  RAW ledgers (dedup-independent), see section 4 preamble.

**(c) Design nulls (same formulas as round 1's `wz_eval.py`):**
`lambda_orb(q,N,L) = sum_{w=L+1}^{L+5} C(N,w) 2^{w-1} / (2N q^L)`,
`Ppred = 1 - exp(-lambda_orb)`, `Epred = sum_w C(N,w)/(2 q^L)`. Numerators:
N=32 L=2: 2.479e8 (lambda = 3.87e6/q^2); N=48 L=1: 4.217e8 (4.39e6/q);
N=48 L=2: 5.134e9 (5.35e7/q^2); N=48 L=3: 5.34e10 (5.57e8/q^3);
N=96 L=1: 3.067e10 (1.60e8/q); N=96 L=2: 7.935e11 (4.13e9/q^2).
For odd-n' cells the null is applied to the GENERIC population (the tagged
populations are measure-zero slivers of the binomial count; stated, not
corrected). Floats only in design; verdict-path arithmetic exact.

## 2. Cells and scales (frozen row sets)

Primes: deterministic rule "first K primes q ≡ 1 (mod n') with q >= 2^b"
(round-1 `first_primes_1mod`). Windows always `[L+1, L+5]`.

**PART 1 (family B, L=2, N=32, n'=64):**
- Frozen round-1 bands (NOT recomputed for the kill statistic):
  b10 (rho=1.615), b12 (rho=2.395), b14 (rho=4.648), K=24 each.
- NEW: b15, K=384; b16, K=384 (mitm).
- DIAGNOSTIC (explicitly outside the kill sequence): b14-deep, K=96 —
  does the noisy K=24 b14 point move with more primes?
- DIAGNOSTIC (mechanism): on every nonempty b15/b16 cell, the count of
  LEVEL-1-only vanishers in the same weight window, giving an empirical
  P(level-2 | level-1) vs 1/q attribution (correlation vs accident).

**PART 2 (odd n'):**
- O96L1: N=48, L=1, bands b21/b23/b25, K=24 each (design lambda_gen 2.09,
  0.52, 0.13). Companion rows N=24 enumerated at b21/b23 (admissible);
  b25 companion vacuous (balance), stated.
- O96L2: N=48, L=2, bands b13/b14/b15, K=24 each (lambda_gen 0.80, 0.20,
  0.050).
- O96L3: N=48, L=3, band b13, K=12 (lambda_gen ~1e-3) — EXPLORATORY
  (integrity controls apply; its outcomes feed round 3, not this round's
  kill verdicts, except via the recurrence/norm controls).
- O192L1: N=96, L=1, bands b25/b27/b29, K=12 each (lambda_gen 4.76, 1.19,
  0.30). Companions N=48 (all bands) and N=32 (all bands) enumerated.
- O192L2: N=96, L=2, bands b16/b17, K=10 each (lambda_gen 0.96, 0.24).
  Only 2 bands -> corroborative for KILL-O2 (which needs >= 3 bands),
  fully subject to KILL-O1 and all controls.

**Replay/audit (PART 0 controls):**
- Banked M2 replay: (L=1, q=7937) and (L=2, q=193), direct engine + mitm
  equality (raw counts and raw W_cl must equal banked EXACTLY).
- Round-1 replay: A/b21 q=2107073 (raw 4; round-1-convention shadow dedup
  1 with 5 links); B/b14 q=21569 (single w=7 orbit, recorded rep,
  W_cl=1/2); C/b21 q=2100353 (raw 44; shadow-only 34 with 10 links; lift
  companion data), plus canonical dedup and BOTH composition orders.
- Deduped-C1' audit (spec section 6): the eight banked rows with <= 350
  window orbits: (1,3137), (1,5569), (1,7937), (1,12289), (2,193),
  (2,257), (2,449), (2,577). E reconstructed exactly from banked
  `m1_dli_m1_results.json` (M2's `full_spectrum_e` logic verbatim);
  exact test `E-1 <= 4r(1+W_cl^dedup)`. Any violation = spec-level FINDING
  (M3-interface inconsistency), pre-declared NOT a WCL-ZONE kill (NK-5).
  The four larger L=1 rows (>350 orbits) are out of scope this round
  (stated).

## 3. Controls

Required to MATCH (else KILL-3 integrity, affected cells INVALID):
- C-1: banked M2 replay exact (counts + W_cl, both engines).
- C-2: round-1 replay exact under the round-1 convention (values above).
- C-3: V1 = direct-vs-mitm equality at L=3 on an engine-test cell N=32,
  q = first q ≡ 1 mod 64 >= 193 with nonempty w<=8 window (scan <= 8
  primes; assert found; direct covers w=4..8 here — N=32 makes this
  affordable; wz-C5 vacuity rule respected). V2 = direct-vs-mitm at N=96,
  w<=4, first O192L1 prime — nonvacuous by the forced plant F192 (w=3).
- C-4: lift identity (T4): zero misses on every admissible companion,
  including the k=3 companions at O192L1 (validates D6 for k=3 on data).
- C-5: forced plants: orbit(F) present in RAW ledger of EVERY O96L1 cell;
  orbit(F192) in EVERY O192L1 cell; per-q exact re-verification. The
  level-1-covering tagged sub-ledger must be IDENTICAL across primes
  within each L=1 odd-n' band up to per-prime primitivity exceptions,
  each individually verified exactly (a sub-vector of the forced vector
  accidentally vanishing at that q) and reported.
- C-6: negative plants: orbit(F) ABSENT from every O96L2/O96L3 ledger;
  orbit(F192) absent from every O192L2 ledger (their uncovered-level
  values have norms with prime factors only 2 and 3 — 1(b)).
- C-7: recurrence/norm law: for EVERY witness orbit at an odd-n' cell and
  every uncovered level, `q` must divide the exact resultant
  `Res(Phi_d, P mod Phi_d)` (sympy, exact); a zero resultant means a
  missed tag (fatal); a non-dividing q is fatal (enumerator or tag bug).
- C-8: conformance suite T1-T10 of `wz2_dedup_spec.md`, including the
  five mutation controls M-A..M-E (each required to trip/be detected).
- C-9: nonemptiness guards (#137, redesigned per 0.3): sides nonempty at
  every cell; band-level candidate streams nonempty at ALL bands; plant
  nonemptiness at odd-n' L=1 cells; saturated-band guards: O96L1/b21 and
  O192L1/b25 must each have >= 1 nonempty GENERIC-population cell... 
  correction (design honesty): generic saturation guard applies to
  O96L1/b21 (lambda_gen 2.09 -> P(all 24 empty) ~ e^-50) and O192L1/b25
  (lambda_gen 4.76, K=12); B/b15-b16 and O96L3 are near-empty BY DESIGN
  and carry no band-emptiness guard (their guard is the stream + plant
  mechanism, 0.3).

## 4. Kill lines (frozen)

Preamble: all kill statistics are computed on RAW ledgers (shadow dedup
preserves nonemptiness by P4; lift ownership and shadow mass-shrink affect
only reported masses). rho(B) = Phat(B)/Ppred(B) as in round 1, with
Phat/Ppred restricted to the stated population.

- **KILL-B (part 1, family B).** Sequence = (b10, b12, b14 frozen round-1
  K=24 values; b15, b16 new K=384). Trips iff ALL of:
  (i) rho strictly increasing across all five bands;
  (ii) rho(b16)/rho(b10) >= 4;
  (iii) >= 4 nonempty primes in b15 UNION b16, with >= 2 in b16.
  Design power: under a continuing-doubling trend (rho ~ 9, 18) expected
  new-band nonempty ~ 2.4 + 2.1 -> P(trip) ~ 0.5; under the Poisson null
  expected ~ 0.27 + 0.12 -> false-trip < 1e-3 (dominated by (iii)).
  Verdict if tripped: KILLED (scaling, analogue scale) — same meaning as
  round-1 KILL-2.
  **SURVIVE-with-explanation** iff rho turns over (rho(b15) <= rho(b14) or
  rho(b16) <= rho(b15)) or the new bands' nonempty counts are within
  2-sigma Poisson of the null: family B declared Poisson-consistent, the
  round-1 monotonicity attributed to small-K noise at b14 (the b14-deep
  diagnostic corroborates or complicates this).
  **UNRESOLVED-ESCALATE** iff monotone but sub-threshold AGAIN: round 3
  pre-commitment = K >= 1536 at b15-b17 with the same statistic, no
  threshold renegotiation.
- **KILL-O1 (part 2, generic channel).** Trips iff, restricted to the
  GENERIC population (u = L): (a) some odd-n' band at L in {1,2} with
  >= 10 primes and Ppred_gen <= 0.25 has Phat_gen >= 0.75; OR (b) >= 3
  distinct generic-tag orbit keys each recur at >= 3 distinct primes
  within one cell family; OR (c) any single generic-tag key recurs at
  >= 5 distinct primes (a fixed w<=8 ternary vector has level-value norm
  <= w^{phi(d)} ~ 2^96; five primes >= 2^13 exceed any plausible smooth
  factorization — and C-7 must confirm each recurrence exactly).
  Meaning: q-robust structure in the channel that round 1 was
  structurally blind to. Verdict: KILLED (structural, analogue scale;
  official lift argued via the mixed channel being live at odd n' —
  noting 1(a) excludes only FIXED vectors, not q-dependent families).
- **KILL-O2 (part 2, semi-forced anomaly).** For the O96L2 family (the
  only odd-n' family with >= 3 bands at L >= 2): SF(band) = mean per-prime
  count of SEMI-FORCED window orbits. Trips iff SF strictly increasing
  across b13 < b14 < b15 AND SF(b15)/SF(b13) >= 2 AND >= 3 semi-forced
  witness orbits in b15. Meaning: the norm-divisor channel GROWS with
  scale instead of decaying ~ q^-1 — structure creation with scale that
  no current algebra predicts. O192L2 (2 bands) is corroborative only.
- **KILL-3 (integrity, never a predicate kill):** any C-1..C-9 failure =>
  round INVALID for the affected engine/cells; DEFER and shrink.

## 5. What does NOT count as a kill (pre-declared)

- **NK-1:** presence and mass of the forced plants (F: raw mass 12; F192:
  raw mass 24) and their lift-ownership pattern — predicted in 1(b).
- **NK-2:** semi-forced populations at rates consistent with a DECAYING
  q^-u law, whatever their absolute size — predictable norm-divisor
  algebra; the official transport of any FIXED vector is excluded by 1(a).
- **NK-3:** degenerate-orbit flags on Phi_{n'}-tagged orbits (0.4).
- **NK-4:** super-volume magnitudes (round-1 NK-i) and nonzero analogue
  ledgers as such (round-1 NK-ii; quantization wz-C1).
- **NK-5:** changes to banked numbers under the NEW canonical dedup —
  findings about the spec (reported with per-link diffs), including any
  deduped-C1' audit violation (spec section 6): that is an M3-interface
  finding, not a WCL-ZONE kill (different predicate).
- **NK-6:** recurrences fully explained by exact norm divisibility below
  the KILL-O1(b)/(c) thresholds.
- **NK-7:** O96L3 outcomes of any kind (exploratory cell), except control
  failures.

## 6. Verdict rules

- **KILLED:** KILL-B, KILL-O1, or KILL-O2 trips with all controls green.
- **SURVIVED (per part):** part 1 — KILL-B does not trip and the
  explanation branch resolves; part 2 — KILL-O1/O2 do not trip and all
  plants/controls hold. Evidence weight to state: q <= 2^17 (L=2 B), 
  q <= 2^29 (odd-n' L=1), n' in {64, 96, 192}, L in {1,2,3}; official-row
  specificity untouched (round-1 caveat stands).
- **UNRESOLVED-ESCALATE:** part 1 monotone-but-sub-threshold (round-3
  pre-commitment in KILL-B).
- **MIXED/DEFERRED:** Modal shard losses; shrink per shard, never rescue
  locally.

## 7. Compute plan (Modal only; COMPUTE LAW)

All computation via
`tools/ramguard modal -- ~/.venvs/modal/bin/modal run tools/modal_run_script.py
--script wz2_census_modal.py [--data m1_dli_m1_results.json] --args "<shard>"`.
Local execution only for the tiny eval (`tools/ramguard tiny`). Shards
(app ids recorded in wz2_results.md): `replay` (C-1/C-2/T1-T10),
`c1audit` (+data), `xcheckl3` (V1), `xcheck96` (V2), `band_b15` (incl.
b14-deep), `band_b16`, `o96_l1`, `o96_l2a` (b13), `o96_l2b` (b14),
`o96_l2c` (b15), `o96_l3`, `o192_l1`, `o192_l2a` (b16), `o192_l2b` (b17).
Any Modal failure => DEFER that shard and shrink scope per section 6.

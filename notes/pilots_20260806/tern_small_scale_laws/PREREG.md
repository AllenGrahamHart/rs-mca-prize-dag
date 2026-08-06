# PRE-REGISTRATION — TERNARY SMALL-SCALE LAWS: do the instances actually track each other? (round 19, ADVERSARIAL-EMPIRICAL)

Round 19, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. MANDATE: the empirical
stress test of the unification. If the three instances are one object
family, their measured laws at matched small parameters must TRACK
each other where the candidate says they should; if they scale
differently, the unification is wrong no matter how pretty the
formalism. Also: explain (or weaponize) the round-18 anomaly.

## 0. The instances at matched scale (quote the minted nodes first)

- (I1-mini) the GRS-dual ternary mass: 2-power 2N, half-system
  evaluation, R = round(S/log2 p) — the z1 pilot's valid-miniature
  protocol (CATCH-Z6: 2-POWER LENGTHS ONLY — composite lengths
  carry p-independent parasitic relations).
- (I2-mini) single-condition relations: eps in {0,±1}^L,
  sum eps_j theta^j = 0, theta of order 2L — the crossing pilot's
  toy object (its measured orbit law: LEMMA ROT, exactly-2L-orbits,
  over-dispersion).
- (I3-mini) the half-length cyclic ternary object of LEMMA AB — the
  efloor pilot's census machinery (reusable:
  notes/pilots_20260806/efloor_sparsity/sp_lib.py).

## 1. Pre-registered deliverables

- **(L1) THE MATCHED CENSUS.** One exact census framework over all
  three instance shapes at matched (effective length, p, condition
  count) grids — 2-power lengths only, all characteristics at once
  where the HNF/bad-prime method reaches. Measure per instance: the
  relation count law in p at fixed shape; the onset threshold (the
  empirical balance point); the orbit structure; the weighted mass
  vs unweighted count ratio.
- **(L2) THE TRACKING TEST (the adversarial core).** The
  unification predicts: (a) the single-condition instances (I2, I3
  at w' = 2) obey the SAME law after the exact dictionary
  (coordinator's expectation from LEMMA STRAT: I3's binding stratum
  IS an I2 instance — verify the dictionary numerically, exactly);
  (b) I1 at R conditions behaves as R "independent" I2-layers to
  first order (the product/syndrome heuristic — the z1 pilot's
  first-moment-restricted-to->2R law). MEASURE both. A significant,
  structured deviation that the dictionaries cannot absorb is a
  REFUTATION of the unification's quantitative content — report it
  as such with the exact deviation law.
- **(L3) THE ANOMALY.** Round-18 efloor residual 4: at n = 32,
  p = 5, w = 2 the flat model predicts ~110 nonzero ternary
  codewords; the exact count is 0. Explain it: is it the
  SP-TERNARY mechanism, a Gauss-sum exactness effect (2-power
  conductor), the orbit over-dispersion, or something new? Whatever
  the mechanism, test whether it appears in the OTHER instances at
  matched parameters — a shared anomaly is the best possible
  positive evidence for the unification; an instance-local one is a
  disanalogy datum.
- **(L4) THE SCALING VERDICT.** For each measured law: does it
  extrapolate consistently ACROSS instances toward their respective
  prize regimes (I1 at p ~ 2^64, I2 at p ~ 2^129, I3 at the
  official q), or do the instances leave the shared regime at
  different rates? No prize-row claims — the deliverable is the
  small-scale consistency verdict with honest scale caveats.

## 2. Pre-registered falsifiers / honesty clauses

- A structured tracking deviation (L2) that survives the exact
  dictionaries = the unification's quantitative refutation. Do not
  absorb deviations into free parameters post hoc — dictionaries
  must be stated BEFORE measuring.
- The composite-length rule is absolute except in one labelled
  control cell (deliberately composite, to reproduce CATCH-Z6's
  parasitic relations as the negative control).
- Nulls from unreached grid cells are reported as unreached.

## 3. Rules of engagement

- DRAFT ONLY: write only inside
  notes/pilots_20260806/tern_small_scale_laws/. Never edit dag.json,
  node shards, tools/, or push. Do NOT read
  notes/pilots_20260806/tern_route_b/ (sibling independence). You
  MAY reuse banked machinery: efloor_sparsity/sp_lib.py,
  es_coprimality/cop_lib.py, crossing_low_w/low_w_lib.py,
  z1_ternary_mass artifacts — all banked, not sibling-active.
- COMPUTE LAW: never bare python3, INCLUDING file patching and JSON
  peeking — tools/ramguard tiny|local -- python3 ..., literal --,
  from repo root /home/u2470931/smooth-read-solomin/prize.
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report; the
  coordinator persists it verbatim.

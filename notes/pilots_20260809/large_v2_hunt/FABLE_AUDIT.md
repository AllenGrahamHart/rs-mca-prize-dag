# FABLE_AUDIT — large_v2_hunt (round 25)

Coordinator: Fable. Date: 2026-08-09. Pilot: Opus (task a36eb38525ff7e4e1,
~79 min, 118 tool uses). Quarantine marker: ledger line 3731, observed.

## Verdict

**BANKED. The mystery-5 narrowing decision now has real support: option
(c) large-v_2 is dead three ways (exhibition to v_2=26, ~2^98 heuristic
counterexamples at the registered threshold 41, and the mechanism PROVED
ABSENT via NORMLAW + the repo's own local-norm surjectivity equality),
and it cannot be repaired — the working threshold ~136 excludes every
deployed Proth row. Option (b) o(1)-sparsity is positively supported
(top-window bad density ~2^-112 with the suppression law exactly
prime-density). My prior recommendation (c)+(b) is WITHDRAWN; the
updated recommendation is (b) primary, (a) fallback. The choice remains
the user's.**

## Replays (all by me, under ramguard)

| what | result |
|---|---|
| repro_v2_r25.py (standalone, zero-import) | **OVERALL: PASS** — the v_2=26 witness: box membership, 2^128 < p <= 253^32, 227-bit independent norm, divisibility + cofactor 197633, rho of exact order 128, kernel membership, odd s |
| d3_thm.py (LAW 1 + LAW 2) | **0 violations**: LAW 2 as an identity at h=2..64 (arbitrary integer coefficients) + corollaries; LAW 1 on non-box vectors at h=8..64 |
| d1_h8.py (exhaustive 5^8 census) | **exact**: 390,624 nonzero norms, 1450 distinct, MAXNORM 614656=28^4, 554 odd prime divisors (536 in the f=1 stratum = round-22's ground truth exactly), MAXV2BAD8=12 (p=12289, the Kyber prime), full v_2 profile identical to the report's table |

I additionally checked the NORMLAW argument myself: ideal-norm
factorization gives every odd Norm(w) as a product of p^f factors with
p^f = 1 mod N' — three lines, sound; and the "onto" reading of the
e1_n256 local-norm EQUALITY is correct (an equality of groups leaves no
room for a forced stronger congruence). LAW 2's Newton-identity proof
sketch is sound for w = 1 + 2v; the pilot itself names general w as an
open gap, so it is banked as proved-in-scope + machine-checked.

Not replayed: the 21.4M-vector h=64 ladder and the 14.7M-incidence V1
test (multi-hour sharded runs; their state/*.json checkpoints and logs
are banked; the calibration arm C1 that anchors them reproduced the
round-22 exhaustive densities to the printed digit inside my d1_h8
replay).

## Audit judgements

- **The decision structure is right**: the pilot separated "dead by
  exhibition" (proved, threshold <= 26), "heuristically false"
  (calibrated expectation, threshold 41), and "mechanism absent"
  (proved), and calibrated its own silence at rung 41 as uninformative
  BEFORE running (expected count 0.005). The registered falsifier
  discipline held.
- **The K=0.736 artefact catch matters**: without the cofactor split,
  the pooled constant would have read as mild structural suppression;
  LAW 2 explains it exactly (cofactor-1 acceptances pinned at v_2=7).
  This is the difference between "weak evidence for (c)" and "no
  evidence for (c)".
- **Self-corrections**: 6, all disclosed — notably R0 FALSE (repaired
  via residue degrees, verified in my census replay: 554 = 536 + 18)
  and the dead-on-arrival registered gate (replaced mid-run by the
  cofactor-congruence rung instrument, a declared deviation from R2).
- **Compliance**: quarantine held, RAM discipline held (checkpointed
  5-min walls), draft-only, stdlib only, no git/Modal.

## Corrections applied

- critical/nodes/integer_code_distance_cert/statement.md — round-25
  narrowing decision-support addendum: (c) dead three ways + not
  repairable (VSTAR 136-139 vs deployed rows at 92-97), (b) positively
  supported, LAW 2 banked with its named gaps, coordinator
  recommendation updated to (b) primary + (a) fallback. The decision
  stays SURFACED to the user. No status flip.

## Follow-ups filed (not executed)

- If the user selects (b): the o(1)-sparsity statement can be posed
  directly from the measured suppression law (BADFRAC flat in v_2,
  density 2^-112 in W_TOP) — a draft-conjecture candidate.
- Named gap 1: LAW 2 for general w (the nodd >= 3 strata) — a small
  algebra target with an existing machine-check harness.
- Named gap 2: box realization of 2-adic norm classes beyond depth
  2^17.

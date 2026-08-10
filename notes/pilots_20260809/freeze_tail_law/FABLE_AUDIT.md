# FABLE_AUDIT — freeze_tail_law (round 26)

Coordinator: Fable. Date: 2026-08-09. Pilot: Opus (task a0f0729dc2e629212,
~45 min, 47 tool uses). Quarantine marker: ledger line 3872, observed
(one pre-registration ckpt key-peek disclosed in the PREREG itself).

## Verdict

**BANKED. The round-25 named obstruction is closed as a THEOREM, not a
fit — the freeze tail is a short-vector census of a rank-e lattice
terminating at an exact integer cutoff — and the pilot's own registered
tail-form predictions MISSED, which is exactly why the theorem is the
right object (there was no curve to fit). S_inf = 1/ln 2 falls to
factorial telescoping. G-c's undecidable band shrinks (232, 256] ->
(251.1, 256], with the calibration caveat named rather than hidden.
Round 25's "measured freeze scales" line is corrected (C26-5): they
were never cutoffs.**

## Replays (all by me)

| what | result |
|---|---|
| tail.py P2 from a scratch copy | **419/419 rows, 0 theorem violations — PASS** |
| the (32,2,1) exact cutoff | **INDEPENDENTLY re-derived: Q* = 273857** by my own full-box Bareiss negacyclic-determinant sweep (machinery disjoint from the pilot's resultant code); also reproduces 1450 distinct norms / MAXNORM 614656, tying to the round-25 large_v2 census |
| S_inf telescoping | identity S_K = K - 2^-K log2((2^K)!) verified to 1e-15 at K = 6/12/18; the telescoping algebra and the Stirling step verified BY HAND |
| the cutoff theorem's proof | verified BY HAND: non-frozen forces some Phi_{d_v} coprime-to-C hence a nonzero integer resultant; q = 1 mod n splits the power-of-two cyclotomic with distinct roots, so the g_v imposed frequencies give q^{g_v} | Res; Hadamard bounds the box. Sound |
| escape tests | the pilot replayed phase A (PASS 8/8 + PR-A) and analytic.py (break scale 255.999999987544, rebuild 5/5) — both of which I had already replayed independently in the round-25 bank |

Not replayed: the 144 new census rows (L3-reduced; rest on L3's
181/181 bit-exact verification against banked rows + two guards per
cell — frozen at 2^{B+4} and Galois invariance; the pilot declares the
absence of an independent MITM cross-check as the very point of L3);
the depth-window refits (deterministic given cdata.json, which P2
consumed on my replay).

## Audit judgements

- **The theorem is the right closure and the misses prove it**: PR-6
  missed by 0.7 and PR-6b's 2/e slope was refuted — because the tail
  has no deterministic exponent. The pilot reported the misses first
  and converted PR-6's failure into finding C26-9 (contamination
  reaches 3-5 bits BELOW LamStar), which retroactively explains
  round 25's fit scatter.
- **C26-5 is a genuine forced correction of round-25 banked text**
  (my addendum item (7) cited "measured freeze scales 14.5..67") —
  the excess is non-monotone in q and "smallest frozen scale" was
  never an estimator. Applied to dli_c2pp_joint_reserve.
- **The licensed-range extension is banked WITH its caveat as
  load-bearing text**: the power re-calibration at the new tolerance
  is the named next job; until it runs, 251.1 is [law]-grade, not
  clean.
- **The near-self-falsification episode (self-correction 2) is the
  right discipline**: the pilot traced the 34/67 scales to sparse
  grid points before registering a refutation of its own theorem.
- **Compliance clean**: quarantine held, compute law total
  (RAMGUARD_TIMEOUT documented at 600-3000s, background jobs for
  long enumerations), RAM discipline held (the norm enumeration
  restructured mid-design to avoid a multi-million-entry set,
  declared), draft-only held (round-25 dir read-only; the
  __pycache__ timestamps predate the session).

## Corrections applied

- critical/nodes/dli_c2pp_joint_reserve/statement.md — round-26
  addendum: the cutoff theorem + L3 + the sharp max-norm law, the
  C26-5 forced correction of round-25 item (7), S_inf proved with
  the explicit mint form, the licensed range 232.7 -> 251.1 with
  caveat, the census pricing of (232, 256] (unreachable; tolerance
  route only), the C26-7 model flag. No status flip.

## Follow-ups filed (not executed)

- power.py re-run on synthetic worlds at the new tolerance — the
  single item between 251.1 [law] and 251.1 clean.
- The max-norm law (e-1)^{e/2} u^e beyond e = 8 — a small conjecture
  with an existing verification harness.
- Mint queue: the freeze-tail cutoff theorem; S_inf = 1/ln 2 with
  the R3inf_full asymptotic (both self-contained).
- C26-7: the linear coset-term model understates true depth exactly
  in the break-constant window — flagged for any future packet
  audit; no transport licensed.

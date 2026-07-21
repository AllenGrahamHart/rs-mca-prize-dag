# dli_c1r3_gated_envelope_bound

- **status:** TARGET (red leaf; minted at the 2026-07-21 dli amber ceremony,
  maintainer Decision 6)

## Statement (C1'-r3 — the official-scoped, extended-ledger successor of the REFUTED C1')

Let `(q, n'=2N, L)` be a generated prime-field full-half-section row with

```text
(H1)  q prime,  q = 1 mod n',
(H2)  2^N >= q^L,  N >= 16L,
(H3)  OFFICIAL-ADMISSIBILITY GATE:  v_2(q-1) >= 41   [analogue scale: >= 20].
```

With `T, E, r` exactly as in `C1PRIME_LEVEL_SCALED_POSE.md` and the EXTENDED
RAW ledger `w_max_r3(L) = L+7`,
`W_ext(q,N,L) = sum_(primitive signed-shift orbit O, L+1 <= w(O) <= L+7) 2N 2^(-w(O))`,
the claim is

```text
E - 1 <= 4 r (1 + W_ext).                              (C1'-r3)
```

All r2 conventions (RAW primitive signed-shift orbit ledger per
`dli_wcl_raw_ledger_interface_guardrail` and maintainer decision 4a,
exact-rational verdict path, #137 normalization discipline) are kept verbatim;
the ONLY changes from the refuted r2 pose are the official gate (H3) and the
window extension L+5 -> L+7. Pose frozen 2026-07-19 BEFORE the round-1
falsifiers were armed (`notes/c1r3_program_20260719/c1r3_pose.md`).

## Evidence state (two survived pre-registered adversarial rounds)

- **Round 1** (33-row complete in-gate census below 2^28): both refuting kill
  lines NOT FIRED; worst K'_r3 = 1058880560632659/1033540934303744 ~ 1.0245
  (3.9x margin under the literal-4 line); gate-mirror weight-3 census max
  v_2 = 16 < 20; the then-armed K'>=1 amber tripped at two bare-envelope rows
  -> verdict MIXED under that calibration, prompting the round-2
  recalibration (below).
- **Round 2** (segmented DP census q in [2^28, 2^32), 52 ledgered rows +
  octave worsts + the accident row): ALL pre-registered lines NOT FIRED.
  Worst K'_r3 = 35507502101438673/25332747971067904 ~ 1.4016 (2.85x margin);
  **zero rows at K' >= 2**; the accident row 918552577 reprices 3.000 -> 1.333
  through the load-bearing extended window; the legacy band [1,2) grows in
  population while its ceiling plateaus at ~1.4 (extreme-value effect,
  finding c1r3b-C4). Envelope saturates at the iid baseline (E-1)/r -> 1.

## Standing watch (maintainer Decision 6, 2026-07-21 — binding for all future rounds)

- **KILL-LITERAL:** any in-hypothesis row with K'_r3 > 4 (never moved).
- **AMBER-2:** any row with K'_r3 >= 2, measured on the EXTENDED ledger
  (2x the iid asymptote) -> re-examination trigger; with a sustained
  iid-excess trend it is a kill.
- **KILL-TREND:** the iid-excess trend line as frozen in
  `notes/c1r3_program_20260719/c1r3b_falsifiers.md`.
Rows in [1,2) are the legacy band: recorded, non-triggering.

## Non-claims

Twice-survived evidence is NOT a proof. The L=2 in-gate regime is exactly
unreachable (near-gate ladder is the standing instrument); the octave-31
census is incomplete (4 rows outside the compute law); no official-row
certificate family is supplied. This node prices the per-level envelope
only — zone mass `W_ext <= 1/32` is the SEPARATE `dli_wcl_zone_coverage`
predicate (extended slots), and the joint reserve is `dli_c2pp_joint_reserve`.

# Brief 1 — the gated envelope bound (C1'-r3)

**Node:** `critical/nodes/dli_c1r3_gated_envelope_bound/` ·
**status TARGET** · minted 2026-07-21 (amber-ceremony Decision 6) ·
**upstream:** no counterpart (OURS_ONLY).

## The mystery in one paragraph

For prime-field rows passing an official 2-adic admissibility gate, an
empirically bulletproof envelope bounds a spectral excess `E-1` by four
times a rank parameter times an *extended orbit-weight ledger* — and we do
not know why. The pose has survived two pre-registered adversarial censuses
(85 rows total, worst observed ratio 1.40 against an allowance of 4, i.e. a
2.85x margin) after its two predecessors were *refuted*, so the envelope is
calibrated by falsification, not curve-fitting. What is missing is any
mechanism: nothing currently explains why weight-truncating the orbit ledger
at `L+7` (and not `L+5`, which failed) suffices, or why the official gate
`v_2(q-1) >= 41` is the right hypothesis.

## Formal pose (frozen 2026-07-19, before round-1 falsifiers were armed)

Let `(q, n'=2N, L)` be a generated prime-field full-half-section row with

```text
(H1) q prime, q = 1 mod n'
(H2) 2^N >= q^L,  N >= 16L
(H3) v_2(q-1) >= 41        [analogue scale: >= 20]
```

With `T, E, r` as in `C1PRIME_LEVEL_SCALED_POSE.md` and the RAW primitive
signed-shift orbit ledger truncated at `w_max_r3(L) = L+7`,

```text
W_ext(q,N,L) = sum over primitive signed-shift orbits O with
               L+1 <= w(O) <= L+7   of   2N * 2^(-w(O))

CLAIM (C1'-r3):   E - 1 <= 4 r (1 + W_ext).
```

Conventions (kept verbatim from r2): RAW orbit ledger per
`dli_wcl_raw_ledger_interface_guardrail`, exact-rational verdict path, the
`#137` normalization discipline.

## Death ledger — do not resurrect

- **C1 (original):** refuted in the dli falsification round (F-round);
  both frozen conditions failed. The amber status lasted one round.
- **C1' (r2 pose, window `L+5`, no official gate):** REFUTED. The r3
  changes are exactly: add gate (H3); extend the window `L+5 -> L+7`.
- A `K' >= 1` amber line (round-1 calibration) tripped at two bare-envelope
  rows; the round-2 recalibration replaced it. Any proposal reusing the
  round-1 calibration must address those two rows explicitly.

## Evidence state (why we believe it anyway)

- **Round 1:** complete 33-row in-gate census below `2^28`. Both refuting
  kill lines NOT FIRED. Worst `K'_r3 ~ 1.0245` (3.9x margin). Gate-mirror
  weight-3 census max `v_2 = 16 < 20` (the gate is doing real work).
- **Round 2:** segmented DP census `q in [2^28, 2^32)`, 52 ledgered rows +
  octave worsts + one "accident row". ALL pre-registered lines NOT FIRED.
  Worst `K'_r3 ~ 1.4016` (2.85x margin); zero rows at `K' >= 2`. The
  accident row `918552577` reprices `3.000 -> 1.333` **through the
  load-bearing extended window** — the `L+7` extension is what absorbs it.
  The legacy band `[1,2)` grows in population while its ceiling plateaus
  near 1.4 (an extreme-value signature, not a drift).

Full record:
`critical/nodes/dli_prime_weighted_large_block_support/notes/c1r3_program_20260719/`
(pose, falsifiers, both round ledgers),
`critical/nodes/dli_prime_weighted_large_block_support/DLI_CLOSE_PINNED.md`
(the lane's Pro-dialogue history).

## Why it resists — and the conversion ask

The obstruction: `E` is a global spectral quantity of the row, while
`W_ext` is a local weight-census; every attempted per-level or per-junction
factorization of the comparison has been refuted (see brief 2 — the C2
factorization died too; these two heads fail for the *same* reason,
cross-level accidents that no uniform local bound absorbs).

**The ask.** Find a case structure. Candidate axes we have looked at, none
carried through:

1. **By orbit-weight class** `w in {L+1, ..., L+7}`: is there a per-weight
   comparison `E_w - contribution <= 4r * (window slice)` with a finite
   list of cross-weight interaction types? The accident row's repricing
   through the window suggests interactions are few and classifiable.
2. **By 2-adic stratum:** the gate `v_2(q-1) >= 41` suggests stratifying
   rows by `v_2(q-1)` and proving the envelope on each stratum, with the
   low strata (where it can FAIL — we hold refuting instances below the
   gate) explicitly excluded by the official row spec. A proposal that
   explains the gate's role structurally would be a major step alone.
3. **Budget form (the E1-ladder move):** replace the per-row envelope by an
   aggregate over the (finite, gated, official) row family: the prize only
   needs official rows. If the row family is finite and enumerable, C1'-r3
   could in principle become a *census with a completeness theorem* — the
   question is whether the official row family's enumeration is provably
   complete and the per-row check is bounded (the round-2 DP census
   machinery already decides single rows in bounded exact arithmetic).

Route 3 is the most concrete: **what is missing is a finiteness/enumeration
theorem for the gated official rows and a complexity bound making the DP
verdict per row a certified decision procedure.** If both exist, this whole
head converts to an m2-style program overnight.

> **[CORRECTION 2026-08-01 — route 3 is REFUTED by the Pro dossier's
> stress test, audited and accepted on our side.]** The official row
> family is universal, not finite: `official_row_primes_pinning` (PROVED)
> denies any hidden finite list, and even under the `q < 2^256` cap the
> progression `q = 1 + k*2^41` has `2^215 - 1` candidates while the
> round-2 DP is `Theta(q)` in state (>= 2^44 bytes at the smallest
> official scale). The finiteness that exists is in WITNESS TYPES, never
> in primes. The corrected conversion is the consumer-exact zero-window
> theorem **C1-ZERO / SWIF-4** (variance form + cyclotomic-ideal geometry
> + the new 256-basis block orbit), composed with the ten
> `dli_wcl_slot_*` leaves and the Newton exclusion. See
> `responses/BRIEF1_PRO_DOSSIER.md` and
> `responses/BRIEF1_DOSSIER_AUDIT.md`.

## Guards

- Exact rationals only; the DP census path is the reference implementation.
- The RAW ledger definition is normative (`dli_wcl_raw_ledger_interface_guardrail`);
  proposals using a smoothed/pruned ledger must prove equivalence first.
- Any weakening of (H3) must confront the sub-gate refuting instances.

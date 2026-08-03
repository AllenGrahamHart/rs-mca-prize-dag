# Coordinator audit — round-7 anchor: |K| vs the escape residual

**Auditor:** Fable, 2026-08-03. **Verdict: BANKED — verdict accepted as
stated (UNIFIED as one operator, SEPARATED as sets).**

## Replay

`tools/ramguard tiny -- python3 notes/pilots_20260803/k_escape_unification/verify.py`
-> 18 checks, 0 FAIL (reproduced by the coordinator). All seven
pre-registered falsifiers survived.

## Hand-verification (line-audited)

- **Lemma 0**: correct; the two cited ingredients (S4-1 localisation,
  MDS weight kill) are the banked ones, correctly quoted.
- **U1 (one-pass)**: the key identity `mult_{V,T^1}(x) = mult_{V,S}(x)`
  for `x in W_0` (and `0` otherwise) is exact — a point leaves every
  support simultaneously or none. Hand-checked. DEFINITIONAL finding;
  Claim 6's floor and all recorded fixture values unchanged.
- **U2 (P-A1 peel = full closure)**: the induction invariant
  `W(F_i, T^i) = W_i` needs `W_i <= W_{i-1}`, which follows from
  `F_i <= F_{i-1}` (multiplicity monotone). Hand-checked; the death-test
  match `|T^{i+1}_a| <= k <=> |S_a ^ W_i| <= k` is exact.
- **U3 (kernel floor)**: the identity `h - (|T|-k)^+ = min(h, |S_a\T|)`
  verified in both branches (`|T| >= k` and `|T| < k`) using
  `|S_a| = k + h` — the same cap mechanism as the banked escape floor.
- **U4/U5**: immediate given U1-U3 (`T^inf_a <= S_a ^ W_0`).
- **S1 fixture**: `W_0 = {0,1,2}`, round-1 deaths, round-2 collapse to
  `K = empty`, escape floor 8, kernel floor 10 = Vh — every number
  hand-recomputed and machine-confirmed.
- **The dictionary** (`>= h` at coverage `<= 2` iff `<= k` surviving)
  is an exact complement count at `|S_a| = A = k + h`.

## Flag adjudication (8 flags, all raised not guessed)

1 (lane families not identified) — ACCEPTED as the correct scope; no
cross-lane hypothesis transport. 2 (`|S_a| = A` consumed) — consistent
with definitions item 7; U3 stated per-ray if sizes vary: fine.
3 (`Gamma_0 <= (2R-1)/2` conditional) — recorded as CONDITIONAL only;
noteworthy: first finite ceiling on the currently unbounded `|K|` term.
4 (U1 definitional, addendum recommended) — APPLIED: dated addenda to
`background/nodes/xr_support4_structure/statement.md` and
`notes/BAND_LANE_DEFINITIONS.md` (item 12'), plus a factual pointer in
the band TARGET's statement; the RE-POSE of the open input in U5 form is
SURFACED to the user, not applied. 5 (escape-1 gate-clean realizability
OPEN) — correctly separated from the proved floor gap; this is the
sharpest new open question of the round. 6/7 (toy scale; sweep =
consistency) — correct posture. 8 (per-ray accounting consumed) —
banked input, cross-checked per system.

Process note: the pilot's REPORT.md write was blocked by the harness and
staged via scratchpad copy — self-reported, transparent, accepted. The
duplicate spot (D0-3 = S4-14 upper half) is recorded as CONCORDANCE per
the determined-family rule.

## What this changes

- The two lanes' residuals are ONE covering-design condition; work on
  either heart now transfers verbatim at the residual-object level.
- The kernel floor strictly dominates the escape floor and is the floor
  of record going forward (addendum applied; nodes unchanged in status).
- The band heart's remaining channels are EXACTLY escape-0 (the measured
  collapse — the sibling pilot's objective) and escape-1 (new; gate-clean
  realizability OPEN).
- Conditional chain to a first `|K|` ceiling recorded (not banked as a
  bound).

## Surfaced decisions (for the user)

- Re-pose the band TARGET's single open input in the strictly weaker U5
  (iterated-core) form? Recommended: YES — no cost, smaller residual
  class; the statement text already points to item 12'.
- Commission the escape-1 realizability question (flag 5) as the next
  pilot anchor alongside the zero-escape channel? Recommended: YES —
  it now decides whether the S1 phenomenon can reach the admissible
  class at all.

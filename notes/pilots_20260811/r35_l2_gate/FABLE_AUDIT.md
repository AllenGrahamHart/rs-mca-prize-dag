# FABLE_AUDIT — r35_l2_gate (round 35, bank 1/4)

Auditor: coordinator (Fable). Date: 2026-08-11.
Verdict: **BANKED — R-L2 RESOLVED NONEMPTY, accepted as a THEOREM
(witness-checkable existence), with the strict-endpoint stake
re-priced by the pilot's MISS-2 flag (a coordinator forced
correction of my own round-34 close).** Node work: RESOLVED marker
on the round-34 close's R-L2 paragraph + the round-35 R-L2
addendum. No status flips; census unchanged.

## Verification (the decisive step)

- **Coordinator-INDEPENDENT witness check, from-scratch code**
  (scratchpad verify_l2_witness.py, zero pilot code): the
  published q=97 witness passes ALL checks — E1/E2 clearing
  identities; all four blocks of M(Z)Q_Z = 0 entrywise; degrees
  (7,7,7); s = deg gcd = 0; generic rank 7; rank-drop set exactly
  {z=10} with rank 6 there and full rank at infinity (delta = 1
  reduced, matching D-D); nullity(36x32) = 1; degree-<=1 kernel
  dimension 0 (e = 2 exactly). This is a second, independent code
  path — the strongest audit level available, stronger than
  replay.
- Pilot results files (d1-d4) consistent with every number quoted
  in the REPORT. The pilot's scripts were not replayed
  byte-for-byte (the independent verification supersedes replay
  for the headline; the D-B 120/120 and D-E 40/40 controls are
  internal to d1 and consistent).
- REPORT.md persisted via recover_report.py (WROTE verified,
  39,250 chars).

## Hand-checks (mathematics)

1. **11m-4:** 4m(m+1)-1 - (4m^2-7m+3) = 11m-4 — CHECK; positive
   at every m >= 1. The reading is honest: it is a heuristic
   ledger (the pilot flags pb_design_ceiling itself) whose one
   confirmed instance is m=2, where the witness makes it moot.
2. **Determinantal codim 5:** (36-31)(32-31) = 5 = (14-9)(10-9) —
   CHECK; the round-34 "+4" was an equation-count excess, and
   round 34's own MISS 2 already used q^-5 without drawing the
   consequence. The correction of my round-34 close reading is
   VALID and applied.
3. **DEF-ID identity:** (m+2)(4m+1) + m(3m-2) = 7m^2+7m+2 =
   (m-1)(7m-2) + 16m — CHECK exact. The coincidence verdict is
   sound (shapes incompatible; the shared quantity governs
   neither layer — both layers realizable despite positive
   deficits). Closed as posed.
4. **D-B/D-F structure:** the block split (B0/B3 rank 9 leaving
   the two locator spaces; the +4 in the cross blocks as
   5+5-14 = -4 in the [14,5] GRS code) and the 24x24 squareness
   at m=2 (12+12 cleared coefficients vs 24 curve coefficients)
   are coherent; the m=3 non-portability (80 vs 48) checks.
5. **MISS-2 triage (the round's board correction):** the PROVED
   node rate_half_ca_hankel_endpoint_residual_pole_interpolation_
   exclusion read in full — scope exactly as the pilot reported
   (strict A=3, e=m endpoint profiles, even m >= 6, official
   m = 2^37 covered; T=4m+1 with O <= m-1 hypotheses; scope
   section names what remains open). The pilot's m=2/T=0 witness
   is outside its hypotheses twice over — no contradiction. My
   round-34 close's "empty => strict endpoint closes outright"
   was over-priced (the official-row strict endpoint was already
   excluded); forced correction applied in the addendum and the
   RESOLVED marker. The header-level tension the pilot flagged is
   resolved: no conflict, only a mis-pricing.

## Honesty audit

Exemplary: D-D self-subtracted as banked-twice ((MI1) +
(SAT1)'s delta display); D3's deliverable reported as killed by
the pilot's own D2; the (SAT1)-(SAT5) table refused (vacuous at
T=0, not verified); the a* = 12 disagreeing witness reported
before the five agreeing; the sibling-name ls disclosed. The
"existence is a theorem" claim is correct as scoped (witness-
checkable; the five-field/no-Z-lift caveat is Z5 and declared).

## Compliance

Compute law CLEAN 4/4 (all local, documented timeouts; zero bare
python3 — fifth consecutive clean pilot). Upgraded write
discipline CLEAN (no sed/awk/perl/tee/redirection-onto-existing;
the new clause held on its first outing). Quarantine clean
(search-level excludes; sibling names seen via ls of the shared
parent, disclosed — same class as round-34's disclosure; ACTION:
round-36 CONSTRAINTS will pre-list sibling dir names so no ls of
the parent is needed). Write scope clean. Registrations followed
in order; no post-registration addenda.

## Mint queue additions

1. The (L2) nonemptiness theorem node (the witness family, the
   D-B criterion, the D-F inversion, the 11m-4 ledger with its
   heuristic grading, the excess/good component split).
2. The (SAT3)-on-(L2) gate as the target of record (design B so
   locators split over mu_32 at T = rho+2).
3. The board correction: R-L2's stake vs the residual-pole
   exclusion node (strict-endpoint accounting note).

## Round-36 anchors fed by this bank

(SAT3)-on-(L2) via the free B-parameters (THE instrument);
the m=3 inversion (new squareness needed); the endpoint a* on any
future supported-slope object.

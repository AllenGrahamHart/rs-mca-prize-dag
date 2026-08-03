# List-size terminus pilot — REPORT (2026-08-03)

(Coordinator-persisted; write harness-blocked. Replay: census PASS 0
violations / rows PASS / selection_gap PASS 0 P1 violations. PREREG
pre-dated; all six predictions resolved, P4 confirmed in kind.)

## VERDICT: the assigned target is FALSE and was ALREADY RETIRED

The "RS list-size bound at tau = k + ceil(h/2)" handed as the primary
surface was refuted 2026-08-02 (list_bound_transfer R1+R2; the KEY
LEMMA node's explicit non-claim; xr_band_occupancy FABLE_AUDIT
amendment). CONSOLIDATION UPDATE 3 and the ld_core_count report
carried the dead terminus forward — a REPEAT of the fifth-surface
subtraction failure.

Pilot output instead:
1. INDEPENDENT RE-DERIVATION of the refutation: critical depths
   d*_single/h = 0.8163/0.5496/0.6850 vs tau at 0.5000, inside the
   tangent gate (d* < h), high band generically empty (d*_joint/h =
   0.41/0.27/0.34 < 0.5) — reproducing the banked 0.55-0.82h / 0.41h
   / 2^(10^11) margins verbatim. Diagnosis: d*_joint = d*_single/2 —
   THEOREM 2 halves conditions-per-point, stepping over tau.
2. SHADOW LEMMA (proved): every raw joint-explanation pair of depth
   >= ceil(h/2) projects to a DISTINCT codeword at agreement >= k+d
   at EVERY member — so min_m L >= RAW_high: the min-over-members
   freedom buys exactly log2(q+1) = 256 bits against a ~1e12-bit
   deficit. Route (a) dead; refutation structural and
   selection-insensitive (4 toy fixtures: N_selected = 0 yet
   min L = 1). min_m L = RAW_high exactly in 8/8 fixtures.
3. LOCALISATION: the occupancy lemma survives MC by EXACTLY ONE DEPTH
   — MC populates d = h-1 (cascade tier) only, excluded from the band
   proper by BP(1)/BP(3) parity (h odd at all six rows). That margin
   is a proved theorem, not slack — and depends on h ODD.
4. AVERAGING LEDGER (proved, and proved useless): the exact
   sum-over-members identity gives min_m L <= R_j/((q+1)C(tau,j)) +
   D_j/C(tau,j), monotone in j, deficit ~1e12 bits at j = k+1; the
   optimistic second-moment variant misses by 1.10-1.75x and is
   KILLED-WITH-CERTIFICATE (a proof would contradict the first
   moment).

## Corrected primary surface + ranked sub-lemmas

PRIMARY (corrected): the UN-REDUCED two-slope band occupancy at
band-proper high depths [ceil(h/2), h-2] — the "positive target #1
species" label is STRUCK (the reduction that made it list-species is
what failed).
- SL-1 (RANK 1, the ONLY known repair): WINDOWED PROJECTION — do
  band-proper pairs project at agreement <= A-2 (never A-1/A)? If
  yes, THEOREM 2 upgrades windowed and MC no longer refutes it. SAME
  SPECIES as L-B over-agreement — unifies the lane's open surfaces.
  Falsifier: an admissible band-proper pair projecting at A-1/A at
  every member. Toy-testable now (census.py profile()).
- SL-2 (RANK 2, Pro-brief scale): UNSTRUCTURED HIGH-WINDOW EXCLUSION
  — can an unstructured admissible family reach a band-proper high
  depth with > 0.68n^2 members? (Structured half proved by
  BP(1)/BP(3); first moment gives margin.)
- SL-3 (RANK 3, diagnostic): shadow saturation = sub-criticality
  conjecture (why toy batteries can never exhibit the blow-up).
- SL-4: KILLED, do not spend.

## Flags: adjudication (stale surface, twice); h-even rows lose the
parity protection; 2 census fixtures fail the pencil gate (known
planting artifact, excluded); first moment is expectation (certified
refutation remains MC, consumed not re-derived); toy regime
sub-critical in principle (SL-3); q unpinned (<= 6-bit sensitivity).

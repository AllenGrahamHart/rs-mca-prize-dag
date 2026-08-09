# PREREG — umin_spike_hunt (round 26)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

Round 25 (z_n32_band) broke the N=32 wall and found the mechanism that
sets the band max: rare cells carrying low-weight mu_64-orbits (record
cells have UMIN = 9 against the typical 11; weights <= 12 supplied 48%
of the record's excess). Its 47-cell sample cannot see the tail of
~2.1e7 admissible kappa=1 primes, and the heuristic extrapolation puts
the band max at ~1.88 — ABOVE the N=16 record 1.7681. **Your job is
the named follow-on: hunt the spikes DIRECTLY. This is a
kill-or-confirm experiment on CONJECTURE Z-CEILING's decay direction.**
Sources to read FIRST: notes/pilots_20260809/z_n32_band/
{REPORT.md,FABLE_AUDIT.md,PREREG.md}; the round-25 addendum on
background/nodes/f2_z1_mass_knife_edge/statement.md.

## Deliverables

**D1 — THE TRIAGE INSTRUMENT.** wenum.py (in the z_n32_band dir —
REUSE, do not rewrite) computes exact AU[U] for U <= 12 at ~3x the
cost of a full BBM cell. Design and register a CHEAPER pre-filter if
one exists (e.g. AU[9] alone via truncated enumeration, or a
necessary condition on p for a weight-9 orbit to exist — think: when
does a norm equation Norm(w) = 0 mod p with |w|_1 = 9 have solutions?
An arithmetic characterization would replace enumeration entirely).
Price the instrument per prime BEFORE running. Register the triage
threshold (what AU profile promotes a cell to exact computation).

**D2 — THE HUNT.** Sweep as many admissible kappa=1 primes in
[2^30, 2^34] as the budget allows (register the target count from
your D1 pricing — the round-25 sample was 47; aim for orders of
magnitude more THROUGH THE FILTER, not exhaustively). Compute exact
CRATIO via BBM (reuse bbm.py + the 1402 checkpoint files — cells
already computed must not be recomputed) at every promoted cell.
Also register: the kappa=2 band deserves at least the 266-cell
exhaustive sweep round 25 declared post-hoc and never ran, if the
budget covers it (RC protection is weakest there and the official
row has kappa >> 1).

**D3 — THE VERDICT.** Three registered outcomes, decided in advance:
- Any cell with CRATIO > 2: Z-CEILING's C-form is DEAD (the ratio
  form's own bar). State it plainly.
- Any cell with CRATIO > 1.7681: the N-decay direction is REFUTED
  (the N=32 band max exceeds the exhaustive N=16 record); the
  round-24 repricing C >= 1.7681 moves up accordingly.
- Neither found through a filter that provably (or with measured
  recall) catches UMIN <= 10 cells: the strongest pro-decay evidence
  yet — quantify the filter's recall so the silence has a number.

**D4 — TWO-WAY VERIFICATION.** Every cell that enters the verdict
gets an independent re-derivation (BBM-ALT permutation/RBUCK variant,
as ver.py does). The round-25 standard: all verdict-bearing cells
two-way, disagreements = 0.

## Escape tests (run before the main work)

- Reproduce the record cell (p=4683696257: TNUM 11700545024, NKER
  392641, CRATIO 1.4210954721) and its AU profile (AU[9]=128,
  AU[10]=320, AU[11]=192, AU[12]=704) from the banked machinery.
- Verify your triage instrument FIRES on the two known UMIN=9 cells
  (p=4683696257, and the kappa=2 record p=63361) and stays silent on
  two known UMIN=11 cells — a power control on the filter itself.

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md at
  or below line 3872; do not read any other round-26 pilot dir
  (b_sparsity_pose, freeze_tail_law, m7_falsifier_hunt). Pass this
  clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root —
  including file patching and JSON peeking. RAMGUARD_TIMEOUT may
  extend a wall; document it.
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no bulk
  loads; checkpoint everything (extend ckpt/, do not duplicate);
  background batches with results files for >10-min runs. This box is
  shared — measure your throughput early and register the honest
  reachable count.
- DRAFT-ONLY: writes only in notes/pilots_20260809/umin_spike_hunt/
  (EXCEPTION: you may append new checkpoint files to
  notes/pilots_20260809/z_n32_band/ckpt/ since the format is shared —
  never modify existing ones); no dag/nodes/tools writes; no git; no
  Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing; misses
  first. Name every measured functional. The f2 calibration clause
  binds: all numbers are about the FORM of Z-CEILING, never about Z_1
  at the official row.
- Your final message IS the report. End with a compliance paragraph.

## Pilot registrations (appended by the pilot before any computation)

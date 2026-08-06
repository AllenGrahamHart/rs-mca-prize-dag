# PRE-REGISTRATION — ES-G-LANES: re-check all four consuming lanes against (ES-G)

Round 17, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation.

## 0. The re-pose being applied (source of record)

Round 16 split (ES) by reading: the PER-WEIGHT balance form
(Lam(w) := log2 C(n,r') - |Z_w| log2 p, round-15's) is REFUTED (five
sub-balance witnesses); the GLOBAL form (the u2c floor's q^t >= 2^n)
survives everything measured. The statement of record is now

> **(ES-G)**: global balance with the TRUE cyclotomic-closure size
> |Z_w| per row, imposed STRATUM-BY-STRATUM (a union of mu_{2^a}-
> cosets sees only the surviving conditions of the n/2^a instance;
> the binding stratum is not always a = 0).

Sources (read ALL, quote verbatim):
- `notes/pilots_20260806/es_boundary_adversary/REPORT.md` — the two
  readings (§1), the stratum mechanism (C4-a), the delta > 1 residual
  (C4-d: at the prize rows the balance STATUS ITSELF depends on the
  true |Z_w|, with verify_rows.py showing sign flips between the
  256-bit-prime and small-q_char ends), the coprimality mechanism
  (C4-c).
- `notes/pilots_20260806/es_boundary_adversary/FABLE_AUDIT.md` — the
  adopted (ES-G) re-pose.
- `notes/pilots_20260804/mun_anticoncentration/REPORT.md` (RECOVERED,
  now on disk) — §1 "THE UNIFIED STATEMENT" incl. the scope split
  (exact for crossing, strictly finer for band), §2 "THE ROW MAP",
  and how (ES) discharges all four consumers.
- The four lanes' own nodes: `critical/nodes/xr_band_fullrank_window_divisor_count`,
  `critical/nodes/rate_half_list_adjacent_crossing` (+ the crossing
  bracket in `notes/pilots_20260804/crossing_w2_opening/`),
  `critical/nodes/xr_band_forced_commonroot_syzygy_count` (BC routing:
  `notes/pilots_20260804/bc_block_census/REPORT.md`),
  `critical/nodes/u2c_giant_tnull_dichotomy` (whose banked re-pose is
  (ES) verbatim — check WHICH reading it actually pinned).

## 1. Pre-registered deliverables

- **(L1) True |Z_w| per row.** For each of the four lanes' rows of
  record (crossing bracket w in [2^34, 2^39]; three band rows; the
  u2c/dli RES row; the syzygy row), compute or bound the TRUE
  p-cyclotomic closure size |Z_w| under each admissible delta in
  {1,2,4} — exactly where closed-form, rigorous brackets otherwise
  (the round-15 bracket was [w-1, delta(w-1)]; sharpen it per row
  using the actual orbit structure of {1..w-1} mod n under
  multiplication by p, which for n = 2^41 and delta | 4 is explicit).
- **(L2) Global-balance status per lane per reading.** Decide, per
  row: is C(n,r') < p^{|Z_w|} (global sub-balance) — and does the
  answer flip across the admissible (p, delta) range as C4-d's
  verify_rows sign flip suggests? Exact integer/lgamma comparisons,
  both endpoints of every bracket.
- **(L3) The stratum condition per lane.** Identify each lane's
  stratum decomposition (which mu_{2^a}-coset unions are admissible
  members of its window system) and state the BINDING stratum. For
  the band instance (strictly finer than the cyclic-code slice) state
  precisely what "stratum" means there or why it does not apply.
- **(L4) The per-lane obligation under (ES-G), stated exactly.** For
  each lane: what (ES-G) must deliver, at which parameters, and
  whether the lane's row is in the regime where (ES-G) even applies.
  If any lane's row turns out ABOVE global balance at some admissible
  (p, delta), that lane CANNOT cite (ES-G) there — say so plainly and
  state what replaces it.
- **(L5) The u2c pin check.** Quote verbatim which balance functional
  u2c_giant_tnull_dichotomy pre-registered; confirm the round-16
  claim that its falsifier excludes the five witnesses; flag any
  drift between its wording and (ES-G).

## 2. Pre-registered falsifiers / honesty clauses

- If a lane's row is above global balance for ALL admissible (p,
  delta), that lane's routing to the terminal is BROKEN — report it
  as a routing defect, not a softer "needs care".
- If true |Z_w| cannot be pinned beyond the [w-1, delta(w-1)] bracket
  at some row, report the bracket and BOTH balance verdicts; do not
  pick the convenient end.
- No new balance functional may be introduced; the two on record are
  the only ones in play.

## 3. Rules of engagement

- DRAFT ONLY: write only inside `notes/pilots_20260806/es_g_lanes/`.
  Never touch dag.json, node shards, tools/, or push. Do NOT read
  `notes/pilots_20260806/es_coprimality/` (sibling this round).
- COMPUTE LAW: never bare python3; `tools/ramguard tiny -- python3 ...`
  (256M/60s) or `tools/ramguard local -- python3 ...` (1G/5min);
  literal `--`; run from repo root
  `/home/u2470931/smooth-read-solomin/prize`.
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — return the full report as your final
  message; the coordinator persists it verbatim.

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

---

# PILOT PRE-REGISTRATION (appended by the ES-G-LANES pilot BEFORE any computation)

Appended 2026-08-06 by the round-17 ES-G-LANES pilot, before running any
script. Everything below is mine; §0-§3 above are the coordinator's.

## 4. The two functionals, frozen (no third is introduced)

For a window system with condition count `c` over a value field of size
`V`, domain = subsets of the order-`n` group:

```text
PER-WEIGHT (round-15's, REFUTED as a statement):  Lam  := log2 C(n,r') - c*log2 V
GLOBAL     ((ES-G), the statement of record):     LamG := n            - c*log2 V
sub-balance  <=>  the functional is <= 0.
```

`GLOBAL => PER-WEIGHT` since `C(n,r') <= 2^n`. I introduce no other
functional. Where a lane's own pin uses a third quantity (e.g. a budget
`B` subtracted, as in `descent.py:211-213`), I say so and price it
separately rather than folding it in.

## 5. My model of `c` and `V` per lane (declared before computing)

- **Crossing** (prefix/cyclic instance, exact): the conditions are
  `p_s(T)=0, s=1..w-1` on 0/1 vectors, which are `F_p`-rational. The
  `F_p`-linear condition count is therefore `c = |Z_w| :=` the size of
  the closure of `{1,...,w-1}` in `Z/n` under multiplication by `p`
  (`dim C = n - |Z_w|`, `mun PREREG.md:60`), and `V = p`. NOT `q`:
  THEOREM Q (`crossing_w2_opening/REPORT.md:69-71`) proves the count
  depends on `q` only through `p`.
- **Band (full-rank)**: `c = 2d` generic `F_q`-linear forms, `V = q`.
  No cyclotomic closure exists (the window is not Galois-stable).
- **Band (syzygy / rank-deficient)**: `c = rank J_d = 2d - dim K_d < 2d`.
  I will report the BRACKET `[2d - (3d-2h-ell), 2d]` from (SL2-ABN) and
  BOTH verdicts, never the convenient end.
- **u2c**: `c = t`, `V = |B0| = |F_p(D)|` per CATCH #11, and `V = q`
  per the frozen falsifier wording; I report both.
- **dli RES**: `c = L_j`, `V` per CATCH #13 (generated field), read off
  the node; I report the row's own balance direction verbatim.

## 6. Pre-registered predictions (each with an explicit kill line)

- **(P1) `|Z_w|` closed form.** At `n=2^41`, `delta=ord_n(p) in {1,2,4}`
  and `w-1 < 2^38`, the seven non-identity `p`-classes give exactly five
  values of `|Z_w|/(w-1)`: `{1, 3/2, 2, 11/4, 3}`. **PREDICT: HOLDS.**
  KILL: any admissible `p`-class whose exact closure size differs from
  the closed form, or any brute-force disagreement at small `n`.
  Corollary predicted: the round-15 bracket top `delta(w-1)` is NOT
  attained for `delta=4` (max is `3(w-1) < 4(w-1)`). **PREDICT: HOLDS.**
- **(P2) Crossing sign flip is REAL and admissible.** There exist
  admissible official rate-1/2 rows (obeying `|F|<2^256`, `k<=2^40`,
  `n|q-1`, `p` prime, `q=p^e`) at which the crossing row `w=2^34` is
  ABOVE global balance. **PREDICT: FIRES.** KILL: every admissible row
  is sub-balance at `w=2^34`.
- **(P3) rate-1/16 band.** For the rate-1/16 band row, `2d*log2 q < n`
  at EVERY band-proper `d in [2^31+1, 2^32-1]` and every `q < 2^256`.
  **PREDICT: FIRES** (=> that lane cannot cite (ES-G) anywhere =>
  BROKEN routing per §2). KILL: some admissible `(q,d)` is sub-balance.
- **(P4) The binding stratum is the DEEPEST one, and it is unpayable.**
  For the crossing lane at `w=2^v`, the stratum `a=v-1` reduces to
  `n_a=2^{42-v}` with a single surviving condition, so global balance
  there needs `log2 p >= 2^{42-v}`; at `v=34` that is `log2 p >= 256`,
  which `|F| < 2^256` forbids. **PREDICT: FIRES at v in {34,35,36}.**
  KILL: the stratum-`a` reduction does not have `|Z^{(a)}|=1` there, or
  the deepest stratum is not the binding one.
- **(P5) u2c falsifier excludes all five round-16 witnesses.** Each of
  the five has `p^{|Z_w|} < 2^n`. **PREDICT: HOLDS.** KILL: any witness
  with `p^{|Z_w|} >= 2^n`.
- **(P6) The band `q >= 2^209` pin is a PER-WEIGHT threshold.** The
  banked `log2_q_critical = 208.47593052630532` equals
  `(log2 C(n,r') - log2(0.68 n^2))/(2d)` at `d = ceil(h/2)`, i.e. it is
  derived from the REFUTED functional, and the corresponding (ES-G)
  threshold `n/(2d)` is ~47.5 bits higher. **PREDICT: HOLDS.**
  KILL: reproduction misses the banked constant by more than 1e-6.

## 7. My own honesty clauses

- Every balance verdict is decided by EXACT integer/rational reasoning
  on `c*log2 V >= n`, using rigorous rational bounds for `log2 p`
  (never a bare float compare); any case whose margin is smaller than
  the certified error bar is reported as UNDECIDED, not resolved.
- Brackets are reported at BOTH ends with BOTH verdicts (§2 clause 2).
- `|Z_w|` closed forms are cross-validated against brute-force closure
  at small `n = 2^m` (m = 5..16) over ALL `p` of order 1,2,4; a single
  disagreement voids the L1 deliverable and I say so.
- Where a lane's obligation is only a RELAXATION of the cyclic form
  (mun REPORT.md:30-36), I do not silently transport the cyclic
  computation onto it.
- Reachable-scale caveat: nothing here is an extrapolation from the
  n in {16,32} census; all prize-row numbers are exact arithmetic at
  the prize parameters themselves.

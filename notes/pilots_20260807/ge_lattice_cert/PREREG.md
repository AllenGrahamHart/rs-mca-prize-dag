# PRE-REGISTRATION — THE DIM-64 LATTICE CERTIFICATION RUN (round 23)

Round 23, 2026-08-07. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: mystery 5's first
executable positive step. Round 22 proved the per-row GE-WEAK
certificate at N' = 128 is a dimension-64, radius-16 lattice
enumeration (~2^27.4 nodes LLL-only, ~2^10-2^17 with better
reduction). EXECUTE IT: certify kernel ternary emptiness at real
pinned rows, with checkpointing across the compute walls.

## 0. Sources (quote verbatim first; REUSE the round-22 machinery —
it is coordinator-replayed)
- notes/pilots_20260807/ge_floor_falsifier/{gelib.py, d4_cone.py,
  d4_price.py, REPORT.md} — the exact-rational LLL + Fincke-Pohst
  implementation, validated at h = 4, 8 against exhaustive brute
  force in BOTH directions.
- critical/nodes/lattice_cone_certificate/statement.md round-22
  addendum — the pricing of record + the production spec.
- critical/nodes/integer_code_distance_cert/statement.md — the
  system of record (K_p, ternary, support <= 2l', the antipodal
  cyclotomic relations) + "no hidden finite registry" (the
  universality residue — you are NOT closing it; you are
  certifying pinned rows).
- THE ROW LIST: derive from the frozen prize spec + the deployed
  row registry which primes p = 1 mod 128 the campaign actually
  needs certified (the official/deployed rows the generator_economy
  and kernel-lattice consumers quantify over — quote the spec rows
  with file:line; if the spec pins few rows, certify all of them;
  if it pins a family, certify the named representatives and say
  exactly what remains).

## 1. Deliverables
- (D1) THE ROW LIST with provenance (file:line per row).
- (D2) VALIDATION FIRST: re-certify the round-22 boundary cells
  (h = 8: p = 463249 must yield its 2 witnesses with Norm = p;
  p = 463457 must certify EMPTY; the C-4 anchor cells) — your
  pipeline must reproduce all of them EXACTLY before any dim-64
  run is trusted.
- (D3) THE RUN: for each row, exact integer LLL (deep insertions /
  iterated reduction as needed — stdlib only) then a COMPLETE
  Fincke-Pohst enumeration of {w != 0 : ||w||_inf <= 2} in the
  folded kernel lattice Lambda_p (dim 64, det p), with
  per-coordinate box pruning. CHECKPOINTING IS MANDATORY: the
  ramguard local wall is 5 minutes — design the enumerator to
  serialize its DFS state to YOUR OWN dir and resume across
  invocations; never run bare python3 to dodge the wall. Each
  certificate = the reduced basis + the node count + the empty (or
  witness) result + a fail-closed mutation control (a deliberately
  planted vector must be FOUND by the same code path).
- (D4) THE HONEST LEDGER: rows certified / rows attempted-not-
  finished (with exact node counts + projected cost) / rows out of
  reach. Plus the universality statement of what per-row
  certificates do NOT close (quote integer_code_distance_cert).

## 2. Falsifiers / honesty
- If a prize-row enumeration finds a WITNESS (nonzero ternary
  kernel vector in the box): that is a MAJOR event — GE-WEAK's
  emptiness expectation fails at that row. Verify the witness
  exactly (Norm divisibility, unfolded support), report with a
  standalone reproduction script, and STOP the campaign line for
  the coordinator to re-pose. Register this response in advance.
- A run that cannot finish is reported with its exact state, not
  extrapolated to a verdict.

## 3. Rules
- DRAFT ONLY in notes/pilots_20260807/ge_lattice_cert/. Never edit
  dag.json/nodes/tools; no git; no Modal; no package installs
  (stdlib only — fplll is NOT available; the round-22 exact
  implementation is your base). COMPUTE LAW: every python3
  invocation via tools/ramguard tiny|local -- python3 ... (literal
  --), from repo root, INCLUDING file patching and JSON peeking;
  checkpoint files live in your own dir. Name every measured
  functional (CATCH-19C). Verbatim quotes with file:line. No
  REPORT.md — your final message IS the report. QUARANTINE: do not
  read notes/pilots_20260802/CAMPAIGN_LEDGER.md at or past line
  2786 (the "ROUND 23 LAUNCHED" marker); do not read the other
  round-23 pilot dirs (cw_shared_target, fpc5_diag, c2pp_diag);
  PASS THIS QUARANTINE CLAUSE VERBATIM to any subagent you
  dispatch.

# PILOT REGISTRATIONS

Appended 2026-08-07 by the round-23 ge_lattice_cert pilot BEFORE any
computation (no python3 has been run in this pilot at the time of
this append; only Read/grep/ls of the sources above and of the row
registry). Everything below is pre-committed.

## P0. Named measured functionals (CATCH-19C)

- `FPNODES(cell)`  — enumeration nodes visited by my Fincke-Pohst DFS
  (implementation-dependent; reported as measured, never treated as a
  canonical constant, never compared to round-22's counts as if the
  two enumerators were the same program).
- `FPFOUND(cell)`  — the exact set of nonzero w in the declared box
  found in the lattice.
- `LLLSWAPS(cell)`, `LLLSEC(cell)` — swap count / wall seconds of the
  exact integer LLL.
- `GSPROFILE(cell)` — the vector (log2 ||b*_i||^2)_{i<n} of the final
  basis, exact rational, printed rounded.
- `RHF(cell)` = (||b_0|| / det^{1/n})^{1/(n-1)} — realised root
  Hermite factor of the final basis.
- `BOXCOUNT(h,L)` = #{w in {-2..2}^h : ||w||_1 <= L}, exact DP.
- `CLASSHEUR(cell)` = (BOXCOUNT(h,L) - 1)/p — the expected number of
  nonzero folded box classes in the kernel. This is the round-22
  CATCH-1-corrected heuristic (classes, not unfolded multiplicity).
- `GHRATIO(cell)` = R / lambda_1^GH with R^2 = min(4h, 2L),
  lambda_1^GH = sqrt(n/(2 pi e)) * p^{1/n}.
- `MAXNORMCEIL(h)` = (4h)^{h/2}, the rigorous AM-GM norm ceiling.
- `DETCHECK(cell)` in {PASS, FAIL} — |det B| = p by exact Bareiss.
- `MEMBERCHECK(cell)` in {PASS, FAIL} — every final basis row w has
  w(rho) = 0 mod p.

## P1. Row-list derivation plan (registered before deriving it)

Selection rules, applied in this order:

- **R1 (PINNED rows).** A row is IN iff some DAG node makes a literal
  folded-kernel certificate over an explicitly printed (field, root,
  quotient order N', box) its own payload. These are the rows a
  consumer actually quantifies over at a pinned constant.
- **R2 (DEPLOYED-CHARACTERISTIC extension rows).** Real deployed prize
  characteristics p that satisfy p = 1 mod N' but that no node pins to
  an N'-folded cell are certified as EXTENSION rows and are labelled
  EXTENSION everywhere. They are the strongest available test of the
  pipeline against genuinely deployed constants, and they are the rows
  nearest the norm ceiling; they are NOT claimed to discharge any
  consumer.
- **R3 (PRICED-NOT-RUN rows).** Rows whose folded dimension h exceeds
  64 are priced (GHRATIO, CLASSHEUR, FP model) and explicitly NOT run.
  I register in advance that I expect these to be out of reach and
  that I will say so rather than start and extrapolate.
- **R4 (FAMILY residue).** If the spec pins a family (interval +
  congruence) rather than a finite list, I quote the sentence that
  does so with file:line and state exactly what per-row certificates
  leave open, quoting `integer_code_distance_cert`.

Provenance discipline: every row carries file:line for its prime, its
root, its N', and its box/support bound. A row whose prime I cannot
quote from a repo file is not a row.

## P2. Validation gates. ALL must PASS before any dim-64 result is
reported as a certificate.

- **G1 (round-22 boundary cells, both directions).** My pipeline must
  reproduce `d4_cone.py`'s six rows with the SAME witness counts and
  the SAME witness sets: (h=4,p=137,L=8) -> 2 witnesses;
  (4,401,8) -> 0; (8,12289,6) -> 0; (8,12289,16) -> 6;
  (8,463249,16) -> 2 with Norm = p exactly; (8,463457,16) -> 0.
  Node counts MAY differ (different reduction, different DFS order)
  and are reported, not gated.
- **G2 (C-4 anchor).** N'=16, p=12289, support <= 6, order-16 root:
  576 cyclotomic kernel vectors (= 288 up to global sign) and 0
  non-cyclotomic, reproduced by direct unfolded enumeration.
- **G3 (brute force, both directions).** At h = 4 and h = 8 the
  enumerator's witness SET must equal the exhaustive box sweep's
  witness set, at a cell of each verdict.
- **G4 (basis soundness).** For every reported cell: DETCHECK = PASS
  and MEMBERCHECK = PASS. A basis that fails either voids the cell.
- **G5 (fail-closed mutation control).** See P3. The control must be
  run at the SAME dimension and determinant as the certified cell,
  through the SAME code path, and must return NONEMPTY.

If any gate fails I report the failure and withhold the dim-64
verdict.

## P3. The fail-closed mutation control, specified exactly

`PLANT-C(h, p, v)`: let v be a nonzero vector in {-2..2}^h. Pick
c_1..c_{h-1} uniformly in [0,p), pick an index t with v_t invertible
mod p, and solve c_t = -(sum_{j != t} v_j c_j) * v_t^{-1} mod p, with
c_0 normalised to 1 by scaling (so the co-cyclic lattice
Lambda^c = { w in Z^h : sum_j w_j c_j = 0 mod p } has determinant
exactly p). By construction v is in Lambda^c.

Then run the IDENTICAL basis-build -> integer LLL -> Fincke-Pohst code
path on Lambda^c with the same radius and box, and REQUIRE that v is
in FPFOUND. This is a same-dimension, same-determinant, same-radius,
same-code-path control whose answer is known to be NONEMPTY. A run
whose control does not find its planted vector is reported as a FAILED
control and its companion emptiness claim is withdrawn.

Rationale for choosing a co-cyclic plant rather than a planted prime:
constructing a prime p with a known box witness would require
factoring a ~2^250 norm, and constructing a planted ideal lattice
would change the determinant. PLANT-C changes only the linear
functional, which is exactly the input my code path consumes.

Additionally, at h = 4 and 8 I run PLANT-C against brute force
(G3), so the control is itself validated where validation is cheap.

## P4. Checkpointing design (registered)

- Every long-running stage (integer LLL; Fincke-Pohst) writes a JSON
  state file under `notes/pilots_20260807/ge_lattice_cert/state/`.
- Each state file carries `problem_hash` = sha256 of the canonical
  problem tuple (h, p, root, R2, L, basis-construction tag). Resume
  ABORTS if the hash differs; a checkpoint is never silently reused
  across problems.
- **Self-imposed soft wall.** Each invocation stops voluntarily at
  `SOFT_WALL = 235 s` under `ramguard local` (300 s hard) and 45 s
  under `ramguard tiny` (60 s hard), saves, and exits 0 with status
  `RUNNING`. I never raise `RAMGUARD_TIMEOUT`; the wall is a design
  constraint. If a process is nevertheless killed by the hard wall,
  the last checkpoint is authoritative and the nodes since it are
  RE-DONE, so counts stay exact (no double counting: the resume
  restarts from the saved DFS frontier, and `FPNODES` is stored in
  the same atomic write as the frontier).
- The DFS state serialized is: the level index, the full coefficient
  vector x, the per-level enumeration windows already consumed, the
  accumulated partial sums, `FPNODES` so far, and `FPFOUND` so far.
  Writes are atomic (temp file + os.replace).
- Determinism: the DFS visits coefficients in a fixed ascending order
  at every level (no randomised zig-zag), so `FPNODES` is a
  deterministic function of the problem and the basis, and is additive
  across resumes.

## P5. Registered predictions (pre-committed, before any run)

- **Q1.** The pinned N'=128 cell (p = 904625697166646869347790708689
  937759412227977745095982970820953353127723009, rho_128, box
  {-2..2}^64) certifies EMPTY. Basis: CLASSHEUR = (5^64-1)/p =
  2^-101.4.
- **Q2.** FPNODES at that cell, with an LLL-only basis, lands in
  [2^14, 2^27.4]. Round-22's GSA model says 2^27.4 and reports itself
  as over-predicting by 2-3x at the cells where it was validated, so I
  predict strictly below it.
- **Q3.** The four deployed Proth prize primes (167-171 bits) at the
  same N'=128 full-box cell also certify EMPTY (CLASSHEUR = 2^148.6/
  2^167 = 2^-18.4 at the smallest), but cost at least 2^15 times more
  nodes than Q1's cell, and I register in advance that one or more of
  them may be OUT OF REACH inside this pilot's compute law.
- **Q4.** The deployed clean-anchor rows sit at quotient order
  N' in {256, 512}, i.e. folded dimension h in {128, 256}. I predict
  GHRATIO > 1 at all six and CLASSHEUR >> 1 at the rate-1/4 rows
  (N'=256, ell'=65) — i.e. witnesses EXPECTED there — and I predict
  all six are out of reach. These are R3 rows: priced, not run.
- **Q5.** No witness is found at any h = 64 cell; the positive line
  stays closed and P6 is not triggered.
- **Q6.** RHF of my exact integer LLL at n = 64 lands in
  [1.018, 1.030].

Each prediction is reported CONFIRMED / FALSIFIED / UNRESOLVED
against its outcome.

## P6. Witness-response protocol (registered in advance)

If any prize-row or pinned-row enumeration returns a nonzero
w in {-2..2}^h inside the declared box:

1. **STOP the positive line immediately.** No further rows are run.
   The verdict for every other row stays whatever it was at that
   moment, reported with its exact state.
2. **Verify exactly and independently of the enumerator:**
   (a) w != 0 and ||w||_inf <= 2;
   (b) sum_j w_j * rho^j = 0 mod p by direct modular arithmetic from
       the PINNED root constant, not from the lattice basis;
   (c) `tower_norm(w) % p == 0` via the round-22 exact 2-adic tower
       norm, plus `tower_norm(w) != 0`;
   (d) ||w||_1 <= 2l' for the row's declared support bound, and print
       the unfolded ternary v in {-1,0,1}^{N'} that realises w
       (v_j = +1 where w_j > 0 etc., splitting |w_j| = 2 across the
       antipodal pair), then verify sum_a v_a rho^a = 0 mod p
       directly;
   (e) report the rotation/Galois orbit of w (the folded box is stable
       under x -> x^s for odd s and under negacyclic shift, so a
       witness comes with up to 2h * phi(2h)/... conjugates; I print
       the orbit size actually observed).
3. **Standalone reproduction script.** Write
   `witness_repro.py` in my own dir taking only the literal constants
   (p, rho, w) and re-verifying from scratch with zero imports from my
   library, runnable under `tools/ramguard tiny -- python3`.
4. **Report as the headline**, name it as the registered falsifier of
   `e1_folded_no_vector_certificate_128_payload`'s falsifier clause
   ("A nonzero non-cyclotomic folded vector in the displayed `N'=128`
   field/root"), and make NO status flip and NO closure claim — the
   coordinator re-poses.
5. State explicitly whether the witness contradicts anything BANKED
   (in particular `PRO_W3_e1_density.md:49`'s "The N'=128 zero cert
   already HELD, lambda_1 = 31.67 > 16").

## P7. Honesty rules

- No status flips, no closure claims; certificates and verdicts only.
- Any run that does not finish is reported with its exact FPNODES, its
  resume state, and a projected cost — never extrapolated to a
  verdict.
- Node counts from my enumerator are NOT comparable to round-22's
  `d4_cone.py` counts (different reduction, different DFS); I report
  both and say so.
- Prior-art subtraction before any novelty claim: the observation
  `lambda_1 > 16 at N'=128` is BANKED at
  `background/nodes/e1_folded_no_vector_certificate_256_payload/
  PRO_W3_e1_density.md:49`, and round-22 already claimed only its
  price. I claim neither; what I can claim is only the COMPLETE
  enumeration transcript, which the repo itself rules is what is
  missing (`critical/nodes/.../status_ruling.md:12`, quoted in the
  round-22 report: "The prior BKZ observation was explicitly
  inconclusive.").
- Every python3 invocation goes through `tools/ramguard tiny|local --`
  from the repo root, including file peeking. Writes confined to
  `notes/pilots_20260807/ge_lattice_cert/`.
- QUARANTINE held: `notes/pilots_20260802/CAMPAIGN_LEDGER.md` is not
  read at or past line 2786; the round-23 pilot dirs
  `cw_shared_target`, `fpc5_diag`, `c2pp_diag` are not read. The
  clause is passed verbatim to any subagent dispatched.

## P9. AMENDMENTS (appended AFTER computation began -- flagged as post-hoc,
## not pre-registered)

Registered honestly as amendments rather than silently folded into P2-P4.

- **A1 (added gate G6, SHARD EQUIVALENCE).** The original design was a
  single-process enumerator. During the E1-128 run I added exact
  DFS-subtree sharding to use more than one core. Sharding was NOT
  pre-registered, so I added gate **G6**: for every validation cell and
  five (nshard, sdepth) configurations, the sum of the shards' FPNODES
  must equal the single-process FPNODES EXACTLY and the union of the
  shards' FPFOUND must equal the single-process FPFOUND EXACTLY.
  `shardtest.py`. A dim-64 sharded verdict is reported only if G6 passes.
- **A2 (G1 restated).** G1 as registered said my pipeline must reproduce
  round-22's boundary cells. It does not: round-22's published witness
  COUNTS are wrong on three of six rows (CATCH-23A). G1 was restated to
  gate on (i) my witness SET == the exhaustive brute-force set and (ii)
  my VERDICT == round-22's verdict, with round-22's counts reported
  alongside as a delta. The restatement was forced by evidence, is
  strictly stronger (brute force is ground truth), and is disclosed here
  rather than in the report only.
- **A3 (discarded work).** A 246,022,144-node unsharded E1-128 partial
  enumeration was abandoned when sharding was introduced; the sharded run
  is a fresh COMPLETE enumeration and does not reuse it. The abandoned
  state is kept at `state/E1-128.unsharded-partial.json`.
- **A4 (deep-insertion LLL, abandoned).** `improve.py` (deep-LLL) was run
  as an experiment and reached FPEST 2^29.43 from 2^30.88. It is NOT used
  for any reported certificate; every reported dim-64 basis is the plain
  escalating-delta integer LLL basis in `state/CELL.lll.json`.
- **A5 (behaviour-preserving optimisation mid-run).** The enumerator's
  centre computation was changed from a Python loop to a C-level
  map/sum. Gates were re-run and returned IDENTICAL node counts
  (30, 4, 76, 1096, 80, 58) and identical witness sets.
- **A6 (added cells).** `CORRIDOR-128` (a deployed 256-bit prime already
  free by the PROVED high-field branch -- run as an independent check of
  that theorem) and `CORRIDOR-128-CONJ` (the same cell at a Galois-
  conjugate root -- an independent replication) were not in the original
  row plan. Both are labelled EXHIBIT / REPLICATION, not prize rows.

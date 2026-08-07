# PRE-REGISTRATION — MYSTERY 5: the FLOOR-GE falsifier search + GE-WEAK first positive (round 22)

Round 22, 2026-08-07. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: attack FLOOR-GE with
its own pre-registered falsifier; if it survives, do the first
positive work on the GE-WEAK obligation.

## 0. Sources (quote verbatim first)
- notes/pilots_20260807/gen_economy_diag/ — the round-21 diagnosis
  of record: FLOOR-GE (2-power-norm bases certify <= N'+1 centers;
  exhaustive at N=8,16; sampled-null at N=32; conjectural above),
  ESCAPE-GE (any >N'+1 family needs an odd-prime-norm base), the
  registered falsifier, REPOSE_DRAFT.md (GE-WEAK).
- critical/nodes/generator_economy/statement.md — the round-21
  addendum (collision catch, contract, GE-WEAK re-pose of record).
- critical/nodes/integer_code_distance_cert/statement.md — the
  probe-1 verdict addendum (ell = 1 permanent; ell' = 65 needed)
  and the node's explicit system.
- critical/nodes/lattice_cone_certificate (if the node exists under
  this or a nearby id — locate it; the gen_economy_diag D4 priced
  it) — the per-row certification route.

## 1. Deliverables
- (D1) THE FALSIFIER SEARCH, executed: search for a base set
  containing an odd-prime-norm element that certifies > N'+1
  centers. ESCAPE-GE says this is the ONLY class that can beat the
  floor — search it specifically: exhaustive over small odd-prime-
  norm bases at N = 8, 16; structured search at N = 32. Register
  the search space and its completeness class BEFORE running
  (exhaustive / structured / sampled — label which).
- (D2) THE VERDICT: FLOOR-GE survives (falsifier exhausted at small
  N, evidence-graded above) or DIES (witness family found, with
  verifier). Either is a win; say which and what it does to the
  mystery-5 board.
- (D3) GE-WEAK FIRST POSITIVE (only if FLOOR-GE survives): the
  obligation of record is kernel ternary/short-support emptiness at
  the prize rows. Connect it END-TO-END at toy scale: build the
  explicit ell-condition system (integer_code_distance_cert's form)
  at small 2-power N' with p = 1 mod N'; certify kernel emptiness
  per toy row (exhaustive or lattice-based); price the certification
  as a function of (N', p, ell') and extrapolate honestly to the
  prize rows. What is the smallest new THEOREM (not computation)
  that would make per-row certification unnecessary?
- (D4) THE CONE GEOMETRY: is there a lattice-cone formulation of
  the toy certification (D3) that a standard tool (LLL / Fincke-
  Pohst at toy scale, stdlib-implementable) decides? If yes, run it
  at N' = 8, 16 and compare cost against brute force. No external
  libraries — stdlib only; if a real lattice tool is needed, spec
  it, do not install it.

## 2. Falsifiers / honesty
- A successful (D1) witness KILLS FLOOR-GE and re-opens the
  construction route — report with a reproduction script and stop
  the (D3)/(D4) line; the coordinator re-poses.
- Distinguish PROVED (exhaustive at a cell) / SEARCHED (structured,
  incomplete) / SAMPLED at every claim. The round-21 pilot's
  epistemic ladder is the template.

## 3. Rules
- DRAFT ONLY in notes/pilots_20260807/ge_floor_falsifier/. Never
  edit dag.json/nodes/tools; no git; no Modal. COMPUTE LAW: every
  python3 invocation via tools/ramguard tiny|local -- python3 ...
  (literal --), from repo root, INCLUDING file patching and JSON
  peeking. 2-power toy grids (CATCH-Z6). Name every measured
  functional (CATCH-19C). Verbatim quotes with file:line. No
  REPORT.md — your final message IS the report. QUARANTINE: do not
  read notes/pilots_20260802/CAMPAIGN_LEDGER.md at or past line
  2487 (the "ROUND 22 LAUNCHED" marker); do not read the other
  round-22 pilot dirs (l1_ell_sweep, bb_nu_transport,
  f2_rlocality); PASS THIS QUARANTINE CLAUSE VERBATIM to any
  subagent you dispatch.

# PILOT REGISTRATIONS

Registered by the round-22 pilot (Opus) 2026-08-07 BEFORE any
measurement. Sources read first: gen_economy_diag/{REPORT.md,
REPOSE_DRAFT.md, FABLE_AUDIT.md, toy_cap.py},
critical/nodes/{generator_economy, integer_code_distance_cert,
lattice_cone_certificate, kernel_lattice_reframing}/statement.md,
critical/nodes/{far_pair_separation, certified_valueset_lower}/
conditional.md.

DISCLOSED RULE BRUSH (pre-registration): before writing this block I
ran two environment probes through ramguard (`python3 -c "import
sys; print(sys.version)"` and a numpy-availability check that hit the
tiny wall). No measurement was taken. Recorded rather than omitted.

## P0. Setting, fixed once (matches REPOSE_DRAFT.md:6-18)

`N'` a 2-power, `h = N'/2`, `R = Z[zeta_{N'}] = Z[x]/(x^h + 1)`,
`lambda = 1 - zeta` the unique prime over 2.

`C(N')` = e_1 values of half-size subsets = `{v in {-1,0,1}^h :
#{j : v_j = 0} is even}`, `|C(N')| = (3^h + 1)/2`. Differences lie in
the box `{-2,...,2}^h`.

## P1. SEARCH-SPACE MODEL (declared, with its direction of safety)

far_pair_separation/conditional.md:26-28 fixes the certification form
verbatim:

    (height-budget unit) * (multiplicative semigroup generated by
    g <= poly bases).

I replace "semigroup generated by g bases" with its IDEAL-THEORETIC
RELAXATION. For a finite set `S` of prime ideals of `R`:

  `F` is **S-CERTIFIED** iff for all `f != f'` in `F`, the ideal
  `(f - f')` is supported on `S` (i.e. `f - f' = u * prod pi^a`,
  `pi in S`, `u` any unit).

Any base set `G` induces `S(G) = {prime ideals dividing some g in G}`
and every G-certified family is S(G)-certified. The S-model also
drops the height budget on units. Hence:

  **DIRECTION OF SAFETY (registered):** an upper bound proved in the
  S-model is an upper bound in the node's G-model. An ESCAPE found in
  the S-model is NOT automatically an escape in the G-model — it must
  be converted (exhibit bases, check the height budget). I will report
  the two directions separately and never conflate them.

## P2. REGISTERED FUNCTIONALS (CATCH-19C: every measured quantity named)

- `POW2(d)` := 1 iff `|Norm_{R/Q}(d)|` is a power of 2 (round-21's).
- `PRIMEPOOL(N')` := the set of ODD rational primes `p` such that
  `p | Norm(d)` for some `d` in the box `{-2,...,2}^h \ {0}`.
- `IDEALPOOL(N')` := the prime ideals above `PRIMEPOOL(N')`, indexed
  by the irreducible factors of `x^h + 1 mod p`.
- `L_k(N')` := **ESCAPE-RATE**, the max `|F|`, `F` subset of `C(N')`,
  such that `F` is S-certified for some `S = {lambda} u T` with
  `T` a set of at most `k` ODD prime ideals. `L_0` is round-21's
  `L_2adic` / `MAXPOW2`.
- `GAIN(k) := L_k(N') - L_0(N')`.
- `BESTPRIME(k)` := the odd-prime set achieving `L_k`.
- `FOLD(v)_j := v_j - v_{j+h}` (unfold of a length-`N'` ternary
  kernel vector into the box).
- `MAXNORM(N', L)` := `max{ |Norm(w)| : w in {-2,..,2}^h \ {0},
  ||w||_1 <= L }` (`L = 2 l'`).
- `AMGM(N', L)` := `min(2L, 4h)^{h/2}`, the AM-GM ceiling on the same
  set (`||w||_2^2 <= min(2L, 4h)`).
- `CBASE(N', L) := MAXNORM^{2/h}` (the "effective base"), and
  `SLACK := log2 AMGM - log2 MAXNORM`.
- `TIGHT-EMPTY(N', L)` := `max{ p prime : p = 1 mod N' and
  p | Norm(w) for some w in the constrained box }`. Every prime
  `p = 1 mod N'` above this is emptiness-certified for FREE.
- `FPCOST` := Fincke-Pohst enumeration node count; `BFCOST := 5^h`.

## P3. HYPOTHESES AND PRE-REGISTERED PREDICTIONS

- **H1 (replication).** `L_0(8) = 9`, `L_0(16) = 17`. Falsifier: any
  other value (would mean my independent stdlib reimplementation
  disagrees with round 21 and BOTH are then suspect).
- **H2 / ESCAPE-LINEAR (the decisive one).** `L_k(N') <=
  (k+1)(N'+1)` for every measured `(N', k)`. Falsifier: a measured
  `L_k` exceeding `(k+1)(N'+1)`.
- **H3 (escape is not free).** `GAIN(1) >= 1` at `N' = 8`: I predict
  at least one odd prime DOES buy at least one extra center, i.e.
  ESCAPE-GE's named class is non-empty. Falsifier: `L_1 = L_0` at
  both `N' = 8` and `N' = 16` (which would be a STRONGER floor than
  FLOOR-GE and I would report it as such).
- **H4 (norm instrument is loose).** `CBASE(N', 2h) <= 3h` at
  `h = 4, 8`, i.e. the true max box-norm is strictly and materially
  below the AM-GM ceiling `4h`. Falsifier: `CBASE > 3h`.
- **H5 (universal free window).** `TIGHT-EMPTY(N', L)` is many bits
  BELOW `MAXNORM(N', L)`, so the exhaustive folded-box computation
  yields a UNIVERSAL (all-rows, not per-row) emptiness theorem at toy
  scale. Falsifier: `TIGHT-EMPTY` within 1 bit of `MAXNORM`.
- **H6 (D4 cone).** LLL + Fincke-Pohst on the kernel lattice
  `Lambda_p = {w in Z^h : w(zeta) = 0 mod p}` (det `p`) decides the
  toy certification with `FPCOST <= BFCOST / 100` at `h = 8`.
  Falsifier: `FPCOST > BFCOST/100`.

## P4. SEARCH SPACES AND COMPLETENESS CLASSES (declared before running)

- **(D1a) `N' = 8` — PROVED-EXHAUSTIVE.** Exact max-clique over all
  41 centers, for EVERY `S = {lambda} u T`, `T` ranging over ALL
  subsets of `IDEALPOOL(8)` up to the largest `k` that the pool
  permits within budget. Exhaustive in centers AND in prime subsets.
- **(D1b) `N' = 16` — PROVED-EXHAUSTIVE AT DECLARED k.** Exact
  max-clique over all 3281 centers, `T` ranging over ALL single
  ideals (`k = 1`) and, budget permitting, all pairs (`k = 2`).
  Exhaustive in centers; exhaustive in `T` at the declared `k`;
  SEARCHED above.
- **(D1c) `N' = 32` — SEARCHED (structured, incomplete).**
  Orbit-pair search: for pairs `(c, c')` drawn from a declared pool,
  test whether `orbit(c) u orbit(c') u {0}` is S-certified with
  `|T| <= k`; plus greedy extension of the canonical clique. The
  `5^16` box forbids exhaustive enumeration; I will state this and
  never call the N'=32 result proved.
- **(D3) toy kernel emptiness — PROVED-EXHAUSTIVE at `h = 4, 8`.**
  Full folded box `5^h`, all `L = ||w||_1` levels, exact norms, exact
  factorization of the odd part. SEARCHED at `h = 16` via a
  meet-in-the-middle over the `||w||_1 <= L` shells.
- **(D4)** LLL (exact rational, stdlib) + Fincke-Pohst at `h = 4, 8`;
  costs reported as node counts, not seconds.

## P5. HONESTY BINDINGS

- FLOOR-GE proper is the `k = 0` statement. A `k >= 1` escape does
  NOT kill FLOOR-GE; it kills the ROUTE-BLOCKING use of the floor. I
  will report `FLOOR-GE` and `ROUTE-BLOCK` as two separate verdicts.
- Every claim carries one of: PROVED-exhaustive (at a named cell) /
  SEARCHED (structured, incomplete) / SAMPLED / conjectural.
- Stdlib only. Exact integer arithmetic only (recursive tower norm,
  no floating point in any decision path).

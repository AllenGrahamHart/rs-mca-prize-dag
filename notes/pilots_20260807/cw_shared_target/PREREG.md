# PRE-REGISTRATION — THE CONSTANT-WEIGHT INSTRUMENT AS THE SHARED TARGET OF MYSTERIES 2 AND 4 (round 23)

Round 23, 2026-08-07. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: round 22 ended with
FOUR lanes converging on one instrument cluster. Price the
constant-weight cell as ONE target: state both consumers' exact
needs side by side, derive the weakest common form (or prove the
overlap is a shape-pun), and run the first attack on whichever form
survives.

## 0. Sources (quote verbatim first)
- Mystery 4's need: notes/pilots_20260807/bb_nu_transport/
  {REPORT.md, PROOFS.md} — the crux after PROPOSITION U2:
  Acc_shallow + aperiodic S = a constant-weight population cap for
  BCH_w in a prescribed sig class, via the banked LEMMA Y/MW
  equality W_w = BCH_w at w <= p (locate the Y/MW source in
  notes/pilots_20260804/crossing_w2_opening/); plus the ternary
  relation set R (#R ~ 3^L/Q measured, weight enumerator upper
  bound = the sharp deep-stratum route).
- Mystery 2's need: notes/pilots_20260807/f2_rlocality/
  {REPORT.md, PROOFS.md} D4 + the round-22 addendum on
  background/nodes/f2_z1_mass_knife_edge/statement.md — the
  non-local obligation: "no codeword of the GRS value code C* is
  unusually smooth", quantifying over Theta(S) coordinates, and
  under the finite target essentially EXACT (the 4.77-bit window).
- The instrument side: the constant-weight Z-FLOOR cell (grep for
  the CW-FLOOR theorem / constant-weight Z-FLOOR node id in
  critical/ and background/ — quote its exact statement); the
  round-22 addendum on
  critical/nodes/rate_half_list_adjacent_crossing (statement_
  addenda/14) for U2's Ramanathan/Lehmer machinery; THEOREM Z-2's
  l1-restricted moment supply (nodes of record).
- critical/nodes/integer_code_distance_cert/statement.md round-22
  addendum (the convergence-point declaration).

## 1. Deliverables
- (D1) THE TWO CONTRACTS, EXACTLY: for each mystery, the precise
  statement it needs — functional (named), quantifiers, row
  region, precision (mystery 2: essentially exact; mystery 4:
  which margin below B*), and what each banked partial supplies.
  A table, no prose hand-waving.
- (D2) THE SHARED-FORM VERDICT (the round-19 gates, graded
  honestly): OBJECT (same functional on the same code?), REGIME
  (overlapping rows/parameters?), METHOD (does one proof shape
  serve both directions?). NO unification language unless all
  three pass. If the overlap is partial, state the weakest COMMON
  strengthening that implies both, and whether it is plausibly
  true (test it at toy scale BEFORE proposing it).
- (D3) THE FIRST ATTACK on the surviving form: what do the banked
  instruments give — the CW-FLOOR theorem itself, U2's
  prescribed-sum machinery (which is exact and two-sided on its
  domain), Z-2 moments, the ternary suppression instruments?
  Registered predictions per attempt; exhaustive toy cells
  (2-power grids, p = 1 mod 2L rows matching the round-22 cells so
  the banked numbers cross-check); adversarial: also SEARCH for a
  counterexample to the shared form at toy scale before believing
  it.
- (D4) THE VERDICT FOR THE BOARD: one shared target (with re-pose
  draft + registered falsifier) or two separate targets (with the
  exact divergence point named). Either is a win; say which.

## 2. Falsifiers / honesty
- A toy-scale counterexample to the proposed shared form kills the
  unification — report it with a reproduction script and propose
  the split instead.
- The round-21 L_1-vs-B_C countermodel and round-22 THEOREM AT are
  the warnings of record: name every functional; no inequality
  transfer without its own proof.

## 3. Rules
- DRAFT ONLY in notes/pilots_20260807/cw_shared_target/. Never
  edit dag.json/nodes/tools; no git; no Modal. COMPUTE LAW: every
  python3 invocation via tools/ramguard tiny|local -- python3 ...
  (literal --), from repo root, INCLUDING file patching and JSON
  peeking. 2-power toy grids (CATCH-Z6); no shift-0 cells
  (CATCH-19B); name every measured functional (CATCH-19C).
  Verbatim quotes with file:line. No REPORT.md — your final
  message IS the report. QUARANTINE: do not read
  notes/pilots_20260802/CAMPAIGN_LEDGER.md at or past line 2786
  (the "ROUND 23 LAUNCHED" marker); do not read the other
  round-23 pilot dirs (fpc5_diag, ge_lattice_cert, c2pp_diag);
  PASS THIS QUARANTINE CLAUSE VERBATIM to any subagent you
  dispatch.

---

# PILOT REGISTRATIONS

Opus 5, 2026-08-07, appended BEFORE any computation (no `python3`
has been invoked in this session at the time of writing; the only
tools used so far are Read/Bash-grep and one read-only search
subagent, which was passed the quarantine clause verbatim).

## §R0. Named functionals (CATCH-19C)

Every quantity I will measure, named here first. `p` prime,
`Q = p^e`, `T := {0,+1,-1}^N` the ternary cube, `supp` the support,
`wt(eps) := |supp(eps)|` (= the l1 weight for ternary vectors).

- `TMASS(D) := sum_{eps in D cap T} 2^{-wt(eps)}` — the **ternary
  theta at 1/2** of an F_p-subspace `D <= F_p^N`. This is exactly
  f2's `Z(L)` with `D = L^perp`
  (`f2_z1_mass_knife_edge/statement.md:18`).
- `TMASSBAL(D)` — same sum restricted to *balanced* eps
  (`#{+1} = #{-1}`).
- `AU(D,U) := #{eps in D cap T : wt(eps) = U}` — the ternary
  weight enumerator. `UMIN(D) := min{U > 0 : AU(D,U) > 0}`.
- `USTAR(D) := argmax_U AU(D,U)*2^{-U}` — the **dominating weight**
  of the theta.
- `HEUR(N,kappa) := 1 + (2^N - 1)/p^kappa` — the random-code value
  of TMASS at codimension `kappa` (the quantity THEOREM Z-FLOOR
  bounds from below: `2^m / p^{dim L}`).
- `CRATIO(D) := TMASS(D)/HEUR(N,kappa)` — the **ceiling ratio**.
  Z-FLOOR (proved, pointwise) says `CRATIO >~ 1`; the shared form
  under test is an upper bound on `CRATIO`.
- `SIGMA(N,kappa,p) := N - kappa*log2 p` — the **saturation
  exponent** `= log2` of the heuristic ternary theta mass above 1.
- `RSET(L,p,e)` := bb_nu_transport's relation set
  `R = {eps in {0,+-1}^L : sum_{j<L} eps_j theta^j = 0 in F_Q}`,
  `theta` of exact order `2L`.
- `GW(L,r',U) := C(L-U,(r'-U)/2)/C(L,r'/2)` — LEMMA TC's normalized
  fibre weight; `GDEV(L,r',U) := GW(L,r',U)*2^U` — its deviation
  from mystery 2's weight `2^{-U}`.
- `FIB(L,r',D) := sum_{eps in D} C(L-U(eps),(r'-U(eps))/2)` — the
  deep-stratum population; `ACC := FIB - C(L,r'/2)` (the accident
  count; bb's `N_acc`).
- `WCODE(n,p,theta) := {x in {0,1}^n : sum_i x_i theta^i = 0}` with
  `|x| = r'` — the primal constant-weight population at `w = 2`,
  `n = 2L`; `NW := |WCODE|`.
- `COLL(n,r',D) := sum_{eps in D cap T, balanced} C(n-U, r'-U/2)` —
  the collision (L2) upper bound on `NW^2`.
- `L2LOSS := 0.5*log2(COLL) - log2(NW)` — the bits lost by the
  collision/Cauchy-Schwarz step.
- For the mystery-2 toy: `ZTOY(p,S,R) := TMASS(C^perp)` on the
  `[S,S-R,R+1]_p` negacyclic GRS code with `Lambda = {1,3,...,2R-1}`
  (exponent 0 never occurs — CATCH-19B).

## §R1. The two contracts as I read them (to be checked in D1)

- **M2 (f2) contract.** UPPER bound on `TMASS(L^perp)` at
  `N = m = S = 2.75e11`, `kappa = dim L = R`, `R/S = 1/log2 p`,
  `p >= 2^39`. Proved floor `2^{17.98}` (exact-balance reading);
  finite target `Z(L) <= 1 + N^3 = 2^{22.75}`. **Tolerance above its
  own proved floor: 4.77 bits.** `SIGMA = +46.02` (the knife-edge
  constant Delta).
- **M4 (crossing) contract.** UPPER bound on `X_w(gamma)`; budget
  `B* = 2^127.5098`; banked proved floor `2^73.061`. **Tolerance
  above its own proved floor: 54.45 bits.** Two sub-needs:
  **M4-b** (sharp deep stratum) = upper bound on the ternary
  relation weight enumerator of `RSET`, `N = L = 2^{41-v} <= 128`,
  `kappa = e`; **M4-a** (the LIVE crux) = constant-weight population
  cap for `BCH_w` in a prescribed sig class, `N = n = 2^41`,
  `kappa = w-1 = 2^35-1`, covering `Acc_shallow` + aperiodic `S`.

## §R2. Hypotheses under test

- **H1 (OBJECT).** M4's deep-stratum functional and M2's `Z_1` are
  the *same* functional up to the explicit ratio `GDEV(L,r',U)`,
  i.e. `FIB(L,r',D) = C(L,r'/2) * sum_{eps in D} GDEV(U)*2^{-U}`
  with `GDEV in [1, poly(L)]` and `GDEV -> 1` as `U/L -> 0`.
- **H2 (the shared form, to be proposed only if it survives).**
  **TMASS-CEILING**: on the 2-power grid there is an absolute
  constant `C` with `TMASS(D) <= C * HEUR(N,kappa)` for every
  admissible `D`. This is the exact upper companion of the proved
  THEOREM Z-FLOOR.
- **H3 (the predicted divergence).** Three named gaps: (i)
  DIRECTION — the banked instrument on the named bridge (THEOREM
  CW-FLOOR, `es_ternary_suppression_instruments/statement.md:92-97`)
  is a **lower** bound, while both consumers need an **upper**
  bound; (ii) L2 LOSS — M4-a reaches the shared functional only
  through a collision/Cauchy-Schwarz step that recovers half the
  suppression exponent (`p^{-kappa/2}` not `p^{-kappa}`), which M2
  does not pay because its terminal *is* the theta; (iii) REGIME —
  `N` and `kappa` differ by ~9 and ~7 orders of magnitude, and the
  two consumers sit on opposite sides of `SIGMA = 0`.
- **H4.** M4's *live* crux (M4-a) is NOT supplied by H2; only M4-b
  is, and M4-b is not on M4's critical path because the trivial
  ternary bound `TMASS <= 2^L` already gives U1 `= C(2L,r') =
  2^{124.08} < B*`.
- **H5 (dominating weight).** M4's theta is MINIMUM-weight
  dominated (`USTAR = UMIN`, small); M2's is BULK dominated
  (`USTAR = Theta(N)`).

## §R3. Registered predictions (with falsifiers)

- **Q1.** `GDEV(L,L-2,U) in [1,1.6]` for every admissible `U` at
  `L in {8,16,32,64,128}`, increasing in `U`; specifically
  `GDEV(64,62,2) = 1.0149 +- 0.001`. *Falsifier:* `GDEV` outside
  `[1,2]` anywhere, or non-monotone ⇒ H1's "same functional"
  reading needs a correction factor and I will state it.
- **Q2.** `ACC` computed from `RSET` reproduces bb_nu_transport's
  banked `N_acc` **exactly** at all 12 of its cells
  (L=8: p=17→416, 97→80, 113→16, 193→16, 241→0; L=16: p=97→4848608,
  193→2432064, 257→1823616, 353→1332800, 449→1042272, 577→808256,
  641→744128). *Falsifier:* any mismatch ⇒ my reconstruction of the
  object is wrong and every downstream number is void.
- **Q3.** `CRATIO(RSET) <= 2` at every 2-power cell
  (`L in {4,8,16}`, `p = 1 mod 2L`, `p < 2000`). *Falsifier:* a cell
  with `CRATIO > 2` ⇒ H2 is false as stated and I report the
  counterexample plus the corrected form.
- **Q4 (adversarial, expected to FIRE).** At a composite-`2L` cell
  (`3 | 2L`), `CRATIO` grows without bound in `p` (p-independent
  cyclotomic ternary relations, CATCH-Z6). Predict `CRATIO > 100`
  at `L = 6, p > 500`. *Falsifier:* `CRATIO` bounded there ⇒ the
  2-power hypothesis is not load-bearing for H2 and I must say so.
- **Q5.** `USTAR(RSET) = UMIN(RSET) in {3,4}` at (L=16, p=97);
  `USTAR(ZTOY) >= S/2` at the M2 toy (p=17,S=8,R=2). *Falsifier:*
  either one reversed ⇒ H5 dead.
- **Q6.** `L2LOSS >= 0.40 * kappa * log2 p` at the `w=2` toy cells
  (`n = 2L`, `kappa = 1`), i.e. the collision route recovers at most
  ~half the suppression. *Falsifier:* `L2LOSS < 0.1*kappa*log2 p`
  ⇒ H3(ii) is wrong and M4-a may after all ride the shared form.
- **Q7.** `TMASS(RSET)` at the official witness row is heuristically
  `1 + 2^64/2^{255.5} = 1 + 2^{-191.5}`, i.e. `SIGMA = -191.5 < 0`,
  while M2 has `SIGMA = +46.02 > 0`. Exact arithmetic check only.
- **Q8.** THEOREM CW-FLOOR's own criterion `C(L,r'/2) > p^{delta_a}`
  fails at the witness row by `3.85` bits (banked); I predict the
  recomputation gives `3.85 +- 0.05` at `v = 35`, `p = 3*2^41+1`.
  *Falsifier:* a different number ⇒ I flag it as a forced
  correction candidate, not a claim.

## §R4. Toy cells declared (2-power grids; CATCH-Z6, CATCH-19B)

- **CELL-M4a:** `L in {4,8,16}`, `n_a = 2L`, `r'_a = L-2`,
  `p = 1 mod 2L` prime, `e = 1`, `theta` of exact order `2L`.
  Exhaustive over `3^L` (meet-in-the-middle at `L = 16`).
  `p` lists exactly matching bb_nu_transport's cells plus a sweep
  `p < 2000` for the adversarial search.
- **CELL-M4b (`w = 2` primal):** `n = 2L`, `L in {4,8}`,
  weight-`r'` 0/1 vectors with `sum_i x_i theta^i = 0`; exhaustive.
  Used for `NW`, `COLL`, `L2LOSS`.
- **CELL-M2:** negacyclic GRS toy, `(p,S,R) in {(17,8,2),(97,16,2),
  (97,16,4)}`, `Lambda = {1,3,...,2R-1}` (no exponent 0).
  Exhaustive / MITM over `3^S`.
- **CELL-ADV (invalid-by-CATCH-Z6, used only to show the
  hypothesis is load-bearing):** `L = 6` (so `2L = 12`, `3 | 2L`),
  `p = 1 mod 12`, sweep.

## §R5. Honesty / subtraction commitments

- **Subtraction (hard law 5), disclosed up front.** The
  identification of LEMMA TC's fibre weight with a
  difference-multiplicity weight is **already banked** as G2.1:
  `notes/pilots_20260806/crossing_gap/REPORT.md:79-85` — *"the
  constant-weight collision multiplicity `C(L−U, W−U/2)` at
  `W+W' = r'` is identically LEMMA TC's fibre size
  `C(L−U,(r'−U)/2)` ... the exact constant-weight analogue of
  THEOREM Z-FLOOR, with the cube `2^L` replaced by the shell
  `C(L,r'/2)` and the difference-multiplicity weight `2^{L−U}`
  replaced by LEMMA TC's binomial."* I claim **no novelty** for
  H1's shape; what I claim is the quantitative ratio `GDEV`, the
  side-by-side contract pricing, and the graded verdict.
- I will name every functional, quote every source with file:line,
  and transfer NO inequality without its own proof (round-21
  L_1-vs-B_C countermodel; round-22 THEOREM AT).
- I will not use unification language unless OBJECT, REGIME and
  METHOD all pass. If any fails I report the divergence point.
- No status flip, no closure claim, no node edit.

---

# OUTCOMES (appended AFTER computation, 2026-08-07)

Artifacts in this directory: `cw.py` -> `CENSUS.txt` (106 PASS / 25 FAIL),
`attack.py` -> `ATTACK.txt` (12/3), `adv.py` -> `ADV.txt` (7/1),
`consist.py` -> `CONSIST.txt` (5/0).  Total 130 PASS / 29 FAIL; **every FAIL
is a registered-prediction miss or a strictness-threshold miss, not a
verifier error** — they are listed as such below.

| reg. | outcome |
|---|---|
| Q1 | **SPLIT.** Monotonicity HELD at L=8..128; `GDEV(64,62,2)=1.014881` HELD. The band `[1,1.6]` **FALSIFIED** at L=32/64/128 (max 1.8980 / 2.5951 / 3.6073). Corrected law: `max_U GDEV(L,L-2,U) = 2^{L-2}/C(L,L/2-1) = Theta(sqrt L)`. |
| Q2 | **HELD, 12/12 exactly** (bb_nu_transport's `N_acc` reproduced from an independent code path). |
| Q3 | **HELD.** `CRATIO <= 1.2610` over every swept 2-power cell of BOTH families (L in {4,8,16} to p<200000/20000; M2 toys to p<30000). |
| Q4 | **FALSIFIED as registered.** Composite `2L` gives `CRATIO` only 1.51 (L=6) / 1.27 (L=12) below p=2000, never >100. But in the EXCESS normalization it reaches **178.51** at L=6, p=19993, growing linearly in p. CATCH-Z6 is load-bearing for the EXCESS form, not for the CRATIO form. |
| Q5 | **FALSIFIED, both clauses.** M4: `USTAR = 8 = L/2` (bulk) at L=16, not `UMIN=3`. M2 (G1): `USTAR = 0`. Corrected law (same in both families): `USTAR` is governed by `SIGMA` — bulk `N/2` when `SIGMA >> 0`, `eps=0` when `SIGMA < 0`. H5 dead. |
| Q6 | **SPLIT.** Fraction `L2LOSS/(kappa log2 p)` measured in `[0.3120, 0.4993]`, mean 0.4069 at L=8 — never above 1/2. The registered threshold 0.40 fails at 4/8 L=8 cells; all 12 L=4 cells are degenerate (`RSET={0}`, `NW` = structural fibre only) and the registered form does not apply there. The D-section conclusion uses the most favourable measured fraction and is robust. |
| Q7 | **SPLIT.** `SIGMA(v=35, witness) = -191.5098` under the `kappa=e` reading HELD; but `kappa = e` was **WRONG** (see SC-1). Under the corrected `kappa = delta_a = 1`, `SIGMA(v=34, witness) = +85.415 > 0`. The "SIGMA<0 at every official row" clause is FALSE. |
| Q8 | **HELD but MIS-REGISTERED by me.** `3.85` reconstructs as `128 - log2 C(128,63) = 128 - 124.1491 = 3.8509` at **v=34**, reference `log2 p = 128`; my PREREG guessed v=35 / the witness p. |
| H1 | **HELD** with the corrected ratio (Q1). |
| H2 | **SPLIT.** The EXCESS form with an absolute constant is **FALSIFIED at toy scale**: `(S,R,p) = (16,2,3137)` gives EXCESS = **2.3463 > 2**, and the values do not look bounded. The weaker CRATIO form survives every swept cell with `C <= 1.2610`. |
| H3 | (i) HELD (CW-FLOOR and Z-FLOOR are both LOWER bounds; both consumers need UPPER). (ii) HELD, quantified: >= 4.57e11 bits vs a 54.45-bit tolerance. (iii) HELD but with the corrected `kappa`. |
| H4 | **HELD.** `U1 = C(128,62) = 2^124.0820 < B* = 2^127.5098` at v=35: the trivial ternary bound already suffices; the sharp route is optional except at v=34. |
| H5 | **DEAD** (see Q5). |

**SC-1 (my own defect, forced correction to my own work).** `attack.py`
Section B used `kappa = e` (the extension degree) for the deep-stratum
relation set. The correct codimension is `kappa = delta_a = 1` on every
break-region row (`p = 1 mod n_a`, so `theta in F_p`; bb_nu_transport's own
"the measured U2 loss factor tracks `Q = p`"). Found because the wrong value
made the proposed ceiling contradict banked THEOREM BB at v=34; the
contradiction is what located the error. `consist.py` is the corrected
section, and with `kappa = 1` the ceiling is CONSISTENT with THEOREM BB
(slack 11.8400 bits) and de-vacuums v=34 only at the `e=1` prime rows
(+2.0947 bits), exactly the rows BB provably cannot reach.

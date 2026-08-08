# PRE-REGISTRATION — CONJECTURE Z-CEILING: THE ASSAULT (round 24)

Round 24, 2026-08-08. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: Z-CEILING is the
board's highest-payoff conjecture (if true with C < 2^4.77 it
closes mystery 2's finite target with 4.44 bits of headroom).
Attack it in its WORST directions; if it survives, sharpen it
toward a proof on tractable subfamilies. Either outcome is a win:
a counterexample saves us from chasing a false theorem; survival
plus partial proofs builds the case.

## 0. Sources (quote verbatim first)
- background/nodes/f2_z1_mass_knife_edge/statement.md — the
  round-23 addendum (the conjecture of record in its RATIO form:
  Z(L) <= C*(1 + 2^m/p^dim L) on the 2-POWER grid; the sharp
  EXCESS form is ALREADY FALSIFIED at (S,R,p) = (16,2,3137) with
  EXCESS 2.3463 growing along SIGMA -> -infinity — do not re-pose
  it; the load-bearing 2-power hypothesis: composite 2L drives
  EXCESS to 178.51, linear in p; the normalization pin).
- notes/pilots_20260807/cw_shared_target/ — the round-23 machinery
  (REUSE: cw.py, adv.py — coordinator-replayed), the 7,000+-cell
  survival at C <= 1.2610, THEOREM Z-FLOOR (the proved lower
  companion), the official-row consistency datum (the official
  ternary theta sits 11.84 bits BELOW its volume heuristic).
- THEOREM Z-1/Z-2 (the l1-restricted moment supply) and the
  admissibility definitions in the f2 nodes of record.

## 1. Deliverables
- (D1) THE WORST-DIRECTION HUNT (falsification): the EXCESS
  counterexample family (32 weight-11 vectors at (16,2,3137))
  is the known enemy shape. Push the RATIO form where that family
  and its relatives are strongest: (a) follow the SIGMA -> -inf
  family lines to larger S and larger p (does CRATIO grow past
  1.2610 -> past 2 -> unboundedly, or saturate?); (b) STRUCTURED
  adversarial subspaces (not just row sweeps): design L to
  concentrate ternary kernel mass — use the known counterexample's
  structure as the seed; (c) THE BOUNDARY: walk from the 2-power
  grid toward composite 2L in controlled steps (which arithmetic
  feature of 2-power-ness carries the conjecture? p-free
  cyclotomic relations are the composite killer — find the exact
  gate). Registered predictions per direction BEFORE running.
- (D2) THE CONSTANT'S LAW: is C <= 1.2610 an artifact of swept
  ranges? Fit and REGISTER a growth law for max CRATIO as a
  function of (S, kappa, p) on the admissible grid; test it
  out-of-sample. If C grows without bound along any admissible
  direction, the conjecture is DEAD even without a single cell
  crossing a fixed constant — say so.
- (D3) THE SHARPENING (only if (D1)/(D2) do not kill it): proof
  attempts on tractable subfamilies, in order: (a) the
  second-moment/ensemble-average version (the banked factor-2
  calibration suggests the ENSEMBLE form may be provable — prove
  E_L[Z] and Var_L[Z] bounds over the admissible family exactly);
  (b) fixed small codimension (kappa = 1, 2: is Z-CEILING a
  theorem there? The kernel is a single hyperplane section —
  possibly exactly computable); (c) the weight-truncated form
  (Z restricted to wt <= W — Z-2's moments control low weights;
  where exactly does control run out?). Label every partial:
  PROVED / PROVED-AT-CELL / CONJECTURAL.
- (D4) THE VERDICT + the re-posed conjecture of record (if it
  needs re-scoping, e.g. a kappa-dependent or S-dependent C), with
  a registered falsifier.

## 2. Falsifiers / honesty
- A cell with CRATIO > 2 (double the banked calibration) is a
  MAJOR event — verify exactly, write a standalone reproduction
  script, report as the headline.
- Census evidence is evidence, never proof. The calibration
  clause of the f2 node binds: no toy is evidence about Z_1 at
  the official row — every toy number is about the FORM.

## 3. Rules
- DRAFT ONLY in notes/pilots_20260808/z_ceiling_assault/. Never
  edit dag.json/nodes/tools; no git; no Modal. COMPUTE LAW: every
  python3 invocation via tools/ramguard tiny|local -- python3 ...
  (literal --), from repo root, INCLUDING file patching and JSON
  peeking. 2-power grids of record; composite cells ONLY as
  declared boundary probes (CATCH-Z6); no shift-0 cells
  (CATCH-19B); name every measured functional (CATCH-19C).
  Verbatim quotes with file:line. No REPORT.md — your final
  message IS the report. QUARANTINE: do not read
  notes/pilots_20260802/CAMPAIGN_LEDGER.md at or past line 3173
  (the "ROUND 24 LAUNCHED" marker); do not read the other
  round-24 pilot dirs (kernel_window_hunt, t_petal_lemma,
  c2pp_gb_probe); PASS THIS QUARANTINE CLAUSE VERBATIM to any
  subagent you dispatch.

# PILOT REGISTRATIONS

Appended 2026-08-08 by the Opus pilot BEFORE any computation. Every
number below is derived by hand/analytically from the two source
files quoted in section 0; nothing here has been measured yet. Where
I predict a banked number I have NOT yet looked it up in the
round-23 output files (CENSUS.txt/ADV.txt/REPORT.md) — the
predictions are made from the node statement alone.

## R0. NAMED FUNCTIONALS (CATCH-19C)

All on a cell = (family, N, kappa, p) with p prime, p == 1 mod 2N,
p > 2N. Coefficient vectors:
- family M2 (negacyclic GRS of record, I1): N = S coordinates,
  kappa = R rows, row_i = (w^{(2i-1)e})_{e=0..S-1}, w of exact order
  2S, Lambda = {1,3,...,2R-1} (all-odd, 0 NOT in Lambda: CATCH-19B
  asserted in code).
- family M4 (RSET / crossing deep stratum, I2): N = L coordinates,
  kappa = 1, row = (th^j)_{j=0..L-1}, th of exact order 2L,
  Lambda = {1} (0 not in Lambda: CATCH-19B asserted in code).

- `TMASS(cell)` = Z(L) = sum over eps in ker ∩ {0,±1}^N of
  2^{-wt(eps)}; the eps = 0 term contributes 1.
- `H(N,kappa,p)` = (2^N - 1)/p^kappa.   `HEUR` = 1 + H.
- `CRATIO` = TMASS / HEUR.   (the RATIO form of record)
- `EXCESS` = (TMASS - 1)/H = (TMASS-1) p^kappa/(2^N-1).  (FALSIFIED
  form; measured only as a diagnostic / for banked-number replay)
- `SIGMA` = N - kappa*log2 p.   (log2 H to O(2^{-N}))
- `ZFRATIO` = TMASS/(2^N/p^kappa)  (Z-FLOOR slack).
- `AU[U]` = ternary kernel weight enumerator; `UMIN` = least U>=1
  with AU[U] > 0.
- `PFREE(n)` = the char-0 ("p-free") ternary relation set
  {eps in {0,±1}^{n/2} : sum_j eps_j z^j = 0 for z a primitive
  n-th root of unity in C}; `PFMASS(n)` = sum over PFREE of 2^{-wt}
  (so PFMASS >= 1 always, = 1 iff PFREE = {0}).
- `RELDIM(n)` = n/2 - phi(n)  (rank of the p-free relation lattice).
- `SMOOTH(cell)` = sum_{u in F_p^kappa, u != 0} prod_{j}
  cos^2(pi <u, col_j>/p)   (the non-trivial smoothness mass; see R6).
- `MAXCR(N,kappa,band)` = max CRATIO over the swept cells in a band.

## R1. THE ALGEBRAIC IDENTITY THAT RE-AIMS THE HUNT (registered as a
##     forced self-correction of the brief's direction D1(a))

Identity (trivial, but decisive): with H = (2^N-1)/p^kappa,

    CRATIO = (1 + EXCESS*H)/(1 + H),

so **CRATIO > 2  <=>  EXCESS > 2  AND  H > 1/(EXCESS - 2)**.

Consequence I register now: the brief's direction D1(a) ("follow the
SIGMA -> -inf family lines") is aimed at the regime where the RATIO
form is structurally SAFE — as p grows at fixed (N,kappa), H -> 0 and
CRATIO -> 1 no matter how large EXCESS gets. The known EXCESS
counterexample (S,R,p) = (16,2,3137) has SIGMA = 16 - 2*log2 3137 =
-7.2725, H = 65535/3137^2 = 0.00665955.

- **P1a.** CRATIO(16,2,3137) = **1.0089** +- 0.0010.  (Not a threat.)
- **P1b.** max CRATIO over the whole SIGMA<0 arm of the M2 sweep
  (S=8 and S=16, R=2, p up to 20000) is **< 1.05**.
- **P1c.** The correct worst direction for the RATIO form is the
  OPPOSITE one: SIGMA -> 0^+ and SMALL N. I predict the round-23
  record CRATIO = 1.2610 was attained at the SMALLEST N in the swept
  grid with SIGMA near 0 — concretely at **(M4, N=4, p=17)**
  (SIGMA = -0.0875) or failing that at (M4, N=8, p in {193,241}).
  I have not looked; this is checkable by re-running the banked code.

## R2. D1(b) — STRUCTURED ADVERSARIAL SUBSPACES

- **P2a (rigidity).** Inside the admissible family the subspace is
  essentially UNIQUE per cell: replacing w by w^t (t odd, so
  gcd(t,2S)=1) permutes coordinates and flips signs, and TMASS is
  invariant under both. PREDICTION: TMASS is bit-identical across all
  phi(2S) primitive 2S-th roots at every test cell. Hence there is NO
  design freedom in (b) beyond (S,R,p) and Lambda.
- **P2b (Lambda relaxation, DECLARED BOUNDARY PROBE, not
  admissible).** Non-consecutive all-odd Lambda of the same size
  keeps CATCH-19B but breaks the GRS/MDS shape. PREDICTION: max
  CRATIO over all all-odd Lambda of size R at fixed (S,R,p) exceeds
  the consecutive value at some cell, but stays **< 2** for S <= 16.
- **P2c (SCOPE PROBE — the word "admissible" is load-bearing).**
  For a GENERAL F_p-subspace the ratio form is trivially false: take
  L = span{(1,1,...,1)}. Since |sum eps_j| <= N < p the condition is
  the INTEGER condition sum eps_j = 0, so
  TMASS = sum_{U even} C(N,U) C(U,U/2) 2^{-U}, p-independent.
  At N = 8 this is exactly 50.2734375, and at p = 257
  PREDICTION: **CRATIO = 25.23 +- 0.05**, unbounded in p.
  This does NOT falsify Z-CEILING (that vector is not an admissible
  parity row) — it is registered as evidence that the statement of
  record must PIN "admissible", since the companion THEOREM Z-FLOOR
  is stated for "EVERY F_p-subspace" (statement.md:17-18) while
  Z-CEILING says "every admissible F_p-subspace" (statement.md:186)
  with the pin only implicit at statement.md:13-15.

## R3. D1(c) — THE COMPOSITE BOUNDARY, THE EXACT GATE

Credited upstream FIRST (hard law 5, subtraction): the gate itself is
ALREADY BANKED as **CZ-M** in background/nodes/tern_master_threshold/
statement.md:37-38 — "char-0 emptiness iff n is a 2-power (CATCH-Z6
upgraded to a rank statement, count 3^{N-phi(n)} - 1)". I claim only
the CRATIO/EXCESS *quantification* below.

Registered derivation (pen and paper, to be verified):
sum_j eps_j z^j = 0 for z primitive n-th root <=> Phi_n(x) divides
sum_j eps_j x^j, deg < n/2. So RELDIM(n) = n/2 - phi(n), and
RELDIM = 0 <=> phi(n) = n/2 <=> n is a 2-power. For n = 2^a*3
(a >= 2): Phi_n(x) = x^{n/3} - x^{n/6} + 1 has ternary coefficients
and its n/6 shifts x^i*Phi_n (i = 0..n/6-1) have PAIRWISE DISJOINT
supports {i, i+n/6, i+n/3} inside [0, n/2). Hence every {0,+-1}
combination is ternary, |PFREE| = 3^{n/6}, matching CZ-M's
3^{n/2-phi(n)} exactly, and

    **PFMASS(2^a*3) = (1 + 2*2^{-3})^{n/6} = (5/4)^{L/3},  L = n/2.**

- **P3a.** lim_{p->inf} EXCESS(L,1,p)/p = (PFMASS-1)/(2^L - 1).
  At L = 6 (n = 12): PFMASS = (5/4)^2 = 1.5625, |PFREE|-1 = 8,
  slope = 0.5625/63 = 0.00892857, so
  PREDICTION **EXCESS(6, 19993) = 178.51 +- 0.02** — an exact
  closed-form reproduction of the banked number at
  statement.md:198-199.
- **P3b.** lim_{p->inf} CRATIO(L,1,p) = PFMASS(2L) exactly, and
  CRATIO(L,1,p) ~= (PFMASS + H)/(1 + H).
- **P3c (THE GATE IS NOT A TECHNICALITY).** sup_p CRATIO over
  composite cells is UNBOUNDED: (5/4)^{L/3} -> inf. First composite
  cell that breaks CRATIO > 2: **n = 24, L = 12**, PFMASS =
  (5/4)^4 = 2.44140625, |PFREE| = 3^4 = 81. At the least prime
  p == 1 mod 24 above 10^6, H = 4095/p ~= 0.0041, PREDICTION
  **CRATIO = 2.4355 +- 0.03, and > 2**.
  Cross-check cell n = 48, L = 24: PFMASS = (5/4)^8 = 5.96046,
  |PFREE| = 3^8 = 6561, RELDIM = 24 - 16 = 8.
- **P3d.** On the 2-POWER grid PFREE = {0} so PFMASS = 1 and
  CRATIO -> 1 as p -> inf at fixed N. Therefore *no* 2-power
  counterexample can live at SIGMA << 0. Registered as the reason the
  hunt must go to SIGMA ~ 0.

## R4. D2 — THE CONSTANT'S LAW (registered growth model + its
##     out-of-sample test)

Model (second moment of TMASS under the random-code null, derived
now): if kernel membership were p^{-kappa}-random then
E[TMASS] = 1 + H exactly, and, using that eps and -eps are perfectly
correlated (pair factor 2),
    Var(TMASS) = 2 p^{-kappa} ((3/2)^N - 1).
Hence
    **SD(CRATIO) = sqrt(2) * 2^{-0.20752*N} * g(SIGMA)**,
    **g(sigma) = 2^{sigma/2}/(1 + 2^sigma)**, max g = 1/2 at sigma=0,
with the exponent -0.20752 = (1/2)log2(3/2) - 1 + 1/2 registered to
5 decimals. Extreme-value form over M cells in a bin:
    **MAXCR - 1 ~= A * sqrt(2) * 2^{-0.20752 N} * g(SIGMA)
                    * sqrt(2 ln M)**, A = O(1) fitted.

- **P4a (the DEATH condition, registered).** If the measured
  exponent of (MAXCR - 1) in N, at fixed SIGMA-bin, is >= 0 — i.e.
  the record constant does not decay as N grows — Z-CEILING is DEAD
  and I will say so even with no single cell above 2. PREDICTION: the
  measured exponent lands in **[-0.30, -0.12]** (model: -0.2075).
- **P4b (SDTEST, the strong test).** For every (family, N, kappa,
  SIGMA-bin) with >= 8 cells, measure sd(CRATIO) and form
  RSD = measured/model. PASS if RSD in [0.5, 2.0] for >= 80% of bins.
- **P4c (out-of-sample).** Fit A on N = 8 and N = 16 ONLY, then
  predict, before looking: MAXCR at **N = 4** and at **N = 32**
  (the latter reachable only at SIGMA >> 0, which also tests the
  g(SIGMA) factor). Point predictions from the unfitted model
  (A = 1): N=32, kappa=1, p in [193, 20000] (SIGMA in [17.7, 24.4])
  gives MAXCR - 1 ~ **1e-4** (predict MAXCR < 1.001); N=4, p=17
  gives MAXCR - 1 ~ **0.40** (predict MAXCR in [1.15, 1.60]).
  PASS = within a factor 2 on (MAXCR - 1) at N = 32 and within a
  factor 1.5 at N = 4.
- **P4d (the verdict this implies).** If P4a/P4b/P4c hold, the
  admissible official row has N = S = 2^40/e, so the model gives
  MAXCR - 1 < 2^{-0.2*2^33}: Z-CEILING would hold with C = 1 + o(1),
  i.e. C < 2^4.77 with grotesque room. I register in advance that
  this is a HEURISTIC extrapolation of a census and is NOT a proof —
  the calibration clause (statement.md:92-98) binds.

## R5. ESCAPE TESTS (must pass or the census is worthless)

- **E1.** THEOREM Z-FLOOR at every computed cell: TMASS >= 2^N/p^kappa.
- **E2.** My fast exact-rational DP (accumulate 2^{-wt} directly,
  integers scaled by 2^N) must agree with the round-23 machinery's
  `weight_enum_kernel` / `weight_enum_kernel_multi`, executed
  VERBATIM out of notes/pilots_20260807/cw_shared_target/cw.py, on
  >= 12 shared cells to 1e-12 relative.
- **E3.** Full-cube identity: with kappa = 0, TMASS = 2^N exactly.
- **E4.** w-invariance (P2a) across all primitive 2S-th roots.
- **E5.** Banked-number replay: EXCESS(16,2,3137) = 2.3463;
  max CRATIO over the round-23 grid = 1.2610; EXCESS(6,19993)=178.51.
- **E6.** Grid asserts in code: 2N a 2-power for every non-probe
  cell (CATCH-Z6); 0 not in Lambda (CATCH-19B).
- **E7.** Any cell reported with CRATIO > 2 must be re-derived by an
  INDEPENDENT standalone script (brute-force ternary enumeration
  where N <= 16, character sum otherwise) before it is reported.

## R6. D3 — THE SHARPENING I WILL ATTEMPT (registered targets)

- **S1 (ensemble form).** Prove E[TMASS] = 1 + H exactly and the
  variance above, over the uniform-parity-check ensemble. Expected
  verdict: PROVED but INERT — it says nothing about the one
  structured L that matters. Registered in advance so that a PROVED
  label here is not mistaken for progress.
- **S2 (the exact character form).** Registered identity to prove:
  TMASS = p^{-kappa} sum_{u in F_p^kappa} prod_j (1 + cos(2 pi
  <u,col_j>/p)) = (2^N/p^kappa) sum_u prod_j cos^2(pi <u,col_j>/p),
  every term NON-NEGATIVE. Consequence I register now:
      **Z-CEILING(C)  <=>  SMOOTH <= (C-1) + C*(p^kappa - 1)/2^N**,
  and E[SMOOTH] = (p^kappa - 1)/2^N. So in the supercritical regime
  (SIGMA >> 0) Z-CEILING is EXACTLY "the non-trivial smoothness mass
  of the value code is bounded by an absolute constant". PREDICTION
  (registered as a likely DISAPPOINTMENT for the route framing):
  this is the SAME object as the "non-local smoothness count" already
  named as mystery 2's required input at statement.md:158-161 — i.e.
  Z-CEILING is a faithful restatement of the requirement, not a
  weaker stepping stone. If so I will say so plainly.
- **S3 (kappa = 1).** Attempt an exact evaluation of SMOOTH for the
  M4 family using th^L = -1 (so G(u) depends only on the coset
  u<th>). PREDICTION: I get an exact orbit decomposition SMOOTH =
  2L * sum over cosets, and a PROVED-AT-CELL bound only; no uniform
  theorem. Registered so a failure here is a registered miss.
- **S4 (weight truncation).** Locate the weight W at which the
  Z-2/moment-controlled head accounts for >= 90% of TMASS-1 as a
  function of SIGMA. PREDICTION: for SIGMA <= 0 the head is
  everything (W = UMIN suffices); for SIGMA >> 0 the mass is carried
  by U ~ N/2, so moment control at W = o(N) is USELESS — predict the
  90% crossing point W_90/N -> 1/2 as SIGMA grows.

## R7. VERDICT RULES (registered before the fact)

- DEAD if: an admissible 2-power cell with CRATIO > 2 (verified by
  E7), or a fitted N-exponent >= 0 (P4a), or a proved unbounded
  admissible family.
- SURVIVES-AND-SHARPENED if: no 2-power cell above the round-23
  record beyond the model's tolerance, P4a/P4b/P4c pass, and S2 is
  proved.
- I will report NO status flip and NO closure either way.


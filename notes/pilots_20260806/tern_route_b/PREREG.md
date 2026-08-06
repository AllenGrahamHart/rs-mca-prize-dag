# PRE-REGISTRATION — ROUTE (b): character sums for ternary relations over 2-power subgroups (round 19, GENERATIVE)

Round 19, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. MANDATE: the one route left
open by round-18's THEOREM Z-NOGO — make it precise, machine-checked,
and either advance it or kill it. If the ternary unification is real,
this is its shared attack; if route (b) dies too, the F2 knife edge
has NO known route and that changes the board.

## 0. The state (quote the minted nodes verbatim first)

- background/nodes/f2_z1_mass_knife_edge: THEOREM Z-NOGO (the
  distance+counting family needs p <= 8 — dead); route (b) = "Weil-
  type / square-root cancellation for products over the
  2^{e_p}-subgroup inside F_p (sizing: sqrt(p)·log p = 2^38 vs
  subgroup 2^39 — a factor-2 headroom; back-of-envelope, NOT a
  theorem)". The object: Z_1 = sum over ternary eps of
  2^{-wt(eps)} [eps in the GRS dual], on the half-system of
  mu_{2^{e_p}}, R/S = 1/log2 p.
- The round-15 measured barrier (mun REPORT §3): the L2/sqrt method
  loses 1-2 orders at every fixture because sqrt-cancellation is
  exactly what fails on structured sets — route (b) must beat THAT
  precedent, not just the envelope.

## 1. Pre-registered deliverables

- **(R1) THE EXACT CHARACTER-SUM FORM.** Express Z_1 (and its
  unweighted sibling |T|) as an exact character/exponential sum:
  the syndrome indicator over the R conditions gives
  Z_1 = p^{-R} sum over multiplicative-character tuples of a
  PRODUCT over the S evaluation points of local factors
  (1 + 2·2^{-1}·cos-type terms — derive the exact local factor for
  the {0,±1} alphabet with the 2^{-wt} weighting; note the
  weighting makes each local factor (1 + 2^{-1}(chi(x) +
  chi(x)^{-1}))-shaped — write it exactly). Machine-verify the
  identity exactly at toy scale (2-power lengths only, CATCH-Z6).
- **(R2) THE CANCELLATION LEDGER.** The main term (trivial
  characters) gives the random-baseline 2^{m - R log2 p} — the
  knife edge. The error is a sum over nontrivial character tuples
  of products over the half-system. State EXACTLY what bound per
  tuple is needed for the total error to stay below the main term
  at k = e, and what Weil/Deligne-type bounds give: complete-sum
  bounds over subgroups (Gauss-sum / Katz), the subgroup structure
  (the half-system is a coset-like half of mu_{2^{e_p}} — is the
  relevant complete sum over the FULL subgroup, recovering exact
  Gauss sums, or genuinely over the half, where partial-sum losses
  bite?). The factor-2 headroom claim must come out of this ledger
  as a theorem-grade statement or die.
- **(R3) THE STRUCTURED-SET PRECEDENT TEST.** The round-15 barrier:
  L2 loses 1-2 orders on structured sets. Determine whether route
  (b)'s sums are the SAME sums that failed there (in which case the
  headroom is illusory — report the kill) or genuinely different
  (independence across the R conditions / the product structure —
  in which case say exactly what is new).
- **(R4) TOY VALIDATION.** At reachable (p, S) with the exact shape
  (p = c·2^{e_p}+1, half-system evaluation, R = S/log2 p rounded):
  compute Z_1 exactly AND via the character-sum decomposition;
  measure the actual per-tuple cancellation against the Weil
  prediction. Pre-register the grid (2-power only). The measured
  constants calibrate (R2)'s ledger.
- **(R5) THE VERDICT.** One of: (i) ROUTE LIVE — a theorem-grade
  conditional ("if [named character-sum bound] then Z_1 <= ...")
  with the named bound's status in the literature stated honestly;
  (ii) ROUTE DEAD — the ledger shows the needed cancellation
  exceeds what any square-root-type bound can give (state the gap
  in bits); (iii) ROUTE TRANSFORMED — the analysis reveals a
  different decomposition (e.g. Gauss-sum exact evaluation at
  2-power conductors — these are classically computable!) that
  changes the question. Chase (iii) hard: at 2-power conductor the
  relevant Gauss/Jacobi sums have KNOWN exact evaluations
  (quadratic + quartic residue symbols) — this may make parts of
  the error term EXACT rather than bounded.

## 2. Pre-registered falsifiers / honesty clauses

- The (R1) identity failing at any toy point kills everything
  downstream — it is the gate.
- No congruence conclusions about counts (AK-UNIT); character sums
  bound archimedean size, which is the admissible shape.
- If the honest ledger says DEAD, say DEAD — the board needs to
  know the knife edge has no route more than it needs optimism.

## 3. Rules of engagement

- DRAFT ONLY: write only inside notes/pilots_20260806/tern_route_b/.
  Never edit dag.json, node shards, tools/, or push. Do NOT read
  notes/pilots_20260806/tern_small_scale_laws/ (sibling
  independence).
- COMPUTE LAW: never bare python3, INCLUDING file patching and JSON
  peeking — tools/ramguard tiny|local -- python3 ..., literal --,
  from repo root /home/u2470931/smooth-read-solomin/prize.
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report; the
  coordinator persists it verbatim.

---

# PILOT ADDENDUM — pre-registrations (Opus pilot, round 19)

Appended 2026-08-06 BEFORE any computation. Everything below is a
prediction or a declared procedure, not a result.

## A. The object, fixed exactly (so nothing drifts later)

Fix `p` prime, `e_p := v_2(p-1)`, `zeta in F_p^*` of exact order
`2^{e_p}`, `S := 2^{e_p-1}`, half-system `Y := {zeta^s : 0 <= s < S}`
(`verify.py:134-140` of z1_ternary_mass; `o1_generating_adversary/
PROOFS.md:241-245`), full subgroup `H := mu_{2^{e_p}} = Y u (-Y)`,
`|H| = 2S`. `Lambda := {1, 3, ..., 2R-1}` (shift `a = 0`;
`z1_ternary_mass/verify.py:143-145`). Parity check
`A[r,s] = (zeta^s)^{2r+1}`, `0 <= r < R`, `0 <= s < S`.
`T := {0,+1,-1}^S`, `wt` = Hamming weight,
`Z_1 := sum_{eps in T, A eps = 0} 2^{-wt(eps)}` (includes `eps = 0`).
Official row: `p = 18446735827372343297`, `e_p = 39`, `S = 2^38`,
`R = 4294967340` (banked) / `4294967339` (exact-balance),
`log2 p = 63.999999355`.

## B. Pre-registered predictions (each is falsifiable)

- **P1 (the local factor).** The exact identity is
  `Z_1 = p^{-R} sum_{u in F_p^R} prod_{s<S} (1 + cos(2 pi f_u(zeta^s)/p))`
  with `f_u(X) = sum_{r<R} u_r X^{2r+1}`, i.e. local factor
  `1 + cos`, NOT `1 + 2cos`. PREDICTION: the banked line
  `z1_ternary_mass/PROOFS.md:394` (`prod_s (1 + 2cos(...))`) is the
  formula for the UNWEIGHTED count `|T cap ker A|`, not for `Z_1`.
  Falsifier: a toy row where `p^{-R} sum_u prod_s (1+cos)` != `Z_1`.
- **P2 (characters are additive).** The syndrome group is `F_p^R`
  (additive), so the tuples are ADDITIVE characters, contra
  `PREREG.md:30` ("multiplicative-character tuples"). Falsifier: a
  correct multiplicative-tuple form reproducing `Z_1`.
- **P3 (the half is not a half).** Because every `l in Lambda` is
  ODD, `f_u` is an odd polynomial, so
  `2 Re W_j(u) = V_j(u) := sum_{x in H} e_p(j f_u(x))` EXACTLY: the
  relevant object is the COMPLETE sum over the full subgroup
  `mu_{2^{e_p}}` and no partial-sum/half-system loss occurs. This
  answers PREREG.md:44-47. Falsifier: a toy `(u,j)` with
  `2 Re W_j != V_j`.
- **P4 (the main term is not the main term).** At the official row
  the trivial-character term equals `2^S p^{-R} = 2^{-46.02}`, while
  `Z_1 >= 1` unconditionally (the `eps = 0` term). PREDICTION: the
  R2 target "total error below the main term" is UNCONDITIONALLY
  FALSE by `>= 46` bits, and the correct target is
  `error <= 2^{o(S)}`. Falsifier: an admissible reading where the
  trivial term exceeds 1.
- **P5 (AM-GM reduction).** `P(u) := prod_s (1+cos theta_s)` obeys
  `P(u) <= (1 + V_1(u)/|H|)^S` by AM-GM, so a bound on the SINGLE
  complete sum `V_1` suffices; no harmonic/`log J` truncation loss
  is needed. PREDICTION: `|V_1(u)| <= eta |H|` for all `u != 0`
  gives `Z_1 <= 2^{S log2(1+eta)} + 2^{S - R log2 p}`.
  Falsifier: a toy `u` with `P(u) > (1+V_1(u)/|H|)^S`.
- **P6 (Weil is vacuous by degree, not by subgroup size).**
  `|V_1(u)| <= deg(f_u) sqrt p = (2R-1) sqrt p`; at the official row
  `(2R-1) sqrt p = 2^{65.0}` against `|H| = 2^{39}`. PREDICTION:
  vacuous by `26 +- 1` bits; non-vacuity needs
  `deg <= |H|/sqrt p = 2^7 = 128`, i.e. `u` supported on the first
  64 coordinates out of `R = 2^32`. The node's `sqrt p log p = 2^38`
  vs `2^39` "factor-2 headroom" silently drops the degree factor.
  Falsifier: a sharper unconditional complete-subgroup bound for
  dense odd polynomials of degree `~ |H|/64`.
- **P7 (the moment substitute lands on Z-NOGO).** Replacing Weil by
  the `2k`-th moment of `V_1` over `u` and evaluating the moment by
  THEOREM Z-2 (`l_1` Newton exclusion, valid for `2k <= 2R`) gives
  an unconditional bound of the shape `Z_1 <= 2^{c S}` with
  `c` bounded away from 0, and closes to `2^{o(S)}` only if
  `log2 p <= log2(e log2 p)`. PREDICTION: that threshold is
  `p <= 8`-shaped, i.e. the SAME barrier as THEOREM Z-NOGO
  (`f2_z1_mass_knife_edge/statement.md:40-44`), against
  `log2 p >= 39`. I pre-register that the numerical constant `8` is
  constant-sensitive and will be reported as a shape, not a
  canonical value.
- **P8 (R5(iii) as briefed is misdirected).** The characters trivial
  on `H = mu_{2^{e_p}}` have order dividing `(p-1)/2^{e_p}`, which
  is ODD. PREDICTION: the classical quadratic/quartic Gauss-Jacobi
  exact evaluations do NOT apply to sums over `H`; they apply to
  sums over the index-`2^j` subgroups (the `2^j`-th powers), the
  opposite object. Falsifier: an exact evaluation of
  `sum_{x in mu_{2^{e_p}}} e_p(a x)` in closed form.

## C. Pre-registered toy grid (2-power only, CATCH-Z6)

`S = 2^{e_p-1}` is a 2-power by construction, so the grid rule is
automatic. `R := round(S / log2 p)`, clipped to `R >= 1`.

| id | p | e_p | S | R | p^R |
|----|---|-----|---|---|-----|
| G1 | 17 | 4 | 8 | 2 | 289 |
| G2 | 113 | 4 | 8 | 1 | 113 |
| G3 | 241 | 4 | 8 | 1 | 241 |
| G4 | 97 | 5 | 16 | 2 | 9409 |
| G5 | 353 | 5 | 16 | 2 | 124609 |
| G6 | 673 | 5 | 16 | 2 | 452929 |

- EXACT tier (cyclotomic arithmetic in `Z[x]/(x^p-1)`, zero
  floating point): G1, G2, G3, and G4 if it fits the compute law.
- MEASUREMENT tier (double precision, tolerance stated in the
  script): all rows.
- `Z_1` computed by TWO independent exact methods (brute-force over
  `3^S` ternary vectors; syndrome-DP over `F_p^R` with integer
  weights `2^{S-wt}`) and cross-checked.

## D. Pre-registered measurements (R4)

For every grid row, over all `u in F_p^R`:
`max_{u != 0} |V_1(u)|` against (i) trivial `|H|`, (ii) RMS
`sqrt(|H|)` (Parseval), (iii) Weil `deg(f_u) sqrt p`;
`max_{u != 0} log2 P(u) / S` against `log2(1+eta_meas)`;
the counting function `|{u : P(u) >= 2^{cS}}|` against the moment
ledger. PREDICTION: `max|V_1|/|H|` is bounded away from 0 (a
constant fraction, NOT `o(1)`), so the per-`u` uniform route
provably cannot give `2^{o(S)}`; the surviving question is the
COUNT of bad `u`, not their existence.

## E. Honesty clauses added by the pilot

- No toy row is evidence about the official row (the standing
  calibration clause, `f2_z1_mass_knife_edge/statement.md:64-69`).
  Toys test IDENTITIES and CONSTANTS only.
- If P1 holds, the banked `PROOFS.md:394` line is wrong and I will
  say so as a catch against our own bank.
- If the ledger says the route cannot reach `2^{o(S)}`, I report
  DEAD with the gap in bits even though a nontrivial exponential
  saving is obtained on the way.

# PRE-REGISTRATION — FPC5 DIAGNOSIS: the three new reds classified (round 23)

Round 23, 2026-08-07. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: wave 48 replaced the
retired Conjecture-F LIST route with three exact FPC5 payment reds.
They are deliberately UNCLASSIFIED. Run the mystery pipeline first
pass on each and return a classification verdict: standard-technique
grind (name the technique, price it) or mystery-hard (name the wall
and which existing mystery shares it).

## 0. Sources (quote verbatim first)
- notes/CONJECTURE_F_FALSE_GREEN_AUDIT_20260807.md — the FPC5
  derivation (the leaf M>=4, d<ell(M-2), t<2M-4; the official-cell
  decomposition; the sharp rate-half boundary 5ell=k+4, b=r=s=
  ell-3, d=2ell-3; the dimension-(ell-1) guarded congruence
  kernel).
- The three reds + their router:
  critical/nodes/l1_fpc5_ratehalf_m4_t2_payment (the rate-half
  guarded split-locator congruence kernel),
  critical/nodes/l1_fpc5_ratehalf_m4_t3_split_slice_payment (the
  Johnson-nonpositive guarded LS6 slices),
  critical/nodes/l1_fpc5_large_source_payment (M>=5,5,7,15 at
  rates 1/2,1/4,1/8,1/16),
  critical/nodes/l1_full_petal_fpc5_payment (the CONDITIONAL
  router) — statements, claim contracts, attack surfaces.
- The proved suppliers: the 15 pma_* reduction nodes named in the
  router's requires; l1_fpc5_ratehalf_ls6_pair_determinant_router
  + l1_fpc5_ratehalf_ls6_canonical_owner_packing (the LS6 chart);
  l1_fpc5_ratequarter_m4_t2_payment (the PROVED sibling — its
  bound-10 proof is the template for what "standard" looks like).
- The disjoint-branch fence: l1_mixed_petal_amplification carries
  the MIXED branch (mystery 6) — the round-21/22 addenda give the
  counting laws there; check which transfer.

## 1. Deliverables (per red, all three)
- (D1) THE CONSUMER CONTRACT: what the router needs from this red,
  quantified (allowance, exponent, rows).
- (D2) THE OBSTRUCTION MADE EXACT: formalize the open kernel/gap
  (rate-half: the dimension-(ell-1) guarded split-core-locator and
  ownership count; m4_t3: the guarded LS6 max-to-mean gap; large
  source: what exactly). Compute the object at toy scale — build
  the guarded congruence kernel explicitly at small official-
  arithmetic-shaped cells and MEASURE the count the payment must
  bound.
- (D3) MANDATORY ADVERSARIAL: attempt to build a violating witness
  at reachable scale (a cell where the payment target fails)
  BEFORE believing emptiness/boundedness. Register the escape
  test in advance.
- (D4) CROSS-LANE MATRIX: which banked instruments apply
  (applies/fails-because per cell): the rate-quarter uniqueness
  template, first-layout domination, the LS6 determinant chart,
  mystery 6's counting laws, the exact-shell machinery.
- (D5) THE CLASSIFICATION VERDICT per red: STANDARD (name the
  closing technique + estimate the work) / MYSTERY-HARD (name the
  wall + the existing mystery it shares, with the shape-pun test
  applied) / MIXED. Plus the cheapest decisive next probe per red,
  executed now if it fits local scale.

## 2. Falsifiers / honesty
- If (D3) finds a violating witness, the FPC5 partition needs
  re-posing — report with a reproduction script; that outranks
  everything else.
- The rate-quarter PROVED sibling is the control: any claimed
  "standard" verdict must point to a mechanism of comparable
  concreteness (over-determination, exact counting), not vibes.

## 3. Rules
- DRAFT ONLY in notes/pilots_20260807/fpc5_diag/. Never edit
  dag.json/nodes/tools; no git; no Modal. COMPUTE LAW: every
  python3 invocation via tools/ramguard tiny|local -- python3 ...
  (literal --), from repo root, INCLUDING file patching and JSON
  peeking. 2-power toy grids where yours to choose (CATCH-Z6);
  official-arithmetic-shaped cells where the object demands them
  (say which and why); name every measured functional
  (CATCH-19C). Verbatim quotes with file:line. No REPORT.md —
  your final message IS the report. QUARANTINE: do not read
  notes/pilots_20260802/CAMPAIGN_LEDGER.md at or past line 2786
  (the "ROUND 23 LAUNCHED" marker); do not read the other
  round-23 pilot dirs (cw_shared_target, ge_lattice_cert,
  c2pp_diag); PASS THIS QUARANTINE CLAUSE VERBATIM to any
  subagent you dispatch.

---

# PILOT REGISTRATIONS (appended 2026-08-07, BEFORE any computation)

Author: Opus pilot, round 23, `fpc5_diag`. Everything below is
registered before a single line of code is run.

## R0. Sources READ at registration time

`notes/CONJECTURE_F_FALSE_GREEN_AUDIT_20260807.md` (all 234 lines);
`critical/nodes/l1_full_petal_fpc5_payment/{statement,conditional,
claim_contract,node.json}`; `critical/nodes/l1_fpc5_ratehalf_m4_t2_
payment/{statement,claim_contract,attack,node.json,dependency_subdag}`;
`critical/nodes/l1_fpc5_ratehalf_m4_t3_split_slice_payment/{statement,
claim_contract,attack,node.json}`; `critical/nodes/l1_fpc5_large_
source_payment/*`; `critical/nodes/l1_fpc5_ratequarter_m4_t2_payment/*`
(the PROVED sibling, incl. `verify.py`); `critical/nodes/l1_fpc5_m4_t2_
payment/statement.md`; `critical/nodes/l1_general_first_layout_
domination/statement.md`; `notes/pilots_20260807/l1_pma_diag/{PREREG,
REPORT}.md`; `critical/nodes/l1_mixed_petal_amplification/
statement_addenda/07-round22-ell-sweep.md`; ledger lines 1745-1834
only. Three read-only subagents harvested the 9 rate-half-m4_t2
background suppliers, the 10 m4_t3/LS6 suppliers + 2 PMA reductions,
and the small-source sieve + `imgfib` consumer contract; each carried
the quarantine clause verbatim.

## R1. What I claim to have DERIVED BY HAND before computing

- **H1 (the FPC5 shape identity).** For a full-petal contributor
  touching `t` petals, the ambient linear slice
  `{(F,W): deg<=d, L_i|(W-c_iF), i=1..t}` has each petal imposing
  `ell` conditions on `2(d+1)` unknowns, so its dimension is at
  least `2d+2-t ell = e+1`. **`e` IS the (affine) dimension of the
  petal slice minus one.** So FPC5's `e->infinity` says exactly:
  *count split-on-core locators in a flat whose dimension grows*.
  This is one statement covering all three reds; it is the
  shape-pun candidate.
- **H2 (the sharp rate-half m4_t2 cell is pinned to one line).**
  From `k+1=4ell+b` (rate 1/2, M=4) and the sharp `b=s=ell-3`:
  `k=5ell-4`, `n=2k=10ell-8`, `|C|=k-1=5ell-5`, `d=2ell-3`.
  **PREDICTION P1: `n=10ell-8` is a 2-power exactly for
  `ell in {4, 52, 820, ...}` (`n=2^m`, `m=5,9,13,...`, i.e.
  `m==1 mod 4`).** Hence the ONLY exhaustively reachable 2-power
  official-shaped sharp cell is `n=32, ell=4` — which is precisely
  the banked certificate's cell. CATCH-Z6 declaration: for `ell>=5`
  I must leave the 2-power grid (`n=42,52,62`); every such cell is
  labelled NON-2-POWER.
- **H3 (`t<=M` always).** `t` counts petals touched, `M` petals
  exist. Combined with FPC5's `t<2M-4`: the true range is
  `2<=t<=min(M,2M-5)`. In particular `t>=M+1` (which would give
  free pair-uniqueness) is **impossible**; the rate-quarter
  uniqueness template needs `t ell>k-1`, i.e. `(t-M)ell>b-2`,
  which holds only for `t=M` with `b<=1`. Self-correction flagged
  in advance: I initially thought `t>=M+1` was reachable.
- **H4 (Johnson denominator in general `t`).** Generalizing
  `pma_three_petal_projective_johnson_bound` (`J=d^2-N(e-1)`,
  `N=|C|=k-1`), the projective-flat dimension is `e` and the
  pairwise root-overlap cap is `e-1` (PROVED at `t=3` by (PJ2);
  PROVED at `t=2` by the cofactor determinant (RH0a) with
  `2s=2d-2ell=e-1`). **Registered as CONJECTURAL for `t>=4`.**
- **H5 (`binom(M,t)` is already polynomial).** By (GL7)
  `M<=log_2(n)/c_0`, so `binom(M,t)<=2^M<=n^(1/c_0)`. Touched-
  subset multiplicity is therefore NOT the obstruction in
  `l1_fpc5_large_source_payment`.
- **H6 (the first-moment margins).** Guarded rate-half m4_t2 mean
  split count per (source, touched pair):
  `mu_(t2)(ell,q)=binom(5ell-5,2ell-3)/q^(ell-1)`,
  since the monic guarded chart has `q^(ell-2)` points, split
  targets number `binom(5ell-5,2ell-3)`, ambient monic degree-`d`
  count is `q^(2ell-3)`. **`log_2 mu ~ 4.855 ell - ell log_2(10 ell)
  -> -infinity super-exponentially.**

## R2. Registered predictions (falsifiable, stated before compute)

- **P1** (above): 2-power official m4_t2 sharp cells are exactly
  `ell in {4,52,820,...}`. FALSIFIED by any other `ell<=2000`.
- **P2 (certificate scope).** The banked
  `l1_fpc5_ratehalf_m4_t2_sharp_cell_nonemptiness` count (71
  primitive contributors, 41/50 layouts nonempty, max 5) is a
  **label-ratio-FREE** count: its solver derives `lambda` from the
  second-petal system. The FIXED-SOURCE object that the payment
  actually has to bound is `~q` times smaller. PREDICTION: an
  exhaustive fixed-source enumeration at `ell=4, q=97` over
  `>=1500` random admissible sources gives mean `N_split` per
  (source, pair) within 10x of `mu_(t2)=3003/97^3=3.29e-3`,
  NOT within 3x of `q*mu_(t2)=0.32`.
  FALSIFIED if the measured mean lands within 3x of `q*mu`.
- **P3 (first-moment law).** Over random admissible sharp-cell
  sources, `mean(N_split)/mu_(t2)(ell,q)` lies in `[1/3, 3]` at
  `(ell,q) = (4,97), (4,193), (5,127), (6,157)`. FALSIFIED
  otherwise.
- **P4 (max is not growing).** `max_source N_exact` over the
  sampled sources satisfies `max(ell=5)<=2*max(ell=4)` and
  `max(ell=6)<=2*max(ell=5)`.
- **P5 (m4_t3 is out of exhaustive reach).** The minimal
  Johnson-NONPOSITIVE rate-half `M=4,t=3` LS6 cell (subject to
  `b>=7`, `b<ell`, `1<=a<=floor((b-3)/4)`, `J<=0`) has
  `(ell,b,a)=(9,8,1)`, `N=|C|=42`, `j=17`, `n=86`, and
  `binom(42,17)=2.5e11` — no exhaustive census of the live atom is
  reachable at ANY local scale. FALSIFIED if an exact integer
  search finds a live cell with `binom(N,j)<10^8`.
- **P6 (owner aggregation is the live gap, measurable off-tail).**
  In shape-matched but Johnson-PAID (`J>0`) LS6 atoms at
  `(ell,b,a)=(4,1,1),(5,1,1),(6,1,1)`, the canonical-owner
  distribution `g=deg gcd(D_0,D_H)` will be concentrated at
  `g=0` (co-deficiency `c=h=ell-2a`, the chamber the packing does
  NOT pay), not at `g=h`. FALSIFIED if >=50% of non-base members
  have `g>=h-2` at any of the three cells.
- **P7 (large-source Johnson sieve).** Under H4, exact integer
  enumeration of all large-source FPC5 cells at `k=2^40` shows a
  nonempty `J<=0` residual at rate 1/2 for `M=5` (i.e. the Johnson
  instrument does NOT clear `M>=5`).
  FALSIFIED if `J>0` on every large-source cell.
- **P8 (shared wall).** Both m4_t2 and m4_t3 residuals are
  instances of H1 with first moment exponentially below 1
  (`2^(-3ell-4)` printed for m4_t3; super-exponentially small for
  m4_t2), so in both the ONLY missing ingredient is max-to-mean
  for a growing-dimensional split flat.

## R3. The MANDATORY adversarial attempt (D3) — escape tests
registered IN ADVANCE

I attempt to build a violating witness at reachable scale before
believing any emptiness or boundedness.

- **A1 (replication gate).** Independently rebuild the guarded
  congruence kernel at the banked cell `(n,k,ell,M,b,s,d) =
  (32,16,4,4,1,1,5)` over `H_32 subset F_97^*` and confirm
  `dim ker = ell-1 = 3`, monic chart affine dim `ell-2 = 2`,
  locator codimension `ell-1 = 3`. NOTHING below is reported
  unless A1 passes.
- **A2 (random source search, m4_t2).** Exhaustive
  `binom(|C|,d)`-subset census of `N_split`, `N_prim`, `N_exact`
  over many random admissible sharp-cell sources at
  `ell=4,5,6`, and a `q`-sweep at `ell=4`.
- **A3 (designed source search, m4_t2).** Hill-climb / structured
  search over the source (core placement, petal placement, label
  pair) maximizing `N_exact` at `ell=4` and `ell=5`; plus the
  symmetry attack — choose `C,B,T_1,T_2` as unions of cosets of a
  subgroup of `mu_n` with labels compatible, aiming at the
  reciprocal/dihedral stratum the node flags as OPEN.
- **A4 (period attack).** At `ell=5, n=42, d=7`: `7|42` and
  `7|7`, so a `mu_7`-periodic locator IS arithmetically admissible
  (unlike the official 2-power rows, where
  `l1_fpc5_ratehalf_m4_t2_sharp_dyadic_quotient_absence` kills it
  by odd `d`). I will hunt for it explicitly and report whether it
  populates the guarded flat. A hit is a genuine warning that the
  dyadic-parity route-cut is arithmetic luck, not structure.
- **PRE-REGISTERED ESCAPE TEST (ESCAPE-RH, red 1).** The
  adversarial construction SUCCEEDS — I report a violating witness,
  the FPC5 partition needs re-posing, and that outranks everything
  else — IF EITHER
  - **(a)** some admissible sharp-cell source at `ell in {4,5,6}`
    yields `N_exact >= 4(ell-2)` for a single touched pair
    (i.e. `>=8, 12, 16`), which is at or above the PROVED
    rate-quarter sibling's absolute bound `10` and grows with the
    flat dimension; OR
  - **(b)** `max_source N_exact` at least doubles from `ell=4` to
    `ell=5` AND again from `ell=5` to `ell=6`.
  Otherwise the construction FAILS and I report the blocking
  mechanism, quantified.
- **PRE-REGISTERED ESCAPE TEST (ESCAPE-LS6, red 2).** In the
  off-tail LS6 ladder `(ell,b,a)=(4,1,1),(5,1,1),(6,1,1)`, the
  construction SUCCEEDS IF the total atom size `|LS6|` grows by a
  factor `>=q^(1/2)` per unit `ell` (super-polynomial in `n`
  along the ladder), OR if the summed owner charge
  `sum_G |F_G|` exceeds `3^(h+1)` (the trivial all-owners bound)
  at any cell — i.e. the aggregation gap is not merely unproved
  but actually violated by the fixed-owner instrument.
- **PRE-REGISTERED ESCAPE TEST (ESCAPE-LS, red 3).** The
  construction SUCCEEDS IF the exact large-source cell
  enumeration exhibits, at the official rows, a cell with
  `t=2` (the branch with NO mu-basis/Johnson instrument at all)
  and `e` growing, for which no proved instrument in the whole
  banked set applies — reported as an EXPOSURE, not a witness.

## R4. Toy-cell declarations (CATCH-Z6 / CATCH-19C)

- **T-A (red 1, official-arithmetic-shaped, NOT free choice).**
  `(n,k,ell,M,b,r,s,d) = (10ell-8, 5ell-4, ell, 4, ell-3, ell-3,
  ell-3, 2ell-3)` for `ell=4,5,6`. Justification for leaving the
  2-power grid: the object only exists on the line `5ell=k+4`
  (`l1_fpc5_ratehalf_m4_t2_codimtwo_guarded_slice` (GS1)); by P1
  that line meets the 2-power grid only at `ell=4` (`n=32`) and
  `ell=52` (`n=512`, `binom(255,101)` — unreachable). `ell=4` IS
  2-power and is my control.
- **T-B (red 2, official-arithmetic-shaped but OFF-TAIL).**
  `(ell,b,a)=(4,1,1),(5,1,1),(6,1,1)`, `n=8ell+2b-2`,
  `k=4ell+b-1`, `N=|C|=4ell+b-2`, `j=2ell-a`, `M=4`, `t=3`.
  These satisfy the rate-half `M=4` source equation exactly and
  `n=32,40,48` (2-power only at `ell=4`). They have `J>0`, so they
  are Johnson-PAID and are NOT the live tail — labelled OFF-TAIL
  throughout. They are used ONLY to measure the LS6 chart's owner
  structure, which is `J`-independent.
- **T-C (red 3).** No toy; exact integer cell enumeration at the
  four official rows `k=2^40`, `n=rk`.

## R5. Named measured functionals (CATCH-19C)

- `N_split(source,pair)` := `#{D subset C : |D|=d, L_D in A_F}`
  where `A_F` is the monic guarded chart of
  `l1_fpc5_ratehalf_m4_t2_sharp_projective_flat_descriptor` (FD2).
- `N_prim` := those with `gcd(F,W_F)=1`.
- `N_exact` := those additionally with `(W_F-c_uF)(x)!=0` at every
  untouched-petal point (`u=3,4`).
- `mu_(t2)(ell,q)` := `binom(5ell-5,2ell-3)/q^(ell-1)` (the
  first-moment prediction, R1/H6).
- `|LS6|(ell,b,a,lambda)` := the guarded atom size (LS6).
- `g` := `deg gcd(D_0,D_H)`; `c := h-g`, `h=ell-2a`.
- `J(N,d,e)` := `d^2-N(e-1)`.

## R6. Honesty pins

- Census/enumeration evidence is EVIDENCE, never proof; labelled
  at every use.
- DERIVED+CHECKED vs MEASURED labels on every number.
- If A1 disagrees with the banked kernel dimensions I report the
  disagreement and stop rather than adjust.
- Every self-correction is stated plainly, including H3 above,
  which corrects an error I made before registering.

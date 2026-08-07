# PRE-REGISTRATION — MYSTERY 5 DIAGNOSIS: generator_economy (round 21)

Round 21, 2026-08-07. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: the full mystery
pipeline, first pass, for the newly promoted mystery 5.

## 0. Sources (quote verbatim first)
- critical/nodes/generator_economy/statement.md (the construction,
  the E12 early-cap ledger entry, the profile_covering_obstruction
  scope, the kernel-lattice alternative) + the legacy consumer
  sketch it cites (proof_sketch/s2_paid_ledger.md#3 — locate the
  migrated copy in-repo).
- The consumers: trace which critical nodes require
  generator_economy (dag.json edges) and what they need QUANTIFIED.

## 1. Deliverables
- (D1) THE CONSUMER CONTRACT: what exactly does the chain need —
  the full B*/2^33 centers, or a weaker certified fraction? Quote,
  then derive the weakest sufficient form.
- (D2) THE EARLY-CAP MADE QUANTITATIVE: reproduce E12's linear-
  growth measurement; derive the exact gap (bits) between
  orbit-union growth and the requirement; determine whether template
  compression or imported difference-set designs can close it IN
  PRINCIPLE (dimension/counting argument), or whether the cap is
  structural.
- (D3) THE TERNARY BRIDGE TEST (criticality-compatibility, the
  round-19 gate): the germ zeta^a - zeta^b = zeta^b(zeta^{a-b} - 1)
  lives in Z[zeta]; the campaign's CS/norm machinery
  (es_ternary_suppression_instruments, tern_master_threshold) lives
  in the same ring. Formalize whether generator_economy is an
  instance of T(P, Lambda) or its DUAL (a CONSTRUCTION problem where
  the mysteries are EXCLUSIONS — the tau side matters: construction
  wants supercritical, exclusion wants subcritical). Graded verdict:
  object / regime / method, per the standing third gate.
- (D4) THE KERNEL-LATTICE ROUTE: price the named alternative
  (lattice_cone_certificate) — what would per-row certification
  cost, and is it Modal-scale?
- (D5) The weakest-form re-pose draft (floor-campaign style) with a
  pre-registered falsifier.

## 2. Falsifiers / honesty
- If the early cap is STRUCTURAL (a proved ceiling), say so plainly
  — that makes mystery 5 hard and the kernel-lattice route the only
  lane.
- The ternary bridge must pass the shape-pun test before any
  unification language is used.

## 3. Rules
- DRAFT ONLY in notes/pilots_20260807/gen_economy_diag/. Never edit
  dag.json/nodes/tools; no git. COMPUTE LAW: tools/ramguard
  tiny|local -- python3 (including file patching and JSON peeking).
  2-power toy grids; name functionals (CATCH-19C). Verbatim quotes
  with file:line. No REPORT.md — your final message IS the report.
  Do not read CAMPAIGN_LEDGER entries after the "ROUND 21 LAUNCHED"
  marker; PASS THE QUARANTINE CLAUSE to any subagent you dispatch.

---

# PILOT REGISTRATIONS (Opus pilot, round 21, appended BEFORE any computation)

All toy grids are 2-powers (CATCH-19C); every measured quantity is a
NAMED functional. Each registration carries its falsifier. Nothing below
was computed at the time of writing.

## R1 — COLLAPSE(N): does the Pro-Brief-F family collapse under e_1?
Definition. For the antipodal zero-sum padding family of
`notes/pro_construction.md` at ring Z[z]/(z^N-1) (z = zeta_N):
`B(s,T) = {z^s, z^{s+1}} u T`, T a set of N/4-1 antipodal pairs
{z^j, z^{j+N/2}} drawn from the N/2-2 residual positions.
  COLLAPSE(N) := |F(N)| / #{ distinct e_1(B) : B in F(N) }.
Prediction (pre-registered): COLLAPSE(N) = C(N/2-2, N/4-1) exactly, i.e.
the number of pairwise e_1-DISTINCT centers is exactly N, independent of
the padding factor, for N = 8, 16, 32.
Falsifier: any tested N with #distinct > N refutes the collapse reading;
the padding factor then survives and D2's cap must be re-derived.

## R2 — SLOPE(N), CURV(N): reproduce E12's linear orbit-union growth.
Definition. Template = an admissible half-size subset; its center orbit is
the mu_N-orbit {z^r * e_1(B)}. For t templates,
  U(t,N) := |union of the t center orbits| ;
  SLOPE(N) := U(t,N) - U(t-1,N)  (mean over t) ;
  CURV(N)  := max_t [ U(t+1,N) - 2 U(t,N) + U(t-1,N) ].
Prediction: SLOPE(N) <= N with CURV(N) <= 0 (concave/linear): unions grow
at most linearly, so t ~ (target)/N templates are needed.
Falsifier: CURV(N) > 0 at N = 16 or 32 refutes "linear only" and reopens
plain orbit unions as a route.

## R3 — CROSSBASES(t,N): the quantity E12 did NOT measure.
Definition. For a t-template union, CROSSBASES(t,N) := the number of
distinct multiplicative bases required to factor ALL pairwise differences
of centers, INCLUDING cross-template pairs, over the certified base set
G = {z, 1+z} u {z^k - 1}.
Prediction: CROSSBASES(t,N) grows linearly in t (unbounded in t), so the
`poly(N')` base budget — not the union SIZE — is the binding constraint.
Falsifier: CROSSBASES(t,N) <= c*N for all t <= 8 at N = 16, 32 would show
plain unions are base-economical and relocate the early cap elsewhere.

## R4 — SEMIGROUP-COUNT: the in-principle dimension/counting cap for D2.
Claim to be derived and checked, not assumed: if F is a set of centers in
the additive group of Z[z] with (F - F) \ {0} contained in
S = U * Sg(g bases, multiplicative degree <= d), U the height-budget unit
set, then |F| <= |S| + 1 <= |U| * C(g + d - 1, d) + 1.
Toy check (brute force, N = 8 and 16): the maximum |F| with F - F inside a
prescribed S equals the clique number of the Cayley graph on S, and is
<= |S| + 1.
Pre-registered verdict rule: I will call the early cap STRUCTURAL if and
only if the height budget forces d = O(1) or O(log N'), so that
|U| * C(g+d-1, d) < B*/2^33 at N' = 128 for every poly(N') base count.
Otherwise I will report NOT STRUCTURAL (a counting bound that leaves room)
and say plainly that the cap is empirical, not proved.
Falsifier: a toy F with F - F inside S and |F| > |S| + 1 would refute the
bound (it cannot happen in a group; this is the sanity check).

## R5 — TERNARY BRIDGE, graded verdict (round-19 third gate).
Pre-declared PASS bar, fixed before looking at the instruments:
  OBJECT passes only if the ternary machinery and generator_economy bound
    the SAME functional on the SAME ring with the SAME coefficient class.
  REGIME passes only if the parameter ranges overlap at N' = 128 / the
    prize rows, not merely in form.
  METHOD passes only if the CS/norm instrument produces the inequality
    direction the construction needs.
Pre-registered expectation (to be scored honestly against the outcome):
OBJECT partial (same ring Z[zeta], different coefficient class), REGIME
partial-or-fail, METHOD fail by DUALITY — exclusion instruments deliver
UPPER bounds on admissible families, i.e. they serve the CAP direction,
not the construction direction. If METHOD fails this way I will say the
bridge is a shape-pun for the construction and note whether it is live for
the cap. No unification language unless all three pass.

## R6 — D4 PRICING: lattice_cone_certificate.
Cost model to be filled from the node's own spec:
  COST = (#rows to certify) * (cone dimension) * (per-cone solve cost).
Pre-registered Modal-scale threshold: "Modal-scale" iff the total fits
~10^4 core-hours AND per-row working set <= 1.5 GB (the ramguard `modal`
profile ceiling). If the node does not pin enough to price it, I report
UNPRICEABLE and name the missing constants rather than inventing them.

## R7 — Scope honesty.
This is a first-pass diagnosis. Every number I report is either quoted
with file:line, or computed here at toy scale and labelled as such. Where
the extrapolation from a 2-power toy to N' = 128 is a leap, I label it a
leap rather than a result.

# PREREG — r38_sporadic_det (round 38)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r36_m4_nonsplit/REPORT.md` (round 36)
2. `notes/pilots_20260811/r37_share3_gap/REPORT.md` (round 37)

## Mandate

THE LAST TWO m=4 ROUTES. (A) SPORADIC (non-factoring) 3-sharing:
Lueroth forces UNIFORM sharing to factor through a degree-3 w;
sporadic = non-uniform (8 shared triples WITHOUT a global
quotient map). Priced < 1e-4 by round 36, never searched, and
the pricing was a naive count in a lane where counting is dead
(five refutations in two rounds — including round 37's own
constant-norm mechanism beating its naive count by 3400x).
STRUCTURE FIRST: what does a non-factoring Psi with 8 shared
triples look like? The 8 shared-triple conditions are
Res_gamma(R(.,t_i), R(.,t_j))-type coincidences WITHOUT the
lattice structure — is there a WEAKER factoring (through a
correspondence rather than a map? a degree-3 rational curve
in P^1 x P^1?) that Lueroth does not forbid and that carries
sharing at sub-naive cost? Derive the taxonomy BEFORE searching.
(B) THE DETERMINANTAL 11-MERGE SOLVE: the 13-slope variety is
dim 4 over F_qbar (two agreeing counts) but unreachable by
incremental instruments (budget 8). Attack the simultaneous
system EXPLOITING ITS STRUCTURE: the merges are "the twisted
cubic C meets 11 named lines l_ij" — use the resultant/
elimination structure (each "meets l_ij" is one determinantal
condition on the 4-dim family; the family after 8 prescribed
merges is EXPLICIT with kernel dim 2 — parameterize it and solve
the REMAINING 3 conditions on ~3 parameters as a small
polynomial system: 3 resultants in 3 unknowns, NOT generic
Groebner). Even deciding solvability at q = 193 decides whether
the round-37 fence's "free-merge" reading was the whole truth.

## Deliverables

**D1 — THE SPORADIC TAXONOMY.** Non-uniform sharing patterns
compatible with the (OV)/per-side caps: which (n_3', n_2', n_1')
mixtures short of full uniformity survive round 36's exclusion
(it forced n_3 = 8 ASSUMING the demand ledger — recheck at the
degenerate-fibre slot count 23 too); the correspondence-sharing
question (Lueroth's scope: does a (3,3)-correspondence in
P^1 x P^1 carry 8 triples without factoring?); the cost ledger
for each surviving pattern. Then a TARGETED search of the
cheapest pattern only (two fields).

**D2 — THE 3-IN-3 SOLVE.** From a fixed 8-prescribed-merge state
(kernel dim 2 + the slope choices — derive the exact residual
parameter count), write the 3 remaining merge conditions as
polynomials in the residual parameters; solve by iterated
resultants/gcds (stdlib-feasible if degrees stay < ~50 — derive
the degrees FIRST). Sweep enough 8-merge states at q = 193 to
either find a 13-slope solution (=> hand to the pipeline: this
is the same witness event as the side door) or state the
solvability rate exactly on the swept sample.

**D3 — RECONCILIATION.** If D2 finds solutions the round-37
budget fence needs its scope tightened (it bounds INCREMENTAL
instruments only — confirm its own caveat); if D2 exhausts
negative on a large sample, the free-merge reading hardens
toward an exclusion CONJECTURE (state it with falsifiers).
Either way: the exact relationship between the dim-4 variety,
its F_q-points, and the budget-8 reachable locus.

**D4 — VERDICT.** The m=4 route map after this round; misses
first; cross-pilot flag (do NOT read siblings).

## Blind priors to register

P(a correspondence-sharing pattern exists legally), P(the 3-in-3
degrees are stdlib-feasible), P(a 13-slope solution from D2),
P(the dim-4 variety has F_q-points at q=193), expected outcome
(a phrase).

## Pilot registrations

Appended with the Edit tool after reading EXACTLY the two named
anchors (`r36_m4_nonsplit/REPORT.md`, `r37_share3_gap/REPORT.md`)
and BEFORE any other read, any grep, any `ls`, and any interpreter
invocation. Everything below is derived from the two anchors alone.

### R0 - SCOPE AND METHOD

- R0.1 Two anchors only. No sibling `r38_*` directory read, named
  or listed; the parent is never `ls`-ed.
- R0.2 AUDIT-AND-DRAFT: every write inside this directory. No
  `dag/`, `nodes/`, `critical/`, `background/`, `tools/`, no git.
- R0.3 Two-field confirmation (`q = 193`, `257`) on every
  structural claim. The admissible window is `q = 1 mod 64`, i.e.
  `{193,257,449,577,641}` below 690 (r37 R4.1, banked).
- R0.4 D1's taxonomy and D2's degree derivations are registered
  here, BEFORE any search, as the brief requires.

### R1 - D1 STRUCTURE: THE COINCIDENCE-SCHEME DICHOTOMY

- **R1.1 (the dichotomy).** Let `Z = closure{(x,y) in P^1 x P^1 :
  x != y, Psi(x) = Psi(y)}`. Either `Z` is FINITE (sporadic), or it
  contains a curve. If it contains a curve `C`, then `Psi` is
  constant on the TRANSITIVE CLOSURE of `C`; that closure is either
  all of `P^1 x P^1` (forcing `Psi` constant, excluded) or a proper
  equivalence relation, which by Lueroth is the fibre relation of a
  single map `w`. **SPORADIC XOR UNIFORM. There is no third case,
  and in particular no "weaker factoring".** `P = 0.85`.
- **R1.2 (the brief's correspondence question, answered blind:
  NO).** Symmetric bidegree-(2,2) forms on `P^1 x P^1` (the
  off-diagonal part of a (3,3) fibre relation) have 6 coefficients,
  i.e. `P^5`. The fibre-product locus `{C_w : deg w = 3}` is the
  image of `(P,Q)` (8 coefficients) modulo `GL_2` acting on the
  target (4), hence **dimension 4: a HYPERSURFACE in `P^5`.** So a
  generic symmetric (2,2)-correspondence does NOT factor - and by
  R1.1 it carries no non-constant `Psi`, because it is not
  transitive. **A (3,3)-correspondence carries 8 triples only when
  it IS a map's fibre relation.**
  `P(a correspondence-sharing pattern exists legally) = 0.07`.
- **R1.3 (the (1,1) sub-case, and a REPAIR of r36's R1.7).** If `Z`
  contains the graph of `sigma in PGL_2` of order 3, then `w` is the
  Galois quotient. `sigma` must carry 24 points of `mu_64` into
  `mu_64` in 8 `sigma`-stable triples. r36's R1.7 argues
  *"gcd(3,64)=1 so `mu_64` has no order-3 element"* - that excludes
  MULTIPLICATIVE order-3 elements only, and does NOT by itself
  exclude an order-3 Moebius map: `64 = 3*21 + 1`, so 1 fixed point
  plus 21 triples is numerically legal. **The correct argument is
  the setwise stabiliser: `Stab_{PGL_2}(mu_N)` is dihedral of order
  `2N = 128`, a 2-group, with no element of order 3.**
  `P(no order-3 sigma at q=193 and q=257) = 0.90`. Registered as an
  EXHAUSTIVE check: `sigma` is determined by the images of 3 points,
  so at most `64*63*62 = 249984` candidates.

### R2 - D1 LEDGER: THE PATTERN LADDER AND A PATTERN-INDEPENDENT DEFICIT

- **R2.1 (slot law, m=4).** `slots = 3 t_D - delta + (m-2) t_M`,
  `rho = 15`, demand `D = slots - rho`; `t_D` = number of tuple
  classes on the `6m = 24` points of `S_g D S_h`, `t_M` = classes on
  the `m-1 = 3` middles, `delta` = number of classes whose slope
  cubic has a repeated root. (OV) caps class size at `m-1 = 3`
  (r36 D1.3). Calibration: `t_D = 8, t_M = 1, delta = 0` gives
  `D = 24 + 2 - 15 = 11` (r36's value).
- **R2.2 (the ladder).** `n_1 + 2n_2 + 3n_3 = 24` and
  `t_D = n_1+n_2+n_3` give `24 <= 3 t_D`, so **`t_D >= 8` with
  equality iff `(n_1,n_2,n_3) = (0,0,8)`**, hence
  > **`D = 11 + 3(t_D - 8) + 2(t_M - 1) - delta`.**

  **Every pattern has `D >= 11 - delta`, and the uniform pattern is
  the UNIQUE minimiser at every value of `delta`.** `P = 0.92`.
- **R2.3 (near-uniform enumeration, registered before computing).**
  `t_D = 9` admits EXACTLY TWO patterns, `(1,1,7)` and `(0,3,6)`,
  both `D = 14`. `t_D = 10` admits EXACTLY FOUR, `(3,0,7)`,
  `(2,2,6)`, `(1,4,5)`, `(0,6,4)`, all `D = 17`. `P = 0.85`.
- **R2.4 (the brief's degenerate-fibre recheck, slot count 23).**
  `delta` shifts EVERY pattern by the same `-delta`, so the ranking
  is `delta`-invariant: **uniform stays uniquely optimal at slot
  count 23** (uniform `D = 10`, the two `t_D=9` patterns `D = 13`).
  A non-uniform pattern becomes nominally admissible only at
  `delta >= 2` against r36's nominal supply 12, and at `delta >= 3`
  against the measured legal supply 10/9 (r36 D2.2).
  `P(a non-uniform pattern survives at the MEASURED supply) = 0.03`;
  `P(some non-uniform pattern is nominally admissible at supply 12
  with delta = 2) = 0.75` - an ADMISSIBILITY statement, not an
  existence statement.

### R3 - D1 COST LEDGER: THE SPORADIC DEFICIT (main blind derivation)

- **R3.1** The banked `x`-degree budget `deg_x <= 3(m-1) = 9`
  (r36 D1.2) gives `Psi = [U : E_1 : E_2 : E_3]` with `4 x 10 = 40`
  coefficients, i.e. **`P^39`**.
- **R3.2** A class `c` of size `s` sharing the projective value
  `tau_c in P^3` is `3s` LINEAR conditions on `Psi` for fixed
  `tau_c`, and `tau_c` carries 3 free parameters, so the **net cost
  is `3s - 3` per class** (a singleton is free).
- **R3.3** Slope layer: the `3 t_D - delta` slots must use at most
  13 distinct values (2 of `rho = 15` reserved for the middles), so
  `3 t_D - delta - 13` merge conditions on the `tau`'s.
- **R3.4 (THE CANCELLATION).** Total dimension of the sporadic
  system, `D`-part only:
  > `39 + 3 t_D - 72 - (3 t_D - delta - 13) = -20 + delta`.

  **The `t_D`-dependence CANCELS EXACTLY: the sporadic deficit is
  20 (`20 - delta` with degenerate fibres) and is INDEPENDENT of the
  sharing pattern `(n_1,n_2,n_3)`.** `P = 0.80`. Consequence: D1's
  "cost ledger for each surviving pattern" is FLAT to leading order,
  and the only pattern-dependence is the discrete count `N`.
- **R3.5 (first moment, registered as numbers).** `M = N * q^{-20}`
  with `N` = number of ways to choose the classes inside `mu_64`.
  Registered at `q = 193`: `N(0,0,8) ~ 10^30.4`,
  `N(1,1,7) ~ 10^30.1` (each +/- 0.3 dex), `q^20 = 10^45.7`, so
  **`M ~ 10^-15.3`, and within one order of magnitude for every
  pattern.** This is ELEVEN ORDERS OF MAGNITUDE BELOW r36's
  `< 1e-4` pricing (r36 R1.9): **r36's price was OPTIMISTIC, not
  conservative.** `P(the exponent -20 is right) = 0.75`;
  `P(M within 2 dex of 10^-15.3) = 0.55`.
- **R3.6 (why uniform is different).** The uniform route buys all
  `72 - 24 = 48` incidence conditions with the 7 parameters of `w`;
  that bulk purchase is exactly what R1.1's dichotomy says has no
  analogue in the sporadic case. Measured cheapness of the uniform
  pencil layer: 5056 pencils with `>= 8` complete disjoint fibres at
  `q=193` (r37 D1(b)).
- **R3.7 (mechanism search, registered blind).** The only `mu_64`
  mechanism at multiplicity 3 known to this lane is r36's
  constant-norm family, and it is a condition on a PENCIL of cubics,
  i.e. it lives on the uniform route. `gcd(3,64) = 1` kills
  multiplicative 3-sharing; R1.3's dihedral stabiliser kills Moebius
  3-sharing. **Prediction: no structured sporadic sub-family with
  deficit `< 20` exists.** `P = 0.75`.
  **FALSIFIER F-R3: exhibit any sporadic family whose deficit is
  `< 20`, or measure a sporadic hit rate above `10^-10` at
  `q = 193`. Either fires and the pricing above is withdrawn.**

### R4 - D2: RESIDUAL PARAMETER COUNT AND DEGREES (derived first)

- **R4.1** Slope layer of record (r37 D2.3):
  `R(t,gamma) = w(t)^T Psi v(gamma)`, `w(t) = (1,t,t^2,t^3)`,
  `v(gamma) = (gamma^3, -gamma^2, gamma, -1)`, `Psi in P^15`. A
  merge on edge `(i,j)` at slope `gamma` is
  `R(t_i,gamma) = R(t_j,gamma) = 0`.
- **R4.2 (CORRECTION TO THE BRIEF).** The brief states *"the family
  after 8 prescribed merges is EXPLICIT with kernel dim 2"*. By
  r37's own cost table (7 edges at cost 2 give rank 14; the 8th
  costs 1 and gives rank 15, `d3_alloc_results_d.txt:17-25`),
  **8 prescribed merges leave kernel dimension `16 - 15 = 1` - a
  single point of `P^15`, with NO free parameter.** The state with
  kernel dimension 2 is the **7**-prescribed-merge state.
  > **Registered residual count: after `r` prescribed edges with
  > explicit slopes, rank `= 2r` and kernel dim `= 16 - 2r` for
  > `r <= 7`. The correct working state is `r = 7`: kernel dim 2,
  > ONE projective parameter `(alpha:beta)`, and FOUR residual merge
  > conditions - not three.** `P = 0.85`.
- **R4.3 (DEGREES - the brief's "derive the degrees FIRST").** On
  the pencil `Psi = alpha A + beta B` every coefficient of
  `R(t_i,.)` is linear in `(alpha,beta)`. A residual merge `(i,j)`
  is `Res_gamma(R(t_i,.), R(t_j,.)) = 0`, the `6x6` Sylvester
  determinant of two cubics, homogeneous of degree 3 in each cubic's
  coefficients:
  > **a BINARY FORM OF DEGREE 6 in `(alpha:beta)`.**

  On the legal branch where an endpoint already carries two
  prescribed slopes `c, f`, `R(t_j,gamma) = (gamma-c)(gamma-f)
  L(gamma)` and the condition reduces to `Res(R(t_i,.), L) = 0`, **a
  binary form of degree 4**. **ALL DEGREES `<= 6`.**
  `P(the 3-in-3 degrees are stdlib-feasible) = 0.97`;
  `P(degrees <= 6) = 0.85`.
- **R4.4 (instrument and rate).** Four binary sextics in ONE
  projective unknown, solved by iterated `gcd` over `F_q` (Euclid on
  degree `<= 6` polynomials) - exactly the brief's "iterated
  resultants/gcds, NOT generic Groebner". Naive Bezout gives a
  per-draw hit rate `6^4 / q^3 = 1296/q^3 =` **`1.84e-4` at
  `q=193`** and **`7.63e-5` at `q=257`**.
  `P(the measured rate is within 10x of this) = 0.55`.
- **R4.5 (a THIRD independent dimension count).** In the
  (slope, scale) chart the 8 slope cubics are
  `f_i = s_i * prod_{gamma in S_i}(X - gamma)` and must satisfy the
  4 left-kernel relations of the `8x4` matrix `[w(t_i)]`, i.e. 16
  linear conditions on `13` slopes `+ 8` scalars `= 21` parameters,
  20 projective: **`20 - 16 = 4`.** This agrees with r37's
  `15 - 11 = 4` and with its intrinsic `12 - 11 + 3 = 4`.
  `P = 0.85`. Corollary registered: for FIXED slopes the system is
  LINEAR in the 8 scalars - a `16x8` matrix required to drop to rank
  `<= 7`, codimension `(16-7)(4-3)`-style `= 9` on 13 slope
  parameters, `13 - 9 = 4`.
- **R4.6** The merge graph is UNIQUE up to isomorphism
  (`K_{4,4}` minus a perfect matching minus one edge, degrees
  `(3,3,3,2 | 3,3,3,2)`, r37 R1.2). What is swept is the ASSIGNMENT
  of the 8 fibre values to its 8 vertices and the choice of 8 fibres
  from a pencil's complete fibres (`C(12,8) = 495` at `q=193`'s best
  pencil).

### R5 - D2 SWEEP DESIGN AND PRIORS

- **R5.1 Two arms.** (A) REAL-`t`: the `t_i` are fibre values of
  actual pencils with `>= 8` complete disjoint fibres in `mu_64`, at
  `q = 193` and `q = 257`. (B) GENERIC-`t` CONTROL: the `t_i` are
  random in `F_q`. **If B yields solutions and A does not, the fence
  is ARITHMETIC; if neither does, the fence is GEOMETRIC and the
  dim-4 count is misleading.** `P(the two arms differ by > 10x in
  rate) = 0.35`.
- **R5.2 Priors.** `P(>= 1 verified 13-slope solution, arm A, within
  budget) = 0.20`. `P(>= 1 in arm B) = 0.45`.
  `P(the dim-4 variety has F_q-points at q = 193) = 0.60`.
  `P(any verified witness this round) = 0.22`.
- **R5.3** Registered expected solvability rate, arm B: `1.8e-4` per
  draw (R4.4). Arm A: same point estimate, band
  `[1e-2, 1e+1] x` the arm-B rate; I decline a sharper prediction.
- **R5.4 EXPECTED BEST `|slopes|` if nothing lands: 14 at `q=193`**,
  tying r36 and r37. `P(best = 14) = 0.50`, `P(best = 13, a
  witness) = 0.20`, `P(best >= 15) = 0.30`.

### R6 - MISS-2 GUARD (no solution is reported unless all clauses pass)

- **G1 NO DEGENERACY.** `Psi != 0`; `R(t_i,.) != 0` for all 8 `i`;
  the `gamma^3` coefficient `U~(t_i) != 0` for all `i` (a vanishing
  leading coefficient makes two cubics "share a root at infinity"
  and voids the resultant test).
- **G2 RATIONAL AND SIMPLE.** Each of the 8 cubics splits over
  `F_q` with 3 DISTINCT roots (the `delta = 0` arm). A resultant may
  vanish through a NON-RATIONAL or a REPEATED common root; neither
  is a merge.
- **G3 STRUCTURAL VERIFICATION** (r36 D2.2's verifier,
  re-implemented, never imported): `|distinct slopes| = 13`
  EXACTLY; hypergraph degree `d_gamma <= 2` for every slope; pair
  multiplicity `<= 1`; merge graph bipartite with a 4/4 per-side
  balance and degree sequence `(3,3,3,2 | 3,3,3,2)`. **A raw
  resultant hit is NOT a witness.** This clause exists because
  r36's raw `C = 12` "witness" was one slope of hypergraph degree 8
  (r36 MISS 5), and because r37's guard killed 21/18 and 37/36
  draws per cell.
- **G4 NO COUNT-AS-CONFIGURATION.** I will not report a
  supply/demand crossing, a dimension count, or a first moment as
  existence; specifically I will not read "the variety has dim 4"
  as "a solution exists" (r37 MISS 6).
- **G5 TWO-FIELD.** Every structural claim is stated only if it
  reproduces at `q = 193` AND `q = 257`.

### R7 - ZERO-POWER DECLARATIONS (pre-declared)

1. A D2 negative is a SAMPLED negative over named merge-graph
   assignments, named pencils and a named draw budget at two
   fields. It is NOT an exclusion of the 11-merge variety, NOT a
   statement about its `F_q`-points in general, and NOT a decision
   of `m = 4`.
2. R3.4's deficit-20 count is a NAIVE FIRST MOMENT of exactly the
   kind r36's MISS 3 refuted by 3400x. **It has ZERO power to
   exclude sporadic sharing**; it is a price with F-R3 as its
   falsifier.
3. R2's taxonomy is a statement about the SLOT/DEMAND ledger,
   conditional on (OV), (OUT-m), (DEG-m) and the banked
   `rho = 4m-1`, `T_2 = rho` accounting, which is POSED with
   coordinator corrections (r36 ZP-10). It inherits that status.
4. No `G` is built, no outside completion, no bivariate system, no
   `|W| = 27` on actual points, no per-side split, no `mu(x)` check
   at the middles, no layer A, no (SAT3)/(SAT4) resolution unless
   explicitly reported. **`biv_core.py` will NOT be imported and
   `share3_pencil.py` will NOT be imported** - both have
   module-level writes outside my scope (r37 COMPLIANCE). **Nothing
   this round will be gated by bank 2's verifier.**
5. Two fields is not `q`-uniformity. No claim at official scale
   `q ~ 2^167`.
6. **I claim NO credit for**: Lueroth / the pullback lattice, the
   rational normal curve, the twisted cubic, the Segre dimension
   count, `(SPLIT-m)` / `(OV)` / `(OUT-m)` / `(DEG-m)`, the demand
   law, the constant-norm family, `K_{4,4}` minus a perfect
   matching. All are banked (r36 CATCH-24A, r37 CATCH-24A).
   CATCH-24A greps run before every novelty claim, hyphenated and
   infixed variants separately, `--exclude=dag.json` and the full
   `--exclude-dir` set at the SEARCH level on every recursive grep.
7. If D2 exhausts negative, the free-merge reading hardens only to
   a CONJECTURE with named falsifiers - never to an exclusion.

### R8 - THE BLIND PRIORS THE BRIEF DEMANDS

| quantity | prior |
|---|---|
| P(a correspondence-sharing pattern exists legally) | **0.07** (R1.2: derived dead) |
| P(the 3-in-3 degrees are stdlib-feasible) | **0.97** (R4.3: derived `<= 6`) |
| P(a 13-slope solution from D2) | **0.20** arm A / **0.45** arm B / **0.22** any verified |
| P(the dim-4 variety has `F_q`-points at `q=193`) | **0.60** |
| P(a non-uniform pattern survives at measured supply) | **0.03** |
| P(the sporadic deficit is exactly 20) | **0.75** |

**EXPECTED OUTCOME (a phrase):** *"the taxonomy collapses to the one
uniform pattern and the fence moves from incremental to
determinantal - a sharpened negative, not a witness."*

### R9 - EXPECTED MISSES (registered so they are graded, not excused)

- R9.1 I expect at least one registered dimension count (39, `-20`,
  4, rank `2r`) to be off by a small integer, most likely the
  `x`-degree budget `9 -> 40` coefficients.
- R9.2 I expect the naive rate `1.8e-4` to be wrong in the same
  direction r36's was - TOO LOW - because real-pencil `t_i` are
  multiplicatively structured.
- R9.3 I expect guard G3 to kill raw resultant hits, and I expect
  at least one raw "solution" that is a slope collision.
- R9.4 I expect the brief's "kernel dim 2 after 8 merges" to be the
  brief's slip and not mine (R4.2); if I am wrong, that is my miss.
- R9.5 I expect NOT to reach a witness, and I pre-commit to
  reporting the exact swept sample size and the exact solvability
  rate rather than a ceiling narrative.

# PREREG — collinearity_object (round 29)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

TWO round-28 pilots, quarantined from each other, found THE SAME
GEOMETRIC OBJECT from opposite sides. apolar_origin derived the
RECIPROCAL-LOCATOR NORMAL FORM: extremal type-2 slopes are exactly
points P_S = [1/(sigma'_W(x) sigma_S(x))]_{x in W} lying on the
pencil line; structured collinear families (rho+1 points, present at
EVERY field, killed by the banked counting layer) vs SPORADIC
collinearities that die with q (0.000 per word at q >= 97; the q=17
fence violation IS one sporadic triple) — and named the remaining
residual-budget proof obligation as "bound sporadic collinearities
of {P_S} at large w* over prime q > 2^167" with the heuristic
q^{-(3m-2)4m}. ssparse_endpoints, blind to that, measured F_COLL
(max collinear locator points) at 7-9x the random model (28 vs ~3-4
at q=65537) — real algebraic structure, 2^126 short of F2's need.
YOUR JOB: unify the two measurements into one theory of the
collinear structure of {P_S}, and attempt the sporadic bound.
Read first: notes/pilots_20260810/apolar_origin/{REPORT.md,
FABLE_AUDIT.md, d3_collinear.py, d5_sporadic.py};
notes/pilots_20260810/ssparse_endpoints/{REPORT.md, FABLE_AUDIT.md,
d2_sparse.py}; the round-28 addenda on
critical/nodes/rate_half_band_crossing_location/statement.md.

## Deliverables

**D1 — THE UNIFICATION.** Are ssparse's excess-collinear
configurations (F_COLL 10-34) exactly apolar's structured families
(the P_{U\{u}} = [A - uB] lines of size rho+1), sporadics, or a
third class? Compute BOTH functionals on THE SAME cells (register
the cell grid; 2-power; two fields per cell) and classify every
collinear family found: structured (rho+1, counting-layer-killed) /
sporadic / other. A third class would be a discovery; exact overlap
would let each side's results transport to the other.

**D2 — THE STRUCTURED CENSUS, COMPLETE.** apolar found the
structured lines and the flat 840 = C(10,4)*C(4,3) count at m=1.
Derive the complete structured-family census as a function of
(m, W): every parametric family of >= 3 collinear P_S points that
exists over every sufficiently large field, with its size, its
counting-layer status (killed or not — THE key safety question:
apolar verified killed for the P_{U\{u}} family; a structured
family that SURVIVES the counting layer would threaten the residual
budgets), and its exact count. Register the candidate list before
enumerating.

**D3 — THE SPORADIC BOUND (the main event).** The residual-budget
obligation in its sharpest form: over prime q, bound the number of
sporadic (non-structured) collinear (rho+2)-point configurations of
{P_S} on a pencil line. Routes to register: (a) the
Cayley-Bacharach / curve-degree route (P_S lies on an explicit
rational curve parameterized by S — collinearity is a determinantal
condition; count its solutions); (b) the character-sum route (the
sporadic count as an incomplete character sum — square-root
cancellation would give the q-decay the data shows); (c) the
specialization route (sporadics at q come from char-0 collinearity
specializing — bound the char-0 locus's degree and apply effective
Bezout/height bounds). EVEN A CONDITIONAL BOUND (e.g. under GRH or
a standard incidence conjecture) is bankable — state the hypothesis
exactly. The q=17 triple is your test case: your theory must
explain WHY q=17 supplies it and q >= 97 does not.

**D4 — THE PAYOFF MAP.** If a sporadic bound lands at any strength:
state exactly what it closes — the residual budgets {2^39, 2^39+1}
(via apolar's mechanism C + the closure band), and the bracket-top
extension chain (with the sliver arithmetic: q >= 2^167 + 2^128
for budget 2^39+1 alone; the pair for all q > 2^167). Re-derive,
do not cite.

## Escape tests (before the main work)

- Replay apolar's d5_sporadic.py (SCRATCH COPY; coordinator got
  IDENTICAL): the flat 840, the sporadic 0.167/0.000 split, the
  fence's triple.
- Replay ssparse's F_COLL numbers at one cell (SCRATCH COPY of
  d2_sparse.py): 28 at (16, tau=2, q=65537).

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4474; do not read the other round-29 pilot dirs
  (list_profile_bound, k_extremal, slack_recursion). Pass this
  clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root —
  including file patching and JSON peeking. RAMGUARD_TIMEOUT
  documented per use.
- BANKED SCRIPTS FROM SCRATCH COPIES ONLY.
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no
  bulk loads; checkpoint long runs; background batches with results
  files for >10-min runs.
- DRAFT-ONLY: writes only in
  notes/pilots_20260810/collinearity_object/; no dag/nodes/tools
  writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing;
  misses first. Name every measured functional (CATCH-19C).
  Two-field confirmation for structural claims. Own-repo grep
  before claiming anything is missing (CATCH-24A). Zero-power
  declarations where a claim quantifies over a max.
- Your final message IS the report. End with a compliance
  paragraph.

## Pilot registrations (appended by the pilot before any computation)

Appended 2026-08-10 by collinearity_object (Opus) with the Edit tool,
BEFORE any interpreter run. Inputs read first: apolar_origin
{REPORT.md, FABLE_AUDIT.md, d3_collinear.py, d3_collinear_results.txt,
d5_sporadic.py}; ssparse_endpoints {REPORT.md, FABLE_AUDIT.md,
d2_sparse.py}; critical/nodes/rate_half_band_crossing_location/
statement.md (all three round-28 addenda).

### R0 — NOTATION AND MEASURED FUNCTIONALS (CATCH-19C)

`D` = the multiplicative subgroup of `F_q^*` of order `N` (`N | q-1`).
`V ⊆ D`, `a = |V|`. For `T ⊆ D\V` write `sigma_T(X) = prod_{y in T}(X-y)`.

- **`L_T := [sigma_T(x)]_{x in V} in P^(a-1)`** — the DIRECT locator
  point (ssparse's `[p_Z]`, with `V = E`, `T = Z`).
- **`P_S := [1/(sigma'_V(x) sigma_S(x))]_{x in V}`** — the RECIPROCAL
  locator point (apolar's `(AO2)` normal form, `V = W`, `|S| = rho`).
- **`Lam(V,t) := {L_T : |T| = t}`**, **`Lam*(V,s) := {P_S : |S| = s}`**.
- **`F_COLL(q,N,V,t)`** (ssparse's functional, here generalised to any
  ambient) `= max over lines l of P^(a-1) of #(l n Lam)`.
- **`STRUCT3 / SPOR3`** (apolar's functionals) = number of collinear
  triples of `Lam*` with `|S_1 u S_2 u S_3| <= s+1` / `> s+1`.
- **`PEN(N,a,s) := s+1`** — the size of the linear (pencil) family.
- **`k`** = MOVING DEGREE of a collinear family: with `G = S_1 u S_2`,
  `I = S_1 n S_2`, `k := |G| - s = s - |I|`.
- **`d_x`** = number of members of a family whose locator vanishes at
  `x` (the counting-layer functional; the banked layer is `d_x <= e`).
- **`RIG := a - 1 - 2s`** — the RIGIDITY INDEX. `RIG >= 0` is the
  hypothesis of my main route. **`s_l`** (a line functional) `=` number
  of distinct `gamma in P^1` with `n_gamma >= 1`, `n_gamma = #{x in V :
  z_{0,x} + gamma z_{1,x} = 0}`.
- Official profile (as re-derived from apolar's numbers, to be
  re-verified): `N = 16m`, `rho = 4m-1`, `R+1 = 8m+1`, `e = m`,
  `a = w* in [4m+2, 8m-2]`, target `T <= rho+1 = 4m`, budgets
  `{rho+1, rho+2} = {2^39, 2^39+1}` at `m = 2^37`, `N = n = 2^41`.

### R1 — THE UNIFICATION HYPOTHESIS (registered, to be tested)

**(U1)** `P_S = Delta_V . L_T` with `T = (D\V)\S` and
`Delta_V = diag(x/N)_{x in V}`, i.e. the reciprocal-locator set and the
direct-locator set of complementary index size are the SAME point set up
to a fixed diagonal projective linear map. Proof sketch to be checked
numerically: `sigma_D(X) = X^N - 1`, `sigma'_D(x) = N/x` for `x in D`,
and `sigma'_D(x) = sigma'_{V}(x) sigma_{D\V}(x)`... applied to
`W u S`: `1/sigma'_{WuS}(x) = x sigma_{D\(WuS)}(x)/N`.
**Consequence if true:** the two pilots measured ONE functional
(`F_COLL`) on ONE object, at `(a,t) = (3,7)` [ssparse] and `(6,7)`
[apolar], both with `N = 16`.

### R2 — THE REGIME LAW (registered prediction, the D1 verdict I expect)

Collinearity of `Lam*(V,s)` is governed by `RIG = a-1-2s`:
- **RIGID (`RIG >= 0`)**: for `M >= 3` collinear points, multiplying
  `1/sigma_{S_i} = alpha_i/sigma_{S_1} + beta_i/sigma_{S_2}` by
  `sigma_{S_1}sigma_{S_2}sigma_{S_i}` gives a degree-`2s` polynomial
  vanishing on `V`, hence an identity; hence `sigma_{S_i} |
  sigma_{S_1}sigma_{S_2}`, hence `S_i ⊆ G := S_1 u S_2` for all `i`,
  and the `G\S_i` are DISJOINT fibres of a degree-`k` map. Predicted
  consequences: `M <= 1 + s/k <= s+1`, and `F_COLL = s+1` exactly.
- **FLOPPY (`RIG < 0`)**: no such identity; `F_COLL` may greatly
  exceed `s+1` (ssparse's 28 vs `s+1 = 7`).
- **The official stratum**: `s = R+1-a = 8m+1-a`, so `RIG >= 0` iff
  `a >= ceil((16m+3)/3)`; `m=1` forces `a=6, s=3, RIG = -1` — the
  fence sits exactly ONE below the rigid threshold.

### R3 — CANDIDATE STRUCTURED-FAMILY LIST (registered before enumeration)

Every field-independent collinear family should be the set of totally
`D\V`-split members of a pencil `{alpha f + beta g}` of degree-`s`
polynomials with fixed part `h = gcd(f,g)` and moving degree `k`:
- **(F1) LINEAR / PENCIL family** (`k=1`): `S_i = I u {u_i}`,
  `|I| = s-1`; size up to `min(s+1, N-a-s+1)`; present at every field.
  This is apolar's `P_{U\{u}} = [A - uB]` family.
- **(F2) COSET / CYCLOTOMIC family** (`k = h | N`): moving part
  `X^h - c`, fibres = cosets of `mu_h`; size up to `N/h`; present at
  every field with `h | N`. (apolar's R3 object.)
- **(F3) DIHEDRAL / INVERSE-PAIR family** (`k = 2h`): fibres
  `{u, zeta/u}` (`h=1`) or `u mu_h u zeta/(u mu_h)`; the pencil is
  `<X^2h + zeta, X^h>`; size up to `~N/2h`; present at every field.
  **I believe this one is NOT in the round-28 census; own-repo grep
  before claiming it (CATCH-24A).**
- **(F4) GENERAL degree-`k` pencils** (non-Galois): fibres of an
  arbitrary degree-`k` rational map; NOT field-independent — these are
  the sporadics.
Predicted counting-layer status for ALL of F1-F3 in the rigid regime:
either `∩S_i != {}` (then `d_x = M` on the intersection, so `M <= e`)
or the `G\S_i` exactly partition `G` (then `d_x = M-1` for every
`x in G`, so `M <= e+1`). **Prediction: NO structured family survives
the counting layer beyond size `e+1 = m+1`, and `m+1 <= 4m = rho+1`
for all `m >= 1` — i.e. no structured family threatens the budgets.**

### R4 — D3 ROUTE ORDER (registered)

**(a) determinantal / Bezout / curve-degree FIRST** (R2's identity plus
the fibre count `M k <= |G|`); then **(c) specialization** (only if (a)
leaves a gap); then **(b) character sums** (expected to be needed only
for the AVERAGE `q`-decay, not the max). Registered expectation: (a)
yields an UNCONDITIONAL bound in the rigid regime and (b) is needed only
to explain the `q=17` vs `q>=97` *frequency*, which is a mean statement
and therefore zero-power over the max (see R7).

### R5 — CELL GRID (registered before any run; 2-power `N`)

All cells `q`-two-field: **`q in {97, 65537}`** (both `= 1 mod 32`;
`65537 = 2^16+1`), plus **`q = 17` as a labelled small-field control**
(zero-power for structural claims, see R7).

| cell | N | a | s | t=N-a-s | RIG | regime |
|---|---|---|---|---|---|---|
| C1 | 16 | 3 | 6 | 7 | -11 | floppy (ssparse's) |
| C2 | 16 | 4 | 5 | 7 | -7 | floppy |
| C3 | 16 | 5 | 4 | 7 | -4 | floppy |
| C4 | 16 | 6 | 3 | 7 | -1 | boundary (apolar's, m=1) |
| C5 | 16 | 7 | 3 | 6 | 0 | rigid |
| C6 | 16 | 8 | 3 | 5 | 1 | rigid |
| C7 | 16 | 9 | 4 | 3 | 0 | rigid |
| C8 | 16 | 10 | 4 | 2 | 1 | rigid |
| C9 | 16 | 8 | 4 | 4 | -1 | boundary |
| C10 | 32 | 3 | 2 | 27 | -2 | floppy, direct-rigid |
| C11 | 32 | 12 | 5 | 15 | 1 | rigid |
| C12 | 32 | 14 | 6 | 12 | 1 | rigid |

Escape cells: apolar `(N,a,s,q) = (16,6,3,{17,97,113,193,241})`;
ssparse `(N,a,t,q) = (16,3,7,{17,97,65537})`.

### R6 — PREDICTIONS WITH NUMERIC WINDOWS (before any run)

- **P1** (escape) scratch replay of `d5_sporadic.py`: structured mean
  `840.000` at all five `q`; sporadic `0.167` at `q=17` and `0.000` at
  `q in {97,113,193,241}`; fence `W` sporadic count `= 1`. Exact.
- **P2** (escape) scratch replay of `d2_sparse.py`: `F_COLL` at
  `n_s=16`, `tau=2` `= 16 / 34 / 28` at `q = 17/97/65537`; `tau=3`
  `= 12 / 10 / 10`. Exact.
- **P3** (U1): identity holds for `100%` of `>= 256` random `(V,S)`
  at `q in {97, 65537}`, `N in {16,32}`. Any failure falsifies R1.
- **P4** (cross-pilot): my reciprocal-side code at `(N=16,a=3,s=6,
  q=65537)` over ssparse's first three rotation classes reproduces
  `F_COLL = 28` EXACTLY. (This is the unification's sharpest test.)
- **P5** (regime law, rigid side): `F_COLL = s+1` EXACTLY at C5, C6,
  C7, C8, C11, C12, at both fields. Window: `{s+1}`; anything `> s+1`
  falsifies R2.
- **P6** (boundary): at C4 and C9, `F_COLL = s+1` at `q in {97,65537}`
  and `F_COLL in [s+1, 3(s+1)]` at `q=17`.
- **P7** (floppy): C1 `F_COLL = 28` at `q=65537`, `34` at `q=97`;
  C2 `F_COLL in [7, 60]`; C3 `F_COLL in [5, 40]`; C10
  `F_COLL = 28` exactly (the `k=1` family at `s=2`: `N-a-s+1 = 28`).
- **P8** (the `q=17` test case): for the fence
  `W={1,2,3,5,7,11}`, `q=17`, its three pairwise-disjoint type-2
  supports satisfy `sigma_{S_1}sigma_{S_2} -
  sigma_{S_3}(alpha sigma_{S_2}+beta sigma_{S_1}) = c sigma_W`
  with `c != 0` — i.e. it fails R2's identity by exactly the boundary
  term. Predict `c != 0` (and `k = s = 3`, `M = 3 > 1+s/k = 2`).
- **P9** (family classification): in every RIGID cell the maximal
  collinear family has `k=1` (`|G| = s+1`, all `G\S_i` singletons).
  Predict 100% of maximal families; any `k>=2` maximal family in a
  rigid cell is a registered surprise.
- **P10** (counting layer): every maximal family satisfies
  `max_x d_x in {M-1, M}`. Predict 100%.
- **P11** (coverage arithmetic): combining apolar's `(AO1)` closure
  band `[4m+2, a_max(m)]` (to be re-derived from a SCRATCH COPY of
  their `d2_scan.py`) with my rigid band `[ceil((16m+3)/3), 8m-2]`
  leaves a gap of size `0, 1 or 2` for every `m in [2, 2^20]`;
  predict gap `= 0` exactly when `m = 0 mod 3`.
- **P12** (payoff arithmetic, re-derived not cited):
  `2^128 * (2^39+1) = 2^167 + 2^128` exactly; `2^128 * 2^41 = 2^169`;
  `2^41/(2^39+1) = 4 - 7.28e-12`, i.e. `4.000000` to six decimals but
  **NOT exactly 4**; `rho <= R-r = 2^34` at the low end.
- **P13** (registered miss-likely, honest): I do NOT expect to close
  either residual budget. Expected landing: an unconditional bound on
  the weight-extremal type-2 count on a band of `w*`, complementary to
  apolar's, with a small residual gap and the non-weight-extremal
  stratum untouched.

### R7 — ZERO-POWER DECLARATIONS

- Any `F_COLL` measurement in a FLOPPY cell (`RIG < 0`) has **zero
  power** over the official residual, because the official stratum has
  `s = R+1-a` and `RIG >= 0` for `a >= (16m+3)/3`; ssparse's 28 is a
  floppy-cell number and cannot transport upward. (This is a
  registered claim about my own headline: if R2 is falsified, the
  zero-power declaration falls with it.)
- Any `q=17` number is a small-field control only: at `q=17`,
  `N=16 = q-1`, so `D = F_q^*` and `m=1` is forced; no structural claim
  will rest on it. Two-field confirmation `{97, 65537}` for every
  structural claim.
- Any statement quantifying over a MAX (`F_COLL`, `T`, `w*`) will be
  reported with its own zero-power line where the measurement is a
  sample rather than an exhaustion.
- The `q`-decay of the sporadic count is a MEAN statement over random
  `W` and has **zero power** over the existence of a single bad `W`;
  route (b) is therefore explicitly NOT load-bearing for any bound I
  claim.

### R8 — COMPLIANCE PLAN

Scratch copies for every banked script (`d5_sporadic.py`,
`d2_sparse.py` + `ffield.py`, `d2_scan.py`), staged in the session
scratchpad and run unmodified. Every interpreter invocation under
`tools/ramguard tiny|local -- python3` from the repo root with
`RAMGUARD_TIMEOUT` documented. Writes confined to
`notes/pilots_20260810/collinearity_object/`. No subagents (so the
quarantine clause needs no propagation); `CAMPAIGN_LEDGER.md` never
opened; the three sibling round-29 pilot dirs never read. Own-repo grep
(CATCH-24A) before claiming (F3) is new, before claiming the counting
layer `d_x <= e` is banked, and before claiming R2's identity is new.


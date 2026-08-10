# PREREG — apolar_origin (round 28)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

THE NAMED THEOREM TARGET of the RH-AC program
(rate_half_band_crossing_location, created in the band
decomposition). Round 27's staircase_extension diagnosed the
wave-10 residual budgets {2^39, 2^39+1} TO THE UNIT: the counting
layer's cap (ERC2) is exactly ONE SLOPE above the target at the
first live degree, the cap is ATTAINED by non-Hankel objects (9
collinear disjoint split cubics at N=28 with Hankel nullity 0 —
exact certificates banked at
notes/pilots_20260809/staircase_extension/d1_realizability*), and
the m=1 fence (rate_half_ca_hankel_strict_m1_corefree_five_slope_
route_fence, PROVED, explicit F_17 witness) proves NO
incidence/core-freeness/split-fiber/Hankel-equation argument closes
the endpoint uniformly. The truth evidence is prime-field clean
(the only scaled violation is a q=17 smallest-field artifact; and
rate_half_residual_prime_field_collapse (PROVED) forces the
residual onto prime fields q > 2^167). YOUR JOB: prove the two
budgets by adding the missing ingredient — the APOLAR ORIGIN of the
Hankel system, i.e. the fact that realizable far-CA configurations
arise from an apolarity/kernel structure the design-cap-attaining
configurations lack. The round-27 cyclotomic law is your model
result: "realizable exactly when it does not exceed the target" —
that law, proved uniformly, IS the theorem.

## Deliverables

**D1 — THE MECHANISM EXTRACTION.** From the banked material (the
m=1 fence's proof; the realizability certificates; the Hankel suite
nodes' proofs — read them, they state their own domains), extract
exactly WHAT distinguishes a realizable configuration from a
design-cap-attaining one. The round-27 data says: over-target
instances have Hankel nullity 0; at-or-below-target instances have
positive nullity. Register a candidate characterization (an exact
condition C on configurations such that realizable => C and C =>
count <= target) BEFORE attempting the proof.

**D2 — THE PROOF ATTEMPT (the main event).** Prove, for the two
residual strata (w10-H1: budget 2^39 = strict A=3, s=0, e in
[2^37, floor((2^39-1)/3)]; budget 2^39+1 = A=3 e >= 2^37+1 plus
A=1 rows): every REALIZABLE configuration satisfies T <= rho+1.
Routes to consider (register your order): (a) uniformize the
cyclotomic realizability law — show every cap-attaining family is
cyclotomic-type and inherits the law; (b) the apolarity route —
the Hankel system M_r(y_0+Zy_1)Q(Z)=0 has an apolar/annihilator
interpretation; show cap saturation forces nullity 0 by a rank
argument uniform in the scale; (c) the one-slope route — the
deficit is exactly 1, so a parity/involution argument that any
realizable T = rho+2 configuration contains a forbidden
sub-structure. PARTIAL RESULTS ARE BANKABLE: the theorem at one of
the two budgets, or on a sub-stratum (e.g. e = m sharp face only),
each has named payoff.

**D3 — VERIFICATION.** Machine-check whatever lands at every
accessible scale (the round-27 harness: d1_realizability.py,
d1_cyclotomic_threat.py, d3_scale_field_census.py — SCRATCH
COPIES). The theorem must reproduce: the q=17 violation (your
statement must EXCLUDE q=17 by an explicit hypothesis, not ignore
it), the prime-field cleanliness, and the nullity dichotomy.

**D4 — THE PAYOFF, PRICED EXACTLY.** If D2 lands: state the
corollary chain — the far-CA layer extends to r <= 2^39+1, (RQ4)
completes, the crossing formula a_RH = n - B + 1 becomes
unconditional on all 2^128 < q < 2^167 WITHOUT residual, AND the
bracket top a_RH <= 3n/4 extends from q >= 2^169 to all q > 2^167
(the round-27 D4 cross-link — re-derive it, do not trust it). If
D2 does not land: the sharpest statement of what the apolar route
still lacks, with the failed attempts as evidence.

## Escape tests (before the main work)

- Replay d1_realizability.py + d1_cyclotomic_threat.py (SCRATCH
  COPIES; coordinator got byte-identical).
- Reproduce the m=1 fence's F_17 witness from the node's own
  verifier.

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4302; do not read the other round-28 pilot dirs
  (ssparse_endpoints, maxscan_algorithm, mca_safe_rewire). Pass
  this clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from
  /home/u2470931/smooth-read-solomin/prize — including file
  patching and JSON peeking. RAMGUARD_TIMEOUT documented per use.
- BANKED SCRIPTS FROM SCRATCH COPIES ONLY.
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no
  bulk loads; checkpoint long runs; background batches with
  results files for >10-min runs.
- DRAFT-ONLY: writes only in notes/pilots_20260810/apolar_origin/;
  no dag/nodes/tools writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing;
  misses first. Name every measured functional (CATCH-19C).
  Own-repo grep gates every "missing ingredient" claim (CATCH-24A)
  — four missing-theorem claims in a row were bookkeeping; check
  whether the apolar characterization already exists under another
  name before building it.
- Your final message IS the report. End with a compliance
  paragraph.

## Pilot registrations (appended by the pilot before any computation)

Appended by apolar_origin (Opus) 2026-08-10, with the Edit tool, BEFORE any
interpreter run. Reading of repo primary text and of the round-27 banked
material preceded this; no computation did.

### M0 — CATCH-24A gate (own-repo grep, run before every "missing" claim)

Greps run (read-only, no interpreter): `apolar`, `catalecticant|inverse
system|macaulay|annihilat`, `realizab`, `coset`, `minimum-weight|minimal
support|unique decoding|uniquely decodable` over `background/nodes` and
`critical/nodes`. Findings that pre-empt parts of my mandate, disclosed
up front:

- `rate_half_ca_hankel_minimal_index_budget` already names the object
  "apolar generator `Q_Z`" and states the argument is the divided-power
  apolar action with the syndrome Hankel matrix as the literal
  catalecticant. **The apolar origin is NOT a missing name.**
- `rate_half_ca_hankel_endpoint_saturation_rigidity` (PROVED) is the
  counting layer: `T<=4m+1`, `sum_x (m-d_x)=1+O`, `>=15m` saturated
  columns.
- `rate_half_ca_hankel_endpoint_rational_normal_kernel_curve` (PROVED)
  already gives the degree-`m` rational normal kernel curve and names the
  residual gate: "a rigidity theorem for this rational normal kernel curve
  together with its Hankel/apolar origin".
- `rate_half_ca_hankel_endpoint_norm_factorization` (PROVED) already has
  the norm-power identity `J R = H^rho S` and the product-code reading.
- **`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_minimal_
  support_uniqueness` and `..._quotient_minimal_support_packing` (both
  PROVED) already run a minimal-support-uniqueness + disjoint-cancellation
  + Johnson-packing argument of exactly the species I intend to use,** on
  the `A=1` core-one exceptional-only quotient face. `(QMU5)`
  `floor(2e/(h-1))` is the same shape as my type-1 count and `(QMP1)`
  `lambda_h=2h-2e-4` is the same MDS-distance intersection bound.
  So my D1 mechanism is **a port, not an invention**; what I claim as new
  is (i) its formulation for the FULL strict `A=3` pencil rather than a
  core quotient, (ii) the type-1/type-2 dichotomy driven by the two MDS
  codes `K`, `K'` below, and (iii) the two corollaries R3/R4.
- `rate_half_ca_hankel_distance_three_e1_hankel_design_route_fence`
  (PROVED) is a SECOND design-vs-Hankel fence beyond the `m=1` fence the
  brief named.

### R0 — Notation (mine, fixed here)

Strict endpoint: `D=mu_N` with `N=16m | q-1`, `R=8m`, `k=8m`,
`r=rho=4m-1`, `A=3`, `e=m`, `s=0`, `delta=m-1`.

- `K := {c in F^D : sum_x c_x x^i = 0, 0<=i<R}` — the **kernel code**; it
  is `[N, N-R, R+1] = [16m, 8m, 8m+1]` MDS (BCH/Vandermonde).
- `K' := {psi in F^D : sum_x psi_x x^i = 0, 0<=i<=R-r-1=4m}` — the
  **apolarity code**; `[16m, 12m-1, 4m+2]` MDS.
- `w(y)` = minimum weight of a `D`-supported representation of the
  syndrome `y`. `w*` = minimum joint support size of the pair
  `(y_0,y_1)`; column-far `<=> w* > r`.
- `S_gamma` = support of the minimum-weight representative `v_gamma` of
  the coset of `y(gamma)`; `|S_gamma| = u_gamma = rho - o_gamma`.
- `W` = a joint support (e.g. `S_gamma u S_gamma'`), `a=|W|`,
  `(c_0,c_1)` its (unique when `a<=R`) representation,
  `n_gamma = #{x in W : c_{0,x}+gamma c_{1,x}=0}`,
  `z_gamma = c_0+gamma c_1` (supported in `W`).

### R1 — D1 CANDIDATE CHARACTERIZATION `C` (registered before testing)

For a collinear family of split squarefree degree-`rho` locators
`{Q_gamma}_{gamma in Z}` over `D`, with root sets `S_gamma`:

- **(C0) Coset origin.** Hankel-realizable by a column-far pencil `=>`
  there is a 2-dimensional space of `K`-cosets (a projective line in
  `F^D/K`) such that `S_gamma` is the support of the UNIQUE minimum-weight
  representative of the `gamma`-th coset. Uniqueness is legitimate because
  `2 rho = 8m-2 < 8m+1 = d(K)`.
- **(C1) Injectivity.** `gamma |-> S_gamma` is injective on supported
  slopes. (Two equal supports of size `<= r` make the pair jointly
  supported on `<= r` points, i.e. NOT column-far.)
- **(C2) Dichotomy.** For every joint support `W` (`a=|W|<=2rho`) and
  every supported `gamma`, exactly one of
  - **type-1**: `S_gamma = W \ K_gamma`, i.e. `n_gamma = a-rho+o_gamma`;
  - **type-2**: `psi_gamma := z_gamma . Q_gamma|_D` is a nonzero word of
    `K'`, forcing `|S_gamma \ W| >= (R+1) - a + n_gamma` and
    `|S_gamma n W| <= a - n_gamma - (R-r+1)`.
- **(C3) Degree cap on type-1.** The `F[Z]`-valued word
  `Psi(Z) = ((c_{0,x}+Z c_{1,x}) Q(Z;x))_{x in D} in K'[Z]` has
  `deg_Z <= e+1` and is not identically zero when `s=0`; its common root
  set is exactly the type-1 slope set, so `T_1 <= e+1 = m+1`.
- **(C4) Counting layer (banked).** `d_x <= e = m`,
  `sum_x (m-d_x) = 1+O`, `O <= delta = m-1`.

Derived cap, replacing `(ERC2)` by a `W`-indexed bound:

```text
T <= min( m+1, floor(a/(a-rho)), floor((a m + O)/rho) )
     + floor( ((N-a) m) / ((R+1) - a) ) ,     a < R+1.      (AO1)
```

`C => T <= rho+1` is what must be checked; I do NOT claim it holds for
all `a`. I claim `realizable => C`, and I will MEASURE the set of `(m,a,O)`
on which `C => T <= rho+1`.

### R2 — Route order (registered)

1. **(b) apolarity/MDS-coset route** — primary, the whole of R1.
2. **(c) one-slope route** — secondary; the deficit is exactly 1, so I
   look for a forbidden sub-structure at `T=rho+2` via `(AO1)` equality.
3. **(a) cyclotomic uniformization** — tertiary; I expect `C1` alone to
   kill it at official scale, so I run it as a corollary, not a route.

### R3 — Registered claim (to be proved, not yet proved)

**Cyclotomic exclusion at official scale.** If every supported-slope root
set is a coset of a fixed subgroup `mu_rho <= mu_N` (`rho | N`), then
`C1` gives `T <= N/rho`. At the official `A=1` half-distance profile
(`rho=2^39`, `N=2^41`) this is `T <= 4`, far below `rho+1`; at the strict
`A=3` profile `rho=4m-1` does not divide `N=16m` for `m>=1`, so the family
is empty there. Hence the round-27 structural threat dies uniformly in `q`.

### R4 — Registered claim (to be proved, not yet proved)

**Disjoint-support fence.** A column-far pencil whose supported root sets
are pairwise disjoint needs both `T rho <= N` and `A <= rho`
(from `|S_gamma \ W| >= R+1-2rho = A` and `|S_gamma| = rho`). At `A=3`:
`T rho <= N` reads `(4m+1)(4m-1) <= 16m`, true only for `m=1`. This is my
proposed explanation of BOTH banked certificates at once.

### R5 — Explicit `q=17` exclusion hypothesis (required by the brief)

Every statement I assert carries the hypothesis **`m >= 2`** (equivalently
`N >= 32`, `rho >= 7`). This excludes the `m=1` fence witness by
hypothesis rather than by neglect. Note `q=17` forces `m=1`: `N=16m` must
divide `q-1=16`. So "`m>=2`" implies `q>=97` on the admissible list, and
is vacuous at official scale (`m=2^37`).

### Predictions with numeric windows (registered before computing)

- **P1 (escape).** Scratch copy of `d1_realizability.py` reproduces
  round-27 exactly: nullities `1 / 0 / 3`; case (a) `T=5`, case (c) `T=4`;
  fence line parameters `[0,1,2,4,15]`. Window: exact, 0 deviations.
- **P2 (escape).** Scratch copy of `d1_cyclotomic_threat.py` reproduces
  all 7 rows of `d1_cyclotomic_results.txt`. Window: exact, 7/7.
- **P3 (fence witness under `C`).** For the `m=1` `F_17` witness the five
  minimal supports equal the five triples of `(M1F3)`; they are pairwise
  DISJOINT; `w* = 6`; for `W=S_1 u S_2` (`a=6`): `T_1 = 2` exactly and
  `T_2 = 3` exactly; every type-2 slope has `S_gamma n W = {}` and
  `|S_gamma \ W| = 3`, meeting `|S \ W| >= R+1-a = 3` with EQUALITY.
  `(AO1)` returns exactly `2+3 = 5 = rho+2`. Window: all six numbers
  exact; `(AO1)` value in `{5}`.
- **P4 (`N=28` 9-line under `C`).** The nine triples are pairwise
  disjoint. `(R4)` needs `A <= rho`, i.e. `9 <= 3`: FALSE. So `C`
  refutes realizability with NO linear algebra, and the refutation must
  agree with round-27's `nullity = 0`. Window: predicted type-2 lower
  bound `R+1-a = 15-6 = 9 > 3 = |S_gamma|`, contradiction margin exactly
  `6`; `T` forced to `2`.
- **P5 (cyclotomic law under `C`).** The round-27 law "realizable exactly
  when it does not exceed the target" is explained by `C1`: the number of
  DISTINCT root sets is `N/rho`, so `T <= N/rho`. Predicted per-row:
  `N=16 rho=4` -> `4` distinct sets, design `T=8` and `16` -> repeats ->
  nullity 0; `N=24 rho=6` -> `4`, design `8` -> repeats -> nullity 0;
  `N=12 rho=3` -> `4`, design `4` -> no repeat -> nullity `>0`;
  `N=20 rho=5` -> `4`, design `4` -> no repeat -> nullity `>0`.
  Window: 7/7 rows must match sign (`repeat <=> nullity 0`).
- **P6 (`(AO1)` closure scan).** I will tabulate, for `m` in `[1,40]`,
  `a` in `[rho+1, 2rho]`, `O` in `[0, m-1]`, whether `(AO1) <= rho+1`.
  Registered prediction: closure holds at `a = 4m+2, O = 0` for every
  `m >= 2` and FAILS at `m=1` (the fence). Registered window for the
  closure band width `#{a : (AO1)<=rho+1}` at `O=0`: I predict a NARROW
  band, `1 <= width <= 4`, containing `a=4m+2`, for every `m` in `[2,40]`.
  I predict `(AO1)` does NOT close the endpoint for all `a` — i.e. the
  uniform theorem does NOT land this session (registered as a MISS).
- **P7 (`O` sensitivity).** I predict the `a=4m+2` closure is destroyed by
  `O >= 1` at `m=2` (bound returns `4m+1` not `4m`), so any theorem I bank
  carries the hypothesis `O=0` or an `O`-corrected `a` window. Window:
  `(AO1)(m=2,a=10,O=1) = 9 = rho+2`.
- **P8 (scaled reproduction, D3).** At the first scale above the fence
  (`m=2`: `N=32`, `R=16`, `r=rho=7`, `e=2`, `A=3`, `q=97`), I predict NO
  realizable column-far pencil with `T = rho+2 = 9` is found by the
  structured searches I can afford, and I predict the disjoint-support
  mechanism is arithmetically impossible there (`9*7=63 > 32`). Window:
  0 witnesses found; `63 > 32` exact.
- **P9 (D4 payoff, re-derived from primary text).** Far-CA caps at the
  razor bracket ends reproduce round-27 finding 4 exactly: `2^34` at
  `a=k+2^34` and exactly `n=2^41` at `a=3n/4`; and the `q>=2^169`
  condition on `a_RH<=3n/4` is imposed by the `A=1` half-distance far-CA
  term alone, so closing budget `2^39+1` extends it to all `q>2^167`
  (a 2-bit window). Window: both constants exact; the extension exponent
  pair `(169,167)` exact.
- **P10 (verdict shape).** Registered in advance: I expect a PARTIAL
  landing — the mechanism `C` + R3 + R4 + a per-stratum closure — and NOT
  the uniform theorem. Anything better is an upside; anything worse
  (e.g. `C` failing on a banked certificate) is a registered falsification
  of `C`.

### ADDENDUM (post-registration, marked as such): the extremal normal form

**Derived AFTER computation began** (it is a consequence of `C2`, not an
independent hypothesis), and registered here BEFORE the experiment it
predicts. Any number produced by it is an UNREGISTERED-at-dispatch
measurement and is labelled so in the report.

Let `W` be a joint support with `a=|W|`, and let `gamma` be a type-2
supported slope in the EXTREMAL case `n_gamma=0`, `S_gamma n W = {}`,
`a+rho = R+1`. Then `kappa_gamma = z_gamma - v_gamma` is a codeword of `K`
of weight exactly `R+1` supported exactly on `W u S_gamma`. Because `K` is
`[N,N-R,R+1]` MDS, that codeword is unique up to scalar and is explicitly
`kappa_x = 1/sigma'_{W u S}(x)`. Restricting to `W` (`sigma_W(x)=0` there)
gives `sigma'_{W u S}(x) = sigma'_W(x) sigma_S(x)`, hence

```text
z_gamma|_W  is proportional to  ( 1/(sigma'_W(x) sigma_{S_gamma}(x)) )_{x in W}.
```

Define the **reciprocal-locator point set**
`P_S := [ 1/(sigma'_W(x) sigma_S(x)) ]_{x in W} in P^(a-1)`,
for `S` a `rho`-subset of `D \ W`. Since `z_gamma = c_0+gamma c_1` runs
over a LINE `L` of `P^(a-1)`, the extremal type-2 slopes are exactly the
`S` with `P_S in L`. So:

**(AO2)** `T_2^extremal <= max over lines L of #{S : P_S in L}`.

Predictions registered now, before running:

- **A1.** For the `m=1` fence (`q=17`, `W=S_0 u S_1={1,2,3,5,7,11}`), the
  three type-2 supports `{9,12,13}`, `{4,6,16}`, `{8,10,15}` give `P_S`
  points that are EXACTLY collinear, and the line is the pencil line.
  Window: exactly 3 of 3 on one line; reconstructed `(c_0,c_1)`
  proportional to the measured `z` vectors.
- **A2.** The `q=17`-only phenomenon is a POINT-COUNT coincidence.
  Heuristic count of collinear triples among the `M=C(10,3)=120` points
  `P_S in P^5` is `C(M,3)/q^4 = 280840/q^4`. Registered windows for the
  MEAN number of collinear triples per `W`, over sampled `W`:
  `q=17` in `[1.0, 8.0]` (heuristic 3.36);
  `q=97` in `[0, 0.05]` (heuristic 0.0032);
  `q=113` in `[0, 0.05]` (heuristic 0.0017);
  `q=193` and `q=241` in `[0, 0.02]`.
  And: at `q=17` at least one sampled `W` carries a line with `>=3`
  points; at `q>=97` I predict NO sampled `W` does.
- **A3.** At `m=2` (`N=32`, `rho=7`, `a=10`, `q=97`) the required
  extremal type-2 count is `3m=6`. [A2/A3 as first registered were WRONG —
  see ADDENDUM 2.] Heuristic expected number of collinear
  TRIPLES per `W` is `C(M,2) M q^(-(a-2))/3` with `M=C(22,7)=170544`,
  `= 0.11`; expected number of 6-point lines `~1e-33`. Registered window:
  the sampled search finds max collinear count `<= 2` and ZERO lines with
  `>= 3`; certainly zero with `>= 6`.

### ADDENDUM 2 (post-A2, registered before the corrected run)

A2 as registered was **wrong**, and the measurement falsified it at every
field: `mean trip(W) = 840.0` and `max collin(W) = 4` at
`q = 17, 97, 113, 193, 241` alike — flat in `q`, so the collinearity is
NOT an arithmetic coincidence. Diagnosis, derived from the miss:

`840 = C(10,4) * C(4,3)`. For any `(rho+1)`-subset `U` of `D\W` and
`u in U`, `S = U\{u}` gives `sigma_S(x) = sigma_U(x)/(x-u)`, hence

```text
P_(U\{u}) = [ (x-u) / (sigma'_W(x) sigma_U(x)) ]_{x in W} = [A - u B],
A_x = x/(sigma'_W(x)sigma_U(x)),   B_x = 1/(sigma'_W(x)sigma_U(x)).
```

So the `rho+1` points `{P_(U\{u})}` are collinear **for every `U`, over
every field**. Call these the **structured lines**; everything else is
**sporadic**.

Corrected registrations, before the corrected run:

- **A2'.** Structured lines carry exactly `rho+1` points and are KILLED by
  the banked counting layer: their supports `U\{u}` give `d_x = rho` for
  `x in U`, and `d_x <= e = m` requires `rho <= m`, i.e. `4m-1 <= m`,
  false for all `m >= 1`. Window: structured line size exactly `rho+1`
  (`=4` at `m=1`, `=8` at `m=2`), `d_x` exactly `rho`.
- **A3'.** The real threat is SPORADIC collinearity (triples whose union
  exceeds `rho+1` points). Registered windows for the mean number of
  sporadic collinear triples per random `W` at `m=1`
  (heuristic `(C(120,3)-840)/q^4 = 280000/q^4`):
  `q=17` in `[0.5, 12]`; `q=97` in `[0, 0.05]`; `q=113` in `[0, 0.05]`;
  `q=193`, `q=241` in `[0, 0.02]`.
- **A4.** The `m=1` fence's OWN `W = {1,2,3,5,7,11}` at `q=17` must be
  sporadic-rich: I predict `sporadic_trip(W_fence) >= 1` (it contains the
  fence's own pairwise-disjoint triple), and I predict a random `W` at
  `q=17` typically has `0`. Window: `sporadic_trip(W_fence) in [1, 30]`.


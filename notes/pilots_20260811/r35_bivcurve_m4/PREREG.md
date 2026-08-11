# PREREG — r35_bivcurve_m4 (round 35)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r34_bivcurve_m34/REPORT.md` (round 34)
2. `background/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LINEAR_HYPERGRAPH_COMPILER.md`

## Mandate

THE m = 4 DECISION + THE PARITY FALSIFIER. Round 34 realized
(BIV-CURVE) at m = 3 ((SPLIT-m) + involution) and left m = 4 OPEN
as a searched negative over EXACTLY ONE ansatz class ((SPLIT-4)
with sigma(x) = -x and the forced 3+3+2 split; ceiling 7 of 12
triples). Its own report names the three unexplored routes (its
F2): (a) NON-SPLIT G; (b) sigma(x) = c/x (two fixed points on
mu_64 — a different orbit structure); (c) the un-symmetrised
(3,3,3) split. The obstruction it measured is the (OV) pair cap
forcing the 12 shared slope-triples into a LINEAR 3-uniform
hypergraph — and the repo already holds a PROVED
linear-3-uniform-hypergraph compiler (anchor 2, the u1_x4 lane:
pair-uniqueness forcing linearity, plus finite guardrails) that
the round-34 pilot's grep missed. YOUR JOB: decide m = 4, or
tighten its obstruction to the wider class with the scope stated
exactly; and run the cheap m = 5 parity experiment either way.

## Deliverables

**D1 — THE m = 4 DECISION PROGRAM.** Routes (a)/(b)/(c) in
whatever order your registered analysis ranks them, plus the
compiler import: transport anchor 2's machinery to the m = 4
selection problem (12 triples, degrees <= 3, <= 15 slopes) — does
pair-uniqueness + the guardrails DECIDE satisfiability of the
selection layer, separating it cleanly from the arithmetic
(value-coincidence) layer? Round 34's supply/demand analysis says
the shortfall is in the cross-coincidence term (even-m
sigma-invariant factor injective on orbits) — route (b) changes
exactly that term (fixed points!), so derive its orbit arithmetic
BEFORE searching. Either outcome certified: a witness (full
incidence + (BIV-CURVE) table, two fields) or the obstruction
extended with named scope (what class is excluded, what remains
untouched).

**D2 — THE m = 5 PARITY FALSIFIER.** (SPLIT-5)+sigma all-swapped
(m-1 = 4 factors, no invariant factor forced). A witness CONFIRMS
the parity prediction (odd m easy / even m obstructed, currently 2
data points); a failure REFUTES it. Also check the round-34
caution: at m = 5 the (OV) cap m-1 = 4 re-admits tuple
multiplicity 4 — does the linearity constraint really vanish, and
does that change the selection problem's character?

**D3 — (OUT-m) STRESS TEST, CORRECTED FORM.** The coordinator's
corrections are on the node (round-34 (BIV-CURVE) addendum,
`critical/nodes/rate_half_band_crossing_location/statement.md`):
per-slope X' + 2X'' >= m-1 - eps~ with eps~ <= 1+O; aggregate
(m-1)(1+O); the X = 0 corollary gated on O <= m-3. Stress-test the
corrected statement on every configuration this round produces
(m = 4 candidates, m = 5 witnesses, deficient-point placements
inside vs outside W — the case that refuted the original rider).
A violation of the CORRECTED form is a registered falsifier of a
coordinator-audited statement: report it loudly if it fires.

**D4 — VERDICT.** The (BIV-CURVE) m-boundary of record, updated;
misses first; cross-pilot flag (do NOT read siblings) for anything
bearing on layer A or the realizability layer.

## Blind priors to register

P(m = 4 realizable via route (a)), P(via (b)), P(via (c)),
P(the m = 5 parity witness lands), P(the u1_x4 compiler transports
usefully), P(the corrected (OUT-m) survives all stress).

---

## Pilot registrations

Appended with the Edit tool after reading EXACTLY the two named anchors
(`r34_bivcurve_m34/REPORT.md`,
`background/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LINEAR_HYPERGRAPH_COMPILER.md`)
and BEFORE any other read, any grep, any `ls`, and any interpreter
invocation.

### R0 — notation (from anchor 1, not re-derived)

`m`; `N = 16m`; `D = mu_N ⊂ F_q^*` (`N | q-1`); `rho = 4m-1`; `R = 8m`;
`e = m`; `T = rho+2`, `T_1 = 2` (`g,h`), `T_2 = rho`;
`a = w* = a* = 7m-1`; `delta = m-1`; `|S_g ^ S_h| = 2rho-a = m-1`;
`|S_g D S_h| = 2(a-rho) = 6m`; `(OV)` cap `|S_al ^ S_be| <= 2rho-a = m-1`;
per-slope cap `X_gamma <= 2m-2`, per-side `|S_gamma ^ S_g| <= m-1`;
`(SAT4)`: `sum_x (m - d_x) = 1 + O`, `O <= delta = m-1`.
`(SPLIT-m)`: `G = prod_{j=1}^{m-1}(u_j(x)Z - v_j(x))`, `deg u_j,v_j <= 3`,
`sum_j deg_x <= 3m-3`.

### R1 — THE INVARIANT-FACTOR LEMMA (derived before any search)

**R1.1.** For ANY involution `sigma` of `P^1` over `F_q`, the invariant
subfield is `F_q(w)` for a single degree-2 quotient coordinate
(`w = x^2` for `sigma(x) = -x`; `w = x + c/x` for `sigma(x) = c/x`). A
`sigma`-invariant `(SPLIT-m)` factor has `chi = v/u ∈ F_q(w)` with
`deg_x <= 3`; after cancelling the forced common factor it is a **Möbius
map in `w`**, hence `deg_x chi = 2` and **`chi` is INJECTIVE ON
`sigma`-ORBITS**. Registered `P(true for both involutions) = 0.90`.
Falsifier: an invariant factor of `deg_x <= 3` that is 2-to-1 or 3-to-1
on orbits.

**R1.2 (catch on anchor 1, registered before checking).** Therefore the
`x`-degree of any invariant factor is **EVEN**, so at `m = 4` the
`(SPLIT-4)+sigma` degree split is **`(3,3,2)`, total 8 < 9 — NOT
`(3,3,3)`**. Anchor 1 asserts both: `(3,3,3)` "forced" at its D3.1,
`3+3+2` at its MISS 1 / D3.3. I predict `3+3+2` correct and the
`(3,3,3)`-forcing argument false as stated. `P = 0.90`.

**R1.3 (the brief's route-(b) hypothesis, pre-registered as PREDICTED
FALSE).** The brief says `sigma(x) = c/x` "changes exactly that term
(fixed points!)". By R1.1 the invariant factor of `x ↦ c/x` is Möbius in
`w = x + c/x`, hence **still injective on orbits**.
`P(route (b) removes the injectivity) = 0.10`.

### R2 — FIXED-POINT ARITHMETIC of `sigma(x) = c/x` on `mu_N`

**R2.1.** `sigma` preserves `mu_N` iff `c ∈ mu_N`; `Fix = {x : x^2 = c}`
has size **2 if `c ∈ (mu_N)^2 = mu_{N/2}`, else 0** (`N` even). So
`#Fix ∈ {0,2}` — **never odd**. `P = 0.95`.

**R2.2.** At `x0 ∈ Fix` the swapped pair collapses
(`phi(x0) = phi(sigma x0)`), so `G(.,x0)` has a repeated root,
`|A_{x0}| <= m-1`, and `x0` is a **deficient point** charged to `(SAT4)`
(`budget 1+O <= m`). Predicted placements: outside `W` (free), or as a
middle / deficient `Delta`-point (1 unit each, behaving like a middle:
`m-2` prescribed roots + 1 free root that absorbs the repeat).

**R2.3 (middle-parity).** `|S_g ^ S_h| = m-1` is ODD for even `m`; a
`sigma`-stable set of odd size needs an odd number of fixed points;
`#Fix ∈ {0,2}` ⟹ **no involution of either named family makes `W`
`sigma`-stable at even `m`**. `P = 0.85`.

**R2.4 (route (b) is not cheaper).** With both fixed points in
`S_g D S_h`: `24 = 2 + 11 orbits`, slot count `11*3 + 2*2 = 37` into
`<= 15` slopes ⟹ `>= 22` coincidences, versus `21` for route (a).
**PREDICTION: route (b)'s coincidence demand is `>=` route (a)'s.**
`P = 0.80`.

### R3 — `(SUPPLY-CODIM)`: the calibrated excess model (HEURISTIC)

For an ansatz class `C`: `P(C)` = projective parameter count of the
pencil data (**7 per free degree-3 pencil**; **3 per `sigma`-invariant
factor**, by R1.1); `D(m,C)` = (type-2 slope SLOTS carried by
`S_g D S_h`) − (distinct type-2 slopes available to them, `rho - 1`):

```text
sigma-symmetric : slots = 3m(m-1)     D = 3m^2 - 7m + 2
un-symmetrised  : slots = 6m(m-1)     D = 6m^2 - 10m + 2
EXCESS  E = P - D
```

Registered table (to be reproduced by hand and by code):

```text
m=2, one free pencil, no involution : P= 7  D=  5   E = +2   CALIBRATION (realizable)
m=3, sigma-split (1 swapped pair)   : P= 7  D=  8   E = -1   CALIBRATION (marginal; witness at trial 632 / 24939)
m=4, sigma-split (1 pair + 1 inv)   : P=10  D= 22   E = -12
m=4, route (b) (2 fixed points)     : P=10  D= 23   E = -13
m=4, route (c) un-symmetrised       : P=21  D= 58   E = -37
m=5, sigma-split (2 swapped pairs)  : P=14  D= 42   E = -28
```

**R3.1 PREDICTIONS.** (i) no witness at `m = 4` or `m = 5` in any class
I can search; (ii) **parity is NOT the mechanism** — upgrading the
invariant factor to a free pencil (`P: 10 -> 14` at `m=4`) still leaves
`E = -8`; (iii) the ceiling on selection size under random pencils is set
by the ensemble coincidence supply, not by the combinatorics.
**FALSIFIER F-CODIM: any witness at `E <= -5` refutes the model.**

**R3.2 THE DECISIVE FORK (registered).** Anchor 1's parity prediction
(odd `m` easy / even `m` obstructed) and `(SUPPLY-CODIM)` **agree at
`m=3,4` and DISAGREE at `m=5`**: parity predicts a witness,
`(SUPPLY-CODIM)` predicts `E = -28` and none. These are mutually
exclusive; I will report whichever fires.
`P(m=5 witness lands) = 0.10`.

### R4 — THE SELECTION-LAYER IMPORT (anchor 2)

**R4.1.** Anchor 2 proves pair-uniqueness ⟹ linear 3-uniform hypergraph
(`F3_H3_REPEAT_LINEAR_HYPERGRAPH_COMPILER.md:31,35-39`). At `m=4` the
`(OV)` cap `m-1 = 3` gives the same conclusion for the 12 shared
slope-triples. **PREDICTION: the transport is exact in FORM but OPPOSITE
in EFFECT** — the abstract problem "12 linear triples, max degree 3,
`<= 15` vertices" is **SATISFIABLE** (`36 <= 45` slots; predicted
certificate: 12 blocks drawn from 3 parallel classes of a Kirkman triple
system `KTS(15)`, every vertex of degree `<= 3`, linear because a
sub-hypergraph of an `STS(15)` is linear). Hence the compiler **DECIDES
the selection layer POSITIVELY** and the `m = 4` obstruction is located
**entirely in the arithmetic (value-coincidence) layer**.
`P(selection layer satisfiable) = 0.93`;
`P(compiler transports usefully, i.e. decides it either way) = 0.75`.

**R4.2 Falsifier.** If no 12-edge linear 3-uniform hypergraph with
`Delta <= 3` on 15 vertices exists, the obstruction IS combinatorial and
my D1 verdict inverts.

**R4.3 Zero-power, pre-declared.** A positive decision on the ABSTRACT
selection layer has **no power** over realizability — it only relocates
the obstruction, and I pre-commit not to report it as progress toward a
witness.

### R5 — STRUCTURED (fibre-prescribed) PENCILS

**R5.1 derivation.** A degree-3 pencil is determined up to ONE remaining
parameter by prescribing two size-3 fibres `{x1,x2,x3} ↦ t1`,
`{y1,y2,y3} ↦ t2`: with `P_1,P_2` the monic cubics,
`(t2-t1)B = c1 P_1 - c2 P_2` and `A = t1 B + c1 P_1`; so `7 = 6 + 1`.
This is the structured search round 34 declared itself zero-power over
(its ZP item 5: "a structured (non-random) pencil could beat the
ensemble").

**R5.2 predictions.** `P(k_max under fibre-prescription > 7) = 0.60`;
`P(k_max = 12, a witness) = 0.05`. A higher `k_max` is **not** a witness
(R6b).

### R6 — MISS-2 GUARD (mean-vs-max), both directions

**(a)** NO aggregate/mean comparison (total slots vs total capacity,
ensemble-mean coincidences vs demand, "slack `> 0`") has ANY power over
existence. Only per-object constraints bind: per-slope `X_gamma`,
per-pair `|S_al ^ S_be|`, per-block `(OUT-m)`, per-point `d_x`. Anchor
1's MISS 4 is the precedent (a satisfied aggregate over an infeasible
configuration). **I pre-commit: every feasibility claim carries an
explicit per-object table; every infeasibility claim carries a per-object
violation or an explicitly scoped search budget.**
**(b)** Conversely a MAX measured over a truncated search is a **ceiling
under that search**, never an upper bound; every `k_max` I report carries
its budget.
**(c)** I will NOT infer non-existence from `E < 0`; `(SUPPLY-CODIM)` is
graded HEURISTIC everywhere, with its calibration points named.

### R7 — `(OUT-m)` CORRECTED FORM (D3), pre-declared

Corrected form (per the brief, to be read from the node):
`X'_gamma + 2X''_gamma >= m-1-eps~` with `eps~ <= 1+O`, aggregate
`(m-1)(1+O)`, `X = 0` corollary gated on `O <= m-3`.

**R7.1** `P(corrected form survives all stress this round) = 0.85`.
**R7.2** Registered structural prediction: the gate `O <= m-3` is
**empty at `m=2`** (`O <= -1`) and **forces `O = 0` at `m=3`**, so the
`X = 0` corollary first acquires slack at `m = 4` (`O <= 1`). I will
check it on every candidate.
**R7.3 Falsifier:** any configuration this round produces with
`X'_gamma + 2X''_gamma < m-1-eps~`, or `sum eps~ > 1+O`. **Reported
loudly if it fires.**
**R7.4** I will stress both deficient-point placements — INSIDE `W` (the
case that refuted the original rider) and OUTSIDE `W` — on the `m=4`
candidates and the `m=5` configurations.
**R7.5** If the node's own text disagrees with the brief's paraphrase,
**the node wins** and I report the discrepancy.

### R8 — BLIND PRIORS (the six the brief demands)

```text
P(m=4 realizable via route (a), non-split G)      = 0.20
P(m=4 realizable via route (b), sigma(x)=c/x)     = 0.05
P(m=4 realizable via route (c), un-symmetrised)   = 0.03
P(the m=5 parity witness lands)                   = 0.10
P(the u1_x4 compiler transports usefully)         = 0.75
P(the corrected (OUT-m) survives all stress)      = 0.85
```

Named in advance for route (a): the untested degenerate stratum
`G = Q(Z,x)*L(Z,x)` with `Q` a quadratic in `Z`, **irreducible over
`F_q(x)`** but with discriminant `Delta(x)` a SQUARE at all `a = 27`
points of `W` ("conditionally split"). Registered observation: the 27
square-conditions are CHEAP (a `2^-27` fraction of a `~q^20` family) while
the slope confinement is not — so route (a)'s freedom is real but is
predicted to be spent in the wrong place. `P(this sub-route lands) = 0.07`.

### R9 — ZERO-POWER PRE-DECLARATIONS

1. Every negative is scoped to a NAMED ansatz class plus a NAMED search
   budget.
2. `(SUPPLY-CODIM)` is a dimension heuristic; negative excess is NOT a
   proof and will never be graded as one.
3. Two fields per scale is not `q`-uniformity; no claim at official
   scale.
4. A positive decision of the abstract selection layer says nothing about
   realizability (R4.3).
5. Layer A is NOT run this round (inherited MISS 7); every configuration
   is a `W`-layer object only.
6. Everything is `(SAT3)`-conditional (`T = rho+2`).
7. No `m=4` theorem will be claimed: the deliverable is a witness or an
   obstruction with named scope.

### R10 — EXPECTED MISSES

1. I expect an off-by-one in the slot bookkeeping (middles vs `Delta`
   points); anchor 1's own `21`-vs-`22` ambiguity is the warning.
2. I expect the `m=5` run to be the expensive one and to risk the
   ramguard wall; I pre-commit to checkpointed batches with results
   files written incrementally.
3. I expect to mis-handle deficient-point accounting at fixed points at
   least once.
4. I expect to need `O` / `eps~` definitions I do not yet have (R7.5).

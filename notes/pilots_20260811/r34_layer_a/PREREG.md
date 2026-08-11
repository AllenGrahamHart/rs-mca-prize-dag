# PREREG — r34_layer_a (round 34)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/rh_psi_degree/REPORT.md` (round 33)
2. `notes/pilots_20260811/rh_bivariate_system/REPORT.md` (round 33)

## Mandate

THE CONVERGED TYPE-2 INSTRUMENT. Round 33's banks 1+2 converged
from opposite directions on the FULL-DOMAIN layer: one bivariate
Q(Z,x) of bidegree (rho, m) on all of D (deficit 12m^2 - 4m, ~3x
the W-layer), which killed bank 2's own m=2 exhibit. Bank 1 named
its statement form: **(NS-m)** — every type-2 h_gamma carries >= m
of its degree in irreducible factors of degree >= 2 — which IMPLIES
closure of residual (ii); and its geometric form: all a fibres of
H(Z,x) are totally split over F_q (the rigidity), so (NS-m) asks
whether the TRANSVERSE family (h_gamma, one per curve point) can
also split — a Wronskian/ramification question on a g^{m+1}_d on
P^1. THE REGRESSION TEST IS MANDATORY (round 33 bank 3): (SAT3) is
REALIZED at m = 1, so any (NS-m)-type theorem must either hold on
the m=1 witnesses or be m-dependent and fail there — CALIBRATE
FIRST. YOUR JOB: the layer-A attack on (NS-m).

## Deliverables

**D1 — THE m=1 CALIBRATION (first, mandatory).** On the 16 realized
m=1 configurations (banked in rh_sat3_realizability/): compute the
h_gamma family and measure (NS-m) directly (does every type-2
h_gamma at m=1 carry >= 1 of its degree non-split?). If VIOLATED,
(NS-m) as stated is FALSE and needs restatement (m-dependence or a
stratum hypothesis) — that changes everything downstream, so it
comes first. Also run layer A's rank system on a realized witness
(it MUST be consistent there — nullity >= 1; if not, the layer-A
builder is wrong: a built-in control).

**D2 — THE WRONSKIAN ATTACK.** The rigidity forces every fibre
P_x(Z) totally split; the Wronskian of the g^{m+1}_d counts total
ramification (2(d + (m+1)(g... on P^1: deg W = (m+2)(d - m-1) +
...) — derive the exact ramification budget and what total
fibre-splitness costs against it. Does the budget FORCE >= m
non-split degree in the transverse direction (= (NS-m))? This is
the round's theorem attempt. POSE with falsifiers what you cannot
prove; the m=1 calibration bounds what the theorem may claim.

**D3 — LAYER-A RANK AT SCALE.** Using bank 2's biv_core.py (banked,
copy first): the layer-A system's rank/nullity on (a) the m=1
witnesses (control: consistent), (b) bank 2's m=2 W-layer exhibit
(known: killed — reproduce), (c) structured m=2/m=3 candidates
from the (BIV-CURVE) fibre method. Where layer A kills, extract
WHICH equations bind (the consistency relations = candidate (NS-m)
mechanisms).

**D4 — VERDICT.** (NS-m) proved / restated / walled, with the m=1
regression status explicit. Misses first.

## Blind priors to register

P((NS-m) survives the m=1 calibration as stated), P(the Wronskian
budget yields the theorem this round), P(layer A consistent on all
16 m=1 witnesses).

---

## Pilot registrations

Appended after reading **exactly** the two named anchors
(`rh_psi_degree/REPORT.md`, `rh_bivariate_system/REPORT.md`) and
**before** any other read, any grep, any `ls`, and any interpreter
invocation.

### R0 — notation, and the m=1 arithmetic I am about to test

Derived from the anchors alone (no further read), so that the m=1
calibration is a test and not a fit:

```text
m = 1 :  N = 16m = 16,  rho = 4m-1 = 3,  R+1 = 8m+1 = 9,  e = m = 1,
         delta = rho-3e = m-1 = 0,  T = rho+2 = 5,  T_2 = rho = 3 (if T_1 = 2)
band     a in [4m+2, 8m] = [6, 8];  (NEWCAP) a* <= 7m-1 = 6
argmax   a = (20m-2)/3 = 6 = 4m+2 exactly;  16m/3 = 5.333
d       := a - (4m+2) = a - 6  in {0,1,2}
need_X   = d - m = d - 1  in {-1, 0, 1}
Eneed    = m = 1;  FR-canonical proved cap 2m-2 = 0;  a/4 = 1.5 at a = 6
deg_Z H <= m+1 = 2 ;  deg_x H <= d
```

### R1 — the three mandated blind priors

- **P((NS-m) survives the m=1 calibration as stated) = 0.10.**
  Reason registered in advance: at `m=1` the whole degree budget of
  `h_gamma` is `d = a-6 <= 2`, and `(NS-1)` demands at least `1` of
  that degree in factors of degree `>= 2` — i.e. it demands
  `deg h_gamma >= 2`, hence `a = 8m = 8` exactly, and then demands
  `h_gamma` be an **irreducible quadratic**. At the argmax `a = 6`
  the budget is `d = 0` and `h_gamma` is a constant. I therefore
  expect VIOLATION, not survival. Split of the residual mass:
  `P(survives non-vacuously) = 0.03`, `P(survives vacuously — no
  type-2 slope with `h_gamma != 0` at m=1) = 0.07`.
- **P(the Wronskian budget yields the theorem this round) = 0.05.**
- **P(layer A consistent — nullity >= 1 — on all 16 m=1 witnesses)
  = 0.85.** If the witnesses are genuinely realized pencils, layer A
  is a *necessary* condition, so nullity `>= 1` is forced and any
  failure indicts my builder, not the mathematics. The `0.15` is
  entirely my builder at degenerate parameters (`delta = 0`,
  possibly `d = 0`), plus the risk that bank 3's "realized" means
  something weaker than a Hankel pencil at `T = rho+2`.

### R2 — pre-registered derivations, each falsifiable

- **R2.1 (DEGENERACY).** At `m=1`, `a = 6`: `d = 0`, so **every**
  `h_gamma` is a constant. `P = 0.90`.
- **R2.2.** Hence `nonsplit_gamma = 0` for every type-2 slope at
  `a = 6`, so `(NS-1)` is FALSE there unless vacuous.
  `P(violated | at least one type-2 slope with h_gamma != 0) = 0.92`.
- **R2.3.** The `m=1` failure will be a **degree-budget artifact**
  (`d < 2`, resp. `d < 2m`), not a structural refutation of the
  mechanism at `m >= 2`; the correct restatement is
  budget-shaped (`nonsplit >= min(m, ...)`, or a hypothesis
  `d >= 2m`) rather than stratum-shaped. `P = 0.60`.
- **R2.4 (the calibration's own zero-power).** At `m=1` the PROVED
  FR-canonical cap is `X_gamma <= 2m-2 = 0` at a minimising pair
  union, so residual (ii) is already closed at `m=1` **for a reason
  that never mentions `(NS-m)`**. Therefore the `m=1` regression can
  only KILL `(NS-m)`; it can never certify it. `P = 0.75`.
- **R2.5 (the Wronskian number, registered before computing it).**
  Writing `H(Z,x) = sum_{j=0}^{m+1} Z^j f_j(x)` with
  `deg f_j <= d`, the `f_j` span a `g^{m+1}_d` on `P^1`; Plücker at
  genus `0` gives total ramification weight `(m+2)(d-m-1)`. At the
  argmax `d = (8m-8)/3`, so the budget is
  `(m+2)(5m-11)/3 ~ 5m^2/3`, against the `(NS-m)` aggregate demand
  `T_2 * m = rho*m = 4m^2-m`. **Prediction: budget < demand for
  every `m`, ratio `-> 5/12 = 0.4167`.** `P = 0.70`.
- **R2.6.** A totally split fibre is **reduced**, hence
  **unramified**, so the banked rigidity (all `a` fibres `P_x(Z)`
  totally split) costs the ramification budget **nothing**. If so,
  the brief's D2 framing ("what total fibre-splitness costs against
  the budget") is misposed and I must say so rather than manufacture
  a cost. `P = 0.65`.

### R3 — MISS-2 GUARD (mean-vs-max), written before any computation

Rounds 32 and 33 both nearly died on this trap (bank 1 MISS 9), so
the guard is registered *ahead* of the instrument:

1. Every Wronskian / ramification / degree-budget instrument bounds a
   **SUM** over points or over slopes. `(NS-m)` is a `forall`
   statement over type-2 slopes and closure needs `max X <= need_X`.
   **`sum_gamma nonsplit_gamma >= T_2*m` is NOT `(NS-m)` and NOT
   closure** — it gives only "some slope". I will not claim
   otherwise, and I will label any aggregate result as aggregate at
   the point of statement.
2. The asymmetry I will hold myself to: `(NS-m) => sum >= T_2*m`, so
   an instrument that **caps** `sum_gamma nonsplit_gamma` strictly
   below `T_2*m` **REFUTES** `(NS-m)`. Aggregate instruments can kill
   `(NS-m)`; they cannot prove it. The refutation direction is the
   one worth spending compute on.
3. Symmetrically, and this is the round-32/33 trap proper: I will
   **not** conclude "the route is dead" from `budget < demand` alone.
   The Plücker budget is over the whole linear series, while the
   `h_gamma` are the members indexed by the rational normal curve
   only — a sub-family, on which a *per-member* bound may hold
   without any aggregate one. A `T`-free per-slope bound stays live
   even if every aggregate reading of it fails.

### R4 — zero-power flags, declared in advance

1. Random-embedding nullity-`0` results have essentially zero power
   to establish infeasibility (bank 2 MISS 4). I will claim none.
2. `m = 1` is banked as structurally disjoint. Any `m=1` outcome can
   refute a `forall m` statement; it can never support one.
3. 16 witnesses is a sample; a max/min over them falsifies only.
4. Two fields is not `q`-uniformity.
5. If `T_2 <= 1` on the realized `m=1` witnesses, max-vs-mean has
   zero power there, exactly as in bank 1's P3.3.
6. Anything I say about `m >= 3` structured candidates is a
   construction attempt, not a census; absence of a witness where
   none was sought is not evidence.

### R5 — subtraction plan (CATCH-24A), before any novelty claim

Own-repo greps over `critical/`, `background/`, `notes/pilots_2026080*/`
and `notes/pilots_20260810/`, with `--exclude-dir` at the SEARCH
level for the sibling `pilots_20260811` dirs and any `prize-codex-`
path, for: `Wronskian`, `ramification`, `Pl(u|ü)cker`, `linear
series`, `g^r_d`, `inflection`, `osculating`, `order sequence`,
`Stohr|Stöhr`, `Voloch`, `totally split`, `nonsplit|non-split`,
`NS-m`, `m = 1`.

### R6 — expected misses

- The layer-A builder will need a degenerate-case fix at `m=1`
  (`delta = 0`, `d` possibly `0`, `deg_Z = 2`); I expect at least one
  control failure before it is right, and I will report it.
- I expect NOT to prove `(NS-m)` and to deliver a POSED statement
  with falsifiers plus an explicit `m=1` restatement.

### R7 — execution order (D1 gates)

D1 (m=1 calibration + layer-A control) → D3 (rank at scale, reusing
bank 2's `biv_core.py`) → D2 (Wronskian budget) → D4. If D1 refutes
`(NS-m)` as stated, D2's target becomes the *restated* statement and
I will say explicitly which statement the budget is being run
against.

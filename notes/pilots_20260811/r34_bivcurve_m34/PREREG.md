# PREREG — r34_bivcurve_m34 (round 34)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/rh_bivariate_system/REPORT.md` (round 33)
2. `notes/pilots_20260811/rh_psi_degree/REPORT.md` (round 33)

## Mandate

THE m >= 3 FORK OF (BIV-CURVE). Round 33 fenced the W-layer
bivariate system by an m = 2 witness: T = rho+2 = 9 slope classes
on W realized as fibres of a degree-3 pencil (a degree-(3m-3)
dimension-m linear series in general). The first-moment heuristic
says such series with the prescribed fibre structure stop existing
around m ~ 16 — but the m = 2 witness proves the heuristic wrong at
small m, so the boundary is UNKNOWN. The decisive computation
(round 33's own naming): a CONSTRUCTIVE search at m = 3, 4 —
degree-6/9 linear series of dimension 3/4 with 18/24 prescribed
fibres. IF the construction extends: the W-layer fence extends and
the type-2 exclusion must come from layer A alone. IF it fails at
m = 3 with the obstruction visible: the W-layer starts excluding at
m = 3, and the obstruction IS a candidate (NS-m) mechanism. Either
way the m-boundary of (BIV-CURVE) is the deliverable.

## Deliverables

**D1 — THE CONSTRUCTION SPACE, STRUCTURED.** From bank 2's (BIV-G):
G(Z,x) of bidegree (3m-3, m-1); the fibre prescription = the
per-side (OV) cap structure (all but m-1 type-2 slopes carry
exactly m-1 points per side — bank 2's slack rigidity). Set up the
m=3 search as bank 2's exhibit was built (the fibre profile first,
then the incidence realization, then the outside completion) — NOT
random draws (q^-Theta(m^2) power; the round-33 lesson).

**D2 — m = 3 DECIDED (the round's core).** Either an explicit
witness (T = 13, a = 20, all incidence axioms + (BIV-CURVE), two
fields, the full measured table) or the named obstruction (which
step of the m=2 construction fails: the fibre profile? the
degree-6 series' ramification budget? the outside completion's
K_7-analogue?). A fields-searched negative is not a theorem —
grade it honestly.

**D3 — m = 4 + THE BOUNDARY.** Same at m = 4 if m = 3 resolves
quickly; state the (BIV-CURVE) m-boundary of record and its
relation to TCAP-DIM's boundary (different objects — the W-layer
incidence structure vs full Hankel realizability; a divergence
between the two boundaries is itself a finding).

**D4 — VERDICT.** Misses first. Cross-pilot flag (do NOT read
siblings): your obstruction, if any, is a candidate mechanism for
the sibling layer-A lane — write it self-contained for the
coordinator's reconciliation.

## Blind priors to register

P((BIV-CURVE) realizable at m=3), P(at m=4), P(the obstruction if
any is the ramification budget), P(the (BIV-CURVE) boundary ==
TCAP-DIM's boundary).

## Pilot registrations

Written after reading EXACTLY the two named anchors
(`rh_bivariate_system/REPORT.md`, `rh_psi_degree/REPORT.md`) and
BEFORE any other read, any grep, any `ls`, and any interpreter
invocation.

### R0 — notation carried from anchor 1

`m`, `N=16m`, `rho=4m-1`, `R=8m`, `e=m`, `T=rho+2`, `T_1=2`,
`T_2=rho=4m-1`, `delta=m-1`, `a=w*=a*=7m-1`, `W=S_g u S_h`,
`|S_g|=|S_h|=rho`, `|S_g ^ S_h| = 2rho-a = m-1`,
`|S_g D S_h| = 6m`. `X_gamma = |S_gamma ^ W|`, per-side
`X_gamma^g = |S_gamma ^ S_g|`. `G(Z,x)` of bidegree
`(deg_x <= 3m-3, deg_Z <= m-1)`, `(BIV-G)`/`(BIV-CURVE)` as stated
at anchor 1 D3.1.

### R1 — THE SPLIT ANSATZ (my primary constructive mechanism, registered before testing)

I will NOT search `G` by random draw (anchor 1 MISS 4: per-draw
power `~q^{-Theta(m^2)}`). I register the following ansatz as the
constructive route, with its degree arithmetic done by hand now:

> **(SPLIT-m).** Take `G(Z,x) = prod_{j=1}^{m-1} ( u_j(x) Z - v_j(x) )`
> with `deg u_j, deg v_j <= 3`. Then `deg_Z G = m-1` (exact) and
> `deg_x G <= 3(m-1) = 3m-3` — **the budget is met with equality, at
> every `m`**. The fibre of `G` at `x` has roots
> `phi_j(x) = v_j(x)/u_j(x)`, i.e. the `m-1` type-2 slopes at `x` are
> the images of `x` under `m-1` degree-`<=3` PENCILS.

So `(BIV-CURVE)` at every `m` is IMPLIED by: the existence of `m-1`
degree-`<=3` rational maps `phi_1..phi_{m-1}` on `W` whose value
tuple at each `x in S_g D S_h` is exactly `A_x \ {g,h}` (`m-1`
distinct type-2 slopes), and at each `x in S_g ^ S_h` gives the
`m-2` type-2 slopes plus one free value `mu(x)`. At `m=2` this
degenerates to anchor 1's single degree-3 pencil — i.e. **the m=2
exhibit is the `m-1 = 1` case of (SPLIT-m)**, which is why I expect
it to extend rather than break.

- R1.1 `P(the degree budget claim 3(m-1) = 3m-3 is exact) = 0.95`
  (it is arithmetic; I have checked it, but I register it as
  falsifiable in case `deg_Z <= m-1` is not the right budget).
- R1.2 `P((SPLIT-m) yields an admissible m=3 witness) = 0.70`.
- R1.3 `P(the m=3 witness, if it exists, needs a NON-split G) = 0.15`.

### R2 — counting registrations (derived by hand now, falsifiable)

At general `m`, with `T=rho+2`, `T_1=2`, `W = S_g u S_h` minimising:

```text
sum_{type-2} X_gamma        = 6m(m-1) + (m-1)(m-2) = (m-1)(7m-2) = 7m^2-9m+2
capacity (X <= 2m-2)        = (4m-1)(2m-2)         = 8m^2-10m+2
TOTAL SLACK                 = m(m-1) = m^2-m
per-side demand             = 3m(m-1) + (m-1)(m-2) ... = (m-1)(4m-2)
per-side capacity (<= m-1)  = (4m-1)(m-1)
PER-SIDE SLACK              = m-1                  [anchor 1 D3.2, re-derived]
```

- R2.1 At `m=3`: `sum X = 38`, capacity `44`, slack `6`; per-side
  demand `20`, capacity `22`, slack `2`. `P(these reproduce) = 0.90`.
- R2.2 At `m=4`: `sum X = 78`, capacity `98`, slack `12`; per-side
  demand `42`, capacity `45`, slack `3`. `P = 0.85`.
- R2.3 Note `sum X` equals anchor 1's CONDITION count `7m^2-9m+2`
  exactly — registered as an identity to check, not a coincidence.
- R2.4 Outside completion at `m=3`: `N-a = 28` outside points,
  `sum_{x notin W} d_x = 28m - def_out = 84-1 = 83 = sum_gamma (rho - X_gamma)
  = 121-38`. Dual: `27` blocks-triples + `1` pair on `11` vertices,
  `82` outside pair-slots + `18` inside pair-slots `= 100` against
  capacity `C(11,2) * (m-1) = 55*2 = 110`. `P(feasible) = 0.85`.

### R3 — MISS-2 GUARD (mean-vs-max; the proven guard pattern, written before any computation)

I anticipate reasoning of the form: *"the mean pencil fibre size is
`6m/(4m-1) ~ 1.5`, well under the degree cap `3`, and the per-side
slack is `m-1 > 0`, therefore the assignment fits."* **GUARD: a mean
strictly under a cap NEVER establishes feasibility of an assignment,
and positive slack is not existence.** Feasibility here requires
simultaneously (i) an explicit integer fibre PROFILE, (ii) that
profile realized as the actual fibres of a genuine degree-`<=3`
rational map on the chosen point set (an algebraic condition the
profile count cannot see), and (iii) per-side compliance of the
union over the `m-1` pencils. I will not report existence without
(ii) verified over two fields. **Symmetrically**: I will not report
non-existence from a negative slack count either — a profile-LP
infeasibility is an obstruction only for the profile layer, and must
be stated with its scope. Anchor 2's MISS 9 (two consecutive rounds
caught by this trap) is the reason this is registered first.

### R4 — blind priors demanded by the brief

- `P((BIV-CURVE) realizable at m=3) = 0.80`
- `P((BIV-CURVE) realizable at m=4) = 0.72`
- `P(the obstruction, if any, is the ramification budget
  [i.e. the discriminant of G(.,x) failing to be a square / the
  Riemann-Hurwitz count of the m-1 pencils]) = 0.20`
- `P(the (BIV-CURVE) m-boundary == TCAP-DIM's boundary) = 0.12`
  (different objects: W-layer incidence vs full Hankel
  realizability; anchor 1 D5 already shows the m=2 W-witness dies at
  layer A, so I expect the two boundaries to DIVERGE).

### R5 — expected misses (registered so they are not retro-fitted)

- R5.1 The per-side cap at `m=3` is `m-1 = 2` while a degree-3
  pencil has fibres of size up to `3`; so every size-3 fibre must
  split `2+1` across `S_g\S_h` / `S_h\S_g`. `P(this collision is
  fatal at m=3) = 0.15`.
- R5.2 Distinctness `phi_i(x) != phi_j(x)` at all `6m` points is a
  real constraint (`A_x` has distinct slopes) and I expect to lose
  candidate pencil pairs to it.
- R5.3 The `m-1` middle points `S_g ^ S_h` carry only `m-2` type-2
  slopes, so one pencil is *free* there — at `m=3` that is one
  pencil free at 2 points; at `m=2` it was the whole of `w13`.
  I expect to mis-handle this at least once.
- R5.4 I expect the outside completion, not the algebra, to be the
  fiddly part (anchor 1's `K_7`-analogue).

### R6 — zero-power pre-declaration

A fields-searched negative at `m=3` is NOT a theorem and I will
grade it as `searched-negative, scope = <the ansatz class actually
enumerated>`, with the enumerated class stated explicitly. Any
maximum over a search is a max over a sample. Two fields is not
`q`-uniformity. Everything remains `(SAT3)`-conditional and
`W`-layer only (layer A is the sibling's lane; anchor 1 D5 kills the
`m=2` W-witness there and I expect the same at `m=3`).


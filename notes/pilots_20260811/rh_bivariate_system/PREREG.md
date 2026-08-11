# PREREG — rh_bivariate_system (round 33)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260810/rh_fr_algebraic/REPORT.md` (round 32 —
   D2.4's bivariate paragraph)
2. `background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md`

## Mandate

THE OVERDETERMINED REALIZABILITY SYSTEM — round 32's unexploited
instrument. Under (SAT1)-(SAT4) with T = rho+2 at a = w* = a*, the
banked saturation rigidity forces every coordinate of the bivariate
Psi(Z) to factor as P_x(Z) = lambda_x * prod_{gamma in A_x}(Z - gamma)
* (Z - mu(x)) for x in W (A_x = the slopes through x, |A_x| = d_x;
mu(x) = the fibre slope) — (m+2)(4m+1) linear conditions on the
a = 7m-1 unknowns lambda_x: OVERDETERMINED BY A FACTOR ~O(m), and
nobody has computed its rank. YOUR JOB: exploit it. If the system's
rank exceeds a - 1 generically (projective lambda), the failure
configuration is KILLED outright; if consistency forces relations
on the incidence data (A_x, mu), those relations are new axioms
beyond the incidence fence — potentially the a/4 cap or the T-cap.

## Deliverables

**D1 — THE SYSTEM, DERIVED CLEANLY.** From the banked rigidity
(quote its exact statement + hypotheses file:line — note its
saturated-point scope >= 15N/16 and carry the unsaturated-point
exception honestly): write the linear system on (lambda_x)
explicitly. What are the equations indexed by? (The pilot text
says (m+2)(4m+1) conditions — re-derive that count; if it differs,
that is a finding.)

**D2 — RANK AND CONSISTENCY AT SMALL SCALE.** At m = 2, 3, 4 (two
fields each): build the system for (a) the K_7-star incidence
system (round 32's residual-(i) fence — does the bivariate layer
kill what incidence admits?), (b) the round-31 wave-57 fence's
m = 64 system restricted/scaled if feasible, (c) random admissible
incidence data. Compute exact ranks. THE DECISIVE QUESTION: does
the rank generically exceed the unknowns (=> the incidence-feasible
systems are algebraically infeasible)?

**D3 — THE CONSISTENCY RELATIONS.** Where the system IS consistent:
extract the relations on (A_x, mu) that consistency forces (kernel
dimensions, minor vanishing). Are they equivalent to / stronger
than the a/4 cap? POSE the resulting theorem with falsifiers.

**D4 — VERDICT.** The failure configuration killed / constrained /
untouched, with the exact algebra that remains. Cross-pilot note:
this instrument and the psi_gamma degree count are two views of one
layer — flag convergences for the coordinator, do NOT read the
sibling dir. Misses first.

## Blind priors to register

P(the condition count re-derives exactly), P(generic rank kills the
failure configuration), P(consistency relations imply X <= a/4),
expected rank deficit at m=2.

---

## Pilot registrations

Written after reading EXACTLY the two named anchors
(`notes/pilots_20260810/rh_fr_algebraic/REPORT.md`,
`background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md`)
and BEFORE any other read, any grep, and any interpreter invocation.

### R0 — notation I will use

`m>=1`, `N=16m`, `rho=4m-1`, `R=8m`, `e=m`, `T=|Z|=rho+2=4m+1` (SAT3),
`D` = evaluation domain (`|D|=N`), `d_x=|{gamma in Z: Q_gamma(x)=0}|`,
`A_x={gamma in Z: Q_gamma(x)=0}` (so `|A_x|=d_x`), `O=sum(rho-u_gamma)`,
`W` = the joint support with `a=|W|=7m-1` at the banked evaluation point
`a=w*=a*`, `mu: W -> P^1` the fibre slope, `F_g=mu^{-1}(g)`,
`n_g=|F_g|`, `S_gamma` the locator set, `X_gamma=|S_gamma ^ W|`,
`K'=[16m, 12m-1, 4m+2]` the apolarity code
(`rh_fr_algebraic/REPORT.md:134`), `K'|_W` its shortening to `W`,
`lambda_x` the unknown scalar in `P_x(Z)=lambda_x prod_{A_x}(Z-gamma)(Z-mu(x))`.

### R1 — my derivation of the count, registered BEFORE computing

I claim the `(m+2)(4m+1)` arises as **(number of `Z`-levels) x (codimension
of `K'|_W`)**:

- `deg_Z Psi <= e+1 = m+1` (`(C3)`, quoted at `REPORT.md:135`) gives
  `m+2` coefficient vectors `v^(j) in F^W`, `j=0..m+1`;
- `K'` MDS `[16m, 12m-1, ...]` has codimension `4m+1`; shortening to
  `W` with `a >= 4m+1` preserves codimension `4m+1` (dimension
  `a-(4m+1)`, matching the stated `deg h <= a-(4m+2)`,
  `REPORT.md:134`);
- each `v^(j) in K'|_W` is therefore `4m+1` linear conditions, total
  `(m+2)(4m+1)`, and each is linear in `lambda` because
  `v^(j)_x = lambda_x e_j(x)` with `e_j(x)` fixed by the incidence data.

**P(this count re-derives exactly as `(m+2)(4m+1)`) = 0.80.**

**P(the unknown count is exactly `a=7m-1`, with no correction) = 0.20.**
I predict a correction: the rigidity gives `d_x=m` only at the
`>= N-(1+O) >= 15N/16` saturated points
(`saturation_rigidity/statement.md:56-60`), so up to `1+O <= m` points
may be unsaturated, and ALL of them may lie in `W` (nothing in the
banked statement locates them off `W`). At an unsaturated `x`,
`Q_Z(x) = c_x prod_{A_x}(Z-gamma) g_x(Z)` with `deg g_x <= m-d_x` and
`g_x` rootless in `Z`; that is `m-d_x` extra unknowns beyond
`lambda_x`. **Registered prediction: the honest unknown count is
`a + (1+O) <= 8m-1`, not `a`,** and the honest equation count is
unchanged. Overdetermination survives (`~4m^2` vs `<= 8m-1`).

### R2 — the mechanism I expect to be the content (falsifiable)

Eliminate the code membership into a bivariate interpolation statement.
Write `nu_x = lambda_x sigma'_W(x)`. Then the whole system is equivalent
to: **there exists `H(Z,x)` of bidegree `deg_Z <= m+1`,
`deg_x <= a-(4m+2) = 3m-3`, with**

```text
H(Z,x) = nu_x prod_{gamma in A_x}(Z-gamma) . (Z-mu(x))   for every x in W.
```

Consequences I register in advance as the expected D3 output:

- **(G-bound).** Let `G = {gamma in Z : H(gamma,.) === 0}`. Then
  `(Z-gamma) | H(Z,x)` for all `x`, so `gamma in A_x u {mu(x)}` for
  every `x in W`, i.e. `W subset S_gamma u F_gamma`, hence
  `a <= X_gamma + n_gamma <= rho + n_gamma` forces `n_gamma >= 3m`.
  Since `sum_g n_g = a = 7m-1 < 9m`, **`|G| <= 2`.**
- **(per-slope).** For `gamma !in G`, `H(gamma,.)` is a nonzero
  polynomial in `x` of degree `<= 3m-3` vanishing on
  `(S_gamma ^ W) u F_gamma`, so
  `X_gamma + n_gamma - |S_gamma ^ F_gamma| <= 3m-3`.
- **I register that this is (C2) re-derived, not beaten**: round 32
  records `(C2)` as `X <= a-n_gamma-(R-r+1) = 3m-3-n_gamma` at
  `a=7m-1` (`rh_fr_algebraic/REPORT.md:55`). So my honest expectation is
  that the bivariate layer's *per-slope* content is exactly banked, and
  any new content is **joint** (one curve for all slopes at once).

**P(the bivariate consistency relations imply `X_gamma <= a/4`
(~`1.75m`), for the `(SAT3)` failure configuration) = 0.10.**
**P(they re-derive `(C2)`-strength `3m-3` and no more, per slope) = 0.60.**
**P(a genuinely new JOINT relation, i.e. one not implied by the
per-slope `(C2)` family, is extractable and checkable) = 0.45.**

### R3 — rank priors

The system matrix has columns `h_x (x) e_x` (Khatri-Rao / column-wise
Kronecker of the `(4m+1) x a` parity check `H|_W` with the `(m+2) x a`
coefficient matrix `E`), so the generic rank is `min(a, (m+2)(4m+1)) = a`.

- **P(rank = `a` (full column rank, only `lambda = 0`) for RANDOM
  admissible incidence data at `m=2,3,4`) = 0.75.**
- **P(this KILLS the failure configuration — i.e. rank `>= a` for ALL
  incidence-feasible data, not merely generic) = 0.10.** A true
  configuration necessarily has rank `<= a-1`, so full generic rank
  only says the failure configuration must be non-generic; killing it
  needs an all-data statement, and I expect degenerate but
  incidence-admissible data to exist with a kernel.
- **Expected rank deficit at `m=2`** (`a=13`, `(m+2)(4m+1)=36`,
  `T=9`, `|A_x|=2`, `deg h <= 3`): **0** for random admissible data;
  **1** (a one-dimensional kernel, projectively a unique `lambda`) for
  structured/incidence-fence data. Registered window: deficit in
  `{0}` random, `{0,1,2}` structured; deficit `>= 3` at `m=2` would
  falsify my picture.
- **P(the `K_7`-star incidence system — round 32's residual-(i) fence,
  which I have NOT yet read — is killed by the bivariate layer) = 0.30.**
  Hedged: I do not yet know that object; this is a genuinely blind
  number.

### R4 — carried caveats (registered so I cannot quietly drop them)

1. `(SAT3)` (`T=rho+2`) is a hypothesis of everything here
   (`saturation_rigidity/statement.md:39-41`); any small-`m` census I
   build has `T=3` in the realizable world (round 31/32 MISS 5,
   `rh_fr_algebraic/REPORT.md:31`) and therefore **zero power** over the
   failure configuration.
2. The saturated-point scope is `>= N-(1+O)`, NOT all of `D`
   (`statement.md:56-60`); the unsaturated exception is R1's correction
   and I will carry it into every rank count.
3. `a = w* = a* = 7m-1` is `(NEWCAP)`, itself `(SAT3)`-conditional
   (`rh_fr_algebraic/REPORT.md:33,108`).
4. `lambda_x != 0` is NOT free: `x in F_infinity` (i.e. `c_{1,x}=0`)
   gives `deg P_x = m`, not `m+1`. The `(Z-mu(x))` factor must be read
   projectively. Registered as a live degeneration, not assumed away.
5. Everything I compute is over small fields; two-field confirmation for
   every structural claim.

### R5 — subtraction plan (CATCH-24A, before any novelty claim)

Grep own repo (`critical/`, `background/`, `notes/`, excluding sibling
round-33 dirs and any `prize-codex-` path) for: `bivariate`,
`Khatri-Rao`, `lambda_x`, `realizability system`, `rank of the`,
`(C2)`, `A_x`, `mu(x)`, `fibre slope`, `overdetermined`. Expect `(C2)`
and the `P_x` factorization itself to come back banked
(`rh_fr_algebraic/REPORT.md:56` already flags the factorization as
banked from `statement.md:62-69`).

### R6 — misses I expect to have to report

That the instrument's per-slope content is banked `(C2)`; that the
"factor `O(m)` overdetermination" is an artifact of not counting the
`H`-coefficients as unknowns (in the `H` picture the ratio is
`~(m+2)a / (m+2)(3m-2) -> 7/3`, a CONSTANT factor, not `O(m)`) — I
register that re-framing now, before computing, as the likeliest
correction to the mandate's premise.

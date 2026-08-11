# PREREG — rh_sat3_realizability (round 33)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260810/rh_type2_stratum/REPORT.md` (round 31)
2. `background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md`

## Mandate

ROUTE-DECIDING. The entire type-2 program ((NEWCAP), the 7/4
ledger, FR-canonical's ledger use, the one-integer residual (i)) is
CONDITIONAL on (SAT3): T = rho+2 supported slopes. NO census has
ever produced T > 3 (round 31: "the census has zero power over the
failure configuration"; round 32: T = 3 in 420/420). The falsifier
F2 (a realizable T = rho+2 configuration with a* > 7m-1) has never
been exercised — and neither has the OTHER direction: nobody has
shown T = rho+2 is realizable AT ALL for strict A=3 pencils at any
scale. YOUR JOB: settle the realizability of large T. If T = rho+2
is unrealizable (a T-cap theorem below rho+2), the failure
hypothesis is VACUOUS and the whole conditional stack closes for
free — that would be the largest single result of the campaign. If
it IS realizable, the constructions calibrate every conditional
result and exercise F2.

## Deliverables

**D1 — THE T-LADDER BY CONSTRUCTION.** Random sampling caps at
T = 3 because bad slopes are rare. Build TARGETED constructions
(the LB1 pattern: design locators/syndromes directly, then verify
supported-ness) pushing T as high as possible at m = 1..4: LB1-type
maximal-core pencils give T = r+1 = rho+... wait — CHECK FIRST what
LB1's T means for THIS count: LB1 lives on the far-CA object
(supported slopes of a column-far pair) — quote both definitions
side by side (CATCH-24C) and determine whether LB1's r+1 slopes ARE
"supported slopes" in the (SAT) sense. If yes, T = r+1 >= rho+2 is
ALREADY REALIZED and the question becomes the profile (does an
LB1-type configuration satisfy (SAT1)/(SAT2)/(SAT4)?). This
definitional reconciliation is the round's first obligation — the
two lanes may have been talking about the same T all along.

**D2 — THE (SAT) PROFILE OF LARGE-T CONFIGURATIONS.** For whatever
large-T objects D1 yields: measure the full (SAT) data (o_gamma, O,
d_x, the deficit identity, w*/a*). Does any satisfy (SAT3) with the
strict-A=3 profile? If yes: F2's premise is live — check a* vs 7m-1
((NEWCAP)'s falsifier F1!). If no: name the exact (SAT) axiom that
large T violates — that axiom becomes the T-cap candidate theorem.

**D3 — THE T-CAP ATTEMPT.** Whichever way D2 points: either draft
the T-cap theorem (T <= f(m) < rho+2 for realizable strict-A=3
saturated pencils — the vacuity result) with proof sketch and
falsifiers, or draft the honest statement that (SAT3) is realized
with the calibration table. POSE, don't claim.

**D4 — VERDICT.** The conditional stack's status: vacuously closed
/ calibrated / still conditional-with-power. Misses first.

## Blind priors to register

P(LB1's slopes are (SAT)-supported slopes — the lanes reconcile),
P(T = rho+2 realizable), P(a T-cap theorem this round), P((NEWCAP)'s
F1 fires if realizable).

---

## Pilot registrations

Appended by the round-33 pilot after reading EXACTLY the two named
anchors (`notes/pilots_20260810/rh_type2_stratum/REPORT.md`,
`background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md`)
and BEFORE any other read, any grep, and any interpreter invocation.

### R0 — notation I will use

From (SAT1): `m>=1`, `rho=4m-1`, `N=16m`, `A=3`, `e=m`, `s=0`,
`delta=rho-3e=m-1`. `Z` = set of finite supported slopes, `T=|Z|`,
`c_gamma=rho-rank M(gamma)`, `u_gamma` = #distinct domain roots of
`Q_gamma`, `O=sum(rho-u_gamma)`, `d_x=|{gamma: Q_gamma(x)=0}|`.
Round-31 imports: `S_gamma` (locator support), `W`, `w*=a` = MINIMUM
joint support over pairs, `p_gamma=|S_gamma\W|`, `j_gamma`,
`CAP(m,a)=floor((N-a)e/(R+1-a))`, `R=8m`, `(NEWCAP)`, `(OV)`, `(FR)`.
I will write `T_SAT` for the (SAT) count and `T_LB1` for LB1's count
and will NOT identify them until D1 has quoted both definitions.

### R1 — the four demanded blind priors

| prior | value |
|---|---|
| P(LB1's `r+1` slopes ARE (SAT)-supported slopes in the same sense — full reconciliation, same `T` on the same object) | **0.35** |
| P(same *notion* of supportedness but a different ambient pencil/normalisation, so the counts are cousins not equals) | **0.45** |
| P(neither — genuinely different objects, CATCH-24C fires as a real equivocation) | **0.20** |
| P(`T = rho+2` shown REALIZABLE this round, by explicit construction, with the strict-`A=3` (SAT) profile) | **0.12** |
| P(a T-cap theorem this round: proved `T <= f(m) < rho+2`, i.e. vacuity) | **0.08** |
| P(a T-cap *candidate with a named axiom and a proof sketch*, short of proof) | **0.55** |
| P((NEWCAP)'s F1 fires — a realizable `T=rho+2` config with `w* > 7m-1` — CONDITIONAL on realizability being established) | **0.10** |

### R2 — the load-bearing blind arithmetic prediction (register now, check in D1)

Round-31's CATCH-24A table records `r = rho` **on this profile**
(`rh_type2_stratum/REPORT.md:65`, citing
`background/nodes/rate_half_ca_hankel_exceptional_root_charge/statement.md:128`).
If LB1 delivers `T_LB1 = r+1` and the lanes reconcile, then

```text
T_LB1 = r+1 = rho+1 = 4m
```

which is **exactly the strict target `T <= rho+1`**, i.e. exactly ONE
slope short of the failure size `rho+2` demanded by (SAT3).

> **R2 (registered blind):** the reconciliation, if it succeeds, will
> show that LB1 realizes `rho+1` and NOT `rho+2`; the failure
> hypothesis will be exactly one slope beyond a realized construction.
> P(this is the shape of the answer | full reconciliation) = **0.70**.
> P(LB1 reaches `>= rho+2` on the (SAT) count) = **0.15**.

I register in advance that if R2 resolves YES this is a *calibration*,
not a close: a construction at `rho+1` does not make `rho+2` realizable
and does not make it vacuous. I will not dress it up as either.

### R3 — numbered predictions with windows

- **P1.** The (SAT) supported-slope count is a count over the PARAMETER
  variable (slopes `gamma` with `Q_gamma` splitting in `D`), whereas
  LB1's count is a count attached to a fixed pair of columns. Predicted:
  the two agree only after a transposition/duality of the incidence
  array. P(a transposition is involved) = **0.50**.
- **P2.** No census in the repo has produced `T > 3` (brief; round 32:
  420/420). Predicted: my own targeted constructions reach
  `T >= 4` at `m=1..4`. P = **0.60**. Reaching `T = rho+2` at any
  `m >= 2` (i.e. `T >= 9`): P = **0.15**.
- **P3.** The binding axiom against large `T` will be **(SAT4)**, the
  deficit identity `sum_x (m-d_x) = 1+O <= m`, not (SAT2) and not
  (SAT3). P = **0.55**. Runner-up (SAT2) (`O <= delta = m-1`): **0.25**.
- **P4.** The pure counting identity `T*rho - O = sum_x d_x <= N*m`
  is EXACTLY consistent at `T = rho+2` (it reduces to
  `16m^2-1-O <= 16m^2`), so there is **no cheap counting contradiction**
  and any T-cap must use structure beyond the incidence layer.
  P(this is right) = **0.85**. This is registered as a prediction that
  the cheap route FAILS.
- **P5.** At `m = 1`: `rho = 3`, `rho+2 = 5`, `N = 16`, `delta = 0`, so
  `O = 0` forced and (SAT4) reads `sum_x(m-d_x) = 1` with `d_x <= 1`:
  exactly 15 of 16 columns have `d_x = 1` and one has `d_x = 0`. Then
  `sum d_x = 15` must equal `T*rho - O = 5*3 = 15`. **Consistent.**
  Predicted: `m=1` is the cleanest realizability test in existence and
  is fully enumerable. P(I can settle `m=1` realizability this round)
  = **0.65**.
- **P6.** If large `T` is realizable at `m=1`, the profile will FAIL a
  strictness/genericity side condition (`A=3` strict, or `Q_gamma`
  being the *specialized generic* apolar generator) rather than a
  counting axiom. P = **0.40**.
- **P7.** `w*` for a large-`T` configuration will come out BELOW
  `7m-1`, i.e. (NEWCAP) will be respected and F1 will not fire.
  P = **0.85** (this is the complement of the F1 prior).
- **P8.** At least one CATCH-24A subtraction will land against my own
  "new" objects this round. P = **0.90**.

### R4 — zero-power declarations pre-committed

I commit in advance to declaring ZERO POWER on: (a) any random-sampling
result about `T` (round 31 MODE A is a complete null and my sampler will
be no better); (b) any max-over-sample statement about `T` (it can
falsify a cap, never establish one); (c) small-`m` extrapolation to
`m = 2^37`; (d) any claim that an axiom is "the" binding one on the
basis of a single scale; (e) absence of a construction as evidence of
unrealizability — **failure to construct is not a T-cap**, and I will
say so in D4 rather than let the reader infer vacuity.

### R5 — route order (fixed now)

D1 definitional reconciliation (quote both definitions side by side,
file:line, CATCH-24C) -> only then construction -> D2 (SAT) profile
measurement -> D3 cap attempt / honest statement -> D4 verdict.
If D1 shows the lanes do NOT reconcile, I will say so and NOT quietly
substitute one count for the other.

### R6 — falsifiers for whatever I produce

Pre-registered: **G1** a (SAT)-profile configuration with `T > f(m)`
for my proposed cap `f`; **G2** a violation of the incidence identity
`T*rho - O = sum_x d_x`; **G3** an LB1-type object whose slope set fails
`Q_gamma` split-in-`D`; **G4** a construction meeting my cap that fails
`A=3` strictness. I will exercise every one I can afford.

### R7 — compliance plan

All interpreter runs via `tools/ramguard tiny|local -- python3 ...`
from the repo root with a literal `--` and a documented
`RAMGUARD_TIMEOUT`; stdlib only; no Modal/network/git/subagents.
`dag.json` never opened. Writes confined to
`notes/pilots_20260811/rh_sat3_realizability/`. Sibling round-33 dirs
under `notes/pilots_20260811/` excluded by an explicit filter on every
recursive grep, along with any path containing `prize-codex-`;
`notes/pilots_20260802/CAMPAIGN_LEDGER.md` never opened. Banked scripts
from `notes/pilots_20260810/` and earlier copied into my dir before any
execution. MISSES FIRST in the report.

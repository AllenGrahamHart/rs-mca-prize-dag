# (LA-EQ) and the layer-A geometry counterexamples

- **status:** PROVED (the (LA-EQ) reading; the H1 and H1+H2 refutations; the
  generalized fence's lower bound). **POSED** for (LA-PADE)/(LA-DEG).
- **closure:** constructive refutation of two hypothesis rungs + an infinite
  fence family
- **consumer:** `rate_half_band_crossing_location`
- **wired:** 2026-08-11 mint session (task #41), from the round-37 draft
  `notes/pilots_20260811/r37_mint_drafts/la_eq_and_geometry_counterexamples/`,
  coordinator line-audited; requires edge to the m = 2 fence node added,
  and the (RIC3) wiring gap the draft recorded is now closed.

## (LA-EQ) — the repricing reading

> For any hypothesis set `H` satisfied by the restriction of a strict `A=3`,
> `e=m` endpoint configuration to `7m-1` of its `>= 15m` parameter-saturated
> points, **`(LA-W COUNT | H)` IMPLIES the endpoint is empty**.

The endpoint's own nonzero kernel biform lies in the layer-A kernel of the
restriction, so a rank theorem would give nullity `0` where nullity `>= 1` is
forced. **The rank theorem was never a route to the exclusion — it is a
STRICT strengthening of it** (strict because of the refutations below). Five
lines from (SAT4)-(SAT5) + (RNC1)-(RNC2), both PROVED. A reading, not new
mathematics; priced as such.

## (H1) The first rung is CONSTRUCTIVELY FALSE

The closed form

```text
Q = (Z-g)(Z-h)C(X) + a(Z-h)sigma_g(X) - b(Z-g)sigma_h(X),   deg C <= rho
```

satisfies H1 by construction: `Q(g, .) = a(g-h)sigma_g` and
`Q(h, .) = b(g-h)sigma_h`, so `S_g` and `S_h` are two degree-`rho` supports
split over `mu_32` with `|S_g ^ S_h| = m-1 = 1`, giving
`a = |W| = 7m-1 = 13` saturated points and `26` incidences against `24`
biform coefficients — **count excess `3m^2-5m = +2`**.

Every admissible build has layer-A nullity **exactly 1**: `47/47` at `q=97`
and `37/37` at `q=193` here; `4047/4047` and `4426/4426` in the source bank
(and a fresh deterministic build at `q = 577` in the wiring audit).
Positive count excess does not force full rank.

## (H1+H2) The second rung is CONSTRUCTIVELY FALSE

Forcing H2 — **all** pair intersections `<= m-1 = 1` and `T = rho+2 = 9`
exactly — still admits exhibits. **Mechanism (made explicit here):**
prescribe the five merged second-slope VALUES `tau_1..tau_5`; then each merge
condition becomes a prescribed VALUE of `C`,

```text
x in S_g\S_h merged at tau:   C(x)(tau - h) = b*sigma_h(x),
x in S_h\S_g merged at tau:   C(x)(g - tau) = a*sigma_g(x),
```

which is **LINEAR in `C`**. Five cross pairs give `10` equations on `9`
unknowns (`C`'s eight coefficients and the scalar `a`), so solvability is
**ONE scalar condition** — solved here by scanning the fifth target slope.
Merging *across* the two sides is what keeps every new slope's support to one
point in `S_g` and one in `S_h`, which is exactly what H2 demands.

Reproduced exhibit (`q = 97`): supports `[7,7,2,2,2,2,2,1,1]`, `T = 9`,
max pair-intersection `1`, `26 x 24`, **nullity 1**.

## (FENCE-m) The fence is an INFINITE FAMILY

```text
Q_0 = Z^m - X^{2m},   W inside 4 fibres of x -> x^{2m} on mu_{16m},
Gamma = the 4m m-th roots + one spare,
a = 7m-1 saturated,   nullity EXACTLY 2m.
```

Verified here at a **fresh `m = 3`** over `mu_48` at `q = 97`: `a = 20`,
`T = 13 = 4m+1`, `rho = 4m-1 = 11`, matrix `60 x 48`, rank `42`, **nullity
`6 = 2m`**, against count excess `3m^2-5m = +12` (and at a fresh `m = 4`
over `mu_64` at `q = 193` in the wiring audit: `108 x 80`, nullity
`8 = 2m`). The bare count is dead at EVERY `m >= 2`.

**PRIOR ART — NOT re-claimed by this package.** The `m = 2` member is the
PROVED node `rate_half_layer_a_saturation_count_route_fence` (wired here as
a REQUIRES edge), and **the `Z^m - X^{2m}` generalization is already
recorded in that node's coordinator addendum**
(`background/nodes/rate_half_layer_a_saturation_count_route_fence/
statement.md:73-89`, measured `m = 2,3,4,6` over five fields). This package
contributes independent `m = 3` and `m = 4` replays and CITES, not
duplicates.

## (LA-PADE)/(LA-DEG) — the exact failure locus (POSED here)

`nullity(E_I)` equals the dimension of the simultaneous Pade/Hankel kernel
over the elementary-symmetric slope data, with reduced-basis degree formula

```text
dim K_j = max(0, 4m-d_j) + max(0, 4m-d'_j),      d_j + d'_j = 7m-1.
```

Agrees `9/9` with direct nullity in the source. The mechanism is the PROVED
`(RIC3)` (single-coefficient rational interpolation criterion,
`rate_half_bivariate_single_coefficient_rational_interpolation_criterion`),
found by subtraction after derivation. **NOT re-verified here** — carried
at POSED.

**CROSS-POINTERS OF RECORD:** the saturation-count fence node, `(RIC3)`, and
the row-surplus fence (`rate_half_bivariate_row_surplus_route_fence`, its
`m=1` instance) are three faces of one mechanism. [WIRING NOTE 2026-08-11:
the draft recorded that neither fence node cited (RIC3); the wave-59
coordinator addendum on the saturation fence node added those
cross-pointers, and this node's explicit citations close the gap from this
side.]

## The ladder terminates at the open problem

The rung that kills every constructed counterexample is (SAT2) / global block
completion (the exhibits sit at `O in [34,37]` against the cap `m-1 = 1`) —
and a configuration PASSING that rung **is** a realized (SAT3) witness at
`m = 2`. **The layer-A lane and the realizability lane are the same question
from two sides: a positive on either settles the other's negative.** The
closed form above is transportable to the realizability search as a starting
variety that satisfies the pair-union and pair-cap geometry exactly, leaving
all freedom for block completion.

## Status after this bank

Layer A remains a **per-witness instrument** (round 35's
completion-independent kills at `m = 2, 3` are untouched); the ambition of a
standalone universal exclusion at `a = 7m-1` is **RETIRED**.

## Scope

- H3/H4 untested (structural coverage via (LA-EQ) only).
- The H1+H2 refutation is `m = 2` / two-field — enough to kill the
  `m >= 2`-quantified statement, no more.
- The `O` minima are SAMPLE minima over six exhibits (**MAX/MIN-over-sample,
  not a bound**).
- The generalized fence's `2m` is constructed-lower-bound plus
  measured-equality (ten cells in the source; fresh cells at `m = 3` here
  and `m = 4` in the audit).
- **No (SAT2)-satisfying configuration at `m >= 2` was built or sought.**
  Everything hypothesis-class conditional.

## Source

- `critical/nodes/rate_half_band_crossing_location/statement.md:4270-4345`
  (Round-36 (LA-EQ) addendum, coordinator-audited; round 36 bank 1, pilot
  `r36_lawcount_geom`). Coordinator hand-checks: ibid. :4272-4278.
- (LA-EQ): ibid. :4280-4288. H1/H1+H2: ibid. :4289-4300.
- The infinite family: ibid. :4301-4308. (LA-PADE): ibid. :4309-4321.
- The ladder/(SAT2) terminus: ibid. :4322-4331.
- The retirement of the bare rank target: ibid. :3945-3954.
- Prior art for the generalization:
  `background/nodes/rate_half_layer_a_saturation_count_route_fence/statement.md:73-89`.

## Replay

```text
tools/ramguard local -- python3 \
  background/nodes/rate_half_layer_a_equivalence_and_geometry_counterexamples/verify.py
tools/ramguard local -- python3 \
  background/nodes/rate_half_layer_a_equivalence_and_geometry_counterexamples/verify_audit.py
```

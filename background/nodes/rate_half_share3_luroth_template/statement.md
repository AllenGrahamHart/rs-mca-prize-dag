# (SHARE3-m): the Lüroth pullback template and the constant-norm mechanism

- **status:** MIXED, node-level CONJECTURE (the DAG-schema bucket for
  POSED; the headline `m = 4` object does not exist). **PROVED:** the Lüroth degree arithmetic, the waste law, the
  demand calibrations, Lemma 1, the constant-norm existence mechanism.
  **POSED:** everything inheriting (OUT-m)/(DEG-m). **CONDITIONAL:** the
  flat-supply law's death regime.
- **closure:** template + existence mechanism; `m = 4` remains OPEN
- **consumer:** `rate_half_band_crossing_location`
- **wired:** 2026-08-11 mint session (task #41), from the round-37 draft
  `notes/pilots_20260811/r37_mint_drafts/share3_luroth_template/`,
  coordinator line-audited; the m=4-gap and sporadic sections carry
  round-37/38 wiring updates (see below).

## (LUR) Order-3 sharing is a Lüroth pullback

The machinery is **BANKED**: `f_weight2_inverse`'s GLOBAL PULLBACK Theorem 1
plus `payment_completeness`'s Lüroth-lattice unification (textual
ingredient citations — the DAG schema keeps CONJECTURE nodes as leaves, so
no requires edges are drawn) — the repo already states that the lattice subsumes
multiplicative and affine-involution as one class. What is new is the
*identification* of (BIV-CURVE) tuple-sharing as a lattice member, together
with the x-degree arithmetic:

```text
deg_x = k * deg_w,     k = m-1  =>  deg_w = 3 exactly,
waste  = 3(m-1) mod k.
```

**Maximal sharing is FREE in the budget** — the exact opposite of the
involution's wasted unit (`k = 2` reproduces the even-`m` lost unit).

## (DEM) The demand arithmetic

| quantity | value | status |
| --- | --- | --- |
| round-35 quadratic row `3m(m-1)-(rho-1)` | `8, 22, 42` at `m=3,4,5` | superseded |
| corrected 2-sharing row (with ceilings) | `8, 25, 47` | **banked, no closed form** |
| printed `m=4` derivation | `25 = 36 + 4 - 15` | hand-checked |
| `D(2,2)` at `m=3` | `8` | hand-checked |
| `D(3,3)` at `m=4` | `11` | hand-checked |
| `D_max(m) = (8m-9)-(4m-1)` | `4m-8`, LINEAR for `m >= 7` | hand-checked |

Best-achieved supply is `8, 12, 9` at `m = 3,4,5`, so **supply meets demand
only at `m = 3`** — which is why the `m=3` witness cost `632/24939` trials
and why the `m >= 5` fence is linear, not quadratic.

**THREE TEXT DEFECTS FOUND (see DISCREPANCY):** (i) the corrected row
`8/25/47` has no printed closed form (its residuals over `3m(m-1)-rho` are
`1, 4, 6` and nothing in the source generates them); (ii) the parenthetical
"`D_max(m) = 4m-8 ... (11 at m=4)`" conflates `D_max(4) = 8` with the
separate calibration `D(3,3) = 11` [D7 RULED NOT-A-DEFECT at round-37
triage: the `4m-8` law is `m >= 7`-scoped and the `11` at `m = 4` is the
ceilinged true value — the trap is disarmed, the display stands]; (iii) the
flat-supply bound "`>= ~m-5`, vacuous for `m <= 6`, binding from `m = 7`"
is off by one as printed.

## (CN) The constant-norm existence mechanism — and how large it really is

A 3-sharing pattern is a **line through `>= 8` of the `C(64,3) = 41664`
`mu_64`-split cubics**. Any line joining two cubics of equal root-product
stays at that product, so the `mu_N` group structure supplies the sharing at
cost `1/N`, **not** `1/q` — which is why the pilot's own registered `q^-12`
moment was refuted by `3400x` (falsifier fired, threshold withdrawn).

**Exhaustive scan at `q = 193` (this package):** the `41664` split cubics
fall into `64` equidistributed norm classes of `651` each; scanning **every**
class exhaustively gives

```text
max collinear split cubics = 31,        lines reaching >= 8 : 9152.
```

The mechanism is now explicit: **fix one root `r` and let the other two vary
at fixed product `nu/r`**. Writing `u = s+t`, one gets
`(a, b) = (-(r+u), ru + nu/r)`, which is a LINE parametrized linearly by `u`;
the members are exactly the `u` for which `y^2 - uy + nu/r` splits inside
`mu_64`. The line supply is therefore **structurally forced, not accidental**
(the wiring audit exhibits the same mechanism at the fresh field `q = 577`).

**MISS-2 GUARD, applied:** the source's `12/9/9` "complete fibres at
`q = 193/257/449`" come from SAMPLED base triples (`60-800` of `41664`,
exhaustive per base) and are gated by downstream structural verification.
The numbers above count the RAW geometric supply of lines and are **not** the
same quantity — they do not supersede the `12/9/9` census, they show the
binding constraint is not line existence.

## Status of the m=4 gap

`|W| = 27 = 7m-1` lands exactly; the selection layer is **FREE**
(`13208 + 14594` of `40000` structurally-verified legal draws); `k = 8 of 8`
reached — the first `m=4` class ever to reach its full target. **The
shortfall is `|slopes| = 14/15` against the `13` required: ONE/TWO
coincidences.** `m = 4` stays OPEN with six classes searched-negative; this
is the live route.

[WIRING UPDATE 2026-08-11 — the gap moved twice after drafting. Round 37
proved DEMAND MINIMALITY: every legal `m = 4` object needs `>= 10` merges
with EXACTLY TWO placements for the saving. Round 38 closed both placements
at reachable level: Door A (double-root outer fibre) is legal on every
axiom but BUDGET-NEUTRAL (the tangency costs one merge — deficit invariant
at 3), and DOOR B (middle-reserves-one-slope, deficit 2, the existing
14-slope objects as candidates) is the live route of record. The `15` in
"14/15" above was CORRECTED to `14` in round 38 (the `q = 257` ceiling —
the 15 was a stale count); the ceiling `14` is now three-instrument
invariant and CONJECTURE C38 poses it as intrinsic to the 11-merge
variety. See A1's round-37 (SHARE3-4)-gap and round-38 side-door addenda.]

## (DEG-m): zero selection power, decisive at completion

Tightened and relaxed 2-sharing ceilings are **BIT-IDENTICAL** (`7/12`, two
fields) — it is a completion-level condition. But every ceiling configuration
has `n_1 = 9` against the completeness bound `4`, so the 2-sharing `m=4`
negative **upgrades from a ceiling to dead-objects-at-the-ceiling**.

## The flat-supply law (PART-PROVED / CONDITIONAL)

Unconditional for pencil-image classes: no degree-1 factor (Lemma 1: Möbius
injectivity `6m > rho`) + AM-HM + Cauchy-Schwarz give required
cross-coincidence `>= ~m-5`, vacuous at small `m` and binding from `m = 7`.
With the measured Weil-type supply the pencil classes die for `q >~ 10^4` at
every `8 <= m <= 128` — **CONDITIONAL**. The `o(m^2)` supply bound is NOT
delivered; **`m = 4` is untouched by the theorem** (vacuous there,
pre-declared).

## Scope and provenance

- No `G` built, no completion, no bivariate system, nothing gated by bank
  2's verifier; `mu(x)`-at-middles unchecked at drafting. [WIRING NOTE: the
  round-38 side-door bank later ran the first gated pipeline — the Door-A
  object SURVIVES the deficiency-aware bivariate layer with `mu` forced.]
- Sporadic (non-factoring) sharing: the draft carried "unsearched, priced
  `< 1e-4`". [WIRING UPDATE 2026-08-11: CLOSED BY DICHOTOMY in round 38 —
  Z finite XOR contains a curve, and a curve forces Lüroth, with NO
  correspondence case; the sporadic cost ledger is FLAT (deficit
  `20 - delta`) and **the `< 1e-4` price was WITHDRAWN as 11 orders
  optimistic** (first moment `10^-15.3`). See A1's round-38
  sporadic/determinantal addendum.]
- Base triples SAMPLED in the source (`60-800` of `41664`, exhaustive per
  base); the constant-norm censuses are exhaustive over their named
  sub-families only.
- (OUT-m)/(DEG-m)-derived statements **inherit POSED status**.
- **COMPLIANCE CENSURE ON THE SOURCE BANK (recorded, not adjudicated):**
  round-36 bank 4 committed ONE bare-python3 breach (an empty-heredoc no-op),
  the first since the round-33 censures; the 11-pilot clean streak ended. It
  was **self-reported FIRST** and censured. Recorded here because the brief
  requires the flag in provenance; it does not bear on the mathematics.

## Source

- `critical/nodes/rate_half_band_crossing_location/statement.md`, section
  "Round-36 (SHARE3-4) addendum" (coordinator-audited; round 36 bank 4,
  pilot `r36_m4_nonsplit`; line refs drift with inline markers — anchor to
  the title; the addendum includes the AUDIT NOTE that the closed-form
  demand display is the divisible-case idealization and the ceiling version
  is operative).
- Predecessor demand law and its correction: ibid. :3731-3751.
- Round-37/38 updates: ibid., sections "Round-37 (SHARE3-4)-gap addendum"
  and "Round-38 side-door addendum" / "Round-38 sporadic/determinantal
  addendum".

## Replay

```text
tools/ramguard local -- python3 \
  background/nodes/rate_half_share3_luroth_template/verify.py
tools/ramguard tiny -- python3 \
  background/nodes/rate_half_share3_luroth_template/verify_audit.py
```

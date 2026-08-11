# The negation-closure excess and its razor kill

- **status:** PROVED (mechanism exact, counts exhaustive, kill by condition
  counting)
- **closure:** exact structural excess family with a rho-threshold fence
- **consumer:** `rate_half_band_crossing_location`
- **wired:** 2026-08-11 mint session (task #41), from the round-37 draft
  `notes/pilots_20260811/r37_mint_drafts/negation_closure_excess_fence/`,
  coordinator line-audited; the rho >= 3 symmetric-T gap carried by the
  draft has since CLOSED (see Scope).

## The find

On a **negation-closed** evaluation domain — which the official power-of-two
multiplicative subgroup IS — column-far razor-faithful pencils exist with

```text
T = 95..98        against        r + 1 = 9,
```

field-size independent, at `mu_1` down to `1.26e-7`: beating the first moment
by `750x` with **zero saturation**. The control is decisive: the same family
on the non-closed domain `{1,...,20}` gives `T = 10`.

## (NCE) The mechanism — EXACT

Let `D = {+-1, ..., +-m}` (so `n = 2m`) be negation-closed, let the error
support `T = {1, ..., r+1}` meet orbits `1..r+1` one-sidedly, and take
`e_1 = x^2 e_0` (so `d = 2`, `h_r = rho + 2`). Because `v_{-x} = (-1)^{n-1}v_x`
on a negation-closed `D` and `sum_{x in D} v_x g(x) = 0` for `deg g <= n-2`,
an **even locator** `sigma(x) = Q(x^2)`, i.e. a root set `S = A u (-A)` with
`|A| = r/2`, makes every **ODD-index** Hankel row collapse onto the orbits
that `T` does not meet. If `S` covers those orbits, the odd rows vanish
identically and what remains is

```text
ceil(rho/2)  genuine conditions on the SINGLE unknown slope gamma.     (NCE)
```

Hence

```text
rho = 2   ->  1 condition, 1 unknown  ->  ONE slope per covering even locator;
rho >= 3  ->  >= 2 conditions, 1 unknown  ->  generically NOTHING.
```

Verified here directly: the odd rows vanish on all `1158` covering even
locators scanned, and the bad set at `rho = 2` is **exactly** the covering
set (set equality, not merely equal counts).

## (CNT) The count — corrected to its general form

Let `off = m - (r+1)` be the number of orbits `T` misses. Then the number of
covering even locators is

```text
C(m - off,  r/2 - off).                                              (CNT)
```

**The banked form `C(m-1, r/2-1)` is the `off = 1` face of (CNT)** and is
NOT valid in general; the source addendum states it without that hypothesis.
(CNT) reproduces all six banked cells exactly:

| cell | `n` | `rho` | `r` | `off` | covering | bad even locators |
| --- | --- | --- | --- | --- | --- | --- |
| H1 | 20 | 2 | 8 | 1 | 84 | **84** |
| H3 | 24 | 2 | 10 | 1 | 330 | **330** |
| H4 | 26 | 3 | 10 | 2 | 165 | **0** |
| H6 | 30 | 3 | 12 | 2 | 715 | **0** |
| H7 | 34 | 3 | 14 | 2 | 3003 | **0** |
| H8 | 36 | 4 | 14 | 3 | 1365 | **0** |

**MISS-2 GUARD, fired:** at H3 the `330` bad even LOCATORS carry only `329`
DISTINCT SLOPES — two locators share a slope. Locator count and slope count
are different quantities and only the latter enters `T`.

## (KILL) Killed at the razor EXACTLY

`ceil(rho/M) = 1` requires `M >= rho = 2^34`. At `M = 2` — negation closure,
the case the official domain realises — the system is over-determined by

```text
ceil(rho/2) - 1 = 2^33 - 1 = 8589934591 conditions.
```

**This is a rho-threshold, not a field threshold: the count is `q`-free.**

**WARNING OF RECORD:** any far-CA counting argument that treats `D` as a
generic point set is **unsound at small rho**. The excess is invisible to
every first-moment estimate in the lane.

## Shape scoping (sharpened here)

Both exhibit cells sit at `r > R/2` (`8 > 5`, `10 > 6`), and so does the
**razor row at the crossing offset**: `r = 63*2^34 > 2^39 = R/2`. The proved
bound `B_ca^far(n-r) <= r+1` is established only at `r <= R/2` (shape fence
recorded on `rate_half_ca_hankel_split_pencil_equivalence`), so it covers
**neither** the exhibits **nor** the crossing offset. At the crossing offset
the cap must therefore come from the fibre pigeonhole recorded in
`rate_half_far_ca_crossing_offset_value_ledger`, not from that node.
[WIRING NOTE 2026-08-11: at drafting time that cap belonged to STATEMENT U;
U was refuted in round 37 — the crossing-offset count is
`r+1 + Theta(n/rho)` — which strengthens, not weakens, this scoping: the
proved `<= r+1` bound provably CANNOT extend to the crossing offset.]
Note `2r > R` at razor is the *same* inequality that makes the type-2
spend/list ledger vacuous by sign (sibling node
`rate_half_type2_ledger_vacuous_by_sign_fence`) — one inequality, two
fences.

## Carrier and cross-pointers

The carrier is the banked **e22 orbit-invariant locator algebra**
`L_B(X)G(X^M)`, here deployed as a far-CA bad-slope mechanism for the first
time. It is the `T_sym` mode of the (R36-D) decomposition; (KILL) is exactly
the argument that condition-kills U-sym. [WIRING NOTE 2026-08-11: U-sym is
now fully CLOSED — round 37 corrected the parity count to `ceil(rho/2)` for
the symmetric carrier `(X-x_0)P(X^2)` and measured its death at `rho = 3`,
and round 38 proved that carrier family EXHAUSTIVE by degree parity at odd
`r` (R-USYM closed). See A1's Round-37 U-rand and Round-38 URATE/genericity
addenda.]

## Scope

- All machine numbers at `q in {65537, 999983}`, `rho <= 4`.
- The draft carried "the symmetric-T variant is UNMEASURED at `rho >= 3`"
  as its named gap. [WIRING UPDATE 2026-08-11: CLOSED. Round 37 measured
  the symmetric carrier at `rho = 3` and `4` (carrier = fibre exactly,
  excess 0, 2 fields x 2 shapes x 2 domain types) after correcting the
  parity count from floor to ceil — so it dies at `rho = 3`, not `rho = 4`
  — and round 38 closed carrier-exhaustiveness (counts match
  `C(n/2,(r-1)/2)*(n-r+1)` exactly over ~560k locators). The even-locator
  mechanism (NCE) of THIS node is untouched by the correction: it already
  counts `ceil(rho/2)`.]
- The even-locator carrier is swept COMPLETELY at the scanned cells; no
  exhaustive total-`T` census at `rho >= 3` from this node (the round-37/38
  full `C(26,10)` censuses are banked on A1 separately).
- Characteristic 2 unmeasured. **ZERO POWER at razor scale by measurement.**
- **The `rho >= 3` kill is GENERIC in `q`, not field-uniform** (wiring-audit
  sharpening, 2026-08-11): the two residual conditions on one unknown can be
  accidentally consistent at rate `~#covering/q`. The wiring audit exhibited
  exactly one such accidental covering solution at H4 over `q = 1009`
  (`A = {6,9,11,12,13}`, slope `291` — `certificate.json`,
  `generic_qualifier_exhibit`), matching the predicted rate `165/1009`; at
  the banked fields `q in {65537, 999983}` the count is `0`. The razor kill
  is unaffected — its surplus is `2^33 - 1` conditions, and the accident
  rate `~1/q^(2^33-1)` is zero for every purpose.

## Source

- `critical/nodes/rate_half_band_crossing_location/statement.md:4479-4496`
  (the negation-closure-excess bullet of the Round-36 R-HRLOW addendum,
  coordinator-audited; round 36 bank 3; line refs drift with inline
  markers — anchor to the addendum title).
- Shape fence: ibid. :4541-4546. `rho=3` gap: ibid. :4494-4496 (closed by
  the Round-37 U-rand addendum, ibid. :4734-4742, and the Round-38
  URATE/genericity addendum, ibid. :5299-5305).
- Mechanism text: `notes/pilots_20260811/r36_hrlow/f4_close.py:5-21`.
- Banked scan rows: `notes/pilots_20260811/r36_hrlow/f4_results.txt:6-24`;
  control at `:26-27`; razor closed forms at `:29-45`.

## Replay

```text
tools/ramguard local -- python3 \
  background/nodes/rate_half_far_ca_negation_closure_excess_fence/verify.py
tools/ramguard tiny -- python3 \
  background/nodes/rate_half_far_ca_negation_closure_excess_fence/verify_audit.py
```

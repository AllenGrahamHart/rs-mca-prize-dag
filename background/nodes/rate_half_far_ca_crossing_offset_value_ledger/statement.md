# The far-CA value at the crossing offset: Statement U refuted, the ledger of what stands

- **status:** TARGET (the exact value of `B_ca^far(k + 2^34)`). PROVED and
  REFUTED components separated in the status ledger below.
- **closure:** value ledger — the refutation, the floor, the cap, and the
  named residues, in one place
- **consumer:** `rate_half_band_crossing_location`
- **wired:** 2026-08-11 mint session (task #41). RE-DRAFTED by the
  coordinator from the round-37 draft package
  `notes/pilots_20260811/r37_mint_drafts/statement_u/` (which was drafted
  against the round-36 pin that round 37 bank 1 refuted hours later); the
  re-draft was a recorded wiring pre-condition and folds in the round-38
  URATE/genericity results.

## Razor shape (all constants EXACT)

```text
n = 2^41,  k = R = n-k = 2^40,  rho = 2^34,
a = k + 2^34 = 1116691496960,   r = n - a = R - rho = 63*rho = 1082331758592.
```

## STATEMENT U — the round-36 definition, REFUTED as a theorem (round 37)

> (U) At razor shape, every bad slope of a column-far pencil admits a
> locator INSIDE `W = S_1 u S_2`.

U is equivalent to `T_sym = T_rand = 0` in the decomposition (R36-D) below,
and would have implied `B_ca^far(k + 2^34) = r + 1 = 1082331758593` exactly.

**U IS FALSE.** (Round-37 U-rand addendum, coordinator-audited.) The
adversary CHOOSES the collinearity: fixing `j` configurations and solving
the linear system (unknowns `2(r+1)+j`, equations `j(rho+1)`) yields
column-far razor-faithful pencils with `T = (r+1) + j` **exactly** —
verified by exhaustive census at `mu_20` (`j = 1,2,4,6,8`, three fields)
and by the full `C(26,10) = 5,311,735` census at `mu_26` (`T = 17`, a
factor `45,000` over the first moment; the round-38 exchange-law analysis
then showed even that census was search-limited — `j = 7` is reachable, so
`T = 18`, and rank-deficiency pushes `T = 19` at C3). On the razor's own
domain type; needs NO automorphism; works at `rho = 3`.

## The price of record

```text
B_ca^far(k + 2^34) = r + 1 + Theta(n/rho).
```

- **Floor (constructive, modulo TWO named residues):**
  `r + 1 + 126 = 1,082,331,758,719`. The razor design `j = 126` is exactly
  the one-common-point exact double cover (`126*rho = 2r` on the nose,
  equivalently `2(r+1) - 126*rho = 2`), with kernel dimension exactly `2`
  in closed form. Round 38 PROVED the rank half of R-GENERICITY (the
  line-pencil decoupling `rank M = j(rho+1) - L + rank Phi`; multiplicity
  `<= 2` implies full rank) and two of the four side-conditions, leaving
  the floor modulo: (i) chi-injectivity inside forced multi-edges
  (relaxable to `<= 125` collisions), and (ii) column-farness Case B.
- **Cap (normal-form-conditional):** the round-38 EXCHANGE LAW replaces
  the refuted R-URATE:

  ```text
  T <= (r+1) - delta + floor((2(r+1) - 1 + delta)/rho),
  ```

  where `delta` is the rank drop of the concurrency matrix `Phi`. At razor
  `delta = 0` is optimal (the derivative `1/rho - 1 < 0`), giving cap
  `r + 1 + 126`; but the cap is a theorem only within the shared-`A*`
  normal form, and its safety margin is PIGEONHOLE
  (`m_pig = 1.00e9` vs break-even `m* = 1.72e10`, margin `17.17x`) — not
  algebraic. At small rho the trade PROFITS: `T = 19 >` cap `18` at C3
  (`rho = 3`), full census, three fields.
- **In bits, nothing moves:** `log2(r+1) = log2(r+1+126) = 39.977280` to
  six decimals. The prize question is untouched either way.

## (R36-D) The decomposition of record

```text
T = T_fib + T_sym + T_rand.
```

- **T_fib (PROVED bracket).** With `f = |W| - r`,

  ```text
  ceil((r+1)/d) <= T_fib <= floor((r+f)/f) = floor(r/f) + 1,      (FIB)
  ```

  and `T_fib = r+1` iff `f = 1` and `chi` is injective. The upper form is a
  from-scratch pigeonhole on r-subsets of `W`: nothing is imported through
  the type-2 ledger, which is vacuous on this bracket (sibling node
  `rate_half_type2_ledger_vacuous_by_sign_fence`). At `d = 1` the floor and
  the cap coincide at `r+1`: the LB1 configuration
  (`rate_half_far_ca_hr_dictionary_common_support`), which is the `T_fib`
  part of the constructive floor.
- **T_sym (CLOSED).** Carried by the e22 orbit-invariant locator algebra
  `L_B(X)G(X^M)`; condition-killed at razor (below). Round 37 corrected
  the parity count to `ceil(rho/2)` and measured the carrier's death at
  `rho = 3`; round 38 proved the carrier family `(X-x_0)P(X^2)` EXHAUSTIVE
  by degree parity at odd `r` (R-USYM closed).
- **T_rand (the load-bearing mode).** Round 36 declared it unpriced; round
  37 priced it: `Theta(n/rho)` by the collinearity mechanism. The exact
  razor value is THE open question — the two floor residues and the cap's
  normal-form conditionality above.

## (U-SYM) The razor kill of the symmetric mode

On a `mu_M`-invariant domain the orbit-invariant locators annihilate the
non-met orbits and leave

```text
ceil(rho/M)   genuine conditions on the SINGLE unknown slope gamma.
```

The carrier therefore survives only when `ceil(rho/M) <= 1`, i.e. only when
`M >= rho = 2^34`. At `M = 2` (the negation-closed case, which the official
power-of-two multiplicative subgroup realises) the surplus is

```text
ceil(rho/2) - 1 = 2^33 - 1 = 8589934591 conditions.
```

**This is a rho-threshold, not a field threshold: the count is
q-independent.** The mechanism lives in sibling node
`rate_half_far_ca_negation_closure_excess_fence`. The draft's named gap
(the symmetric-T variant at `rho >= 3`) is CLOSED — see T_sym above.

## Status ledger

| component | status | why |
| --- | --- | --- |
| razor integers, all arithmetic here | PROVED | exact integers, replayed by both verifiers |
| (FIB) cap and its two displayed forms | PROVED | pigeonhole; forms identical for all `f >= 1` |
| (U-SYM) razor kill | PROVED | condition counting; q-free; carrier-exhaustiveness closed round 38 |
| Statement U | **REFUTED** | round-37 collinearity construction, exhaustive censuses |
| `B_ca^far(k+2^34) = r+1` (U-VAL) | **REFUTED** | falls with U; count is `r+1 + Theta(n/rho)` |
| floor `r+1+126` | constructive **modulo 2 residues** | rank half + 2 side-conditions proved (round 38) |
| cap `r+1+126` | **normal-form-conditional** | exchange law; pigeonhole margin `17.17x`, not algebraic |
| the exact value | **TARGET** | the two residues + the normal-form conditionality |

**Named breakers (round 38, of record):** an algebraic family with
`m > 1.7e10` (cosets EXCLUDED — the `X^d - c^d` identity forces `m <= 2`,
proved and measured), or a deficiency mechanism cheaper than one fibre
slope per unit (unenumerated). TRANSPORT WARNING: any "`c` conditions per
slope implies `<= 2(r+1)/c` slopes" cap is FALSE in general — the joint
rank of `Phi` is the correct object.

**Queued correspondence (answered NEGATIVE).** The T_sym carrier count at
`M = rho`, `C(128,63)`, is NOT the banked qcore plateau `C(127,64)`: the
ratio is exactly `128/65` (`0.9776` bits, one binomial step). `T_sym` does
NOT inherit the proved qcore cap by identification; any transfer must be an
inequality argument.

**Shape fence (inherited).** `B_ca^far(n-r) <= r+1` is PROVED only at the
official row's own shape `r <= R/2`; it is FALSE as a universal at
`r > R/2` on negation-closed `D` (the `T = 95` exhibit — sibling node
`rate_half_far_ca_negation_closure_excess_fence`), and after round 37 it
is also provably NOT extendable to the crossing offset (where the true
count exceeds `r+1`).

**Zero power:** everything numeric here is exact integer arithmetic on
already-banked razor constants. No measurement at razor scale exists (all
machine numbers in the source banks are at `q <= 999983`, `rho <= 4`;
exhaustive censuses at `C(20,8)/C(22,9)/C(24,10)/C(26,10)` only).

## Source

- Round-36 R-HRLOW addendum (the definition of U, (R36-D), (FIB), U-sym):
  `critical/nodes/rate_half_band_crossing_location/statement.md`, section
  "Round-36 R-HRLOW addendum" (current span :4435-4528; line refs drift
  with inline markers — anchor to the title).
- Round-37 U-rand addendum (the REFUTATION, the coset-leader frame, the
  `r+1+126` floor, FENCE-1): ibid., section "Round-37 U-rand addendum".
- Round-38 URATE/genericity addendum (the rank half proved, the exchange
  law, R-USYM closed, the two residues): ibid., section "Round-38
  URATE/genericity addendum".
- Razor constants independently banked at
  `notes/pilots_20260811/r36_hrlow/f4_results.txt:29-45`.

## Replay

```text
tools/ramguard tiny -- python3 \
  background/nodes/rate_half_far_ca_crossing_offset_value_ledger/verify.py
tools/ramguard tiny -- python3 \
  background/nodes/rate_half_far_ca_crossing_offset_value_ledger/verify_audit.py
```

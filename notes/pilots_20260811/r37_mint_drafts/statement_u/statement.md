# Statement U and the far-CA exact value at the crossing offset

- **status:** TARGET (Statement U itself). PROVED components separated below.
- **closure:** reduction of the far-CA residual to one sentence, plus the
  exact-value consequence
- **consumer:** `rate_half_band_crossing_location`

## Razor shape (all constants EXACT)

```text
n = 2^41,  k = R = n-k = 2^40,  rho = 2^34,
a = k + 2^34 = 1116691496960,   r = n - a = R - rho = 63*rho = 1082331758592.
```

## STATEMENT U (the target)

> At razor shape, every bad slope of a column-far pencil admits a locator
> INSIDE `W = S_1 u S_2`.

**(U-VAL) The exact-value consequence.** U implies

```text
B_ca^far(k + 2^34) = r + 1 = 1082331758593 = 2^39.977280   EXACTLY.
```

The floor is the banked LB1 construction; the cap is the fibre pigeonhole
(FIB) below. U is equivalent to `T_sym = T_rand = 0` in the decomposition
(R36-D).

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
  the type-2 ledger, which is vacuous on this bracket (see the sibling
  package `type2_ledger_scope_fence`). At `d = 1` the floor and the cap
  coincide at `r+1`, which is the LB1 configuration.
- **T_sym.** Requires an automorphism of order `>= rho` of the evaluation
  domain; carried by the e22 orbit-invariant locator algebra
  `L_B(X)G(X^M)`.
- **T_rand.** Moment-priced only. **Unpriced; ZERO POWER declared.**

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
q-independent.** U-sym is therefore condition-killed at razor rho.

## (U-RAND) The honest residual

`T_rand` is completely unpriced. U-rand is OPEN.

## Scope and status ledger

| component | status | why |
| --- | --- | --- |
| razor integers, (U-VAL) arithmetic | PROVED | exact integers, replayed |
| (FIB) cap and its two displayed forms | PROVED | pigeonhole; forms identical for all `f >= 1` |
| (U-SYM) razor kill | PROVED **modulo the rho=3 gap** | condition counting; q-free |
| Statement U | **TARGET** | U-rand unpriced |
| (U-VAL) as a value for `B_ca^far` | **conditional on U** | not an unconditional bound |

**Named gap carried forward (do not drop):** the symmetric-T variant is
UNMEASURED at `rho >= 3`. Parity predicts survival at `rho = 3` and death at
`rho >= 4`; there are `2^33` conditions of razor slack either way, so the gap
does not threaten the razor kill, but it is not closed.

**Queued correspondence (answered NEGATIVE here).** The T_sym carrier count
at `M = rho`, `C(128,63)`, is NOT the banked qcore plateau `C(127,64)`: the
ratio is exactly `128/65` (`0.9776` bits, one binomial step). `T_sym` does
NOT inherit the proved qcore cap by identification; any transfer must be an
inequality argument.

**Shape fence (inherited).** `B_ca^far(n-r) <= r+1` is PROVED only at the
official row's own shape `r <= R/2`; it is FALSE as a universal at `r > R/2`
on negation-closed `D` (the `T = 95` exhibit — sibling package
`negation_closure_excess_fence`).

**Zero power:** everything numeric here is exact integer arithmetic on
already-banked razor constants. No measurement at razor scale exists (all
machine numbers in the source bank are at `q <= 999983`, `rho <= 4`).

## Source

- `critical/nodes/rate_half_band_crossing_location/statement.md:4420-4505`
  (Round-36 R-HRLOW addendum, 2026-08-11, coordinator-audited; round 36
  bank 3, pilot `r36_hrlow`).
- Statement U and (U-VAL): ibid. :4482-4488.
- (R36-D): ibid. :4475-4481.
- (U-SYM) threshold: ibid. :4468-4470.
- rho=3 gap: ibid. :4472-4474.
- Queued `C(128,63)` correspondence: ibid. :4426-4429 and :4492-4495.
- Shape fence: ibid. :4496-4500.
- Razor constants independently banked at
  `notes/pilots_20260811/r36_hrlow/f4_results.txt:29-45`.
- Coordinator hand-checks recorded at ibid. :4422-4429 (all pass).

## Replay

```text
tools/ramguard tiny -- python3 \
  notes/pilots_20260811/r37_mint_drafts/statement_u/verify.py
```

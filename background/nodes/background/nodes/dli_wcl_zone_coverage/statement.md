# DLI primitive-ledger zone coverage

- **status:** see `dag.json`

At every official production row, after generated-field normalization and
first-owner de-duplication of multiplier shadows and level lifts, every one of
the 34 levels `L=1..34` satisfies

```text
W_cl(R,L) <= 1/32,                                 (WCL-ZONE)
```

where `W_cl` is exactly the C1' primitive signed-shift ledger

```text
sum_(primitive O, L+1<=w(O)<=L+5) 2N_L*2^-w(O),
N_L=256L.
```

Equivalently, every official row admits a complete per-level certificate for
that inequality. A certificate must pin the row and generated field, prove
the primitive ledger complete in the stated weight window, and prove
multiplier/lift ownership. A density bound over primes or a list of merely
exhibited relations is not coverage.

No C1' inequality, C2'' joint reserve, residual near-peak bound, or final
endpoint check is part of this statement. In particular, the old
reserve-credit mechanism is absent.


## SCHEDULE CORRECTION r2 + RAW-LEDGER RULING (2026-07-13, wave-7
## audited, w7-C1/w7-C2 = catches #205/#206, maintainer-ratified)

The production schedule of record is the dyadic odd-index tower
t = 2^33, j = 0..33, ell_j = ceil(floor(t/2^j)/2), N_j = 256*ell_j,
n'_j = 2N_j, dims (2^32,...,2,1,1) summing to t — NOT N_L = 256L at
L = 1..34 (a level-index/level-dimension conflation). W_cl is the RAW
primitive signed-shift ledger (no shadow/lift/cluster de-duplication),
per the C1' pose of record and `dli_wcl_raw_ledger_interface_guardrail`.
After the wave-7 exclusions (Newton short-window w <= 2ell; terminal
and ell-2 ambient censuses), WCL-ZONE is EQUIVALENT to six emptiness
slots: (ell,w) = (1,5),(1,6),(2,5),(2,6),(2,7),(4,9) — see
`official_terminal_attack.md`.

## NORM-GCD UPDATE (2026-07-14)

The exact `dli_wcl_ell2_weight5_norm_gcd_exclusion` certificate closes
`(ell,w)=(2,5)` on every official row. WCL-ZONE is therefore equivalent to
the five remaining emptiness slots

```text
(1,5), (1,6), (2,6), (2,7), (4,9).
```

This is a one-slot closure only; WCL-ZONE remains unproved.

## WEIGHT-SIX ROUTER UPDATE (2026-07-14)

The proved `dli_wcl_ell2_weight6_triple_cubic_router` reduces the next slot
`(ell,w)=(2,6)` to at most `1,550,336` guarded pair-product candidates.
Each candidate has two explicit division-free cyclotomic norm obstructions.
No candidate census or factor exclusion is yet claimed, so the five-slot
equivalence and WCL-ZONE status do not change.

## SPLIT-16 ROUTE CUT (2026-07-16)

The proved `dli_wcl_ell2_weight6_split16_counterfixture` gives an exact
reduced antipodal-free order-1024 six-set in `GF(65537)` satisfying both odd
moments. Since `v_2(65537-1)=16`, exact order-1024 splitting alone does not
exclude `(ell,w)=(2,6)`. The fixture is not official (`16<41`), so the
five-slot frontier is unchanged; a closing norm or ideal theorem must retain
the full official ambient valuation.

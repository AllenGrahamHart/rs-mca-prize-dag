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

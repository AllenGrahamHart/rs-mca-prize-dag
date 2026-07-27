# Tangent-floor route audit

Date: 2026-07-27.

## Finding

Upstream `tex/slackMCA_v4.tex`, `prop:floor`, proves that an RS code has at
least `m=floor(delta n)` bad slopes on one tangent line whenever
`delta<1-rho`. At an integer predecessor agreement `a`, this is

```text
m=n-a.
```

The local packet reconstructs the line directly and verifies two complete toy
RS instances. At target `2^-128`, the strict unsafe test is equivalent to

```text
n-a > floor(q/2^128)
q <= (n-a)2^128-1.
```

## Route impact

The exact six-row classifier prints all field cutoffs. They are 138-bit on
the RowC formulas and 169-bit on the prize-max formulas. This closes the
guaranteed `n-a`-slope payload on the low-field branch but that payload does
not reach the named envelope budgets. It neither certifies safety at larger
fields nor upper-bounds the full bad set of the constructed tangent line.

The remaining clean-envelope unsafe work is therefore concentrated in:

1. direct E1/value-set control on the pair-feasible generated-field class;
2. a different explicit received line;
3. an exact post-paid occupancy supplier.

## Provenance and cost

- upstream pin: `b13de8113a03f06b6fc22bbd2f289a8abcdf7e95`;
- upstream file hash:
  `810ac469b8a8a8ba4638d882ec8426be95ffddf0f8888b83315afb4d60e990b4`;
- upstream label: `prop:floor`;
- computation: bounded local exact arithmetic only; no Modal spend.

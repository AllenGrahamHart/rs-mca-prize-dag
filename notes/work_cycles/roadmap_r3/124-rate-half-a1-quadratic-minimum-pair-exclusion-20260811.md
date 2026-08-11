# Cycle 124: quadratic minimum-pair exclusion (2026-08-11)

## Cycle pins

```text
our start:       65d752a85
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         two local tiny integer verifiers
critical open:   28
```

## The `rho+3` profile is empty

For a hypothetical minimum pair, let `J` be the common light support outside
the fixed core. A residual split-pencil slope cannot support `J`: it already
contains the core and its unique difference row, so one `J` point triggers
minimum-distance line ownership. A slack slope contributes at most one `J`
incidence, and only at deficit zero.

If the common gcd degree were at most `e-2`, the global degree-`e` demand of
the `3e-R-5` rows in `J` would exceed the exact slack by

```text
e(3q-5)+R+3>0,       q=e-g>=2.
```

Thus `g=e-1`. The exact line-missing count then needs
`3e-R-6+d_L` slack incidences on `J`, while only
`e-R+3+d_L` zero-deficit slack slopes can provide them. This forces
`2e<=9`, impossible. Therefore every pair has union at least `rho+4`.

## Burn-down

```text
result:                  CLOSED the complete rho+3 pair profile
DAG delta:               +1 PROVED leaf, +1 req edge, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: exact Lane-T route cut now bankable
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The next boundary has pair union `rho+4`, coefficient-row rank at most
three, and the stronger center-line cap `4h+sum r<=rho+4`.

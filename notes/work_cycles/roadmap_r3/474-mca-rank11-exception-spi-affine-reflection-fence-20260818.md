# Cycle 474: affine-reflection exception-SPI fence

## Starting pins

```text
our SHA: ef05c8cb6
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream factor-synchronization tip: #1173 at 2788d5ec3
upstream denominator-root tip: #1156 at 7c0e45eb5
```

## Result: PROVED official-field route fence

On the official base field, put `H=mu_N`, `N=2^21`, and

```text
R_c=#{x in H:c-x in H}.
```

Ordered-pair counting gives `sum_c R_c=N^2`, while `R_0=N`. Since
`p-1=127*2^24`, the exact average over nonzero `c` is

```text
(N^2-N)/(p-1)=2064+127/1016.
```

Some nonzero reflection therefore has at least 2,065 domain points. After
deleting its possible fixed point, it has at least 1,032 two-cycles. Each
cycle `{x,c-x}` is one split fiber of

```text
X^2-cX+x(c-x).
```

Distinct cycles have distinct products and disjoint roots. This satisfies
the abstract exception-SPI interface on the exact official field, but the
reflection does not globally stabilize the multiplicative domain.

## Strategic consequence

The rank-eleven branch cannot close from a twenty-fiber bounded-degree
classification alone. Global cyclic and dihedral pullbacks are not the full
boundary: partial affine pullbacks are already forced by the ambient additive
energy. Progress must return to the retained heavy-ruling semantics or
amplify the synchronized packet past a genuine incidence threshold.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +2 edges
critical status delta: none
route delta: bare twenty-fiber classification retired on the official field
new assumptions: none
next action: owner/chronology payment or synchronized-packet amplification
```

## Nonclaims

- no explicit maximizing reflection constant is required or claimed;
- no heavy-ruling lift or unsafe received line is constructed;
- no adjacent-row safety or prize closure.

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_exception_spi_affine_reflection_fence/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_exception_spi_affine_reflection_fence/verify.py --tamper-selftest
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_exception_spi_affine_reflection_fence/verify_audit.py
```

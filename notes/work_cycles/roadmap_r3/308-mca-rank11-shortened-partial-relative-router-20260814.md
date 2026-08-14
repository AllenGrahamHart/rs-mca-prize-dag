# Cycle 308: MCA rank-11 shortened partial-relative router (2026-08-14)

Cycle 307 restores slope degree `18..31` on one selected unsafe rank-eleven
seed. The new proved node
`rate_half_mca_rank11_shortened_partial_relative_router` now sends that seed
to the standard local Grande Finale interfaces without assuming that the
deployed degree theorem is puncture-uniform.

Maximalize the 32 explanations and cancel their complete common agreement
set `C`. Non-affinity forces `|C|<K`, and the maximal-core adapter supplies
actual noncontained witnesses through `C`. At shortened parameters

```text
K'=K-c,  m'=m-c,  d=m'-K'=67472,
```

the support-collapsed interpolation system has exactly

```text
(d+1)+2(m'+1)=3m'-K'+3
```

unknowns. Thus low two-cover complexity gives either a pure-locator
certificate or a scalar-locator rational certificate of denominator degree
at most `67472`; global affinity is excluded by the dense-pair off-line
witness. Denominator roots remain explicit.

The shortened certificate

```text
Q h_i' + c_i Lambda_i' = A' + gamma_i B'
```

lifts exactly to

```text
Q h_i + c_i Lambda_i
  = (Q A_C+L_C A') + gamma_i (Q B_C+L_C B').
```

Both lifted coefficient polynomials have degree at most `m`. In the
high-complexity branch, every common coordinate contributes exactly two, so

```text
chi = chi' + 2c >= 3m-K+3 = 2299571.
```

Focused verification:

```text
RATE_HALF_MCA_RANK11_SHORTENED_PARTIAL_RELATIVE_ROUTER_PASS
  chi=2299571 toy_degree=8 stairs=4 controls=6/6
RATE_HALF_MCA_RANK11_SHORTENED_PARTIAL_RELATIVE_ROUTER_AUDIT_PASS
  chi=2299571 toy_degree=8 controls=5/5
```

No Modal computation was used.

```text
start:                   22c2c5f6f
DAG delta:               +1 PROVED local partial-relative router,
                         +3 requirement edges, +1 evidence edge
critical status delta:   none
upstream terminal delta: rank-eleven seed reaches lifted scalar-locator
                         or official high-complexity interfaces
delta-star movement:     none
compute:                 exact local arithmetic and GF(17) control only
next route action:       wire the scalar-locator branch to the pole-tolerant
                         E packet and isolate the exact same-owner
                         spread-abundance obligation for the other branch
```

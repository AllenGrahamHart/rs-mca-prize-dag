# FPC5 shifted-Johnson first-layout payment

- **status:** PROVED
- **consumer:** `l1_fpc5_large_source_payment`

Fix an official row, source scale `M`, touched count `t`, and defect degree
`d`. Use the parameters `W`, `K`, `Q_m`, and `L_m(q)` of
`l1_fpc5_shifted_johnson_grs_shell_cap`. Then the complete canonical
first-owner class across every admissible maximal source layout has size at
most

```text
A_(M,t,d)(q)=binom(M,t) W L_m(q)+M.                  (FL1)
```

More generally, for a set `Delta` of exact defect cells at one fixed
`(M,t)`, possibly with different `W_d`, `K_d`, and `m_d`, the union satisfies

```text
A_(M,t,Delta)(q)
  =binom(M,t) sum_(d in Delta) W_d L_(m_d)(q)+M.     (FL2)
```

Hence the selected class is globally paid whenever

```text
A_(M,t,Delta)(q)<=B*=floor(q/2^128).                 (FL3)
```

No multiplier over maximal source layouts occurs.

## Smallest-row global replay

At `n=8192`, the following shifted-Johnson classes are globally paid on the
printed sufficient upper field ranges:

```text
rate   M   exact shifted cells                     sufficient q
1/2    5   (t,d,u)=(4,2264,-193)                   2^228
1/4   13   (t,d,u)=(3,911,-33)                     2^233
1/8   29   (t,d,u)=(3,486,-8)                      2^220
1/16  61   (t,d,u)=(3,248,-2),(3,292,42)           2^254
```

For the rate-`1/16`, `M=61` slice, each of the other six genuinely new
shifted/nonpositive-Johnson defects `d=286,...,291` exceeds the prize budget
after the exact `binom(61,3)` touched-set multiplier, even at
`q=2^256-1`. Thus fixed-cell affordability at `d=288,...,291` does not survive
the first-layout aggregate.

## Scope

This theorem removes source-layout and touched-set multiplicity for the
selected exact shifted cells. It does not sum other source scales, touched
counts, defect cells, or FPC5 branches; it does not pay fields below the
printed sufficient gates; and it does not assert that any parameter cell is
nonempty. The six failed rate-`1/16` cells are a route cut for this exact
Haboeck/deep-point bound, not a lower bound on their true contributor count.

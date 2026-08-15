# Cycle 342: MCA rank-11 shortening-weighted kernel closure (2026-08-15)

This cycle performs the scaling audit requested by cycle 341 and closes the
remaining fixed-kernel branch without extending the uniform-cap ladder to
coranks four through nine.

## Coupled shortening invariant

Fix a corank-`d` basis `B`, put `S=K'-10`, and let `z` be the number
of common zero normals of `ker(ev_B)` outside `B`.  The support-local
shortening gap is `t=S-z`.  The same `z` controls the number of tuple
extensions:

```text
records over B:       at most M_d(t),
extensions per record: at most C(z,d+1)=C(S-t,d+1).
```

Earlier capacity cuts replaced these factors by separate maxima.  Keeping
them coupled gives

```text
M_d(t) C(S-t,d+1).
```

For `d>=2` and `t>=1`, the unfloored successive ratio is

```text
(R+d+t+1)(w+d+t)(S-t-d-1)
-------------------------------- < 1.
(R+t)(w+d+t+1)(S-t)
```

Thus every noncomplete weighted chart is controlled by `t=1`.  The proved
uniform caps handle `d=1,2,3`; exact cross multiplication at `K'=796599`
shows that `t=1` dominates the complete weighted branch for every
`d=4,...,9`, and that dominance only increases with `K'`.

## Terminal capacity polynomial

Define

```text
U_d(K')=P_d C(K'-10,d+1),           d=1,2,3,
U_d(K')=F_d(1) C(K'-11,d+1),       d=4,...,9.
```

All-bases decoration gives the direct upper bound

```text
sum_(d=1)^9 C(1048576+K',10-d) U_d(K')/(d+2).
```

Subtract this unfloored capacity from the dominant-lane demand

```text
(495405467/10^9) 274980728111260126 C(67472+K',11).
```

The difference `G(K')` is a degree-eleven polynomial.  At
`K_0=796599`, every exact Newton coefficient is positive:

```text
Delta^j G(K_0)>0,       j=0,...,11.
```

Therefore `G(K_0+s)>0` for every integer `s>=0`.  An independent audit
expands `G(K_0+s)` in ordinary powers of `s` and finds all twelve
coefficients positive.  The proof uses the unfloored capacity, so integer
rounding only strengthens the exclusion.

```text
RATE_HALF_MCA_RANK11_KERNEL_SHORTENING_WEIGHTED_EXTENSION_CAP_PASS
  dominance=6 ratios=54 controls=6/6
RATE_HALF_MCA_RANK11_KERNEL_SHORTENING_WEIGHTED_EXTENSION_CAP_AUDIT_PASS
  checks=48
RATE_HALF_MCA_RANK11_KERNEL_SHORTENING_WEIGHTED_CAPACITY_CUT_PASS
  interval=796599..1048576 newton=12 controls=7/7
RATE_HALF_MCA_RANK11_KERNEL_SHORTENING_WEIGHTED_CAPACITY_CUT_AUDIT_PASS
  positive_power_coefficients=12
```

```text
DAG delta:             +2 PROVED nodes
kernel interval:       completely removed
rank-eleven remainder: K'=10..22525 rank eight only;
                       K'=22526..37995 dense-owner chronology only
delta-star movement:   none
compute:               exact symbolic arithmetic under the 256 MB guard;
                       no Modal run needed
next route action:     attack the lower rank-eight interval or discharge
                       the chronology-correct owner terminal
```

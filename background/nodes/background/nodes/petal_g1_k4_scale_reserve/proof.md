# Proof

For a rate-preserving quotient row of length `n'`, G1 supplies a finite
first-match atlas with

```text
sum_(chart chi) (m_chi+1) <= (121/128)(n')^6.
```

K4 bounds the complete full-petal image in chart `chi` by `m_chi+1`.
Assigning every contributor to its first covering chart and summing gives the
same `(121/128)(n')^6` upper bound for the aggregate primitive payment. The
coefficient satisfies `121/128<63/64`.

The quotient-length pin is unchanged. At the four maximal petal rows, the slack
is below `n/128`; an intrinsic dyadic scale satisfies `M<=t<n/128`, hence
`M<=n/256` and `n'=n/M>=256`.

`intrinsic_scale_geometric_ledger` proves that all proper intrinsic dyadic
descendants cost less than `C n^6/63` when every row payment is
`C(n')^6`. Adding the current-row payment gives less than

```text
(64/63) C n^6 <= (64/63)(121/128)n^6 = (121/126)n^6.
```

This is strictly below the single `n^6` allocation. The cyclic-fiber descent
and exact-support projection identify each small intrinsic class with the
aperiodic quotient-row object to which quotient-closed G1 and K4 apply. Thus
the aggregate small-scale class is paid, conditional only on G1.

# L1 FPC5 large-source payment

- **status:** TARGET
- **consumer:** `l1_full_petal_fpc5_payment`

After the official small-source sieve, the remaining large source scales are

```text
rate 1/2:   M>=5,
rate 1/4:   M>=5,
rate 1/8:   M>=7,
rate 1/16:  M>=15.
```

Every cell satisfies

```text
2<=t<2M-4,       d<ell(M-2),
max(0,2d+1-t ell)->infinity.
```

The target is one disjoint polynomial/profile allocation across first-owned
sources, touched-petal sets, defects, and exact owners. Raw enumeration of
sources or touched subsets is not an admissible payment.

# E1 profile-(1,14) split-prime payment router

- **status:** PROVED
- **closure:** local cofactor census, profile-invariant norm transport, and exact payment trigger
- **scope:** binding prize rate-`1/8` row, profile `(1,14,S=18)`

Every profile-`(1,14,S=18)` collision has the same thirteen possible
cofactors as the preceding square-mass-18 profile:

```text
2,4,8,16,32,64,128,256,512,1024,514,1028,1538.
```

There are ten pure ideal families and 128 families for each split cofactor.
The square-mass/local-valuation norm argument excludes `1538`; the
profile-invariant cofactor-`1028` arguments exclude energies two, three, five,
and six. Thus

```text
T_114<=266,
cofactor 1028 can survive only at energy E=4.
```

If the queued exact E=4 norm certificate is empty, then

```text
T_114<=10+128=138,
|D_114|<=35328<39193.
```

That exact condition is sufficient to pay profile `(1,14)` and advance to
`(0,18,S=18)` with residual oriented cap `3994`. The implication and all
printed arithmetic are proved; emptiness of the E=4 certificate remains the
single pending premise.

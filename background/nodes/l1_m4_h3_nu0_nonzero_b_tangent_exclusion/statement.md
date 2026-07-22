# L1 m=4, h=3, nu=0 nonzero-b tangent exclusion

- **status:** PROVED
- **dependency:** `l1_m4_h3_euler_quotient_factorization`
- **consumer:** `l1_mixed_petal_amplification`

Assume `nu=0` and `b!=0`. Put

```text
Delta=-4a^3-27b^2 !=0,
y_0=-3b/(2a),
kappa=-48 alpha a^2/Delta.                            (NTE1)
```

For the tangent polynomial

```text
T=2aR+3b=2a(R-y_0),
```

one has

```text
rad(T) divides H-kappa.                               (NTE2)
```

If `h=deg H`, then

```text
deg rad(T)>=5-h.                                      (NTE3)
```

Consequently:

```text
h=0: H=kappa and R(0)Delta+12a^2g(R(0))=0;
h=1: impossible;
h=2: impossible;
h=3: 2<=deg rad(T)<=3 and rad(T) divides H-kappa.     (NTE4)
```

Thus the two middle `nu=0` eliminant degrees are empty on the entire
`b!=0` arm, the constant case loses one scalar, and the cubic case has a
two-or-three-point tangent passport.
This does not treat `b=0`, exclude `h=0` or `h=3`, classify their remaining
passports, treat positive valuation or wider `m`, or close L1.

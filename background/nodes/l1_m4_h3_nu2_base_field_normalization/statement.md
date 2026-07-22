# L1 m=4, h=3, nu=2 base-field normalization

- **status:** PROVED
- **dependencies:** `l1_m4_h3_nu2_prime_field_belyi_normal_form`,
  `l1_m4_positive_value_coset_certificate`
- **consumer:** `l1_mixed_petal_amplification`

The positive `(nu,deg H)=(2,1)` stratum is already empty for
`p=8191,131071`. For either remaining characteristic

```text
p in {524287,2147483647},                              (BFN1)
```

write the Belyi normalization as

```text
R(X)=lambda^p R_0(X/lambda),       R_0 in F_p[Z],
y_0=lambda^p y_0',                 y_0' in F_p^*.       (BFN2)
```

There is a nonzero `c in F_p` such that the three normalized split values
are the roots of

```text
g_0(Y)=Y^3-2c^2Y+c^3 in F_p[Y].                        (BFN3)
```

One value is `c in F_p`; the other two are the conjugate roots of
`Y^2+cY-c^2`. They lie in `F_(p^2)\F_p` because `p=2 mod 5`.

Let `C=lambda^(-1)H` be the normalized multiplicative coset, written

```text
C={z:z^n=A}.
```

Then

```text
C^p=C,       A in F_p,                                 (BFN4)
```

and the normalized complement satisfies

```text
g_0(R_0(Z))D_0(Z)=Z^n-A,
D_0 in F_p[Z].                                         (BFN5)
```

Thus this surviving positive stratum is fully base-field-normalized: one
complete fiber is Frobenius-stable, the other two are exchanged, and the
complement is stable. This does not exclude the stratum, classify its
multiplicity triples, treat `(nu,deg H)=(1,2)` or `nu=0`, classify
nonembedded `h=2`, or close L1.

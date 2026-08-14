# `A=1` shape-A center-fiber coprimality and Pade quotient

- **status:** PROVED
- **closure:** every center locator is coprime to its split-biform fiber,
  with an exact center-specialized Pade factorization
- **consumer:** `rate_half_band_crossing_location`

Retain Shape A. For a center `gamma`, write

```text
L_U0=L_Mgamma L_rest,gamma,                      (CCP1)
Qbar(gamma,X)=chi_gamma R_gamma(X)L_rest,gamma(X),
R_gamma=1                     for a small class,
R_(gamma_0)=X-x_*             for the large class.          (CCP2)
```

Then

```text
gcd_X(Qbar(gamma,X),G(gamma,X))=1                (CCP3)
```

for all three centers. Equivalently, `G(gamma,X)` is nonzero at every
actual or padded root of the center locator. In particular,

```text
G(gamma_0,x_*)!=0,
T_3(gamma_0)!=0                                  (CCP4)
```

for the exact heavy-row factorization

```text
G(t,x_*)=g_off(t)S_B(t)T_3(t).                   (CCP5)
```

There is also an exact center specialization of the Pade syzygy. Let
`B_src` denote the source numerator, so

```text
Qbar B_src-Lambda G=L_U0 P_F.                    (CCP6)
```

For every center there is a nonzero polynomial `C_gamma(X)` such that

```text
B_src(gamma,X)=L_Mgamma(X)C_gamma(X),
P_F(gamma,X)=chi_gamma R_gamma(X)C_gamma(X).      (CCP7)
```

The degree bounds are

```text
deg C_gamma<=d-1       for either small class,
deg C_(gamma_0)<=d-2   for the large class.       (CCP8)
```

Thus the large-center contact numerator is divisible by `X-x_*`, while
the split-biform center fiber is nonzero at `x_*`.

## Scope

The theorem proves center-fiber coprimality and the Pade quotient but does
not make the three center fibers linearly independent or exclude their
common source-Gram packet.

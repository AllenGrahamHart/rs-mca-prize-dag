# `A=1` core-one quadratic gap-four two-simple center spread

- **status:** PROVED
- **closure:** exact two-heavy locator design and deficit-weighted center cap
- **consumer:** `rate_half_band_crossing_location`

Retain the two-simple-root arm of the core-one scalar quadratic packet at
`u=4`. Label its heavy roots so that

```text
c_1=(e+3)/2,       c_2=(e+9)/2.                      (TSS1)
```

For every supported slope `gamma`, let `E_gamma` be the full split
degree-`rho` locator root set, and put

```text
Z_i={gamma:x_i in E_gamma},
r_gamma=1_(gamma in Z_1)+1_(gamma in Z_2).            (TSS2)
```

Then the exact block degrees are

```text
T=rho+4,       |E_gamma|=rho;
deg_Z(s_0)=T;
3rho+5 light points have degree e;
deg_Z(x_1)=(e-3)/2;
deg_Z(x_2)=(e-9)/2;
rho-8 other heavy points have degree zero.            (TSS3)
```

The two incidence sets `Z_1,Z_2` may overlap. At every supported slope the
unique radius-`rho` error has exact weight

```text
wt(f_gamma-c_gamma)=rho-r_gamma.                     (TSS4)
```

If an affine codeword line contains assigned centers at a slope set `A` of
size `h`, then

```text
h<=rho+1-sum_(gamma in A)r_gamma.                    (TSS5)
```

Consequently, for every two distinct supported slopes `alpha,beta`, at
least

```text
3+r_alpha+r_beta                                     (TSS6)
```

other supported slopes `gamma` satisfy

```text
|E_alpha union E_beta union E_gamma|>=2rho+1.        (TSS7)
```

## Scope

The theorem does not exclude the two-simple-root packet or constrain
`|Z_1 intersect Z_2|`. It supplies the exact joint support/center condition
that any field-valued realization must satisfy.

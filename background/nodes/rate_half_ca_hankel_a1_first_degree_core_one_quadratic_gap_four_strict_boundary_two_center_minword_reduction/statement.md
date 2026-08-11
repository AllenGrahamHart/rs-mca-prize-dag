# `A=1` quadratic strict-boundary two-center minimum-word reduction

- **status:** PROVED
- **closure:** exact minimum-word family at the first strict pair boundary
- **consumer:** `rate_half_band_crossing_location`

Retain either quadratic `u=4` arm and suppose distinct supported slopes
satisfy

```text
|S_alpha union S_beta|=rho+p=3p,
p=rho/2.                                             (SBR1)
```

The endpoint codeword line contains exactly the two supported centers
`alpha,beta`. Put

```text
U=S_alpha union S_beta,
U_0=U\{s_0},
r_A=r_alpha+r_beta.                                  (SBR2)
```

The endpoint missing sets

```text
M_gamma=U_0\S_gamma       (gamma in {alpha,beta})   (SBR3)
```

are disjoint and obey

```text
|M_gamma|=p+r_gamma,
|M_alpha union M_beta|=2p+r_A,
|U_0\(M_alpha union M_beta)|=p-1-r_A.               (SBR4)
```

For each of the `T-2=3e+1` off-line slopes define

```text
a_delta=|U union S_delta|-(2rho+1)>=0.              (SBR5)
```

Then

```text
sum_(delta notin {alpha,beta})a_delta=p.            (SBR6)
```

Consequently at least

```text
3e+1-p=p+2                                          (SBR7)
```

off-line slopes have `a_delta=0`. For each, the center difference

```text
g_delta=c_delta-c^L(delta),                         (SBR8)
```

where `c^L` is the endpoint codeword line, is a nonzero RS codeword with

```text
supp(g_delta)=U union S_delta,
wt(g_delta)=2rho+1=d_min.                           (SBR9)
```

At least

```text
p+2-(e-6-r_A)=(e+15)/2+r_A                         (SBR10)
```

of these zero-excess slopes also have `r_delta=0`.

For the official row, the zero-excess and deficit-free lower bounds are

```text
274877906946,
91625968989+r_A.                                    (SBR11)
```

## Scope

The theorem treats only the first strict boundary `j=p`. It does not assert
the minimum words are distinct or exclude this boundary.

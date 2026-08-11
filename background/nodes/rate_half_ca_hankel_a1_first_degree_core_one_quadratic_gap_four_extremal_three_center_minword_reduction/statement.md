# `A=1` quadratic extremal three-center minimum-word reduction

- **status:** PROVED
- **closure:** the sole floor case produces at least `2e` exact RS minimum words
- **consumer:** `rate_half_band_crossing_location`

Retain either core-one quadratic `u=4` arm and put `p=rho/2`. Every pair
obeys exactly one of the following alternatives.

## Strict branch

```text
|S_alpha union S_beta|>=rho+p=3rho/2.               (ETR1)
```

The endpoint codeword line contains no third supported assigned center.

## Extremal branch

```text
|S_alpha union S_beta|=rho+p-1=3rho/2-1.            (ETR2)
```

The endpoint codeword line contains exactly three supported slopes

```text
A={alpha,beta,theta},       sum_(gamma in A)r_gamma<=1. (ETR3)
```

Put `U=S_alpha union S_beta`, `U_0=U\{s_0}`, and for every supported slope
`delta notin A` define

```text
a_delta=|U union S_delta|-(2rho+1)>=0.               (ETR4)
```

Then

```text
sum_(delta notin A)a_delta=e.                        (ETR5)
```

There are `T-3=rho+1=3e` off-line slopes, so at least `2e` of them have
`a_delta=0`. For each such slope, choose an affine parameter chart containing
the three slopes. The affine second difference

```text
w_delta=(beta-delta)c_alpha
       +(delta-alpha)c_beta
       +(alpha-beta)c_delta                         (ETR6)
```

is a nonzero Reed--Solomon codeword with

```text
supp(w_delta)=U union S_delta,
wt(w_delta)=2rho+1=d_min.                            (ETR7)
```

Equivalently, its polynomial is a nonzero scalar multiple of the locator of
the `k-1=2rho-1` domain points outside `U union S_delta`.

## Scope

The theorem reduces the remaining equality branch to a large, coupled
family of exact minimum words. It does not prove those minimum words
distinct, form a pencil, or make the extremal branch empty.

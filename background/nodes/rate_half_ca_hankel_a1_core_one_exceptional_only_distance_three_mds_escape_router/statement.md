# `A=1` core-one distance-three MDS-escape router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_distance_router`

Retain the official exceptional-only sharp-cap profile and assume that the
quotient distance is three. Put

```text
r=2e+1,       |D_res|=8e+7,
A(X)=Q(0;X),  R_A={a:A(a)=0},       |R_A|=r-1=2e,
T={t_0,t_1,t_2},       B_T(X)=product_(t in T)(X-t).   (MER1)
```

Use the local coordinate whose exceptional slope is `z=0`, and write the
`2r+1`-term residual moment pencil as

```text
h(z)=h_0+z h_1,       c(x)=(1,x,...,x^(2r))^T.
```

There are unique coefficients with

```text
h_0=sum_(a in R_A) beta_a c(a),       beta_a!=0,
h_1=sum_(a in R_A) alpha_a c(a)+sum_(t in T) omega_t c(t),
omega_t=Theta_2/(A(t)^2 B_T'(t))!=0.                 (MER2)
```

For an ordinary supported slope `z`, let `G_z` be the `r` roots of its clean
residual locator and define

```text
j_z=#{a in R_A: beta_a+z alpha_a=0}.                  (MER3)
```

Exactly one of the following alternatives holds.

1. **Internal two-cancellation fiber.** Here `j_z=2`, and

   ```text
   G_z=(R_A minus the two cancelled roots) union T.   (MER4)
   ```

   The displayed source representation of `h(z)` is the clean `r`-point
   representation.

2. **Minimum-distance escape.** Here `j_z=0`, `G_z` is disjoint from
   `S=R_A union T`, and `S union G_z` is the support of the unique
   `2r+2`-point Vandermonde circuit. In particular there is a nonzero
   `kappa_z` such that

   ```text
   G_z(t)/A(t)=kappa_z       for every t in T,          (MER5)
   ```

   where `G_z(X)=product_(g in G_z)(X-g)`.

No ordinary supported slope has `j_z=1` or `j_z>=3`. Distinct internal
fibers cancel disjoint pairs of `R_A`.

On the official profile there are exactly

```text
e internal fibers,       3e minimum-distance escapes. (MER6)
```

The internal pairs partition `R_A`. Every external locator is supported on
the `6e+4` points of `D_res\S`; each such point lies in at most `e` external
locators, and the exact external incidence deficit is

```text
(6e+4)e-3e(2e+1)=e.                                  (MER7)
```

Consequently at least `5e+4` points outside `S` occur in exactly `e`
external locators.

This theorem does not exclude the distance-three chart. It replaces an
arbitrary family of `4e` ordinary fibers by an exact `e+3e` composition,
with disjoint internal pairs and a three-value interpolation gate on every
external locator.

# `A=1` quadratic paired all-excess residual-fiber factorization

- **status:** PROVED
- **closure:** exact fiber factorization and first jet at every off-line slope
- **consumer:** `rate_half_band_crossing_location`

Retain either paired profile. For any off-line supported slope `delta`, put

```text
I_delta=S_delta intersect U_0,
P_delta=S_delta\U,
X_delta=U_0\I_delta,
A_delta(X)=product_(x in I_delta)(X-x),
B_delta(X)=product_(x in P_delta)(X-x).            (AEF1)
```

Let `a_delta` be the union excess and `r_delta` the padded-heavy degree.
Then

```text
|I_delta|=n-a_delta-r_delta,                       (AEF2)
```

where `n=p-3` in the extremal profile and `n=p-2` in the first strict
profile.

There is a nonzero polynomial `H_delta(X)` with

```text
deg H_delta<=a_delta                               (AEF3)
```

and a nonzero scalar `zeta_delta` such that

```text
Qbar(delta,X)
 =chi_delta A_delta(X)B_delta(X)R_delta(X),

G(delta,X)
 =zeta_delta A_delta(X)H_delta(X)R_delta(X).       (AEF4)
```

Thus every off-line padded-heavy factor divides the corresponding split-
biform fiber, not only the zero-excess fibers. More exactly,

```text
deg_X G(delta,X)=n-a_delta+deg H_delta,
q_delta:=n-deg_X G(delta,X)
             =a_delta-deg H_delta.                (AEF5)
```

The residual polynomial is coprime to the outside-support locator:

```text
gcd(B_delta,H_delta)=1.
```

Consequently the complete vertical-fiber gcd is

```text
gcd_X(Qbar(delta,X),G(delta,X))
 =A_delta(X)R_delta(X)                             (AEF6)
```

up to a nonzero scalar.

At every actual-support root `x in I_delta`, the two global curves are
smooth and transverse. With `e_delta=f-c_delta`,

```text
G_t/Q_t-G_X/Q_X
 =(x-s_0)v_x L_U0'(x)e_delta(x)/Lambda(delta) !=0. (AEF7)
```

This extends the zero-excess first-jet theorem to every off-line supported
slope.

## Scope

The residual polynomial `H_delta` need not split over the base field or
have degree exactly `a_delta`. It has no root on the outside-support set,
so there are no vertical common roots beyond actual support and padding.

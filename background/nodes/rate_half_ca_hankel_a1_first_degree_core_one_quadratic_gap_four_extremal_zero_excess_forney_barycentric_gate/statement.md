# `A=1` quadratic extremal zero-excess Forney-barycentric gate

- **status:** PROVED
- **closure:** exact outside-locator interpolation at every zero-excess slope
- **consumer:** `rate_half_band_crossing_location`

Retain the extremal branch and notation of the three-center source
partition. Put `d=rho-1=2p-1`. For an off-line slope `delta` with
`a_delta=0`, define

```text
I_delta=S_delta intersect U_0,
P_delta=S_delta\U,
X_delta=U_0\I_delta.                                (FBG1)
```

Then

```text
|I_delta|=p-3-r_delta,
|P_delta|=p+2,
|X_delta|=rho+1+r_delta=d+2+r_delta.                (FBG2)
```

Let

```text
q_delta(T)=product_(x in S_delta\{s_0})(T-x),
B_delta(T)=product_(x in P_delta)(T-x),
L_X,delta(T)=product_(x in X_delta)(T-x),
L_U0(T)=product_(x in U_0)(T-x).                    (FBG3)
```

Normalize the specialized full residual locator as

```text
Q_delta=q_delta R_delta,       deg R_delta=r_delta, (FBG4)
```

where `R_delta` is the monic padded-heavy factor. There is a nonzero scalar
`kappa_delta` such that, for every `x in X_delta`,

```text
omega_x(delta)Q_delta(x)L_X,delta'(x)
 =kappa_delta R_delta(x).                           (FBG5)
```

Equivalently, after cancelling the actual inside-support locator,

```text
omega_x(delta)B_delta(x)L_U0'(x)=kappa_delta
                                      (x in X_delta). (FBG6)
```

In particular every displayed factor is nonzero. If `x in M_gamma` for a
line slope `gamma`, write `omega_x(t)=eta_x ell_gamma(t)` as in `(ESP7)`.
Then `(FBG6)` becomes the three-class law

```text
eta_x B_delta(x)L_U0'(x)
 =kappa_delta/ell_gamma(delta)
                  (x in X_delta intersect M_gamma). (FBG7)
```

There are at least

```text
2e                                                   (FBG8)
```

zero-excess slopes satisfying these identities. If
`d_A=sum_(gamma in A)r_gamma`, at least

```text
e+6+d_A                                              (FBG9)
```

of them have `r_delta=0`; there `(FBG5)` has `R_delta=1` and
`|X_delta|=rho+1`.

For the official row, `(FBG8)` and the deficit-free lower bound in `(FBG9)`
are respectively

```text
366503875926,
at least 183251937969.                              (FBG10)
```

## Scope

This is a necessary field-valued interpolation gate, not an exclusion.
The coordinate scalars `eta_x` remain unconstrained, and the locators
`B_delta` are not asserted distinct or contained in a pencil.

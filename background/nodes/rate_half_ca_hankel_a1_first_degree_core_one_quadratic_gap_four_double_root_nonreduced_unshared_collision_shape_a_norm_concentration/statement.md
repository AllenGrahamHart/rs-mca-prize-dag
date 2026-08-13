# `A=1` collision shape-A norm concentration

- **status:** PROVED
- **closure:** shape A reduces to one degree-at-most-`e` excess norm
- **consumer:** `rate_half_band_crossing_location`

Retain the sole surviving shape A. Thus the split biform `G(t,X)` is its
single large factor, with

```text
(m,n)=((e-2),(3e-7)/2),       |U_0|=(9e-7)/2,
Gamma=the 3e off-line supported slopes.            (SNC1)
```

For every `delta in Gamma`, use the all-excess fiber factorization

```text
G(delta,X)=zeta_delta A_delta(X)H_delta(X)R_delta(X),
deg H_delta=a_delta-q_delta.                       (SNC2)
```

Then all off-line padding is concentrated at the collision heavy row:

```text
product_(delta in Gamma) R_delta(X)
                    =(X-x_*)^(e-7).                (SNC3)
```

Consequently, for one nonzero scalar `c`, the complete off-line norm is

```text
product_(delta in Gamma)G(delta,X)
 =c L_U0(X)^(e-2)(X-x_*)^(e-7)T(X),               (SNC4)

T(X)=product_(delta in Gamma)H_delta(X),
deg T=e-sum_delta q_delta<=e,
gcd(T,L_U0)=1.                                     (SNC5)
```

For every `x in U_0`, with the tangent product `D_x(G)` from the off-line
norm theorem,

```text
T(x)=c^(-1)D_x(G)/
 [L_U0'(x)^(e-2)(x-x_*)^(e-7)].                   (SNC6)
```

Since `deg T<=e<|U_0|`, these values reconstruct `T` uniquely.

## Scope

The theorem does not identify `T` or exclude shape A. It removes every
padding variable and leaves one source-defined product of excess residuals
as the entire norm frontier.

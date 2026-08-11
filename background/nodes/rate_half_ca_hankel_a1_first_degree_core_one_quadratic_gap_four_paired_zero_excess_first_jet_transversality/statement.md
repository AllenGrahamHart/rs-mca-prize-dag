# `A=1` quadratic paired zero-excess first-jet transversality

- **status:** PROVED
- **closure:** exact support-root first jet and common-factor reduction
- **consumer:** `rate_half_band_crossing_location`

Retain either paired split biform. Write `Q(t,X)=Qbar(t;X)` for the
core-contracted full locator, and let `delta` be a zero-excess off-line
slope. Its two vertical fibers have the proved factorizations

```text
Q(delta,X)=chi_delta A_delta(X)B_delta(X)R_delta(X),
G(delta,X)=zeta_delta A_delta(X)R_delta(X),         (PJT1)
```

where `chi_delta,zeta_delta` are nonzero, `A_delta` is the locator of
`I_delta=S_delta intersect U_0`, `B_delta` is the outside-support locator,
and `R_delta` is the padded-heavy factor.

For every `x in I_delta`, both curves are smooth and meet transversely:

```text
J_(delta,x)
 =Q_t(delta,x)G_X(delta,x)
  -Q_X(delta,x)G_t(delta,x) !=0.                   (PJT2)
```

More exactly, let

```text
e_delta=f-c_delta,
g_delta=c_delta-c^L(delta),
b(delta)=e_delta+g_delta,
omega_x(delta)=(x-s_0)v_x b(delta)(x).             (PJT3)
```

With `Lambda` equal to the three center factors in the extremal profile and
the two endpoint factors in the strict profile,

```text
G_t/Q_t-G_X/Q_X
 =(x-s_0)v_x L_U0'(x)e_delta(x)/Lambda(delta) !=0. (PJT4)
```

All denominators in `(PJT4)` are nonzero. This formula deliberately uses
the actual nonzero error `e_delta(x)`: the Forney constant controls the
minimum-word summand `g_delta`, not the full source at a support root.

## Common-factor consequences

Take the complete gcd over the algebraic closure,

```text
C=gcd(Q,G),       (deg_X C,deg_t C)=(a,b).         (PJT5)
```

No parameter-only nonconstant factor divides `G`.

In the extremal profile,

```text
(deg_X G,deg_t G)=(p-3,e-2),
|Z_0|>=2e,       sum_(delta in Z_0)r_delta<=e-6-d_A.
```

Transversality and the padding budget force

```text
a=b=0;                                              (PJT6)
```

hence `Q` and `G` are coprime.

In the first strict profile,

```text
(deg_X G,deg_t G)=(p-2,e-1),
|Z_0|>=p+2,       sum_(delta in Z_0)r_delta<=e-6-r_A.
```

Every nonconstant common factor must have

```text
a=1,
b>=(e+15)/2+r_A,
r_A<=(e-17)/2.                                    (PJT7)
```

That last profile is also impossible. On all but at most one classified
row, an `X`-linear factor of parameter degree `b` contributes `b` distinct
off-line roots. On each off-line fiber it contributes at most one
classified root. Therefore

```text
b(2p+r_A-1)<=3e+1,                                 (PJT8)
```

which contradicts `(PJT7)`. Hence

```text
gcd(Q,G)=1                                         (PJT9)
```

in the strict profile as well.

## Scope

The theorem does not exclude the extremal or strict biform. It rules out
the tempting but false extension of the nonincidence Forney law to support
roots and proves that the full locator and split-biform curves are coprime
in both profiles.

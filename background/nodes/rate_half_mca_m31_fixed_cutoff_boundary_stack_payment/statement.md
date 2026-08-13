# Mersenne fixed-cutoff boundary-stack payment

- **status:** PROVED
- **scope:** pair-noncontained Mersenne-31 full-lift branch

Fix a deficit cutoff `h0` below the synchronized top threshold

```text
s=floor((e-K)/3),       H=e-s-1.
```

Let `P_h0(e)` be the independently truncated punctured
Johnson/mean-centered prefix through `h0`.  For every exact layer
`h0<h<=H`, put

```text
A_h=2h-e,
J_h=floor(e(A_h-c)/(A_h^2-ec)),
Q_h=floor((N-e-c)/(m-h-c)),
D_h=1+J_h(Q_h-1).
```

Under the guards

```text
2h>e,       A_h^2>ec,       N-e>m-h>c,
```

the selected family satisfies

```text
|Z| <= F_e+|T|,
F_e=P_h0(e)+sum_(h=h0+1)^H D_h,                    (BS1)
```

where `T` is the synchronized top affine line.

If `F_e+(N-m+1)<=B`, the support is safe directly.  Otherwise, if
`F_e<B`, unsafety forces

```text
L_e=B-F_e+1
```

top slopes and hence common core

```text
g_e=ceil((L_e*m-N)/(L_e-1)).
```

Put `u_e=g_e-c`, `a_e=e-u_e+K`, and let `M_e` be the punctured ordinary
Johnson cap at outside agreement `m-a_e+1`.  If that cap is legal and

```text
e*M_e+(N-m+1)<=B,                                  (BS2)
```

then the support is safe.

For the official Mersenne row, the single fixed cutoff

```text
h0=65200
```

pays every support

```text
98232<=e<=101155.
```

The first `2918` rows through `e=101149` pay directly by `(BS1)` and the
line cap.  The final six rows use `(BS2)`.  At the endpoint `e=101155`,

```text
F_e=16667033,       L_e=110183,       g_e=67446,
M_e=28,             final bound=3813469.
```

The adjacent fixed-cutoff charge at `e=101156` is `16951223>B`; this is a
method wall, not an unsafe certificate.  The Mersenne full-lift residual
now starts at `e=101156`.

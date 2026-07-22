# XR low-core oriented-difference puncture compiler

- **status:** PROVED
- **consumer:** `xr_lowcore_spread_heart`

Use the P-B setting with domain `D`, `|D|=N`, code `RS[D,K]`, agreement
`A=K+h`, and a globally generic received pair `(u,v)`. Fix one exact-`A`
selected support per slope, with all pairwise support intersections at most
`K-1`.

Fix a nonzero oriented indicator difference `(X,Y)` of width

```text
H=h+1<=t=|X|=|Y|<=K-1,
```

and let `mathcal I_(X,Y)` be its residual fiber: every `I` gives selected
supports `X union I` and `Y union I`. Put

```text
N'=N-2t,       K'=K-t,       A'=A-t=K'+h,
r'=N'-A'=N-A-t.                                                (PC1)
```

Let `Lambda_X` be the locator of `X`, and let `a_X,b_X` be the unique
degree-below-`t` interpolants to `u,v` on `X`. On
`D_0=D\(X union Y)`, define

```text
u_X'=(u-a_X)/Lambda_X,       v_X'=(v-b_X)/Lambda_X.             (PC2)
```

For every `I` in the fiber, with selected X-side slope/codeword `(z,p_z)`,
there is a unique `q_z` of degree below `K'` such that

```text
p_z=a_X+z b_X+Lambda_X q_z,
u_X'+zv_X'=q_z              on I.                               (PC3)
```

The reduced pair `(u_X',v_X')` is globally generic for agreement `A'` in
`RS[D_0,K']`, and the residual supports satisfy

```text
|I|=A',       |I intersect J|<=K'-1.                            (PC4)
```

The same construction holds from `Y`. Thus one oriented-difference fiber is
simultaneously a low-core support family for two smaller generic RS-line
instances, with the excess `h` unchanged.

The X-side reduced errors lie in an affine space of dimension at most
`K'+1`. The all-LineRay affine-core theorem therefore gives

```text
|mathcal I_(X,Y)|<=C(K'+1+r',K'+1).                             (PC5)
```

In particular, at every official row the two boundary widths
`t=K-1,K-2` have `K'=1,2`, respectively, and each fixed oriented fiber costs
strictly less than `n^3`, hence less than the P-B budget `8n^3`.

This is a per-fiber compiler and bound. It does not count oriented
differences, aggregate fibers, or prove P-B.

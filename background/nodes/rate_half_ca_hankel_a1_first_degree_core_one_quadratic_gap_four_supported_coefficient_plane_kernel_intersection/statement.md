# `A=1` quadratic supported coefficient-plane kernel intersection

- **status:** PROVED
- **closure:** exact rank-one intersection and rank-two Witt cap
- **consumer:** `rate_half_band_crossing_location`

Retain the quadratic `u=4` packet and write its primitive kernel as

```text
q(z)=sum_(i=0)^e z^i q_i,
W_q=span{q_0,...,q_e},       dim W_q=e+1.            (QKI1)
```

Let `gamma` be a supported positive-rank-loss slope away from the
correction divisor, let `c=c_gamma`, and put

```text
K_gamma=ker M_gamma=Q_min F[X]_(<=c),
H_gamma=W_q intersect K_gamma.                      (QKI2)
```

Then

```text
span{Q_gamma} subset H_gamma,
dim(H_gamma/span{Q_gamma})<=floor(c/2),             (QKI3)

dim H_gamma<=1+floor(c/2).                          (QKI4)
```

Let `T_gamma` be the `d-c` distinct contracted actual-error sources, which
are exactly the roots of `Q_min`. The coefficient evaluation matrix

```text
E_gamma=(Q_i(x))_(x in T_gamma,0<=i<=e)             (QKI5)
```

satisfies

```text
e-floor(c/2)<=rank E_gamma<=e.                      (QKI6)
```

In particular, every correction-free rank-one loss slope has

```text
H_gamma=span{Q_gamma},       rank E_gamma=e.         (QKI7)
```

At a correction-free rank-two loss slope,

```text
dim H_gamma<=2,       rank E_gamma in {e-1,e}.       (QKI8)
```

Thus `(QKI7)` holds at all but at most two supported rank-loss slopes in
the double-root arm. In the two-simple arm `(QKI6)--(QKI8)` hold away from
at most four correction slopes.

## Scope

This is a coefficient-plane rank theorem, not a packet exclusion. It does
not choose between the two possible ranks in `(QKI8)`, and it makes no
claim at a supported slope shared with the correction divisor.

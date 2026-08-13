# `A=1` quadratic squarefree unified heavy-row remainder gate

- **status:** PROVED
- **closure:** one exact constant/linear remainder gate for all squarefree double-root packets
- **consumer:** `rate_half_band_crossing_location`

Retain the double-root extremal profile and assume only that `S_B` is
squarefree. Supported/correction roots may be shared. Put

```text
J=gcd(Lambda,g_*S_B^2),       j=deg J,
H=g_*S_B^2/J.                                      (HUG1)
```

Then

```text
j<=1.                                               (HUG2)
```

There is a nonzero parameter form `T_j` of degree at most one such that

```text
G(t,x_*)=H(t)T_j(t),
T_j!=0,       deg T_j<=j<=1,
gcd(T_j,S_B)=1.                                     (HUG3)
```

More exactly, at a correction root `tau`, let

```text
r_tau=ord_tau g_* in {0,1},
c_tau=ord_tau Lambda in {0,1}.                      (HUG4)
```

Then

```text
ord_tau G(t,x_*)=r_tau+2-c_tau=ord_tau H.           (HUG5)
```

For the unique connected-weld candidate on a classified row set `X`, define
the barycentric polynomial `R_lambda` as in the separated remainder theorem.
The complete augmented heavy-row gate remains exactly

```text
H divides R_lambda,                                 (HUG6)
```

equivalently `B_H lambda=0`; on passage,

```text
R_lambda=H T_j!=0.                                  (HUG7)
```

Thus every squarefree double-root packet is reduced to one nonzero constant
or linear quotient.

## Scope

The theorem does not prove the remainder gate fails. It makes no assertion
for nonreduced `S_B` or for the two-simple correction arm.

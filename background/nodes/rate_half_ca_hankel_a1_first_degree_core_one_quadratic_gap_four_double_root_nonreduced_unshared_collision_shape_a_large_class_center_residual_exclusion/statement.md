# `A=1` shape-A large-class center-residual exclusion

- **status:** PROVED
- **closure:** the large-class rank-`r-2` branch is impossible, so all
  three interpolation defects are exactly the center fibers
- **consumer:** `rate_half_band_crossing_location`

Retain Shape A, with large-class center `gamma_0`. The large source class
has size `n+3`, but its locator-interpolation map does not take the lower
Sylvester rank:

```text
rank T_(gamma_0)=r-1.                             (LRE1)
```

Consequently

```text
im T_gamma=V_gamma={f in V:f(gamma)=0}            (LRE2)
```

for every one of the three centers, and

```text
ker(T_gamma^*)=span{G(gamma,X)}.                  (LRE3)
```

Here the transpose kernel is identified with a subspace of the common
domain coefficient space `W_X` by contraction of a minimal tensor
presentation.

For the large class, whose unique padded center root is `x_*`, the sole
defect has the explicit dual-RS values

```text
D_xG(gamma_0,x)
 =kappa_0(x-x_*)/L_M0'(x),
D_x=eta_x^(-1)/L_U0'(x)^2.                       (LRE4)
```

In particular, there is no nonzero `B_0 in W_X` such that

```text
G(gamma_0,X)=(X-x_*)B_0(X).                      (LRE5)
```

## Scope

This removes the multiplication-chain branch but does not exclude Shape A.
The remaining exact target is compatibility of the three center fibers
`G(alpha,X),G(beta,X),G(theta,X)` with the common source-Gram, split-row,
and collision identities.

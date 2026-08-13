# `A=1` shape-A center residue-pairing common-kernel router

- **status:** PROVED
- **closure:** the three locator-interpolation maps are restrictions of
  explicit corank-one residue pairings
- **consumer:** `rate_half_band_crossing_location`

Retain Shape A and put

```text
n=(3e-7)/2,       V=span_t G,       W_X=span_X G,
M_gamma={the source class at gamma}.                         (CRP1)
```

For a small center set `R_gamma=1`; for the large center `gamma_0` set

```text
R_(gamma_0)(X)=X-x_*.
```

For `f,h in S_n=F[X]_(<=n)`, define

```text
beta_gamma(f,h)
 =sum_(x in M_gamma)
   R_gamma(x)f(x)h(x)/
   [G(gamma,x)L_Mgamma'(x)].                       (CRP2)
```

Every denominator is nonzero. Each symmetric form has exact rank `n` and
radical

```text
rad(beta_gamma)=span{G(gamma,X)}.                  (CRP3)
```

Under the minimal tensor identification `W_X^*=V`, the classwise
locator-interpolation map `T_gamma:S_n->V` is, up to a nonzero scalar,

```text
h |-> [f |-> beta_gamma(f,h)] restricted to W_X.  (CRP4)
```

Consequently

```text
ker T_gamma=W_X^(perp,beta_gamma),
dim ker T_gamma=n-r+2,
rank T_gamma=r-1.                                  (CRP5)
```

Let

```text
K_cap=intersection_gamma ker T_gamma,
kappa=dim K_cap.                                   (CRP6)
```

For the combined interpolation map

```text
T=(T_alpha,T_beta,T_(gamma_0)):S_n->ker Phi,
```

one has the exact rank and resulting rank constraint

```text
rank T=n+1-kappa,
3r-(e+1)>=n+1-kappa,
r>=ceil((5e-3-2kappa)/6).                          (CRP7)
```

In particular, at the current lower boundary

```text
r=(e+1)/2,
```

Shape A requires

```text
kappa>=e-3=183251937960.                           (CRP8)
```

Thus `kappa<=e-4` would exclude that boundary and raise the separation-rank
floor by one.

## Scope

This theorem does not bound `kappa`. It replaces three anonymous weighted
evaluation matrices by explicit corank-one residue forms and isolates the
common-kernel dimension as the exact next rank quantity.

# `A=1` shape-A three-class Koszul/Gram router

- **status:** PROVED
- **closure:** exact three-quadratic generation and proportional classwise
  source Gram matrices
- **consumer:** `rate_half_band_crossing_location`

Retain Shape A and put

```text
m=e-2,       n=(3e-7)/2,       p=n+3,
R=(9e-7)/2,  r=sr(G),
V=span_F{G(t,x):x in U_0} subset F[t]_(<=m).       (KGR1)
```

Let `a=ell_alpha`, `b=ell_beta`, `c=ell_theta` and

```text
q_alpha=bc,       q_beta=ac,       q_theta=ab.     (KGR2)
```

Every source class `M_gamma` has size `n+2` or `n+3`, and its evaluated
rows span all of `V`. Moreover

```text
F[t]_(<=e)=q_alpha V+q_beta V+q_theta V.           (KGR3)
```

Thus the restricted Koszul map

```text
Phi:V^3 -> F[t]_(<=e),
(f_alpha,f_beta,f_theta)
  |-> q_alpha f_alpha+q_beta f_beta+q_theta f_theta (KGR4)
```

is surjective and

```text
dim ker Phi=3r-(e+1).                              (KGR5)
```

Define the first inverse prolongation

```text
J={h in F[t]_(<=e-3):ah,bh,ch all lie in V}.       (KGR6)
```

Then

```text
q_alpha V intersect q_beta V intersect q_theta V=abc J,
2 dim J<=3r-(e+1).                                 (KGR7)
```

The two endpoint source-frame cancellations give nonzero constants
`u_alpha,u_beta,u_theta` and one symmetric matrix `K` such that the three
classwise weighted locator Gram matrices satisfy

```text
sum_(x in M_gamma)eta_x v_x v_x^T=u_gamma K,       (KGR8)
```

where `v_x` is the coefficient vector of `Qbar(t,x)`. If `k=rank K`, then

```text
im K subset abc J,
max(0,2r-(n+2))<=k<=dim J.                         (KGR9)
```

At the earlier three-source-class rank bound `r=61083979322`, one has
`dim ker Phi=2`. If

```text
r>=137438953472,                                   (KGR10)
```

then `K` is forced nonzero. The later locator-interpolation theorem raises
the live rank floor to `91625968982`.

## Scope

This theorem does not prove that `K` is nonzero throughout the full live
rank interval and does not exclude Shape A. It identifies the exact
macroscopic obstruction: a split coefficient space `V` must simultaneously
generate the whole degree-`e` space through three quadratic shifts and
support the proportional source-Gram packet `(KGR8)--(KGR9)`.

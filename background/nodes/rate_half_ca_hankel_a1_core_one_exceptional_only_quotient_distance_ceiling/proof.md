# Proof

Let `W_A` be the span of the moment columns at the `r-1=2e` roots `R_A` of
the exceptional locator. The exceptional source `h_0` belongs to `W_A`.

Fix one of the `4e` ordinary supported slopes `z`. In the local coordinate
used by the quotient-distance router, the exceptional slope is `z=0`, so an
ordinary supported slope has `z!=0`. Its middle Hankel matrix has rank `r`
and its squarefree clean locator `G_z` has a source representation

```text
h_0+z h_1=sum_(x in G_z) lambda_(z,x)c(x),
lambda_(z,x)!=0.                                      (1)
```

Reduce `(1)` modulo `W_A`. The terms at `G_z intersect R_A` disappear and
`[h_0]=0`, hence

```text
[h_1]=z^(-1) sum_(x in G_z\R_A) lambda_(z,x)[c(x)].   (2)
```

By definition, `h=delta_A(h_1)` is the least number of residual-domain
columns outside `R_A` that represent this quotient class. If
`a_z=|G_z intersect R_A|`, equation `(2)` therefore gives

```text
h<=|G_z\R_A|=r-a_z.                                   (3)
```

It remains to average the exact intersections. Every `a in R_A` is a root
of the exceptional fiber. The unique zero-trace row is not in `R_A`, and the
two-sided saturation theorem says that every other residual-domain row has
exactly `e` distinct supported parameter roots. Thus each `a in R_A` occurs
in exactly `e` supported locators. One occurrence is the exceptional slope,
so exactly `e-1` are ordinary. Double counting gives

```text
sum_(z ordinary) a_z=|R_A|(e-1)=2e(e-1).              (4)
```

Sum `(3)` over the `4e` ordinary slopes and use `(4)`:

```text
4e h
 <=4e r-2e(e-1),

h<=r-(e-1)/2
  =3(e+1)/2.                                          (5)
```

For `e=2^38-1`, the last quantity is `412316860416`. The quotient-distance
gap already proves that `h=3` or `h>=183251937965`; combining it with `(5)`
proves `(QDC3)`. Since the ambient Vandermonde argument gives `h<=r+2`, the
discarded upper interval is exactly
`412316860417,...,549755813889`. QED.

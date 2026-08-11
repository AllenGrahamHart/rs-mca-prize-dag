# Proof

For one orientation, the rank-two normal form gives `m=r_sigma+3` distinct
squarefree forms `A+xB` with common gcd degree `g` and disjoint residual
root sets. Their root union has size

```text
g+m(e-g).                                           (1)
```

The source slope `sigma` is supported but is not a root of any of these row
forms. Thus `(1)` is at most `T-1=3e+2`, not merely `T`. Rearrangement gives

```text
(r_sigma+2)g>=r_sigma e-2,                          (2)
```

and the target endpoint is a common root, so `g>=1`. This proves `(OGC1)`.

Now assume `r_alpha=r_beta=0`. The endpoint locators have no padded roots.
The oriented normal-form proof shows that every root of `G_X` has its center
on the codeword pencil through the endpoint centers. The root `beta` belongs
to `G_X`, while `alpha` does not.

Take `delta in Z(G_X)\{beta}`. Every `x in X` lies in `S_delta`. On the
endpoint codeword pencil, every coordinate in `Y` is nonzero at `alpha`,
zero at `beta`, and therefore nonzero at every third slope. Hence

```text
Y subset S_delta,
```

so `delta` is a common root of all reverse row forms and belongs to `G_Y`.
The reverse argument gives

```text
Z(G_X)\{beta}=Z(G_Y)\{alpha}.                       (3)
```

This proves `(OGC2)` and equality of the two gcd degrees.

It remains to compare residual roots. Outside `G_X`, a supported slope is a
root of at most one forward form; outside `G_Y`, it is a root of at most one
reverse form. Suppose one slope `delta` were both a forward and reverse
residual root. Its locator would contain the fixed core point, one point of
`X`, and one point of `Y`. Since

```text
E_alpha union E_beta=S_alpha union S_beta
```

has size `rho+3`,

```text
|E_alpha union E_beta union E_delta|
 <=(rho+3)+rho-3=2rho.                              (4)
```

Minimum distance puts the center at `delta` on the endpoint codeword pencil.
But every third center on that pencil contains all of `X` and all of `Y`, so
`delta` would be a common gcd root in both orientations, a contradiction.
Thus no forward residual root is a reverse residual root.

The union of `Z(G_X)` and `Z(G_Y)` has `g+1` slopes by `(OGC2)`. There are
three forward forms and three reverse forms, each with `e-g` residual roots,
and all six residual root sets are pairwise disjoint. They all lie in the
`T=3e+3` supported slopes, so

```text
g+1+6(e-g)<=3e+3.                                   (5)
```

Equation `(5)` is `5g>=3e-2`, proving `(OGC3)`. Direct exact division gives
`(OGC4)`. Finally apply `(OGC1)` from an endpoint of maximum deficit; for
deficits one and two it gives the last two lines of `(OGC5)`, while `(OGC3)`
gives the first. QED.

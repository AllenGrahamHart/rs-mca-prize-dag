# Proof - L1 two-petal small-support anchor closure

Let the two positive support sizes be `a>=z`. The list threshold, after the
retained core is removed, gives

```text
a+z+r >= ell+d.                                      (1)
```

The non-planted per-petal cap gives `a<=d`. Rearranging (1),

```text
ell-r <= a+z-d <= z.                                 (2)
```

The residual numerator `W` is nonzero and has degree at most `d`. Its `r`
background agreements are distinct roots, so `r<=d`. Combining this with
the upper bound on `d` from (1) gives

```text
r <= d <= a+z+r-ell,
ell-a <= z.                                          (3)
```

Since `a<=ell` and maximality gives `r<=b<ell`, equation (1) also gives

```text
d <= a+z+r-ell <= ell+z-1 <= ell+A-1.                (4)
```

For two petals the smallest deficit is `v_(1)=ell-a`. Equations (2) and (3)
therefore imply

```text
G_R=(ell-r)+v_(1) <= 2z <= 2A.                       (5)
```

Equations (4) and (5) place every such word in the B11 bounded-defect
background-petal gate with `E_d=A-1` and `V_R=2A`. The B11 first-match router
proves that gate polynomial at the L1 lower cutoff, so the entire class is
polynomially bounded.

Now take `z=1`. Equation (2), together with the strict maximality bound
`r<ell`, forces `r=ell-1`. Substituting into (1) gives `d<=a`; the per-petal
cap gives `a<=d`, hence `d=a`. Finally `r<=d` and `a<=ell` give
`d=a in {ell-1,ell}`. This proves `(TS2)` and the singleton corollary.

# Proof

The center-fiber theorem gives, for `x in M_gamma`,

```text
G(gamma,x)=c_gamma eta_x L_Mgamma'(x)
             L_rest,gamma(x)^2 R_gamma(x),          (1)
```

where `c_gamma`, `eta_x`, and every displayed factor are nonzero. Also

```text
L_U0'(x)=L_Mgamma'(x)L_rest,gamma(x).               (2)
```

Substituting `(1)--(2)` into the matrix weights of the proved
locator-interpolation map gives

```text
eta_x^(-1)/L_U0'(x)^2
 =c_gamma R_gamma(x)/
   [G(gamma,x)L_Mgamma'(x)].                        (3)
```

This proves `(CRP4)` once `(CRP2)` is defined. Center-fiber coprimality
proves that every denominator in `(CRP2)` is nonzero.

We next determine the radical. Write `N_gamma=|M_gamma|`. Suppose
`f in S_n` lies in `rad(beta_gamma)`. Put

```text
y(x)=R_gamma(x)f(x)/G(gamma,x).                    (4)
```

Then

```text
sum_(x in M_gamma)y(x)h(x)/L_Mgamma'(x)=0
                                                        (h in S_n). (5)
```

For a small class, `N_gamma=n+2`. The dual Reed--Solomon parity formula
says that `(5)` holds exactly when `y` is constant on `M_gamma`. Hence for
some scalar `a`,

```text
f(x)=aG(gamma,x)             (x in M_gamma).       (6)
```

Both sides have degree at most `n` and agree at `n+2` points, so `(6)` is
a polynomial identity.

For the large class, `N_(gamma_0)=n+3`. The same dual-code formula says
that `(5)` holds exactly when

```text
y(x)=ax+b                       (x in M_(gamma_0)) (7)
```

for some `a,b`. Therefore

```text
R_(gamma_0)f=(aX+b)G(gamma_0,X)                    (8)
```

at `n+3` points. Both sides have degree at most `n+1`, so `(8)` is a
polynomial identity. The center-coprimality theorem gives

```text
gcd(R_(gamma_0),G(gamma_0,X))=1.                  (9)
```

Thus `R_(gamma_0)` divides `aX+b`; the quotient is a scalar and `(8)`
again gives `f in span{G(gamma_0,X)}`.

Conversely, `G(gamma,X)` is visibly in the radical: after cancellation in
`(CRP2)`, the numerator has degree at most `N_gamma-2`, so the barycentric
sum is zero. This proves `(CRP3)`, and the form has rank
`dim S_n-1=n`.

Minimality of

```text
G(t,X)=sum_(j=1)^r A_j(t)B_j(X)                   (10)
```

identifies `W_X^*` with `V`. Equation `(3)` says that the coordinates of
`T_gamma(h)` in the basis `A_j` are the functionals
`beta_gamma(B_j,h)`, up to one common nonzero scalar. This proves `(CRP4)`.

Since `G(gamma,X)` belongs to `W_X` and spans the complete radical, the
image of `W_X` in the nondegenerate quotient

```text
S_n/span{G(gamma,X)}
```

has dimension `r-1`. Its orthogonal complement therefore has codimension
`r-1` in `S_n`. This proves `(CRP5)`.

Finally, the kernel of the combined map `T` is exactly the intersection in
`(CRP6)`, so rank-nullity gives

```text
rank T=n+1-kappa.                                  (11)
```

The locator-interpolation syzygy theorem puts `im T` inside `ker Phi`, and

```text
dim ker Phi=3r-(e+1).                              (12)
```

Equations `(11)--(12)` give `(CRP7)`. At
`r=(e+1)/2`, comparison of `(11)` with `(12)` gives

```text
kappa>=n+1-r=e-3.                                  (13)
```

The official value of `e` yields `(CRP8)`. QED.

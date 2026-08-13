# Proof

Let `Gamma` be the `T=3e` off-line supported parameter values and let `X`
be the classified `R`-set. The exact row factorization gives

```text
#{(gamma,x) in Gamma x X:G(gamma,x)=0}=RM,          (1)
```

with no row multiplicities.

For a primitive factor `Q_j`, let `I_j` be its zero set on this grid. No
specialization `Q_j(-,x)` is the zero polynomial: otherwise the product
`G(-,x)` would vanish identically, contrary to its exact row degree `M`.
Likewise, no `Q_j(gamma,-)` is zero. Such a specialization would make the
parameter line at `gamma` divide `Q_j`, hence make `G(gamma,-)=0`. The row
root identity would then put every `x in X` in the radius-`rho` support
`S_gamma`, impossible because

```text
R=3p-3+d_A>rho=3e-1.                               (2)
```

Therefore a row count and a fiber count give

```text
|I_j|<=R m_j,       |I_j|<=T n_j.                  (3)
```

Every zero counted in `(1)` belongs to at least one factor, while the
content `c(X)` is nonzero on `X`. Gauss's lemma and additivity of degree
give

```text
sum_j m_j=M,       sum_j n_j<=N.                   (4)
```

Consequently

```text
RM<=sum_j |I_j|
  <=sum_j min(Rm_j,Tn_j)
  <=R sum_j m_j
  =RM.                                             (5)
```

Every inequality is an equality. In particular `Tn_j>=Rm_j` for every
factor, proving `(PMF3)`, and `|I_j|=Rm_j`. Equality in the row bound means
that every classified specialization of `Q_j` has full degree, all its
roots are in `Gamma`, and they are distinct. Equality in the union bound
makes the factor root sets disjoint.

For a clean parameter `delta`, the dual-MDS theorem gives

```text
G(delta,X)=zeta_delta A_delta(X),
deg A_delta=N,
```

where `A_delta` is squarefree and split over `U_0`. Degree in `X` is
additive in the primitive factorization, including the content:

```text
deg c+sum_j n_j=N.                                  (5a)
```

Every specialized factor has degree at most its corresponding term in
`(5a)`. Since their product at `delta` has exact degree `N`, every one has
full specialized degree. Since that product is squarefree and split, each
`Q_j(delta,-)` is squarefree and split over `U_0`, and distinct factors
have disjoint roots. The clean-fiber count is at least `e+6+d_A`, proving
`(PMF3a)`.

It remains to use the one-unit degree slack. Write

```text
c=9-2d_A in {9,7}.
```

From `(PMF1)` one has

```text
R/T=3/2-c/(6e),
N=(3M-1)/2,       M=e-2 odd.                       (6)
```

Suppose every factor had

```text
m_j<3e/c.                                          (7)
```

Then `0<c m_j/(6e)<1/2`, and `(PMF3)` implies

```text
n_j>=ceil(Rm_j/T)=ceil(3m_j/2).                    (8)
```

Let `o` be the number of odd `m_j`. Since their sum `M` is odd, `o` is odd
and at least one. Summing `(8)` gives

```text
sum_j n_j>=(3M+o)/2>=(3M+1)/2=N+1,                (9)
```

contradicting `(4)`. Hence some factor has

```text
m_j>=ceil(3e/c).                                   (10)
```

For `d_A=0`, this is `ceil(e/3)`; for `d_A=1`, it is
`ceil(3e/7)`. Substitution of the official `e` gives `(PMF5)`. QED.

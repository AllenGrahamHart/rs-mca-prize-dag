# Proof

We first remove the apparent content in `(FDT2)`. Choose one clean
parameter `delta`. The dual-MDS split-fiber theorem gives

```text
G(delta,X)=zeta_delta A_delta(X),                  (1)
```

where `zeta_delta` is nonzero and all roots of `A_delta` are distinct
points of `U_0`. If `c` were nonconstant, choose one of its roots `y` in
an algebraic closure of `F`. Equation `(1)` would force `y in U_0`, and
hence `y in F`.

On the other hand, the coefficientwise dual-MDS construction gives for
every `y in U_0`

```text
G(t,y)=L_U0'(y) H_y(t),
H_y(t)=omega_y(t)Qbar(t;y)/Lambda_A(t).            (2)
```

The evaluation points are distinct, so `L_U0'(y)` is nonzero. The source
form `omega_y` and locator row `Qbar(-;y)` are nonzero, and division by
the nonzero polynomial `Lambda_A` preserves nonzeroness. Thus the row in
`(2)` is not the zero polynomial. But `c(y)=0` in `(FDT2)` would make it
zero, a contradiction. Therefore `c in F^x`. Degree additivity in the
two variables now gives `(FDT3)`.

The preceding factor-incidence theorem proves

```text
Tn_j>=Rm_j                                         (3)
```

for every factor. Define

```text
n_j^min=ceil(Rm_j/T),       a_j=n_j-n_j^min>=0.    (4)
```

From `(FDT1)` and `q=9-2d_A`,

```text
R/T=3/2-q/(6e),
N=(3M-1)/2,       M=e-2 odd.                       (5)
```

Because `1<=m_j<=M<e`, direct rounding in `(4)--(5)` gives

```text
chi_j:=2n_j^min-3m_j
 = 1    for a small odd factor,
 =-1    for a large odd factor,
 = 0    for an ordinary-even factor,
 =-2    for a huge-even factor.                    (6)
```

Indeed, for odd `m_j`, the correction `qm_j/(6e)` crosses the half-unit
rounding boundary exactly when `qm_j>=3e`. For even `m_j`, it crosses the
one-unit boundary exactly when `qm_j>=6e`. Its maximum is strictly below
`3/2`, so there are no further cases.

Let `S,L,H` denote the numbers of small odd, large odd, and huge even
factors, and put `E=sum_j a_j`. Summing `(6)` and using `(FDT3)` and
`(5)` yields the exact deficit equation

```text
-1=2N-3M=S-L-2H+2E.                               (7)
```

The total parameter degree `M=e-2` imposes three elementary restrictions.
There are at most two large odd factors, because three of them have total
degree at least `9e/q>=e>M`. There is at most one huge even factor,
because two have total degree at least `12e/q>M`. Finally, a huge even
factor and a large odd factor would have total degree at least
`9e/q>=e>M`. Hence

```text
L<=2,       H<=1,       H=1 implies L=0.           (8)
```

If `H=0`, equations `(7)--(8)` say

```text
L=S+1+2E<=2.
```

Thus `E=0` and either `(S,L,H)=(0,1,0)` or `(1,2,0)`. If `H=1`, then
`L=0`, and `(7)` becomes `S+2E=1`. Hence `E=0` and
`(S,L,H)=(1,0,1)`. These are exactly `(FDT6)`. In all cases `E=0`, so
every `a_j=0`; equation `(4)` proves `(FDT5)`. The thresholds following
`(FDT6)` are just the definitions in `(FDT4)`. QED.

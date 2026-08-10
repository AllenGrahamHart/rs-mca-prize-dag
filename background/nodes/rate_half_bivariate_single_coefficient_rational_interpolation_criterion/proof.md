# Proof

Let `V_s(W)` be the top block of `(RIC2)`. The standard barycentric identity

```text
sum_(x in W) F(x)/sigma'_W(x)=0       for deg F<=n-2   (1)
```

shows that every polynomial `P` of degree below `r` gives a kernel vector

```text
lambda_x=P(x)/sigma'_W(x).                            (2)
```

Indeed, for `0<=i<s`, the polynomial `X^iP(X)` has degree at most
`s-1+r-1=n-2`. Conversely, `V_s(W)` has rank `s`, so its kernel has dimension
`n-s=r`; evaluation is injective on polynomials of degree below `r`.
Therefore `(2)` describes the whole kernel.

Now `lambda` lies in the kernel of the lower block of `(RIC2)` exactly when

```text
(h(x)P(x)/sigma'_W(x))_(x in W)
```

also lies in `ker V_s(W)`. By the same characterization, this holds exactly
when there is `Q` of degree below `r` with

```text
Q(x)=h(x)P(x)       on W.
```

A nonzero matrix-kernel vector has `P!=0`, proving `(RIC3)` and the first
equivalence.

For the deficient branch, let `eta` be the lower-clone variable and let its
nonzero coefficient be `kappa`. The equations are

```text
V_s lambda=0,
V_s(h lambda)+kappa eta (x_0^i)_i=0.                  (3)
```

Again write `lambda_x=P(x)/sigma'_W(x)`. The second line says that the vector
`h lambda+kappa eta e_(x_0)` belongs to `ker V_s(W)`, hence equals
`(Q(x)/sigma'_W(x))_x` for some `deg Q<r`. At every `x!=x_0` this is exactly
`Q(x)=h(x)P(x)`. At `x_0`, the nonzero scalar `kappa` determines `eta` and
imposes no further condition. This proves `(RIC4)`.

Finally, `(RIC5)` is the first elementary symmetric sum in `(SID5)`; zero
roots from deficiencies do not change it. At `m=2`, both type-1 slopes are
roots of every highest-clone polynomial on their canonical pair union. The
remaining monic linear factor defines `nu_x`, and coefficient comparison
gives `h_2=-(g+h)-nu_x`. Adding a constant does not alter the existence of a
degree-`<r` rational interpolant, proving the final specialization. QED.

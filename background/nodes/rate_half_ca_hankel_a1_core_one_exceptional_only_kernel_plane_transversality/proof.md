# Proof

The pinned-factor theorem gives

```text
rank M_0=r-1,       dim ker M_0=2.                  (1)
```

The exceptional-root theorem identifies the minimal homogeneous apolar
generator at `gamma_0` with the squarefree degree-`r-1` polynomial
`Q(gamma_0;X)`, up to a nonzero scalar. The residual divided-power form has
degree `2r`. Its two complete-intersection generator degrees sum to `2r+2`,
so the other generator has degree `r+3`. Consequently every degree-`r`
apolar form is a linear multiple of `Q(gamma_0;X)`. The degree-`r` middle
catalecticant kernel is therefore

```text
span{Q(gamma_0;X), XQ(gamma_0;X)}.                  (2)
```

In coefficient coordinates these are exactly the two vectors in `(KPT2)`.
They are independent because a nonzero polynomial and its product by `X`
are not scalar multiples. Equation `(1)` now proves `(KPT3)`.

The polynomial kernel identity is

```text
M(z)q(z)=0.
```

Its coefficient of `z` is `(KPT4)`. Since `M_0` is symmetric and both
`u,v` lie in its kernel, left multiplication of `(KPT4)` by `u^T` and
`v^T` gives the two zero pairings in `(KPT5)`.

It remains to prove the nonzero pairing. Choose a vector-space complement
`C` to `span{u,v}` on which the symmetric form `M_0` is nonsingular. In the
basis `(C,u,v)`, write its nonsingular block as `A`. The restriction of
`M_1` to the kernel plane has first row and column zero by the two pairings
already proved, so it is

```text
[[0,0],[0,beta]],       beta=v^TM_1v.               (3)
```

Deleting the `u` row and column from `M(z)` gives a maximal minor whose
coefficient of `z` is `det(A)beta`; all terms involving an off-diagonal
kernel-to-`C` entry use at least two powers of `z`. The Hankel-factor pin
proves that `adj M/z` has a nonzero specialization at `z=0`. Hence some
maximal minor has a nonzero linear coefficient, forcing `beta!=0` in `(3)`.
This proves the final assertion in `(KPT5)` and completes the theorem. QED.

# Proof

Let `f` be the number of full `M`-fibers contained in an admissible support
`R`. The residual tail has size

```text
|B_M(R)| = A-fM < M.
```

Since `A=hM+b` with `0<=b<M`, this inequality forces `f>=h`. On the other
hand, `fM<=A` forces `f<=h`. Hence every admissible support has exactly `h`
full fibers and a residual tail of size exactly `b`.

Choose the `h` full fibers in `C(N,h)` ways. In each of the remaining `N-h`
fibers choose a proper subset. The size enumerator for one proper subset is

```text
H_M(x) = sum_{j=0}^{M-1} C(M,j)x^j.
```

Consequently the number of ways to choose a residual tail of total size `b`
is `[x^b]H_M(x)^(N-h)`, proving

```text
raw_M(A) = C(N,h) [x^b]H_M(x)^(N-h).
```

The fixed-tail quotient profile uses `Q_M(A)=C(N-1,h)`. The elementary
identity

```text
C(N,h) = C(N-1,h) N/(N-h)
```

gives the claimed conversion. The argument applies at every intrinsic
periodicity scale, including `M<=t`; the condition `h<N` is exactly the
nontrivial quotient-profile range in which the printed denominator is
defined.

# Proof

The standard even Gegenbauer transformation gives

```text
C_(2M)^lambda(x)=((lambda)_M/(1/2)_M)
                  J_M^(lambda-1/2,-1/2)(2x^2-1).      (1)
```

Taking `lambda=1/4` proves the first line of `(EJN2)`. The odd Legendre
transformation and the Chebyshev doubling identities give

```text
P_(2n+1)(x)=xJ_n^(0,1/2)(2x^2-1),
T_(2n)(x)=T_n(2x^2-1),
U_(2n-1)(x)=2xU_(n-1)(2x^2-1).                        (2)
```

Use `n=L-1` in the first identity and `n=L` in the last two. This proves all
of `(EJN2)`.

The scalar in `(1)` is nonzero because every numerator and denominator index
is smaller than the characteristic. Also

```text
C_(2M)^(1/4)(0)=(-1)^M(1/4)_M/M! !=0.                (3)
```

Thus a common root of the primary and torsion equations never has `x=0`.
Likewise `C_(2M)^(1/4)(+/-1)=(1/2)_(2M)/(2M)!` is
nonzero, so the retained `x^2!=1` condition is automatic on this common-root
locus.

Division of an odd polynomial by an even polynomial leaves an odd remainder.
Since the remainder of `P_(2L-1)` modulo `C_(2M)^(1/4)` has degree less than
`2M=L`, it has a unique form `xQ(w)` with `deg Q<M`. Applying `(1),(2)` to
the Euclidean division proves `(EJN3)` and the asserted identity for `R`.

Now substitute `R=xQ` and `x^2=z` into the three polynomials `(TGR4)`. Direct
expansion gives

```text
E_(j,s)(x)=A_j(w)+xB_j(w)                              (4)
```

with exactly the six formulas in `(EJN4)`. Therefore

```text
E_(j,s)(x)E_(j,s)(-x)=A_j(w)^2-zB_j(w)^2=F_(j,s)(w).  (5)
```

If a signed branch exists, `(1)--(5)` immediately give `(EJN5)`.
Conversely, suppose `(EJN5)` holds. Over the algebraic closure choose one of
the two nonzero square roots `x` of `z`. Equation `(5)` says that either this
choice or its negative makes `E_(j,s)` zero. Both choices satisfy the primary
equation. Equations `(2),(3)` show that they also satisfy the correct torsion
equation: for `epsilon=1` the harmless factor `2x` in the `U` identity is
nonzero. The trace reconstruction in `(TGR6)` then recovers the original
signed branch. This proves the equivalence `(EJN5)`.

Three univariate polynomials have no common root over the algebraic closure
exactly when their monic gcd is one, proving `(EJN7)`. The polynomial `J` has
degree `M`; all other inputs may be reduced modulo it before the gcd. Finally,
the official values are `M=2^35`, `L=2^36`, proving `(EJN8)`. QED.

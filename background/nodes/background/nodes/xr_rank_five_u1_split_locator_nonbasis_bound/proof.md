# Proof

Restriction `W -> F^T` fails to be injective exactly when a nonzero quartic
in `W` vanishes on all four points of `T`. Such a polynomial is a scalar
multiple of the monic locator `L_T`, proving (NB1).

Write `W=ker Lambda` for a nonzero linear functional on
`F[X]_{<=4}`. For a three-set `S`, a fourth point `x notin S` completes it to
a nonbasis exactly when

```text
0=Lambda((X-x)L_S)=Lambda(XL_S)-x Lambda(L_S).          (1)
```

Call `S` degenerate when both coefficients on the right vanish. A degenerate
triple has all `N-3` possible completions; every other triple has at most one.

Consider the linear map

```text
M:F[X]_{<=3} -> F^2,
M(f)=(Lambda(f),Lambda(Xf)).                            (2)
```

If `rank M=1`, there are two cases. If `Lambda` vanishes on all cubics, then
`W=F[X]_{<=3}` and no monic quartic locator belongs to `W`. Otherwise the two
rows of (2) are proportional. Writing `lambda_j=Lambda(X^j)` gives
`lambda_(j+1)=a lambda_j` for `0<=j<=3`, with `lambda_0!=0`. Hence

```text
Lambda(f)=lambda_0 f(a),       W={f:f(a)=0}.
```

The no-common-evaluation-root hypothesis forces `a notin E`, so again no
locator `L_T` belongs to `W`. Rank zero is impossible because `Lambda` is
nonzero. Thus the only nontrivial case has `rank M=2`.

In that case the projectivized kernel of `M` is a line in the projective
space of cubics. The sharp split-locator line bound gives at most `N-2`
split cubic locators on this line. For completeness, this special case follows
by the deletion/restriction induction: deleting one evaluation point splits a
projective line transversely into at most one locator containing that point
and at most `(N-1)-2` avoiding it; if the line lies in the evaluation
hyperplane, division by the corresponding linear factor reduces to a line of
split quadratics and gives the same `N-2` bound. The boundary `N=3` is one.
Therefore the number `D` of degenerate triples obeys

```text
D<=N-2.                                                 (3)
```

Count pairs `(S,T)` in which `S` is a three-subset of the nonbasis four-set
`T`. Every `T` is counted four times. Equation (1) and (3) give

```text
4 Z_4(W,E)
 <= D(N-3)+(C(N,3)-D)
 = C(N,3)+D(N-4)
 <= C(N,3)+(N-2)(N-4).
```

Taking the integer floor proves (NB2). Applying the same argument to an
agreement subset preserves distinctness and the no-common-root hypothesis.
Substitution at sizes `10,10,8` gives nonbasis caps `42,42,20`; subtracting
from `C(10,4),C(10,4),C(8,4)` gives `168,168,50` bases.

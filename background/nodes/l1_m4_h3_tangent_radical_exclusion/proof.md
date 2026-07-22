# Proof - L1 m=4, h=3 tangent-radical exclusion

For `nu>0`, one has `R(0)=0`. The exact domain identity at zero is

```text
bD(0)=-alpha,
```

so `b!=0`. The earlier theorem gives `a!=0`; hence `y_0` in `(TRE1)` is
nonzero. If `g(y_0)=0`, then

```text
3g(y_0)-y_0g'(y_0)=2ay_0+3b=0
```

would force `g'(y_0)=0`, contradicting the three distinct roots of the outer
cubic. Thus `g(y_0)!=0` and `kappa!=0`.

Take any root `x` of `T`. Since `T(0)=3b`, it is nonzero, and `R(x)=y_0`.
The Euler quotient factorization

```text
DTV=Hg(R)-4alpha U                                    (1)
```

evaluated at `x` gives

```text
H(x)g(y_0)=4alpha U(x)=4alpha y_0/x^nu.
```

Therefore `P(x)=0`. Every distinct root of `T` is a root of the nonzero
polynomial `P`: its constant term is `-kappa`, while `nu>0`. This proves
`(TRE2)`.

Differentiate `T=2aR+3b`. Since `R=X^nu U`,

```text
T'=2aR'=2aX^(nu-1)(nu U+XU')=2aX^(nu-1)V.             (2)
```

The Euler theorem gives `V!=0` and `deg V=p+eta-4`, proving `(TRE3)`.
Also `gcd(T,X)=1`, so

```text
deg gcd(T,T')<=deg V=p+eta-4.                          (3)
```

The degree-`p` polynomial `T` has nonzero derivative. No root can have
multiplicity `p`, since that would be its only root and make the derivative
zero. Hence

```text
deg gcd(T,T')=p-deg rad(T).                            (4)
```

Combining `(TRE2)`, (3), and (4) gives

```text
p-(nu+eta)<=p+eta-4,
nu+2eta>=4,
```

which proves `(TRE4)`. Listing `0<=eta<=3-nu` proves `(TRE5)--(TRE6)` and
excludes `nu=3`.

At `(nu,eta)=(2,1)`, `(TRE2)` gives `deg rad(T)<=3`, while (3)--(4) give
`deg rad(T)>=3`. Thus the radical has degree three. It divides the cubic
`P`, so the two are proportional. Equality in (3) says the degree-`p-3`
polynomial `gcd(T,T')`, equivalently `T/rad(T)`, is proportional to the
degree-`p-3` polynomial `V`. This proves `(TRE7)`. For `(nu,eta)=(1,2)`,
the same lower bound is two and the upper bound is three.

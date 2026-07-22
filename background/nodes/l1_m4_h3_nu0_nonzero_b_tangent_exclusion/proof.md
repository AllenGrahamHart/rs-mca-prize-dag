# Proof - L1 m=4, h=3, nu=0 nonzero-b tangent exclusion

The outer cubic is squarefree, so its discriminant `Delta` in `(NTE1)` is
nonzero. At the root `y_0` of `2aY+3b`, direct substitution gives

```text
g(y_0)=b Delta/(8a^3) !=0,
4alpha y_0/g(y_0)=-48alpha a^2/Delta=kappa.           (1)
```

Let `x` be any root of `T`. Then `R(x)=y_0`. Evaluating the exact Euler
factorization

```text
D(2aR+3b)(XR')=H g(R)-4alpha R                       (2)
```

at `x` makes its left side zero. Equation (1) therefore gives
`H(x)=kappa`. This holds at every distinct tangent root, proving `(NTE2)`.

The Euler degree formula at `nu=0` is

```text
deg(XR')=p+h-4,
```

so `deg T'=deg R'=p+h-5`. The derivative is nonzero. If `r=deg rad(T)` is
the number of distinct tangent roots, then

```text
p-r=deg gcd(T,T')<=deg T'=p+h-5,
```

which proves `r>=5-h` and `(NTE3)`.

For `h>0`, the polynomial `H-kappa` is nonzero of degree `h`, so `(NTE2)`
also gives `r<=h`. Hence `5-h<=h`, which excludes `h=1,2`; at `h=3` it
gives `2<=r<=3`. For `h=0`, the degree-`p` polynomial `T` has a root over
the algebraic closure. Equation `(NTE2)` then forces the constant
`H-kappa` to vanish. This proves every line of `(NTE4)`.

For the additional constant-case equation, evaluate the original domain
identity and (2) at zero:

```text
g(R(0))D(0)=-alpha,
H g(R(0))=4alpha R(0).                                (4)
```

Thus `H=-4R(0)D(0)`. Equating this with `kappa` from `(NTE1)` and eliminating
`D(0)` through (4) gives

```text
R(0)Delta+12a^2g(R(0))=0,
```

as claimed.

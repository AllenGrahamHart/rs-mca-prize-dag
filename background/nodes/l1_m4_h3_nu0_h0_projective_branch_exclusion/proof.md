# Proof - L1 m=4, h=3, nu=0, h=0 projective branch exclusion

The dependency gives

```text
r Delta+12a^2g(r)=0,       Delta=-4a^3-27b^2.         (1)
```

Divide by `r^7`, using `A=a/r^2` and `B=b/r^3`. Equation (1) becomes

```text
27B^2-12A^2B-8A^3-12A^2=0
 =(3B+2A)(9B-4A^2-6A),                               (2)
```

which proves `(PBE2)`.

Suppose the first factor vanishes. Then

```text
2ar+3b=0,
```

so `r=y_0=-3b/(2a)` is the tangent value. Put `S=R-r` and
`m=ord_0(S)>=1`. The Euler node proves `XR'!=0`, so `S` is not a `p`th
power and `ord_0(XR')=m`. Hence the left side of

```text
D(2aR+3b)(XR')=H g(R)-4alpha R                       (3)
```

has exact order `2m` at zero.

Since `H` is constant, write the right side as `Phi(R)` with

```text
Phi(Y)=H g(Y)-4alpha Y.
```

The dependency proves `H g(r)=4alpha r`, so `Phi(r)=0`. Also

```text
3g(r)-r g'(r)=2ar+3b=0.
```

Here `r`, `g(r)`, and `alpha` are nonzero. Therefore

```text
Phi'(r)=H g'(r)-4alpha=8alpha !=0.                    (4)
```

It follows that `Phi(R)=Phi(r+S)` has exact order `m`, contradicting the
order `2m` on the left of (3). The first factor in `(PBE2)` is impossible,
and the second factor gives both forms of `(PBE3)`.

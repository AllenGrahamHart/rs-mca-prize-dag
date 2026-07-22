# Proof - L1 m=4, h=3 Euler quotient factorization

Differentiate the exact domain identity and multiply by `X`:

```text
X g'(R)R'D+X g(R)D'=n X^n
                    =4(g(R)D+alpha),                  (1)
```

because `n=4(p+1)` equals `4` in characteristic `p`. Rewriting the
Wronskian eliminant in terms of `R=X^nu U` gives

```text
X^nu H=3X R'D+X R D'-n R D.                           (2)
```

Multiply (2) by `g(R)`, multiply (1) by `R`, and subtract. The two
`R g(R)D` terms cancel. Since

```text
3g(Y)-Yg'(Y)=2aY+3b,                                  (3)
```

the result is

```text
X(2aR+3b)R'D=X^nu H g(R)-4alpha R.                    (4)
```

Finally

```text
X R'/X^nu=nu U+XU'=V,
```

and division of (4) by `X^nu` proves `(EQF3)`.

For the constant term, first take `nu>0`. Then `R(0)=0`, the original
identity gives `bD(0)=-alpha`, and `(EQF3)` at zero gives

```text
bH(0)=(4-3nu)alpha U(0).                               (5)
```

Every factor on the right is nonzero for `nu=1,2,3`, so `H(0)!=0`. If
`nu=0`, then `V(0)=0`, while `(EQF3)` gives

```text
H(0)g(U(0))=4alpha U(0).
```

Here `U(0)!=0` and `g(U(0))D(0)=-alpha`, so again `H(0)!=0`.

The right side of `(EQF3)` has degree exactly `3p+h`: its leader comes from
`H R^3`, while `U` has degree only `p-nu`. On the left, `D` has degree
`p+4`, `2aR+3b` has degree `p` because `a!=0`, and `V` cannot vanish.
Degree comparison gives

```text
(p+4)+p+deg V=3p+h,
deg V=p+h-4,
```

proving `(EQF4)`. Combining this with `0<=h<=3-nu` proves `(EQF5)`.

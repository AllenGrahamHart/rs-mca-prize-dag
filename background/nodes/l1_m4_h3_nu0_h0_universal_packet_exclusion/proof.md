# Proof - L1 m=4, h=3, nu=0, h=0 universal packet exclusion

Assume `(UPE1)`. Then

```text
g(Y)=Y^3+6r^2Y+20r^3,
Delta=-11664r^6,
H=-48alpha a^2/Delta=4alpha/(27r^2).                  (1)
```

Substitute these values into the exact Euler factorization

```text
D(2aR+3b)(XR')=Hg(R)-4alpha R.
```

The two nonconstant factors are

```text
2aR+3b=12r^2(R+5r),
R^3-21r^2R+20r^3=(R-r)(R-4r)(R+5r).
```

Cancelling `R+5r` gives

```text
DXR'=alpha(R-r)(R-4r)/(81r^4).                       (2)
```

Now put

```text
F=X^n(R-4r)/(D(R-r)^4).
```

The domain identity `g(R)D=X^n-alpha`, its derivative, and the rational
identity

```text
1/(Y-4r)+g'(Y)/g(Y)-4/(Y-r)
 =324r^4/((Y-r)(Y-4r)g(Y))                           (3)
```

give

```text
F'/F
 =n/X-nX^(n-1)/(X^n-alpha)
   +R'(1/(R-4r)+g'(R)/g(R)-4/(R-r))
 =-4alpha/(X(X^n-alpha))+4alpha/(Xg(R)D)
 =0.                                                  (4)
```

Here the scalar `n=4(p+1)` equals `4` in characteristic `p`, and (2) is used
in the second term. The coefficient field is finite and hence perfect, so
the kernel of the rational derivative is `F(X^p)=F(X)^p`. This proves
`(UPE2)` and, in particular, every valuation of `F` is divisible by `p`.

Let `m=ord_0(R-r)`. One has `1<=m<p`: equality with `p` would make the monic
degree-`p` polynomial `R-r` equal to `X^p`, contradicting (2). Since
`D(0)!=0`, `r!=0`, and `n=4(p+1)`,

```text
ord_0(F)=n-4m=4(p+1-m).
```

Divisibility by `p` forces `m=1`.

Let `x!=0` be a root of `R-r` of multiplicity `e`. Since `R-r` has total
degree `p` and already has the simple root zero, `1<=e<=p-1`. Also
`R(x)-4r=-3r!=0`. If `d in {0,1}` is the multiplicity of `x` in the
squarefree polynomial `D`, then

```text
ord_x(F)=-(4e+d),       p divides 4e+d.               (5)
```

If `d=0`, (5) would make `p` divide `e`, impossible. Hence `d=1`. Every
official `p` is `3 mod 4`; because `0<4e+1<4p`, equation (5) now gives

```text
4e+1=3p,       e=(3p-1)/4.
```

Every nonzero root has this same multiplicity. For `p>3`, however,

```text
(3p-1)/4 < p-1 < (3p-1)/2.
```

Thus the remaining total multiplicity `p-1` is neither one nor at least two
copies of `e`, a contradiction. The universal packet is impossible. Combining
this with the complete packet table from the dependency proves `(UPE4)`.

# Proof - L1 official first-checkpoint split-pencil reduction

## 1. Constant difference

Let `R=F_Y-F_X`, so `deg R<=p-1`. The collision Wronskian is

```text
W=F_X'F_Y-F_XF_Y'=F_X'R-F_XR'.                      (1)
```

The Wronskian supplier gives

```text
deg W<=2p-d-2<=p-2.                                  (2)
```

If `R` were nonconstant of degree `r`, then `1<=r<p`, so `R'` has degree
`r-1`. Since the leading `Z^p` term of `F_X` has zero derivative,

```text
deg(F_XR')=p+r-1,
deg(F_X'R)<=p+r-2.
```

The leading term in `(1)` could not cancel, contradicting `(2)`. Hence
`R=c` is a nonzero constant. Equation `(1)` becomes

```text
W=cF_X'.                                             (3)
```

By `(2)`, every nonconstant term of `F_X-Z^p` has degree at most
`2p-d-1`. Absorb its constant term into `b`; this proves `(FSP3)`.

Conversely, two polynomials in `(FSP3)` differ by `c` and have Wronskian
`cQ'` of degree at most `2p-d-2`. Dividing by their product at infinity shows
their logarithmic derivatives agree through `Z^(-d-1)`, so all moments
through `d` agree. The p-free coordinates therefore agree.

## 2. Nonzero-fiber ratio multiplicity

Normalize `Q(0)=0` by absorbing its constant term into the two distinct fiber
values. At least one value, say `beta`, is nonzero. Put

```text
P(Z)=Z^p+Q(Z),       X_beta={x in H:P(x)=beta}.
```

Fix `lambda` in the order-`n` subgroup `K` underlying `H`. If both `y` and
`lambda y` lie in `X_beta`, then

```text
Q(lambda y)-lambda^p Q(y)=(1-lambda^p)beta.          (4)
```

For `lambda!=1`, the polynomial

```text
E_lambda(Z)=Q(lambda Z)-lambda^p Q(Z)
             -(1-lambda^p)beta                       (5)
```

is nonzero. Indeed, its constant term is
`-(1-lambda^p)beta`, and `lambda^p=1` would force `lambda=1` because
`K` has power-of-two order while `p` is odd. Its degree is at most
`r_d=2p-d-1`. Thus `(5)` has at most `r_d` roots, proving `(FSP5)`.

The `p^2` ordered pairs in `X_beta^2` are grouped by their ratio in `K`.
The identity ratio receives exactly `p` diagonal pairs; every other ratio
receives at most `r_d` pairs. Therefore

```text
p^2-p<=r_d(|X_beta/X_beta|-1),                        (6)
```

which proves `(FSP6)`. If

```text
r_d<=r_*(p,n)=floor((p(p-1)-1)/(n-1)),
```

then `r_d(n-1)<p(p-1)`, so

```text
1+ceil((p^2-p)/r_d)>=n+1,
```

contradicting `X_beta/X_beta subset K`. This proves `(FSP7)`.

For the uniform corollary, `11n<=256p` and `p>=3583` give

```text
256(p(p-1)-1)
 >=(p-1)(256p-11)
 >=11(p-1)(n-1).
```

Hence `r_*(p,n)>=floor(11(p-1)/256)`, proving `(FSP7a)`.

## 3. The terminal affine line

At `d=2p-2`, write

```text
F_X=Z^p+aZ+b.
```

The coefficient `a` is nonzero because `F_X` has `p` distinct roots. If
`x_0` is one root and `lambda` is the difference of two roots, then
`lambda!=0` and `lambda^p+a lambda=0`. The kernel of
`Z^p+aZ` contains the `p` points `lambda F_p` and has degree `p`, so the
complete root set is

```text
x_0+lambda F_p.                                      (7)
```

## 4. Direct terminal ratio-set check

Suppose `(7)` lies in the multiplicative coset `H=gamma K`, where `|K|=n`.
The line contains no zero. After scaling by `lambda`, put `c=x_0/lambda`.
If `c` lay in `F_p`, then `c+F_p` would contain zero, so `c notin F_p`.

All ratios of points of the line belong to `K`. We claim that the map

```text
(u,v) -> (c+u)/(c+v),       u,v in F_p              (8)
```

is injective off the diagonal, while the diagonal has the single value one.
If two ratios agree, linear independence of `1,c` over `F_p` gives

```text
u+v'=u'+v,       uv'=u'v.                            (9)
```

Put `delta=u-u'=v-v'`. The second equality gives
`delta(v'-u')=0`. If `delta!=0`, both pairs are diagonal. Thus two
off-diagonal pairs coincide, and no off-diagonal pair has value one. This
proves `(FSP8)`.

Finally `p>=3583` gives `p^2-p+1>256p/11`, while the official router gives
`n<=256p/11`. This contradicts containment of the ratio set in `K`, proving
`(FSP9)--(FSP10)`.

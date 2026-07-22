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

## 2. The terminal affine line

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
x_0+lambda F_p.                                      (4)
```

## 3. Ratio-set exclusion

Suppose `(4)` lies in the multiplicative coset `H=gamma K`, where `|K|=n`.
The line contains no zero. After scaling by `lambda`, put `c=x_0/lambda`.
If `c` lay in `F_p`, then `c+F_p` would contain zero, so `c notin F_p`.

All ratios of points of the line belong to `K`. We claim that the map

```text
(u,v) -> (c+u)/(c+v),       u,v in F_p              (5)
```

is injective off the diagonal, while the diagonal has the single value one.
If two ratios agree, linear independence of `1,c` over `F_p` gives

```text
u+v'=u'+v,       uv'=u'v.                            (6)
```

Put `delta=u-u'=v-v'`. The second equality gives
`delta(v'-u')=0`. If `delta!=0`, both pairs are diagonal. Thus two
off-diagonal pairs coincide, and no off-diagonal pair has value one. This
proves `(FSP4)`.

Finally `p>=3583` gives `p^2-p+1>24p`, while the official router gives
`n<24p`. This contradicts containment of the ratio set in `K`, proving
`(FSP5)--(FSP6)`.

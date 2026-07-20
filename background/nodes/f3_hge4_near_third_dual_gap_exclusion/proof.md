# Proof

Put `c=h+e`. The near-third Belyi theorem supplies polynomials and formal
series

```text
F=Z^(-1/3),       B=Z^(2/3)=ZF,
deg Z=e,          deg S=h,
S=F mod y^c,      Z(0)=S(0)=1.                    (1)
```

Writing the reciprocal ordered pair as

```text
U=S-ay^h,       V=S+ay^h,
D=UV=S^2-a^2y^(2h),
```

the cyclotomic complement gives

```text
DW=1-y^m,       deg W=m-2h=c.                     (2)
```

All formal coefficients used below have index below `2h`; the characteristic
hypothesis makes their defining scalars invertible.

## The dual gap

Equation `(2)` and `D(0)=1` imply

```text
[y^j]D^(-1)=0,       c<j<m.                       (3)
```

Before degree `2h`, the `a^2y^(2h)` term has not begun, so

```text
D^(-1)=S^(-2) mod y^(2h).                         (4)
```

Let `T=F-S`. From `(1)`, `T=O(y^c)`. Since `c>h`, for `j<2h<2c`,

```text
S^(-2)=(F-T)^(-2)=F^(-2)+2F^(-3)T
       =B+2ZT mod y^(2h).                          (5)
```

Write `F=sum f_jy^j`, `B=sum b_jy^j`, and
`Z=sum_(k=0)^e z_ky^k`. For `c<j<2h`, every index `j-k` is greater than
`h`. If `j-k<c`, then `f_(j-k)=0` because `S=F mod y^c` and `deg S=h`;
if `j-k>=c`, then `T_(j-k)=f_(j-k)`. Consequently

```text
[y^j]ZT=[y^j]ZF=b_j.
```

Combining `(3)--(5)` and using `3!=0` gives the second coefficient gap

```text
b_j=0,       c<j<2h.                              (6)
```

## Backward propagation

The identity `B=Z^(2/3)` satisfies

```text
3ZB'=2Z'B.
```

Its coefficient recurrence is

```text
3n b_n+sum_(k=1)^e (3n-5k)z_k b_(n-k)=0.          (7)
```

Assume `h>=2e+1`. Then `c+e=h+2e<=2h-1`, so `(6)` contains the `e`
consecutive zeros

```text
b_(c+1)=...=b_(c+e)=0.                            (8)
```

If `b_(r+1),...,b_(r+e)` vanish, apply `(7)` at `n=r+e`. Every term
vanishes except the `k=e` term, giving

```text
(3r-2e)z_e b_r=0.                                 (9)
```

Here `z_e!=0`. For `0<=r<=c`, the integer `3r-2e` lies strictly between
`-p` and `p`, so it can vanish in the field only when it is literally zero.

Because `m` is dyadic, `3` does not divide `m`; since `e=m-3h`, it also does
not divide `e`. Therefore `3r-2e` is never literally zero for an integer
`r`. Backward propagation from `(8)` reaches `b_0=0`, contradicting
`b_0=1`. This proves `(DGE2)`. Finally,
`h>=2(m-3h)+1` is equivalent to `7h>=2m+1`; its integer complement is
`7h<=2m`, proving `(DGE3)`. QED.

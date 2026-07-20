# Proof - L1 joint-Johnson source-scale gate

First suppose `b>0`. In the tail coordinates from the joint Johnson theorem,

```text
c=a+u-ell.
```

Its nonpositive-denominator condition is

```text
a^2/N+u^2/b<=c=a+u-ell.                                (1)
```

Rearranging `(1)` gives the two-universe variance constraint

```text
a(N-a)/N+u(b-u)/b>=ell.                                (2)
```

Each summand is at most one quarter of its universe size. Hence `(2)`
requires

```text
N+b>=4ell.                                              (3)
```

If `b=0`, every populated cell has `u=0` and `s=ell`, so `c=a-ell`.
Failure of the separate core-defect Johnson payment would give

```text
a^2<=Nc=N(a-ell),
a(N-a)>=Nell.                                          (4)
```

Again `a(N-a)<=N^2/4`, so `(4)` requires `N>=4ell`, which is exactly `(3)`
when `b=0`. Therefore every bounded-polarity cell violating `(3)` is paid by
either the joint Johnson theorem or the core-defect Johnson theorem, with
aggregate bound `(SG3)`.

Since `b<=ell-1`, condition `(3)` implies

```text
N>=4ell-b>=3ell+1.                                     (5)
```

It remains to translate `(5)` to the official source scale. If
`M<3(r-1)`, then `M<=3(r-1)-1`; using `(SG1)` and `b<ell` gives

```text
(r-1)N+r=Mell+b<3(r-1)ell.                             (6)
```

Thus `N<3ell`, contradicting `(5)`. This proves `(SG2)--(SG5)`.

Finally, direct substitution of `(SG6)` gives

```text
(r-1)k+1=6r^2-4r-1=Mell+b
```

and `N+b=(6r+1)+(2r-1)=8r=4ell`. This proves the arithmetic sharpness
claim.

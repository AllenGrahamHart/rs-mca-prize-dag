# Proof

Fix `t!=1` and abbreviate `u=u(t)`, `v=v(t)`, so `u+v=1`. Parameters `t'`
in the same coefficient block correspond bijectively to pairs `(h,k) in H^2`
such that

```text
uh+vk=1.                                          (B1)
```

Indeed, the coefficient point `(uh,vk)` determines
`t'=-(vk)/(uh)` and lies on `U+V=1`; conversely every parameter in the block
has this form uniquely.

Equation `(B1)` is

```text
h-tk=1-t.
```

After writing `h=w`, `k=z`, this is equivalent to

```text
1-w=t(1-z).
```

The pair `(h,k)=(1,1)` always solves `(B1)` but corresponds to the excluded
zero/zero ratio. Every other solution has `h!=1` and `k!=1`: if one equals
`1`, `(B1)` forces the other to equal `1`. Thus the remaining `|B|-1`
coefficient points are exactly the pairs `(c,d)=(1-z,1-w) in A^2` with
`d/c=t`. This proves `R(t)=|B|-1`, hence constancy on `B`.

Finally, summing `R(t)` over all nonidentity `t` counts every ordered
off-diagonal pair in `A^2`, so

```text
sum_B |B|(|B|-1)=sum_(t!=1)R(t)=|A|(|A|-1)=(n-1)(n-2).
```

The corrected global identity is therefore `(n-1)(n-2)`, not `(n-1)^2`.

# Proof

Absorb the signs of a reduced DLI word into its roots; since `-1 in H`, this
gives an antipodal-free set `R` of five distinct elements of `H`. Scale by a
chosen `e in R`, so the selected root is `1`. Partition the other roots as
`{x,y}` and `{z,t}` and define

```text
u=x+y, A=xy, v=z+t, B=zt.
```

The first moment says `u+v=-1`. Neither `u` nor `v` is zero, since either
equality would make the corresponding pair antipodal. For a pair with sum
`s` and product `p`, the sum of cubes is `s^3-3ps`. Hence the cubic moment is

```text
u^3-3Au + v^3-3Bv + 1.
```

Using `u+v=-1` gives

```text
u^3+v^3+1 = -3uv(u+v) = 3uv.
```

Because the characteristic is not `3`, cubic-moment vanishing is equivalent
to

```text
Au+Bv=uv,
```

and therefore to `B=u(v-A)/v`. The final roots are consequently the roots of
`T^2-vT+B`. This proves the forward direction. Reversing the calculation proves
the converse, with the stated distinctness, disjointness, and antipodal guards.

For the recurrence criterion, let `z,t` be the two roots. The standard Newton
recurrence gives

```text
D_m(v,B)=z^m+t^m
```

for every `m`. If `z,t in H`, then `B^M=1` and `D_M=2`. Conversely those two
equalities give, for `Z=z^M` and `T=t^M`,

```text
ZT=1, Z+T=2.
```

Thus `(Z-1)^2=0`, so `Z=T=1`. Since `X^M-1` is split and separable in the
official field, both quadratic roots lie in `H`. The nonzero discriminant is
exactly the distinct-root guard.

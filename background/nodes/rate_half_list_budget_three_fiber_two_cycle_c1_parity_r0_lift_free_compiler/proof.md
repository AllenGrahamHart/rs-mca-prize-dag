# Proof

For the `R0` cross ratio, direct simplification of the Mobius-router formula
gives

```text
y_R0
 =-2iota(r^4+iota r^2-1)/r^2
 =2-2iota(u-u^(-1)),       u=r^2.                   (1)
```

The Frobenius-router dependency proves `u in F_p` in both cases: this is
immediate when `r in F_p`, while `r^p=-r` gives `u^p=u`. Replacing the
square root `u` of `t` by `-u` gives the other lift trace. From `(1)`,

```text
t(y_R0-2)^2
 =-4t(u-u^(-1))^2
 =-4(t-1)^2.                                        (2)
```

This is `K_t(y_R0)=0`. Conversely, since `iota,u in F_p`, the two roots of
`K_t` are

```text
2-2iota(u-u^(-1)),       2+2iota(u-u^(-1)),          (3)
```

which are obtained from the two choices `u,-u`. Thus the root list is exact.
The discriminant is `-16t(t-1)^2`, nonzero because `t!=0,1`, so `K_t` is
separable.

For any root `y` of `K_t`, recurrence `(R0C2)` gives

```text
C_m(y)=y_m=q_out^(2^m)+q_out^(-2^m)                 (4)
```

whenever `y=q_out+q_out^(-1)`. As in the nonharmonic compiler,
`C_39(y)=2` is equivalent to both reciprocal roots lying in `mu_L`. Because
`K_t` is separable, existence of such a source root is exactly the nonconstant
gcd condition `(R0C3)`.

We next eliminate the source trace from the scalar identity. Its resultant
with `K_t` is, up to a nonzero scalar, obtained by substituting
`Y=S^2/T-2` and clearing `T^2`:

```text
T^2 K_t(S^2/T-2)
 =t(S^2-4T)^2+4(t-1)^2T^2.                          (5)
```

There is no loss when `T=0`: on a complete nonharmonic branch,
`T=q_out Z^2` with `q_out,Z` nonzero. For a direct converse, factor the
right side of `(5)` using `t=u^2`:

```text
[u(S^2-4T)+2iota(t-1)T]
[u(S^2-4T)-2iota(t-1)T].                            (6)
```

The polynomial ring `F_p[x]` is an integral domain. Hence `(R0C5)` makes one
factor in `(6)` zero, and rearrangement gives `(R0C4)` for one of the two
traces in `(3)`. This proves the scalar equivalence.

The scalar identity and trace recurrence must select the same root. For a
candidate root, every coefficient of `S^2-(Y+2)T` is a polynomial of degree
at most one in `Y`. A common root of those coefficients, `K_t`, and
`C_39-2` is therefore exactly one lift trace passing both gates. Since
`K_t` is separable, the printed positive-degree gcd criterion is equivalent
to existence and has no multiplicity ambiguity.

Finally the constant/Legendre dependency inside the nonharmonic compiler
gives

```text
S(0)=2H,       T(0)=-1/t.                            (7)
```

Evaluate `(R0C5)` at `x=0`, substitute `(7)`, and multiply by the nonzero
scalar `t^2/4`. The result is exactly

```text
4t(1+tH^2)^2+(t-1)^2=0.
```

This proves `(R0C6)` and all claims. QED.


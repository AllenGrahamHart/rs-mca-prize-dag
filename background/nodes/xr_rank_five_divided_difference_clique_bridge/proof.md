# Proof

The `r=2` instance of the proved rich-line hierarchy leaves at most

```text
C(m,4)-d_2 = 1,3,4
```

four-subsets of a retained member unreused on the three RowC rows.

Suppose instead that `[S]q=0` for a five-set `S subset A`. For each
`x in S`, put `T=S\{x}`. The Newton interpolation identity gives

```text
q(x)-I_Tq(x) = [S]q product_(t in T)(x-t) = 0.          (1)
```

If `T` were reused by another selected agreement set, the corresponding
codeword `c'` would lie on the exact collision line

```text
c'=c+lambda(q-I_Tq),       lambda!=0.
```

Both codewords agree with `U` on `T`. Equation (1), together with
`c(x)=U(x)`, would also give `c'(x)=U(x)`. Their agreement sets would then
intersect in all five coordinates of `S`, contradicting the P-A pair cap
four. Therefore all five four-subsets of `S` are unreused. This contradicts
the row-uniform upper bound `4`, and proves (DD1).

Write the selected codeword as `c=gamma q+p`, where `deg p<4`. On its
chosen agreement set `A`,

```text
U=gamma q+p.
```

Fourth divided differences annihilate `p`, so for every five-set `S subset A`

```text
[S]U=gamma[S]q.
```

The denominator is nonzero by (DD1), proving (DD3). Distinct selected
members occupy distinct quotient classes of `C_E/K_E`, so their coefficients
`gamma`, and hence their colors, are distinct.

Finally Newton interpolation on `T union {x}` gives

```text
q(x)-I_Tq(x) = [T union {x}]q product_(t in T)(x-t),
U(x)-I_TU(x) = [T union {x}]U product_(t in T)(x-t).
```

Because `c` agrees with `U` on `T`, its cubic part is
`p=I_T(U-gamma q)`. Dividing the two displayed identities therefore yields

```text
(U-c)(x)/(q-I_Tq)(x)
 = [T union {x}]U/[T union {x}]q-gamma
 = Phi(T union {x})-gamma.
```

This is (DD4). Equality at two star coordinates is exactly the determinant
zero proved in the ratio/minor dictionary, completing the bridge.

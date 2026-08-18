# Proof

Use the coprime-direction normal form

```text
(a_p,b_p)=(a_0,b_0)+R_p(U,V),       gcd(U,V)=1.
```

## Affine-line cap

Fix a nonzero scalar polynomial `T` and an affine scalar line

```text
L=S+F T.
```

Suppose the selected family has `t` points on this line, written
`R_i=S+lambda_i T` with distinct `lambda_i`. For two such types their
codeword-pair difference is

```text
(lambda_i-lambda_j)T(U,V).                         (1)
```

Bezout for the coprime pair `(U,V)` shows that outside `Z_D(T)` the two
codeword pairs are distinct. On `Z_D(T)`, every codeword pair indexed by
the affine line has the same value. Consequently every pair of complete
received-pair cores on this affine line has the same intersection

```text
J_L={x in Z_D(T): (r_0,r_1)(x)
                     =(a_0,b_0)(x)+S(x)(U,V)(x)}.    (2)
```

Thus `H_i intersection H_j=J_L` for all distinct `i,j` on the line. Since
two distinct Reed--Solomon codeword pairs agree on at most `K-1` points,

```text
j=|J_L|<=K-1=1048575.                              (3)
```

Every quotient core has size `s=m-2=1116046`. Outside `J_L` the `t` cores
are pairwise disjoint, so their union has exact size

```text
j+t(s-j).
```

It lies in the `n=2097152` coordinate domain. Since `s>K-1`, `(3)` gives

```text
t(s-(K-1))<=n-(K-1),
t<=floor(1048577/67471)=15.                         (4)
```

All 520 scalar points would lie on one affine line if their span had
dimension one, contradicting `(4)`. The prior dimension cap is four, so the
dimension is in `{2,3,4}`.

## Projective direction count

Fix one projective direction `[T]`. The selected scalar points partition
among the parallel affine lines with this direction. Each part has size at
most 15 by `(4)`. Convexity of `binom(x,2)` shows that the number of selected
unordered pairs with direction `[T]` is at most

```text
34*binom(15,2)+binom(10,2)=3615,                    (5)
```

because `520=34*15+10`. Every selected unordered pair has exactly one
projective secant direction. Hence the number of directions is at least

```text
ceil(binom(520,2)/3615)=ceil(134940/3615)=38.        (6)
```

For any represented direction choose one pair `p,q` on a corresponding
affine line. Its direction polynomial is a nonzero scalar multiple of
`R_p-R_q`. The coprime-direction normal-form theorem gives

```text
H_p intersection H_q subset Z_D(R_p-R_q),
|H_p intersection H_q|>=134940.
```

The direction therefore has at least 134940 distinct official-domain roots.
If the scalar span has dimension two, its projectivization is one polynomial
pencil containing every direction in `(6)`. QED.

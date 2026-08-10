# Proof: joint-owner ambient MDS census

The joint-owner theorem gives

```text
gcd(H,P_0)=gcd(G_H,F) gcd(B_H,L_(R_0)).               (1)
```

More explicitly, at an anchor defect root `x`,

```text
G_H(x)=-Lambda(x)H(x)/W(x),                          (2)
```

and at an anchor background root `y`,

```text
B_H(y)=Lambda(y)H(y)/F(y).                            (3)
```

Every displayed multiplier is nonzero by primitivity and the disjoint
source partition. Thus the combined failure-value vector on the roots of
`P_0` is a nonzero diagonal rescaling of the evaluation vector of `H`.
Since `deg Lambda>d`, one has `r<d<=p`. Therefore evaluation is injective,
and since `deg H<=r`, these vectors form a generalized Reed-Solomon code of
length `p` and dimension `r+1`. The anchor-coordinate theorem makes `(MC2)`
a bijection, so this code support census is also the complete monic-chart
owner census.

Fix `Q|P_0` of degree `q`. Since `P_0` is squarefree,

```text
gcd(H,P_0)=Q
```

holds exactly when

```text
H=QK,       deg K<=s=r-q,
K(z)!=0 for every root z of P_0/Q.                    (4)
```

There are `m=p-q` evaluation points in `(4)`. Inclusion-exclusion over the
hyperplanes `K(z)=0` gives `(MC3)`: for any `j<=s`, vanishing on a fixed
`j`-subset leaves `Q_f^(s+1-j)` polynomials, while all intersections of
more than `s` such hyperplanes contain only the zero polynomial. Using

```text
sum_(j=0)^m (-1)^j binom(m,j)=0
```

combines the zero-polynomial tail with the first `s+1` terms and yields

```text
sum_(j=0)^s (-1)^j binom(m,j)(Q_f^(s+1-j)-1).
```

The squarefree split polynomial `P_0` has exactly `binom(p,q)` monic
degree-`q` divisors, proving `(MC4)`. If `q=r`, then `s=0`; equation `(4)`
says `K` is any nonzero scalar, giving `(MC5)` and `(MC6)`. QED.

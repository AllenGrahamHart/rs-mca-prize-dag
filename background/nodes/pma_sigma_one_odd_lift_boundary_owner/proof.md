# Proof

Because the domain has even order, the characteristic is odd.  Every source
word has a unique parity decomposition on the quotient domain:

```text
U(x)=U_0(x^2)+xU_1(x^2),

U_0(x^2)=(U(x)+U(-x))/2,
U_1(x^2)=(U(x)-U(-x))/(2x).
```

If `U(x)=(x-a)V(x^2)`, then `U_1=V` and `U_0=-aV`.  Since `U` is nonzero,
`V` is nonzero at some quotient point, and `a=-U_0/V` there.  Thus a source
word admits at most one such split point.  This is why the owner pays no
factor `n` for choosing `a`.

Now let `P(x)=(x-a)G(x^2)` be in the owner.  Away from the split fiber
`{a,-a}`, agreement of `P` and `U` is constant on each fiber of `pi`.  At
`a` the common linear factor forces agreement, while the owner condition
excludes agreement at `-a`.  Hence the exact agreement support is

```text
{a} union pi^(-1)(A)
```

for a subset `A` of the `N-1` quotient points other than `a^2`.  Exact support
size `k+1` gives `|A|=k/2`, and exact size `k+3` gives `|A|=k/2+1`.
Agreement supports have size greater than `k-1`, so interpolation uniqueness
makes the map from codewords to these supports injective.  Therefore

```text
#QOWN_odd2(U)
 <= binom(N-1,k/2)+binom(N-1,k/2+1)
  = binom(N,k/2+1)
```

by Pascal's identity.

Put `h=k/2+1`.  The ratio to the first scale-two column is exact:

```text
binom(N,h)/binom(N-1,h)=N/(N-h).
```

At every official rate, `h<=N/2+1`; since `N>=4096`,

```text
N/(N-h) <= N/(N/2-1) < 3.
```

This proves `(ODD2)`.  The preceding two global owners have combined count at
most `8(1+2^-690)Q_2(k+2)`.  Canonical first-match selection makes the new
owner disjoint from them, and

```text
8(1+2^-690)Q_2+3Q_2
 <11(1+2^-690)Q_2
 <719(1+2^-690)Q_2,
```

which proves `(ODD2-COMB)`.

Catch #171 supplies exactly this source shape: its received word is
`(x-a)V(x^2)` and its two displayed odd-lift strata have agreement sizes
`k+1` and `k+3`.  The factorization and support description are proved in
`petal_g1_layer_maps/notes/cp_packet_20260713/cp_proof.md`, sections 4-5.
Consequently those two complete strata enter this owner before any of the
many layout charts used in that packet are selected.

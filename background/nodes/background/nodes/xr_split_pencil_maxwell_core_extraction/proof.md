# Proof

Choose `G` inclusion-minimal among subfamilies satisfying

```text
c|G| >= 2|union G|-8.
```

Such a family exists by (MC1), since every union has size at most `N`.
Define `L,v,e` as in the statement. The defining inequality gives `e>=0`.
Minimality gives, for every proper `J subset G`,

```text
c|J| < 2|union J|-8,
```

which is the integer inequality in (MC2).

Fix a block `A` and let `u_A` be its number of coordinates absent from all
other blocks of `G`. Applying the proper-subfamily inequality to `G\{A}`
gives

```text
c(L-1) <= 2(v-u_A)-9.
```

Substitute `cL=2v-8+e` and cancel `2v` to obtain

```text
e+2u_A <= c-1.
```

This proves (MC3), and in particular `e<=c-1`. Since `v<=N`,

```text
cL=2v-8+e <= 2N+c-9,
```

which proves the size bound in (MC2).

Restrict the rank-certificate matrix to the union `V`. Cubic evaluation on
`V` has dimension four. The genuine pair `(U,q)` gives a ninth kernel
direction beyond the cubic-pair kernel; equivalently, `q|V` is noncubic.
This also follows from any block of `G`, because all its fifth divided
differences of `q` are nonzero. Hence

```text
rank M_G <= 2v-9.
```

The matrix has exactly `cL=2v-8+e` rows, because each `H_i` has full row
rank `c`. Rank-nullity on the transpose now gives

```text
dim leftker(M_G)
 >= (2v-8+e)-(2v-9)=e+1.
```

If the only right kernel were the eight-dimensional cubic-pair space, row
overdetermination would force only `e` left-kernel dimensions. The remaining
one is the asserted anomalous dependence. Substituting the six official
`(N,m)` pairs gives the printed circuit and private-coordinate caps.

# Proof

Let `x_j`, `p_j`, and `q_j` be the source labels, target products, and
signed target sums of the five common roles. The primitive product-row
cofactor vector has six coordinates

```text
kappa = (A_0,A_1,A_2,B_0,B_1,B_2).
```

For the `AB` pivot put `x=x_AB=r^2`, `s=x(1-x)`, and

```text
gamma = q_AB (A_0 + A_1 x + A_2 x^2).
```

Then

```text
(s A_0,s A_1,s A_2,s B_0,s B_1,s B_2,-gamma,gamma)       (KBP1B11-K)
```

annihilates every product row. It also annihilates the `LA` sum row because
`q_LA=0` and `x_LA=1`, and it annihilates the `AB` row by the definition
of `gamma`. Exact gcd removal and scalar normalization remove the common
factor `r^4-r^2` and produce the primitive kernel in the statement.

The compiler performs this construction independently in all four source
sign rows. The resulting eight coordinate digests are identical. It then
loads the chart-independent lex basis certified by the parent common-locus
node, saturates by every route guard, and reduces all ten row pairings. The
ten remainders are zero in each sign row; the guarded ideal remains
dimension one. Thus the three nonformal identities hold everywhere on each
guarded common component. QED.

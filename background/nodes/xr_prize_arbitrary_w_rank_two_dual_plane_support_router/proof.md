# Proof

Extend each trade row by zero to

```text
X=union_i supp(lambda_i).
```

Because `lambda_i` is a parity row of `W` on its selected block and is zero
outside its support, it annihilates `W|X`. Two independent rows span the
trade row space, so `(DP1)` follows.

Choose a basis `F,G` of that plane. Write

```text
lambda_i=c_iF+d_iG.
```

No point of `X` is a common zero of `F,G`: such a point would be zero in
every trade row and would not lie in their support union. Therefore the map
`phi=[F:G]` is defined everywhere on `X`, and the zero/support identities in
`(DP2)` are immediate.

If `beta_i` and `beta_j` are distinct, the two equations

```text
c_iF(x)+d_iG(x)=c_jF(x)+d_jG(x)=0
```

force `F(x)=G(x)=0`. Thus `Z_i` and `Z_j` are disjoint. The four-block Segre
router gives a nonconstant Mobius map from distinct slopes to row classes, so
all four directions are distinct.

In a five-block circuit, three equal coefficient directions would put the
corresponding three Segre points on one ruling line. Those three columns would
be dependent, contradicting the fact that every four columns are independent.
Hence every direction has multiplicity at most two.

Suppose `beta_i=beta_j`. The two rows are nonzero scalar multiples and have
the same support `S`, which lies in both selected blocks. Restrict the two
selected-zero equations to `S` and pass to `F^S/(W|S)`:

```text
[b]+gamma_i[q]=0,       [b]+gamma_j[q]=0.
```

The slopes are distinct, so subtraction proves `(DP3)`. If `S` spans `W`,
its first basis is shared by both blocks and the persistent moving-zero proof
gives `floor((R-v)/h)`. If it does not span, its closure is a proper flat of
size at most its rank plus `u`. This is exactly the prior owner dichotomy; its
proof used only two distinct slopes for the local cancellation and basis cap.

For `(DP4)`, fix a row support `S_i`. Lagrange interpolation gives one unique
polynomial `Q_i` of degree below `s_i` with

```text
Q_i(x)=lambda_i(x)Lambda'_(S_i)(x)       (x in S_i).
```

Exact support makes every displayed value nonzero. The row annihilates `W`,
which is precisely the second identity in `(DP4)`. Conversely that identity
says that the locator vector is in `(W|S_i)^perp`.

Finally, start from a plane `L subset (W|X)^perp`, coefficient rows satisfying
the certified Segre dependence, and blocks containing the resulting supports.
Every row is a valid `W` parity word. The two coefficient sums and two slope-
weighted coefficient sums vanish, so the rows satisfy both trade equations.
This proves the converse and exactness of the dual-plane representation. QED.

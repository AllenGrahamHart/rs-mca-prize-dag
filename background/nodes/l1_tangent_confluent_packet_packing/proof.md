# Proof - L1 tangent confluent-packet packing

Fix `j` in the stated range.  A confluent packet carried by `P` consists of

```text
E subset Z(D_P),        |E|=j,
V subset S_P\E,         |V|=k-2j.                    (1)
```

At every point of `E`, impose both the value and first Hasse-derivative
conditions of `P`; at every point of `V`, impose only the value condition.
The packet contains exactly

```text
2j+(k-2j)=k
```

independent Hermite conditions.  A member with tangent degree `r_P` carries

```text
binom(r_P,j) binom(a-j,k-2j)                          (2)
```

such packets.

No packet is carried by two distinct codewords.  Indeed, if `P_1,P_2` carry
the same `(E,V)`, then `P_1-P_2` has a double zero at every point of `E` and
a simple zero at every point of `V`.  It therefore has at least `k` roots
counted with multiplicity.  But `deg(P_1-P_2)<k`, so it is zero and the two
codewords are equal.

There are exactly

```text
binom(n,j) binom(n-j,k-2j)                            (3)
```

possible packets on `H`: first choose `E`, then choose `V` outside it.
Counting incidences between exact shell codewords and packets proves `(HP2)`.
For every `r_P>=r0`, monotonicity gives
`binom(r_P,j)>=binom(r0,j)`; division and integer flooring prove `(HP3)`.
Taking `j=1` in `(HP2)` gives `(HP4)`, and each tangent member has `r_P>=1`,
which proves `(HP5)`.  The `j=0` specialization is the usual uniqueness of a
degree-below-`k` polynomial from its values on `k` points.

For the mixed packing, put `C_P=H\S_P`, so `|C_P|=omega`.  For two distinct
codewords, their difference has simple zeros on `S_1 intersect S_2` and an
additional zero multiplicity on `D_1 intersect D_2`.  Hence

```text
|S_1 intersect S_2|+|D_1 intersect D_2|<=k-1.         (4)
```

Since

```text
|S_1 intersect S_2|=n-2omega+|C_1 intersect C_2|,
```

equation `(4)` is equivalent to

```text
|C_1 intersect C_2|+|D_1 intersect D_2|<=s-1.         (5)
```

Choose `j` tangent roots and `s-j` complement roots from one codeword.  If
two distinct codewords carried the same role-labelled packet, the left side
of `(5)` would be at least `s`, a contradiction.  One member contributes
`binom(r_P,j)binom(omega,s-j)` packets and the full domain contains
`binom(n,j)binom(n-j,s-j)` role-labelled packets.  Incidence counting proves
`(HP7)`; monotonicity in `r_P` and flooring prove `(HP8)`.

Using

```text
binom(n,j)binom(n-j,s-j)=binom(n,s)binom(s,j),
```

the ratio of consecutive unfloored bounds in `(HP8)` simplifies to

```text
(s-j)/(r0-j) * binom(omega,s-j)/binom(omega,s-j-1)
=(omega-s+j+1)/(r0-j)
=(w+j+1)/(r0-j).
```

It is increasing in `j`, so the sequence is unimodal.  It decreases exactly
while `2j<r0-w-1`, proving `(HP9)`, `(HP10)`, and the threshold `r0>w+1`.

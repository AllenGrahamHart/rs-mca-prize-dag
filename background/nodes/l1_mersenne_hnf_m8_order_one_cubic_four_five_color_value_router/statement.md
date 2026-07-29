# L1 Mersenne HNF m=8 order-one cubic four/five-color value router

- **status:** PROVED
- **dependencies:** `l1_mersenne_hnf_order_one_color_degree_barrier`,
  `l1_mersenne_hnf_m8_order_one_conic_reduction`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** h=7 cubic colored interpolants using exactly four or five colors

Let

```text
V_E(X)=Res_W(L_(r,d)(W),X-E(W)).                     (FFV1)
```

For a packet with used-color multiplicities `(n_epsilon)`, define

```text
M(X)=product_(epsilon missing)(X-epsilon),
D(X)=product_(epsilon used)(X-epsilon)^(n_epsilon-1). (FFV2)
```

Every packet in scope satisfies the exact monic polynomial identity

```text
V_E(X)M(X)=(X^8-1)D(X).                             (FFV3)
```

The three possible profiles and cyclic-orbit packet counts are

| profile | `deg M` | `D` | cyclic packets |
|---|---:|---|---:|
| `2+1+1+1+1` | 3 | one repeated-color linear factor | 35 |
| `3+1+1+1` | 4 | square of the triple-color linear factor | 35 |
| `2+2+1+1` | 4 | product of the two repeated-color factors | 54 |

Thus all four/five-color cubic packets reduce to 124 fixed p-free value
systems before row and norm-color sharding. Each system also carries the
h=7 conic. Saturate by the HNF factors, `lc(E)`, `disc(L)`, squarefreeness
of `M`, disjointness of `M` and `D`, and exact fiber-gcd subresultants.

A unit saturation of all 124 packets closes the four/five-color cubic
chamber. No unit verdict, another cubic profile, higher degree, cyclotomic
converse, inner lift, or L1 close is asserted.

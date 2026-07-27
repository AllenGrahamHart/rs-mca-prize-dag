# Budget-three common-mismatch zero theorem

- **status:** PROVED
- **closure:** proof
- **dependency:** `rate_half_list_budget_three_intersection_reduction`
- **consumers:** `rate_half_list_chamber_affine_rank_bridge`,
  `rate_half_list_adjacent_crossing`

Let `C=RS[F,D,2d]` have length `n=4d`. Suppose four distinct codewords
`c_0,...,c_3` agree with one received word `u` on at least `3d-1`
coordinates. Choose `3d-1` agreement coordinates `S_i` for each codeword, as
in the proved budget-three intersection reduction. Let

```text
C'=span{c_1-c_0,c_2-c_0,c_3-c_0},
G={x in D : v(x)=0 for every v in C'},
z=|G|,
g=#{x in G : c_0(x)=u(x)},
b=z-g.
```

Then

```text
g=z,       b=0.
```

The conclusion holds in all six incidence types and all thirteen edge-degree
chambers. It does not determine the generalized Hamming weights of `C'`,
exclude a chamber, or improve the adjacent list threshold by itself.

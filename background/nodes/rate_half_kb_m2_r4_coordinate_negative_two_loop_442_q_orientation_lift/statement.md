# KoalaBear m2 r4 coordinate negative two-loop 442 q-orientation lift

- **status:** PROVED
- **scope:** every injective geometric root of the six common-`K` product
  rows `(KB4P-3)--(KB4P-5)`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_product_q_weld` and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_exceptional_product_classifier`
- **consumer:** `rate_half_band_closure`

For each of the three cross-edge deck orbits `AB,AC,BC`, there are two ways
to assign its two deck-conjugate edges to the two source lifts.  Among the
eight orientation triples, exactly two satisfy both common-`K` q welds.

More explicitly, orient `AB,AC` by their shared `A` endpoint.  The first
label identity `(KB44-1)` gives

```text
[x_AB(k_AC-k_B)/(x_AC(k_AB-k_B))]^2=1.            (KB4Q-1)
```

Orient `AB,BC` by their shared `B` endpoint.  The second identity gives

```text
[x_AB^(B)(k_BC-k_A)/(x_BC(k_AB-k_A))]^2=1.        (KB4Q-2)
```

Here each `x_E^2=k_E`; `x_AB^(B)` equals `+x_AB^(A)` or `-x_AB^(A)`
according to the `AB` product sign.  Flipping the `AC` orbit changes only
the sign in `(KB4Q-1)`, while flipping `BC` changes only the sign in
`(KB4Q-2)`.  Once the `AB` orientation is chosen, the other two are uniquely
forced.  Hence there are exactly two solutions.

For either solution, the two weld equalities connect all three nonloop rows.
The product-to-q theorem therefore reconstructs one nonzero scalar `c_1`
such that

```text
A_1(W)=c_1(W-k_A)(W-k_B),
A_1(s)+q_s B_2(s)=0       for every s in K.        (KB4Q-3)
```

Thus no injective root of the six product rows is deleted by common-`K` q
orientation alone.  Source-facet compatibility of the chosen orientations,
the `eta` and six `L^c` fibers (the other seven), paired-product involution, deployed-field
descent, and all global conclusions remain open.

## Falsifier

An injective root of `(KB4P-3)--(KB4P-5)` for which no orientation triple
satisfies both welds, or for which a satisfying triple fails `(KB4Q-3)`.

# KoalaBear m2 r4 coordinate negative one-loop 442 aligned outside-product router

- **status:** PROVED
- **scope:** the two aligned common-`K` families and every complete outside
  skeleton in the negative one-loop `(4,4,2)` packet
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_aligned_pair_classifier`,
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_complete_edge_skeleton_classifier`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate`
- **consumer:** `rate_half_band_closure`

The common products in either aligned family are

```text
(-b^2,b,-b,c,-c),             b^2!=c^2.           (KB41R-1)
```

The two complete antipodal pairs force the product involution to be
negation.  Consequently the complementary record opposite the common
singleton has product `b^2`, and the other six outside products must form
three negation pairs.

For signed representatives `D=d,E=e,F=f` and signs
`alpha,beta,gamma,delta in {+1,-1}`, this requirement routes the three
outside skeletons exactly as follows.

* `S0` is empty.  Its outside products are
  `alpha*c*e,beta*c*f,+/-d*e,+/-d*f,gamma*e*f`; no singleton can be the
  forced `b^2` while the other two singletons negate each other.
* In `S1`, with products

  ```text
  alpha*c*e, beta*c*f, -d^2, gamma*d*e, delta*d*f, +/-e*f,
  ```

  the forced product can only be one of the two singleton internal edges.
  The two exact branches are

  ```text
  S1-DE: gamma*d*e=b^2, alpha*c*e+delta*d*f=0,
         beta*c*f-d^2=0;
  S1-DF: delta*d*f=b^2, alpha*c*e-d^2=0,
         beta*c*f+gamma*d*e=0.                    (KB41R-2)
  ```

  Either branch implies

  ```text
  d^4=-alpha*beta*gamma*delta*b^2*c^2.            (KB41R-3)
  ```

* In `S2`, whose products are
  `+/-c*d,-e^2,+/-d*f,+/-e*f`, the forced product must be the loop:

  ```text
  -e^2=b^2.                                       (KB41R-4)
  ```

Subject to the existing distinctness guards, `(KB41R-2)` and `(KB41R-4)`
are also sufficient for the outside product multiset to complete the six
negation pairs.  Thus `S0` is deleted, while `S1` and `S2` are genuine
product-level survivors.

This theorem does not impose the outside q equations, choose the full source
placement, prove complete interpolation, classify a nonloop-singleton
common matching orbit, handle one-loop 433 or zero-loop, close the coordinate
orientation, close a row, or prove either Prize result.

## Falsifier

An admissible `S0` product completion, an `S1` completion outside the two
branches in `(KB41R-2)`, an `S2` completion without `(KB41R-4)`, or a
guarded failure of the converse pairing.

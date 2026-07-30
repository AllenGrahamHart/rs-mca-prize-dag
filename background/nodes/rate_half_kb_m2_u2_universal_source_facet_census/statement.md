# KoalaBear m2 u2 universal source-facet census

- **status:** PROVED
- **scope:** every actual `(m,r,delta)=(2,4,2)` component, independent of
  its order-two stabilizer orientation, and every actual `(8,1)`
  trivial-stabilizer component
- **dependencies:** `rate_half_kb_q6_s6_common_five_outgoing_fiber_pin`
  and `rate_half_kb_m2_r4_source_row_interpolation_compiler`
- **consumer:** `rate_half_band_closure`

Let `I,L` be the invariant-coordinate and invariant-fiber six-sets,
`J=I^c`, `K subset I intersect L` the common five-set, and
`eta=L minus K`. Every actual degree-two source component has, among its 24
complete-source stars counted with divisor multiplicity, the exact census

```text
J-J: 10,       I-I: 10,       I-J: 4.              (KBUS-1)
```

Let `d_j` be the number of incidences of `j in J` among the ten `J-J`
stars over the five complete `K` fibers. Then

```text
0<=d_j<=4,       sum_(j in J)d_j=20,                (KBUS-2)
```

and, up to permutation of `J`, the exhaustive degree profiles are

```text
(0,4,4,4,4,4),
(1,3,4,4,4,4),
(2,2,4,4,4,4),
(2,3,3,4,4,4),
(3,3,3,3,4,4).                                    (KBUS-3)
```

In particular at most one `J` label is absent from the `K` fibers. The
coordinate-order-two involution narrows `(KBUS-3)` to the two profiles
already proved there; no such narrowing is asserted for the diagonal or
trivial-stabilizer type.

This theorem does not construct or delete a source packet, stabilizer
orientation, order-two type, trivial type, owner, payment, row, or Prize
result.

## Falsifier

An actual degree-two source component with a category count outside
`(KBUS-1)`, a `K`-fiber degree profile outside `(KBUS-3)`, or a use of the
coordinate pair symmetry in the diagonal or trivial-stabilizer branch.

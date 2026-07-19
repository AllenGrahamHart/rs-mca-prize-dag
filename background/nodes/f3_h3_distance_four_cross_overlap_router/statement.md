# H3 distance-four cross-overlap router

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`
- **dependencies:** `f3_h3_rich_fiber_norm_cutoff`,
  `f3_h3_distance_two_collision_2primary_exclusion`

Take two distinct unordered shifted-root pairs `E,F` from the seven-vector
selection in one odd-characteristic rich product fiber. Thus neither pair is
diagonal or contains `-1`, and both coefficient vectors have squared norm one
or three. If

```text
||v_E-v_F||_2^2=4,                                  (D4R1)
```

then exactly one of the following lanes applies:

1. **antipodal lane:** after relabeling, `E={x,-x}` and `F={u,v}` with

   ```text
   x^2=u+v-uv;                                      (D4A)
   ```

   exactly one endpoint is antipodal, and its coefficient vector has squared
   norm one;
2. **cross-overlap lane:** both vectors have squared norm three, and a product
   monomial of one pair equals the negative of one root monomial of the other.

After exchanging the two pairs and their internal roots, the cross-overlap
lane has the canonical finite-field form

```text
E={x,y},       F={u,v},       uv=-y,
u x (1-y)=u^2-y,                                    (D4R2)
```

where `x,y,u,v` belong to the order-`n` subgroup and none is `1`. In
particular,

```text
x=(u^2-y)/(u(1-y)).                                 (D4R3)
```

Thus both distance-four lanes are two-free-variable subgroup incidences, not
four-exponent norm families. In `(D4A)`, the right side must lie in the square
subgroup and then determines the unordered antipodal pair. This theorem does
not exclude either lane and makes no distance-six claim.

Let `N_4` be the number of unordered edges `{E,F}` over all product targets in
one row that satisfy the selection conditions and `(D4R1)`. Then

```text
N_4 <= n^2+n(n+1)/2=(3n^2+n)/2.                    (D4R4)
```

Consequently the number of rich targets having no distance-six edge among all
their eligible squared-norm-at-most-three representations is at most

```text
floor((3n^2+n)/12).                                 (D4R5)
```

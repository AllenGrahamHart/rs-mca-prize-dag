# KoalaBear m2 r4 coordinate negative two-loop 442 signed-pair matching-template exclusion

- **status:** PROVED
- **scope:** the 24 invariant-product cells with forced `xi` type `cD` or
  `sigma DE` in `(KB44R-2)`, over the deployed KoalaBear field
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_outside_product_involution_compiler`
  and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_product_invariance_router`
- **consumer:** `rate_half_band_closure`

After removing the forced value, either cell has the residual product form

```text
{a,q,+x,-x,+y,-y},                               (KB44T-1)
```

with six distinct nonzero entries.  In every actual completion, `a` and
`q` lie in different product-involution orbits.

Indeed, if `a` were paired with `q`, the four signed values would have one
of only three matchings:

```text
(x,-x),(y,-y);
(x,y),(-x,-y);
(x,-y),(-x,y).                                   (KB44T-2)
```

The first forces the product involution to be negation.  This contradicts
the common pair `(-1,c)` on `H6`, `(b,c)` on `H8-L`, or `(c,-1)` on
`H8-M`, using `(KB4P-2)`.  Either cross matching forces the middle
involution coefficient `Alpha` in `(KB44O-3)` to vanish.

After removing only protected nonzero factors, the six `Alpha` factors and
their exact iterated resultant norms are

```text
row       protected Alpha factor             norm
H6,-      (b+1)(b^2-b+1)                     30625
H6,+      (b-1)(b^2+b+1)                     18225
H8-L,-    (b-1)(b+1)                         49
H8-L,+    b^2+1                              2401
H8-M,-    (b-1)(b+1)                         49
H8-M,+    b^2+1                              2401.              (KB44T-3)
```

All are nonzero in characteristic `2130706433`.  Thus all three templates
`(KB44T-2)` are impossible.  This deletes exactly

```text
6 common rows x 2 sigma x 2 xi types x 3 templates = 72
```

of the 540 sign-and-location-gauged perfect-matching subcases, leaving at
most 468.  Equivalently, the 24 affected invariant sextics may be saturated
by the condition that `a,q` are not one involution pair.

This theorem does not delete an entire invariant cell, treat forced type
`DF`, impose full interpolation or the remaining q/colored-resultant rows,
close the coordinate orientation, move an owner/payment, close a row, or
prove either Prize result.

## Falsifier

A guarded deployed-field completion in which the two unsigned residual
values pair together, or a root of one of the six exact common-row ideals
on which its protected `Alpha` factor vanishes.

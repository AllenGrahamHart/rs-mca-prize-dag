# Repeated-BC cell-11 common-kernel reconstruction

- **status:** PROVED
- **field:** `F_2130706433`
- **scope:** all eight cell-11 symmetric function-field towers

Let the five common labels, products, and endpoint sums be
`lambda_i`, `p_i`, and `s_i`.  On the selected-cofactor open, the five product
rows

```text
(-p_i, -p_i lambda_i, -p_i lambda_i^2, 1, lambda_i, lambda_i^2)
```

have the exact cofactor kernel `(A_0,A_1,A_2,B_0,B_1,B_2)`.  Thus, with
`A(z)=sum A_j z^j` and `B(z)=sum B_j z^j`, all five identities
`B(lambda_i)=p_i A(lambda_i)` hold.

There is a linear polynomial `beta(z)` for which all five sum identities

```text
(root_i s_i) A(lambda_i) + lambda_i beta(lambda_i) = 0
```

hold.  At the missing common label `lambda`, wherever `A(lambda)` is
invertible, the missing coordinates are therefore

```text
product = B(lambda)/A(lambda),
sum^2  = lambda beta(lambda)^2/A(lambda)^2.
```

The native quotient-algebra audit replays all seven tower/lift identities,
all five product identities, and all five sum identities in every sign row.
It records the exact rational guards needed by the inversions.

This reconstructs necessary outside input only.  It does not prove that an
outside endpoint exists, exclude a residual matching, pay a label, or handle
the finite guard boundary.

## Falsifier

A tower/lift residual, a nonzero product- or sum-kernel residual, a zero
cofactor tuple on the selected open, or disagreement between the reconstructed
and directly constrained missing coordinates.

# b2_modp_giant_extras conditional proof

## Predicate nodes

- `b2b_dyadic_descent_packet`
- `b2b_near_tail_bound`
- `b2b_primitive_core`

## Claim

Conditional on the primitive-core estimate, the number of non-coset-union
`t`-null blocks at official prize-max rows is at most `n^3 = 2^123`.

## Proof

The proved `b2b_dyadic_descent_packet` supplies the structural reductions:
complement duality, iterated dyadic descent with multiplicity bookkeeping,
per-fiber lift counts, exact retention of the odd skew equations, coset fixed
points, and the repaired boundary scale `M_0`.

The proved `b2b_near_tail_bound` removes the near-tail layers. At official
parameters, the two near-tail sides together contribute less than `2^122`,
which is half of the available `n^3 = 2^123` budget.

After the boundary class and the near tails are stripped, the remaining
unpaid contribution is exactly the primitive core

```text
#{t-null primitive B : t+16 <= |B| <= n/2}.
```

The predicate `b2b_primitive_core` bounds this core by `2^122`. Therefore the
near-tail contribution plus the primitive-core contribution is less than

```text
2^122 + 2^122 = 2^123 = n^3.
```

Thus the B2 mod-p giant-extras bound follows conditionally on the primitive
core. The unresolved frontier is now isolated in `b2b_primitive_core`.

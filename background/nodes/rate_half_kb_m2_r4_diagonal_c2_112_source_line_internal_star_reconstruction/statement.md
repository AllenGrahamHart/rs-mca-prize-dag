# KoalaBear m2 r4 diagonal c2 (1,1,2) source-line internal-star reconstruction

- **status:** PROVED
- **scope:** every saturated source-line `(1,1,2)` packet
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_ramified_complete_source_repair` and
  `rate_half_kb_m2_r4_diagonal_c2_112_saturated_defect_classifier`
- **consumer:** `rate_half_band_closure`

Fix a sign `epsilon`, orient the forced square orbit by `w`, and put
`q=P_(J_1)`. Let `S_epsilon(w,q)` be the reciprocal `U` space satisfying

```text
U(T,w) in <q>.
```

It has dimension three for `epsilon=+1` and two for `epsilon=-1`. If
`{z,z^(-1)}` is the internal common-`K` orbit, evaluation gives an injective
map

```text
ev_z:S_epsilon(w,q) -> Sym^2(T),                  (KBSR-1)
```

which is an isomorphism in the positive sign and has a two-dimensional
image in the negative sign.

Let `e,f` be the two distinct pure edge quadratics over one source fiber
above `z`, ordered compatibly with a lift `x`, `x^2=z`. The pinned nonzero
odd part determines unique nonzero scalars `lambda,mu`, up to their common
normalization, such that

```text
2x V(T,z)=lambda e(T)-mu f(T).                    (KBSR-2)
```

Define

```text
P_(e,f)(T)=(lambda e(T)+mu f(T))/2.               (KBSR-3)
```

Then an actual packet must satisfy

```text
ev_z(U)=P_(e,f).                                   (KBSR-4)
```

For `epsilon=+1`, `(KBSR-4)` has exactly one solution `U`. For
`epsilon=-1`, it has either no solution or exactly one, decided by one
linear image-plane equation. Thus every fixed internal edge assignment and
sign produces at most one projective source form `H=U+XV`, modulo exchange
with its source-deck conjugate.

Each of the five labeled pure multisets has at most four compatible
internal edge pairs. Therefore every classified source-line packet produces
at most eight projective source-deck pairs before the colored quotient and
remaining source rows are checked. No continuous coefficient family remains.

This theorem does not assert that a reconstructed candidate passes the
colored quotient, full interpolation, irreducibility, endpoint norm, or
outer equation. It deletes no packet, row, owner, payment, or Prize result.

## Falsifier

A saturated source-line packet for which `(KBSR-1)` has a kernel, a fixed
edge assignment admits two different source forms of one sign, or a pure
multiset has more than four compatible internal edge pairs.

# Denominator-root cancellation dichotomy

- **status:** PROVED
- **scope:** the post-cancellation source gap in a coherent exact-locator
  rational atom

Use the notation of the pole-tolerant harvest. Let `t=|P|` and, for every
remaining nonzero-scalar index, let

```text
D'   = D \ P,
S_i' = S_i \ P.
```

The indices split canonically and disjointly into:

- `N`: no degree-`<k` pair simultaneously explains `r0,r1` on `S_i'`;
- `T`: some degree-`<k` pair `(p0_i,p1_i)` does so.

The source degree profile gives `t<=m-k`, hence `m-t >= k`.

Indices in `N` remain support-wise MCA witnesses in the reduced root-free
certificate, with the original received-line and slope owner retained.

For every `i in T`,

```text
h_i = p0_i + gamma_i p1_i                         globally,
u_i + gamma_i v_i = 0                             on P,
u_i = r0-p0_i,  v_i = r1-p1_i,  v_i|_P != 0.
```

Thus `gamma_i` is recovered from any pole coordinate at which `v_i` is
nonzero. Distinct slopes cannot use the same ordered pair `(p0_i,p1_i)`.

This is an exact same-owner source decomposition. It does not bound `|T|`
or route these records into a paid `(S)` or `(A)` class.

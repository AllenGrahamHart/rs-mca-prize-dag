# Sub-square-root interleaving collapse

- **status:** PROVED
- **consumer:** `list_large_m_scope_closure`
- **object:** common-support interleaved lists of a finite-field linear code

## Statement

Let `C <= F^n` be an `F`-linear code, let `q=|F|`, and fix an agreement
threshold `a`. Write

```text
L = max_u |{c in C : agr(c,u) >= a}|
```

and let `L_m` be the corresponding worst received-word list size for the
`m`-fold common-support interleaving `C^{==m}`. If `1 <= L < q`, then for every
`m >= 1`,

```text
L <= L_m <= floor(L(q-1)/(q-L)).
```

In particular, if `L^2 < q`, then

```text
L_m = L
```

for every `m >= 1`.

The theorem is pointwise in the agreement threshold. It uses only linearity
over `F`; it is not specific to Reed-Solomon codes.

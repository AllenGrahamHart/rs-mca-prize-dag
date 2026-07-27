# Averaged locator-to-slope conversion

- **status:** PROVED
- **closure:** exact occupancy inequality

Let `A` be a deterministic family of exact `(k+t)`-supports. For a random
independent pair of words, let `X_z(A)` be the number of supports contributing
the finite slope `z`, let

```text
N(A)=sum_z X_z(A),
Y(A)=#{z:X_z(A)>0},
```

and let `C_t(A)` be the exact fixed-slope ordered second factorial moment
proved by `averaged_xr`. Then

```text
E[Y(A)] >= E[N(A)]-(q/2)C_t(A).
```

Consequently, for every integer `B>=1`, if

```text
nu(A)=E[N(A)]-(q/2)C_t(A) > B-1,
```

some received pair has at least `B` distinct finite bad slopes witnessed by
`A`. Prize use takes `B=B*+1`, so the strict certificate is `nu(A)>B*`.

This theorem is valid for every deterministic family. A prize-level unpaid
payload must separately supply post-paid ownership, its exact strict-overlap
profile, and the ambient-field interpretation.

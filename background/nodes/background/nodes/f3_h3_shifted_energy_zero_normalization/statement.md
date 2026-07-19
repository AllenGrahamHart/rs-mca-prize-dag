# Shifted-energy zero normalization

- **status:** see `dag.json` (single source of truth)
- **consumer:** `f3_h3_three_to_one_c36`
- **dependency:** `f3_h3_identity_deficit_energy_close`

Let `H<=F_p^*` have official order `n`, put

```text
S=H-1,       A=S\{0},
```

and let `E_x` denote multiplicative energy. Then

```text
E_x(S)=E_x(A)+(2n-1)^2.                         (ZN1)
```

Consequently the full-shift estimate

```text
E_x(H-1) <= (145/4)(n-1)^2+(2n-1)^2            (ZN2)
```

implies C36' on every official order. Equivalently, the right side of `(ZN2)`
is

```text
(161/4)n^2-(153/2)n+149/4.                     (ZN3)
```

If a source is stated in the centered form

```text
E_x(H-1)-n^4/p <= Err(n,p),
```

it is enough to prove

```text
Err(n,p)
 <= (145/4)(n-1)^2+(2n-1)^2-n^4/p.             (ZN4)
```

Since every official prime satisfies `p>n^2`, the right side of `(ZN4)` is
strictly greater than

```text
(157/4)n^2-(153/2)n+149/4 > 39.24 n^2.         (ZN5)
```

This corrects the former audit that applied the published full-shift estimate
directly to the zero-deleted set. It does not prove `(ZN2)` or promote C36'.

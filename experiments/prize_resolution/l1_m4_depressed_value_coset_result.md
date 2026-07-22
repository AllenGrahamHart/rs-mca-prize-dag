# M4 depressed-value coset certificate

- **status:** COMPLETE exact finite certificate
- **script:** `l1_m4_depressed_value_coset_check.py`
- **scope:** the 16 quarter-class pairs for each of the four official
  `n=4(p+1)` characteristics
- **resources:** local RAMguard, below one second, negligible memory

## Exact output

```text
p=8191 survivors=0
p=131071 survivors=0
p=524287 survivors=3
  epsilon=1  eta=-1  ALL_QUADRATIC_ROOTS
  epsilon=-1 eta=1   ALL_QUADRATIC_ROOTS
  epsilon=-1 eta=-1  ALL_QUADRATIC_ROOTS
p=2147483647 survivors=3
  epsilon=1  eta=-1  ALL_QUADRATIC_ROOTS
  epsilon=-1 eta=1   ALL_QUADRATIC_ROOTS
  epsilon=-1 eta=-1  ALL_QUADRATIC_ROOTS
```

Each `ALL_QUADRATIC_ROOTS` entry contributes two ordered roots. The six
ordered pairs are the six permutations of one projective triple. It may be
normalized to the roots of

```text
Y^3-2Y+1=(Y-1)(Y^2+Y-1),
```

whose discriminant is nonzero because the official characteristics are not
five. Thus the corresponding depressed outer cubic satisfies
`a^3+8b^2=0`.

The certificate uses exact arithmetic in `F_(p^2)[u]/(q)` and binary
exponentiation by `p+1`; it is not a heuristic search. Its exclusion applies
to positive inner valuation, where the depressed split values equal the
products of their domain roots. It does not apply directly to `nu=0`.

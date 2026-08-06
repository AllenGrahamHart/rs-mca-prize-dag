# F2 admissible extension-degree and order classification

- **status:** PROVED
- **closure:** proof

Put `k=ord_(2^41)(p)`. Every official maximal rate-half row lies in exactly
one of the following signed types:

```text
branch       valuation             k       possible e
p=1 mod 4    v2(p-1)>=41           1       1,2,3,4,5,6
p=1 mod 4    v2(p-1)=40            2       2,4
p=1 mod 4    v2(p-1)=39            4       4
p=3 mod 4    v2(p+1)>=40           2       2,4
p=3 mod 4    v2(p+1)=39            4       4
```

All 12 types are nonempty. Exactly seven are non-generating (`k<e`):

```text
plus,  k=1, e in {2,3,4,5,6};
plus,  k=2, e=4;
minus, k=2, e=4.
```

There is no official `e=6,k=2` row in either branch. This is a field-cap
and primality exclusion, not merely an omitted table entry.

The theorem classifies rows; it does not pay the seven non-generating
families or prove an F2/Prize bound.

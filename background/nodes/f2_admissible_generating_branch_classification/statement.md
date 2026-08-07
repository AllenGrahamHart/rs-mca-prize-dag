# F2 admissible generating-row branch classification

- **status:** PROVED
- **closure:** proof

Fix an official maximal rate-half row

```text
n=2^41, q=p^e<2^256, n divides q-1,
```

and assume the row is generating: `ord_n(p)=e`. Exactly five
residue-signed types are possible:

```text
branch       valuation                         e=ord_n(p)
p=1 mod 4    v2(p-1)>=41                       1
p=1 mod 4    v2(p-1)=40                        2
p=1 mod 4    v2(p-1)=39                        4
p=3 mod 4    v2(p+1)>=40                       2
p=3 mod 4    v2(p+1)=39                        4
```

All five types are nonempty. In table order, certified prime witnesses are

```text
3*2^41+1,  27*2^40+1,  5*2^39+1,
2^61-1,    25*2^39-1.
```

Taking `q=p^e` gives `q<2^256` and `ord_n(p)=e` in each case. Therefore an
unsigned census containing only the three `p=1 mod 4` types is not an
all-admissible generating-row census.

This node classifies generating rows only. It makes no weighted-mass,
non-generating-row, adjacent-row, or Prize claim.

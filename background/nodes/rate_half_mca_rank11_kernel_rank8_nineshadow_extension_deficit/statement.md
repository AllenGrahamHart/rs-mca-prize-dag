# Rank-eight nine-shadow extension deficit

- **status:** PROVED
- **scope:** one exact residual support and all rank-eight nine-subsets
- **units:** support pairs extending a fixed nine-subset

Let `S` be one exact residual support, `|S|=m'=K'+67472`, and let `U`
be a rank-eight nine-subset of `S`. At least

```text
L_2=C(67474,2)=2276336601
```

pairs in `C(S minus U,2)` raise the rank from eight to ten. Consequently
`U` has at most

```text
D_2=C(m'-9,2)-L_2
```

extensions to a rank-deficient eleven-set.

If `I_d(S)` counts corank-`d` kernel eleven-sets, the full-containment
resource sharpens to

```text
[52+3E_0/E_1] I_1
 +[55+6L_2/E_2] I_2
 +55 sum_(d=3)^9 I_d
 <= E_0 C(m',9),                                  (R8FC)

E_0=C(m'-9,2), E_1=C(K'-10,2), E_2=C(K'-11,2).
```

Terms with zero extension coefficient vanish.

## Falsifier

A rank-eight nine-subset with fewer than `C(67474,2)` full-rank pair
extensions, a rank-nine closure exceeding `K'-1`, or a record violating
(R8FC).

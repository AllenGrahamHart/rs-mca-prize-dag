# Budget-three maximal-row field-degree collapse

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`

Let `q=p^e` be an admissible field order on the maximal rate-half row

```text
n=2^41,       k=2^40,       B*=floor(q/2^128)=3.    (MFC1)
```

Then `e` is either one or two. More precisely,

```text
e=1  ==>  p=q and p=1 mod 2^41,
e=2  ==>  q=p^2 and p=+/-1 mod 2^40.               (MFC2)
```

No cubic or higher extension field occurs in this branch.

The conclusion uses both official-scale inputs: `2^41 | q-1` and the narrow
budget interval

```text
3*2^128<=q<4*2^128=2^130.                          (MFC3)
```

It does not apply to smaller evaluation domains merely from `B*=3`.

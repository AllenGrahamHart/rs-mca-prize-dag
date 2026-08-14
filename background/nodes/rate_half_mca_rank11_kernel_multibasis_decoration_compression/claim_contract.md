# Claim contract

## Input

One kernel-lane `(record,T)` incidence from the ten-dimensional residual
correction space, with `|T|=11`, evaluation corank `1<=d<=9`, no global
common-zero coordinate, and the fixed-basis cap supplied by the canonical
basis globalizer.

## Output

At least `d+2` valid basis decorations per incidence and the aggregate
rank-`d` capacity

```text
floor(C(n',10-d) M_d C(K'-10,d+1)/(d+2)).
```

## Nonclaim

No claim is made that there are more than `d+2` bases, that different
bases have disjoint record families, or that the resulting capacity pays
every shortening.

# Paper D v13.2 near-rational support-wise payment

- **status:** REFUTED
- **source:** Paper D v13.2 `cor:capfp-line`

## Refuted claim

At agreement `m`, put `w=m-K` and assume `n-3w>=m`. If two finite slopes
have `d1(u+z_i v)<=w` and nonzero census, the resulting common codeword-pair
proximity implies that no slope is support-wise MCA-bad.

The implication is false, already for a rate-half Reed-Solomon code on
`mu_8 subset F_17`. A common codeword-pair explanation on one support does
not force an unrelated support explaining a line word to extend to the same
or another codeword pair.

This refutation does not by itself refute the displayed upper bound

```text
N_MCA-bad <= 1 + #{z: d1(u+zv)>=w+1 and cen(u+zv;m)>0}.
```

It refutes the proof step offered for paying the near-rational slopes. A
valid replacement needs a support-wise first-match or mismatch census.

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

The original `mu_8` witness below isolates the false support inference. A
second smooth rate-half witness on `mu_16=F_17^*`, recorded in
`refutation.md` and replayed by `verify.py`, refutes the displayed upper
bound itself:

```text
N_MCA-bad <= 1 + #{z: d1(u+zv)>=w+1 and cen(u+zv;m)>0}.
```

In that witness every slope is within distance `w=2` of the zero codeword,
so the right-hand set is empty, while two distinct slopes are support-wise
MCA-bad. The proved replacement is the uniform `2w` theorem in
`v13_2_near_rational_supportwise_two_anchor_payment`.

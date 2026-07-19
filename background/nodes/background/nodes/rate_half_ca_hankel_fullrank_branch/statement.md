# Full-column-rank Hankel branch

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`

In the setting of `rate_half_ca_hankel_split_pencil_equivalence`, assume

```text
r<R/2
```

and let

```text
M(Z)=M_r(y_0)+Z M_r(y_1)
```

be the `(R-r) x (r+1)` syndrome Hankel pencil. If

```text
rank_{F(Z)} M(Z)=r+1,                                  (HF1)
```

then at most `r+1` finite slopes have a nonzero kernel. In particular,

```text
#{gamma:ker M(gamma) intersects D_r(D)}<=r+1.          (HF2)
```

Thus every column-far pair in this branch has at most `r+1` CA-bad slopes.

At the first unresolved official rate-half candidate, `r=B*(q)-1`. For

```text
B_Q<B*(q)<=2^39,
```

the full-column-rank branch proves the required far-CA bound `<=B*(q)` and
therefore closes that candidate. Only pencils with generic rank at most `r`
remain. At the last CA-only block `B*(q)=2^39+1`, one has `r=R/2`; the matrix
has only `r` rows and `r+1` columns, so generic rank deficiency is automatic.

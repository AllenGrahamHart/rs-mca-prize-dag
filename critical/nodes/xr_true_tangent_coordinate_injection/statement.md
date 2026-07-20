# True tangent coordinate injection

- **status:** PROVED
- **consumers:** `xr_tangent_support_mismatch_bridge`,
  `xr_clean_residual_any_gate`

Let `C` be a linear code of length `n`. Suppose

```text
u=c_0+e_0,       v=c_1+e_1,
T=supp(e_0,e_1),       |T|<=n-A,
```

with `c_0,c_1 in C`. Consider finite slopes `z` having a support-wise MCA-bad
witness `S`, `|S|>=A`, whose explaining codeword is exactly
`c_0+z c_1`. Then

```text
# such slopes <= |T| <= n-A.
```

Thus the genuine recovered-line tangent branch fits inside the printed
`n-A+1` slot without any deep-regime hypothesis. The unresolved nondeep
content consists only of witnesses explained by a different codeword.

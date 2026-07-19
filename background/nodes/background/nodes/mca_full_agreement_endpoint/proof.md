# Proof

Pass to the quotient vector space `F^D/C`. For a received pair `(f_1,f_2)`, a
full-agreement slope must satisfy

```text
[f_1]+gamma[f_2]=0.
```

If `[f_2]!=0`, this equation has at most one finite slope. If `[f_2]=0`, it has
no solution unless `[f_1]=0`; when both classes vanish, the pair itself lies in
`C^2`, so every full-support witness extends mutually and no slope is MCA-bad.
Therefore `B_mca(n)<=1`.

For the reverse inequality, choose `f_2` outside `C`, a codeword `c_0`, and a
slope `gamma_0`, and put

```text
f_1=c_0-gamma_0 f_2.
```

At `gamma_0` the line word is exactly `c_0`, so `(c_0,D)` is a full-agreement
witness. It cannot extend mutually: an extension on all of `D` would put
`f_2` in `C`. Hence this slope is MCA-bad, proving `(FA1)`. The same witness
has agreement at least `a` for every `a<=n`, proving the lower statement.

Dividing the exact numerator by `q` gives `(FA2)`. At the official rate-half
row, the proved pole floor makes every agreement through
`k+8,594,128,895` unsafe, while `(FA1)` makes agreement `n` safe whenever
`floor(q/2^128)>=1`. Monotonicity gives `(FA3)`. QED.

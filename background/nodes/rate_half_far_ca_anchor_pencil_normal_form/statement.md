# Far-CA anchor-pencil normal form

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`

Let `C` be a linear code over `F`, let a received pair `(f_1,f_2)` be
column-far at integer radius `r`, and let `B` be its finite CA-bad slope set.
Fix `gamma_0 in B`, a witness `c_0 in C`, and put

```text
e_0=f_1+gamma_0 f_2-c_0,       E_0=supp(e_0),       s=|E_0|<=r.
```

Then the non-anchor bad slopes have the exact presentation

```text
B\{gamma_0}
 ={gamma_0+lambda:
   lambda in F^*, there exists p in C with
   wt(e_0+lambda(f_2-p))<=r}.                         (AP1)
```

For every pair `(lambda,p)` in `(AP1)`, define

```text
T={j outside E_0:p(j)!=f_2(j)},       t=|T|.
```

Column farness and the radius budget force

```text
r-s+1<=t<=r,                                           (AP2)
#{j in E_0:p(j)=f_2(j)+e_0(j)/lambda}>=s+t-r>=1.       (AP3)
```

If `2r<d_min(C)`, the codeword `p` is unique for each non-anchor slope.

For the first unresolved official rate-half range, `r=B*(q)-1<=2^39` and
`d_min=k+1=2^40+1`, so uniqueness holds. The remaining far-CA assertion is
therefore a direct count of the distinct nonzero `lambda` admitted by
`(AP2)--(AP3)`, with at most `r` non-anchor values required. This exact
anchor-pencil object is strictly sharper than an unrestricted deficient
pair-list count.

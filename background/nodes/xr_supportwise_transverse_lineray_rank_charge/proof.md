# Proof

Fix one selected ray and abbreviate `e=e_z`, `E=supp(e)`, and `S=D\E`.
Suppose, contrary to `(TR)`, that both endpoint syndromes have lifts supported
on `E`. Thus there are vectors `a_0,a_1` supported on `E` with

```text
Ha_0=Hu,       Ha_1=Hv.
```

Then `c_i=u_i-a_i` (with `u_0=u` and `u_1=v`) lies in `ker H=C`. Since each
`a_i` vanishes on `S`, the pair `(c_0,c_1)` agrees with `(u,v)` throughout
`S`. This contradicts support-wise nontriviality.

Conversely, if a codeword pair agrees with `(u,v)` on `S`, the differences
`u-c_0` and `v-c_1` are supported on `E` and lift `Hu` and `Hv`. Hence
support-wise nontriviality is in fact equivalent to `(TR)` for the selected
zero mask.

Choose one retained `(z,p_z)` above every retained slope. The errors are
distinct as LineRay pairs, have weight at most `r`, satisfy

```text
He_z=Hu+zHv,
```

and obey `(TR)` individually. The selector inequality `(SEL)` in
`xr_all_lineray_affine_core_bound` therefore gives `(SWLR)`. Notice that the
argument never excludes a different joint agreement support; this is why it
applies to the mismatch branch.

For `sigma<=3`, monotonicity in `sigma` and the exact official-row replay in
the audit give

```text
C(sigma+r,sigma)<=C(r+3,3)<8n^3.
```

At RowC rate `1/4`, `n=1024`, `A=261`, and `r=763`; direct integer
evaluation gives the displayed rank-four inequality. At every other row the
rank-four binomial exceeds `16n^3`, so no stronger rank conclusion is
claimed.

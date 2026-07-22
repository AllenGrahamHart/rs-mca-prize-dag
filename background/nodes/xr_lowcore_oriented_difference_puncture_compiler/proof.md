# Proof

Fix `I` in the oriented fiber and its X-side selected slope/codeword
`(z,p_z)`. On `X`, both `p_z` and `a_X+z b_X` equal `u+zv`. Their difference
is a degree-below-`K` polynomial vanishing on `X`, so

```text
p_z-a_X-zb_X=Lambda_X q_z
```

for one polynomial `q_z` of degree below `K-t=K'`. Dividing the agreement
identity on `I`, which is disjoint from `X`, proves `(PC3)`. Uniqueness is
immediate from polynomial division.

The support size is

```text
|I|=A-t=A'.
```

For distinct residuals `I,J`, their original X-side supports intersect in
`X union (I intersect J)`. The P-B cap gives

```text
t+|I intersect J|<=K-1,
```

which is `(PC4)`.

Suppose the reduced pair were not globally generic. Then degree-below-`K'`
polynomials `q_0,q_1` would jointly agree with `(u_X',v_X')` on some
`R subset D_0` of size at least `A'`. The lifted polynomials

```text
c_0=a_X+Lambda_X q_0,       c_1=b_X+Lambda_X q_1
```

have degree below `K`. They agree with `(u,v)` on `X` by interpolation and
on `R` by `(PC2)`, hence jointly explain the original pair on at least
`t+A'=A` coordinates. This contradicts original global genericity. The
Y-side argument is identical.

For the rank bound, every reduced selected error has the form

```text
e_z'=u_X'+zv_X'-q_z.
```

All these vectors lie in the affine space

```text
u_X'+span(v_X', ev_(D_0)(F[T]_<K')),
```

whose dimension is at most `K'+1`. Global genericity supplies the
support-wise LineRay transversality hypothesis. Applying
`xr_all_lineray_affine_core_bound` with radius `r'=N'-A'` proves `(PC5)`.

For `K'=1`, `(PC5)` is `C(r'+2,2)<n^2` at every official `n>=1024`; for
`K'=2`, it is `C(r'+3,3)<n^3`. Both are strictly below `8n^3`.

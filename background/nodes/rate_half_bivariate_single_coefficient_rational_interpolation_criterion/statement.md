# Single-coefficient rational-interpolation criterion

- **status:** PROVED
- **closure:** dual Reed-Solomon kernel characterization
- **consumer:** `rate_half_band_crossing_location`

Let `W` contain `n=s+r` distinct field points, where

```text
s=4m+1,       r=n-s>=1,
sigma_W(X)=product_(x in W)(X-x).                     (RIC1)
```

For scalar data `h:W->F`, form the two-block matrix

```text
G_h = (x^i)_(0<=i<s,x in W)
      --------------------------------
      (h(x)x^i)_(0<=i<s,x in W).                      (RIC2)
```

Then `G_h` has full column rank `n` if and only if there do not exist
polynomials

```text
0!=P in F[X],       Q in F[X],
deg P<r,            deg Q<r,
Q(x)=h(x)P(x)       for every x in W.                 (RIC3)
```

Thus rank failure is exactly a rational interpolant `h=Q/P` of numerator and
denominator degree below the residual width.

In the clean endpoint `O=0`, suppose the unique deficient point `x_0` lies
in `W`. The chosen coefficient block also contains one lower-clone column
whose top block is zero and whose lower block is a nonzero multiple of
`(x_0^i)_(0<=i<s)`. The resulting `2s x (n+1)` matrix has full column rank if
and only if there are no `P,Q` as above satisfying

```text
Q(x)=h(x)P(x)       for every x in W\{x_0}.           (RIC4)
```

No condition at `x_0` is required because the lower clone absorbs that one
value.

For the deficiency-aware bivariate matrix, take `h=h_m`, the coefficient one
below the top of the normalized highest-clone polynomial. Formula `(SID5)`
gives the official scalar datum

```text
h_m(x)=-(mu_x+sum_(gamma in A_x)gamma).                (RIC5)
```

When `m=2` and `W=S_g union S_h` is canonical, write

```text
H_x(Y)=(Y-g)(Y-h)(Y-nu_x).
```

Then `h_2(x)=-(g+h)-nu_x`, so `(RIC3)--(RIC4)` reduce exactly to exclusion
of a degree-`<r` rational interpolant for the third-root data `nu_x`.

## Scope

This criterion is an equivalence for one coefficient block. It does not prove
that the official trace data `(RIC5)` avoid low-degree rational interpolation,
nor does it use the remaining coefficient blocks.

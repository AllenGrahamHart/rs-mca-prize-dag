# Proof: sharp fixed-agreement shortening

At the sharp endpoint the background has `ell-3` points and both touched
petals have `ell` points, proving `(SH1)`. Every contributor agrees with the
received word on all of `S_0`. Interpolation gives the unique `Q_0` of
degree below `|S_0|`. Therefore `P-Q_0` vanishes on `S_0` and is divisible
by `L_(S_0)`, giving `(SH2)`. The quotient is unique and

```text
deg T <= (k-1)-|S_0|
      =(5ell-5)-(3ell-3)=2ell-2.
```

The core is disjoint from `S_0`, so its locator is nonzero at every core
point and `(SH3)` is defined. For `x in C`, equation `(SH2)` gives

```text
P(x)=U(x)  iff  T(x)=v(x).                            (1)
```

The exact defect locator has `2ell-3` roots in `C`. On its complement the
candidate agrees with `U`; at each defect root it does not agree, by the
exact core-defect condition `gcd(F,W)=1`. Hence `T` has exactly
`(5ell-5)-(2ell-3)=3ell-2` agreements with `v` on `C`. This proves the
injection into `(SH4)`. The arithmetic in `(SH5)` follows directly, since
`N-K_0=3ell-4` and

```text
floor(2(3ell-4)/3)=2ell-3.
```

Finally, `P` is recovered uniquely from `T` by `(SH2)`, so the map is
injective. The remaining FPC5 guards can only shrink the shortened list.

For the determinant specialization, substitute the parameters in `(SH5)`
into the balance definitions of
`l1_balanced_pencil_anchor_determinant_atlas`:

```text
w=m'-k'=ell-1,
omega=n'-m'=2ell-3,
s=omega-w=ell-2.
```

Thus `s>=1` and the balanced-shell theorem applies. Its deficiency variable
is `j=s-1-deg D=ell-3-deg D`, proving `(SH7)`. Its determinant degree is at
most `s-1=ell-3`. Substituting `m'=3ell-2` and
`h=w+1+j=ell+j` into its two fixed-owner bounds gives

```text
floor( binom(m',j+1)/binom(h,j+1) )
 =floor( binom(3ell-2,j+1)/binom(ell+j,j+1) ),

floor( binom(m',r)/(h-r+1) )
 =floor( binom(3ell-2,r)/(ell+j-r+1) ),
```

which proves `(SH8)`. At `j=0` the realized projective rank is one and the
moving-root bound is `floor(m'/(w+1))=floor((3ell-2)/ell)=2`, proving
`(SH9)`. The atlas explicitly retains the sum over the possible gcd owners,
so no aggregate bound follows. QED.

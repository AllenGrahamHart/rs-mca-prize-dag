# Proof

The values in `(SP1)` define unique interpolating polynomials of degree below
`h` because the `y_i` are the distinct roots of `Y^h-1`.

Write `A(Y)=sum_(s<h) alpha_sY^s`. Fourier inversion on `H` gives

```text
alpha_s=h^(-1) sum_i A(y_i)y_i^(-s).                     (1)
```

For `1<=r<=L`, the even moment `2r` is

```text
sum_i (a_i+b_i)y_i^r
 = sum_i A(y_i)y_i^r + sum_i y_i^r
 = sum_i A(y_i)y_i^r,                                    (2)
```

because `r<h`. By `(1)`, these equations kill exactly the coefficients
`alpha_(h-1),...,alpha_(h-L)`. They are therefore equivalent to
`deg A<=h-L-1`.

Similarly, write `W(Y)=sum_(s<h) omega_sY^s`. The odd moment `2r+1` is

```text
sum_i (a_i-b_i)x_i y_i^r=sum_i W(y_i)y_i^r.              (3)
```

For `0<=r<L`, Fourier inversion says that `(3)` kills `omega_0` and
`omega_(h-1),...,omega_(h-L+1)`. This is exactly `W(0)=0` and
`deg W<=h-L`. Thus the moment equations are equivalent to `(SP2)`.

At each `y_i`, the four binary pair states give

```text
(a_i,b_i)  A(y_i)  W(y_i)
   (0,0)     -1       0
   (1,1)     +1       0
   (1,0)      0      +x_i
   (0,1)      0      -x_i.
```

Hence `A(A^2-1)` and `W^2+YA^2-Y` vanish at every root of `Y^h-1`, proving
`(SP3)`.

Conversely, the first congruence in `(SP3)` puts every `A(y_i)` in
`{0,+1,-1}`. If `A(y_i)=+1` or `-1`, the second congruence forces
`W(y_i)=0`; if `A(y_i)=0`, it gives `W(y_i)^2=y_i=x_i^2`, hence
`W(y_i)=+x_i` or `-x_i`. Odd characteristic makes these alternatives
distinct. The displayed table therefore recovers one and only one binary
pair at every coordinate. This proves the bijection.

The word is antipodally invariant exactly when `a_i=b_i` for every `i`,
equivalently when all `W(y_i)` vanish. Since `deg W<h`, that is equivalent
to `W=0`. Thus nonzero `W` is exactly primitive first ownership, and the
count is `Z_0-C_1`.

Finally, the second polynomial in `(SP3)` has degree at most `2h-2L`.
If `L<=h/2`, division by `Y^h-1` gives `(SP4)`. If `L>h/2`, its degree is
strictly below `h`, so divisibility forces it to vanish identically. QED.

# Proof

Because `v_2(514)=1`, the singleton parity polynomial has multiplicity one at
`X=1`, and its parity autocorrelation has multiplicity exactly two. In the
profile `(0,2,0)`, every autocorrelation is even. Its parity autocorrelation is
therefore zero, of multiplicity at least 128, a contradiction. This removes
the energy-eight all-even profile.

It remains to treat the sole energy-thirteen survivor `(13,0,0)`. At an odd
conjugate `u`, its deviation is

```text
x_u=sum_(j=1)^13 epsilon_j
       (zeta_256^(u d_j)+zeta_256^(-u d_j)),         (1)
```

with 13 distinct positive-half lags. Odd multiplication and folding permute
the 63 nonfixed lag classes. Hence, regardless of the signs,

```text
x_u<=2 sum_(j=1)^13 cos(pi*j/128).                  (2)
```

We certify a rational upper bound for `(2)`. Machin's identity

```text
pi=16 atan(1/5)-4 atan(1/239)
```

and alternating rational series give

```text
333/106<pi<355/113.                                 (3)
```

For `0<=t<1`, the alternating cosine series gives
`cos(t)<=1-t^2/2+t^4/24`. Applying the lower bound in `(3)` to the negative
quadratic term and the upper bound to the positive quartic term yields

```text
2 sum_(j=1)^13 cos(pi*j/128)
 <=2(13-(333/106)^2 sum j^2/(2*128^2)
        +(355/113)^4 sum j^4/(24*128^4))
 <2551/100.                                         (4)
```

The final rational margin in `(4)` is

```text
7795466688479683619/12294344879326520934400.
```

Put `M=2551/100`, `z=683/500`, and `C=z/(128*13)`. A two-term positive atanh
sum plus its geometric tail proves

```text
log(1+M/18)<M/18-C M^2,                             (5)
```

with positive rational margin

```text
1589177092552089193351/25273817512265112960000000.
```

Also

```text
1/(36(18+M))<C<1/648.
```

The derivative argument from the preceding logarithm leaves therefore makes
`log(1+x/18)<=x/18-Cx^2` valid on `(-18,M]`. Equations `(1)--(5)` and
`sum x_u^2=128*13` give

```text
log Norm<64log(18)-683/500.                         (6)
```

Finally the degree-six positive exponential Taylor polynomial proves exactly

```text
exp(683/500)>18^64/(514*p_min).                     (7)
```

Equations `(6)--(7)` put the norm below `514*p_min`, excluding the
energy-thirteen profile. Removing these two rows from the 17-profile router
leaves 15. QED.

# Proof

Fix a nonzero oriented difference `(X,Y)`. A pair `(S,T)` with

```text
1_S-1_T=1_X-1_Y
```

has the unique form

```text
S=X union I,       T=Y union I,
I=S intersect T subset Omega\(X union Y).
```

Since `|S|=|T|=a`, both `X` and `Y` have size `t`, and `|I|=a-t`.
The low-core hypothesis gives

```text
a-t=|S intersect T|<=a-H,
```

so `t>=H`. Also `|S union T|=a+t<=N`, hence `t<=N-a`. This proves
`(TS3)` and identifies the multiplicity of the difference with `(TS2)`.

If `I!=J` lie in the same fiber, then the distinct members `X union I` and
`X union J` intersect in at least all `t` points of `X`. By `(TS1)`,
`t<=K-1`. This proves `(TS3a)`.

Take distinct `I,J` in `R_(X,Y)`. The two members `X union I` and
`X union J` of `mathcal F` satisfy

```text
t+|I intersect J|
 = |(X union I) intersect (X union J)|
 <=a-H.
```

Therefore

```text
|I intersect J|<=(a-t)-H,
|I triangle J|>=2H.                                      (1)
```

The residual sets are consequently a binary constant-weight code of length
`N-2t` and distance at least `2H`.

For `r=|R_(X,Y)|`, sum pairwise Hamming distances coordinatewise. If a
coordinate occurs in `b_x` residual sets, its contribution is
`b_x(r-b_x)<=r^2/4`. Thus

```text
C(r,2)2H<=(N-2t)r^2/4.                                  (2)
```

When `N-2t<4H`, rearranging `(2)` gives `(TS4)`. At equality, the sign-vector
form of the Rankin bound gives at most `2(N-2t)=8H` codewords, proving
`(TS5)`.

Every ordered pair `(S,T)` has one unique oriented difference `(X,Y)`, so

```text
sum_(X,Y) r_(X,Y)=M^2.
```

The zero difference has multiplicity `M`, and the nonzero fibers account for
`M(M-1)` ordered pairs. Equality of two differences is exactly the quadruple
condition in `(TS6)`, proving the energy identity. On the terminal range,
`r_(X,Y)<=8H`; hence

```text
E_term=sum_terminal r_(X,Y)^2
      <=8H sum_terminal r_(X,Y)
      <=8H M(M-1),
```

which is `(TS7)`. Finally, if `N,H<=n` and `M>8n^3`, then

```text
8H M(M-1)<8nM^2<M^3/n^2.
```

This proves `(TS8)`. Independently, `(TS3a)` gives

```text
sum_(t>=K) r_(X,Y)^2=sum_(t>=K) r_(X,Y)<=M(M-1),
```

which proves `(TS7a)` and confines every repeated difference to `(TS9)`.
At each printed official row the terminal threshold is strictly above `K`,
so the entire terminal interval is already in this multiplicity-one range.

It remains only to justify the distinct-support input for P-B. Suppose finite
slopes `z!=w` have selected codewords `p_z,p_w` and the same agreement support
`S`. Put

```text
c_1=(p_z-p_w)/(z-w),       c_0=p_z-zc_1.
```

On `S`, subtracting `u+zv=p_z` and `u+wv=p_w` gives `v=c_1`, and then
`u=c_0`. Thus `(c_0,c_1)` is a joint codeword-pair explanation on `S`,
contrary to global genericity. The projective infinity chart is identical
after swapping the two received directions. Hence one selected support per
slope gives distinct members of `mathcal F`.

# Proof

At `u=4`, the quadratic normal form gives

```text
O=0,       C_tot=I_H=e-6.                            (1)
```

As in the double-root arm, zero omission forces every residual locator to
have exactly `d=rho-1` distinct residual-domain roots. Adding the fixed core
point `s_0` gives `|E_gamma|=rho` for all `T=rho+4` supported slopes.

The heavy factor has degree `rho-6`, so its complement in the residual
domain is a light set of size `3rho+5`; every light point is saturated and
has degree `e`. The two-simple normal form gives distinguished counts

```text
|Z_1|=e-c_1=(e-3)/2,
|Z_2|=e-c_2=(e-9)/2.                                 (2)
```

They sum to `e-6=I_H`, so these are all heavy incidences. The remaining
`rho-8` heavy rows have degree zero. This proves `(TSS3)`, including the
handshake identity

```text
T+(3rho+5)e+(e-3)/2+(e-9)/2=T rho.                  (3)
```

Every excess root in the zero-omission packet is simple and new relative to
the specialized minimal locator, and there is no excess degree away from
`x_1,x_2`. Therefore the specialized rank loss is exactly `r_gamma`: one
for each heavy padded root present in `E_gamma`. A split syndrome with at
most `rho` sources has middle-Hankel rank equal to its number of nonzero
sources. The rate-half minimum distance `2rho+1` makes its radius-`rho`
codeword center unique. Hence the actual error weight is `rho-r_gamma`,
proving `(TSS4)`.

Let an affine codeword line contain the assigned centers at `h` slopes
`A`, and subtract it from the received pencil. Its error pencil has joint
support `U` of size at least `rho+1` by column-farness. At each coordinate
of `U`, a nonzero affine value vanishes at at most one slope, so

```text
(h-1)|U|
 <=sum_(gamma in A)wt(f_gamma-c_gamma)
 =h rho-sum_(gamma in A)r_gamma.                     (4)
```

Using `|U|>=rho+1` in `(4)` gives `(TSS5)`.

Finally fix `alpha,beta`. If a third locator has triple union at most
`2rho`, the difference between its assigned center and the affine codeword
line through the first two centers is a codeword supported on that union.
Minimum distance makes the difference zero. Thus every nonexpanding third
center lies on the same line.

That line contains at least `r_alpha+r_beta` heavy-root deficits. By
`(TSS5)` it contains at most `rho+1-r_alpha-r_beta` assigned centers. Since
`T=rho+4`, at least `3+r_alpha+r_beta` centers lie off the line, and their
locator triples have union at least `2rho+1`. This proves `(TSS6)--(TSS7)`.
QED.

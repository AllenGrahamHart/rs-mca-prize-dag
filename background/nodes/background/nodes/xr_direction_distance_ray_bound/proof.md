# Proof

If `|Z|<=1`, the result is immediate from the displayed bound, whose numerator
exceeds its positive denominator. Otherwise two distinct line points lie in
`im(H_U)`, so both `y_0` and `y_1` do. Choose lifts
`b_0,b_1 in F^U`. For each `gamma in Z`, choose a
lift of weight at most `t` and write it as

```text
e_gamma=b_0+gamma*b_1+z_gamma,       z_gamma in K.
```

Put

```text
c_gamma=-gamma*b_1-z_gamma in K+<b_1>.
```

Distinct slopes give distinct `c_gamma`, since equality for two slopes would
put the nonzero syndrome `y_1` in `H_U(K)=0`. More precisely, the difference
of two selected words is a nonzero scalar multiple of a lift of `y_1`.
Therefore, by the definition `d=d_U(y_1)`,

```text
dist(c_gamma,c_gamma') >= d
```

for distinct slopes. Also `dist(b_0,c_gamma)=wt(e_gamma)<=t`, so all selected
words lie in one radius-`t` Hamming ball.

Set `s=N-t`. For every slope choose an `s`-set `B_gamma` of coordinates on
which `b_0` and `c_gamma` agree. The distance bound gives

```text
|B_gamma intersect B_gamma'| <= N-d = mu.
```

If `M=|Z|` and `r_x` is the number of chosen sets containing `x`, then

```text
sum_x r_x = Ms,
sum_x r_x^2 <= Ms+M(M-1)mu.
```

Cauchy--Schwarz supplies `sum_x r_x^2 >= M^2 s^2/N`. Under `(DD)`, rearranging
these inequalities gives

```text
M <= N(s-mu)/(s^2-Nmu)
  = N(d-t)/((N-t)^2-N(N-d)).
```

The denominator is a positive integer and the numerator is at most `N^2`,
which proves `(DDR)`.

Finally, failure of `(DD)` is

```text
d <= 2t-t^2/N.
```

Since `d` is the weight of a minimum lift, this proves the sparse-direction
alternative directly.

## Provenance and scope

The argument independently rederives the direction-distance compiler in
`rs-mca-vendor-20260711@e190193c`,
`experimental/notes/thresholds/direction_distance_large_kernel_ray_compiler.md`.
That source explicitly leaves the low-direction locus and atlas exhaustion
open. The same boundaries are retained here.

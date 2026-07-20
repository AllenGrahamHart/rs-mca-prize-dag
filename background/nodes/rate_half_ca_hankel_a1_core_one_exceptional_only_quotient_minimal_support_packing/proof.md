# Proof

Choose two distinct minimal supports `T,T'`, together with source
representations of `h_1` on `R_A union T` and `R_A union T'`. Their
difference is a nonzero moment-column relation: a point in either symmetric
difference has a nonzero minimal coefficient. Every set of at most `2r+1`
residual-domain moment columns is Vandermonde-independent, so

```text
|R_A union T union T'|>=2r+2.                         (1)
```

Since `|R_A|=r-1` and both supports lie outside `R_A`, `(1)` gives

```text
|T union T'|>=r+3=2e+4.
```

Substitution into
`|T intersect T'|=2h-|T union T'|` proves `(QMP1)`. A negative right side
forbids a distinct pair, which also recovers uniqueness through `h=e+1`.

Now let `T_1,...,T_L` be all minimal supports of size `h>=e+2`. For each
point `x` in the `v`-point universe `D_res\R_A`, write `d_x` for the number
of supports containing it. Then

```text
sum_x d_x=Lh,
sum_x binom(d_x,2)=sum_(i<j)|T_i intersect T_j|
                  <=binom(L,2)lambda_h.               (2)
```

Cauchy--Schwarz gives `sum_x d_x^2>=(Lh)^2/v`. Insert this into `(2)`:

```text
L^2h^2/v-Lh<=L(L-1)lambda_h.                          (3)
```

After cancelling `L` and multiplying by `v`, `(3)` is

```text
L(h^2-vlambda_h)<=v(h-lambda_h).                      (4)
```

When `Delta_h>0`, division and integrality prove `(QMP3)`.

It remains only to evaluate the bigint endpoints. With
`e=274877906943` and `v=1649267441665`, direct integer substitution gives

```text
Delta_(302646214511)=350860694341>0,
Delta_(302646214512)=-2342381759966<0.                (5)
```

The quadratic `Delta_h` is decreasing on the entire interval in `(QMP4)`,
so `(5)` proves the cutoff. Formula `(QMP3)` gives five at `h=e+2`, six at
`h=e+3`, remains at most six through `h=279180239468`, and becomes seven at
the next integer. This proves `(QMP4)--(QMP5)`. QED.

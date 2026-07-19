# Proof

The diagonal embedding gives `L_(m,P)>=L_P`, and `m=1` is immediate. Assume
`m>=2`. For the upper bound, fix an
interleaved received word `U` and a property-filtered common-support list `X`
of size `N`.

For `alpha in F^(m-1)`, use the projection

```text
Phi_alpha(c_1,...,c_m)=c_1+sum_(i=2)^m alpha_i c_i.
```

For a tuple `x in X` with exact common support `S`, call `alpha` good for `x`
when the projected codeword has exact agreement support `S`, rather than a
strict superset. At each of the at most `r` coordinates outside `S`, the
projected error is one nonzero affine-linear form in `alpha`. Its zero set is
either empty or a hyperplane of size `q^(m-2)`. Therefore at least

```text
G=q^(m-2)(q-r)
```

projections are good for each tuple.

For fixed `alpha`, let `N_alpha` be the number of tuples for which it is good.
Their projected exact supports still belong to `P`, so their image has at
most `L_P` elements. Cauchy--Schwarz gives at least

```text
(N_alpha^2/L_P-N_alpha)/2
```

colliding unordered pairs. Since `sum_alpha N_alpha>=NG`, another
Cauchy--Schwarz application over the `q^(m-1)` projections gives the lower
bound

```text
1/2 * (N^2 G^2/(L_P q^(m-1))-NG)                 (1)
```

for the total number of good colliding incidences.

As in the unrestricted projection theorem, any fixed pair of distinct tuples
collides for at most `q^(m-2)` projections. Thus (1) is at most

```text
C(N,2)q^(m-2).                                    (2)
```

Substitute `G=q^(m-2)(q-r)` into `(1)<=(2)`, cancel the positive common
factors, and rearrange. When `D=(q-r)^2-L_Pq>0`, this yields

```text
N <= L_P q(q-r-1)/D.
```

Taking the integer floor and maximizing over `U` proves `(ESP)`. If `L_P=0`
but an interleaved tuple existed, any one of its good projections would give
an ordinary codeword with the same exact support in `P`, a contradiction.

# Proof

The dense-pair compiler selects eighteen explanations on one affine
codeword line and one certified explanation off that line. Hence the complete
`32`-tuple is not globally affine.

Maximalize every agreement support and let `C` be their common intersection.
The maximal-support slope-degree theorem gives `c=|C|<K`: if `c>=K`, two
slopes determine a degree-below-`K` codeword line and every other explanation
agrees with it on at least `K` points, forcing global affinity.

Use the proved maximal-common-core adapter. It chooses an actual size-`m`
noncontained witness through `C` for every explanation and then subtracts
the received-column interpolants on `C`, divides by the locator `L_C`, and
deletes `C`. Put

```text
n'=n-c,       K'=K-c,       m'=m-c,       d=m'-K'=m-K=67472.
```

The residual maximal supports have empty common intersection, and actual
support-wise MCA-badness is preserved. The dense-pair proof is unchanged:
its eighteen explanations remain affine in the slope after division, while
the off-line explanation remains off-line. Thus the residual slope degree
is in `18..31`.

## Support-collapsed extraction on the shortened row

Let `Lambda_i'` be the monic locator of the exact residual support `S_i'`.
At a coordinate in at least two supports impose

```text
A'(x)=Q(x)r_0'(x),       B'(x)=Q(x)r_1'(x).
```

At a singleton coordinate belonging to record `i`, impose

```text
A'(x)+gamma_i B'(x)=Q(x)h_i'(x).
```

Use coefficients of

```text
deg Q<=d,       deg A',deg B'<=m'
```

as homogeneous unknowns. Their number is

```text
(d+1)+2(m'+1)=3m'-K'+3.                            (1)
```

The number of equations is at most `chi'`. If
`chi'<3m'-K'+3`, a nonzero solution exists. For every `i`,

```text
P_i=A'+gamma_i B'-Qh_i'
```

has degree at most `m'` and vanishes on the `m'` roots of `Lambda_i'`.
Therefore

```text
Qh_i'+(c_0+c_1 gamma_i)Lambda_i'=A'+gamma_i B'.     (2)
```

The scalar is affine in the slope by comparison of the leading
coefficients of `A'` and `B'`.

If `Q=0`, nontriviality and two distinct slopes force `(c_0,c_1)!=0`, giving
a pure-locator certificate. If `Q!=0` but `(c_0,c_1)=0`, two slope
identities show that `Q` divides `A'` and `B'`; cancellation makes every
`h_i'` globally affine, contrary to the dense-pair off-line witness. The
remaining low-complexity case is a scalar-locator rational certificate,
with denominator roots retained rather than divided silently. If the strict
inequality fails, branch 3 holds.

## Exact lift to the original row

Let `A_C,B_C` be the degree-below-`K` received-column interpolants on `C`.
The shortening identities are

```text
h_i=A_C+gamma_i B_C+L_C h_i',
Lambda_i=L_C Lambda_i'.
```

Multiply (2) by `L_C` and substitute. The original certificate is

```text
Qh_i+(c_0+c_1 gamma_i)Lambda_i=A+gamma_i B,
A=Q A_C+L_C A',       B=Q B_C+L_C B'.               (3)
```

Its degrees are at most `m`: `deg(QA_C)<d+K=m`, while
`deg(L_C A')<=c+m'=m`, and similarly for `B`. The denominator, affine
locator scalars, and monic exact support locators are unchanged.

Finally, every coordinate of `C` lies in all `32` lifted supports and
contributes exactly two to two-cover complexity. Hence

```text
chi=chi'+2c.
```

The residual high-complexity threshold lifts as

```text
3m'-K'+3+2c
=3(m-c)-(K-c)+3+2c
=3m-K+3
=2299571.
```

This proves all three branches and their original-row interfaces.

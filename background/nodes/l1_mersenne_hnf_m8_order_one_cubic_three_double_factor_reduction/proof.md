# Proof - L1 Mersenne HNF m=8 order-one cubic three-double factor reduction

For each color `alpha_i`, the polynomial `E-alpha_i` is cubic with exactly
two distinct roots among the six roots of `L`. Let `F_i` be the monic
quadratic with those two roots. The three selected pairs are disjoint and
exhaust all roots of the monic squarefree sextic, so

```text
L=F_1F_2F_3.                                          (1)
```

After dividing by `e_3`, write

```text
e-a_i=F_i(W)(W-y_i),
F_i(W)=W^2+u_iW+v_i.                                 (2)
```

Comparison with `e=W^3+UW^2+VW+w` gives

```text
u_i-y_i=U,
v_i-u_i y_i=V,
-v_i y_i=w-a_i.                                     (3)
```

The first two equations solve as

```text
y_i=u_i-U,
v_i=u_i^2-Uu_i+V,                                   (4)
```

and the last gives the formula for `a_i` in (TDF3). This proves the
structured factorization.

Since the colors are distinct and `e_3!=0`, subtracting the formulas
`alpha_i=e_3a_i` cancels both `w` and the unknown scale. The ratio of two
differences is therefore (TDF4). The denominator is nonzero because
`alpha_3!=alpha_1`.

An actual packet also has the h=7 conic and norm-color properties from the
dependency. Exact gcd degree two is represented by the first two
subresultant vanishings of `L,E-alpha_i` and the next nonvanishing
subresultant. All displayed polynomial degrees are fixed, and only
quadratic factors occur before the color-ratio equation. QED.

# Proof

In the uniform split-pencil normalization, the error associated with slope
`gamma_i` is

```text
e_i=b+gamma_i q+w_i,       w_i in GRS_a.             (1)
```

It vanishes on the selected block `A_i`. The trade row `lambda_i` is a dual
`GRS_a` word supported inside `A_i`, so pointwise vanishing gives

```text
<lambda_i,b+gamma_i q+w_i>=0.                        (2)
```

The same row, restricted to `X`, is still a dual `GRS_a` word. It therefore
annihilates `w_i`, and `(2)` becomes

```text
<lambda_i,b+gamma_i q>_X=0.                          (3)
```

Substitute `lambda_i=(c_iF+d_iG)/Lambda'_X` into `(3)`. Expanding the four
bilinear terms gives `(RP2)`, which is exactly the dot product of `theta`
with `v_i`. This proves the unified assertion.

In the three-anchor branch, substitute

```text
lambda_i=s_i(P+gamma_iQ)/Lambda'_X
```

into `(3)` and divide by the nonzero `s_i`. The result is

```text
<P,b>_X
 +gamma_i(<P,q>_X+<Q,b>_X)
 +gamma_i^2<Q,q>_X=0.                                (4)
```

The quadratic in `(4)` has at least four distinct roots, so all three
coefficients vanish. This is `(RP4)`, and `(RP5)` is just its matrix form.
If `eta` is nonzero, the determinant of that matrix is `eta^2`, giving the
perfect-pairing branch; otherwise the matrix is zero.

In the four-anchor branch, four coefficient columns are a basis of `F^4`.
Since `theta` annihilates every column, it annihilates that basis and is zero.
This proves `(RP6)`.

Finally, reversing the displayed expansions shows that `(RP4)` makes the
quadratic `(4)` zero for every slope, while `(RP6)` makes every dot product
in `(RP2)` zero. This proves the stated parity-row converses and no more.
QED.

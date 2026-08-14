# Proof

The full-rank branch comes with a descended dense pair
`p_0'=(a_0',b_0')` and a ten-dimensional deviation space

```text
V'=span{d_gamma'},
d_gamma'=h_gamma'-a_0'-gamma b_0'.
```

Hence every selected residual explanation has the form

```text
h_gamma'=a_0'+gamma b_0'+d_gamma',       d_gamma' in V'.
```

Let the 32 fixed core slopes be `gamma_i`. Coefficientwise interpolation is
linear in the 32 values, so

```text
D_H(X,Z):=H(X,Z)-a_0'(X)-Zb_0'(X)
```

is a polynomial in `Z` whose every coefficient is an `F`-linear combination
of the vectors `d_gamma_i'`. Therefore every coefficient of `D_H` belongs to
`V'`. In particular,

```text
H_j in V' for every j>=2.
```

For any other selected slope,

```text
P_gamma
=h_gamma'-H(X,gamma)
=d_gamma'-D_H(X,gamma)
```

belongs to `V'`. Thus the complete correction span `W` is a subspace of
`V'` and has dimension at most ten.

If `dim W=0`, every selected explanation uses the core interpolant; the
relative core-interpolant cap pays the family. If `dim W=1`, all nonzero
corrections lie on one projective correction ray, and the proved core-plus-ray
bound pays the family. Therefore an over-budget survivor has `dim W>=2`.

The relative proper-intersection compiler pays every proper correction space
through dimension 11. Since `dim W<=10`, an over-budget survivor is
nonproper. The nonproper-tuple lemma then supplies an evaluation rank-flat or
an exact positive-dimensional polynomial clone component.

It remains to prove high-core absorption. If `dim W<=9`, this is exactly the
contrapositive of the relative clone-tolerant compiler: every nonabsorbing
space in that range is paid. If `dim W=10`, the inclusion `W<=V'` between
two ten-dimensional spaces is equality. Since every `H_j`, `j>=2`, lies in
`V'`, it lies in `W`. Thus every surviving dimension also absorbs the high
core.

All four conclusions follow.

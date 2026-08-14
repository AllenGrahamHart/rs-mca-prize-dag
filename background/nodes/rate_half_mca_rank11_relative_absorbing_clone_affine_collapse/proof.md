# Proof

Write the fixed core interpolant as

```text
H(X,Z)=sum_(j=0)^31 H_j(X)Z^j.
```

The clone component has full evaluation rank `s` on its `s+1` coordinate
tuple. Choose `s` coordinates `B` whose evaluation map

```text
ev_B:W -> F^B
```

is an isomorphism. Solving the coordinate equations on `B` coefficientwise
defines a unique curve

```text
P_B(Z)=sum_j P_(B,j)Z^j,       P_(B,j) in W.
```

For every `x in B`, the identity

```text
E_x(Z)+P_B(Z)(x)=0
```

holds. The received line has slope degree one. Comparing the coefficient of
`Z^j` for `j>=2` gives

```text
(H_j+P_(B,j))(x)=0       for every x in B.
```

Both summands lie in `W`: `P_(B,j)` by construction and `H_j` by the
high-core absorption theorem. Their sum is therefore a word of `W` in the
kernel of `ev_B`. Injectivity gives

```text
P_(B,j)=-H_j.
```

All coefficients of `H+P_B` of slope degree at least two vanish globally.
Hence

```text
H(X,Z)+P_B(X,Z)=A(X)+ZB(X)
```

for two degree-below-`K'` codewords `A,B`. This is one global affine
codeword owner line.

Let `G` be the coordinate set on which `(A,B)=(r_0',r_1')`. Residual
support-wise badness gives `|G|<m'`. Outside `G`, agreement with the two
affine lines determines at most one slope. If `N` slopes have agreement at
least `m'`, then

```text
N(m'-|G|)<=n'-|G|.
```

The quotient is maximized at `|G|=m'-1`, giving

```text
N<=n'-m'+1=R-d+1=981105.
```

The rank-deficient evaluation alternative does not supply an evaluation
basis and is not covered by this argument. Different clone components may
also yield different affine owners, so no aggregation claim is made.

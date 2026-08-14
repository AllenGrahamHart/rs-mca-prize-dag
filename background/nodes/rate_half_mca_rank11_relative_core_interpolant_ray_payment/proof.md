# Proof

Write `D'=D minus C_*`, and abbreviate the residual parameters by
`n',K',m'`. The full-rank branch has `K'>=10`.

## Core-compatible slopes

Let

```text
H(X,Z)=sum_(j=0)^31 H_j(X)Z^j
```

interpolate the 32 fixed residual explanations. For `x in D'`, put

```text
E_x(Z)=H(x,Z)-r_0'(x)-Zr_1'(x).
```

Every `E_x` is nonzero. Otherwise `H(x,Z)` would equal the residual received
line identically in `Z`, placing `x` in all 32 maximal supports, contrary to
their empty intersection. Thus `E_x` has at most 31 roots.

A slope for which `H(X,gamma)` is an agreement-`m'` explanation consumes at
least `m'` coordinate roots. Double counting gives

```text
|Z_0|m' <= 31n'.
```

The ratio `(R+K')/(d+K')` decreases with `K'`, so its maximum for `K'>=10`
is at `K'=10`, giving `|Z_0|<=481`. The 32 core slopes have already consumed
at least `32m'` roots, so the same count leaves at most

```text
floor((31n'-32m')/m') <=449
```

additional core-compatible slopes.

## A uniform coarse correction-ray bound

Fix nonzero `P in RS[F,D',K']`. At coordinates with `P(x)!=0`, put

```text
f_x(Z)=E_x(Z)/P(x).
```

Equal `f_x` define clone classes; zeros of `P` form the vertical class. A
clone class with at least `K'` coordinates forces every coefficient of

```text
H(X,Z)-f_x(Z)P(X)-r_0'(X)-Zr_1'(X)
```

to vanish as a degree-below-`K'` polynomial. Its correction graph is
therefore one global affine codeword line. Every such graph contributes at
most

```text
n'-m'+1=R-d+1=981105
```

rich slopes. Large clone classes are disjoint and nonempty, so there are at
most `n'` of them. Charging them this deliberately coarse number costs at
most `n'(n'-m'+1)`.

Remove all rich points on those graphs. In every remaining exact size-`m'`
support, the vertical class and every clone class have size at most `K'-1`.
Since `m'>K'-1`, the support meets at least two classes and hence contains at
least one heterogeneous unordered coordinate pair.

One heterogeneous pair supports at most 31 rich correction pairs. For two
different graph classes, equality requires

```text
f_x(gamma)=f_y(gamma),
```

a nonzero polynomial equation of degree at most 31, after which `c` is
fixed. For a vertical/graph pair, `E_x(gamma)=0` has at most 31 roots and the
graph coordinate fixes `c`. Therefore all remaining rich pairs cost at most
`31*C(n',2)`.

Combining both pieces gives

```text
N_ray <= n'(n'-m'+1)+31*C(n',2).
```

Both terms increase with `n'`, while `n'-m'+1=981105` is invariant. The
deployed endpoint `n'=2097152` is therefore worst and equals
`70227214729216`. Adding the uniform core-compatible bound gives
`70227214729697`, below `B_*` by `274910500896665390`.

Every selected slope contributes at most one chosen correction pair, so the
pair bound is a valid slope bound. This proves the result.

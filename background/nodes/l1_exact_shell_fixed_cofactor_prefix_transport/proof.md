# Proof - L1 exact-shell fixed-cofactor prefix transport

## 1. Normalization and degree

Replacing `U` by `U-R` for `deg R<k` translates every candidate codeword
`P` to `P-R` and preserves all agreement sets. Thus remove the low-degree
part of `U`.

If the normalized `U` is zero, it is itself a codeword. Any other
degree-below-`k` codeword differs from it by a nonzero polynomial with at most
`k-1` roots, so no exact shell below `n` occurs at agreement above `k`.

Now let `h=deg U>=k`. In `(FC1)`, subtracting `P` does not change the leading
term of `U`, while `L_A` is monic of degree `a`. Therefore `a<=h`,
`deg Q=h-a`, and `lc(Q)=lc(U)`. This proves `(FC2)` and the empty-shell gate.

## 2. Triangular prefix recursion

Write `l_0=1`. For `t>=0`, the coefficient of degree `h-t=a+e-t` in `QL` is

```text
q_e l_t + sum_(i=1)^min(e,t) q_(e-i) l_(t-i),         (1)
```

where terms with a locator index above `a` are absent. For every
`0<=t<=h-k`, the equation `deg(U-QL)<k` requires `(1)` to equal
`[Z^(h-t)]U`.

At `t=0` this is the already forced equality `q_e=lc(U)`. Since `q_e` is
nonzero, the equations for `t=1,2,...` successively determine `l_t` from the
previous locator coefficients. There are `h-k=w+e` nontrivial equations, but
only `a` nonleading locator coefficients. Thus precisely the first
`d=min(a,w+e)` coefficients are fixed. If `w+e>=a`, the complete monic
locator is fixed and any remaining product equations can only reject it.
This proves `(FC3)` and the per-cofactor fiber statement.

The leading coefficient of `Q` is fixed and nonzero, while its other `e`
coefficients are arbitrary before the split and exactness conditions are
imposed. There are `q^e` choices. Summing the per-cofactor bounds proves
`(FC4)--(FC5)`.

## 3. Scalar cofactor

If `e=0`, the only cofactor is the scalar `c=lc(U)`. The recursion fixes
exactly `w=h-k` nonleading coefficients of `L`. Conversely, any monic
degree-`h` divisor `L` of `Omega` with that prefix makes

```text
P=U-cL
```

have degree below `k`. At a domain point outside the roots of `L`, the
difference `U-P=cL` is nonzero. Hence the agreement set is exactly the root
set of `L`, proving the bijection `(FC6)`.

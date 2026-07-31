# Proof

Write `s=l^3-l+1`.  The `H8-L,tau=-1` row equations are

```text
l^4+1=0,       b^2-bs+1=0,       c=(b-2)s.        (1)
```

Since `b!=0`, `(1)` gives `s=(b^2+1)/b` and the formula for `c` in
`(KB44C-1)`.  Eliminating `l` from the first two equations gives
`P_4(b)^2`; hence every actual packet satisfies `P_4=0`.  Direct reduction
of the numerator minus denominator in `(KB44O-4)` gives zero, so the
protected forced product is `p_xi=1`.

For this row the cross-product coefficients, after removing their common
nonzero factor, are

```text
Gamma=G=b+c,
Alpha=A=-bc(b-1),
Beta=b^2c(b+c).
```

But `b^2c+1=P_4(b)`, so `Beta=-Gamma` on the row.  This proves
`(KB44C-2)` without dividing by `G`.

Forced type `cD` gives `D=1/c`.  If `a=cE` and `x=DF`, then

```text
sigma DE=sigma a/c^2,       EF=ax,
```

which is `(KB44C-3)`.  Product injectivity protects every denominator and
makes its six entries distinct.

Index the fifteen perfect matchings lexicographically as in the verifier.
The parent theorem deletes indices `0,1,2`.  Simultaneously changing the
signs of `x` and `ax` pairs the remaining indices as

```text
(3,6),(4,8),(5,7),(9,13),(10,12),(11,14).         (2)
```

It is therefore enough to treat the six representatives in `(KB44C-4)`.

For a representative with pairs `(i_j,k_j)`, let `E_j(a,x,b)` be the
numerator obtained by substituting the corresponding entries of
`V_sigma` into `(KB44C-2)`.  Define

```text
R_12=Res_x(E_1,E_2),       R_13=Res_x(E_1,E_3),
O=Res_a(R_12,R_13).                                (3)
```

Any common solution of the three pair equations makes `O(b)=0`.  Exact
factorization of `O`, followed factor-by-factor by `Res_b(P_4,f)`, gives
only units and norms with the prime supports `(KB44C-4)`.  The primary
verifier reconstructs every factor and norm.  The audit uses the independent
chain sharing `E_2` instead of `E_1`; all its factor norms are again nonzero.

The deployed prime has nonzero residue modulo every prime in `(KB44C-4)`.
Thus `(3)` cannot vanish at a root of `P_4`, so none of the twelve mixed
matchings exists.  Together with indices `0,1,2`, this exhausts all fifteen
matchings in both signs and proves both cell exclusions. QED.

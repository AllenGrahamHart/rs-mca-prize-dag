# Proof

For every coordinate and slope,

```text
r_0+gamma(r_1-b)=c_gamma-gamma b
```

is equivalent to `r_0+gamma r_1=c_gamma`.  Hence exact and maximal agreement
supports are unchanged.  If `(p_0,p_1)` explains `(r_0,r_1)` on a support,
then `(p_0,p_1-b)` explains `(r_0,r_1-b)` there, and adding `b` gives the
inverse map.  Pair containment and noncontainment are therefore equivalent.

Fix an anchor slope `gamma_0`.  The transformed difference vectors are

```text
(c_gamma-c_gamma0)-(gamma-gamma_0)b.
```

Their span lies in the original difference span plus `<b>`, and the original
differences lie in the transformed difference span plus `<b>`.  This proves
`(G2)`.

Apply the support-wise affine-span theorem to the transformed family in the
ambient shortened row.  Here `n=R+K`, `m=d+K`, the code dimension is `K`,
the excess agreement is `d`, and the explanation affine dimension is `r`.
Substitution gives `(G3)`.

For fixed `r`, only the first term of `(G3)` depends on `K`.  If that term is
`T_K`, then

```text
T_(K+1)/T_K
 = ((R+K+1)/(R+K-r))*((d+K)/(d+K+1)).
```

The sign of `T_(K+1)-T_K` is the sign of

```text
rK+(r+1)d-R+r,
```

so the sequence decreases and then increases, with no second local turn.
The fixed second term is its complete-code endpoint at `K=r`.  Exact integer
evaluation at the contract's adjacent ambient dimensions therefore proves
every displayed interval, including the full ambient cap for the low ranks.

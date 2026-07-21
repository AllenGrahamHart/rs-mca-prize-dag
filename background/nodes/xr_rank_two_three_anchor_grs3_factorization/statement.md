# XR three-anchor rank-two dual-GRS3 factorization

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_rank_two_fundamental_circuit_owner`,
  `xr_higher_rank_uniform_split_pencil_reduction`

Use the uniform rank-two split-pencil setup on active coordinate union `X`,
and suppose the Segre coefficient matrix has rank `q=3`. Put

```text
d=|X|-a-1.
```

There are independent polynomials `P,Q` of degree at most `d` and nonzero
scalars `s_i` such that, after the fixed dual-GRS normalization,

```text
lambda_i(x)=s_i(P(x)+gamma_i Q(x))/Lambda'_X(x).     (TG1)
```

The two trade equations are equivalent to the three exact slope moments

```text
sum_i s_i=sum_i s_i gamma_i=sum_i s_i gamma_i^2=0.  (TG2)
```

Let

```text
L_Gamma(T)=product_i(T-gamma_i).
```

There is a unique polynomial `H` with `deg H<t-3` such that

```text
s_i=H(gamma_i)/L'_Gamma(gamma_i),
H(gamma_i)!=0 for every i.                           (TG3)
```

Thus the scalar ledger is exactly one full-support word of the dual
`GRS_3` code on the active slopes. Conversely, `(TG1)` and `(TG2)` imply
both trade equations whenever the displayed rows lie in the permitted dual
block codes.

The canonical fundamental owner also has an explicit formula. If
`C=B union {e}` is its four-block support and

```text
L_C(T)=product_(j in C)(T-gamma_j),
```

then its normalization `kappa^e_e=1` is

```text
kappa^e_i = s_e L'_C(gamma_e)/(s_i L'_C(gamma_i))
             for i in C,                             (TG4)
kappa^e_i = 0                                        for i notin C.
```

For `t=4`, `H` is a nonzero constant and `(TG3)` is the usual Plucker
barycentric relation. For larger support shells, `(TG1)--(TG4)` is a genuine
global three-anchor factorization, not part of the minimum-face quotient.
The theorem does not count choices of `X,P,Q,H`, prove that abstract choices
embed in selected agreement blocks, choose the first Maxwell core, or pay
the cross-core slope aggregate.

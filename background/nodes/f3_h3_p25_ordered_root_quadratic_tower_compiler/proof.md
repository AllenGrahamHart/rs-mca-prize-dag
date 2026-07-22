# Proof

Suppose `t!=0,1` and `P(t)>=q`. Choose `q` distinct first coordinates
`x_i` from ordered representations. Put `z_i=x_i^(-1)` and

```text
A_(i,0)=1-x_i,       B_(i,0)=1-t/x_i.
```

Both values lie in the order-`n` subgroup, so their `s` repeated squares end
at one. The Vandermonde product of the distinct `x_i` is nonzero and has an
inverse. This supplies a solution of `(ORT1)--(ORT2)` and the prefix-product
equations.

Conversely, the inverse selectors give `T!=0,1`, every `x_i!=0`, and pairwise
distinctness. The terminal tower equations give

```text
1-x_i in mu_n,       1-T/x_i in mu_n.
```

All `n`th roots lie in `F_p`. Hence `x_i` and `T/x_i` are nonzero shifted
subgroup elements, and each `i` gives an ordered representation of `T`.
Distinct `x_i` give distinct records, so `P(T)>=q`. As in the divisor-tower
proof, one record already forces a geometric `T` into `F_p`.

For the size count, each root contributes `x_i,z_i`, one initial `B` value,
`s-1` internal `A` values, and `s-1` further `B` values: `2s+1` variables.
The three global scalar variables and `M` prefix/inverse variables give

```text
q(2s+1)+3+M=2qs+q+M+3.
```

Each root contributes two inverse/initialization equations and `2s` tower
equations, for `2s+2`. The two global selector equations and `M`
prefix/inverse equations give

```text
q(2s+2)+2+M=2qs+2q+M+2.
```

Every equation is linear or quadratic. Characteristic-zero shifted-product
Sidonicity forbids `q=25` distinct records, so the system is empty there.
QED.

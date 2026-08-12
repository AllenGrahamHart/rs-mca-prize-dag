# Proof

Choose a basis `c_1,...,c_s` of `C'`, write

```text
c_gamma=c_0+sum_i lambda_(gamma,i)c_i,
```

and associate the parameter point
`p_gamma=(gamma,lambda_(gamma,1),...,lambda_(gamma,s))`. Agreement at a
coordinate `x` is an affine hyperplane with normal

```text
v_x=(r_1(x),-c_1(x),...,-c_s(x)).
```

The only place where the upstream affine-span theorem uses global direction
separation is to prove that the normals incident with each `p_gamma` span
`F^(s+1)`. Pair noncontainment proves the same fact locally.

Indeed, if those normals do not span, a nonzero relation `(delta,mu)` gives

```text
delta r_1 - sum_i mu_i c_i = 0
```

on all `m` points of `S_gamma`. If `delta=0`, a nonzero degree-`<K`
codeword has at least `m=K+w>K` roots, impossible. If `delta!=0`, then `r_1`
agrees on `S_gamma` with the codeword

```text
b=delta^(-1) sum_i mu_i c_i.
```

Since `r_gamma` agrees there with `c_gamma`, the base word `r_0` agrees on
the same support with `c_gamma-gamma b`. Thus `(c_gamma-gamma b,b)` is a
simultaneous code explanation of the received pair on `S_gamma`, contrary
to the hypothesis. The incident normals therefore have full rank.

The remainder of the upstream incidence proof is unchanged. Zero normals
and normals in each proper `r`-space are bounded by Reed-Solomon root counts.
Counting ordered bases incident with each parameter point gives

```text
|Z| <= (n-g-c)^(falling s+1) /
       ((m-g)(w+c)^(rising s))
```

for the same endpoint parameters `g,c`. The endpoint monotonicity gives the
two displayed terms in the statement.

For the whole-line shortened code, take the affine space to be the complete
dimension-`s` code. Then `K=s`, `n=R+s`, `m=d+s`, and both terms equal

```text
J_s=floor(product_(i=0..s)(R+i)/(d+i)).
```

Exact substitution gives the two deployed boundaries in the certificate.
In the `GF(11)` hostile control, global cancellation gives `(9,4,6)` and the
direction itself has six agreements with a codeword, so the old hypothesis
fails. Nevertheless every selected witness has incident-normal rank five,
and the strengthened theorem gives `7<=J_4=21`.

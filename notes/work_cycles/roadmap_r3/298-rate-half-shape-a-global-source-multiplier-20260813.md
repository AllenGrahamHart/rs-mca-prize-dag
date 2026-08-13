# Cycle 298: rate-half Shape-A global source-multiplier normal form

The three center residue kernels now form one exact Padé intersection in
the full source algebra. In an affine parameter coordinate, write

```text
B_src(z,X)=J(X)z+K(X),       varphi=-K/J mod L_U0.
```

On `M_gamma`, `J(x)=eta_xL_U0'(x)` is nonzero and
`varphi(x)=gamma`. Therefore

```text
E_3=W_X direct_sum varphi W_X direct_sum varphi^2 W_X,
dim E_3=3r,
K_cap=S_n intersect J E_3^perp.
```

At the current lower rank boundary,

```text
dim E_3=n+5=274877906946,
dim E_3^perp=2n+2=549755813884,
required dim K_cap>=e-3=183251937960.
```

The direct-sum claim is exact: a relation restricts on each class to a
degree-`n` polynomial with at least `n+2` roots, and the three center
values then invert by Vandermonde. The resulting large intersection is a
necessary owner-sensitive alignment, not a generic-dimension
contradiction.

```text
new node:               PROVED
critical status effect: none
compute:                local constant-size only
next exact target:      bound S_n intersect J E_3^perp using the fixed
                        factor, split rows, or Hankel/source-Gram identities
```

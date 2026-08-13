# Proof

Anchor at `gamma_0` and write

```text
a_gamma=gamma-gamma_0,       u_gamma=c_gamma-c_gamma0.
```

The projection `pi_C:V->U` is surjective and `dim U=K`, while `V` lies in
the `(K+1)`-dimensional space `F direct_sum C`.  Hence `dim V` is `K` or
`K+1`.

## Lifted rank K

If `dim V=K`, then `pi_C` is an isomorphism.  There is a unique linear
functional `ell:C->F` such that

```text
V={(ell(u),u):u in C}.
```

The slopes are not all equal, so `ell` is nonzero.  Choose any `b in C`
with `ell(b)=1`.  On difference vectors, the gauge acts by

```text
T_b(a,u)=u-a b.
```

Its kernel on `V` is exactly the line spanned by `(1,b)`.  Therefore
`T_b(V)=ker ell` has dimension `K-1`, which is the transformed explanation
affine rank.  Conversely, a gauge drops rank only if `(1,b) in V`, exactly
when `ell(b)=1`.

## Lifted rank K+1

If `dim V=K+1`, then `V=F direct_sum C`.  For every `b in C`, the map
`T_b` is surjective onto `C`, so the transformed explanation affine rank is
exactly `K`.  No codeword gauge drops it.

## Error rank

The selected error differences are the image of `V` under

```text
Phi(a,u)=a r_1-u.
```

This map is injective.  A nonzero kernel vector would have `a!=0` and imply
`r_1=a^(-1)u in C`; the case `a=0` forces `u=0`.  But `r_1 in C` contradicts
pair noncontainment on every selected support: `r_1` itself explains the
direction and `c_gamma-gamma r_1` explains the base there.  Thus the error
affine rank is `dim V`.

Gauge equivalence preserves supports and pair noncontainment, and direction
coset distance is invariant under subtracting a codeword.  In the
gauge-drop branch the corrected occupancy compiler can therefore be applied
at rank `K-1`.  Its already certified penultimate-rank walls give the two
displayed deployed consequences.

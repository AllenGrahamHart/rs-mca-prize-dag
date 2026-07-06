# proof: e22_common_tail_invariance_certificate_soundness

Let the certificate provide a tail `B`, local moduli `M_i`, and touched-petal
sets `T_i`.

The first certificate predicate says that the same set `B` is used for every
touched petal. The second says each `M_i` is dyadic and satisfies `M_i>t`. The
third gives

```text
|B| < min_i M_i.
```

The fourth predicate verifies, for each touched petal, that `T_i \ B` is
invariant under multiplication by the kernel

```text
K_{M_i} = {eta : eta^{M_i}=1}
```

of `x -> x^{M_i}`.

These are exactly the data asserted by
`e22_cofactor_common_tail_kernel_invariance`: one bounded common tail, dyadic
local moduli above the reserve threshold, and kernel invariance for every
non-tail set. Therefore a verified certificate of this form proves the node.

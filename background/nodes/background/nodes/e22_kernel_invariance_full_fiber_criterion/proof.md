# proof: e22_kernel_invariance_full_fiber_criterion

The fibers of

```text
pi_M(x)=x^M
```

are exactly the cosets of the kernel

```text
K_M = {eta : eta^M=1}.
```

Indeed, if `y=x eta` with `eta in K_M`, then

```text
y^M = x^M eta^M = x^M.
```

Conversely, if `y^M=x^M`, then `(y/x)^M=1`, so `y/x in K_M` and
`y=x eta` for some `eta in K_M`.

If `S` is a union of full fibers, then it is a union of `K_M`-cosets, hence
is invariant under multiplying by any element of `K_M`.

If `S` is invariant under `K_M` and `x in S`, then the whole coset
`xK_M`, which is the fiber of `pi_M` through `x`, is contained in `S`.
Therefore `S` is the union of the full fibers through its points.

This proves the criterion.

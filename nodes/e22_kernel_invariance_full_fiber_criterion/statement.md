# e22_kernel_invariance_full_fiber_criterion

- **status:** PROVED
- **closure:** proof

## Statement

Let `D` be the cyclic multiplicative subgroup domain and let `M` divide
`|D|`. Let

```text
pi_M(x) = x^M,
K_M = {eta in D : eta^M = 1}.
```

For a subset `S subset D`, the following are equivalent:

1. `S` is a union of full fibers of `pi_M`;
2. `S` is invariant under multiplication by `K_M`, i.e.

   ```text
   x in S, eta in K_M  =>  x eta in S.
   ```

Thus proving kernel invariance after deleting a tail is enough to prove local
full quotient-fiber structure.

## Falsifier

A subset invariant under `K_M` that is not a union of `pi_M` fibers, or a
union of `pi_M` fibers that is not `K_M`-invariant.

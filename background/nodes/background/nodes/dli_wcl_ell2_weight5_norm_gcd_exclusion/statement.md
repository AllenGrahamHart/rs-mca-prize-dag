# DLI ell-two weight-five norm-gcd exclusion

- **status:** PROVED
- **closure:** exact computation
- **dependencies:** `dli_wcl_ell2_weight5_pair_quadratic_router` and
  `dli_wcl_ell2_weight5_pair_ideal_index_obstruction`

Let `q<2^256` be an official production characteristic with
`v_2(q-1)>=41`, and let `omega` have exact order `1024` in `F_q`. There is no
reduced signed polynomial `P` of weight five such that

```text
P(omega)=P(omega^3)=0.
```

Equivalently, the residual weak-column slot `(ell,w)=(2,5)` is empty on every
official row.

The exact certificate covers all `1,514` odd-dilation orbits of legal pairs in
the pair-quadratic router. For each pair it computes the two cleared
cyclotomic norms and their gcd. The `507` distinct nontrivial gcds factor over
`168` certified primes, with

```text
max v_2(p-1) = 18 < 41.
```


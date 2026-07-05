# dli_log_integral_equidistribution

- **status:** CONDITIONAL
- **closure:** proof

## Statement

For every central profile and every nonzero frequency, the odd low-degree
evaluations on the square-root section satisfy the near-circle log-integral
geometric-mean bound

```text
-sum_y log |mu_hat_y(P_lambda(sigma(y)))|^2
    >= 2(L_j - eps_j) log q - O(1)
```

with `sum_j eps_j = o(t)`.

## Falsifier

A profile/frequency pair whose Dirichlet factors stay near peaks often enough
that the total loss is linear in `t`.

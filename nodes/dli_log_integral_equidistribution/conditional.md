# conditional: dli_log_integral_equidistribution

## Predicate nodes

- `dli_circle_log_integral_constant`
- `dli_odd_evaluation_discrepancy`

## Claim

Conditional on odd-evaluation discrepancy, the DLI log-integral
equidistribution estimate follows from the proved circle constant.

## Proof

The proved constant node evaluates the model circle average:

```text
int_0^1 log |cos(2 pi x)|^2 dx = -2 log 2.
```

The discrepancy predicate supplies the missing sampling statement: for every
central profile and every nonzero frequency, the odd low-degree evaluations on
the square-root section avoid Dirichlet peaks with total error
`sum_j eps_j = o(t)`.

Applying that discrepancy statement to the logarithmic Dirichlet kernel and
using the proved circle constant gives the geometric-mean inequality

```text
-sum_y log |mu_hat_y(P_lambda(sigma(y)))|^2
    >= 2(L_j - eps_j) log q - O(1).
```

Thus this node has no independent analytic content beyond the discrepancy
predicate and the already proved constant. The remaining DLI leaf is
`dli_odd_evaluation_discrepancy`.

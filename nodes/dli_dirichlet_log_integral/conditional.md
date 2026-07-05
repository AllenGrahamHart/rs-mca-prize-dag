# conditional: dli_dirichlet_log_integral

## Predicate node

- `dli_log_integral_equidistribution`

## Claim

Conditional on the log-integral equidistribution predicate, DLI holds and
therefore supplies the Fourier-moment input consumed by `ejm_joint_moment`.

## Proof

The predicate `dli_log_integral_equidistribution` is the uniform statement that
for every central profile and nonzero frequency, the odd low-degree
evaluations on the square-root section sample the circle with enough
geometric-mean control that

```text
-sum_y log |mu_hat_y(P_lambda(sigma(y)))|^2
    >= 2(L_j - eps_j) log q - O(1)
```

with `sum_j eps_j = o(t)`.

This is exactly the DLI inequality stated in this node. The already banked D4
reduction in `ejm_joint_moment/conditional.md` then turns DLI into the
`EJM_2` Fourier-moment bound with `eta_j <= eps_j + O(1)`.
